from geometry import DETAIL, EDGE
from scenes.redraws._w1 import solar_cells
from scenes.redraws.program_impact import community_house

DESCRIPTION = "Two solar modules sit flush on the pitched roof of a house."


def draw(s):
    community_house(s)
    for left in (-29, 1):
        def panel(u, v):
            y = 2 + 17 * v
            return (left + 28 * u, y, 62 - y * 24 / 21)

        front_left, front_right = panel(0, 1), panel(1, 1)
        s.face([front_left, front_right, (front_right[0], 19, front_right[2] - 1.8),
                (front_left[0], 19, front_left[2] - 1.8)], EDGE)
        solar_cells(s, panel, columns=3)
    s.line([(29, 9, 33), (29, 9, 19), (29, 16, 19)], DETAIL)
