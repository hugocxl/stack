from math import cos, radians, sin

from geometry import EDGE
from scenes.redraws._w4 import Surface, folder_emblem, front_surface, support_mark

DESCRIPTION = "Three stepped dividers on a tabbed topic index show a folder, a gear, and a headset."


def draw(s):
    base = front_surface(s, angle=-20, z=8, lean=.33)
    for layer, u in ((2, 66), (1, 37), (0, 8)):
        def place(a, b):
            x, y, z = base.at(a, b)
            return x - layer*5, y - layer*5, z + layer*9

        page = Surface(s, place)
        page.slab([(0, 0), (104, 0), (104, 55), (u + 25, 55),
                   (u + 22, 72), (u + 3, 72), (u, 55), (0, 55)], 4)
        if layer == 2:
            support_mark(page, u + 12, 63, .44)
        elif layer == 1:
            teeth = []
            for tooth in range(32):
                angle = radians(tooth * 360 / 32)
                radius = 7 if tooth % 4 in (1, 2) else 5.4
                teeth.append((u + 12 + radius*cos(angle), 63 + radius*sin(angle)))
            page.outline(teeth, EDGE)
            page.oval(u + 12, 63, 2.4, 2.4, EDGE)
        else:
            folder_emblem(page, u + 6, 58, 13, 9)
            for v, width in ((43, 42), (32, 64), (20, 54)):
                page.rows(12, v, (width,), ink=EDGE)
