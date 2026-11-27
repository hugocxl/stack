from geometry import BOLD, EDGE, oval
from scenes.redraws._sf import ground, plate, smooth, squircle

DESCRIPTION = "Two app tiles are joined by a thick cable with a connector seated in each."


def draw(s):
    for x, y in ((-70, -10), (26, 8)):
        top = ground(x, y, 12)
        plate(s, top, squircle(44, 44, 12), 12, (0, 0, -1))
    s.tube([(x, y, 14) for x, y in smooth([(-26, 12), (-10, 14), (6, 26), (26, 30)], 6)], 3.6, EDGE)
    for x, y in ((-30, 12), (30, 30)):
        s.disk(x, y, 12, 7, 7, 4)
    ta = ground(-70, -10, 12)
    s.line([ta(22 + a, 22 + b) for a, b in oval(0, 0, 9, 9, count=32)], BOLD)
    tb = ground(26, 8, 12)
    s.line([tb(u, v) for u, v in [(12, 32), (32, 32), (22, 13), (12, 32)]], BOLD)
