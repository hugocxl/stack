"""Components for orthographic systems, data, and accessibility figures."""

from math import cos, sin, radians, pi

from geometry import BOLD, DETAIL, EDGE, GUIDE, oval, rounded


def box(s, at, dimensions, ink=EDGE, radius=4):
    """Draw a rounded solid with its dimensions adjacent to its origin."""
    s.box(*at, *dimensions, radius, ink)


def panel(s, x, y, z, w, h, thickness=7, ink=EDGE):
    if isinstance(thickness,str):
        thickness, ink = 7, thickness
    box(s, (x, y, z), (w, thickness, h), ink)


def rectangle(s, x, y, z, w, d, ink=DETAIL, radius=2, dashed=False):
    pts = [(a, b, z) for a, b in rounded(x, y, w, d, radius)]
    s.line(pts + pts[:1], ink, dashed=dashed)


def bezel(s, x, y, z, w, h, ink=DETAIL, radius=3):
    pts = [(a, y, b) for a, b in rounded(x, z, w, h, radius)]
    s.line(pts + pts[:1], ink)


def check(s, x, y, z, length=9, ink=BOLD):
    # Orient the stroke in projection, so one rise doesn't flatten on the worktop.
    pts = [(0, 0), (.30, .34), (1, -.43)]
    s.line([(x+length*(u*.577+v*1.155), y+length*(-u*.577+v*1.155), z)
            for u, v in pts], ink)


def check_upright(s, x, y, z, length=12, ink=BOLD):
    s.line([(x, y, z), (x+length*.25, y, z-length*.18),
            (x+length, y, z+length*.78)], ink)


def guide(s, *points):
    start, end = points if len(points) == 2 else (points[:3], points[3:])
    s.line([start, end], GUIDE, dashed=True)


def arrow(s, x, y, z, direction=0, length=18, ink=EDGE):
    """A directional cue on a horizontal surface, headed at (x,y,z)."""
    angle = radians(direction)
    ca, sa = cos(angle), sin(angle)
    def local(u, v):
        return (x+u*ca-v*sa, y+u*sa+v*ca, z)
    s.line([local(-length,0),local(0,0)], ink)
    s.line([local(-6,-4.2),local(0,0),local(-6,4.2)], ink)


def lines(s, x, y, z, widths, step=7, ink=DETAIL):
    for row, width in enumerate(widths):
        if width:
            s.line([(x,y+row*step,z),(x+width,y+row*step,z)], ink)


def text_upright(s, x, y, z, widths, step=8, ink=DETAIL, rtl=False):
    if isinstance(widths,int):
        widths=(widths,)
    for row, width in enumerate(widths):
        left, right = (x-width,x) if rtl else (x,x+width)
        s.line([(left,y,z-row*step),(right,y,z-row*step)], ink)


def sheet(s, x, y, z, w, d, ink=EDGE, text=True, tab=False):
    if tab:
        s.face([(x,y,z),(x+w*.45,y,z),(x+w*.53,y-6,z),
                (x+w-4,y-6,z),(x+w,y,z),(x+w,y+d,z),(x,y+d,z)], ink)
        top = z
    else:
        box(s, (x,y,z),(w,d,2.2),ink,3)
        top = z+2.2
    if text:
        lines(s,x+w*.15,y+d*.25,top,[w*.60,w*.43,w*.57],d*.16)
    return top


def screen(s, x, y, z, w, h, ink=EDGE, topbar=False):
    panel(s,x,y,z,w,h,7,ink)
    face = y+7
    bezel(s,x+4,face,z+4,w-8,h-8)
    if topbar:
        s.line([(x+5,face,z+h-15),(x+w-5,face,z+h-15)])
        text_upright(s,x+10,face,z+h-10,[w*.13],ink=EDGE)
    return face


def button(s, x, y, z, r=6, ink=EDGE):
    s.disk(x,y,z,r,r,3,ink)


def chip(s, x, y, z, w=39, d=29, h=7, ink=EDGE, contacts=4):
    # Widen the pads just enough to leave distinct contact gaps at thumbnail scale.
    for i in range(contacts):
        u=x+6+(w-12)*i/max(1,contacts-1)
        for v in (y-5,y+d-1):
            box(s,(u-1.3,v,z),(2.6,6,1.5),DETAIL,1)
    box(s,(x,y,z),(w,d,h),ink,4)
    rectangle(s,x+5,y+5,z+h,w-10,d-10,DETAIL,2)
    s.line([(x+10,y+11,z+h),(x+20,y+11,z+h)],DETAIL)


def slider(s, x, y, z, length=36, at=.6, ink=EDGE):
    rectangle(s,x,y,z,length,7,DETAIL,3.5)
    knob=x+length*at
    box(s,(knob-4,y-1,z),(8,9,4),ink,2.4)


def toggle(s, x, y, z, on=True, ink=EDGE):
    rectangle(s,x,y,z,20,10,DETAIL,5)
    s.disk(x+(14 if on else 6),y+5,z,3.4,3.4,3.2,ink)


