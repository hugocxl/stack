from scenes.redraws._kit import badge
from scenes.redraws._sf import cart, carton

DESCRIPTION = "A shopping cart still holds two parcels, and a clock badge shows it has been left waiting."


def draw(s):
    front = cart(s, -30, -22, 0)
    carton(s, -20, -14, 30, 22, 20, 18, tape=False)
    carton(s, 6, -10, 30, 18, 18, 24, tape=False)
    front()
    badge(s, "clock", 38, 22, 54, 12)
