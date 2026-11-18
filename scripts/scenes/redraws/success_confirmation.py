from shapely.geometry import MultiPoint

from geometry import EDGE, oval, project
from scenes.redraws._kit import _screen, badge

DESCRIPTION = "A raised circular seal shows a single bold checkmark."


def draw(s):
    rim = oval(0, 0, 38, 38, count=64)[:-1]
    base = [_screen(0, 0, 0, u - 5, v - 4) for u, v in rim]
    front = [_screen(0, 0, 0, u, v) for u, v in rim]
    hull = MultiPoint([project(point) for point in base + front]).convex_hull
    s.layers.append((hull.boundary, hull, EDGE))
    badge(s, "check", 0, 0, 0, 38)
