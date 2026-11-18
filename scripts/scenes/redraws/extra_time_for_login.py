from geometry import BOLD, EDGE, rounded
from scenes.redraws._kit import badge, glyph
from scenes.redraws._w3 import Surface

DESCRIPTION = "A clock badge overlaps the timeout row below the password field on a laptop’s sign-in screen."


def draw(s):
    s.box(0, -7, 0, 88, 47, 5, 4)
    screen = Surface(s, (0, 0, 4), rise=(-.19, .98), back=(0, -.98, -.19))
    screen.plate(rounded(0, 0, 88, 65, 4), 5)
    screen.rect(6, 6, 76, 53, 3)
    screen.rect(16, 33, 55, 15, 3, EDGE)
    for x in (23, 29, 35, 41):
        screen.oval(x, 40, 1.45, 1.45, BOLD)
    glyph(s, "lock", *screen.point(63, 41), 6, BOLD)
    screen.rules(16, 24, [32], ink=EDGE)
    screen.rules(16, 16, [24])
    for y in (9, 15):
        for x in (17, 29, 41, 53, 65):
            s.line([(x, y, 5), (x + 7, y, 5)])
    trackpad = Surface(s, (0, 39, 5), rise=(-1, 0))
    trackpad.rect(34, 6, 21, 12, 2)
    badge(s, "clock", *screen.point(80, 24, -6), 15)
