import cv2, numpy as np, json
S=np.load('small.npy'); sh=np.load('shift.npy'); C=np.cumsum(sh,0)
M=json.load(open('match.json')); N=len(S)
anchors={}
for i,(s,b) in enumerate(M):
    if s>=0.8: x,y,w,h=b; anchors[i]=(x+w/2,y+h/2,w,h)
anchors[int(34.5*30)]=(272,722,160,38)   # manual (plate separuh di bawah)
ak=np.array(sorted(anchors))
pos=[None]*N
for i in range(N):
    j=ak[np.argmin(abs(ak-i))]
    if abs(j-i)>int(4.6*30): continue
    cx,cy,w,h=anchors[j]; d=C[i]-C[j]
    pos[i]=(cx+d[0],cy+d[1],w,h)
json.dump(pos,open('pos.json','w'))
def draw(t):
    i=int(t*30); g=cv2.cvtColor(S[i],cv2.COLOR_GRAY2BGR)
    if pos[i]:
        cx,cy,w,h=pos[i]; W,H=w*1.7,h*2.6
        cv2.rectangle(g,(int(cx-W/2),int(cy-H/2)),(int(cx+W/2),int(cy+H/2)),(0,0,255),3)
    cv2.putText(g,f"{t}",(10,40),0,1.2,(0,255,255),3)
    return cv2.resize(g,(270,480))
ts=[1.5,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5, 23.5,24.0,24.5,25.0,25.5,26.0,26.5,32.5,33.0,33.5, 34.0,34.5,35.0,35.5,36.0,36.5,37.0,27.0,28.0,30.0]
rows=[np.hstack([draw(t) for t in ts[k:k+10]]) for k in range(0,30,10)]
cv2.imwrite('check.jpg',np.vstack(rows))
