from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import software_package

DESCRIPTION = "Two matching parcels connect to separate marks on a shipment timeline."


def draw(s):
    x, y = -30, 8
    arrow(s, [(x, y, 94), (x, y, -2)], EDGE, head=6)
    for z, box_x in ((75, 8), (24, 18)):
        s.line([(x + 4, y, z), (box_x - 17, y, z)], DETAIL)
        s.face([(a, y, b) for a, b in oval(x, z, 4.8, 4.8, count=24)[:-1]], EDGE)
    software_package(s, 8, 0, 61, .76, show_code=False)
    software_package(s, 18, 0, 10, .76, show_code=False)
