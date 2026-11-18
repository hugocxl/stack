from geometry import BOLD, DETAIL
from scenes.redraws._kit import warning
from scenes.redraws._w5 import cupboard_shell, cupboard_trim

DESCRIPTION = "A stock shelf holds one carton beside a dashed missing-item outline and a large warning triangle."


def draw(s):
    cupboard_shell(s, 85, 29, 51)
    s.box(8, 9, 3, 15, 16, 26, 1.5)
    s.line([(12, 25, 11), (19, 25, 11), (19, 25, 19),
            (12, 25, 19), (12, 25, 11)], DETAIL)
    outline = [(43, 5), (43, 27), (48, 32), (48, 39), (57, 39),
               (57, 32), (62, 27), (62, 5), (43, 5)]
    s.line([(x, 25, z) for x, z in outline], BOLD, dashed=True)
    cupboard_trim(s, 85, 29, 51)
    warning(s, 90, 31, 10, 34)
