from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface
from scenes.redraws.artifact_conservation import museum_vase

DESCRIPTION = "A repaired museum vase sits on a plinth with a donation heart badge at its foot."


def draw(s):
    s.box(-24, -21, 0, 48, 42, 8, 2)
    museum_vase(s, z=8)
    seam = Surface(s, (13, 13, 8))
    seam.stroke([(-4, 24), (0, 29), (-1, 34), (4, 38), (0, 43),
                 (2, 46), (-2, 51)], EDGE)
    for x, v in ((-2, 27), (1, 36), (1, 44)):
        seam.stroke([(x - 4, v + 1), (x + 4, v - 1)], EDGE)
    badge(s, "heart", 23, 18, 7, 13)
