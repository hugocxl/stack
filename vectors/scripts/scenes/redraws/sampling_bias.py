from geometry import BOLD, DETAIL
from scenes.redraws._kit import warning
from scenes.redraws._w2 import funnel

DESCRIPTION = "A sampling funnel receives round and square tokens but releases only round ones."


def draw(s):
    funnel(s)
    s.box(-19, -12, 59, 14, 14, 5, 1.3)
    s.disk(11, 8, 60, 7, 7, 4)
    s.disk(1, 39, 1, 7, 7, 4, BOLD)
    s.disk(17, 21, 1, 7, 7, 4, BOLD)
    s.line([(3, 8, 15), (9, 17, 10), (9, 25, 6)], DETAIL, dashed=True)
    warning(s, 41, 2, 35, 22)
