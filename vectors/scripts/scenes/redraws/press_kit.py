from geometry import EDGE, rounded
from scenes.redraws._w4 import Surface, front_surface, landscape

DESCRIPTION = "A tabbed press folder holds a fact sheet and a photographic print in its front pocket."


def draw(s):
    angle = -22
    back = front_surface(s, angle=angle, y=-10, z=4, lean=.18)
    back.slab([(0, 0), (91, 0), (91, 67), (88, 72), (65, 72), (59, 59), (0, 59)], 4)
    fact_sheet = front_surface(s, angle=angle, y=-3, z=10, lean=.16)
    fact_sheet.slab(rounded(8, 0, 38, 65, 2), 3)
    fact_sheet.rows(14, 57, (24,), ink=EDGE)
    fact_sheet.rows(14, 48, (25, 19, 23), step=-6)
    print_face = front_surface(s, angle=angle, y=2, z=9, lean=.10)
    print_face.slab(rounded(48, 1, 37, 49, 2), 3)
    photo = Surface(s, lambda u, v: print_face.at(52 + u, 46 - v))
    landscape(photo, 0, 0, 29, 20)
    pocket = front_surface(s, angle=angle, y=10, z=4, lean=-.05)
    s.face([back.at(91, 0), back.at(91, 36), pocket.at(91, 35), pocket.at(91, 0)])
    pocket.slab([(0, 0), (91, 0), (91, 35), (74, 35), (69, 30),
                 (24, 30), (19, 35), (0, 35)], 4)
    pocket.rows(12, 10, (21,))
