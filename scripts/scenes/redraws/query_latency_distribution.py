
from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import coin, glyph
from scenes.redraws._w2 import chart_marker, front_bar

DESCRIPTION = "A stopwatch displays a binned response-time histogram across its face."


def draw(s):
    s.box(-8, -6, 74, 16, 12, 11, 2)
    s.box(-10, -7, 82, 20, 14, 5, 2)
    s.box(25, -5, 66, 9, 10, 8, 2)
    coin(s, 0, 0, 38, 38, depth=9)

    def p(x, z):
        return x, 0, z

    chart_marker(s, p, 0, 38, 33, DETAIL)
    glyph(s, "clock", 0, 0, 59, 9, EDGE)
    s.line([p(-24, 25), p(25, 25)], EDGE)
    for i, height in enumerate((8, 17, 23, 15, 9, 5)):
        x = -23 + i*8
        front_bar(s, p, x, 25.5, 7, height, BOLD if i == 2 else EDGE)
        s.line([p(x, 25), p(x, 21)], EDGE)
    s.line([p(25, 25), p(25, 21)], EDGE)
