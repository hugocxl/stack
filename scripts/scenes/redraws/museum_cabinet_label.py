from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w3 import Surface

DESCRIPTION = "A glass museum case encloses a faceted sculpture and carries a caption plaque on its front rim."


def faceted_sculpture(s, place):
    """An abstract stone sculpture that can also lie in a packing recess."""
    a, b, c, d, e = [place(*p) for p in
                      ((-14, 0, 0), (11, 0, 0), (13, 24, 0), (-5, 38, 2), (-14, 25, 0))]
    ridge = place(1, 21, 11)
    s.face([a, b, c, d, e, a], EDGE)
    s.line([a, ridge, c], EDGE)
    s.line([ridge, d], DETAIL)
    s.line([ridge, b], DETAIL)


def draw(s):
    w, d, z, top = 64, 49, 18, 83
    s.box(0, 0, 0, w, d, z, 2)
    s.box(10, 26, z, 28, 17, 4, 1, DETAIL)
    faceted_sculpture(s, lambda u, v, n: (24 + u, 32 + n, z + 4 + v))
    s.line([(0, d, z), (0, d, top), (0, 0, top), (w, 0, top), (w, 0, z)], EDGE)
    s.line([(0, d, top), (w, d, top), (w, 0, top)], EDGE)
    s.line([(w, d, top), (w, d, z)], DETAIL)
    plaque = Surface(s, (0, d + 1, 0))
    plaque.rect(12, 2, 34, 14, 2, EDGE)
    plaque.rules(18, 11, [21, 15], gap=5, ink=BOLD)
