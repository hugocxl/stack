from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import code_window, rule, speech_bubble

DESCRIPTION = "An explanatory speech bubble points to a selected line in a laptop code editor."


def draw(s):
    point = code_window(s, ((16, 46, 35, DETAIL), (26, 36, 53, BOLD),
                            (34, 26, 32, DETAIL), (25, 17, 40, DETAIL)))

    def bubble(x, z):
        return 56 + x, 3, 44 + z

    speech_bubble(s, bubble, 47, 32, tail=.25, depth=4)
    rule(s, bubble, 8, 21, 31, EDGE)
    rule(s, bubble, 8, 11, 23, DETAIL)
