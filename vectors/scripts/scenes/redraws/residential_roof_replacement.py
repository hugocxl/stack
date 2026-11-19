from geometry import DETAIL, EDGE
from scenes.redraws._kit import arrow

DESCRIPTION = "A staggered shingle panel descends toward the exposed front slope of a gabled roof."


def draw(s):
    s.box(-34, -24, 0, 68, 48, 34, 1)
    s.face([(34, -24, 34), (34, 24, 34), (34, 0, 55)])
    s.face([(-36, -26, 34), (36, -26, 34), (36, 0, 55), (-36, 0, 55)])
    s.line([(-34, 0, 55), (34, 0, 55)], EDGE)
    for x in (-32, -12, 10, 32):
        s.line([(x, 0, 55), (x, 24, 34)], DETAIL)
    s.line([(-29, 24, 0), (-29, 24, 23), (-13, 24, 23), (-13, 24, 0)], EDGE)
    s.face([(5, 24.1, 11), (23, 24.1, 11), (23, 24.1, 23), (5, 24.1, 23)])
    s.line([(14, 24.2, 11), (14, 24.2, 23)], DETAIL)

    def roof(x, y):
        return x, y, 71 - y*.80

    for x in (-25, 24):
        arrow(s, [(x, 24, 47), (x, 24, 36)], EDGE, head=4)
    panel = [roof(-36, 0), roof(36, 0), roof(36, 26), roof(-36, 26)]
    s.face(panel)
    s.face([panel[2], panel[3], (-36, 26, panel[3][2] - 3), (36, 26, panel[2][2] - 3)])
    for row, y in enumerate((6, 13, 20)):
        s.line([roof(-36, y), roof(36, y)], DETAIL)
        for x in ((-18, 4, 25) if row % 2 else (-25, -4, 17)):
            s.line([roof(x, y), roof(x, y + 6.6)], DETAIL)
