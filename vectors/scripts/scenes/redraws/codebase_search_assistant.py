from geometry import BOLD, DETAIL
from scenes.redraws._w2 import code_window, magnifier

DESCRIPTION = "A magnifier centers on a bold matching source line in a laptop code editor."


def draw(s):
    code_window(s, ((16, 48, 51, DETAIL), (28, 38, 66, BOLD),
                    (36, 27, 29, DETAIL), (26, 18, 46, DETAIL)))
    magnifier(s, 77, 3, 38, 18, direction=(.80, -.60))
