from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "A handheld microphone has a short tapered grip and a domed crosshatched grille."


def draw(s):
    mic = Surface(s, (0, 0, 0))
    align = mic.viewer_axes(0, 0)

    def point(u, v):
        # Tilt the microphone around its grip while keeping the grille readable.
        return align(u + .67 * v, v - .67 * u)

    for outline, depth in (
        ([(-5, 0), (5, 0), (7, 3), (9, 43), (-9, 43), (-7, 3)], 7),
        (rounded(-10, 39, 20, 8, 2), 8),
        (rounded(-14, 45, 28, 28, 12), 10),
    ):
        mic.plate([point(u, v) for u, v in outline], depth)
    for v, half in ((51, 9), (56, 12), (61, 12), (66, 9)):
        mic.stroke([point(-half, v), point(half, v)], DETAIL)
    for u in (-6, 0, 6):
        mic.stroke([point(u, 50), point(u, 67)], DETAIL)
    mic.stroke([point(-2, 31), point(2, 31)], EDGE)
