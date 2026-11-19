from geometry import BOLD, DETAIL
from scenes.redraws._w2 import column_row

DESCRIPTION = "A bold benchmark rule crosses three bars and separates the bars above and below target."


def draw(s):
    column_row(s, (38, 73, 56))
    s.line([(-10, 20, 48), (83, -30, 48)], BOLD)
    for x, y in ((-10, 20), (83, -30)):
        s.line([(x, y, 43), (x, y, 53)], DETAIL)
