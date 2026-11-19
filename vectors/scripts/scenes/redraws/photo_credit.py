from geometry import EDGE
from scenes.redraws._w4 import camera_emblem, landscape, photo_print

DESCRIPTION = "A photographic print has an integrated credit strip with a camera emblem and a byline rule."


def draw(s):
    print_face = photo_print(s, 94, 81, angle=-23, image=False)
    landscape(print_face, 7, 7, 80, 49)
    camera_emblem(print_face, 10, 62, 15)
    print_face.rows(31, 69, (42,), ink=EDGE)
