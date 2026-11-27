from geometry import DETAIL, EDGE
from scenes.redraws._sf import smooth

DESCRIPTION = "A road curves between two continuous guardrails on short posts."


def draw(s):
    mid = smooth([(-80, -10), (-30, -12), (10, 8), (60, 10), (90, 8)], 8)
    for off in (-24, 24):
        rail = [(x, y + off) for x, y in mid]
        for x, y in rail[::6]:
            s.tube([(x, y, 0), (x, y, 14)], 1.4, EDGE)
        s.tube([(x, y, 14) for x, y in rail], 2.6, EDGE)
    s.line([(x, y, 0) for x, y in mid], DETAIL, dashed=True)
