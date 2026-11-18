from math import pi, sin

from geometry import BOLD
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import server_unit

DESCRIPTION = "A curved arrow returns from the right rack server to an identical rack server on the left."


def draw(s):
    server_unit(s, 17, -12, width=36, depth=27, height=24)
    server_unit(s, -49, 21, width=36, depth=27, height=24)

    path = []
    for step in range(31):
        progress = step / 30
        x = 38 - 73 * progress
        y = -23 + 36 * progress
        z = 25 + 34 * sin(pi * progress) ** 1.7
        path.append((x, y, z))
    arrow(s, path, BOLD, head=10)
