from geometry import BOLD, EDGE
from scenes.redraws._w3 import Surface, printed_check, sheet, speech_outline

DESCRIPTION = "A marked assignment has a circled grade mark and an attached speech bubble with two feedback lines."


def draw(s):
    page = sheet(s, 77, 93, rise=(-.36, .93))
    page.rules(10, 75, [26], ink=EDGE)
    page.rules(10, 62, [31, 24, 34], gap=8)
    page.rules(10, 34, [32, 28, 34], gap=8)
    page.oval(56, 63, 11, 11, BOLD)
    printed_check(page, 56, 63, 8)
    comment = Surface(s, page.point(44, 19, -3), rise=page.rise, back=page.back)
    comment.plate(speech_outline(0, 0, 58, 34), 4)
    comment.rules(10, 22, [35, 26], gap=8, ink=EDGE)
