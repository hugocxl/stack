from scenes.redraws._w5 import van
from scenes.redraws.hotel_search import magnifier

DESCRIPTION = "A magnifying glass covers the front wheel arch of a fleet van."


def draw(s):
    van(s)
    magnifier(s, 63, 39, 12, 13.5)
