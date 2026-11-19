from math import pi, sin

from geometry import DETAIL, EDGE
from scenes.redraws._kit import warning
from scenes.redraws.program_impact import community_house

DESCRIPTION = "Floodwater crosses the lower part of a house door beneath an attached warning triangle."


def draw(s):
    community_house(s, door=False)
    def waterline(x):
        return 11 + 1.1 * sin((x + 29) * pi / 14.5)

    s.line([(-8, 18, waterline(-8)), (-8, 18, 22),
            (6, 18, 22), (6, 18, waterline(6))], EDGE)
    s.line([(x, 18, waterline(x)) for x in range(-29, 30)], EDGE)
    s.line([(29, y, 11 + .9 * sin((y - 18) * pi / 9))
            for y in range(18, -19, -1)], EDGE)
    for y, start, end in ((27, -40, 38), (37, -32, 23), (47, -18, 22)):
        s.line([(start + (end - start) * i / 48,
                 y + 1.6 * sin(i * pi / 8), 10) for i in range(49)], DETAIL if y == 47 else EDGE)
    warning(s, 32, 2, 28, 26)
