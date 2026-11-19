from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import loop, upright

DESCRIPTION = "A framed street scene shows neighboring buildings with a check badge at the lower-right corner."


def draw(s):
    width, height = 106, 66
    s.box(0, -3, 0, width, 3, height, 1.4)
    loop(s, rounded(6, 6, 94, 54, 2), EDGE)

    # A gabled house and a taller shop share a sidewalk.
    s.face(upright([(15, 22), (15, 41), (30, 54), (46, 41), (46, 22)]), EDGE)
    s.line(upright([(11, 37.5), (15, 41)]), EDGE)
    loop(s, [(26, 40), (34, 40), (34, 47), (26, 47)], DETAIL)
    s.line(upright([(25, 22), (25, 34), (34, 34), (34, 22)]), EDGE)

    s.face(upright([(46, 22), (46, 48), (84, 48), (84, 22)]), EDGE)
    s.face(upright([(43, 48), (87, 48), (87, 53), (43, 53)]), EDGE)
    for x in (52, 73):
        loop(s, rounded(x, 37, 7, 7, 1.5), DETAIL)
    s.line(upright([(57, 22), (57, 29), (59, 34), (65, 36),
                    (71, 34), (73, 29), (73, 22)]), EDGE)
    s.line(upright([(11, 22), (84, 22), (94, 16)]), EDGE)
    s.line(upright([(11, 15), (80, 15)]), DETAIL)

    badge(s, "check", 101, 2, 9, 15)
