from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface, photo_art

DESCRIPTION = "An open magazine with a masthead, illustration and text columns rests on an angled reading desk."


def draw(s):
    for x in (11, 79):
        s.box(x, 18, 0, 7, 31, 32, 1.5)
    desk = Surface(s, (0, 58, 31), rise=(-.84, .54), back=(0, -.54, -.84))
    desk.plate(rounded(0, 0, 101, 65, 3), 5)
    s.tube([desk.point(4, 4, -1), desk.point(97, 4, -1)], 1.4)
    for x, left in ((9, True), (51, False)):
        page = Surface(s, desk.point(x, 9, -2), rise=desk.rise, back=desk.back)
        outline = [(0, 1), (7, 0), (35, 0), (42, 3), (42, 48), (35, 46), (7, 46), (0, 48)]
        page.plate(outline, 2)
        if left:
            page.rules(5, 39, [32], ink=BOLD)
            photo_art(page, 5, 16, 32, 18)
            page.rules(5, 10, [30, 21], gap=5)
        else:
            page.rules(5, 39, [29], ink=EDGE)
            for col in (5, 23):
                page.rules(col, 31, [13, 13, 10, 13, 11], gap=5)
