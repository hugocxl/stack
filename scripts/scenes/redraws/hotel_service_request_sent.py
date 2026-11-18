from geometry import BOLD, DETAIL
from scenes.redraws._kit import badge
from scenes.redraws._w5 import bell_mark

DESCRIPTION = "A hotel service bubble shows a front-desk bell and carries an outward arrow at its lower edge."


def draw(s):
    outline = [(0, 19), (0, 52), (5, 57), (57, 57), (62, 52), (62, 19),
               (57, 14), (26, 14), (14, 3), (14, 14), (5, 14)]
    s.face([(x, -5, z) for x, z in outline], DETAIL)
    s.face([(x, 0, z) for x, z in outline])
    bell_mark(s, lambda x, z: (x, 0, z), 30, 34, 1.15, BOLD)
    badge(s, "arrow", 62, 5, 17, 14.5)
