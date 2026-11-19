from math import cos, sin, pi, radians
from geometry import BOLD, EDGE, DETAIL, oval, rounded


def security(s):
    # Draw the connected U section on each side of the shackle. The clear
    # opening remains transparent and the lock case hides both shackle feet.
    for y, ink in ((27, EDGE), (34, BOLD)):
        outer = [(x,y,z) for x,z in oval(62,59,30,30,0,180,52)]
        inner = [(x,y,z) for x,z in oval(62,59,21,21,180,0,48)]
        s.face([
            (92,y,38), *outer, (32,y,38),
            (41,y,38), *inner, (83,y,38),
        ], ink)
    s.box(21,12,0,82,46,48,7)

    # The shoulder of the keyway opens into the stem in the same cutout.
    head = [(x,58,z) for x,z in oval(62,25,5.5,5.5,310,590,42)]
    s.face([*head,(58.45,58,12),(65.55,58,12)], EDGE)


def permissions(s):
    def key(x, y, z, teeth):
        bow = oval(x,y,12,12,111,429,48)
        shaft = [(x+4.3,y+13)]
        for start, end, width in teeth:
            shaft.extend([(x+4.3,y+start),(x+width,y+start),
                          (x+width,y+end),(x+4.3,y+end)])
        shaft.extend([(x+4.3,y+40),(x+2.7,y+43),
                      (x-2.7,y+43),(x-4.3,y+40)])
        return [(px,py,z) for px,py in bow+shaft]

    s.box(1,2,0,136,77,8,7)
    keys = [(26,26,((27,34,10),)), (68,26,((17,22,10),(31,37,10))),
            (110,26,((20,25,9),(29,34,11)))]
    for x,y,teeth in keys:
        s.face(key(x,y,8,teeth), DETAIL)
        lift = 28 if x==68 else 4
        if x==68:
            for dy in (0,40):
                s.line([(x,y+dy,8),(x,y+dy,8+lift)], dashed=True)
        s.face(key(x,y,8+lift,teeth), EDGE)
        s.face(key(x,y,11+lift,teeth), BOLD if x==68 else EDGE)
        s.ellipse(x,y,11+lift,4.2,4.2, EDGE if x==68 else DETAIL)


def privacy(s):
    def front(points, y):
        return [(x,y,z) for x,z in points]

    s.box(0,5,0,115,31,68,6)
    s.face(front(rounded(8,8,99,52,6),36),DETAIL)
    s.line(front([(39,15),(99,15)],36),DETAIL)
    s.line(front([(39,53),(99,53)],36),DETAIL)
    s.line(front(oval(35,34,21,21),36),EDGE)
    s.line(front(oval(35,34,14,14),36),DETAIL)
    s.line(front(oval(35,34,7,7),36),EDGE)

    # The sliding tab masks a portion of the lens. Its profile and
    # orientation match the track on the camera housing.
    shutter = rounded(41,17.5,48,33,4)
    s.face(front(shutter,38),EDGE)
    s.face(front(shutter,41),BOLD)
    for x in (74,78,82):
        s.line(front([(x,28),(x,40)],41),DETAIL)


def identity(s):
    s.box(0,0,0,100,77,8,6)
    s.box(8,8,8,84,53,3,3)
    s.line([(82,69,8),(91,69,8)], EDGE)
    for x,y in ((8,8),(90,62)):
        s.line([(x,y,10),(x,y,28)],dashed=True)
    s.box(5,5,27,89,63,5,5,BOLD)
    s.face([(13,16,32),(42,16,32),(42,52,32),(13,52,32)],DETAIL)
    s.ellipse(27.5,28,32,5.8,5.8,EDGE)
    s.ellipse(27.5,44.5,32,10,8,EDGE,180,360)
    for y,w in ((23,26),(32,31),(41,17)):
        s.line([(52,y,32),(52+w,y,32)])
    s.dots(69,49,32,3,2,3)


