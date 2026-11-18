from geometry import EDGE, oval, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface

DESCRIPTION = "A two-prong plug lines up with a matching socket that carries a refresh badge."


def draw(s):
    s.box(-18, -21, 0, 36, 25, 24, 4)
    socket = Surface(s, (0, 4, 0))
    for x in (-9, 9):
        socket.rect(x - 3, 9, 6, 11, 1.5, EDGE)

    for x in (-9, 9):
        pin = Surface(s, (x, 33, 0))
        pin.plate(rounded(-2, 10, 4, 9, 1), 15)
    s.box(-18, 33, 0, 36, 23, 24, 4)
    collar = Surface(s, (0, 60, 12))
    collar.plate(oval(0, 0, 5, 5, count=24)[:-1], 4)
    bend = oval(-18, 61, 18, 13, 0, 110, 18)
    s.tube([(0, 60, 12), *[(x, y, 12 + x / 6) for x, y in bend]], 1.9)
    badge(s, "refresh", 16, -15, 27, 15)