def ports(s, x, y, z, count=3, gap=10):
    for i in range(count):
        bezel(s,x+i*gap,y,z,5,4,DETAIL,1)


def chassis(s, x, y, z, w=51, d=37, h=18, ink=EDGE, kind="ports"):
    box(s,(x,y,z),(w,d,h),ink,5)
    if kind == "ports":
        ports(s,x+7,y+d,z+5,3,min(10,(w-12)/3))
    elif kind == "drawer":
        bezel(s,x+4,y+d,z+3,w-8,h-6,DETAIL,2)
        s.line([(x+w*.35,y+d,z+h*.57),(x+w*.65,y+d,z+h*.57)],DETAIL)
    elif kind == "sealed":
        s.line([(x+w*.33,y+d,z+h*.38),(x+w*.67,y+d,z+h*.38)],DETAIL)
        rectangle(s,x+w*.35,y+d*.25,z+h,w*.3,d*.45,DETAIL,1.5)


def tray(s, x, y, z, w=54, d=42, front=False, ink=EDGE):
    box(s,(x,y,z),(w,d,4),ink,4)
    box(s,(x,y,z+4),(w,3.6,8),DETAIL,1.5)
    box(s,(x,y+3.6,z+4),(3.6,d-3.6,8),DETAIL,1.5)
    if front:
        lip(s,x,y,z,w,d,ink)


def lip(s, x, y, z, w, d, ink=EDGE):
    box(s,(x+w-3.6,y+3.6,z+4),(3.6,d-3.6,8),DETAIL,1.5)
    box(s,(x,y+d-3.6,z+4),(w-3.6,3.6,7),ink,1.5)


def ring(s, x, y, z, r, ink=EDGE):
    s.ring(x,y,z,r,r,4,2.8,ink)


def lamp(s, x, y, z, r, height, ink=EDGE):
    s.disk(x,y,z,r+2,r+2,3,DETAIL)
    s.disk(x,y,z+3,r,r,height-3,ink)
    s.ellipse(x,y,z+height,r*.55,r*.55,DETAIL)


def ring_upright(s, x, y, z, r, ink=EDGE):
    s.line([(a,y,b) for a,b in oval(x,z,r,r)],ink)


def wave(s,x,y,z,w,h,ink=EDGE,mode="tone"):
    profiles={
        "tone": (1,.56,.91), "soft": (.8,.84,.68), "rough": (.82,1.7,.91),
        "pulse": (1.3,.53,.25), "slow": (.64,.78,.35),
    }
    speed, decay, harmonics=profiles[mode]
    levels=[]
    for i in range(65):
        t=i/64
        a=2*t-1
        v=(sin(t*pi*6*speed)*.68+harmonics*sin(t*pi*17)*.27)*(1-min(1,abs(a)**decay))
        levels.append((x+w*t,y,z+v*h))
    s.line(levels,ink)


def tag(s, x, y, z, w=28, d=19, ink=EDGE):
    s.face([(x,y,z),(x+w-7,y,z),(x+w,y+d*.5,z),
            (x+w-7,y+d,z),(x,y+d,z)],ink)
    s.ellipse(x+w-7,y+d*.5,z,2,2,DETAIL)
    s.line([(x+4,y+d*.53,z),(x+w-12,y+d*.53,z)],DETAIL)


def gauge(s, x, y, z, r, angle=35, ink=EDGE):
    s.disk(x,y,z,r,r,5,ink)
    s.ellipse(x,y,z+5,r*.78,r*.78,DETAIL,start=35,end=307)
    for a in (45,95,145,195,245,295):
        dx,dy=cos(radians(a)),sin(radians(a))
        s.line([(x+dx*r*.66,y+dy*r*.66,z+5),(x+dx*r*.78,y+dy*r*.78,z+5)],DETAIL)
    ang=radians(angle)
    s.line([(x,y,z+5),(x+cos(ang)*r*.67,y+sin(ang)*r*.67,z+5)],BOLD)
    s.ellipse(x,y,z+5,r*.10,r*.10,EDGE)


def document(s,x,y,z,w=51,h=61,ink=EDGE):
    panel(s,x,y,z,w,h,4,ink)
    text_upright(s,x+7,y+4,z+h-13,[w*.61,w*.70,w*.54,w*.61,w*.42],7)


def picture(s,x,y,z,w,h,ink=EDGE,landscape="hills"):
    front=screen(s,x,y,z,w,h,ink)
    if landscape=="buildings":
        p=[(.12,.20),(.23,.20),(.23,.50),(.38,.50),(.38,.30),
           (.57,.30),(.57,.70),(.76,.70),(.76,.45),(.87,.45),(.87,.20)]
    elif landscape=="coast":
        p=[(.12,.24),(.24,.27),(.38,.51),(.51,.45),(.65,.58),(.88,.62)]
    else:
        p=[(.12,.27),(.39,.64),(.60,.34),(.69,.48),(.88,.24)]
    s.line([(x+u*w,front,z+v*h) for u,v in p],EDGE)
    ring_upright(s,x+w*.72,front,z+h*.70,min(w,h)*.065,DETAIL)


