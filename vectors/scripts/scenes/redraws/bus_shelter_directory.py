from geometry import DETAIL, EDGE
from scenes.redraws.garage_vacancy_queue import post
from scenes.redraws.hotel_search import magnifier

DESCRIPTION = "A roofed bus shelter with a bench has a magnifying glass over its posted stop sign."


def bus_pictogram(s, x, y, z, k, ink=EDGE):
    outline = [(-9, -7), (-9, 6), (-7, 9), (7, 9), (9, 6), (9, -7),
               (6, -7), (6, -10), (2.5, -10), (2.5, -7), (-2.5, -7),
               (-2.5, -10), (-6, -10), (-6, -7), (-9, -7)]
    s.line([(x + a * k, y, z + b * k) for a, b in outline], ink)
    s.line([(x + a * k, y, z + b * k) for a, b in
            ((-6, 5), (6, 5), (6, -1), (-6, -1), (-6, 5))], ink)
    for a in (-5, 5):
        s.line([(x + a * k, y, z - 4 * k), (x + (a + 1.4) * k, y, z - 4 * k)], ink)


def draw(s):
    s.box(0, 0, 0, 60, 3, 42, 1)
    s.line([(3, 3, 11), (57, 3, 11), (57, 3, 37), (3, 3, 37), (3, 3, 11)], DETAIL)
    for x in (9, 43):
        s.box(x, 11, 0, 3, 5, 11, 1)
    s.box(6, 5, 11, 46, 15, 3, 1)
    s.box(6, 5, 14, 46, 3, 10, 1)
    for x in (0, 57):
        s.box(x, 24, 0, 3, 3, 41, .7)
    s.box(-3, -4, 42, 67, 35, 5, 2.5)
    post(s, 73, 11, 46, width=2.6)
    s.box(64, 9, 34, 20, 3.5, 20, 1.7)
    bus_pictogram(s, 72, 12.5, 44, .68)
    magnifier(s, 81, 14, 51, 10)
