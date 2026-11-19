from geometry import DETAIL, EDGE
from scenes.redraws._w3 import Surface, printed_glyph

DESCRIPTION = "A corded gallery audio handset rests in a charging cradle above a printed exhibit marker."


def handset(s, *, origin=(0, 0, 0)):
    """A thick handheld audio player, with a wide earpiece and a tapered grip."""
    face = Surface(s, origin, rise=(-.22, .98), back=(0, -.98, -.22))
    face.plate([(10, 0), (34, 0), (40, 5), (43, 49), (48, 61), (48, 76),
                (45, 82), (40, 85), (8, 85), (3, 82), (0, 76), (0, 60),
                (5, 49), (5, 6)], 12)
    face.rect(8, 63, 32, 15, 6, EDGE)
    for v in (68, 73):
        face.rules(15, v, [18], ink=EDGE)
    face.rect(10, 37, 27, 16, 3, EDGE)
    for x in (17, 23, 29):
        face.oval(x, 45, 1.05, 1.05, DETAIL)
    face.oval(23, 20, 7.5, 7.5, EDGE)
    return face


def draw(s):
    s.box(0, 0, 0, 63, 42, 10, 4)
    s.box(5, 4, 10, 52, 14, 49, 4)
    face = handset(s, origin=(8, 25, 17))
    printed_glyph(face, "play", 23, 20, 6)
    s.tube([(63, 13, 5), (73, 13, 5), (80, 15, 10), (82, 18, 18),
            (81, 20, 28), (77, 23, 36), (70, 26, 40),
            (62, 24, 40), (53, 20, 39), (48, 19, 37)], 1.8)
    s.line([(50, 19, 39), (50, 19, 35)], EDGE)
    front = Surface(s, (0, 42, 0))
    front.rect(23, 2, 17, 6, 2, DETAIL)
    front.oval(31.5, 5, 1.3, 1.3, EDGE)
