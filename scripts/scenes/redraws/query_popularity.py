from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import front_bar, front_marks, outline, rule, search_display

DESCRIPTION = "A search analytics display ranks three queries with progressively shorter frequency bars."


def draw(s):
    p = search_display(s, 115, 88)
    outline(s, 10, 0, 54, 94, 14, 6, EDGE)
    front_marks(s, 19, 0, 61, "search", .72)
    rule(s, p, 30, 61, 34, DETAIL)
    for z, label_width, length in ((42, 23, 59), (27, 17, 44), (12, 20, 27)):
        rule(s, p, 12, z + 3, label_width, EDGE)
        front_bar(s, p, 45, z, length, 7, BOLD if length == 59 else EDGE)
