from scenes.commerce import shopping_cart
from scenes.redraws._kit import badge

DESCRIPTION = "A shopping cart still holds two products, and a clock badge shows it has been left waiting."


def draw(s):
    shopping_cart(s)
    badge(s, "clock", 30, 78, 60, 16)
