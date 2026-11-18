"""Scene grammar for explicit technical and accessibility situations."""

from geometry import BOLD, DETAIL, EDGE, GUIDE, oval
from scenes import systems_shapes as P

# Coordinate sizes keep overlap legible across composition formats. Each token
# describes a physical object, and each composition defines its relationship.
def object_at(s, kind, x, y, z, ink=EDGE):
    if kind in {"triangle","square","hex","disk","plus"}:
        P.token(s,x+21,y+17,z,kind,ink,29)
    elif kind == "manual":
        P.sheet(s,x,y,z,49,36,ink,False)
        for i in range(3):
            P.barline(s,x+7,y+8+i*7,z+2.2,14-i*2)
            P.barline(s,x+31,y+8+i*7,z+2.2,12-i)
        P.side_line(s,x+24,y+4,z+2.2,28,ink)
    elif kind == "terminal":
        P.screen(s,x,y,z,49,42,ink,True)
        P.prompt(s,x+8,y+7,z+21,31)
    elif kind == "speaker":
        P.speaker(s,x+3,y,z,35,43,ink)
    elif kind == "microphone":
        P.microphone(s,x+20,y+17,z,48,ink)
    elif kind == "chip":
        P.chip(s,x+2,y+4,z,43,27,8,ink,4)
    elif kind == "processor":
        P.chassis(s,x,y,z,49,35,13,ink,"sealed")
        P.chip(s,x+8,y+6,z+13,32,22,5,ink,3)
    elif kind == "cabinet":
        P.chassis(s,x+3,y,z,42,37,44,ink,"sealed")
        for i in range(3):
            P.port(s,x+7,y+37,z+4+i*12,34,8,DETAIL)
    elif kind in {"port","relay","drawer","drive","sealed","vault"}:
        if kind in {"port","relay"}:
            P.chassis(s,x,y,z,48,34,21,ink)
            if kind == "relay":
                P.toggle(s,x+12,y+8,z+21,True,ink)
                P.button(s,x+36,y+12,z+21,3,DETAIL)
        else:
            P.chassis(s,x,y,z,49,37,22,ink,"drawer" if kind in {"drawer","drive"} else "sealed")
            if kind=="drive":
                s.ellipse(x+24,y+18,z+22,14,11,DETAIL)
                P.button(s,x+24,y+18,z+22,3,ink)
            if kind=="vault":
                P.terminal_lock(s,x+12,y+37,z+5,25,12)
    elif kind == "plug":
        P.block(s,x+2,y+8,z,16,18,7,DETAIL,2)
        P.block(s,x+13,y+5,z,23,25,13,ink)
        P.rail(s,x+34,y+18,z+5,15,4,DETAIL)
        for i in range(3):
            P.barline(s,x+19,y+11+i*7,z+13,11)
    elif kind in {"note","template","plan","credit","receipt","photo_flat"}:
        if kind=="receipt":
            P.strip(s,x+5,y,z,31,45,ink)
            for i in range(5):
                P.barline(s,x+9,y+6+i*7,z+2.2,17-i%3*4)
        else:
            P.sheet(s,x,y,z,48,35,ink,kind=="note",kind=="template")
            if kind=="plan":
                P.grid(s,x+6,y+5,z+2.2,35,25,3,DETAIL)
                P.rail(s,x+8,y+8,z+3,26,14,ink)
            elif kind=="credit":
                P.outline(s,x+7,y+7,z+2.2,12,9,DETAIL)
                P.barline(s,x+26,y+27,z+2.2,16,ink)
            elif kind=="photo_flat":
                P.outline(s,x+4,y+4,z+2.2,40,27,DETAIL)
                s.line([(x+6,y+24,z+2.2),(x+17,y+11,z+2.2),(x+24,y+20,z+2.2),
                        (x+32,y+15,z+2.2),(x+42,y+24,z+2.2)],ink)
    elif kind in {"file","list","form","transcript"}:
        if kind=="file":
            P.document(s,x,y,z,48,46,ink)
        elif kind=="transcript":
            face=P.screen(s,x,y,z,48,47,ink)
            P.wave(s,x+5,face,z+33,37,11,ink,"pulse")
            P.text_upright(s,x+5,face,z+21,[27,32,20],5)
        else:
            face=P.screen(s,x,y,z,48,46,ink,True)
            for idx in range(3):
                a=z+22-7*idx
                if kind=="form":
                    P.bezel(s,x+7,face,a-2,8,5,DETAIL,1)
                    P.barline(s,x+20,face,a,18+idx%2*7,ink if idx==1 else DETAIL)
                else:
                    P.ring_upright(s,x+9,face,a,1.5,DETAIL)
                    P.barline(s,x+15,face,a,22+idx%2*9,ink if idx==1 else DETAIL)
    elif kind in {"photo","building","coast"}:
        P.picture(s,x,y,z,51,45,ink,{"photo":"hills","building":"buildings","coast":"coast"}[kind])
    elif kind == "projector":
        P.block(s,x,y,z,46,37,27,ink,5)
        P.ring_upright(s,x+14,y+37,z+12,7,ink)
        P.ring_upright(s,x+14,y+37,z+12,3,DETAIL)
        P.port(s,x+29,y+37,z+7,12,10,DETAIL)
    elif kind == "sensor":
        P.block(s,x+5,y+4,z,40,31,16,ink,5)
        P.ring(s,x+25,y+17,z+16,11,ink)
        P.concentric(s,x+25,y+17,z+20,6,2,DETAIL)
    elif kind == "meter":
        P.block(s,x+4,y+1,z,44,38,6,DETAIL)
        P.gauge(s,x+26,y+20,z+6,15,52,ink)
    elif kind == "ruler":
        P.ruler(s,x+16,y-4,z,45,ink)
        P.outline(s,x+7,y+4,z,30,31,DETAIL)
    elif kind == "clock":
        P.clock(s,x+22,y+18,z,18,128,ink)
    elif kind == "battery":
        P.chassis(s,x+4,y+7,z,44,27,17,ink,"sealed")
        P.block(s,x+1,y+14,z+5,5,11,7,ink,2)
        for i in range(3):
            P.side_line(s,x+15+i*8,y+13,z+17,13,DETAIL)
    elif kind == "beacon":
        P.lamp(s,x+24,y+18,z,13,34,ink)
    elif kind == "cooler":
        P.chassis(s,x,y,z,51,39,18,ink,"drawer")
        P.ring(s,x+25,y+20,z+18,14,ink)
        for a in range(0,360,90):
            pts=[(u,v,z+22) for u,v in oval(x+25,y+20,10,10,a,a+42,10)]
            s.line(pts,DETAIL)
    elif kind == "keyboard":
        P.block(s,x,y,z,49,35,6,ink)
        for v in range(3):
            for u in range(4):
                P.block(s,x+6+u*10,y+5+v*9,z+6,7,6,2,DETAIL,1)
    elif kind == "phone":
        P.screen(s,x+9,y,z,26,46,ink)
        P.barline(s,x+18,y+7,z+7,9,DETAIL)
    elif kind == "tablet":
        P.screen(s,x+2,y,z,43,41,ink,True)
        P.bezel(s,x+11,y+7,z+11,14,11,DETAIL,2)
        P.barline(s,x+30,y+7,z+25,9)
    elif kind in {"wave","pulse","spectrum","spark","scatter","quantile","bars","matrix","grid"}:
        front=P.screen(s,x,y,z,51,42,ink)
        if kind in {"wave","pulse"}:
            P.wave(s,x+6,front,z+20,39,18,ink,"soft" if kind=="wave" else "pulse")
        elif kind in {"spark","quantile"}:
            P.graph(s,x+6,front,z+6,39,26, "124637" if kind=="spark" else "124679",ink,False)
        elif kind in {"bars","spectrum"}:
            heights=(8,14,20,28) if kind=="bars" else (9,25,34,20,12)
            for idx,h in enumerate(heights):
                P.bezel(s,x+7+idx*8,front,z+7,5,min(h,26),ink if idx%2 else DETAIL,1)
        else:
            coords=((7,9),(14,16),(20,12),(21,24),(30,19),(36,27),(41,31)) if kind=="scatter" else tuple((8+u*9,8+v*8) for v in range(4) for u in range(4))
            for idx,(u,v) in enumerate(coords):
                P.ring_upright(s,x+u,front,z+v,1.25 if kind=="matrix" else 1.8,ink if idx%3==0 else DETAIL)
    elif kind == "spool":
        P.sspool(s,x+22,y+17,z,13,30,ink)
    elif kind == "archive":
        P.tray(s,x,y,z,49,38,False,ink)
        for i in range(3):
            P.panel(s,x+7,y+6+i*9,z+4,34,17+i*5,3,ink if i==2 else DETAIL)
        P.lip(s,x,y,z,49,38,ink)
    elif kind == "lens":
        P.ring(s,x+16,y+15,z,14,ink)
        s.tube([(x+25,y+19,z+2),(x+44,y+32,z+3)],2.9,DETAIL)
    elif kind == "tower":
        P.block(s,x+8,y+4,z,33,30,47,ink)
        P.bezel(s,x+13,y+34,z+6,23,32,DETAIL,2)
        P.port(s,x+17,y+34,z+20,13,7,ink)
    elif kind == "lock":
        P.lock(s,x+6,y+8,z,35,23,24,ink)
    elif kind in {"key","passkey"}:
        P.key(s,x+6,y+18,z,ink,"step" if kind=="key" else "double")
    elif kind in {"curtain","grille"}:
        if kind=="curtain":
            P.shutter(s,x,y,z,49,48,ink)
        else:
            P.gate(s,x,y,z,48,39,ink)
            for u in (12,23,34):
                P.stem(s,x+u,y+6,z+2,31,DETAIL)
    elif kind in {"shield","seal","credential"}:
        if kind=="shield":
            P.shield(s,x+24,y+17,z+5,41,46,ink)
        elif kind=="seal":
            P.ring(s,x+23,y+18,z,15,ink)
            P.check(s,x+17,y+24,z+4,15,ink)
        else:
            P.block(s,x+4,y+2,z,42,35,6,ink)
            s.ellipse(x+17,y+14,z+6,5,5,DETAIL)
            P.barline(s,x+24,y+13,z+6,12,DETAIL)
            P.barline(s,x+27,y+20,z+6,10,ink)
    elif kind in {"warning","approval","stop","eye","play"}:
        face=P.screen(s,x,y,z,49,37,ink)
        P.glyph(s,x+24,face,z+18,17,{"approval":"check","stop":"cross"}.get(kind,kind),ink)
    elif kind=="switch":
        P.block(s,x+4,y+8,z,39,24,7,ink)
        P.toggle(s,x+12,y+13,z+7,True,ink)
    elif kind == "wedge":
        P.ramp(s,x,y+3,z,48,30,18,ink)
    elif kind == "steps":
        P.stairs(s,x,y+30,z,47,26,3,24,ink)
    elif kind == "track":
        P.block(s,x-1,y+1,z,51,35,4,DETAIL)
        P.rail(s,x+5,y+8,z+4,36,18,ink)
        P.button(s,x+23,y+17,z+4,5,ink)
    elif kind == "bridge":
        P.block(s,x+3,y+5,z,7,27,27,DETAIL)
        P.block(s,x+39,y+5,z,7,27,27,DETAIL)
        P.block(s,x+1,y+4,z+26,47,29,4,ink)
    elif kind == "funnel":
        for i,r in enumerate((7,12,19)):
            P.ring(s,x+24,y+18,z+5+i*12,r,ink if i==2 else DETAIL)
    elif kind == "gridrack":
        P.tray(s,x,y,z,49,37,False,ink)
        P.grid(s,x+5,y+5,z+4,37,25,3,DETAIL)
        P.lip(s,x,y,z,49,37,ink)
    elif kind=="network":
        P.diagram(s,x,y,z,48,39,ink)
    elif kind=="tags":
        P.tag(s,x,y,z,37,21,DETAIL)
        P.tag(s,x+9,y+13,z+4,36,22,ink)
    elif kind=="calipers":
        P.gate(s,x,y+6,z,45,40,ink)
        P.graduations(s,x+11,y+17,z+7,5,5)
    elif kind=="glasses":
        P.ring(s,x+12,y+10,z,11,ink)
        s.tube([(x+22,y+12,z+2),(x+28,y+18,z+2)],1.8,DETAIL)
        P.ring(s,x+36,y+20,z,11,ink)
    elif kind=="earpiece":
        pts=[(a,y+12,c) for a,c in oval(x+24,z+13,18,28,0,180,24)]
        s.tube(pts,2.5,ink)
        P.block(s,x+2,y+6,z,10,12,15,DETAIL)
        P.block(s,x+38,y+6,z,10,12,15,DETAIL)
    elif kind=="stencil":
        P.stencil(s,x,y,z+2,48,32,ink)
    elif kind=="lever":
        P.button(s,x+13,y+12,z,9,DETAIL)
        s.tube([(x+13,y+12,z+3),(x+29,y+23,z+27)],2,ink)
        P.token(s,x+29,y+23,z+25,"hex",ink,12)
    elif kind=="capsule":
        P.block(s,x,y+4,z,47,26,20,ink,12)
        P.outline(s,x+10,y+10,z+20,27,13,DETAIL)
    elif kind=="gate_mark":
        P.gate(s,x+2,y+6,z,42,40,ink)
        P.token(s,x+23,y+14,z,"disk",DETAIL,12)
    elif kind == "frames":
        for i in range(3):
            P.panel(s,x+i*10,y+i*10,z+2*i,31,31,3,ink if i==2 else DETAIL)
            P.bezel(s,x+i*10+4,y+i*10+3,z+2*i+4,23,23,DETAIL,1.5)
    elif kind == "audio_clip":
        face=P.screen(s,x,y,z,48,34,ink)
        for i,h in enumerate((4,8,15,10,19,15,8,5)):
            P.linkpath(s,x+7+i*4.5,face,z+16-h*.45,x+7+i*4.5,face,z+16+h*.45,ink)
    elif kind=="outline_map":
        P.block(s,x,y,z,49,36,3,DETAIL)
        P.outline(s,x+4,y+4,z+3,41,26,DETAIL)
        s.line([(x+5,y+28,z+3),(x+12,y+14,z+3),(x+21,y+20,z+3),
                (x+28,y+9,z+3),(x+44,y+27,z+3)],ink)
    elif kind=="portrait":
        face = P.screen(s,x,y,z,45,49,ink)
        P.ring_upright(s,x+22,face,z+31,6,ink)
        s.line([(x+7,face,z+10),(x+11,face,z+17),(x+17,face,z+21),
                (x+28,face,z+21),(x+34,face,z+17),(x+38,face,z+10)],ink)
    elif kind=="pattern":
        P.sheet(s,x,y,z,45,37,ink,False)
        for u,v in ((11,10),(22,10),(33,10),(16,19),(27,19),(22,28)):
            s.ellipse(x+u,y+v,z+2.2,4.3,4.3,ink)
    elif kind == "map":
        P.map_plate(s,x,y,z,49,37,ink)
        P.arrow(s,x+39,y+23,z+4,36,15,DETAIL)
    elif kind == "balance":
        P.block(s,x+10,y+5,z,31,28,4,DETAIL)
        P.stem(s,x+24,y+19,z+4,28,ink,1.65)
        s.tube([(x+4,y+19,z+35),(x+44,y+19,z+30)],1.35,ink)
        s.line([(x+3,y+19,z+34),(x-5,y+19,z+19),(x+11,y+19,z+19),(x+3,y+19,z+34)],DETAIL)
        s.line([(x+44,y+19,z+30),(x+36,y+19,z+15),(x+52,y+19,z+15),(x+44,y+19,z+30)],DETAIL)
        P.ring(s,x+3,y+19,z+16,8,ink)
        P.ring(s,x+44,y+19,z+12,8,ink)
    elif kind=="railoff":
        P.rail(s,x+4,y+8,z+5,15,0,ink)
        P.rail(s,x+27,y+26,z+5,16,0,ink)
        P.button(s,x+19,y+8,z+3,4,DETAIL)
        P.button(s,x+27,y+26,z+3,4,DETAIL)
    else:
        raise ValueError(f"Unknown physical object: {kind}")


