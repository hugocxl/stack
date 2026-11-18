from geometry import BOLD, EDGE
from scenes.redraws._w4 import folder_emblem, front_surface, nav_path

DESCRIPTION = "Two folder levels form a short category path, with an upward arrow pointing back to the parent folder."


def draw(s):
    face = front_surface(s, angle=-19, z=7)
    face.line([(29, 51), (29, 27), (50, 27)], EDGE)
    folder_emblem(face, 1, 51, 57, 37, solid=True)
    folder_emblem(face, 50, 7, 52, 35, solid=True)
    nav_path(face, [(78, 38), (78, 72), (60, 72)], BOLD, head=8)
