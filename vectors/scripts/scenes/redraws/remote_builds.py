from geometry import BOLD, EDGE, oval
from scenes.redraws._w1 import laptop

DESCRIPTION = "A laptop terminal displays a hammer inside the outline of a cloud."


def draw(s):
    y = laptop(s, -43, -8, w=86, h=63, depth=36)
    cloud = [(-25, 22), *oval(-25, 30, 9, 8, 270, 111, 12),
             *oval(-11, 40, 12, 11, 159, 66, 12),
             *oval(8, 38, 12, 11, 110, 18, 12),
             *oval(23, 31, 11, 9, 95, -90, 12), (-25, 22)]
    s.line([(x, y, z) for x, z in cloud], EDGE)

    hammer = [(-13, 29), (-3, 38), (-7, 42), (2, 50), (11, 41),
              (5, 36), (1, 39), (-9, 25), (-13, 29)]
    s.line([(x * .85 + 2, y, 36 + (z - 36) * .79) for x, z in hammer], BOLD)
