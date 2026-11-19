from geometry import EDGE
from scenes.redraws._kit import _strokes, badge
from scenes.redraws._w5 import bound_planner, calendar_grid

DESCRIPTION = "A desk calendar marks an expired date with an X and carries a check badge."


def draw(s):
    face = bound_planner(s, 60, 52, desk=True)
    s.line([face(0, 38), face(60, 38)], EDGE)
    calendar_grid(s, face, 6, 7, 11, 9, 4, 3)
    (first, second) = _strokes("x", 5.3)
    for line in (first, second):
        s.line([face(22.5 + x, 20.5 + z) for x, z in line], EDGE)
    badge(s, "check", *face(58, 13), 12.7)
