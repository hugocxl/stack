from geometry import EDGE
from scenes.redraws._sf import coin_face, coin_stack, screen

DESCRIPTION = "A stack of coins rises until it meets a heavy cap bar held on two posts."


def draw(s):
    for x, y in ((-34, 0), (34, 0)):
        s.tube([(x, y, 0), (x, y, 66)], 2.4, EDGE)
    coin_stack(s, 0, 0, 0, 22, 12)
    s.box(-42, -6, 56, 84, 12, 8, 3)
    coin_face(s, lambda u, v: screen()(u + 62, v + 20), 15)
