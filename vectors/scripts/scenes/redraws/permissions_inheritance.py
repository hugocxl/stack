from geometry import EDGE
from scenes.redraws._w5 import key_mark, tabbed_folder

DESCRIPTION = "A branch connects a parent folder marked with a key to a smaller child folder."


def draw(s):
    s.line([(40, 0, 39), (54, 0, 39), (54, 0, 12), (63, 0, 12)], EDGE)
    parent = tabbed_folder(s, 0, 0, 23)
    key_mark(s, parent, 12.5, 12, .73, angle=9)
    tabbed_folder(s, 63, 0, 0, .74)
