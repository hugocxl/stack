from geometry import BOLD, DETAIL, EDGE

DESCRIPTION = "A round compass has four cardinal ticks, a central pivot, and a bold needle."


def draw(s):
    s.disk(0, 0, 0, 43, 43, 8)
    s.ellipse(0, 0, 8, 37, 37, EDGE)
    for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        s.line([(x*29, y*29, 8), (x*35, y*35, 8)], EDGE)
    for x, y in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
        s.line([(x*23, y*23, 8), (x*24.6, y*24.6, 8)], DETAIL)
    north, west, south, east = (1, -28, 8), (-7, 0, 8), (-1, 24, 8), (7, 0, 8)
    s.line([west, south, east], EDGE)
    s.line([west, north, east], BOLD)
    s.line([west, (-3, 0, 8)], EDGE)
    s.line([(3, 0, 8), east], EDGE)
    s.ellipse(0, 0, 8, 2.9, 2.9, DETAIL)
