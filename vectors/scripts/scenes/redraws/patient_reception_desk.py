from geometry import BOLD
from scenes.redraws._w4 import reception_counter

DESCRIPTION = "A clinic reception counter has a prominent medical cross and a receptionist's monitor and chair behind it."


def draw(s):
    front = reception_counter(s, clinic=True)
    front.outline([(34, 35), (43, 35), (43, 26), (52, 26), (52, 17),
                   (43, 17), (43, 8), (34, 8), (34, 17), (25, 17),
                   (25, 26), (34, 26)], BOLD)
