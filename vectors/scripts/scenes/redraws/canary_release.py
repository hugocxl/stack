from geometry import DETAIL
from scenes.redraws._kit import badge
from scenes.redraws._sf import carton

DESCRIPTION = "A small release carton goes out ahead of a row of full-size cartons, carrying a check badge."


def draw(s):
    s.line([(-90, 30, 0), (70, 30, 0)], DETAIL, dashed=True)
    for x in (-86, -46):
        carton(s, x, 4, 0, 34, 28, 30)
    carton(s, 20, 12, 0, 22, 18, 18)
    badge(s, "check", 31, 21, 36, 10)
