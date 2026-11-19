from geometry import DETAIL, EDGE, oval, rounded
from scenes.redraws._w2 import board, chart_line, chart_marker, closed_outline, lens_outline

DESCRIPTION = "A search panel uses a ringed planet as its query and shows a crescent moon and a rocket as related results."


def draw(s):
    p = board(s, 117, 73, run=.34, rise=.89, depth=9, level=True)
    closed_outline(s, p, rounded(9, 47, 99, 17, 3), EDGE)
    lens_outline(s, p, 20, 56, 4)
    chart_marker(s, p, 48, 55.5, 5.4, EDGE)
    planet_ring = [(48 + (x-48)*.98 + (z-55)*.28, 55 + (x-48)*.28 + (z-55)*.98)
                   for x, z in oval(48, 55, 10, 2.4, start=195, end=515)]
    chart_line(s, p, planet_ring, DETAIL)
    for x in (12, 63):
        closed_outline(s, p, rounded(x, 8, 42, 31, 3), DETAIL)
    moon = oval(33, 23, 9, 11, start=58, end=301, count=28)
    moon += [(33, 17), (31, 21), (31, 24), (32, 28), (35, 31)]
    closed_outline(s, p, moon, EDGE)
    rocket = [(76, 14), (77, 20), (81, 23), (82, 27), (88, 33),
              (91, 34), (92, 30), (91, 25), (88, 20), (88, 15),
              (85, 12), (84, 17), (80, 18)]
    closed_outline(s, p, rocket, EDGE)
    chart_marker(s, p, 87, 26, 2.2, EDGE)
    chart_line(s, p, [(81, 15), (78, 12)], DETAIL)