def _shape(s, kind, at, ink=EDGE):
    object_at(s,kind,*at,ink)


def composition(s, relationship, objects):
    def put(i,x,y,z,ink=EDGE):
        _shape(s,objects[i],(x,y,z),ink)

    if relationship == "exchange":
        P.rail(s,22,17,5,92,38,DETAIL)
        P.arrow(s,74,45,7,37,21,BOLD)
        put(0,-8,-3,0,EDGE)
        put(1,83,36,0,BOLD)
    elif relationship == "convert":
        P.block(s,0,8,0,141,66,5,DETAIL)
        P.rail(s,20,26,5,102,23,DETAIL)
        put(0,4,10,5,DETAIL)
        P.gate(s,54,30,5,34,42,EDGE)
        put(1,93,34,5,BOLD)
    elif relationship == "flow":
        P.rail(s,21,12,6,114,47,EDGE)
        P.arrow(s,68,36,4,26,16,DETAIL)
        P.arrow(s,120,57,4,26,16,DETAIL)
        put(0,0,-2,0,DETAIL)
        put(1,57,17,0,EDGE)
        put(2,114,39,0,BOLD)
    elif relationship == "compare":
        P.block(s,0,0,0,124,59,4,DETAIL)
        P.side_line(s,61,8,4,43,EDGE)
        P.barline(s,12,49,4,101,DETAIL)
        put(0,8,6,4,EDGE)
        put(1,69,11,4,BOLD)
    elif relationship == "bench":
        P.block(s,0,0,0,120,86,7,EDGE)
        P.rectangle(s,7,7,7,105,70,DETAIL,4)
        put(0,14,11,7,EDGE)
        put(1,64,30,7,BOLD)
        P.barline(s,13,70,7,38,DETAIL)
        P.barline(s,64,70,7,25,DETAIL)
    elif relationship == "lift":
        put(0,9,12,0,EDGE)
        P.guide(s,(14,19,6),(14,19,52))
        P.guide(s,(46,40,5),(46,40,54))
        put(1,15,17,55,BOLD)
    elif relationship == "gate":
        P.block(s,0,0,0,132,74,5,DETAIL)
        P.rail(s,13,47,5,98,8,EDGE)
        put(0,5,23,5,EDGE)
        P.gate(s,48,38,5,39,45,BOLD)
        put(1,81,35,5,DETAIL)
    elif relationship == "split":
        P.rail(s,24,37,4,63,-26,DETAIL)
        P.rail(s,26,37,4,65,41,EDGE)
        P.button(s,64,39,4,5,EDGE)
        put(0,2,12,0,BOLD)
        put(1,84,-10,0,DETAIL)
        put(2,85,66,0,EDGE)
    elif relationship == "merge":
        P.rail(s,18,12,4,88,35,DETAIL)
        P.rail(s,21,68,4,86,-21,EDGE)
        P.button(s,78,46,4,6,EDGE)
        put(0,0,-5,0,DETAIL)
        put(1,-1,54,0,EDGE)
        put(2,91,26,0,BOLD)
    elif relationship == "shelter":
        P.tray(s,4,5,0,89,65,False,DETAIL)
        put(0,24,18,4,BOLD)
        P.lip(s,4,5,0,89,65,EDGE)
        put(1,85,62,0,EDGE)
    elif relationship == "dock":
        P.tray(s,0,0,0,69,59,False,DETAIL)
        P.ghost(s,13,10,4,41,37)
        P.lip(s,0,0,0,69,59,EDGE)
        P.arrow(s,72,29,17,180,29,BOLD)
        put(0,78,5,13,BOLD)
        put(1,30,71,0,DETAIL)
    elif relationship == "index":
        P.tray(s,0,0,0,118,71,False,DETAIL)
        put(0,9,8,4,EDGE)
        put(1,58,20,4,DETAIL)
        P.lip(s,0,0,0,118,71,EDGE)
        put(2,26,53,38,BOLD)
        P.tag(s,87,83,0,28,17,DETAIL)
    elif relationship == "stations":
        P.block(s,0,0,0,146,67,5,DETAIL)
        P.barline(s,12,50,5,120,EDGE)
        for i in range(3):
            P.button(s,23+50*i,50,5,3,BOLD if i==1 else DETAIL)
            put(i,5+i*47,9,5,BOLD if i==1 else EDGE)
    elif relationship == "handover":
        put(0,-2,7,0,EDGE)
        put(2,97,51,0,EDGE)
        P.guide(s,(53,41,6),(53,41,32))
        P.guide(s,(75,60,6),(75,60,32))
        put(1,48,24,36,BOLD)
    elif relationship == "watched":
        P.rail(s,36,18,5,65,46,DETAIL)
        put(0,12,-4,0,EDGE)
        put(1,80,50,4,BOLD)
    elif relationship == "independent":
        P.block(s,0,0,0,121,72,4,DETAIL)
        P.rectangle(s,5,6,4,48,51,DETAIL,4)
        P.rectangle(s,65,12,4,50,51,DETAIL,4)
        put(0,6,7,4,EDGE)
        put(1,66,18,4,BOLD)
    elif relationship == "isolated":
        put(0,0,4,0,EDGE)
        P.rail(s,34,32,4,24,10,DETAIL)
        P.ring(s,79,53,0,24,GUIDE)
        put(1,56,38,0,BOLD)
        put(2,116,84,0,DETAIL)
    elif relationship == "protected":
        P.rail(s,24,23,4,88,40,DETAIL)
        put(0,4,1,0,DETAIL)
        P.shield(s,64,36,6,43,43,EDGE)
        put(1,91,52,0,BOLD)
    elif relationship == "outside":
        P.ghost(s,62,29,0,57,51)
        put(0,0,3,0,EDGE)
        P.arrow(s,91,23,5,45,21,BOLD)
        put(1,78,43,1,BOLD)
    elif relationship == "alignment":
        P.block(s,0,3,0,111,94,5,DETAIL)
        for x in (16,54,93):
            P.side_line(s,x,12,5,70,GUIDE)
        P.rail(s,14,48,6,79,0,DETAIL)
        put(0,10,12,5,EDGE)
        put(1,53,47,5,BOLD)
    elif relationship == "orbit":
        P.orbit(s,58,43,0,49,37,EDGE,0,360,False)
        put(0,30,17,1,BOLD)
        put(1,-6,52,0,DETAIL)
        put(2,89,52,0,EDGE)
    elif relationship == "feedback":
        P.orbit(s,62,43,0,54,39,DETAIL,14,333,False)
        P.arrow(s,106,23,2,90,10,BOLD)
        put(0,0,44,0,BOLD)
        put(1,75,21,0,EDGE)
    elif relationship == "relay":
        P.rail(s,20,17,8,107,28,DETAIL)
        put(0,0,0,0,EDGE)
        put(1,52,14,12,BOLD)
        put(2,108,43,0,EDGE)
    elif relationship == "inspect":
        P.block(s,0,0,0,106,75,5,DETAIL)
        put(0,14,9,5,EDGE)
        P.rectangle(s,10,8,5,54,42,DETAIL,4)
        P.guide(s,(41,33,10),(74,38,48))
        put(1,61,24,40,BOLD)
    elif relationship == "replace":
        P.block(s,0,0,0,124,66,5,DETAIL)
        P.ghost(s,12,16,5,44,35)
        P.arrow(s,64,32,12,180,20,EDGE)
        put(0,65,12,5,DETAIL)
        put(1,9,13,32,BOLD)
    elif relationship == "queue":
        P.block(s,1,15,0,127,59,5,DETAIL)
        P.barline(s,10,55,5,108,DETAIL)
        put(0,7,22,5,DETAIL)
        put(1,54,21,5,EDGE)
        put(2,104,10,5,BOLD)
    elif relationship == "boundary":
        P.block(s,0,0,0,129,72,5,DETAIL)
        P.shutter(s,43,22,5,30,50,EDGE)
        put(0,3,4,5,DETAIL)
        put(1,83,33,5,BOLD)
    elif relationship == "surface":
        P.block(s,0,0,0,112,86,5,EDGE)
        P.sheet(s,7,8,5,98,68,DETAIL,False)
        put(0,11,12,7,EDGE)
        put(1,53,41,7,BOLD)
    elif relationship == "elevation":
        P.block(s,0,0,0,117,79,5,DETAIL)
        P.block(s,60,11,5,51,44,23,DETAIL)
        P.stairs(s,12,45,5,48,31,3,23,EDGE)
        put(0,8,43,5,DETAIL)
        put(1,62,14,28,BOLD)
    elif relationship == "pivot":
        P.block(s,0,0,0,125,80,5,DETAIL)
        P.orbit(s,57,34,5,43,26,GUIDE,199,345,True)
        P.button(s,60,34,5,8,EDGE)
        P.rail(s,60,34,16,31,18,BOLD)
        put(0,3,6,5,DETAIL)
        put(1,79,40,5,BOLD)
    elif relationship == "conduit":
        P.block(s,0,0,0,124,68,5,DETAIL)
        P.rail(s,18,13,15,94,30,EDGE)
        put(0,5,2,5,EDGE)
        P.gate(s,50,23,5,26,36,DETAIL)
        put(1,87,31,5,BOLD)
    else:
        raise ValueError(f"Unknown relationship: {relationship}")
