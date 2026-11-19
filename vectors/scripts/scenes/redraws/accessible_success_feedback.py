from geometry import rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface

DESCRIPTION = "A rounded confirmation speech bubble holds one large check badge."


def draw(s):
    face = Surface(s, (0, 0, 0), across=(.94, -.34), back=(-.34, -.94, 0))
    top_and_sides = rounded(0, 14, 87, 55, 12)
    outline = [*top_and_sides, (14, 14), (14, 0), (28, 14)]
    face.plate(outline, 7)
    badge(s, "check", *face.point(45, 42, -1), 19)
