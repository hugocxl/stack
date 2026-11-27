from geometry import DETAIL
from scenes.redraws._kit import _screen, badge
from scenes.redraws._sf import BACK, bubble, plate, screen

DESCRIPTION = "A thick message bubble with two lines of text carries a reply badge at its corner."


def draw(s):
    at = screen()
    b = lambda u, v: at(u - 56, v - 36)
    plate(s, b, bubble(112, 76, 24, (.24, 14, 16)), 9, BACK)
    for v, w in ((50, 64), (34, 44)):
        s.line([b(22, v), b(22 + w, v)], DETAIL)
    badge(s, "back", *_screen(0, 0, 0, 56, 34), 14)
