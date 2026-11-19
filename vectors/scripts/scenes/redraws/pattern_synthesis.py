from geometry import DETAIL, EDGE, rounded

DESCRIPTION = "Nine interlocking tiles repeat a small square motif across a square sheet."


def draw(s):
    height = 8
    border = rounded(0, 0, 96, 96, 3)
    s.solid(border, 0, height, crease=False)
    s.line([(x, y, height) for x, y in border + border[:1]], EDGE)
    interlock = [(0, 0), (0, 9), (-4, 9), (-7, 13), (-7, 19),
                 (-4, 23), (0, 23), (0, 32)]
    for seam in (32, 64):
        for start in (0, 32, 64):
            s.line([(seam + u, start + v, height) for u, v in interlock], EDGE)
            s.line([(start + v, seam + u, height) for u, v in interlock], EDGE)
    for x in (16, 48, 80):
        for y in (16, 48, 80):
            diamond = [(x - 6, y), (x, y - 6), (x + 6, y), (x, y + 6), (x - 6, y)]
            s.line([(u, v, height) for u, v in diamond], DETAIL)
