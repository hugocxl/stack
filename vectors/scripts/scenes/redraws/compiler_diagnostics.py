from geometry import DETAIL, EDGE
from scenes.redraws._kit import warning
from scenes.redraws._w1 import prompt, terminal_console

DESCRIPTION = "A warning triangle touches the highlighted diagnostic line on a compiler terminal."


def draw(s):
    terminal_console(s)
    prompt(s, -25, 0, 37, 4.5)
    s.line([(-8, 0, 37), (20, 0, 37)], DETAIL)
    s.line([(-24, 0, 23), (26, 0, 23)], EDGE)
    s.line([(-24, 0, 15), (-4, 0, 15)], DETAIL)
    warning(s, 30, 2, 12, 27)
