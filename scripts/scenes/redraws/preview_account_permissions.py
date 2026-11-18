from geometry import BOLD, EDGE, oval, rounded
from scenes.redraws._w3 import Surface, profile_art

DESCRIPTION = "A magnifying glass overlaps an account page with a profile avatar and a column of permission switches."


def draw(s):
    page = Surface(s, (0, 0, 0), rise=(-.19, .98), back=(0, -.98, 0), across=(.96, -.28))
    page.plate(rounded(0, 0, 77, 87, 6), 8)
    page.oval(23, 67, 12, 12, EDGE)
    profile_art(page, 23, 67, 14)
    page.rules(43, 71, [24], ink=EDGE)
    page.rules(43, 62, [17])
    page.rules(8, 49, [61], ink=EDGE)
    for v, width in ((35, 25), (23, 20), (11, 26)):
        page.rules(13, v + 3, [width])
        page.rect(47, v, 14, 6, 3)
    lens = Surface(s, page.point(73, 37, -15), across=(.707, -.707))
    align = lens.viewer_axes(0, 0)
    s.tube([lens.point(*align(9, -9)), lens.point(*align(24, -24))], 3.1)
    lens.plate([align(a, b) for a, b in oval(0, 0, 15, 15)[:-1]], 3)
    lens.stroke([align(a, b) for a, b in oval(0, 0, 11, 11)], BOLD)
