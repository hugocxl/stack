from geometry import EDGE, oval
from scenes.editorial_objects import archive
from scenes.redraws._kit import arrow

DESCRIPTION = "A circular rotation arrow sweeps around the front corner of a lidded archive box."


def draw(s):
    path = [(x, y, 2) for x, y in oval(27, 24, 50, 43, 162, -38, 65)]
    arrow(s, path, EDGE, head=8)
    archive(s)
