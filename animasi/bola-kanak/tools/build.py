"""Jana index.html + compositions/*.html untuk animasi "Gol Pertama Adik".
Watak dilukis SVG, dianimasi GSAP. Jalankan: python3 tools/build.py
"""
import os, json

ROOT = os.path.join(os.path.dirname(__file__), "..")
W, H = 1080, 1920
INK = "#2B1D14"

# ---------------------------------------------------------------- watak
KIDS = {
    "abang": dict(jersey="#E63B2E", shorts="#1F3B73", skin="#C98A5E", hair="#1E1410", num="10", hair_style="spike"),
    "kawan": dict(jersey="#2E9E4F", shorts="#F4F1E8", skin="#8C5A3C", hair="#120C08", num="7", hair_style="round"),
    "adik":  dict(jersey="#FFC928", shorts="#2F6FD6", skin="#D9A074", hair="#2A1A10", num="3", hair_style="tuft"),
}


def kid_svg(pid, key, extra_mud=False, flip=False):
    c = KIDS[key]
    i = f"{pid}-{key}"
    sw = 6
    hair = {
        "spike": f'<path d="M-62 -310 Q-70 -372 -20 -372 L-8 -392 L6 -370 L26 -390 L34 -366 Q70 -360 62 -308 Q40 -338 0 -338 Q-40 -338 -62 -310Z" fill="{c["hair"]}" stroke="{INK}" stroke-width="{sw}" stroke-linejoin="round"/>',
        "round": f'<path d="M-64 -300 Q-70 -370 0 -372 Q70 -370 64 -300 Q50 -335 0 -336 Q-50 -335 -64 -300Z" fill="{c["hair"]}" stroke="{INK}" stroke-width="{sw}" stroke-linejoin="round"/>',
        "tuft":  f'<path d="M-62 -306 Q-66 -366 0 -366 Q66 -366 62 -306 Q44 -332 0 -332 Q-44 -332 -62 -306Z M-4 -364 Q4 -400 26 -398 Q10 -386 12 -364Z" fill="{c["hair"]}" stroke="{INK}" stroke-width="{sw}" stroke-linejoin="round"/>',
    }[c["hair_style"]]
    head_scale = 1.22 if key == "adik" else 1.0
    mud = ""
    if extra_mud:
        mud = (f'<g id="{i}-mud" opacity="0">'
               f'<ellipse cx="-20" cy="-150" rx="26" ry="16" fill="#6B4A2B"/><ellipse cx="22" cy="-190" rx="16" ry="11" fill="#6B4A2B"/>'
               f'<ellipse cx="-30" cy="-60" rx="14" ry="10" fill="#6B4A2B"/><ellipse cx="18" cy="-282" rx="10" ry="7" fill="#6B4A2B"/></g>')

    def leg(side, x):
        return (f'<g id="{i}-leg{side}">'
                f'<rect x="{x-13}" y="-128" width="26" height="112" rx="13" fill="{c["skin"]}" stroke="{INK}" stroke-width="{sw}"/>'
                f'<rect x="{x-14}" y="-52" width="28" height="34" rx="6" fill="#FFFFFF" stroke="{INK}" stroke-width="{sw}"/>'
                f'<path d="M{x-18} -18 Q{x-18} -36 {x} -36 Q{x+34} -34 {x+36} -10 L{x+36} -2 L{x-18} -2Z" fill="#20242B" stroke="{INK}" stroke-width="{sw}" stroke-linejoin="round"/></g>')

    def arm(side, x):
        return (f'<g id="{i}-arm{side}">'
                f'<rect x="{x-12}" y="-226" width="24" height="96" rx="12" fill="{c["skin"]}" stroke="{INK}" stroke-width="{sw}"/>'
                f'<rect x="{x-17}" y="-230" width="34" height="40" rx="14" fill="{c["jersey"]}" stroke="{INK}" stroke-width="{sw}"/>'
                f'<circle cx="{x}" cy="-128" r="16" fill="{c["skin"]}" stroke="{INK}" stroke-width="{sw}"/></g>')

    return f'''<g id="{i}" class="kid">
  <ellipse id="{i}-shadow" cx="6" cy="2" rx="78" ry="14" fill="#000" opacity="0.18"/>
  <g id="{i}-body">
    {leg("L", -24)}
    {leg("R", 24)}
    {arm("L", -54)}
    <rect x="-46" y="-150" width="92" height="44" rx="12" fill="{c["shorts"]}" stroke="{INK}" stroke-width="{sw}"/>
    <path d="M-48 -205 Q-48 -238 -18 -238 L18 -238 Q48 -238 48 -205 L46 -132 Q0 -124 -46 -132Z" fill="{c["jersey"]}" stroke="{INK}" stroke-width="{sw}" stroke-linejoin="round"/>
    <text x="0" y="-160" transform="{'scale(-1,1)' if flip else ''}" text-anchor="middle" font-family="Nunito" font-weight="900" font-size="44" fill="#FFFFFF" stroke="{INK}" stroke-width="3" paint-order="stroke">{c["num"]}</text>
    {mud}
    <g id="{i}-head"><g transform="translate(0,-236) scale({head_scale}) translate(0,236)">
      <circle cx="-62" cy="-292" r="13" fill="{c["skin"]}" stroke="{INK}" stroke-width="{sw}"/>
      <circle cx="62" cy="-292" r="13" fill="{c["skin"]}" stroke="{INK}" stroke-width="{sw}"/>
      <circle cx="0" cy="-298" r="62" fill="{c["skin"]}" stroke="{INK}" stroke-width="{sw}"/>
      {hair}
      <circle cx="-36" cy="-276" r="10" fill="#FF7A7A" opacity="0.45"/>
      <circle cx="36" cy="-276" r="10" fill="#FF7A7A" opacity="0.45"/>
      <g id="{i}-eyes">
        <ellipse cx="-22" cy="-302" rx="13" ry="16" fill="#FFF" stroke="{INK}" stroke-width="4"/>
        <ellipse cx="22" cy="-302" rx="13" ry="16" fill="#FFF" stroke="{INK}" stroke-width="4"/>
        <g id="{i}-pupils"><circle cx="-20" cy="-300" r="7" fill="{INK}"/><circle cx="24" cy="-300" r="7" fill="{INK}"/>
          <circle cx="-17" cy="-303" r="2.4" fill="#FFF"/><circle cx="27" cy="-303" r="2.4" fill="#FFF"/></g>
      </g>
      <g id="{i}-brows"><path d="M-34 -326 Q-22 -332 -10 -326" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
        <path d="M10 -326 Q22 -332 34 -326" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/></g>
      <path id="{i}-m-smile" d="M-18 -268 Q0 -252 18 -268" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
      <ellipse id="{i}-m-o" cx="0" cy="-262" rx="10" ry="13" fill="#5A1E1E" stroke="{INK}" stroke-width="4" opacity="0"/>
      <path id="{i}-m-sad" d="M-16 -256 Q0 -272 16 -256" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round" opacity="0"/>
      <path id="{i}-m-grin" d="M-24 -272 Q0 -270 24 -272 Q20 -244 0 -244 Q-20 -244 -24 -272Z" fill="#5A1E1E" stroke="{INK}" stroke-width="4" stroke-linejoin="round" opacity="0"/>
    </g></g>
    {arm("R", 54)}
  </g>
</g>'''


def ball_svg(i):
    return f'''<g id="{i}"><g id="{i}-spin">
  <circle cx="0" cy="0" r="30" fill="#FFFFFF" stroke="{INK}" stroke-width="5"/>
  <path d="M0 -11 L10 -4 L7 9 L-7 9 L-10 -4Z" fill="{INK}"/>
  <path d="M0 -30 L0 -11 M10 -4 L26 -12 M7 9 L17 24 M-7 9 L-17 24 M-10 -4 L-26 -12" stroke="{INK}" stroke-width="3"/>
  <path d="M-8 -29 L8 -29 L4 -22 L-4 -22Z M24 -18 L29 -6 L22 -4Z M-24 -18 L-29 -6 L-22 -4Z M12 26 L20 20 L22 27Z M-12 26 L-20 20 L-22 27Z" fill="{INK}"/>
</g></g>'''


