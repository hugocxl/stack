from geometry import BOLD, DETAIL, oval
from scenes.redraws._kit import _strokes
from scenes.redraws._sf import BACK, plate, screen, squircle

DESCRIPTION = "A plus sign joins a Command keycap and a left-arrow keycap in a keyboard chord."


def key(s, at):
    plate(s, at, squircle(52, 52, 12), 12, BACK)
    inner = [at(u + 5, v + 7) for u, v in squircle(42, 42, 9)]
    s.line(inner + inner[:1], DETAIL)
    return lambda u, v: at(26 + u, 28 + v)


def draw(s):
    at = screen()
    c = key(s, lambda u, v: at(u - 84, v - 26))
    k = 6
    s.line([c(-k, -k), c(k, -k), c(k, k), c(-k, k), c(-k, -k)], BOLD)
    for sx, sy in ((-1, -1), (1, -1), (1, 1), (-1, 1)):
        s.line([c(sx*(k + 4) + a, sy*(k + 4) + b) for a, b in oval(0, 0, 4, 4, 0, 360, 24)], BOLD)
    for d in ((-7, 0, 7, 0), (0, -7, 0, 7)):
        s.line([at(d[0], d[1]), at(d[2], d[3])], BOLD)
    a = key(s, lambda u, v: at(u + 32, v - 26))
    s.line([a(12, 0), a(-12, 0)], BOLD)
    s.line([a(-4, 8), a(-12, 0), a(-4, -8)], BOLD)
