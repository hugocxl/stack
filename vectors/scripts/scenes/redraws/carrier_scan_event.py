from geometry import BOLD
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import barcode, software_package

DESCRIPTION = "A diagonal scan beam crosses the barcode on a taped shipping carton."


def draw(s):
    software_package(s, 0, 0, 0, show_code=False)
    barcode(s, -23, 21, 7, 44, 23)
    arrow(s, [(-26, 21, 11), (24, 21, 25)], BOLD, head=5)
