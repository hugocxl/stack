from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import glyph

DESCRIPTION = "A sturdy hourglass holds a small admission ticket bearing a play symbol against its lower cap."


def draw(s):
    s.disk(0, 0, 0, 23, 18, 6)
    glass = [(21, 8), (19, 15), (12, 23), (4, 31), (3, 36),
             (4, 41), (12, 49), (19, 57), (21, 64)]
    front = [(x, 0, z) for x, z in glass]
    back = [(-x, 0, z) for x, z in reversed(glass)]
    s.face(front + back)
    s.line([(-16, 0, 12), (-8, 0, 14), (0, 0, 21), (8, 0, 14), (16, 0, 12)], DETAIL)
    s.line([(-14, 0, 57), (0, 0, 53), (14, 0, 57)], DETAIL)
    s.line([(0, 0, 31), (0, 0, 24)], DETAIL, dashed=True)
    for x, y in ((-18, 7), (18, -7)):
        s.tube([(x, y, 6), (x, y, 64)], 2.1)
    s.disk(0, 0, 63, 23, 18, 6)
    face = lambda x, z: (x, 13 - .20 * z, z)
    left = oval(17, 14, 3, 2.5, -90, 90, 12)
    right = oval(45, 14, 3, 2.5, 90, 270, 12)
    s.face([face(x, z) for x, z in [(17, 6), (45, 6), *reversed(right),
                                    (45, 22), (17, 22), *reversed(left)]], EDGE)
    glyph(s, "play", *face(31, 14), 8.5)