def lock(s,x,y,z,w=40,d=21,h=26,ink=EDGE):
    pts=[(a,y+d*.48,b) for a,b in oval(x+w*.5,z+h,w*.27,h*.64,0,180,24)]
    s.tube([(pts[0][0],pts[0][1],z+h*.8),*pts,
            (pts[-1][0],pts[-1][1],z+h*.8)],2.3,EDGE)
    box(s,(x,y,z),(w,d,h),ink,4)
    ring_upright(s,x+w*.5,y+d,z+h*.65,2.4,DETAIL)
    s.line([(x+w*.5,y+d,z+h*.61),(x+w*.5,y+d,z+h*.34)],DETAIL)


def key(s,x,y,z,ink=EDGE,form="step"):
    if form=="step":
        shape=[(0,-3.4),(25,-3.4),(25,-6),(31,-6),(31,-2),(37,-2),(37,3.4),(0,3.4)]
    elif form=="double":
        shape=[(0,-3.4),(17,-3.4),(17,-7),(22,-7),(22,-3.4),(29,-3.4),
               (29,-7),(35,-7),(35,3.4),(0,3.4)]
    else:
        shape=[(0,-4),(22,-4),(29,-7),(37,-4),(37,4),(0,4)]
    s.solid([(x+a,y+b) for a,b in shape],z,4,ink=ink,crease=False)
    ring(s,x,y,z,9,ink)


def gate(s,x,y,z,w=48,h=42,ink=EDGE):
    box(s,(x,y,z),(7,11,h),ink,2.3)
    box(s,(x+w-7,y,z),(7,11,h),ink,2.3)
    box(s,(x,y,z+h-6),(w,11,6),ink,2.3)


def block(s,x,y,z,w,d,h,ink=EDGE,r=4):
    box(s,(x,y,z),(w,d,h),ink,r)


def rail(s,x,y,z,w,d,ink=DETAIL):
    s.tube([(x,y,z),(x+w*.25,y,z),(x+w*.75,y+d,z),(x+w,y+d,z)],1.2,ink)


def stem(s,x,y,z,h,ink=DETAIL,r=1.2):
    s.tube([(x,y,z),(x,y,z+h)],r,ink)


def facewire(s,x,y,z,w,h,ink=DETAIL):
    bezel(s,x,y,z,w,h,ink,2)


def ridge(s,x,y,z,w,h,ink=EDGE):
    s.tube([(x,y,z),(x+w*.24,y,z+h*.5),(x+w*.61,y,z+h),(x+w,y,z+h*.36)],1.1,ink)


def stairs(s,x,y,z,w,d,step,h,ink=EDGE):
    n=int(step)
    outline=[]
    for i in range(n):
        u=x+i*w/n
        level=z+(i+1)*h/n
        outline.extend([(u,y,level),(u+w/n,y,level)])
    outline.extend([(x+w,y,z),(x,y,z)])
    s.face([(a,y-d,c) for a,_,c in outline],DETAIL)
    s.face(outline,ink)
    for idx in range(1,len(outline)-2,2):
        a,_,c=outline[idx]
        s.line([(a,y-d,c),(a,y,c)],DETAIL)


def ellipse(s,x,y,z,r,ry=-1,ink=DETAIL):
    s.ellipse(x,y,z,r,r if ry==-1 else ry,ink)


def port(s,x,y,z,w=11,h=6,ink=EDGE):
    bezel(s,x,y,z,w,h,ink,min(w,h)/4)


def barline(s,x,y,z,w,ink=DETAIL):
    s.line([(x,y,z),(x+w,y,z)],ink)


def side_line(s,x,y,z,d,ink=DETAIL):
    s.line([(x,y,z),(x,y+d,z)],ink)


def ghost(s,x,y,z,w,d):
    rectangle(s,x,y,z,w,d,GUIDE,4,True)


def outline(s,x,y,z,w,d,ink=EDGE):
    rectangle(s,x,y,z,w,d,ink,2)


def mount(s,x,y,z,w,d,ink=EDGE):
    tray(s,x,y,z,w,d,True,ink)
    rectangle(s,x+7,y+7,z+4,w-14,d-14,DETAIL,3)


def graph(s,x,y,z,w,h,levels,ink=EDGE,dots=False):
    vals=[int(t) for t in str(levels)]
    pts=[(x+w*i/(len(vals)-1),y,z+h*.11*n) for i,n in enumerate(vals)]
    s.line(pts,ink)
    if dots:
        for a,b,c in pts:
            ring_upright(s,a,b,c,1.55,ink)


