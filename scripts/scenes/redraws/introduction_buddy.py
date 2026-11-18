from geometry import DETAIL, EDGE, oval, rounded
from scenes.redraws._w3 import Surface, speech_outline

DESCRIPTION = "A paired profile card shows two matching avatar pictograms below one shared speech bubble."


def avatar(face, x, v, size, ink=EDGE):
    """Print a featureless profile pictogram in a square of the given size."""
    place = face.viewer_axes(x, v)
    face.stroke([place(a, b) for a, b in oval(0, size * .21, size * .17, size * .17, count=24)], ink)
    face.stroke([place(a * size, b * size) for a, b in (
        (-.35, -.34), (-.35, -.26), (-.28, -.16), (-.15, -.10),
        (.15, -.10), (.28, -.16), (.35, -.26), (.35, -.34), (-.35, -.34)
    )], ink)


def draw(s):
    face = Surface(s, (0, 0, 0), rise=(-.24, .97), back=(0, -.97, -.24))
    face.plate(rounded(0, 0, 92, 66, 6), 7)
    for x in (26, 66):
        avatar(face, x, 22, 28)
        face.rules(x - 9, 7, [18])
    bubble = Surface(s, (0, 3, 0), rise=face.rise, back=face.back)
    bubble.plate(speech_outline(26, 45, 41, 23), 3)
    bubble.rules(35, 61, [23, 17], gap=7, ink=DETAIL)
