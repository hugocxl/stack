from geometry import DETAIL
from scenes.redraws._w4 import Surface, magnifier
from scenes.redraws.pharmacy_pickup_window import prescription_bottle

DESCRIPTION = "A diagonal magnifier overlaps the wraparound label of a capped prescription bottle."


def draw(s):
    prescription_bottle(s, 0, 0, 0, 1.65)

    def place(u, v):
        horizontal = .81*u + .59*v
        return 27 + horizontal*.58, -10 - horizontal*.58, 51 + .68*u - .93*v

    lens = Surface(s, place)
    magnifier(lens, 0, 0, 17)
    lens.line([(-8, -7), (-4, -4), (1, 0), (7, 4)], DETAIL)
    lens.line([(-9, 0), (-5, 3), (0, 6), (4, 9)], DETAIL)
