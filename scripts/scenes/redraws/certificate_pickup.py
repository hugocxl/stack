from shapely.geometry import MultiPoint

from geometry import BOLD, EDGE, oval, project
from scenes.redraws._kit import arrow

DESCRIPTION = "A rolled diploma is tied with a notched ribbon and marked by a pickup arrow curling outward."


def draw(s):
    def roll_surface(y, r):
        return [(x, y, z) for x, z in oval(27, 27, r, r, count=48)[:-1]]

    rear, front = roll_surface(0, 17), roll_surface(87, 17)
    roll = MultiPoint([project(p) for p in rear + front]).convex_hull
    s.layers.append((roll.boundary, roll, EDGE))
    s.face(front)
    spiral = [(27 + (13 - i * .14) * x, 87.1, 27 + (13 - i * .14) * z)
              for i, (x, z) in enumerate(oval(0, 0, 1, 1, 20, 495, count=52))]
    s.line(spiral, EDGE)
    for y in (42, 53):
        points = [(x, y, z) for x, z in oval(27, 27, 17.3, 17.3, -90, 90, count=28)]
        s.line(points, EDGE)
    s.face([(43, 48, 24), (43, 55, 25), (43, 61, 4), (43, 55, 9),
            (43, 49, 4), (43, 50, 15)], BOLD)
    arrow(s, [(47, 43, 9), (52, 35, 4), (60, 27, 4),
              (64, 20, 9), (72, 14, 13)], EDGE, head=9)
