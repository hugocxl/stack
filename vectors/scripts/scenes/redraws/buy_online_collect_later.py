from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge

DESCRIPTION = "A clock badge overlaps the upper-right corner of a parcel locker whose open door reveals a package."


def draw(s):
    # The front surround clips the back wall, shelf and parcel to the opening.
    s.face([(-30, -20, 0), (30, -20, 0), (30, -20, 78), (-30, -20, 78)], EDGE)
    s.face([(-24, -20, 24), (24, -20, 24), (24, 0, 24), (-24, 0, 24)], DETAIL)
    s.box(-12, -12, 24, 22, 11, 15, 1)
    s.line([(-2, -12, 39), (-2, -1, 39), (-2, -1, 33)], DETAIL)
    s.face([(-30, -20, 78), (30, -20, 78), (30, 0, 78), (-30, 0, 78)], EDGE)
    s.face([(30, -20, 0), (30, 0, 0), (30, 0, 78), (30, -20, 78)], EDGE)
    opening = [(-24, 0, 24), (24, 0, 24), (24, 0, 54), (-24, 0, 54)]
    surround = [(-30, 0, 0), (30, 0, 0), (30, 0, 78), (-30, 0, 78)]
    s.face(surround, EDGE, openings=[opening])
    for bottom, height in ((5, 15), (58, 15)):
        door = rounded(-24, bottom, 48, height, 1.5)
        s.line([(x, .01, z) for x, z in door + door[:1]], DETAIL)
        s.line([(11, .01, bottom + 7), (19, .01, bottom + 7)], EDGE)

    s.face([(-24, 0, 24), (-12, 46, 24), (-12, 46, 54), (-24, 0, 54)], EDGE)
    s.line([(-14, 38, 34), (-14, 38, 41)], DETAIL)
    for height in (28, 49):
        s.line([(-27, .01, height), (-24, 0, height), (-22.5, 5.75, height)], EDGE)
    badge(s, "clock", 30, 0, 78, 13)
