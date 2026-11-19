from geometry import BOLD, EDGE, DETAIL, oval, rounded


def modular(s):
    for x,y,z,h in [(0,0,0,65),(52,0,0,43),(0,52,0,48),(52,52,0,27)]:
        s.box(x,y,z,46,46,9,5)
        s.box(x,y,z+12,46,46,h,5,BOLD if (x,y)==(0,52) else EDGE)
        s.dots(x+17,y+17,z+12+h,3,3)


def layers(s):
    for x,y in [(5,5),(90,5),(5,80),(90,80)]:
        s.line([(x,y,12),(x,y,81)], dashed=True)
    s.box(0,0,0,96,86,12,7)
    for x,y in [(12,12),(84,12),(12,74),(84,74)]:
        s.disk(x,y,12,3,3,5)
    s.box(0,0,37,96,86,5,6)
    s.box(32,27,42,32,32,7,4)
    for x in (15,73):
        for y in (21,35,49,63):
            s.line([(x,y,42),(x+8,y,42)])
    s.box(0,0,82,96,86,9,7,BOLD)
    rim = rounded(15,15,66,56,6)
    s.line([(*point,91) for point in [*rim,rim[0]]])
    s.dots(40,38,91,4,3,5)


def performance(s):
    heights = [12,16,24,37,55,79,106,127,92,65,42,26]
    for i,h in enumerate(reversed(heights)):
        s.box(0,i*9,0,112,4.6,h,2,BOLD if h==127 else EDGE)


def responsive(s):
    for x,y,w,h in ((9,0,116,87),(-1,32,66,59),(59,65,30,47)):
        phone = w==30
        s.box(x,y,0,w,7,h,4,BOLD if phone else EDGE)
        frame = rounded(x+4,5,w-8,h-10,2.8)
        s.line([(a,y+7,z) for a,z in [*frame,frame[0]]])
        s.line([(x+9,y+7,h-13),(x+w-9,y+7,h-13)])
        tile = min(w-18,32)
        inset = rounded(x+9,h-23-(11 if phone else 19),tile,11 if phone else 19,2.4)
        s.line([(a,y+7,z) for a,z in [*inset,inset[0]]])
        for index,fraction in enumerate((.88,.65)):
            at = h-(39 if phone else 52)-5*index
            s.line([(x+9,y+7,at),(x+9+tile*fraction,y+7,at)])


def customization(s):
    s.box(0,0,0,115,83,8,7)
    for i,position in enumerate([.77,.33,.63,.2]):
        x = 18 + i*25
        inset = rounded(x-1.5,11,3,60,1.5)
        s.line([(*p,8) for p in [*inset,inset[0]]],EDGE)
        for y in range(16,70,12):
            s.line([(x+6,y,8),(x+11,y,8)])
        y = 12 + 59*position
        s.box(x-6,y-5,8,12,10,9 if i==1 else 6,3,BOLD if i==1 else EDGE)


def integration(s):
    for offset in (0,12):
        points = []
        for step in range(33):
            t = step / 32
            y = 18 + offset + 40 * t * t * (3 - 2 * t)
            points.append((22 + 89*t, y, 12))
        s.tube(points,2.1,BOLD if offset==0 else DETAIL)
    s.box(14,11,7,20,27,10,3)
    s.box(99,51,7,20,27,10,3)
    s.box(-24,2,0,46,45,27,6)
    s.dots(-12,11,27,4,5)
    s.box(111,42,0,48,45,27,6,BOLD)
    s.dots(127,52,27,4,5)


def expansion(s):
    for row, widths in enumerate(((16,27,44),(10,18,28),(5,10,0))):
        for column,h in enumerate(widths):
            x,y = column*35,row*35
            if h:
                s.box(x,y,0,29,29,h,4)
            else:
                rim = rounded(x,y,29,29,4)
                s.line([(*point,0) for point in [*rim,rim[0]]],dashed=True)
                for a,b in ((x+3,y+3),(x+26,y+3),(x+3,y+26)):
                    s.line([(a,b,0),(a,b,20)],dashed=True)
                s.box(x,y,23,29,29,18,4,BOLD)
                s.dots(x+9,y+9,41,3,3)


def portability(s):
    s.box(0,0,0,104,71,28,9)
    s.box(0,0,29,104,71,8,9)
    for x in (12,79):
        s.box(x,68,21,13,4,13,2)
    handle = [(27,37,35)]
    handle.extend((x,37,z) for x,z in oval(38,53,11,11,180,90,14))
    handle.extend((x,37,z) for x,z in oval(66,53,11,11,90,0,14))
    handle.append((77,37,35))
    s.tube(handle,3.9,BOLD)


def accessibility(s):
    s.box(0,0,0,118,79,8,7)
    for x,y,w,d in ((12,12,44,15),(63,12,43,15),(12,38,26,29),(46,38,26,29),(80,38,26,29)):
        ring = rounded(x,y,w,d,4)
        s.line([(*point,8) for point in [*ring,ring[0]]],EDGE if x==46 else DETAIL)
    s.box(49,41,14,20,23,3,3,BOLD)
    s.line([(55,52,17),(63,52,17)],BOLD)


def extensibility(s):
    s.box(4,0,0,104,85,10,6)
    for x,y in [(12,12),(48,12),(84,12),(12,55),(48,55),(84,55)]:
        s.box(x,y,10,17,21,2,3,DETAIL)
    s.box(11,9,12,20,27,23,4)
    s.box(83,9,12,20,27,16,4)
    for x,y in ((49,57),(64,73)):
        s.line([(x,y,12),(x,y,48)],dashed=True)
    s.box(44,51,40,25,29,8,3,DETAIL)
    s.box(40,47,48,33,37,15,4,BOLD)
    s.dots(51,58,63,3,4)


FIGURES = [
    (modular,"Modular design","Four independent modules fit into one assembly."),
    (layers,"Product architecture","An exploded stack reveals a single layer above the platform."),
    (performance,"Fast performance","A tightly spaced pulse rises through a bank of thin fins."),
    (responsive,"Responsive design","Three screen sizes sit together in an isometric arrangement."),
    (customization,"Customization","Four sliders set independent levels on a single control surface."),
    (integration,"Integrations","A bundled connection joins two separate devices."),
    (expansion,"Scalability","A raised module extends a growing grid."),
    (portability,"Portability","A raised handle sits over a compact carrying case."),
    (accessibility,"Focus states","A raised control sits within a visible focus ring."),
    (extensibility,"Plugins","A raised cartridge lines up with an open slot on a baseboard."),
]