# ------------------------------------------------------------ rig (JS)
RIG = r"""
const ORG = {legL:"-24 -126", legR:"24 -126", armL:"-54 -222", armR:"54 -222", head:"0 -238", body:"0 0", eyes:"0 -302"};
function rig(tl, id){ for (const [p,o] of Object.entries(ORG)) tl.set(`#${id}-${p}`, {svgOrigin:o}, 0); }
function place(tl, id, x, y, s=1, flip=false){ tl.set(`#${id}`, {svgOrigin:"0 0", x, y, scaleX: flip?-s:s, scaleY:s}, 0); }
function pose(tl, id, t, o, dur=0.25, ease="power2.out"){
  // tangan: nilai negatif = angkat ke luar/atas (arah dinormalkan)
  for (const [p,v] of Object.entries(o)) tl.to(`#${id}-${p}`, {rotation: p.startsWith("arm") ? -v : v, duration:dur, ease}, t);
}
const MOUTHS = ["smile","o","sad","grin"];
function mouth(tl, id, t, m){ for (const k of MOUTHS) tl.set(`#${id}-m-${k}`, {opacity: k===m?1:0}, t); }
function look(tl, id, t, dx, dy, dur=0.15){ tl.to(`#${id}-pupils`, {x:dx, y:dy, duration:dur, ease:"power2.out"}, t); }
function blink(tl, id, t){ tl.to(`#${id}-eyes`, {scaleY:0.08, duration:0.05, ease:"none"}, t).to(`#${id}-eyes`, {scaleY:1, duration:0.08, ease:"power1.out"}, t+0.06); }
function brows(tl, id, t, y, rot=0){ tl.to(`#${id}-brows`, {y, duration:0.15, ease:"power2.out"}, t); }
// lari: kaki & tangan berselang, badan melantun; offset tangan 1 frame selepas kaki
function run(tl, id, t0, t1, x1, step=0.14, amp=34, y1=null){
  const mv = {x:x1, duration:t1-t0, ease:"power1.inOut"}; if (y1!==null) mv.y = y1;
  tl.to(`#${id}`, mv, t0);
  let k=0;
  for (let t=t0; t<t1-0.01; t+=step, k++){
    const s = k%2?1:-1, a = amp*(0.85+0.15*((k*7)%3)/2);
    tl.to(`#${id}-legL`, {rotation: s*a, duration:step, ease:"sine.inOut"}, t);
    tl.to(`#${id}-legR`, {rotation:-s*a, duration:step, ease:"sine.inOut"}, t);
    tl.to(`#${id}-armL`, {rotation:-s*a*1.1, duration:step, ease:"sine.inOut"}, t+0.03);
    tl.to(`#${id}-armR`, {rotation: s*a*0.9, duration:step, ease:"sine.inOut"}, t+0.03);
    tl.to(`#${id}-body`, {y:-14, duration:step/2, ease:"power1.out"}, t);
    tl.to(`#${id}-body`, {y:0, duration:step/2, ease:"power1.in"}, t+step/2);
  }
  pose(tl, id, t1, {legL:0, legR:0, armL:0, armR:0}, 0.18);
}
// ketawa: badan bergegar kecil
function laugh(tl, id, t0, t1, amt=8){
  mouth(tl, id, t0, "grin");
  let k=0; for (let t=t0; t<t1-0.01; t+=0.12, k++){
    tl.to(`#${id}-body`, {y: k%2? 0 : -amt*(1+(k%3)*0.2), duration:0.12, ease:"sine.inOut"}, t);
  }
  tl.to(`#${id}-body`, {y:0, duration:0.1}, t1);
}
// nafas idle (lakonan watak)
function breathe(tl, id, t0, t1, amt=0.015, per=1.4){
  let k=0; for (let t=t0; t<t1-0.01; t+=per/2, k++){
    tl.to(`#${id}-body`, {scaleY: k%2?1:1+amt, duration:per/2, ease:"sine.inOut", svgOrigin:"0 0"}, t);
  }
}
function arcTo(tl, sel, t, x, y, peak, dur, ease="none"){
  // lontaran: x linear, y naik-turun (dua separuh)
  tl.to(sel, {x, duration:dur, ease:"none"}, t);
  tl.to(sel, {y:peak, duration:dur/2, ease:"power2.out"}, t);
  tl.to(sel, {y, duration:dur/2, ease:"power2.in"}, t+dur/2);
}
"""

# ------------------------------------------------------------ latar
def sky(i, top, bot, sun=True):
    s = f'<linearGradient id="{i}-g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{top}"/><stop offset="1" stop-color="{bot}"/></linearGradient>'
    sunsvg = f'<circle id="{i}-sun" cx="820" cy="420" r="110" fill="#FFF2B8"/><circle cx="820" cy="420" r="150" fill="#FFF2B8" opacity="0.25"/>' if sun else ""
    return f'<defs>{s}</defs><rect id="{i}" x="-400" y="-1400" width="1880" height="4000" fill="url(#{i}-g)"/>{sunsvg}'


def hills(y=1060, dark=False):
    a, b = ("#5E8F4A", "#4C7A3C") if dark else ("#8CC46A", "#73B157")
    return f'''<path d="M-400 {y} Q-100 {y-170} 200 {y-60} Q420 {y-200} 700 {y-80} Q920 {y-180} 1480 {y-40} L1480 {y+40} L-400 {y+40}Z" fill="{a}"/>
<path d="M-400 {y} Q0 {y-90} 360 {y-20} Q700 {y-120} 1100 {y-30} Q1300 {y-70} 1480 {y} L1480 {y+40} L-400 {y+40}Z" fill="{b}"/>'''


def palm(x, y, s=1, col="#3E6B34"):
    return f'''<g transform="translate({x},{y}) scale({s})">
<path d="M0 0 Q8 -130 -6 -260" fill="none" stroke="#6B4A2B" stroke-width="14" stroke-linecap="round"/>
<g fill="{col}"><path d="M-6 -260 Q-80 -300 -140 -240 Q-70 -270 -6 -255Z"/><path d="M-6 -260 Q60 -310 140 -250 Q60 -272 -6 -255Z"/>
<path d="M-6 -260 Q-40 -330 -100 -330 Q-40 -300 -6 -258Z"/><path d="M-6 -260 Q40 -340 100 -320 Q40 -300 -6 -258Z"/></g></g>'''


def house(x, y):
    return f'''<g transform="translate({x},{y})">
<rect x="-70" y="-90" width="140" height="90" fill="#C98B4E" stroke="{INK}" stroke-width="4"/>
<path d="M-95 -88 L0 -160 L95 -88Z" fill="#9C3D2E" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>
<rect x="-20" y="-60" width="40" height="60" fill="#6B4A2B"/><rect x="-60" y="-70" width="26" height="24" fill="#FFE7A0"/>
<rect x="-80" y="0" width="8" height="30" fill="#6B4A2B"/><rect x="72" y="0" width="8" height="30" fill="#6B4A2B"/></g>'''


def field(i, y=1060, col="#5DB443", stripe="#53A63B"):
    stripes = "".join(f'<rect x="{-400 + k*260}" y="{y}" width="130" height="1400" fill="{stripe}"/>' for k in range(8))
    return f'<rect id="{i}" x="-400" y="{y}" width="1880" height="1400" fill="{col}"/>{stripes}'


def goal_side(x, y):
    """gol dilihat dari sisi (hujung kanan padang)"""
    net = "".join(f'<line x1="{x}" y1="{y-300+k*30}" x2="{x+150}" y2="{y-260+k*26}" stroke="#FFFFFF" stroke-width="2" opacity="0.6"/>' for k in range(11))
    net += "".join(f'<line x1="{x+k*30}" y1="{y-300+k*8}" x2="{x+k*30}" y2="{y}" stroke="#FFFFFF" stroke-width="2" opacity="0.6"/>' for k in range(6))
    return f'''<g>{net}<rect x="{x-10}" y="{y-310}" width="20" height="310" rx="6" fill="#FFF" stroke="{INK}" stroke-width="4"/>
<path d="M{x} {y-300} L{x+150} {y-260} L{x+150} {y}" fill="none" stroke="#FFF" stroke-width="10" stroke-linejoin="round"/></g>'''


