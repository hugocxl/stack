from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "A short lanyard clips to a theater access pass printed with parted stage curtains."


def curtain(face, x, v, w, h):
    """Print the proscenium and the two swept-back curtains."""
    face.rect(x, v, w, h, 2, EDGE)
    face.rules(x, v + h * .82, [w], ink=EDGE)
    for anchor, side in ((x, 1), (x + w, -1)):
        for fold in (.29, .46):
            face.stroke([(anchor + side * w * a, v + h * b) for a, b in (
                (fold, .82), (fold*.88, .64), (fold*.50, .41), (.13, .32),
                (.18, .16), (.22, 0)
            )], EDGE if fold == .46 else DETAIL)


def draw(s):
    face = Surface(s, (0, 0, 0), rise=(-.29, .96), back=(0, -.96, -.29))
    s.tube([face.point(u, v, 1) for u, v in [(30, 71), (16, 86), (14, 97),
            (19, 104), (28, 107), (37, 103), (41, 95), (39, 86), (30, 71)]], 1.7)
    face.plate(rounded(0, 0, 61, 75, 6), 6)
    face.rect(24, 64, 13, 5, 2.2, EDGE)
    s.tube([face.point(30, 66, -1), face.point(30, 77, -1)], 1.5)
    curtain(face, 9, 16, 43, 39)
    face.rules(18, 8, [25])
