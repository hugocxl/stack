from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "Two raised letterforms of different sizes stand on the same baseline."


def draw(s):
    face = Surface(s, (0, 0, 0), across=(.94, -.34), back=(-.34, -.94, 0))
    for x, w, h in ((9, 27, 34), (48, 48, 65)):
        def point(u, v):
            return face.point(x + u * w, 5 + v * h)

        front = ((0, 0), (.23, 0), (.33, .23), (.67, .23), (.77, 0),
                 (1, 0), (.61, 1), (.39, 1))
        hole = ((.4, .42), (.6, .42), (.5, .70))
        face.plate([(x + u * w, 5 + v * h) for u, v in front], 6, BOLD)
        s.line([point(u, v) for u, v in (*hole, hole[0])], EDGE)
    face.plate(rounded(0, 0, 106, 5, 1), 7)
