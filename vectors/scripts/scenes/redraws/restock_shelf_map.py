from geometry import BOLD, EDGE, oval
from scenes.redraws._w1 import stock_shelf, upright_profile

DESCRIPTION = "A location pin identifies the empty bay of a stock shelf."


def draw(s):
    stock_shelf(s, empty=((1, 2),))
    x, y, z = 20, 24, 50
    pin = [(x + u, z + v) for u, v in oval(0, 0, 10, 10, 0, 180, count=24)]
    pin += [(x - 8, z - 6), (x, z - 18), (x + 8, z - 6)]
    pin.reverse()
    upright_profile(s, pin, y, 2, EDGE)
    s.line([(a, y, b) for a, b in oval(x, z + .5, 3.8, 3.8, count=24)], BOLD)
