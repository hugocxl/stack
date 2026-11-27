from scenes.redraws._kit import badge
from scenes.redraws._sf import coin_face, coin_stack, screen

DESCRIPTION = "A short stack of coins and a standing coin carry a return badge for a reimbursement."


def draw(s):
    coin_stack(s, -14, 0, 0, 24, 6)
    coin_face(s, lambda u, v: screen()(u + 40, v + 10), 18)
    badge(s, "back", 50, -20, 60, 12)
