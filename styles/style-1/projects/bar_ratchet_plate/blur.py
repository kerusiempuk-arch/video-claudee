import cv2, numpy as np, json, subprocess
W,H=1080,1920
pos=json.load(open('pos.json'))
src='../raw.mp4'; out='../raw_noplate.mp4'
p=subprocess.Popen(['ffmpeg','-v','error','-i',src,'-f','rawvideo','-pix_fmt','bgr24','-'],stdout=subprocess.PIPE)
q=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r','30','-i','-','-i',src,
  '-map','0:v','-map','1:a','-c:v','libx264','-crf','14','-preset','medium','-pix_fmt','yuv420p','-c:a','copy','-shortest',out],stdin=subprocess.PIPE)
i=0
while True:
    b=p.stdout.read(W*H*3)
    if len(b)<W*H*3: break
    f=np.frombuffer(b,np.uint8).reshape(H,W,3).copy()
    if i<len(pos) and pos[i]:
        cx,cy,w,h=[v*2 for v in pos[i]]
        bw,bh=w*1.7,h*3.0; cy+=0.2*h
        x0,x1=int(max(0,cx-bw/2)),int(min(W,cx+bw/2)); y0,y1=int(max(0,cy-bh/2)),int(min(H,cy+bh/2))
        if x1-x0>8 and y1-y0>8:
            r=f[y0:y1,x0:x1]
            sm=cv2.resize(r,(max(1,(x1-x0)//28),max(1,(y1-y0)//28)),interpolation=cv2.INTER_AREA)
            pix=cv2.GaussianBlur(cv2.resize(sm,(x1-x0,y1-y0),interpolation=cv2.INTER_LINEAR),(0,0),12)
            m=np.zeros((y1-y0,x1-x0),np.float32); pad=10
            m[pad:-pad,pad:-pad]=1; m=cv2.GaussianBlur(m,(0,0),5)[...,None]
            f[y0:y1,x0:x1]=(pix*m+r*(1-m)).astype(np.uint8)
    q.stdin.write(f.tobytes()); i+=1
q.stdin.close(); q.wait(); print(i)
