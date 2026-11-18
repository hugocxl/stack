from geometry import EDGE
from scenes.redraws._w4 import product_laptop

DESCRIPTION = "An open laptop shows one large, fully drawn switch in a sparse product wireframe."


def draw(s):
    screen = product_laptop(s)
    screen.frame(20, 21, 43, 20, 10, EDGE)
    screen.oval(52, 31, 6.5, 6.5, EDGE)
