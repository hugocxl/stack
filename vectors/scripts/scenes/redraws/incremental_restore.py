from geometry import BOLD, oval
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import database, platter

DESCRIPTION = "An offset top snapshot sits above a database stack, and a curved arrow returns to that layer."


def draw(s):
    database(s, -5, 4, 25, pitch=8)
    platter(s, 8, -5, 24, 25, 8)

    # The approach bends around the right silhouette before pointing to the delta.
    projected_path = [*oval(19, -17, 42, 29, 74, -78, 36), (16, -45)]
    path = [(32 + (v + u / 2) / .8660254, 32 + (v - u / 2) / .8660254, 32)
            for u, v in projected_path]
    arrow(s, path, BOLD, head=8)
