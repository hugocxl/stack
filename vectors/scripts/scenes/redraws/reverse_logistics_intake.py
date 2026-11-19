from geometry import DETAIL
from scenes.redraws._w1 import intake_arrow, open_carton_back, open_carton_front

DESCRIPTION = "A hooked return arrow turns down into the open mouth of a shipping carton."


def draw(s):
    carton = (-31, 31, -24, 24, 28)
    open_carton_back(s, *carton)
    path = [(29, -6, 85), (14, -6, 77.5), (7, -6, 73), (2, -6, 67),
            (0, -6, 60), (0, -6, 32)]
    intake_arrow(s, path, head=12)
    open_carton_front(s, *carton)
    s.line([(-19, 24, 16), (-8, 24, 16)], DETAIL)
    s.line([(-19, 24, 11), (-2, 24, 11)], DETAIL)
