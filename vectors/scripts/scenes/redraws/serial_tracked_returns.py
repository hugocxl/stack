from geometry import BOLD, oval
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import barcode, software_package

DESCRIPTION = "A curved return arrow hooks around the prominent serial barcode label on a returns carton."


def draw(s):
    software_package(s, 0, 0, 0, 1.26, show_code=False)
    barcode(s, -25, 26.46, 9, 39, 22)
    path = [(x, -1, z) for x, z in oval(48, 29, 18, 20, -106, 131, count=36)]
    arrow(s, path, BOLD, head=9)
