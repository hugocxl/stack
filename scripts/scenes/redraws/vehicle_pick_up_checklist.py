from geometry import BOLD, DETAIL
from scenes.redraws._w5 import car_mark, clipboard, rect

DESCRIPTION = "A rental pickup clipboard shows a car pictogram above three empty checkboxes."


def draw(s):
    face = clipboard(s, w=49, h=66)
    car_mark(s, face, 24.5, 43, .88, BOLD)
    for z, length in ((27, 23), (17, 17), (7, 21)):
        rect(s, face, 8, z, 6.5, 6.5, .75)
        s.line([face(18, z + 3.3), face(18 + length, z + 3.3)], DETAIL)
