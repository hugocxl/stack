from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import _strokes
from scenes.redraws._w5 import panel

DESCRIPTION = "A transit map shows an arrow connecting two rail lines at a shared station."


def draw(s):
    point = lambda x, z: (x, -.2 * z, z)
    panel(s, [(0, 0), (70, 0), (70, 66), (0, 66)], point, 4)
    s.line([point(6, 57), point(64, 57)], DETAIL)

    paths = ([(8, 11, 2.8), (20, 22, 2.8), (20, 41, 4.3), (10, 49, 2.8)],
             [(61, 11, 2.8), (50, 22, 2.8), (50, 41, 4.3), (60, 49, 2.8)])
    for stations in paths:
        s.line([point(x, z) for x, z, _ in stations], EDGE)
        for x, z, radius in stations:
            s.face([point(a, b) for a, b in oval(x, z, radius, radius, count=28)[:-1]])
    for stroke in _strokes("arrow", 12):
        s.line([point(35 + x, 41 + z) for x, z in stroke], EDGE)
