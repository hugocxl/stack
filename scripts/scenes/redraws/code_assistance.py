from geometry import DETAIL, EDGE
from scenes.redraws._w2 import caret, code_window, rule

DESCRIPTION = "A laptop code editor shows a two-line ghost suggestion extending from the insertion caret."


def draw(s):
    point = code_window(s, ((16, 46, 38, EDGE), (26, 37, 46, EDGE), (26, 27, 19, EDGE)))
    caret(s, point, 51, 27)
    rule(s, point, 58, 27, 35, DETAIL)
    rule(s, point, 34, 17, 46, DETAIL)