def glyph(s, x, y, z, size, name, ink=EDGE):
    """Simple marks on upright surfaces for states that already have a literal symbol."""
    S=size
    if name=="check":
        check_upright(s,x-S*.5,y,z-S*.2,S,ink)
    elif name=="cross":
        s.line([(x-S*.36,y,z-S*.36),(x+S*.36,y,z+S*.36)],ink)
        s.line([(x-S*.36,y,z+S*.36),(x+S*.36,y,z-S*.36)],ink)
    elif name=="warning":
        s.line([(x,y,z+S*.62),(x-S*.58,y,z-S*.48),(x+S*.58,y,z-S*.48),(x,y,z+S*.62)],ink)
        s.line([(x,y,z+S*.26),(x,y,z-S*.12)],ink)
        s.line([(x,y,z-S*.25),(x,y,z-S*.28)],ink)
    elif name=="play":
        s.face([(x-S*.39,y,z-S*.5),(x-S*.39,y,z+S*.5),(x+S*.57,y,z)],ink)
    elif name=="plus":
        s.line([(x-S*.44,y,z),(x+S*.44,y,z)],ink)
        s.line([(x,y,z-S*.44),(x,y,z+S*.44)],ink)
    elif name=="minus":
        s.line([(x-S*.44,y,z),(x+S*.44,y,z)],ink)
    elif name=="left":
        s.line([(x+S*.3,y,z-S*.53),(x-S*.3,y,z),(x+S*.3,y,z+S*.53)],ink)
    elif name=="right":
        s.line([(x-S*.3,y,z-S*.53),(x+S*.3,y,z),(x-S*.3,y,z+S*.53)],ink)
    elif name=="eye":
        top = [(a,y,b) for a,b in oval(x,z,S*.62,S*.34,0,180,20)]
        bottom = [(a,y,b) for a,b in oval(x,z,S*.62,S*.34,180,360,20)]
        s.line(top+bottom,ink)
        ring_upright(s,x,y,z,S*.15,ink)
    else:
        raise ValueError(f"Unknown glyph {name}")


def concentric(s,x,y,z,r,count=3,ink=DETAIL):
    for i in range(int(count)):
        s.ellipse(x,y,z,r*(i+1)/count,r*(i+1)/count,ink)


def wirekeys(s,x,y,z,n=4,at=0):
    for i in range(int(n)):
        box(s,(x+16*i,y,z),(12,14,4),BOLD if i==at else EDGE,2.4)


def token(s,x,y,z,kind="disk",ink=EDGE,size=12):
    if kind=="disk":
        s.disk(x,y,z,size*.5,size*.5,5,ink)
        s.ellipse(x,y,z+5,size*.29,size*.29,DETAIL)
    elif kind=="square":
        box(s,(x-size*.5,y-size*.5,z),(size,size,5),ink,2.8)
    elif kind=="triangle":
        s.solid([(x-size*.55,y+size*.45),(x,y-size*.65),(x+size*.55,y+size*.45)],z,5,ink=ink)
    elif kind=="hex":
        corners=[(x+size*.56*cos(pi*i/3),y+size*.56*sin(pi*i/3)) for i in range(6)]
        s.solid(corners,z,5,ink=ink)
    elif kind=="plus":
        box(s, (x-size*.5,y-2.5,z),(size,5,4),ink,1.5)
        box(s, (x-2.5,y-size*.5,z+.5),(5,size,4),ink,1.5)
    else:
        raise ValueError(f"Unknown token type {kind}")


def slots(s,x,y,z,n=3,gap=11):
    for i in range(int(n)):
        rectangle(s,x+i*gap,y,z,5,21,DETAIL,2)


def orbit(s,x,y,z,r,ry=-1,ink=DETAIL,start=0,end=360,dashed=False):
    pts=[(a,b,z) for a,b in oval(x,y,r,r if ry==-1 else ry,start,end)]
    s.line(pts,ink,dashed=dashed)


def profile(s,x,y,z,w,h,kind="ramp",ink=EDGE):
    if kind=="ramp":
        pts=[(x,y,z),(x+w,y,z+h),(x+w,y,z)]
    elif kind=="mountain":
        pts=[(x,y,z),(x+w*.4,y,z+h),(x+w*.66,y,z+h*.24),(x+w,y,z+h*.69),(x+w,y,z)]
    elif kind=="valley":
        pts=[(x,y,z+h),(x+w*.30,y,z+h*.8),(x+w*.52,y,z+h*.2),(x+w*.75,y,z+h*.32),
             (x+w,y,z+h),(x+w,y,z),(x,y,z)]
    elif kind=="breaker":
        pts=[(x,y,z),(x+w*.29,y,z+h*.8),(x+w*.49,y,z+h*.6),(x+w*.60,y,z+h),
             (x+w*.67,y,z+h*.6),(x+w*.79,y,z+h*.64),(x+w,y,z)]
    else:
        raise ValueError(f"Unknown profile type {kind}")
    s.face(pts,ink)


