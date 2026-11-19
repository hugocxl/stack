from geometry import BOLD, DETAIL
from scenes.redraws._w4 import Surface

DESCRIPTION = "An accordion-folded street map outlines one service area across its street grid."


def draw(s):
    x_steps = (0, 30, 60, 90)
    depths = (0, -17, 1, -15)

    def place(u, v):
        panel = min(int(u / 30), 2)
        fraction = (u - x_steps[panel]) / 30
        depth = depths[panel] + fraction*(depths[panel+1] - depths[panel])
        return (u*.94 + depth*.34, -u*.34 + depth*.94 - .33*v, 5 + v)

    def path(points, ink=DETAIL):
        detailed = [points[0]]
        for (a, b), (c, d) in zip(points, points[1:]):
            creases = [u for u in (30, 60) if min(a, c) < u < max(a, c)]
            for u in sorted(creases, reverse=a > c):
                detailed.append((u, b + (d - b)*(u - a)/(c - a)))
            detailed.append((c, d))
        sheet.line(detailed, ink)

    sheet = Surface(s, place)
    for a, b in zip(x_steps, x_steps[1:]):
        sheet.slab([(a, 0), (b, 0), (b, 64), (a, 64)], 4)
    for u in (14, 41, 73):
        path([(u - 7, 6), (u, 24), (u, 44), (u + 9, 58)])
        path([(u - 3, 6), (u + 4, 24), (u + 4, 44), (u + 13, 58)])
    for v in (18, 39, 51):
        path([(5, v - 4), (42, v), (84, v - 5)])
    border = [(25, 20), (35, 12), (60, 16), (72, 27), (68, 43),
              (51, 51), (31, 44), (22, 34), (25, 20)]
    path(border, BOLD)
