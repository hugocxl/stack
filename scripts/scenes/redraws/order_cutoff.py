from geometry import BOLD
from scenes.redraws._kit import badge
from scenes.redraws._w1 import software_package

DESCRIPTION = "A taped shipping carton has an attached clock badge with a bold deadline tick."


def draw(s):
    software_package(s, 0, 0, 0, show_code=False)
    x, y, z = 27, 3, 37
    badge(s, "clock", x, y, z, 14)
    s.line([(x + 5.6, y - 5.6, z), (x + 7.4, y - 7.4, z)], BOLD)
