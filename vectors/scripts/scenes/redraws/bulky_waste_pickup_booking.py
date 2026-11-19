from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import badge, coin

DESCRIPTION = "A flatbed truck carries a couch, with a clock badge above the cab."


def draw(s):
    for x in (-33, 31):
        coin(s, x, -12, 8, 8, depth=4)

    s.box(-46, -15, 9, 91, 30, 7, 2)
    for x in (-33, 31):
        y = coin(s, x, 17, 8, 8, depth=4)
        s.line([(a, y + .01, z) for a, z in oval(x, 8, 3, 3, count=24)], DETAIL)

    # Low feet raise the upholstery off the deck.
    for x in (-39, 3):
        s.box(x, 6, 16, 4, 4, 3, 1, DETAIL)
    s.box(-43, -12, 19, 53, 24, 8, 4)
    for x in (-42, -16):
        s.box(x, -13, 26, 25, 12, 20, 5)
    for x in (-36, -16):
        s.box(x, -1, 27, 19, 12, 4, 3)
    for x in (-43, 2):
        s.box(x, -9, 25, 8, 23, 10, 4)

    s.box(19, -15, 15, 26, 30, 30, 3)
    s.face([(23, 15, 42), (40, 15, 42), (40, 15, 32), (23, 15, 32)], EDGE)
    s.face([(45, -11, 32), (45, 11, 32), (45, 11, 42), (45, -11, 42)], EDGE)
    s.line([(24, 15, 27), (29, 15, 27)], DETAIL)
    for y in (-10, 5):
        s.line([(45, y, 21), (45, y + 5, 21)], EDGE)

    badge(s, "clock", 44, -1, 55, 11)