# ------------------------------------------------------------ dokumen
def scene(cid, dur, body, script, css=""):
    return f'''<template>
  <style>
    #root {{ position:absolute; inset:0; overflow:hidden; background:#FFD08A; font-family:"Nunito", sans-serif; }}
    #root .stage {{ position:absolute; left:0; top:0; width:{W}px; height:{H}px; }}
    #root .ttl {{ position:absolute; left:0; width:{W}px; text-align:center; font-weight:900; color:#FFFFFF;
      -webkit-text-stroke: 0; paint-order: stroke fill; text-shadow: 0 8px 0 {INK}, 0 0 0 {INK}; letter-spacing:-0.01em; }}
    {css}
  </style>
  <div id="root" data-composition-id="{cid}" data-width="{W}" data-height="{H}" data-duration="{dur}" data-layout-allow-overflow>
{body}
  </div>
  <script>
{RIG}
    const tl = gsap.timeline({{ paused: true }});
{script}
    window.__timelines["{cid}"] = tl;
  </script>
</template>
'''


def write(path, s):
    with open(os.path.join(ROOT, path), "w") as f:
        f.write(s)


def stage(cid, inner, cam=True):
    return f'''    <div class="stage" id="{cid}-camwrap"><svg id="{cid}-cam" class="stage" viewBox="0 0 {W} {H}" width="{W}" height="{H}" overflow="visible">
{inner}
    </svg></div>'''


TEXT_STYLE = "font-family:Nunito; font-weight:900; fill:#FFFFFF; stroke:" + INK + "; stroke-width:14px; paint-order:stroke; stroke-linejoin:round;"

# ============================================================ S1 padang
S1_DUR = 5.4
s1 = stage("s1", f'''
{sky("s1-sky", "#FF9F5A", "#FFE1A1")}
{hills()}
{palm(120, 1010, 0.9)}{palm(980, 1000, 1.1)}{house(300, 1000)}{palm(560, 1020, 0.6)}
{field("s1-field")}
{goal_side(940, 1290)}
<g id="s1-kids">
{kid_svg("s1", "kawan", flip=True)}
{kid_svg("s1", "adik")}
{kid_svg("s1", "abang")}
{ball_svg("s1-ball")}
</g>
<g id="s1-title">
<text id="s1-t1" x="540" y="470" text-anchor="middle" font-size="118" style="{TEXT_STYLE}">Gol Pertama</text>
<text id="s1-t2" x="540" y="610" text-anchor="middle" font-size="150" style="{TEXT_STYLE} fill:#FFC928;">Adik</text>
</g>''')

s1_js = r"""
    for (const k of ["abang","kawan","adik"]) rig(tl, `s1-${k}`);
    place(tl, "s1-adik", 360, 1420, 1.0);
    place(tl, "s1-kawan", 900, 1350, 1.05, true);
    place(tl, "s1-abang", -260, 1440, 1.25);
    tl.set("#s1-ball", {x:1200, y:1392}, 0);
    look(tl, "s1-adik", 0, 7, 4, 0.01); mouth(tl, "s1-adik", 0, "smile");
    look(tl, "s1-kawan", 0, 7, 2, 0.01);
    breathe(tl, "s1-kawan", 0, 5.4); breathe(tl, "s1-adik", 0, 1.4);
    // bola bergolek ke kaki adik
    tl.to("#s1-ball", {x:470, duration:1.3, ease:"power2.out"}, 0);
    tl.to("#s1-ball-spin", {rotation:-760, svgOrigin:"0 0", duration:1.3, ease:"power2.out"}, 0);
    look(tl, "s1-adik", 0.9, 9, 9);
    mouth(tl, "s1-adik", 1.25, "o"); tl.to("#s1-adik-eyes", {scale:1.18, svgOrigin:"0 -302", duration:0.15, ease:"back.out(2)"}, 1.25);
    mouth(tl, "s1-adik", 1.55, "grin"); tl.to("#s1-adik-eyes", {scale:1, duration:0.2}, 1.6);
    // tajuk keluar
    tl.to("#s1-title", {opacity:0, duration:0.2, ease:"power2.in"}, 1.6);
    // adik ambil ancang-ancang
    tl.to("#s1-adik-body", {scaleY:0.93, svgOrigin:"0 0", duration:0.2, ease:"power2.out"}, 1.55);
    pose(tl, "s1-adik", 1.6, {legR:38, armL:-30, armR:30}, 0.3);
    // abang meluru masuk, curi bola
    run(tl, "s1-abang", 1.55, 2.35, 760, 0.12, 40);
    tl.to("#s1-ball", {x:820, duration:0.45, ease:"power2.out"}, 2.05);
    tl.to("#s1-ball-spin", {rotation:-1500, duration:0.45, ease:"power2.out"}, 2.05);
    // sepakan adik terlepas -> pusing, jatuh terduduk
    pose(tl, "s1-adik", 2.1, {legR:-85, armL:40, armR:-50}, 0.12, "power3.in");
    tl.to("#s1-adik-body", {scaleY:1, duration:0.1}, 2.1);
    tl.to("#s1-adik-body", {rotation:-18, y:40, duration:0.22, ease:"power2.in"}, 2.25);
    pose(tl, "s1-adik", 2.25, {legL:-70, legR:-80, armL:60, armR:-30}, 0.22, "power2.in");
    tl.to("#s1-adik-body", {rotation:-10, y:46, duration:0.2, ease:"back.out(3)"}, 2.47);
    mouth(tl, "s1-adik", 2.5, "o"); blink(tl, "s1-adik", 2.48);
    mouth(tl, "s1-adik", 2.85, "sad"); look(tl, "s1-adik", 2.85, 10, -2); brows(tl, "s1-adik", 2.85, 6);
    // abang ketawa, kawan minta bola
    
    laugh(tl, "s1-abang", 2.7, 3.4, 7); look(tl, "s1-abang", 2.7, -10, 2); look(tl, "s1-abang", 3.45, 6, 0);
    pose(tl, "s1-kawan", 2.6, {armL:-150, armR:150}, 0.3, "back.out(2)");
    mouth(tl, "s1-kawan", 2.6, "o");
    mouth(tl, "s1-abang", 3.5, "smile");
    // sepakan kuat abang -> bola terbang ke langit
    tl.to("#s1-abang-body", {rotation:-6, duration:0.3, svgOrigin:"0 0", ease:"power2.out"}, 3.55);
    pose(tl, "s1-abang", 3.55, {legR:55, armL:-50, armR:40}, 0.35);
    pose(tl, "s1-abang", 3.95, {legR:-100, armL:50, armR:-60}, 0.1, "power4.in");
    tl.to("#s1-abang-body", {rotation:4, duration:0.12}, 3.95);
    tl.to("#s1-ball", {x:700, y:-420, duration:0.7, ease:"power1.out"}, 4.05);
    tl.to("#s1-ball-spin", {rotation:-2600, duration:0.7, ease:"power1.out"}, 4.05);
    for (const k of ["abang","kawan","adik"]) { look(tl, `s1-${k}`, 4.15, k==="kawan"?-4:4, -9); mouth(tl, `s1-${k}`, 4.25, "o"); }
    tl.to("#s1-adik-body", {rotation:0, y:0, duration:0.3, ease:"power2.out"}, 4.1);
    pose(tl, "s1-adik", 4.1, {legL:0, legR:0, armL:0, armR:0}, 0.3);
    pose(tl, "s1-kawan", 4.15, {armL:-20, armR:20}, 0.3);
    // kamera dongak ikut bola (bergerak laju ke potongan)
    tl.fromTo("#s1-camwrap", {y:0, filter:"blur(0px)"}, {y:1500, filter:"blur(14px)", duration:0.75, ease:"power3.in"}, 4.62);
"""
write("compositions/padang.html", scene("padang", S1_DUR, s1, s1_js))

