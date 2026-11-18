from geometry import BOLD, EDGE
from scenes.redraws._w3 import Surface, podium_art, sheet

DESCRIPTION = "A talk proposal projects from an open envelope and shows a lectern, a title and three abstract lines."


def draw(s):
    back = Surface(s, (0, 0, 0))
    back.plate([(0, 0), (90, 0), (90, 45), (45, 77), (0, 45)], 4)
    page = sheet(s, 66, 71, origin=(12, 1, 12), rise=(0, 1), depth=2)
    podium_art(page, 26, 52, 22)
    page.rules(9, 34, [43], ink=BOLD)
    page.rules(9, 25, [39, 44, 30], gap=6)
    pocket = Surface(s, (0, 5, 0))
    pocket.plate([(0, 0), (90, 0), (90, 37), (48, 18), (0, 37)], 2)
    pocket.stroke([(2, 1), (31, 20)], EDGE)
    pocket.stroke([(88, 1), (63, 21)], EDGE)
