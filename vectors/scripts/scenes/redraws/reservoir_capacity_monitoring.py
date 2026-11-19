from geometry import BOLD, DETAIL, EDGE

DESCRIPTION = "An open reservoir tank has a visible water surface and a side gauge aligned to the waterline."


def draw(s):
    x, y, radius, rim, level = 0, 0, 35, 33, 24
    s.disk(x, y, 0, radius, radius, rim, EDGE)
    s.ellipse(x, y, rim, 31, 31, EDGE)
    s.ellipse(x, y, level, 30, 30, EDGE, start=173, end=279)
    # The front seam is the datum where the gauge meets the water level.
    s.ellipse(x, y, level, radius, radius, DETAIL, start=-40, end=137)
    for a, b in (((-12, -3), (-4, -8)), ((-5, 3), (10, -4))):
        s.line([(*a, level), (*b, level)], DETAIL)
    s.box(10, 30, 3, 15, 4, 33, 1.5)
    s.line([(18, 34, 7), (18, 34, 32)], DETAIL)
    for z in (9, 14, 19, 29, 33):
        s.line([(12, 34, z), (15, 34, z)], EDGE)
    s.line([(12, 34, 24), (23, 34, 24)], BOLD)
