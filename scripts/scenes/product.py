from geometry import BOLD, EDGE, DETAIL


def modular(s):
    for x,y,z,h in [(0,0,0,65),(52,0,0,43),(0,52,0,48),(52,52,0,27)]:
        s.box(x,y,z,46,46,9,5)
        s.box(x,y,z+12,46,46,h,5,BOLD if (x,y)==(0,52) else EDGE)
        s.dots(x+17,y+17,z+12+h,3,3)


def layers(s):
    for x,y in [(0,0),(88,0),(0,78),(88,78)]:
        s.line([(x+4,y+4,30),(x+4,y+4,85)], dashed=True)
    for z in [0,15,30,69]:
        s.box(0,0,z,96,86,13,6,BOLD if z==69 else EDGE)
    s.ellipse(48,43,82,23,22)
    s.ellipse(48,43,82,16,14)
    s.dots(46,41,82,2,2,4,BOLD)


def performance(s):
    heights = [12,16,24,37,55,79,106,127,92,65,42,26]
    for i,h in enumerate(reversed(heights)):
        s.box(0,i*9,0,112,4.6,h,2,BOLD if h==127 else EDGE)


def responsive(s):
    s.box(3,0,0,113,8,88,5)
    s.face([(10,8,7),(109,8,7),(109,8,80),(10,8,80)],DETAIL)
    s.line([(18,8,70),(95,8,70)])
    s.box(-3,23,0,69,8,59,5)
    s.face([(3,31,6),(60,31,6),(60,31,53),(3,31,53)],DETAIL)
    s.box(51,54,0,30,7,49,4,BOLD)
    s.line([(60,61,43),(73,61,43)])
    s.line([(61,61,6),(72,61,6)])


def customization(s):
    s.box(0,0,0,115,83,8,7)
    for i,position in enumerate([.77,.33,.63,.2]):
        x = 18 + i*25
        s.line([(x,11,8),(x,71,8)])
        for y in range(14,70,7):
            s.line([(x+4,y,8),(x+8,y,8)])
        y = 12 + 59*position
        s.box(x-6,y-5,8,12,10,9 if i==1 else 6,3,BOLD if i==1 else EDGE)


def integration(s):
    for z in (7,21):
        s.line([(0,29,z),(32,29,z),(68,65,z),(103,65,z)], BOLD if z==21 else DETAIL)
        s.line([(0,36,z),(29,36,z),(64,72,z),(103,72,z)])
    s.box(-11,5,0,40,51,30,6)
    s.box(15,17,30,13,28,5,3)
    s.dots(-3,18,30,3,4)
    s.box(83,47,0,43,52,33,6,BOLD)
    s.box(84,56,33,13,27,5,3)
    s.dots(106,61,33,3,4)


def expansion(s):
    tiles = [(0,0,18,8),(33,0,20,8),(0,33,24,8),(33,33,40,12),(66,0,0,8),
             (0,66,0,8),(66,33,25,8),(33,66,22,12),(66,66,26,34)]
    for x,y,h,lift in tiles:
        s.box(x,y,0,28,28,8,3)
        if not h:
            continue
        if lift>12:
            for a,b in [(x+2,y+2),(x+26,y+26)]:
                s.line([(a,b,8),(a,b,lift)],dashed=True)
        s.box(x,y,lift,28,28,h,4,BOLD if lift>12 else EDGE)
        if lift>12: s.dots(x+9,y+9,lift+h,3,3)


def portability(s):
    s.box(0,0,0,108,72,15,8)
    for x in (13,73):
        s.box(x,52,15,14,12,38,3)
    s.box(13,52,53,74,12,10,4,BOLD)
    s.box(10,9,15,82,34,11,4)
    s.dots(20,17,26,7,3,5)


def accessibility(s):
    for i,(w,d,h) in enumerate([(99,91,12),(89,79,10),(76,67,9),(62,56,11)]):
        s.box((100-w)/2,(96-d)/2,i*12,w,d,h,6,BOLD if i==3 else EDGE)
    for i in range(3):
        s.ellipse(50,48,47,8+i*6,5+i*6,EDGE if i==0 else DETAIL)
    s.disk(50,48,47,2,2,2,BOLD)


def extensibility(s):
    s.box(4,0,0,104,85,10,6)
    for x,y in [(12,12),(48,12),(84,12),(12,55),(48,55),(84,55)]:
        s.box(x,y,10,17,21,4,3)
    for x,y,z,h in [(38,6,15,37),(74,6,15,25),(38,49,37,28)]:
        if z>15:
            s.line([(x+2,y+2,14),(x+2,y+2,z)],dashed=True)
            s.line([(x+29,y+31,14),(x+29,y+31,z)],dashed=True)
        s.box(x,y,z,31,33,h,5,BOLD if z>15 else EDGE)
        s.dots(x+9,y+10,z+h,3,3)


FIGURES = [
    (modular,"Modular design","Four independent modules fit into one assembly."),
    (layers,"Product architecture","An exploded stack reveals a single layer above the platform."),
    (performance,"Fast performance","A tightly spaced pulse rises through a bank of thin fins."),
    (responsive,"Responsive design","Three screen sizes sit together in an isometric arrangement."),
    (customization,"Customization","Four sliders set independent levels on a single control surface."),
    (integration,"Integrations","A bundled connection joins two separate devices."),
    (expansion,"Scalability","A raised module extends a growing grid."),
    (portability,"Portability","A raised handle sits over a compact carrying case."),
    (accessibility,"Focus states","Concentric rings mark the active surface of a stepped control."),
    (extensibility,"Plugins","A raised cartridge lines up with an open slot on a baseboard."),
]
