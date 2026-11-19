from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w3 import printed_check, sheet

DESCRIPTION = "A rubric sheet aligns three criteria with rising score columns and a marked cell in each row."


def draw(s):
    face = sheet(s, 102, 81, rise=(-.45, .89))
    face.rules(9, 68, [36], ink=BOLD)
    face.rect(9, 9, 83, 49, 2, EDGE)
    for x in (43, 59, 75):
        face.stroke([(x, 9), (x, 58)], EDGE)
    for v in (20, 32, 44):
        face.stroke([(9, v), (92, v)], DETAIL)
    for x, count in ((51, 1), (67, 2), (83, 3)):
        for i in range(count):
            bar_x = x + 4 * (i - (count - 1) / 2)
            face.stroke([(bar_x, 48), (bar_x, 53)], EDGE)
    for v, width, mark in ((38, 23, 67), (26, 19, 83), (14, 21, 51)):
        face.rules(14, v, [width], ink=EDGE)
        printed_check(face, mark, v, 5)