def boxdoc(s,x,y,z,w,d):
    rectangle(s,x,y,z,w,d,DETAIL,1)
    lines(s,x+4,y+6,z,[w-8,w-11,w-8],6)


def sspool(s,x,y,z,r,h,ink=EDGE):
    s.disk(x,y,z,r+3,r+3,4,DETAIL)
    s.disk(x,y,z+4,r,r,h-8,ink)
    s.disk(x,y,z+h-4,r+3,r+3,4,ink)
    s.ellipse(x,y,z+h,r*.42,r*.42,DETAIL)


def terminal_lock(s,x,y,z,w,h):
    bezel(s,x,y,z,w,h,EDGE,3)
    ring_upright(s,x+w*.5,y,z+h*.61,2.4,DETAIL)
    s.line([(x+w*.5,y,z+h*.53),(x+w*.5,y,z+h*.28)],DETAIL)


def partition(s,x,y,z,w,d):
    rectangle(s,x,y,z,w,d,DETAIL,4)
    rectangle(s,x+4,y+4,z,w-8,d-8,DETAIL,3)
    s.ellipse(x+w*.5,y+d*.5,z,min(w,d)*.12,min(w,d)*.12,DETAIL)


def prompt(s,x,y,z,w):
    glyph(s,x+5,y,z,9,"right",BOLD)
    text_upright(s,x+16,y,z+1,(w*.65,),ink=EDGE)
    text_upright(s,x+2,y,z-14,(w*.72,w*.48),6)
    s.line([(x+w*.66,y,z-14),(x+w*.78,y,z-14)],BOLD)


def strip(s,x,y,z,w,d,ink=EDGE):
    sheet(s,x,y,z,w,d,ink,False)
    for i in range(3):
        p=x+w*(i+1)*.24
        side_line(s,p,y+4,z+2.2,d-8,DETAIL)


def plotbox(s,x,y,z,w,h,values,ink=EDGE):
    front=screen(s,x,y,z,w,h,ink)
    s.line([(x+9,front,z+h*.80),(x+9,front,z+10),(x+w-9,front,z+10)],DETAIL)
    graph(s,x+13,front,z+13,w-25,h*.53,values,BOLD)


def benchbar(s,x,y,z,w,d,h1,h2,h3,ink=EDGE):
    block(s,x,y,z,w,d,5,DETAIL,4)
    for i, h in enumerate((h1,h2,h3)):
        block(s,x+8+i*(w-16)/3,y+6,z+5,(w-24)/3,d-12,h,ink if i==1 else DETAIL,3)


def selection(s,x,y,z,w,h):
    for u,v,p,q in ((x,z,1,1),(x+w,z,-1,1),(x,z+h,1,-1),(x+w,z+h,-1,-1)):
        s.line([(u+p*6,y,v),(u,y,v),(u,y,v+q*6)],BOLD)


def dial_upright(s,x,y,z,r,ang,ink=EDGE):
    ring_upright(s,x,y,z,r,ink)
    for n in range(5):
        a=radians(40+n*65)
        s.line([(x+cos(a)*r*.72,y,z+sin(a)*r*.72),(x+cos(a)*r*.85,y,z+sin(a)*r*.85)],DETAIL)
    a=radians(ang)
    s.line([(x,y,z),(x+cos(a)*r*.66,y,z+sin(a)*r*.66)],BOLD)


def linkpath(s,x,y,z,x2,y2,z2,ink=DETAIL):
    s.line([(x,y,z),(x2,y2,z2)],ink)


def graduations(s,x,y,z,n,step):
    for i in range(n):
        linkpath(s,x,y,z+i*step,x+(6 if i%2==0 else 3),y,z+i*step,DETAIL)


def sampleprobes(s,x,y,z,w,h,values):
    vals=[int(t) for t in str(values)]
    for i,n in enumerate(vals):
        u=x+w*i/(len(vals)-1)
        guide(s,(u,y,z+h*.11*n),(u,y,84))
        ring_upright(s,u,y,z+h*.11*n,1.6,EDGE)


def matrix(s,x,y,z,a,b,gap):
    for i in range(a):
        for j in range(b):
            token(s,x+i*gap,y+j*gap,z,"disk", BOLD if (i,j)==(a-1,b-1) else DETAIL,9)


def arm(s,x,y,z,w,d,h,ink=EDGE):
    button(s,x,y,z,11,DETAIL)
    stem(s,x,y,z+3,h*.64,ink,2.4)
    p=(x,y,z+h*.64)
    q=(x+w*.45,y+d*.36,z+h)
    r=(x+w,y+d,z+h*.60)
    s.tube([p,q,r],3.4,ink)
    for u,v,vz in (q,r):
        s.disk(u,v,vz,3,3,2.5,DETAIL)
    s.tube([r,(r[0],r[1],r[2]-7)],1.4,BOLD)


def text_plate(s,x,y,z,w,h,ink=EDGE):
    front=screen(s,x,y,z,w,h,ink)
    text_upright(s,x+9,front,z+h*.72,[w*.67,w*.45,w*.58],h*.15)


