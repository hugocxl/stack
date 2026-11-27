from geometry import EDGE
from scenes.redraws._w3 import classroom_chair

DESCRIPTION = "Three chairs stand behind a long panel table with a microphone at each seat."


def draw(s):
    for i in range(3):
        classroom_chair(s, -54 + i*38, -44, 1.9)
    s.box(-60, -6, 0, 120, 26, 24, 2)
    s.box(-64, -10, 24, 128, 34, 4, 2)
    for i in range(3):
        x = -38 + i*36
        s.disk(x, 0, 28, 4, 4, 2)
        s.tube([(x, 0, 30), (x + 4, 6, 42)], 1, EDGE)
        s.disk(x + 4, 6, 41, 2.4, 2.4, 3)
