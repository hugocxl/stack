from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._kit import arrow
from scenes.redraws._w3 import Surface

DESCRIPTION = "Two dashed focus outlines lead along a pair of arrows to a solid focus outline on the active tile."


def draw(s):
    panel = Surface(s, (0, 0, 0), across=(.22, -.98), back=(-.98, -.22, 0))
    panel.plate(rounded(0, 0, 106, 78, 6), 13)
    panel.rules(9, 67, [25], ink=EDGE)
    for x, v, active in ((8, 36, False), (43, 36, False), (69, 7, True)):
        panel.rect(x + 4, v + 4, 16, 15, 2, DETAIL)
        panel.rules(x + 8, v + 11.5, [8])
        panel.stroke(rounded(x, v, 24, 23, 3), BOLD if active else EDGE,
                     closed=True, dashed=not active)
    arrow(s, [panel.point(34, 48), panel.point(41, 48)], EDGE, head=4)
    move = [(69, 47), (76, 46), (81, 41), (81, 33)]
    arrow(s, [panel.point(x, v) for x, v in move], EDGE, head=4)
