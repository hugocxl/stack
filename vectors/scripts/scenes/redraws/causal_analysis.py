from geometry import BOLD, EDGE, oval
from scenes.redraws._sf import BACK, bolt, chevron_arrow, plate, screen

DESCRIPTION = "A bold arrow leads from a trigger disc marked with a bolt to an effect disc marked with a target."


def draw(s):
    at = screen()
    a = lambda u, v: at(u - 60, v)
    plate(s, a, oval(0, 0, 22, 22, count=64)[:-1], 6, BACK)
    bolt(s, a, 12)
    b = lambda u, v: at(u + 60, v)
    plate(s, b, oval(0, 0, 22, 22, count=64)[:-1], 6, BACK)
    for r in (14, 7):
        s.line([b(u, v) for u, v in oval(0, 0, r, r, count=48)], BOLD if r == 7 else EDGE)
    plate(s, lambda u, v: at(u - 30, v), chevron_arrow(56, 7, 15), 4, BACK)
