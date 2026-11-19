from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w1 import laptop, prompt

DESCRIPTION = "A laptop terminal lists dotted network addresses with a check badge at the upper corner."


def draw(s):
    y = laptop(s, 0, 0, 74, 51, 33)
    for z, widths in ((17, (5.5, 6, 4, 5)), (27, (5, 4, 6, 6)), (37, (6, 4, 5, 4))):
        prompt(s, 9, y, z, 1.7, DETAIL)
        x = 22
        for index, width in enumerate(widths):
            s.line([(x, y, z), (x + width, y, z)], EDGE)
            x += width + 2.5
            if index < len(widths) - 1:
                s.line([(x, y, z), (x + .75, y, z)], EDGE)
                x += 3.5
    badge(s, "check", 71, 1, 49, 12)
