from geometry import DETAIL, EDGE, oval
from scenes.redraws._sf import BACK, plate, screen, smooth

DESCRIPTION = "Two branch lines with commit nodes curve together into one larger merge commit."


def node(s, at, u, v, r):
    plate(s, lambda a, b: at(u + a, v + b), oval(0, 0, r, r, count=48)[:-1], r*.4, BACK)


def draw(s):
    at = screen()
    s.tube([at(u, 0) for u in (-70, 70)], 2.6, EDGE)
    s.tube([at(u, v) for u, v in smooth([(-70, 40), (-20, 40), (8, 26), (28, 0)], 8)], 2.6, EDGE)
    for u, v in ((-60, 0), (-28, 0), (-60, 40), (-26, 40)):
        node(s, at, u, v, 8)
    node(s, at, 30, 0, 14)
    node(s, at, 64, 0, 8)