# ============================================================ S2 pokok
S2_DUR = 9.0
leaves_pos = [(560, 520, 300), (330, 640, 210), (790, 640, 210), (420, 400, 200), (700, 400, 200), (560, 300, 190),
              (250, 800, 150), (870, 800, 150), (560, 760, 240)]
canopy = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{["#3F8E3A","#4FA145","#3A8034"][k%3]}" stroke="{INK}" stroke-width="6"/>' for k, (x, y, r) in enumerate(leaves_pos))
fruits = "".join(f'<circle cx="{x}" cy="{y}" r="13" fill="#E0322B" stroke="{INK}" stroke-width="3"/>' for x, y in
                 [(300, 560), (420, 720), (700, 690), (820, 560), (480, 330), (650, 300), (230, 760), (900, 770), (560, 880), (380, 460), (760, 450)])
fall_leaves = "".join(f'<path id="s2-leaf{k}" d="M0 -14 Q14 0 0 14 Q-14 0 0 -14Z" fill="#4FA145" stroke="{INK}" stroke-width="3" opacity="0"/>' for k in range(6))
s2 = stage("s2", f'''
{sky("s2-sky", "#FFB36B", "#FFE7B0", sun=False)}
{hills(1150)}
{field("s2-field", 1150)}
<g id="s2-tree">
<path d="M500 1440 Q520 1100 500 900 L620 900 Q600 1100 640 1440Z" fill="#7A4E2D" stroke="{INK}" stroke-width="6"/>
<path d="M540 960 Q440 880 380 820 M590 940 Q690 860 760 800" stroke="#7A4E2D" stroke-width="26" stroke-linecap="round" fill="none"/>
<g id="s2-canopy">{canopy}{fruits}
<g id="s2-sel-stuck" opacity="0"><g transform="translate(810,640) rotate(25)"><path d="M-14 -40 Q16 -44 16 0 Q16 40 -2 44 Q-20 40 -18 0Z" fill="#FF8A1F" stroke="{INK}" stroke-width="4"/><path d="M0 -30 L-10 -6 M0 -30 L12 -6" stroke="#2F6FD6" stroke-width="6"/></g></g>
</g>
</g>
{ball_svg("s2-ball")}
<g id="s2-sel"><path d="M-14 -40 Q16 -44 16 0 Q16 40 -2 44 Q-20 40 -18 0Z" fill="#FF8A1F" stroke="{INK}" stroke-width="4"/><path d="M0 -30 L-10 -6 M0 -30 L12 -6" stroke="#2F6FD6" stroke-width="6"/></g>
{fall_leaves}
<g id="s2-kids">
{kid_svg("s2", "abang")}
{kid_svg("s2", "kawan", flip=True)}
{kid_svg("s2", "adik")}
</g>''')

s2_js = r"""
    for (const k of ["abang","kawan","adik"]) rig(tl, `s2-${k}`);
    place(tl, "s2-abang", 250, 1480, 1.15);
    place(tl, "s2-kawan", 860, 1480, 1.05, true);
    place(tl, "s2-adik", 560, 1500, 0.92);
    for (const k of ["abang","kawan","adik"]) { look(tl, `s2-${k}`, 0, k==="kawan"?-3:3, -10, 0.01); mouth(tl, `s2-${k}`, 0, "o"); }
    tl.set("#s2-sel", {opacity:0, x:330, y:1180}, 0);
    // dunia masuk dari atas (sambungan dongakan kamera)
    tl.fromTo("#s2-camwrap", {y:-1300, filter:"blur(14px)"}, {y:0, filter:"blur(0px)", duration:0.5, ease:"power3.out"}, 0);
    // bola jatuh masuk ke dahan, tersangkut
    tl.set("#s2-ball", {x:640, y:-200}, 0);
    tl.to("#s2-ball", {y:600, duration:0.55, ease:"power2.in"}, 0.05);
    tl.to("#s2-ball-spin", {rotation:500, svgOrigin:"0 0", duration:0.6, ease:"none"}, 0.05);
    tl.to("#s2-ball", {y:575, duration:0.12, ease:"power2.out"}, 0.6).to("#s2-ball", {y:590, duration:0.15, ease:"power2.in"}, 0.72);
    // pokok bergoyang
    const wob = [[0.6,2.2],[0.75,-1.6],[0.9,1.0],[1.05,-0.5],[1.2,0]];
    for (const [t,r] of wob) tl.to("#s2-canopy", {rotation:r, svgOrigin:"560 1000", duration:0.15, ease:"sine.inOut"}, t);
    // daun gugur
    const lv = [[420,700],[690,650],[540,820],[300,760],[780,760],[600,560]];
    lv.forEach(([x,y],k)=>{
      const t0 = 0.65 + k*0.07;
      tl.set(`#s2-leaf${k}`, {x, y, opacity:1, rotation:k*40}, t0);
      tl.to(`#s2-leaf${k}`, {y: 1400 + k*15, x: x + (k%2? 60:-60), rotation: k*40 + 360, duration:2.2, ease:"power1.in"}, t0);
      tl.to(`#s2-leaf${k}`, {opacity:0, duration:0.2}, t0+2.0);
    });
    blink(tl, "s2-adik", 1.3); blink(tl, "s2-abang", 1.45);
    // kawan lompat dua kali
    for (const [t,h] of [[1.55,-170],[2.25,-210]]) {
      tl.to("#s2-kawan-body", {scaleY:0.88, svgOrigin:"0 0", duration:0.1}, t);
      tl.to("#s2-kawan", {y:1480+h, duration:0.25, ease:"power2.out"}, t+0.1);
      tl.to("#s2-kawan-body", {scaleY:1.05, duration:0.12}, t+0.1);
      pose(tl, "s2-kawan", t+0.1, {armL:-170, armR:160, legL:20, legR:-15}, 0.15);
      tl.to("#s2-kawan", {y:1480, duration:0.25, ease:"power2.in"}, t+0.35);
      tl.to("#s2-kawan-body", {scaleY:0.9, duration:0.06}, t+0.6).to("#s2-kawan-body", {scaleY:1, duration:0.1}, t+0.66);
      pose(tl, "s2-kawan", t+0.45, {legL:0, legR:0}, 0.12);
    }
    pose(tl, "s2-kawan", 2.95, {armL:-10, armR:10}, 0.3); mouth(tl, "s2-kawan", 2.95, "sad"); brows(tl, "s2-kawan", 2.95, 5);
    // abang baling selipar -> selipar pun tersangkut
    mouth(tl, "s2-abang", 3.0, "smile");
    pose(tl, "s2-abang", 3.05, {armR:120}, 0.35);
    tl.to("#s2-abang-body", {rotation:-5, svgOrigin:"0 0", duration:0.35}, 3.05);
    tl.set("#s2-sel", {opacity:1, x:330, y:1180}, 3.45);
    pose(tl, "s2-abang", 3.45, {armR:-160}, 0.12, "power4.in");
    tl.to("#s2-abang-body", {rotation:4, duration:0.12}, 3.45);
    tl.to("#s2-sel", {x:810, duration:0.6, ease:"none"}, 3.5);
    tl.to("#s2-sel", {y:640, duration:0.6, ease:"power2.out"}, 3.5);
    tl.to("#s2-sel", {rotation:745, duration:0.6, ease:"none"}, 3.5);
    tl.set("#s2-sel", {opacity:0}, 4.1); tl.set("#s2-sel-stuck", {opacity:1}, 4.1);
    for (const [t,r] of [[4.1,1.4],[4.25,-0.8],[4.4,0]]) tl.to("#s2-canopy", {rotation:r, duration:0.15}, t);
    mouth(tl, "s2-abang", 4.2, "o"); tl.to("#s2-abang-body", {rotation:0, duration:0.2}, 4.2); pose(tl, "s2-abang", 4.2, {armR:-10}, 0.3);
    look(tl, "s2-abang", 4.15, 8, -10);
    laugh(tl, "s2-kawan", 4.35, 5.0, 6);
    // adik dapat idea: lompat kecil
    look(tl, "s2-adik", 4.6, -6, -2);
    mouth(tl, "s2-adik", 4.7, "grin");
    tl.to("#s2-adik", {y:1430, duration:0.15, ease:"power2.out"}, 4.75).to("#s2-adik", {y:1500, duration:0.15, ease:"power2.in"}, 4.9);
    pose(tl, "s2-adik", 4.75, {armL:-150, armR:150}, 0.15);
    // menara budak: abang ke bawah bola, kawan naik bahu, adik paling atas
    run(tl, "s2-abang", 5.05, 5.5, 600, 0.11, 30);
    look(tl, "s2-abang", 5.5, 0, -10); mouth(tl, "s2-abang", 5.5, "smile");
    pose(tl, "s2-abang", 5.55, {armL:-120, armR:120}, 0.25);
    arcTo(tl, "#s2-kawan", 5.55, 600, 1170, 1020, 0.5);
    tl.to("#s2-kawan", {scaleX:-1.0, scaleY:1.0, duration:0.3}, 5.55);
    pose(tl, "s2-kawan", 5.6, {legL:-15, legR:15, armL:-60, armR:60}, 0.2);
    mouth(tl, "s2-kawan", 5.7, "grin");
    tl.to("#s2-abang-body", {scaleY:0.94, svgOrigin:"0 0", duration:0.1}, 6.05).to("#s2-abang-body", {scaleY:1, duration:0.15}, 6.15);
    arcTo(tl, "#s2-adik", 6.15, 600, 880, 760, 0.5);
    pose(tl, "s2-adik", 6.2, {armL:-170, armR:170, legL:-10, legR:10}, 0.25);
    tl.to("#s2-kawan-body", {scaleY:0.94, svgOrigin:"0 0", duration:0.1}, 6.65).to("#s2-kawan-body", {scaleY:1, duration:0.15}, 6.75);
    look(tl, "s2-adik", 6.6, 4, -10);
    // menara bergoyang sedikit
    for (const [t,r] of [[6.7,3],[6.85,-3],[7.0,2]]) { tl.to("#s2-kawan-body", {rotation:r, svgOrigin:"0 0", duration:0.15, ease:"sine.inOut"}, t); tl.to("#s2-adik-body", {rotation:-r*1.4, svgOrigin:"0 0", duration:0.15, ease:"sine.inOut"}, t+0.03); }
    // adik goncang dahan
    for (const [t,r] of [[6.95,3],[7.07,-3],[7.19,3],[7.31,-2],[7.43,0]]) tl.to("#s2-canopy", {rotation:r, duration:0.12, ease:"sine.inOut"}, t);
    for (const [t,r] of [[6.95,150],[7.07,175],[7.19,150],[7.31,175]]) pose(tl, "s2-adik", t, {armL:-r, armR:r}, 0.12, "sine.inOut");
    // bola + selipar jatuh
    tl.set("#s2-sel-stuck", {opacity:0}, 7.45); tl.set("#s2-sel", {opacity:1, x:810, y:640, rotation:25}, 7.45);
    tl.to("#s2-sel", {y:1470, rotation:400, duration:0.6, ease:"power2.in"}, 7.45);
    tl.to("#s2-ball", {y:1440, x:760, duration:0.6, ease:"power2.in"}, 7.4);
    tl.to("#s2-ball", {y:1340, x:860, duration:0.25, ease:"power2.out"}, 8.0).to("#s2-ball", {y:1440, x:920, duration:0.25, ease:"power2.in"}, 8.25);
    tl.to("#s2-ball-spin", {rotation:1300, duration:1.1, ease:"none"}, 7.4);
    mouth(tl, "s2-adik", 7.45, "o");
    // menara runtuh -> semua jatuh, ketawa
    tl.to("#s2-adik", {x:420, y:1500, rotation:-30, duration:0.55, ease:"power2.in"}, 7.6);
    tl.to("#s2-kawan", {x:800, y:1480, rotation:20, duration:0.45, ease:"power2.in"}, 7.65);
    tl.to("#s2-abang", {rotation:-12, duration:0.3, ease:"power2.in"}, 7.75);
    for (const k of ["abang","kawan","adik"]) pose(tl, `s2-${k}`, 7.7, {armL:-90, armR:90, legL:-30, legR:30}, 0.25);
    tl.to("#s2-adik", {rotation:-8, duration:0.2, ease:"back.out(3)"}, 8.15);
    tl.to("#s2-kawan", {rotation:6, duration:0.2, ease:"back.out(3)"}, 8.1);
    tl.to("#s2-abang", {rotation:-3, duration:0.2, ease:"back.out(3)"}, 8.05);
    for (const k of ["abang","kawan","adik"]) { look(tl, `s2-${k}`, 8.2, 0, 0); pose(tl, `s2-${k}`, 8.2, {armL:-30, armR:30, legL:-10, legR:10}, 0.25); laugh(tl, `s2-${k}`, 8.25 + (k==="adik"?0.05:k==="kawan"?0.1:0), 9.0, 6); }
"""
write("compositions/pokok.html", scene("pokok", S2_DUR, s2, s2_js))

