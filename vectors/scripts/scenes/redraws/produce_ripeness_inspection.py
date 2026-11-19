from shapely.geometry import MultiPoint, Polygon

from geometry import DETAIL, EDGE, oval, project
from scenes.redraws._w5 import food_loupe, smooth_loop

DESCRIPTION = "A magnifier inspects the cut edge of an avocado half with its pit still in place."


def draw(s):
    def face(u, v):
        return u, -.87*v, 17 + .49*v + .14*u

    outline = smooth_loop([(0, 55), (9, 50), (14, 35), (22, 23),
                           (24, 12), (20, 3), (10, -3), (0, -5),
                           (-12, -2), (-21, 5), (-24, 15), (-20, 26),
                           (-11, 37), (-8, 49)])
    front = [face(u, v) for u, v in outline]
    back = [(x * .8, y - 4, z - 12) for x, y, z in front]
    cut = Polygon([project(p) for p in front])
    hull = MultiPoint([project(p) for p in front + back]).convex_hull
    s.layers.append((hull.boundary.union(cut.boundary), hull, EDGE))
    s.line([face(u*.88, 18 + (v-18)*.9) for u, v in outline + outline[:1]], DETAIL)
    pit = oval(0, 15, 13, 13, count=44)
    s.face([(x, y, z + 2.5) for x, y, z in (face(u, v) for u, v in pit[:-1])], EDGE)
    food_loupe(s, 2, -30, 46, 13.8, handle_y=.25, handle_start=.98)
