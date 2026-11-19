from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge

DESCRIPTION = "A clock badge sits above an open loading bay with a raised dock and rolled-up door."


def draw(s):
    # Recessed floor and jamb are visible through the raised bay opening.
    s.face([(-38, -28, 0), (38, -28, 0), (38, 28, 0), (-38, 28, 0)], DETAIL)
    s.face([(-26, 9, 10), (26, 9, 10), (26, 28, 10), (-26, 28, 10)], EDGE)
    s.face([(-26, 9, 10), (26, 9, 10), (26, 9, 49), (-26, 9, 49)], DETAIL)
    s.face([(-26, 9, 10), (-26, 28, 10), (-26, 28, 49), (-26, 9, 49)], EDGE)
    s.face([(-38, -28, 69), (38, -28, 69), (38, 28, 69), (-38, 28, 69)], EDGE)
    s.face([(38, -28, 0), (38, 28, 0), (38, 28, 69), (38, -28, 69)], EDGE)

    front = [(-38, 0), (38, 0), (38, 69), (-38, 69)]
    opening = [(-26, 10), (26, 10), (26, 52), (-26, 52)]
    s.face([(x, 28, z) for x, z in front], EDGE,
           openings=([(x, 28, z) for x, z in opening],))
    # The canopy projects past the front wall to shelter backup trucks.
    s.face([(-43, -30, 70), (42, -30, 70), (42, 31, 70), (-43, 31, 70)], EDGE)
    s.face([(-43, 31, 66), (42, 31, 66), (42, 31, 70), (-43, 31, 70)], EDGE)
    s.face([(42, -30, 66), (42, 31, 66), (42, 31, 70), (42, -30, 70)], EDGE)
    s.line([(-25, 28, 10), (-17, 17, 10), (17, 17, 10), (25, 28, 10)], DETAIL)
    for z in (45, 49):
        s.line([(-26, 28, z), (26, 28, z)], DETAIL)
    s.line([(-26, 28, 43), (26, 28, 43)], EDGE)
    for x in (-25, 21):
        s.box(x, 28, 5, 4, 3, 7, .4)
    badge(s, "clock", 35, 19, 69, 14)
