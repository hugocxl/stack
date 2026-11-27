from geometry import DETAIL
from scenes.redraws._kit import _screen, badge
from scenes.redraws._sf import lip, turned

DESCRIPTION = "A spinning top stands still on its point, carrying a pause badge."


def draw(s):
    turned(s, [(.4, 0), (5, 7), (14, 20), (23, 34), (25, 38), (21, 42), (9, 45)], steps=4)
    lip(s, 0, 0, 37, 24, DETAIL, -50, 140)
    turned(s, [(3.4, 44), (3.4, 60), (2.6, 62)], steps=2)
    badge(s, "pause", *_screen(0, 0, 0, 38, 44), 12.5)
