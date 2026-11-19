from geometry import BOLD, EDGE
from scenes.commerce import shopping_cart
from scenes.systems_shapes import bezel

DESCRIPTION = "A shopping cart carries a spend meter with a currency sign and a marked shipping threshold."


def draw(s):
    shopping_cart(s)
    # The meter is clipped across the near basket wall.
    s.box(0, 61, 37, 89, 5, 24, 2.5)
    y = 66
    points = [(-2, 1), (-4, 3), (-2, 5), (2, 5), (4, 3), (2, 1),
              (-2, -1), (-4, -3), (-2, -5), (2, -5), (4, -3)]
    s.line([(14 + x, y, 49 + z) for x, z in points], EDGE)
    s.line([(14, y, 42), (14, y, 56)], EDGE)
    bezel(s, 27, y, 44, 53, 10, EDGE, 4)
    s.line([(31, y, 49), (58, y, 49)], BOLD)
    s.line([(66, y, 41), (66, y, 57)], EDGE)
    s.line([(63, y, 57), (66, y, 54), (69, y, 57), (63, y, 57)], EDGE)
