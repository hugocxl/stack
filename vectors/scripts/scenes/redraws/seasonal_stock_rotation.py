from geometry import BOLD, DETAIL, oval
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import stock_shelf

DESCRIPTION = "A looping rotation arrow sweeps along the front row of a stocked shelf."


def draw(s):
    s.line([(x, y, 3) for x, y in oval(0, 4, 53, 40, 195, 333, count=31)], DETAIL)
    sweep = [(x, y, 3) for x, y in oval(0, 4, 53, 40, 195, -27, count=44)]
    arrow(s, sweep, BOLD, head=9)
    stock_shelf(s)
