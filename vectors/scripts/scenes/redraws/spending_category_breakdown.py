from math import cos, radians, sin

from geometry import EDGE
from scenes.redraws._w5 import printed_stroke
from scenes.redraws.portfolio_allocation import pie_slices

DESCRIPTION = "A budget pie chart marks its three spending slices with a house, shopping basket, and fuel pump."


def draw(s):
    slices = ((160, 265, 4), (265, 363, 4), (3, 160, 4))
    surface = pie_slices(s, slices, radius=46, depth=8)
    fuel = [[(-6, -6), (-6, 7), (2, 7), (2, -6), (-7, -6)],
            [(-6, 1), (2, 1)],
            [(2, -3), (5, -3), (6, -1), (6, 5), (4, 7)]]
    basket = [[(-8, 2), (8, 2), (6, -6), (-6, -6), (-8, 2)],
              [(-4, 2), (-2, 7), (2, 7), (4, 2)]]
    home = [[(-8, 0), (0, 8), (8, 0), (6, 0), (6, -7), (-6, -7), (-6, 0), (-8, 0)],
            [(-2, -7), (-2, -2), (2, -2), (2, -7)]]
    for (start, end, gap), drawing in zip(slices, (fuel, basket, home)):
        angle = radians((start + end) / 2)
        x, y = (25 + gap) * cos(angle), (25 + gap) * sin(angle)
        # Orient each printed category upright in the projection.
        for stroke in drawing:
            printed_stroke(s, surface,
                           [(x + .58 * u - .9 * v, y - .58 * u - .9 * v)
                            for u, v in stroke], EDGE)