# ============================================================ S3 hujan
S3_DUR = 7.7
rain_tile = "data:image/svg+xml;utf8," + (
    "<svg xmlns='http://www.w3.org/2000/svg' width='240' height='320'>" +
    "".join(f"<line x1='{x}' y1='{y}' x2='{x-10}' y2='{y+46}' stroke='%23DDEBF5' stroke-width='4' stroke-linecap='round' opacity='0.75'/>"
            for x, y in [(20, 10), (90, 80), (160, 30), (220, 150), (60, 190), (130, 240), (200, 270), (30, 120), (110, 160), (180, 210)]) +
    "</svg>")
puddles = "".join(f'<ellipse id="s3-pud{k}" cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="#7E95A3" stroke="#5B4430" stroke-width="5"/>'
                  for k, (x, y, rx, ry) in enumerate([(640, 1475, 150, 26), (880, 1420, 120, 20), (240, 1560, 110, 22)]))
splash_drops = lambda p, n: "".join(f'<circle id="{p}{k}" cx="0" cy="0" r="{9 + (k%3)*4}" fill="#8A6A48" opacity="0"/>' for k in range(n))
s3 = stage("s3", f'''
{sky("s3-sky", "#FF9F5A", "#FFE1A1")}
<rect id="s3-grey" x="-400" y="-1400" width="1880" height="4000" fill="#6E8796" opacity="0"/>
{hills()}
<g id="s3-hdark" opacity="0">{hills(dark=True)}</g>
{palm(120, 1010, 0.9)}{palm(980, 1000, 1.1)}{house(300, 1000)}
{field("s3-field")}
<rect id="s3-fdark" x="-400" y="1060" width="1880" height="1400" fill="#2F4A2A" opacity="0"/>
<g id="s3-puds">{puddles}</g>
{goal_side(940, 1290)}
<g id="s3-kids">
{kid_svg("s3", "kawan", True, flip=True)}
{kid_svg("s3", "abang", True)}
{kid_svg("s3", "adik")}
{ball_svg("s3-ball")}
</g>
{splash_drops("s3-spA", 7)}{splash_drops("s3-spB", 7)}
<rect id="s3-flash" x="-400" y="-1400" width="1880" height="4000" fill="#FFFFFF" opacity="0"/>''')
s3 += f'''
    <div class="stage" id="s3-rainwrap" data-layout-ignore data-layout-allow-occlusion style="opacity:0; overflow:hidden;">
      <div id="s3-rain1" style="position:absolute; left:-200px; top:-1920px; width:1480px; height:3840px; background-image:url(&quot;{rain_tile}&quot;); background-size:240px 320px;"></div>
      <div id="s3-rain2" style="position:absolute; left:-100px; top:-1920px; width:1480px; height:3840px; background-image:url(&quot;{rain_tile}&quot;); background-size:170px 230px; opacity:0.6;"></div>
    </div>'''

