from geometry import BOLD, DETAIL, EDGE

DESCRIPTION = "A single variance bar is divided into three differently patterned contributor segments."


def draw(s):
    s.box(0, 0, 0, 107, 31, 18, 3, BOLD)
    for x in (38, 80):
        s.line([(x, 0, 18), (x, 31, 18), (x, 31, 0)], EDGE)

    for x in (8, 18, 28):
        s.line([(x, 9, 18), (x + 4, 23, 18)], EDGE)
    for x in (49, 59, 69):
        for y in (10, 21):
            s.ellipse(x, y, 18, 1.9, 1.9, EDGE)
    for x in (90, 98):
        s.line([(x, 9, 18), (x, 22, 18)], EDGE)
    s.line([(0, 39, 0), (107, 39, 0)], DETAIL)
    for x in (0, 38, 80, 107):
        s.line([(x, 36, 0), (x, 42, 0)], EDGE)
