from geometry import DETAIL, EDGE
from scenes.redraws._kit import coin

DESCRIPTION = "A lattice electricity pylon carries a balanced pair of scale pans beneath its crossarm."


def draw(s):
    for y in (-8, 8):
        s.line([(-18, y, 0), (-8, y, 53), (-5, y, 82), (0, y, 91),
                (5, y, 82), (8, y, 53), (18, y, 0)], EDGE)
    for z, half_span in ((6, 17), (24, 13.5), (49, 9)):
        s.line([(-half_span, 8, z), (half_span, 8, z), (half_span, -8, z)], EDGE)
    s.line([(-17, 8, 6), (13.5, 8, 24), (-9, 8, 49)], DETAIL)
    s.line([(17, 8, 6), (-13.5, 8, 24), (9, 8, 49)], DETAIL)
    for span, height in ((21, 79), (36, 60)):
        s.line([(-span, -8, height), (span, -8, height)], DETAIL)
        s.line([(-span, -8, height), (-span, 8, height), (-6, 8, height + 7),
                (6, 8, height + 7), (span, 8, height), (-span, 8, height)], EDGE)
        for x in (-span + 1, span - 1):
            s.tube([(x, 8, height), (x, 8, height - 8)], 1.45, EDGE)
    coin(s, 0, 15, 39, 20, 2.8)
    s.line([(0, 15, 51), (0, 15, 29)], EDGE)
    s.line([(-7, 15, 29), (7, 15, 29)], EDGE)
    s.line([(-12, 15, 47), (12, 15, 47)], EDGE)
    for x in (-10, 10):
        s.line([(x - 5, 15, 37), (x, 15, 47), (x + 5, 15, 37)], EDGE)
        s.line([(x - 5, 15, 37), (x - 2, 15, 34), (x + 2, 15, 34),
                (x + 5, 15, 37), (x - 5, 15, 37)], EDGE)