s3_js = r"""
    for (const k of ["abang","kawan","adik"]) rig(tl, `s3-${k}`);
    place(tl, "s3-abang", 300, 1440, 1.15);
    place(tl, "s3-kawan", 800, 1400, 1.05, true);
    place(tl, "s3-adik", 150, 1500, 0.95);
    tl.set("#s3-ball", {x:380, y:1412}, 0);
    for (const k of ["abang","kawan","adik"]) { mouth(tl, `s3-${k}`, 0, "grin"); look(tl, `s3-${k}`, 0, k==="kawan"?-6:6, 2, 0.01); }
    tl.set("#s3-puds ellipse", {scale:0, svgOrigin:"0 0", transformOrigin:"50% 50%"}, 0);
    laugh(tl, "s3-adik", 0, 0.5, 5); laugh(tl, "s3-abang", 0, 0.45, 5); laugh(tl, "s3-kawan", 0.05, 0.5, 5);
    // langit gelap, kilat, guruh
    tl.to("#s3-grey", {opacity:1, duration:0.7, ease:"power2.inOut"}, 0.3);
    tl.to("#s3-hdark", {opacity:1, duration:0.7, ease:"power2.inOut"}, 0.3);
    tl.to("#s3-fdark", {opacity:0.35, duration:0.7, ease:"power2.inOut"}, 0.3);
    tl.to("#s3-flash", {opacity:0.85, duration:0.04}, 0.75).to("#s3-flash", {opacity:0, duration:0.12}, 0.79)
      .to("#s3-flash", {opacity:0.6, duration:0.04}, 0.95).to("#s3-flash", {opacity:0, duration:0.25}, 0.99);
    for (const k of ["abang","kawan","adik"]) { look(tl, `s3-${k}`, 0.75, 0, -10, 0.08); mouth(tl, `s3-${k}`, 0.77, "o"); tl.to(`#s3-${k}-eyes`, {scale:1.15, svgOrigin:"0 -302", duration:0.1}, 0.77); }
    // hujan turun
    tl.to("#s3-rainwrap", {opacity:1, duration:0.5, ease:"power1.out"}, 0.9);
    tl.fromTo("#s3-rain1", {y:0}, {y:1920, duration:6.8, ease:"none"}, 0.9);
    tl.fromTo("#s3-rain2", {y:0}, {y:1380, duration:6.8, ease:"none"}, 0.9);
    tl.to("#s3-puds ellipse", {scale:1, duration:0.6, ease:"power2.out", stagger:0.15}, 1.0);
    for (const k of ["abang","kawan","adik"]) { tl.to(`#s3-${k}-eyes`, {scale:1, duration:0.15}, 1.35); look(tl, `s3-${k}`, 1.35, k==="kawan"?-6:6, 2); mouth(tl, `s3-${k}`, 1.4, "grin"); }
    // abang gelecek, tergelincir masuk lopak
    tl.to("#s3-ball", {x:600, duration:0.75, ease:"none"}, 1.7);
    tl.to("#s3-ball-spin", {rotation:640, svgOrigin:"0 0", duration:0.75, ease:"none"}, 1.7);
    run(tl, "s3-abang", 1.65, 2.4, 540, 0.13, 32);
    tl.to("#s3-abang-body", {rotation:-75, y:-20, svgOrigin:"0 0", duration:0.22, ease:"power2.in"}, 2.4);
    pose(tl, "s3-abang", 2.4, {legL:-80, legR:-60, armL:-150, armR:-120}, 0.2);
    tl.to("#s3-abang", {x:700, duration:0.6, ease:"power2.out"}, 2.45);
    mouth(tl, "s3-abang", 2.42, "o");
    tl.set("#s3-abang-mud", {opacity:1}, 2.7);
    tl.to("#s3-ball", {x:820, duration:0.5, ease:"power1.out"}, 2.45);
    tl.to("#s3-ball-spin", {rotation:1100, duration:0.5, ease:"power1.out"}, 2.45);
    // kawan meluru, tergelincir meniarap
    run(tl, "s3-kawan", 2.6, 2.95, 760, 0.12, 30);
    tl.to("#s3-kawan-body", {rotation:70, y:-30, svgOrigin:"0 0", duration:0.2, ease:"power2.in"}, 2.95);
    pose(tl, "s3-kawan", 2.95, {armL:-160, armR:-170, legL:40, legR:60}, 0.2);
    tl.to("#s3-kawan", {x:640, duration:0.5, ease:"power2.out"}, 3.0);
    mouth(tl, "s3-kawan", 2.97, "o"); tl.set("#s3-kawan-mud", {opacity:1}, 3.2);
    // bola terlepas, bergolek perlahan ke kaki adik
    tl.to("#s3-ball", {x:285, duration:1.5, ease:"power2.out"}, 3.15);
    tl.to("#s3-ball-spin", {rotation:-200, duration:1.5, ease:"power2.out"}, 3.15);
    laugh(tl, "s3-abang", 3.3, 4.6, 4); laugh(tl, "s3-kawan", 3.6, 4.6, 4);
    // percikan lumpur
    const spl = (p, t, cx, cy) => { for (let k=0;k<7;k++){ const a = Math.PI*(0.15+0.7*k/6); tl.set(`#${p}${k}`, {x:cx, y:cy, opacity:1}, t);
      tl.to(`#${p}${k}`, {x: cx + Math.cos(a)*(110+k*12) * (k%2?1:-1), duration:0.5, ease:"power1.out"}, t);
      tl.to(`#${p}${k}`, {y: cy - Math.sin(a)*170, duration:0.25, ease:"power2.out"}, t).to(`#${p}${k}`, {y: cy + 10, duration:0.25, ease:"power2.in"}, t+0.25);
      tl.set(`#${p}${k}`, {opacity:0}, t+0.5); } };
    spl("s3-spA", 2.62, 660, 1460); spl("s3-spB", 3.15, 650, 1440);
    // adik: pandang bola, pandang gol
    look(tl, "s3-adik", 3.8, 9, 8); mouth(tl, "s3-adik", 4.0, "o");
    blink(tl, "s3-adik", 4.5);
    look(tl, "s3-adik", 4.75, 10, -2, 0.25); mouth(tl, "s3-adik", 4.8, "smile"); brows(tl, "s3-adik", 4.8, 5);
    // kamera tolak masuk ke adik
    tl.fromTo("#s3-camwrap", {scale:1, x:0, y:0}, {scale:1.55, x:380, y:-560, duration:1.0, ease:"power2.inOut", transformOrigin:"0 0"}, 4.6);
    tl.to("#s3-adik-body", {scaleY:0.92, svgOrigin:"0 0", duration:0.45, ease:"power2.out"}, 5.75);
    pose(tl, "s3-adik", 5.75, {legR:50, armL:-40, armR:45}, 0.5, "power2.out");
    pose(tl, "s3-adik", 6.45, {legR:-95, armL:45, armR:-55}, 0.1, "power4.in");
    tl.to("#s3-adik-body", {scaleY:1.04, duration:0.12}, 6.45);
    mouth(tl, "s3-adik", 6.5, "grin");
    // bola meluncur, kamera ikut (potong ketika laju)
    tl.to("#s3-ball", {x:1200, y:1380, duration:0.9, ease:"power2.in"}, 6.55);
    tl.to("#s3-ball-spin", {rotation:1400, duration:0.9, ease:"power2.in"}, 6.55);
    tl.to("#s3-camwrap", {x:-400, filter:"blur(10px)", duration:0.6, ease:"power3.in"}, 7.1);
"""
write("compositions/hujan.html", scene("hujan", S3_DUR, s3, s3_js))

