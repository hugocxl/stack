from geometry import BOLD, DETAIL, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "Two opposing crop corners frame the mountains and sun in a landscape photograph."


def draw(s):
    photo = Surface(s, (0, 0, 0), rise=(-.20, .98), back=(0, -1, 0), across=(.96, -.28))
    photo.plate(rounded(0, 0, 107, 71, 4), 5)
    photo.rect(7, 7, 93, 57, 2)
    photo.oval(72, 48, 6, 6, DETAIL)
    photo.stroke([(7, 18), (34, 40), (48, 26), (65, 39), (100, 19)])
    photo.stroke([(24, 39), (24, 55), (45, 55)], BOLD)
    photo.stroke([(63, 14), (83, 14), (83, 26)], BOLD)
