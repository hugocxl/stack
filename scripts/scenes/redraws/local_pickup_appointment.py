from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import Surface

DESCRIPTION = "A parcel sits inside a pickup locker with a clock badge on the collection compartment."


def pickup_locker(s, *, collection=False):
    """A two-column parcel locker with a narrow electronic access panel."""
    width, depth, height = 76, 34, 80
    front = Surface(s, lambda u, v: (u, depth, v))
    opening = [(35, 45), (61, 45), (61, 72), (35, 72)]
    if collection:
        s.face([(35, 14, 45), (61, 14, 45), (61, 14, 72), (35, 14, 72)], DETAIL)
        s.line([(35, 14, 45), (35, depth, 45)], DETAIL)
        s.box(38, 23, 46, 16, 10, 15, 1)
        s.line([(46, 24, 61), (46, 33, 61), (46, 33, 54)], DETAIL)

    s.face([(0, 0, height), (width, 0, height), (width, depth, height), (0, depth, height)])
    s.face([(width, 0, 0), (width, depth, 0), (width, depth, height), (width, 0, height)])
    holes = [[front.at(*p) for p in opening]] if collection else []
    s.face([front.at(*p) for p in [(0, 0), (width, 0), (width, height), (0, height)]],
           openings=holes)
    front.line([(66, 0), (66, 80)], DETAIL)
    for x in (5, 35):
        for z in (7, 45):
            if collection and (x, z) == (35, 45):
                continue
            selected = not collection and (x, z) == (35, 7)
            front.frame(x, z, 26, 27, 1.6, EDGE if selected else DETAIL)
            front.rows(x + 17, z + 13, (5,), ink=EDGE if selected else DETAIL)
    front.frame(68.5, 43, 5, 13, 1.3)
    for z in (36, 39):
        front.rows(70, z, (2,))
    return front


def draw(s):
    front = pickup_locker(s, collection=True)
    x, y, z = front.at(76, 77)
    badge(s, "clock", x, y - 7, z, 13)
