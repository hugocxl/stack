from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w4 import Surface, front_surface

DESCRIPTION = "A tabletop tent menu shows three service entries down its upright face."


def draw(s):
    front = front_surface(s, angle=-34, y=20, z=4, lean=.38)
    back = Surface(s, lambda u, v: (
        front.at(u, v)[0] - (77-v)*.30,
        front.at(u, v)[1] - (77-v)*.45,
        front.at(u, v)[2],
    ))
    s.face([back.at(u, v) for u, v in rounded(0, 0, 64, 77, 2)], DETAIL)
    s.face([front.at(64, 0), back.at(64, 0), front.at(64, 77)])
    front.slab(rounded(0, 0, 64, 77, 3), 4)
    front.rows(10, 64, (43,), ink=EDGE)
    for v, width in ((49, 30), (32, 25), (15, 32)):
        front.oval(13, v, 2.6, 2.6, EDGE)
        front.rows(22, v + 2, (width,), ink=EDGE)
        front.rows(22, v - 4, (width * .68,))
