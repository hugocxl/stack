from geometry import DETAIL, EDGE
from scenes.redraws._kit import warning
from scenes.redraws._w5 import calendar_header, clipboard, printed_stroke, rect

DESCRIPTION = "A task clipboard shows an empty checkbox and a boxed calendar field beside a warning triangle."


def draw(s):
    face = clipboard(s, 65, 57)
    rect(s, face, 10, 31, 10, 10, 1.5, EDGE)
    printed_stroke(s, face, [(26, 38), (49, 38)], EDGE)
    printed_stroke(s, face, [(26, 32), (42, 32)], DETAIL)
    rect(s, face, 10, 8.5, 42, 19, 2, EDGE)
    calendar_header(s, face, 14, 11.5, .93)
    printed_stroke(s, face, [(33, 17.5), (47, 17.5)], EDGE)
    warning(s, 68, -21, 8, 34)
