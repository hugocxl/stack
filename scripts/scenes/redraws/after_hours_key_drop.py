from geometry import DETAIL, EDGE, oval, rounded
from scenes.redraws._w4 import Surface, printed_glyph

DESCRIPTION = "A toothed room key is halfway into the top slot of a moon-marked drop box."


def draw(s):
    width, depth, height = 70, 38, 47
    slot = [(*p, height) for p in rounded(20, 13, 32, 11, 2)]
    s.face([(0, 0, height), (width, 0, height), (width, depth, height), (0, depth, height)],
           openings=[slot])
    s.face([(width, 0, 0), (width, depth, 0), (width, depth, height), (width, 0, height)])
    s.face([(0, depth, 0), (width, depth, 0), (width, depth, height), (0, depth, height)])
    front = Surface(s, lambda u, v: (u, depth, v))
    printed_glyph(front, "moon", 35, 24, 15, EDGE)
    front.line([(0, 8), (70, 8)], DETAIL)

    key = Surface(s, lambda u, v: (32 + u + .29*v, 19 - .35*v, height + v))
    bow = oval(0, 28, 11, 11, -67, 247, count=40)
    key.slab([*bow, (-4.3, 0), (5, 0), (5, 4), (10, 4),
              (10, 8), (5, 8), (5, 12), (9, 12), (9, 15), (4.3, 15)], 2)
    key.oval(0, 28, 4, 4, DETAIL)
