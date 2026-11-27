from geometry import EDGE
from scenes.redraws._sf import server

DESCRIPTION = "Four parallel cables run between two server units."


def draw(s):
    server(s, -90, -20, 0)
    for k in range(4):
        y = -14 + k*7
        s.tube([(-40, y, 9), (40, y, 9)], 2.2, EDGE)
    server(s, 40, -20, 0)
