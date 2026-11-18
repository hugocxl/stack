from geometry import DETAIL
from scenes.redraws.public_route_accessibility import accessibility_symbol

DESCRIPTION = "An open doorway has a wheelchair plaque and a continuous floor through its threshold."


def draw(s):
    s.face([(9, -24, 0), (41, -24, 0), (41, 18, 0), (9, 18, 0)], DETAIL)
    s.box(40, -4, 0, 25, 8, 58, 1)
    s.box(0, -4, 0, 9, 8, 58, 1)
    s.box(0, -4, 57, 65, 8, 7, 1)

    # The door swings towards the viewer from the left jamb.
    hinge, edge = (8, 3), (13, 29)
    top, bottom = 55, 1.5
    for z in (bottom, top):
        s.face([(a, b, z) for a, b in (hinge, edge, (edge[0] + 3, edge[1]), (hinge[0] + 3, hinge[1]))])
    s.face([(edge[0], edge[1], bottom), (edge[0] + 3, edge[1], bottom),
            (edge[0] + 3, edge[1], top), (edge[0], edge[1], top)])
    s.face([(hinge[0] + 3, hinge[1], bottom), (edge[0] + 3, edge[1], bottom),
            (edge[0] + 3, edge[1], top), (hinge[0] + 3, hinge[1], top)])
    s.tube([(15.2, 24, 27), (19.2, 24, 27), (19.2, 20.5, 27)], 1.08)

    s.box(44, 4, 31, 17, 2, 18, 1.15)
    accessibility_symbol(s, 51.7, 6, 39.4, 13)
