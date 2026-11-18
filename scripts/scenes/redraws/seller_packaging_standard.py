from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w1 import software_package

DESCRIPTION = "A check badge marks a shipping carton with neatly taped seams."


def draw(s):
    software_package(s, 0, 0, 0, 1.32, show_code=False)
    half_width, front, top = 38.28, 27.72, 47.52
    for y in (-24, 24):
        s.line([(-half_width, y - 2.2, top), (half_width, y - 2.2, top),
                (half_width, y - 2.2, top - 10)], DETAIL)
        s.line([(-half_width, y + 2.2, top), (half_width, y + 2.2, top),
                (half_width, y + 2.2, top - 10)], DETAIL)
    s.line([(-6.6, front, top - 7.92), (-6.6, front, 33), (0, front, 35),
            (6.6, front, 33), (6.6, front, top - 7.92)], EDGE)
    badge(s, "check", 38, -13, 45, 12)
