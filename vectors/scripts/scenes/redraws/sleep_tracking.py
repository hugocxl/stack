from geometry import DETAIL, EDGE
from scenes.redraws._kit import glyph
from scenes.redraws._sf import BACK, plate, screen as facing, squircle

DESCRIPTION = "A smartwatch shows a crescent moon above a stepped overnight sleep timeline."


class WatchFace:
    """The watch display, in the old screen coordinates (u from -18 to 18, v from 15 to 52)."""

    def __init__(self, s, at):
        self.s, self.at = s, at

    def line(self, points, ink=EDGE):
        self.s.line([self.at(u, v) for u, v in points], ink)


def smartwatch(s):
    """A viewer-facing smartwatch: rounded case, side crown, and straps above and below."""
    base = facing()
    at = lambda u, v: base(u, v - 33)
    for sign in (1, -1):
        strap = [(-14, 0), (14, 0), (13, 30), (-13, 30)]
        plate(s, lambda u, v, sign=sign: at(u, 33 + sign*(24 + v)), strap, 5, BACK, DETAIL)
    plate(s, lambda u, v: at(u + 25, v + 39), squircle(5, 9, 2), 5, BACK)
    case = [at(u - 25, v + 4) for u, v in squircle(50, 58, 15)]
    plate(s, lambda u, v: at(u - 25, v + 4), squircle(50, 58, 15), 10, BACK)
    glass = [at(u - 20, v + 9) for u, v in squircle(40, 48, 11)]
    s.line(glass + glass[:1], DETAIL)
    return WatchFace(s, at)


def draw(s):
    screen = smartwatch(s)
    glyph(s, "moon", *screen.at(-2, 40), 10)
    screen.line([(-13, 31), (-9, 31), (-9, 25), (-3, 25), (-3, 20),
                 (4, 20), (4, 27), (9, 27), (9, 31), (13, 31)], EDGE)
