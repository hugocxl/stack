from geometry import DETAIL
from scenes.redraws._kit import badge
from scenes.redraws._w3 import design_layer, selection_handle

DESCRIPTION = "A closed lock badge anchors the corner of a single design layer with visible selection handles."


def draw(s):
    face = design_layer(s, (0, 0, 4))
    face.oval(42, 31, 13, 12, DETAIL)
    for u, v in ((11, 11), (11, 52), (74, 11)):
        selection_handle(face, u, v)
    badge(s, "lock", *face.point(76, 51), 15)
