from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w4 import desktop_display, front_surface, upright

DESCRIPTION = "A small overhead spotlight casts a cone onto a single control on a display."


def draw(s):
    angle = -14
    stand = front_surface(s, angle=angle, y=0, z=22)
    s.tube([stand.at(36, 51), stand.at(36, 95), stand.at(38, 99),
            stand.at(49, 99)], 2.2)
    face = desktop_display(s, width=98, height=63, angle=angle)
    shade = [(38, 100), (42, 113), (56, 113), (60, 100)]
    upright(s, shade, 9, 12, angle=angle)
    face.line([(38, 78), (26, 23)], DETAIL)
    face.line([(60, 78), (72, 23)], DETAIL)
    face.frame(32, 17, 34, 16, 6, BOLD)
    face.line([(42, 25), (56, 25)], EDGE)
