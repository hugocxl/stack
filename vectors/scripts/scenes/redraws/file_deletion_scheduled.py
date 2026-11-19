from shapely.geometry import LineString, MultiPoint, Polygon

from geometry import DETAIL, EDGE, Scene, oval, project
from scenes.redraws._kit import badge
from scenes.redraws._w5 import place_scene, ruled_file

DESCRIPTION = "A file protrudes from a tapered wastebasket with a clock badge on its rim."


def draw(s):
    outer = oval(24, 24, 23, 21)[:-1]
    opening = oval(24, 24, 20, 18)[:-1]
    foot = oval(24, 24, 16.5, 15)[:-1]
    s.solid(foot, 0, 34, top=outer, crease=False)
    s.face([(x, y, 34) for x, y in outer],
           openings=[[(x, y, 34) for x, y in opening]])
    file = Scene()
    ruled_file(file)
    place_scene(s, file, 7, 31, 17, .77)
    # Mask the portion of the sheet below the foreground rim.
    near = [project((x, y, 34)) for x, y in oval(24, 24, 23, 21, -42, 137, 44)]
    cover = Polygon([(35, near[0][1]), *near, (-35, near[-1][1]),
                     (-35, 58), (35, 58)])
    silhouette = MultiPoint([project((x, y, z)) for ring, z in ((foot, 0), (outer, 34))
                             for x, y in ring]).convex_hull
    lower = cover.intersection(silhouette)
    outline = LineString(near).union(silhouette.boundary.intersection(cover))
    s.layers.append((outline, lower, EDGE))
    s.ellipse(24, 24, 34, 20, 18, DETAIL, -42, 137)
    for angle in (24, 57, 90, 116):
        x0, y0 = oval(24, 24, 17.3, 15.7, angle, angle, 1)[0]
        x1, y1 = oval(24, 24, 21.5, 19.7, angle, angle, 1)[0]
        s.line([(x0, y0, 5), (x1, y1, 28)], DETAIL)
    badge(s, "clock", 43, 21, 32, 10.5)
