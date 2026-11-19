from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w3 import Surface, clipboard

DESCRIPTION = "A magnifier circles a chip on the rim of a vase drawn on a conservation clipboard."


def vase_outline(face, x, v, size, *, chipped=False, ink=EDGE):
    """Print the same accession vessel on both conservation records."""
    rim = [(.08, .5), (.14, .36), (.24, .45), (.28, .5)] if chipped else []
    outline = [(-.28, .5), *rim, (.30, .5), (.30, .39), (.19, .36),
               (.17, .18), (.34, .07), (.40, -.12), (.34, -.30), (.24, -.40),
               (.21, -.49), (-.21, -.49), (-.24, -.40), (-.34, -.30),
               (-.40, -.12), (-.34, .07), (-.17, .18), (-.19, .36), (-.28, .39)]
    face.stroke([(x + a * size, v + b * size) for a, b in outline], ink, closed=True)
    face.rules(x - .21 * size, v - .40 * size, [.42 * size])


def draw(s):
    face = clipboard(s, w=77, h=88)
    face.rules(13, 64, [17], ink=EDGE)
    face.rules(13, 57, [12])
    vase_outline(face, 32, 36, 35, chipped=True)
    face.rules(16, 12, [26], ink=DETAIL)
    lens = Surface(s, (0, 70, 5), rise=face.rise, back=face.back)
    lens.oval(41, 54, 13, 13, BOLD)
    lens.oval(41, 54, 10.8, 10.8, DETAIL)
    s.tube([lens.point(50, 44), lens.point(65, 25)], 2.25)