# ============================================================ S4 gol (pandangan depan)
S4_DUR = 5.6
netlines = "".join(f'<line x1="{170+k*37}" y1="760" x2="{230+k*31}" y2="1250" stroke="#FFFFFF" stroke-width="3" opacity="0.55"/>' for k in range(21))
netlines += "".join(f'<line x1="{170+3*k}" y1="{760+k*35}" x2="{910-3*k}" y2="{760+k*35}" stroke="#FFFFFF" stroke-width="3" opacity="0.55"/>' for k in range(15))
s4 = stage("s4", f'''
<rect x="-400" y="-1400" width="1880" height="4000" fill="#6E8796"/>
{hills(dark=True)}
<rect x="-400" y="1060" width="1880" height="1400" fill="#4A8A3A"/>
<rect x="-400" y="1060" width="1880" height="1400" fill="#2F4A2A" opacity="0.35"/>
<path d="M-400 1330 L1480 1330" stroke="#FFFFFF" stroke-width="10" opacity="0.8"/>
<g id="s4-net">{netlines}<path d="M230 1250 L850 1250" stroke="#FFF" stroke-width="3" opacity="0.6"/></g>
<g id="s4-postL"><rect x="150" y="740" width="40" height="595" rx="10" fill="#FFF" stroke="{INK}" stroke-width="6"/></g>
<rect x="890" y="740" width="40" height="595" rx="10" fill="#FFF" stroke="{INK}" stroke-width="6"/>
<rect x="150" y="730" width="780" height="40" rx="12" fill="#FFF" stroke="{INK}" stroke-width="6"/>
<path id="s4-twang" d="M120 820 Q100 900 120 980 M220 820 Q240 900 220 980" fill="none" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round" opacity="0"/>
<ellipse id="s4-ballsh" cx="0" cy="0" rx="40" ry="10" fill="#000" opacity="0.25"/>
{ball_svg("s4-ball")}
<path id="s4-drop" d="M0 -30 Q16 0 0 12 Q-16 0 0 -30Z" fill="#DDEBF5" stroke="#5B7C90" stroke-width="3" opacity="0"/>
<g id="s4-kids">
{kid_svg("s4", "abang", True)}
{kid_svg("s4", "kawan", True, flip=True)}
{kid_svg("s4", "adik")}
</g>''')
s4 += f'''
    <div class="stage" id="s4-rainwrap" data-layout-ignore data-layout-allow-occlusion style="overflow:hidden;">
      <div id="s4-rain1" style="position:absolute; left:-200px; top:-1920px; width:1480px; height:3840px; background-image:url(&quot;{rain_tile}&quot;); background-size:240px 320px;"></div>
    </div>
    <div id="s4-gol" class="ttl" style="opacity:0; top:330px; font-size:230px; color:#FFC928; text-shadow: 0 12px 0 {INK}, -6px 0 0 {INK}, 6px 0 0 {INK}, 0 -6px 0 {INK};">GOL!!!</div>'''

s4_js = r"""
    for (const k of ["abang","kawan","adik"]) rig(tl, `s4-${k}`);
    tl.fromTo("#s4-rain1", {y:0}, {y:1920*S4/6.8, duration:S4, ease:"none"}, 0);
    // bola dari depan (besar) ke gol, kena tiang kiri
    tl.fromTo("#s4-camwrap", {x:500, filter:"blur(10px)"}, {x:0, filter:"blur(0px)", duration:0.4, ease:"power3.out"}, 0);
    tl.set("#s4-ball", {x:900, y:1700, scale:3.2}, 0); tl.set("#s4-ballsh", {x:900, y:1790, scale:3.2}, 0);
    tl.to("#s4-ball", {x:200, y:1300, scale:1.25, duration:0.75, ease:"power1.out"}, 0);
    tl.to("#s4-ballsh", {x:200, y:1336, scale:1.25, duration:0.75, ease:"power1.out"}, 0);
    tl.to("#s4-ball-spin", {rotation:-900, svgOrigin:"0 0", duration:0.75, ease:"power1.out"}, 0);
    // TUING
    for (const [t,r] of [[0.75,2.5],[0.82,-2.2],[0.89,1.8],[0.96,-1.3],[1.03,0.8],[1.1,-0.4],[1.17,0]]) tl.to("#s4-postL", {rotation:r, svgOrigin:"170 1335", duration:0.07, ease:"sine.inOut"}, t);
    tl.to("#s4-twang", {opacity:1, duration:0.04}, 0.75).to("#s4-twang", {opacity:0, duration:0.4}, 0.95);
    tl.to("#s4-ball", {x:300, y:1360, scale:1.45, duration:0.45, ease:"power2.out"}, 0.76);
    tl.to("#s4-ballsh", {x:300, y:1398, scale:1.45, duration:0.45, ease:"power2.out"}, 0.76);
    tl.to("#s4-ball-spin", {rotation:-700, duration:0.45, ease:"power2.out"}, 0.76);
    // bola berhenti di garisan, bergoyang... (tahan nafas)
    for (const [t,r] of [[1.25,-760],[1.45,-720],[1.65,-748],[1.85,-735]]) tl.to("#s4-ball-spin", {rotation:r, duration:0.2, ease:"sine.inOut"}, t);
    // titisan hujan jatuh atas bola -> bola masuk!
    tl.set("#s4-drop", {x:300, y:900, opacity:1}, 1.9);
    tl.to("#s4-drop", {y:1300, duration:0.3, ease:"power2.in"}, 1.9);
    tl.set("#s4-drop", {opacity:0}, 2.2);
    tl.to("#s4-ball", {scaleY:1.3, scaleX:1.6, duration:0.06}, 2.2).to("#s4-ball", {scaleX:1.45, scaleY:1.45, duration:0.1}, 2.26);
    tl.to("#s4-ball", {x:420, y:1200, scale:1.0, duration:0.55, ease:"power2.in"}, 2.32);
    tl.to("#s4-ballsh", {x:420, y:1232, scale:1.0, duration:0.55, ease:"power2.in"}, 2.32);
    tl.to("#s4-ball-spin", {rotation:-200, duration:0.55, ease:"power2.in"}, 2.32);
    // jaring mengembung
    tl.to("#s4-net", {scale:1.05, svgOrigin:"420 1200", duration:0.12, ease:"power2.out"}, 2.87).to("#s4-net", {scale:1, duration:0.4, ease:"elastic.out(1,0.4)"}, 2.99);
    // GOL!!!
    tl.fromTo("#s4-gol", {opacity:0, scale:0.2, transformOrigin:"50% 60%"}, {opacity:1, scale:1, duration:0.45, ease:"elastic.out(1,0.5)", immediateRender:false}, 2.9);
    // budak berlari masuk, angkat adik
    place(tl, "s4-abang", -250, 1660, 1.3); place(tl, "s4-kawan", 1330, 1660, 1.25, true); place(tl, "s4-adik", 540, 2500, 1.15);
    tl.set("#s4-abang-mud", {opacity:1}, 0); tl.set("#s4-kawan-mud", {opacity:1}, 0);
    for (const k of ["abang","kawan","adik"]) mouth(tl, `s4-${k}`, 0, "grin");
    tl.to("#s4-adik", {y:1700, duration:0.35, ease:"power3.out"}, 3.1);
    pose(tl, "s4-adik", 3.15, {armL:-160, armR:160}, 0.25, "back.out(2)");
    run(tl, "s4-abang", 3.25, 3.75, 390, 0.12, 30);
    run(tl, "s4-kawan", 3.3, 3.8, 690, 0.12, 30);
    pose(tl, "s4-abang", 3.95, {armL:-150, armR:150}, 0.25, "back.out(2)"); pose(tl, "s4-kawan", 4.0, {armL:-150, armR:150}, 0.2);
    tl.to("#s4-adik", {y:1520, duration:0.35, ease:"back.out(2)"}, 3.95);
    tl.to("#s4-abang", {y:1620, duration:0.2}, 3.95); tl.to("#s4-kawan", {y:1620, duration:0.2}, 4.0);
    laugh(tl, "s4-abang", 4.2, 5.6, 5); laugh(tl, "s4-kawan", 4.25, 5.6, 5);
    tl.to("#s4-adik", {y:1480, duration:0.3, ease:"sine.inOut"}, 4.4).to("#s4-adik", {y:1520, duration:0.3, ease:"sine.inOut"}, 4.7).to("#s4-adik", {y:1480, duration:0.3, ease:"sine.inOut"}, 5.0);
    blink(tl, "s4-adik", 4.6);
    tl.to("#s4-camwrap", {scale:1.08, x:-43, y:-60, duration:2.4, ease:"power1.inOut", transformOrigin:"0 0"}, 3.2);
"""
s4_js = s4_js.replace("S4", str(S4_DUR))
write("compositions/gol.html", scene("gol", S4_DUR, s4, s4_js))

