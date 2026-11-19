from geometry import EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface

DESCRIPTION = "A slatted museum shipping crate bears a ring sculpture label and an outbound arrow badge."


def ring_sculpture(face, x, v, size, ink=EDGE):
    """Print a ring sculpture with a block pedestal."""
    for rx, ry in ((.35, .39), (.18, .23)):
        face.stroke([(a, b) for a, b in oval(x, v + .10 * size, rx * size, ry * size, count=31)], ink)
    face.rect(x - .38 * size, v - .50 * size, .76 * size, .18 * size, .02 * size, ink)


def draw(s):
    s.box(0, 0, 0, 72, 42, 51, 2)
    s.box(-1, -1, 49, 74, 44, 6, 1)
    face = Surface(s, (0, 42, 0))
    for v in (14, 37):
        face.rules(1, v, [70])
        s.line([(72, 0, v), (72, 42, v)])
    for x in (4, 62):
        s.box(x, 42, 1, 6, 2.6, 47, .8)
        for v in (7, 42):
            s.line([(x + 2.4, 44.6, v), (x + 3.6, 44.6, v)])
    label = Surface(s, (0, 43, 0))
    label.plate([(17, 9), (55, 9), (55, 44), (17, 44)], 1)
    ring_sculpture(label, 36, 27, 28)
    badge(s, "arrow", 70, 31, 49, 13)
