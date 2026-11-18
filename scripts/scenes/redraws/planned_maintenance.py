from geometry import EDGE, oval
from scenes.redraws._kit import badge

DESCRIPTION = "A striped traffic cone on a square rubber foot carries a clock badge."


def draw(s):
    s.box(-27, -27, 0, 54, 54, 6, 5)
    s.solid(oval(0, 0, 19, 19)[:-1], 6, 49,
            top=oval(0, 0, 4.8, 4.8)[:-1], crease=False)
    s.ellipse(0, 0, 55, 4.8, 4.8)
    for z in (24, 35):
        radius = 19 - (z - 6) * (19 - 4.8) / 49
        s.ellipse(0, 0, z, radius, radius, EDGE, -45, 135)
    badge(s, "clock", 12, -4, 41, 12)
