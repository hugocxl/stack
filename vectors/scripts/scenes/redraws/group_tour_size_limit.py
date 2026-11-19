from geometry import BOLD, DETAIL
from scenes.redraws._w5 import bus

DESCRIPTION = "A tour coach displays an end-capped capacity bracket beneath three passenger seats."


def draw(s):
    bus(s, coach=True)
    for x in (14, 34, 54):
        s.line([(x - 3, 35, 31), (x - 3, 35, 38), (x + 1, 35, 40),
                (x + 4, 35, 37), (x + 4, 35, 31)], DETAIL)
    s.line([(7, 35, 20), (7, 35, 24), (64, 35, 24), (64, 35, 20)], BOLD)
