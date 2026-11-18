from geometry import BOLD, EDGE
from scenes.redraws._w1 import prompt, terminal_console

DESCRIPTION = "A freestanding terminal displays a large command prompt followed by a short entered command."


def draw(s):
    terminal_console(s)
    prompt(s, -26, 0, 30, 9, BOLD)
    s.line([(-9, 0, 33), (8, 0, 33)], EDGE)
    s.line([(13, 0, 33), (22, 0, 33)], EDGE)
