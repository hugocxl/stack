from geometry import BOLD, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w4 import closed_book, credential_mark

DESCRIPTION = "A bound case study pairs a customer credential with a rising results chart."


def draw(s):
    cover = closed_book(s, angle=-12, width=84, height=102, depth=12)
    credential_mark(cover, 15, 9, 26, 32)
    cover.oval(28, 26, 3.6, 3.6, EDGE)
    cover.rows(48, 18, (26,), ink=EDGE)
    cover.rows(48, 27, (22, 17), step=6)
    cover.frame(15, 46, 60, 41, 2, EDGE)
    cover.line([(22, 54), (22, 79), (67, 79)])
    arrow(s, [cover.at(u, v) for u, v in ((26, 74), (39, 65), (48, 68), (65, 53))],
          ink=BOLD, head=5)
