from geometry import DETAIL, EDGE
from scenes.redraws._w5 import apple_mark, bound_planner, calendar_grid, printed_stroke, rect

DESCRIPTION = "A ring-bound produce calendar highlights an apple in one of its date cells."


def draw(s):
    face = bound_planner(s, 62, 61, desk=True)
    printed_stroke(s, face, [(9, 49), (36, 49)], EDGE)
    rect(s, face, 46, 46, 7, 5, .75, DETAIL)
    calendar_grid(s, face, 6, 7, 16.5, 17, 3, 2)
    apple_mark(s, face, 30.75, 30.4, .62)
