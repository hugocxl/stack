from geometry import oval
from scenes.redraws._kit import _screen, badge
from scenes.redraws._sf import BACK, person, plate, screen

DESCRIPTION = "Three overlapping teammate tokens face the viewer, with one plus badge."


def token(s, u, v, r):
    at = screen()
    plate(s, lambda a, b: at(u + a, v + b), oval(0, 0, r, r, count=72)[:-1], r*.22, BACK)
    person(s, at, u, v - r*.08, r*1.1)


def draw(s):
    token(s, -40, 6, 25)
    token(s, 40, 6, 25)
    token(s, 0, 0, 32)
    badge(s, "plus", *_screen(0, 0, 0, 27, -24), 12)
