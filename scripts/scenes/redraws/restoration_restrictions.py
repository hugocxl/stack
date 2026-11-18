from geometry import EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._w5 import folded_sheet

DESCRIPTION = "A backup snapshot file displays a database pictogram and carries a padlock badge."


def draw(s):
    face = folded_sheet(s, w=55, h=63)
    x, top, radius, height = 26, 41, 13, 22
    s.line([face(u, v) for u, v in oval(x, top, radius, 4.5, count=32)], EDGE)
    for side in (-1, 1):
        s.line([face(x + side * radius, top), face(x + side * radius, top - height)], EDGE)
    for z in (top - 7.3, top - 14.6, top - height):
        s.line([face(u, v) for u, v in oval(x, z, radius, 4.5, 180, 360, 24)], EDGE)
    badge(s, "lock", *face(53, 14), 13)
