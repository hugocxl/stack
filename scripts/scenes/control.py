from math import cos, sin, pi
from geometry import BOLD, EDGE, DETAIL


def security(s):
    for y in (28,38):
        for r in (23,30):
            points = [(62+r*cos(a*pi/36),y,65+r*sin(a*pi/36)) for a in range(37)]
            s.line([(62+r,y,43),*points,(62-r,y,43)], BOLD if y==38 else EDGE)
    s.box(22,12,0,80,43,49,7)
    s.line([(62,55,15),(62,55,28)])
    s.line([(62+6*cos(a*pi/24),55,32+6*sin(a*pi/24)) for a in range(49)],BOLD)


def permissions(s):
    for i,(x,y,w,h) in enumerate([(0,0,117,13),(9,10,99,16),(19,20,79,17),(30,30,57,25)]):
        z = (0,15,33,52)[i]
        s.box(x,y,z,w,w*.71,h,6,BOLD if i==3 else EDGE)
        s.dots(x+w*.4,y+w*.23,z+h,2+i,3)
    s.ellipse(58,50,77,11,10)


def privacy(s):
    for y,xs in [(0,(0,30,56)),(14,(8,31,79)),(28,(0,45,87))]:
        for x in xs:
            s.line([(x,y,3),(111 if x>70 else x+14,y,3)])
    s.box(7,37,0,99,12,69,5,BOLD)
    for z in range(10,64,7):
        s.line([(15,49,z),(98,49,z)])
    for x in (19,55,93):
        s.line([(x,50,3),(x,81,3)],dashed=True)


def identity(s):
    s.box(0,0,0,91,69,7,6)
    s.box(5,5,21,89,63,6,5,BOLD)
    for x,y in ((8,8),(90,62)):
        s.line([(x,y,7),(x,y,21)],dashed=True)
    s.ellipse(28,26,27,7,7,EDGE)
    s.ellipse(28,44,27,14,8,DETAIL,180,360)
    for y,w in ((21,28),(30,33),(39,19)):
        s.line([(52,y,27),(52+w,y,27)])
    s.dots(67,48,27,3,3,3)


def approvals(s):
    s.box(0,0,0,103,79,5,5)
    for y,w in [(12,69),(20,63),(28,55),(36,39),(44,34),(52,24)]:
        s.line([(10,y,5),(10+w,y,5)])
    s.ellipse(73,56,5,16,13,EDGE)
    s.ellipse(73,56,5,11,8)
    s.disk(71,30,27,23,21,9,BOLD)
    s.disk(71,30,36,8,8,23)
    s.disk(71,30,59,16,14,9)


def reliability(s):
    for x in (10,99):
        s.box(x-3,16,-6,31,35,6,4)
        s.box(x,19,0,25,29,39,4)
    for i in range(9):
        x = i*15
        s.box(x,0,39,13,68,8,3,BOLD if i==4 else EDGE)
    for y in (1,67):
        s.line([(0,y,48),(133,y,48)],EDGE)


def guardrails(s):
    s.box(0,0,0,130,63,5,4)
    s.box(0,0,5,130,6,20,3)
    for x in (10,39,68,97):
        s.box(x,19,5,19,19,14 if x==68 else 9,3,BOLD if x==68 else EDGE)
    s.box(0,57,5,130,6,20,3)
    for x in (11,44,77,110):
        s.line([(x,11,7),(x+14,11,7)],dashed=True)


def recovery(s):
    s.box(0,0,0,98,86,8,5)
    for z in (8,22):
        s.box(13,12,z,70,58,12,4)
    s.box(22,19,51,70,58,12,5,BOLD)
    s.ellipse(57,48,63,17,16,EDGE,30,319)
    s.line([(69,57,63),(72,47,63),(62,48,63)],EDGE)
    for x,y in [(25,23),(86,73)]:
        s.line([(x,y,34),(x,y,51)],dashed=True)


def limits(s):
    s.disk(49,49,0,49,49,9)
    s.disk(49,49,10,42,42,8, BOLD)
    s.ellipse(49,49,18,35,35,DETAIL,5,275)
    for i in range(10):
        a = (5+i*30)*pi/180
        s.line([(49+27*cos(a),49+27*sin(a),18),(49+33*cos(a),49+33*sin(a),18)])
    s.line([(49,49,18),(72,38,18)],BOLD)
    s.disk(49,49,18,4,4,3)


def controls(s):
    s.box(0,0,0,103,79,9,6)
    for x,y,state in [(11,14,0),(55,14,1),(11,46,1),(55,46,0)]:
        s.box(x,y,9,37,19,3,8)
        s.disk(x+11+15*state,y+9.5,12,7,7,8 if state else 5,BOLD if x==55 and state else EDGE)
        s.line([(x+16,y-4,9),(x+21,y-4,9)])


FIGURES = [
    (security,"Security","A rounded shackle secures a solid lock body."),
    (permissions,"Permissions","Four nested tiers narrow access to a protected resource."),
    (privacy,"Privacy","A screen obscures records and reveals only sparse outgoing traces."),
    (identity,"Identity","A credential floats over its matching reader."),
    (approvals,"Approvals","A raised stamp is poised above an approval seal."),
    (reliability,"Reliability","A deck distributes weight across two supports."),
    (guardrails,"Guardrails","Two raised edges keep work inside a defined lane."),
    (recovery,"Recovery","A saved state rises from a stack of snapshots."),
    (limits,"Limits","A mechanical dial sets a usage threshold."),
    (controls,"Feature flags","Four toggles set independent options on a control panel."),
]
