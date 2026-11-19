from math import cos, pi, sin

from shapely.geometry import MultiPoint, Polygon
from shapely.ops import unary_union

from geometry import BOLD, DETAIL, EDGE, Scene, oval, project
from scenes.redraws._kit import badge
from scenes.redraws.sync_complete import sync_arrows

DESCRIPTION = "A thick toothed settings gear carries a badge with two circular synchronization arrows."


def draw(s):
    outline = []
    for tool_angle in (i*pi/4 for i in range(8)):
        for angle, radius in ((-.32, 26), (-.23, 26), (-.18, 34), (.18, 34),
                              (.23, 26), (.32, 26)):
            outline.append((radius*cos(tool_angle + angle), radius*sin(tool_angle + angle)))
    front, rear = ([project((x, y, z)) for x, y in outline] for z in (9, 0))
    sides = [MultiPoint((front[i-1], front[i], rear[i-1], rear[i])).convex_hull
             for i in range(len(outline))]
    silhouette = unary_union([Polygon(rear), Polygon(front), *sides])
    s.layers.append((silhouette.boundary, silhouette, EDGE))
    s.face([(x, y, 9) for x, y in outline], EDGE,
           openings=[[(x, y, 9) for x, y in oval(0, 0, 9.5, 9.5, count=40)]])
    s.ellipse(0, 0, 9, 14.7, 14.7, DETAIL)
    center = (22, -17, 12)
    # Keep the kit's rim and use the paired arrows from the sync figure.
    rim = Scene()
    badge(rim, "refresh", *center, 13.4)
    s.layers.extend(layer for layer in rim.layers if layer[2] != BOLD)
    sync_arrows(s, center, 7, 7, 5.4)
