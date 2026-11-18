from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import cover_cap, pen_on, printed_check, sheet

DESCRIPTION = "A marked student worksheet has a mortarboard header, a teacher’s pencil and a star badge."


def draw(s):
    paper = sheet(s, 78, 90, rise=(-.4, .92))
    cover_cap(paper, 23, 68, 25)
    paper.rules(39, 66, [23], ink=EDGE)
    for v, width in ((48, 37), (34, 29), (20, 35)):
        printed_check(paper, 16, v, 6)
        paper.rules(27, v, [width], ink=EDGE)
    pen_on(paper, 50, 9, 46, pencil=True)
    badge(s, "star", *paper.point(72, 72), 13)
