from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w5 import rect

DESCRIPTION = "A thick tabbed record card with three ruled lines carries a padlock badge at its lower corner."


def draw(s):
    face = lambda x, z: (x, -.31 * z, z)
    outline = [(0, 0), (65, 0), (65, 42), (27, 42), (22, 50), (0, 50)]
    front = [face(x, z) for x, z in outline]
    back = [(x, y - 5, z) for x, y, z in front]
    s.face(back, EDGE)
    for a, b in ((1, 2), (2, 3), (3, 4), (4, 5)):
        s.face([front[a], back[a], back[b], front[b]], DETAIL)
    s.face(front, EDGE)
    rect(s, face, 8, 9, 13, 12, 1.5, DETAIL)
    s.line([face(8, 35), face(27, 35)], EDGE)
    for z, width in ((26, 31), (19, 23), (12, 16)):
        s.line([face(27, z), face(27 + width, z)], DETAIL)
    badge(s, "lock", *face(61, 12), 14)
