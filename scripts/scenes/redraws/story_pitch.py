from geometry import BOLD, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import paper

DESCRIPTION = "A short manuscript peeks out of an open mailing envelope with a send badge."


def draw(s):
    mail = paper(s, 87, pitch=.75, run=.58, angle=6, depth=7)
    mail.slab([(0, 45), (54, 14), (108, 45), (108, 87), (0, 87)], 7)
    mail.slab(rounded(19, 0, 70, 71, 3), 3)
    mail.rows(29, 12, (44,), ink=BOLD)
    mail.rows(29, 22, (48, 43, 34), step=7)
    s.face([mail.at(u, v) for u, v in [(0, 45), (54, 68), (108, 45), (108, 87), (0, 87)]])
    mail.line([(0, 87), (35, 60)], EDGE)
    mail.line([(108, 87), (73, 60)], EDGE)
    badge(s, "arrow", *mail.at(103, 73), 16)
