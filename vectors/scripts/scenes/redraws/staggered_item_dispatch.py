from geometry import DETAIL, EDGE
from scenes.redraws._sf import carton

DESCRIPTION = "Two matching parcels sit at separate marks along a dashed shipment timeline."


def draw(s):
    s.line([(-80, 20, 0), (80, 20, 0)], DETAIL, dashed=True)
    for x in (-50, 30):
        s.disk(x, 20, 0, 4, 4, 1.5)
    for x in (-50, 30):
        carton(s, x - 16, -12, 0, 32, 26, 26)
    s.line([(76, 16, 0), (82, 20, 0), (76, 24, 0)], EDGE)