def upright_audio(s,x,y,z,w,h,ink=EDGE):
    panel(s,x,y,z,w,h,6,ink)
    wave(s,x+w*.12,y+6,z+h*.53,w*.76,h*.64,BOLD,"pulse")


def grid(s,x,y,z,w,d,n=4,ink=DETAIL):
    rectangle(s,x,y,z,w,d,ink,1.6)
    for k in range(1,n):
        side_line(s,x+k*w/n,y,z,d,ink)
        barline(s,x,y+k*d/n,z,w,ink)


def cropbench(s,x,y,z,w,h,inner_w,inner_h,ink=EDGE):
    picture(s,x,y,z,w,h,ink,"hills")
    selection(s,x+(w-inner_w)/2,y+7,z+(h-inner_h)/2,inner_w,inner_h)


def waveform_comparison(s,x,y,z,w,h,kind0,kind1):
    face=screen(s,x,y,z,w,h,EDGE)
    wave(s,x+9,face,z+h*.70,w-18,h*.37,DETAIL,kind0)
    text_upright(s,x+8,face,z+h*.51,[w-16])
    wave(s,x+9,face,z+h*.31,w-18,h*.37,BOLD,kind1)


def picture_outline(s,x,y,z,w,h,ink=EDGE):
    s.face([(x,y,z),(x+w*.24,y,z+h*.62),(x+w*.52,y,z+h*.12),
            (x+w*.69,y,z+h*.43),(x+w,y,z),(x+w,y,z-h*.15),(x,y,z-h*.15)],ink)


def checktile(s,x,y,z,w,d,ink=EDGE):
    block(s,x,y,z,w,d,5,ink,3)
    check(s,x+w*.41,y+d*.58,z+5,min(w,d)*.38,BOLD)


def diagram(s,x,y,z,w,d,ink=EDGE):
    block(s,x,y,z,w,d,5,DETAIL)
    rail(s,x+15,y+11,z+5,w-28,d-23,ink)
    token(s,x+16,y+12,z+5,"disk",EDGE,12)
    token(s,x+w*.48,y+d*.52,z+5,"square",ink,14)
    token(s,x+w-15,y+d-13,z+5,"hex",EDGE,12)


def ruler(s,x,y,z,length,ink=EDGE):
    block(s,x,y,z,9,length,3,ink,1.5)
    for i in range(5,int(length)-2,6):
        barline(s,x+.5,y+i,z+3,5 if i%2 else 3,DETAIL)


def mesh_upright(s,x,y,z,w,h):
    for i in range(1,5):
        linkpath(s,x+w*i/5,y,z,x+w*i/5,y,z+h,GUIDE)
        linkpath(s,x,y,z+h*i/5,x+w,y,z+h*i/5,GUIDE)


def stencil(s,x,y,z,w,d,ink=EDGE):
    outline_pts=[(a,b,z) for a,b in rounded(x,y,w,d,4)]
    slots=[]
    for i in range(3):
        v=y+d*.15+i*d*.26
        slots.append([(a,b,z) for a,b in rounded(x+w*.14,v,w*(.75-i*.09),d*.14,2)])
    s.face(outline_pts,ink,openings=slots)


def shield(s,x,y,z,w,h,ink=EDGE):
    shape=[(x-w*.5,y,z+h*.15),(x-w*.5,y,z+h*.8),(x,y,z+h),
           (x+w*.5,y,z+h*.8),(x+w*.5,y,z+h*.15),(x,y,z-h*.07)]
    s.face([(a,b-4,c) for a,b,c in shape],DETAIL)
    s.face(shape,ink)
    s.line([(x-w*.35,y,z+h*.16),(x-w*.35,y,z+h*.71),(x,y,z+h*.85),
           (x+w*.35,y,z+h*.71),(x+w*.35,y,z+h*.16),(x,y,z+h*.08),(x-w*.35,y,z+h*.16)],DETAIL)


def shutter(s,x,y,z,w,h,ink=EDGE):
    front=screen(s,x,y,z,w,h,ink)
    for i in range(5):
        h0=z+h*.17+i*h*.16
        s.line([(x+8,front,h0),(x+w-8,front,h0)],DETAIL)


def tabs(s,x,y,z,n,w,d,space):
    for i in range(n):
        sheet(s,x+space*i,y+space*i*.6,z+4*i,w,d,BOLD if i==n-1 else DETAIL,True,True)


def radial_brackets(s,x,y,z,r,ink=DETAIL):
    for a in (30,120,210,300):
        s.ellipse(x,y,z,r,r,ink,a,a+43)


def map_plate(s,x,y,z,w,d,ink=EDGE):
    block(s,x,y,z,w,d,4,ink)
    s.line([(x+w*.05,y+d*.38,z+4),(x+w*.23,y+d*.31,z+4),(x+w*.33,y+d*.49,z+4),
            (x+w*.52,y+d*.30,z+4),(x+w*.79,y+d*.36,z+4),(x+w*.90,y+d*.23,z+4)],DETAIL)
    s.line([(x+w*.71,y+d*.08,z+4),(x+w*.61,y+d*.38,z+4),(x+w*.66,y+d*.67,z+4),
            (x+w*.56,y+d*.92,z+4)],DETAIL)


