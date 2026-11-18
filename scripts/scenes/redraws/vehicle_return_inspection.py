from scenes.redraws.car_park_height_limit import car
from scenes.redraws.hotel_search import magnifier

DESCRIPTION = "A magnifying glass sits over the passenger door of a rental car."


def draw(s):
    car(s)
    magnifier(s, 41, 40, 23, 13)
