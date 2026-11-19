from geometry import BOLD, EDGE
from scenes.redraws._w4 import bezier_path, front_surface

DESCRIPTION = "A looped product hangtag displays a large map pin above its information lines."


def draw(s):
    tag = front_surface(s, angle=-24, z=6, lean=.33)
    tag.slab([(4, 0), (59, 0), (63, 4), (63, 66), (50, 81),
              (13, 81), (0, 66), (0, 4)], 6)
    tag.oval(31.5, 72, 4, 4, EDGE)
    s.tube(bezier_path(tag.at(31.5, 72),
                       (tag.at(34, 86), tag.at(56, 97), tag.at(68, 94)),
                       (tag.at(81, 88), tag.at(47, 83), tag.at(34, 75))), 1.2)
    pin = bezier_path((31.5, 25),
                      ((27, 30), (16, 40), (16, 49)),
                      ((16, 69), (47, 69), (47, 49)),
                      ((47, 40), (36, 30), (31.5, 25)))
    tag.line(pin, BOLD)
    tag.oval(31.5, 50, 5.5, 5.5, EDGE)
    tag.rows(14, 17, (35,), ink=EDGE)
    tag.rows(14, 9, (24,))
