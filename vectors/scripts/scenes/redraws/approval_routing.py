from geometry import EDGE
from scenes.redraws._kit import _screen, badge
from scenes.redraws._sf import BACK, plate, screen, squircle

DESCRIPTION = "A decision diamond splits a flow into two paths, and the approving path carries a check badge."


def draw(s):
    at = screen()
    s.tube([at(-80, 0), at(-26, 0)], 2.2, EDGE)
    s.tube([at(0, 26), at(0, 44), at(56, 44)], 2.2, EDGE)
    s.tube([at(0, -26), at(0, -44), at(56, -44)], 2.2, EDGE)
    plate(s, at, [(0, -28), (28, 0), (0, 28), (-28, 0)], 8, BACK)
    plate(s, lambda u, v: at(u - 90, v - 10), squircle(20, 20, 5), 5, BACK)
    badge(s, "check", *_screen(0, 0, 0, 68, 44), 13)
    badge(s, "x", *_screen(0, 0, 0, 68, -44), 13)
