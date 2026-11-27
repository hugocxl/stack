from geometry import oval
from scenes.redraws._sf import BACK, person, plate, screen

DESCRIPTION = "A large member token stands behind a small one, a mentor and the person they guide."


def token(s, at, u, v, r):
    plate(s, lambda a, b: at(u + a, v + b), oval(0, 0, r, r, count=72)[:-1], r*.22, BACK)
    person(s, at, u, v - r*.08, r*1.1)


def draw(s):
    at = screen()
    token(s, at, -12, 10, 36)
    token(s, at, 28, -20, 22)
