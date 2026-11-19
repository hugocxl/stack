from scenes.redraws._kit import badge
from scenes.redraws._w1 import stock_shelf

DESCRIPTION = "Cartons fill the shelves of a stock rack, with a plus badge in the remaining open bay."


def draw(s):
    stock_shelf(s, empty=((1, 2),))
    badge(s, "plus", 20, 17, 44, 9)
