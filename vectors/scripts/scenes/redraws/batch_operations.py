from scenes.redraws._kit import badge
from scenes.redraws._sf import BACK, plate, screen, squircle
from geometry import DETAIL

DESCRIPTION = "A fanned stack of three thick cards carries a bolt badge for a batch operation."


def draw(s):
    at = screen()
    for k in range(3):
        c = lambda u, v, k=k: at(u - 48 + k*12, v - 30 + k*12)
        plate(s, c, squircle(84, 56, 8), 5, BACK)
        s.line([c(12, 38), c(56, 38)], DETAIL)
        s.line([c(12, 26), c(40, 26)], DETAIL)
    badge(s, "bolt", *at(60, 46), 13)
