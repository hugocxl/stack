from geometry import DETAIL, EDGE
from scenes.redraws._w5 import bound_planner, calendar_grid, place_setting, printed_stroke

DESCRIPTION = "A thick ring-bound weekly meal planner has one place-setting pictogram in each day column."


def draw(s):
    face = bound_planner(s, 98, 46)
    printed_stroke(s, face, [(7, 36), (32, 36)], EDGE)
    calendar_grid(s, face, 5, 6, 12.5, 23, 7, 1)
    printed_stroke(s, face, [(5, 23), (92.5, 23)], DETAIL)
    for day in range(7):
        x = 11.25 + 12.5 * day
        place_setting(s, face, x, 14.5, 2.9)
        printed_stroke(s, face, [(x - 2.2, 26), (x + 2.2, 26)], DETAIL)
