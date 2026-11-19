from shapely.geometry import MultiPoint
from shapely.ops import unary_union

from geometry import DETAIL, EDGE, oval, project
from scenes.redraws._kit import _screen, badge

DESCRIPTION = "A flared notification bell carries a check badge on its lower-right rim."


def notification_bell(s):
    # Overlapping bands keep the curved shoulders and the flare visible in silhouette.
    sections = [(32, 13), (31.5, 15), (28.5, 18), (25.5, 22), (23.5, 27),
                (23, 33), (22, 39), (19.5, 45), (15.5, 50), (9.5, 54), (3, 55)]
    circles = [[project((x, y, z)) for x, y in oval(0, 0, radius, radius, count=48)]
               for radius, z in sections]
    bands = [MultiPoint(lower + upper).convex_hull for lower, upper in zip(circles, circles[1:])]
    silhouette = unary_union(bands)
    clapper = [project((x, y, z)) for radius, z in ((5.2, -13), (7.4, -10), (5.2, -6))
               for x, y in oval(0, 0, radius, radius, count=32)]
    striker = MultiPoint(clapper).convex_hull
    s.layers.append((striker.boundary, striker, EDGE))
    s.tube([(0, 0, -7), (0, 0, 15)], 2.1, EDGE)
    s.disk(0, 0, 53, 4.5, 4.5, 8)
    s.layers.append((silhouette.boundary, silhouette, EDGE))
    s.ellipse(0, 0, 16.7, 29.8, 29.8, DETAIL, -41, 131)


def draw(s):
    notification_bell(s)
    badge(s, "check", *_screen(0, 0, 0, 33, 9), 12.6)
