from geometry import EDGE
from scenes.redraws._w4 import folder_emblem, front_surface

DESCRIPTION = "A shared category branch connects two matching folder nodes at the same depth."


def draw(s):
    face = front_surface(s, angle=-24, z=6)
    face.line([(57, 69), (57, 49)], EDGE)
    face.line([(24, 35), (24, 49), (90, 49), (90, 35)], EDGE)
    for u in (0, 66):
        folder_emblem(face, u, 0, 48, 35, solid=True)
    face.frame(48, 69, 18, 16, 4, EDGE)
