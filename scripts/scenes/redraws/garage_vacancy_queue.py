from geometry import BOLD, DETAIL, rounded
from scenes.redraws._kit import badge

DESCRIPTION = "A posted parking sign carries a clock badge at its upper corner."


def parking_letter(s, transform):
    stroke = [(-5, -12), (-5, 12), (2, 12), (6, 10), (8, 7),
              (8, 3), (6, 0), (2, -2), (-5, -2)]
    s.line([transform(x, z) for x, z in stroke], BOLD)


def post(s, x, y, h, *, width=4):
    s.box(x - width / 2, y - width / 2, 0, width, width, h, 1)
    s.box(x - width, y - width, 0, width * 2, width * 2, 2.5, 1)


def draw(s):
    post(s, 20, -2, 53)
    s.box(0, -4, 31, 41, 5, 36, 2)
    inset = rounded(4, 34, 33, 30, 2)
    s.line([(x, 1, z) for x, z in inset + inset[:1]], DETAIL)
    parking_letter(s, lambda x, z: (19 + x * .85, 1, 48 + z * .85))
    badge(s, "clock", 43, 2, 66, 11.5)