def approvals(s):
    s.box(0,0,0,103,79,5,5)
    for y,w in [(12,69),(20,63),(28,55),(36,39),(44,34),(52,24)]:
        s.line([(10,y,5),(10+w,y,5)])
    s.ellipse(73,56,5,16,13,EDGE)
    s.line([(68,59,5),(76,62,5),(70,45,5)],BOLD)
    s.disk(71,30,27,23,21,9,BOLD)
    s.disk(71,30,36,8,8,23)
    s.solid(oval(71,30,15,13)[:-1],59,11,top=oval(71,30,17,15)[:-1])


def reliability(s):
    for x in (10,99):
        s.box(x-3,16,-6,31,35,6,4)
        s.box(x,19,0,25,29,31,4)
        s.box(x-2,15,31,29,37,7,3)
    s.box(1,12,37,132,14,8,3)
    s.box(1,45,37,132,14,8,3)
    for i in range(7):
        x = i*19
        s.box(x,0,45,17,71,7,3,BOLD if i==3 else EDGE)


def guardrails(s):
    s.box(0,0,0,130,63,5,4)
    s.box(1,0,5,128,6,15,3)
    s.line([(8,32,5),(121,32,5)], dashed=True)
    for x,y,h in ((13,22,8),(42,22,8),(72,31,19),(101,22,8)):
        s.box(x,y,5,17,17,h,3,BOLD if h==19 else EDGE)
    s.box(1,57,5,128,6,15,3)


def recovery(s):
    s.box(0,0,0,98,86,8,5)
    for z in (8,22):
        s.box(13,12,z,70,58,12,4)
    for x,y in [(25,23),(86,73)]:
        s.line([(x,y,34),(x,y,51)],dashed=True)
    s.box(22,19,51,70,58,12,5,BOLD)
    end_angle = 300
    s.ellipse(57,48,63,17,16,EDGE,32,end_angle)
    angle = radians(end_angle)
    x,y = 57+17*cos(angle),48+16*sin(angle)
    tx,ty = -sin(angle),cos(angle)
    s.line([(x-7*tx-5*ty,y-7*ty+5*tx,63),
            (x,y,63),(x-7*tx+5*ty,y-7*ty-5*tx,63)],EDGE)


def limits(s):
    s.disk(49,49,0,49,49,9)
    s.disk(49,49,10,42,42,8, BOLD)
    s.ellipse(49,49,18,35,35,DETAIL,5,275)
    for i in range(10):
        a = (5+i*30)*pi/180
        threshold = i==8
        start = 23 if threshold else 28
        s.line([(49+start*cos(a),49+start*sin(a),18),
                (49+34*cos(a),49+34*sin(a),18)],BOLD if threshold else DETAIL)
    s.line([(49,49,18),(40,25,18)],BOLD)
    s.disk(49,49,18,4,4,3)


def controls(s):
    s.box(0,0,0,103,79,9,6)
    for x,y,state in [(11,14,0),(55,14,1),(11,46,1),(55,46,0)]:
        s.box(x,y,9,37,19,3,8)
        s.disk(x+11+15*state,y+9.5,12,7,7,8 if state else 5,BOLD if x==55 and state else EDGE)
        s.line([(x+16,y-4,9),(x+21,y-4,9)])


FIGURES = [
    (security,"Security","A rounded shackle secures a solid lock body."),
    (permissions,"Permissions","Three key profiles fit specific slots, with one key lifted from its own slot."),
    (privacy,"Privacy","A physical shutter slides over a camera lens."),
    (identity,"Identity","A credential floats over its matching reader."),
    (approvals,"Approvals","A raised stamp is poised above an approval seal."),
    (reliability,"Reliability","A deck distributes weight across two supports."),
    (guardrails,"Guardrails","Two raised edges keep work inside a defined lane."),
    (recovery,"Recovery","A saved state rises from a stack of snapshots."),
    (limits,"Limits","A mechanical dial sets a usage threshold."),
    (controls,"Feature flags","Four toggles set independent options on a control panel."),
]