def ramp(s,x,y,z,w,d,h,ink=EDGE):
    # Draw the toe, grade, and top landing as one sloping plane.
    s.face([(x,y+d,z),(x+w,y+d,z+h),(x+w,y,z+h),(x,y,z)],ink)
    s.face([(x,y+d,z),(x+w,y+d,z+h),(x+w,y+d,z)],DETAIL)
    s.line([(x+2,y+d-5,z+h*2/w),(x+w-2,y+d-5,z+h*(w-2)/w)],DETAIL)


def clock(s,x,y,z,r,angle,ink=EDGE):
    s.disk(x,y,z,r,r,4,ink)
    s.ellipse(x,y,z+4,r*.78,r*.78,DETAIL)
    a=radians(angle)
    s.line([(x+cos(a)*r*.55,y+sin(a)*r*.55,z+4),(x,y,z+4),
            (x+r*.34,y-r*.09,z+4)],EDGE)


def microphone(s,x,y,z,h,ink=EDGE):
    button(s,x,y,z,10,DETAIL)
    stem(s,x,y,z+3,h*.7,ink,2)
    s.disk(x,y,z+h*.68,6,6,h*.33,ink)
    s.ellipse(x,y,z+h*1.01,4,4,DETAIL)


def speaker(s,x,y,z,w,h,ink=EDGE):
    panel(s,x,y,z,w,h,11,ink)
    ring_upright(s,x+w*.50,y+11,z+h*.40,min(w,h)*.27,DETAIL)
    ring_upright(s,x+w*.50,y+11,z+h*.74,min(w,h)*.12,DETAIL)


def fracture(s,x,y,z,w,d):
    s.line([(x,y,z),(x+w*.31,y+d*.36,z),(x+w*.19,y+d*.55,z),
            (x+w*.61,y+d*.66,z),(x+w*.49,y+d*.83,z),(x+w,y+d,z)],BOLD)


def text_system(s,x,y,z,w,h,rtl=False,ink=EDGE):
    front=screen(s,x,y,z,w,h,ink,True)
    x0=x+w-11 if rtl else x+11
    text_upright(s,x0,front,z+h-24,[w*.58,w*.71,w*.44],7,EDGE,rtl)


def wheelchair_sign(s,x,y,z,w,h,ink=EDGE):
    front=screen(s,x,y,z,w,h,ink)
    center_x=x+w*.47
    wheel_r=min(w,h)*.16
    wheel_z=z+h*.36
    s.line([(a,front,b) for a,b in oval(center_x,wheel_z,wheel_r,wheel_r,45,326,38)],ink)
    s.line([(x+w*.43,front,z+h*.68),(x+w*.49,front,z+h*.47),
            (x+w*.66,front,z+h*.47),(x+w*.73,front,z+h*.28),
            (x+w*.81,front,z+h*.28)],ink)
    ring_upright(s,x+w*.43,front,z+h*.77,wheel_r*.19,ink)


def corrected_image(s,x,y,z,w,h,skew,ink=EDGE):
    p=[(x,y,z),(x+w,y,z),(x+w+h*skew,y,z+h),(x+h*skew,y,z+h)]
    s.face(p,ink)
    def place(u,v):
        return x+u*w+v*h*skew,y,z+v*h
    for u0,u1,v in ((.1,.9,.15),(.1,.9,.82)):
        s.line([place(u0,v),place(u1,v)],DETAIL)
    s.line([place(.17,.16),place(.17,.46),place(.36,.46),place(.36,.16)],DETAIL)
    s.line([place(.48,.16),place(.48,.69),place(.70,.69),place(.70,.16)],ink)


def residual_plot(s,x,y,z,w,h,levels,ink=EDGE):
    face=screen(s,x,y,z,w,h,ink)
    vals=[int(t) for t in str(levels)]
    zero=z+h*.51
    s.line([(x+9,face,zero),(x+w-9,face,zero)],GUIDE,dashed=True)
    for i,v in enumerate(vals):
        u=x+12+i*(w-24)/max(1,len(vals)-1)
        vv=zero+h*.091*(v-5)
        s.line([(u,face,zero),(u,face,vv)],DETAIL)
        ring_upright(s,u,face,vv,2.2,BOLD if v in (1,9) else EDGE)


def eye_heat(s,x,y,z,w,h,ink=EDGE):
    front=screen(s,x,y,z,w,h,ink,True)
    x0=x+w*.39
    z0=z+h*.55
    for j in range(3):
        k=1-j*.23
        samples=[(a,front,c) for a,c in oval(x0+j*1.8,z0+j*1.6,w*.24*k,h*.25*k)]
        s.line(samples,BOLD if j==2 else DETAIL)
    for i in range(3):
        a=z+h*.34+i*h*.13
        barline(s,x+w*.65,front,a,w*.16,DETAIL)


