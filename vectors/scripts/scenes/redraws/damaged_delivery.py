from geometry import EDGE
from scenes.redraws._kit import warning
from scenes.redraws._sf import carton

DESCRIPTION = "A taped carton has a jagged tear down its side and a warning triangle beside it."


def draw(s):
    front = carton(s, -30, -22, 0, 60, 44, 40)
    s.line([front(u, v) for u, v in [(44, 40), (40, 33), (46, 28), (39, 21), (44, 14)]], EDGE)
    warning(s, 40, 26, 4, 26)
