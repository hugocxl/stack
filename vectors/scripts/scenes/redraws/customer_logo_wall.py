from geometry import EDGE, rounded
from scenes.redraws._w4 import front_surface, upright

DESCRIPTION = "A thick wall panel displays six distinct geometric logos in two rows."


def draw(s):
    angle = -16
    upright(s, rounded(0, 0, 105, 66, 3), 10, 15, angle=angle)
    wall = front_surface(s, angle=angle, y=10)
    wall.frame(5, 5, 95, 56, 2)
    wall.outline([(14, 40), (22, 54), (30, 40)], EDGE)
    wall.oval(52, 47, 8, 8, EDGE)
    wall.oval(52, 47, 3.5, 3.5, EDGE)
    wall.outline([(74, 43), (81, 53), (91, 53), (84, 43)], EDGE)
    wall.outline([(13, 18), (22, 27), (31, 18), (22, 9)], EDGE)
    wall.outline([(44, 18), (48, 25), (56, 25), (60, 18), (56, 11), (48, 11)], EDGE)
    wall.oval(79, 18, 4.5, 4.5, EDGE)
    wall.oval(87, 18, 4.5, 4.5, EDGE)
