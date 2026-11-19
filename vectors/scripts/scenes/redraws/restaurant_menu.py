from geometry import DETAIL, rounded
from scenes.redraws._w5 import course_rows, panel, place_setting, printed_stroke

DESCRIPTION = "A two-panel restaurant menu displays a place setting and two dish-and-price rows."


def draw(s):
    back = lambda u, z: (u, 3 + .52 * (u - 25), z)
    front = lambda u, z: (u, 3 - .23 * (u - 25), z)
    panel(s, rounded(0, 0, 25, 62, 1), back, 2.6)
    panel(s, rounded(25, 0, 54, 62, 1), front, 2.6)
    place_setting(s, front, 52, 46, 8.5)
    printed_stroke(s, front, [(33, 34), (71, 34)], DETAIL)
    course_rows(s, front, 35, 26, (18, 20), prices=True)
