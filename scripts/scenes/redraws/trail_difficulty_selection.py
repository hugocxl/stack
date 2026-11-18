from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w5 import panel

DESCRIPTION = "A trail signpost carries three arrow boards with increasingly steep slope marks and a check badge beside the middle board."


def draw(s):
    s.box(27, 0, 0, 5, 6, 91, 1)
    for index, z in enumerate((26, 49, 72)):
        leftward = index == 1
        outline = [(0, z + 3), (8, z), (55, z), (65, z + 8), (55, z + 16),
                   (8, z + 16), (0, z + 13)]
        if leftward:
            outline = [(65 - x, v) for x, v in outline]
        point = lambda x, v: (x, 9, v)
        panel(s, outline, point, 3.8)
        run = (27, 19, 11)[index]
        rise = (4, 7, 10)[index]
        s.line([point(31 - run/2, z + 4), point(31 + run/2, z + 4 + rise)], EDGE)
        s.line([point(31 - run/2, z + 4), point(31 + run/2, z + 4)], DETAIL)
    badge(s, "check", 66, 9, 57, 9.5)
