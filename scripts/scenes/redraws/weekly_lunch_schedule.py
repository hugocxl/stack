from geometry import DETAIL, EDGE
from scenes.redraws._w5 import bound_planner, calendar_grid, printed_stroke, rect

DESCRIPTION = "A folded weekly calendar marks its midday row with three lunchboxes."


def draw(s):
    face = bound_planner(s, 91, 55, desk=True)
    printed_stroke(s, face, [(7, 46), (32, 46)], EDGE)
    calendar_grid(s, face, 5, 6, 11.5, 11, 7, 3)
    for x in (22.25, 45.25, 68.25):
        rect(s, face, x - 4.5, 18.1, 9, 6, 1, EDGE)
        printed_stroke(s, face, [(x - 2, 24.1), (x - 2, 25.9),
                                 (x + 2, 25.9), (x + 2, 24.1)], EDGE)
    for x in (10.75, 33.75, 56.75, 79.75):
        printed_stroke(s, face, [(x - 2, 20.7), (x + 2, 20.7)], DETAIL)
