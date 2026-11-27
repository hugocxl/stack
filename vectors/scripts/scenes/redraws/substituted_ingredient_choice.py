from geometry import DETAIL
from scenes.redraws._sf import BACK, chevron_arrow, lip, plate, screen, turned

DESCRIPTION = "A bold arrow leads from one spice jar to the jar that replaces it."


def jar(s, x, y, tall):
    turned(s, [(14, 0), (15, 2), (15, tall), (12, tall + 3)], x, y, 0, steps=2)
    turned(s, [(12.5, tall + 3), (12.5, tall + 11)], x, y, 0, steps=1)
    lip(s, x, y, tall*.5, 15, DETAIL, -40, 130)


def draw(s):
    jar(s, -50, 20, 34)
    plate(s, lambda u, v: screen()(u - 22, v + 18), chevron_arrow(40, 8, 16), 4, BACK)
    jar(s, 40, -20, 40)
