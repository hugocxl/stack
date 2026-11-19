from shapely.geometry import LineString
from shapely.ops import unary_union

from geometry import DETAIL, EDGE

DESCRIPTION = "A raised watershed map shows three tributaries converging beside a staff gauge."


def draw(s):
    boundary = [(-42, -14), (-33, -29), (-3, -33), (27, -25), (42, -8),
                (38, 15), (21, 26), (8, 29), (-17, 24), (-35, 11)]
    s.solid(boundary, 0, 7, crease=False)
    for left, peak, right, front in (
        ((-36, -21, 7), (-23, -25, 24), (-7, -19, 7), (-24, -16, 7)),
        ((3, -18, 7), (12, -25, 24), (34, -13, 7), (17, -12, 7)),
        ((-35, 1, 7), (-25, 3, 18), (-15, 3, 7), (-23, 8, 7)),
    ):
        s.face([left, peak, right], EDGE)
        s.face([left, peak, front], DETAIL)

    branches = (
        ([(-28, -12), (-21, -10), (-17, -7), (-12, -7), (-3, -2),
          (5, 1), (12, 3), (17, 8), (19, 14), (17, 20), (18, 25.8)], 2.6),
        ([(24, -12), (18, -10), (15, -6), (14, -1), (12, 3)], 1.42),
        ([(-22, 15), (-14, 17), (-7, 17), (3, 13),
          (11, 13), (19, 14)], 1.55),
    )
    stream = unary_union([LineString(path).buffer(width) for path, width in branches])
    s.line([(x, y, 7) for x, y in stream.exterior.coords], EDGE)

    s.box(27, 13, 7, 5, 4, 30, .8)
    s.line([(21, 15, 7), (27, 15, 7)], DETAIL)
    for z in (13, 18, 23, 28, 33):
        s.line([(27.5, 17, z), (31.4, 17, z)], EDGE)