# ============================================================ S5 kad akhir
S5_DUR = 4.2
bands = ["#E63B2E", "#FF8A1F", "#FFC928", "#5DB443", "#2F6FD6", "#7A4FC2"]
rainbow = "".join(f'<path d="M{80+k*34} 1250 A{460-k*34} {460-k*34} 0 0 1 {1000-k*34} 1250" fill="none" stroke="{c}" stroke-width="34"/>' for k, c in enumerate(bands))
s5 = stage("s5", f'''
{sky("s5-sky", "#8EC9F0", "#FFE7B0", sun=False)}
<g id="s5-rainbow" opacity="0.9" mask="url(#s5-mask)">{rainbow}</g>
<defs><mask id="s5-mask"><rect id="s5-wipe" x="0" y="0" width="0" height="1920" fill="#FFF"/></mask></defs>
{hills(1250)}
{field("s5-field", 1250)}
{ball_svg("s5-ball")}
<g id="s5-t1"><text x="262" y="560" text-anchor="end" font-size="130" style="{TEXT_STYLE}">G</text>
<text x="352" y="560" text-anchor="start" font-size="130" style="{TEXT_STYLE}">l Pertama</text></g>
<text id="s5-t2" x="540" y="730" text-anchor="middle" font-size="190" style="{TEXT_STYLE} fill:#FFC928;">Adik</text>
<text id="s5-t3" x="540" y="880" text-anchor="middle" font-size="64" style="{TEXT_STYLE} stroke-width:10px;">— Tamat —</text>''')
s5_js = r"""
    tl.fromTo("#s5-wipe", {attr:{width:0}}, {attr:{width:1080}, duration:0.9, ease:"power2.inOut"}, 0.1);
    tl.set("#s5-t1", {opacity:0}, 0); tl.set("#s5-t2", {opacity:0, scale:0.4, transformOrigin:"50% 50%"}, 0); tl.set("#s5-t3", {opacity:0}, 0);
    tl.to("#s5-t1", {opacity:1, duration:0.2}, 0.35);
    // bola bergolek masuk jadi huruf "o"
    tl.set("#s5-ball", {x:-120, y:1400, scale:1.5}, 0);
    tl.to("#s5-ball", {x:307, duration:0.9, ease:"power2.out"}, 0.3);
    tl.to("#s5-ball", {y:470, duration:0.45, ease:"power2.out"}, 0.3).to("#s5-ball", {y:518, scale:1.45, duration:0.45, ease:"bounce.out"}, 0.75);
    tl.to("#s5-ball-spin", {rotation:900, svgOrigin:"0 0", duration:0.9, ease:"power2.out"}, 0.3);
    tl.to("#s5-t2", {opacity:1, scale:1, duration:0.5, ease:"elastic.out(1,0.55)"}, 1.15);
    tl.to("#s5-t3", {opacity:1, duration:0.3}, 1.7);
"""
write("compositions/akhir.html", scene("akhir", S5_DUR, s5, s5_js))

# ============================================================ root
scenes = [("padang", S1_DUR), ("pokok", S2_DUR), ("hujan", S3_DUR), ("gol", S4_DUR), ("akhir", S5_DUR)]
starts = {}
t = 0.0
for n, d in scenes:
    starts[n] = round(t, 3); t += d
TOTAL = round(t, 3)

hosts = "\n".join(
    f'      <div id="{n}" data-composition-id="{n}" data-composition-src="compositions/{n}.html" data-start="{starts[n]}" data-duration="{d}" data-track-index="1" data-track-kind="graphics" data-width="{W}" data-height="{H}"></div>'
    for n, d in scenes)

S = starts
sfx = [  # (id, file, start, volume)
    ("sx-roll", "bounce.wav", 0.05, 0.25),
    ("sx-whoosh1", "whoosh-short.mp3", S["padang"] + 1.75, 0.6),
    ("sx-thud1", "thud.wav", S["padang"] + 2.47, 0.9),
    ("sx-kick1", "kick.wav", S["padang"] + 3.96, 1.0),
    ("sx-whoosh2", "whoosh.mp3", S["padang"] + 4.6, 0.5),
    ("sx-rustle1", "rustle.wav", S["pokok"] + 0.58, 0.9),
    ("sx-bounce1", "bounce.wav", S["pokok"] + 1.66, 0.35),
    ("sx-bounce2", "bounce.wav", S["pokok"] + 2.36, 0.35),
    ("sx-whoosh3", "whoosh-short.mp3", S["pokok"] + 3.45, 0.5),
    ("sx-rustle2", "rustle.wav", S["pokok"] + 4.1, 0.6),
    ("sx-pop1", "pop.mp3", S["pokok"] + 6.05, 0.6),
    ("sx-pop2", "pop.mp3", S["pokok"] + 6.65, 0.6),
    ("sx-rustle3", "rustle.wav", S["pokok"] + 6.95, 0.9),
    ("sx-bounce3", "bounce.wav", S["pokok"] + 8.0, 0.8),
    ("sx-thud2", "thud.wav", S["pokok"] + 8.1, 1.0),
    ("sx-thunder", "thunder.wav", S["hujan"] + 0.76, 1.0),
    ("sx-rain", "rain.wav", S["hujan"] + 0.9, 0.55, 7.4),
    ("sx-splash1", "splash.wav", S["hujan"] + 2.62, 0.9),
    ("sx-splash2", "splash.wav", S["hujan"] + 3.15, 0.8),
    ("sx-kick2", "kick.wav", S["hujan"] + 6.47, 1.0),
    ("sx-whoosh4", "whoosh-short.mp3", S["hujan"] + 7.1, 0.45),
    ("sx-tiang", "tiang.wav", S["gol"] + 0.75, 0.9),
    ("sx-drop", "pop.mp3", S["gol"] + 2.2, 0.35),
    ("sx-impact", "impact-bass-1.mp3", S["gol"] + 2.88, 0.8),
    ("sx-whistle", "whistle.wav", S["gol"] + 2.95, 0.55),
    ("sx-cheer", "cheer.wav", S["gol"] + 3.0, 0.8),
    ("sx-sparkle", "sparkle.mp3", S["akhir"] + 1.15, 0.6),
]
import subprocess
def fdur(f):
    return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",os.path.join(ROOT,"assets/sfx",f)]).decode())
# lorong SFX: satu lorong, lorong kedua hanya bila bertindih
lanes_end = []
rows = []
for a in sorted(sfx, key=lambda a: a[2]):
    d = a[4] if len(a) > 4 else round(fdur(a[1]), 3)
    st = round(a[2], 3)
    lane = next((k for k, e in enumerate(lanes_end) if e <= st), None)
    if lane is None: lanes_end.append(0); lane = len(lanes_end) - 1
    lanes_end[lane] = st + d
    fade = ' data-fade-out="0.4"' if len(a) > 4 else ''
    rows.append(f'      <audio id="{a[0]}" class="clip" src="assets/sfx/{a[1]}" data-start="{st}" data-duration="{d}"{fade} data-track-index="{3+lane}" data-volume="{a[3]}"></audio>')
audio = "\n".join(rows)
# hujan berterusan ke babak gol
audio += f'\n      <audio id="sx-rain2" class="clip" src="assets/sfx/rain.wav" data-start="{round(S["gol"]+0.6,3)}" data-track-index="{3+len(lanes_end)}" data-volume="0.5" data-media-start="1.0" data-duration="5.6" data-fade-out="1.2"></audio>'

index = f'''<!doctype html>
<html lang="ms">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width={W}, height={H}" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>
      * {{ margin:0; padding:0; box-sizing:border-box; }}
      html, body {{ margin:0; width:{W}px; height:{H}px; overflow:hidden; background:#FFD08A; }}
      #main {{ position:relative; width:{W}px; height:{H}px; font-family:"Nunito", sans-serif; }}
    </style>
  </head>
  <body>
    <div id="main" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="{W}" data-height="{H}">
{hosts}
{audio}
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
'''
write("index.html", index)
print("total", TOTAL, starts)