def highlight_lens(s,x,y,z,w,h,ink=EDGE):
    front=screen(s,x,y,z,w,h,ink,True)
    for i in range(4):
        barline(s,x+10,front,z+h*(.28+i*.11),w*(.42+i%3*.13),BOLD if i==1 else DETAIL)
    center_x=x+w*.62
    center_y=y+21
    center_z=z+h*.54
    pts=[(u,center_y,v) for u,v in oval(center_x,center_z,12,12)]
    s.tube(pts,1.65,EDGE)
    s.tube([(center_x+8,center_y,center_z-8),(center_x+21,center_y,center_z-21)],2,ink)


def caption_ticks(s,x,y,z,w,h,ink=EDGE):
    front=screen(s,x,y,z,w,h,ink,False)
    wave(s,x+10,front,z+h*.70,w-20,h*.37,EDGE,"soft")
    baseline=z+h*.47
    barline(s,x+9,front,baseline,w-18,DETAIL)
    for idx in range(5):
        a=x+16+(w-32)*idx/4
        s.line([(a,front,baseline+3),(a,front,baseline-4)],DETAIL)
    p=x+20
    q=z+h*.16
    bezel(s,p,front,q,w*.53,h*.20,BOLD,2)
    barline(s,p+5,front,q+h*.10,w*.53-10,DETAIL)


def confusion_cells(s,x,y,z,w,d,ink=EDGE):
    block(s,x,y,z,w,d,5,DETAIL)
    cell_w=(w-34)/2
    cell_d=(d-24)/2
    for u,v,lift in ((0,0,18),(1,0,4),(0,1,6),(1,1,16)):
        left=x+10+u*(cell_w+7)
        top=y+8+v*(cell_d+6)
        block(s,left,top,z+5,cell_w,cell_d,lift,ink if u==v else DETAIL,3)
        pz=z+5+lift
        hatch_coords=[(left+7,top+7),(left+15,top+7),(left+7,top+14),(left+15,top+14)]
        for a,b in hatch_coords:
            s.line([(a,b,pz),(a+2.5,b,pz)],DETAIL)
    for i in (0,1):
        barline(s,x+12+i*(cell_w+7),y+d-3,z+5,cell_w*.50,EDGE)
        side_line(s,x+w-4,y+10+i*(cell_d+6),z+5,cell_d*.53,EDGE)


def signature_pen(s,x,y,z,w,d,ink=EDGE):
    s.tube([(x,y,z+2),(x+w*.15,y+d*.12,z+6),(x+w,y+d,z+8)],2.9,ink)
    s.line([(x-3,y-2,z+1),(x,y,z+2)],DETAIL)
    s.line([(x+w*.73,y+d*.73,z+9),(x+w*.94,y+d*.94,z+11)],DETAIL)


def distribution_row(s,x,y,z,shape,ink=EDGE):
    for i,h in enumerate(map(int,str(shape))):
        block(s,x+i*11,y,z,8,12,h*4+2,ink if h>5 else DETAIL,2)


def averaging_trace(s,x,y,z,w,h,ink=EDGE):
    face=screen(s,x,y,z,w,h,ink)
    raw=(2,5,3,6,4,3,8,5,7,5,7,4,6)
    averaged=[sum(raw[max(0,i-1):i+2])/len(raw[max(0,i-1):i+2]) for i in range(len(raw))]
    def points(vals):
        return [(x+10+i*(w-20)/(len(vals)-1),face,z+10+(h-18)*v/9) for i,v in enumerate(vals)]
    s.line(points(raw),DETAIL)
    s.line(points(averaged),BOLD)
    for a,b,c in points(averaged)[1::3]:
        ring_upright(s,a,b,c,1.9,BOLD)


def spectral_gate(s,x,y,z,w,h,ink=EDGE):
    face=screen(s,x,y,z,w,h,ink)
    zero=z+13
    heights=(9,14,18,12,21,16,62,18,10,15,9,17)
    for i,height in enumerate(heights):
        a=x+11+i*(w-22)/(len(heights)-1)
        s.line([(a,face,zero),(a,face,zero+height*.75)],BOLD if i==6 else DETAIL)
    s.line([(x+7,face,zero+16),(x+w-7,face,zero+16)],GUIDE,dashed=True)


def shuffle_grid(s,x,y,z,w,d,placements,ink=EDGE):
    block(s,x,y,z,w,d,4,DETAIL)
    grid(s,x+8,y+8,z+4,w-16,d-16,3,ink)
    for i,k in enumerate(map(int,str(placements))):
        u=x+8+(w-16)*(k%3+.5)/3
        v=y+8+(d-16)*(k//3+.5)/3
        token(s,u,v,z+4,"hex" if i%2 else "disk",ink,8)
