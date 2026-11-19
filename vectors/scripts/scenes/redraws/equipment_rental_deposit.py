from geometry import DETAIL, EDGE, oval
from scenes.redraws._w5 import clipboard, currency_mark, printed_stroke, rect

DESCRIPTION = "An equipment-rental agreement on a clipboard shows a wrench above a boxed deposit amount."


def draw(s):
    face = clipboard(s, 53, 66)
    point = lambda u, v: (18 + .82 * u + .38 * v, 45 - .41 * u + .84 * v)
    head = oval(0, 0, 7, 7, 29, 151, 14)
    contour = [*head, (-6, 3.5), (-1, 3), (-1, -3), (-6, -3.5),
               (-4, -5.5), (0, -7), (6, -4), (23, -4), (25, -2),
               (25, 2), (23, 4), (6, 4), head[0]]
    printed_stroke(s, face, [point(u, v) for u, v in contour], EDGE)
    printed_stroke(s, face, [(10, 31), (40, 31)], DETAIL)
    rect(s, face, 9, 8, 35, 15, 2)
    currency_mark(s, face, 17, 15.5, 4.5)
    printed_stroke(s, face, [(24, 15.5), (38, 15.5)], EDGE)
