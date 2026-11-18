from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface, cover_cap

DESCRIPTION = "A campus welcome credential hangs from a looped lanyard and carries an outward arrow badge."


def draw(s):
    turn = [(32, 24, 57), (12, 15, 69), (-3, 1, 87), (-5, -18, 91),
            (5, -32, 88), (25, -34, 82), (45, -23, 72), (42, -6, 64),
            (32, 24, 57)]
    strap = [turn[0]]
    for a, b in zip(turn, turn[1:]):
        strap.extend(tuple(p * (1 - t) + q * t for p, q in zip(a, b))
                     for t in (.25, .75))
    strap.append(turn[-1])
    s.tube(strap, 3.3)
    face = Surface(s, (0, 30, 0), rise=(-.33, .94), back=(0, -.94, -.33))
    face.plate(rounded(0, 0, 64, 62, 6), 5)
    face.rect(22, 51, 20, 5, 2.4, EDGE)
    s.tube([(32, 24, 57), (32, 15, 54), face.point(32, 54)], 2)
    cover_cap(face, 30, 35, 34)
    face.rules(13, 15, [32, 23], gap=7)
    badge(s, "arrow", 66, 19, 36, 14)
