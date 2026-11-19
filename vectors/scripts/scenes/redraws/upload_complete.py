from shapely.geometry import MultiPoint, Polygon
from shapely.ops import unary_union

from geometry import BOLD, DETAIL, EDGE, project
from scenes.redraws._kit import _strokes, badge
from scenes.redraws._w5 import smooth_loop

DESCRIPTION = "A thick cloud with an upward upload arrow carries a check badge on its upper-right lobe."


def draw(s):
    def face(u, v):
        return .73*u, -.27*u - .2*v, v

    contour = smooth_loop([(10, 0), (3, 2), (0, 10), (2, 20), (9, 26),
                           (20, 27), (27, 39), (38, 45), (51, 42),
                           (59, 31), (68, 31), (78, 25), (82, 15), (79, 5),
                           (71, 0), (57, 0), (24, 0)])
    points = [face(u, v) for u, v in contour]
    front, back = ([project((x, y - depth, z)) for x, y, z in points] for depth in (0, 7))
    sides = [MultiPoint((front[i-1], front[i], back[i-1], back[i])).convex_hull
             for i in range(len(contour))]
    front_face = Polygon(front)
    outline = unary_union([front_face, Polygon(back), *sides])
    s.layers.append((outline.boundary, outline, EDGE))
    seam = front_face.boundary.difference(outline.boundary.buffer(.13))
    s.layers.append((seam, None, DETAIL))
    for stroke in _strokes("up", 15):
        s.line([face(42 + u, 19 + v) for u, v in stroke], BOLD)
    badge(s, "check", *face(69, 32), 12.8)
