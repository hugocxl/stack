from geometry import DETAIL, EDGE
from scenes.redraws._w5 import avatar_mark, clipboard, rect
from scenes.redraws.notifications_grouped import bell_badge

DESCRIPTION = "A task clipboard shows a checkbox and an assignee row beside a bell badge."


def draw(s):
    face = clipboard(s, 65, 57)
    rect(s, face, 10, 31, 10, 10, 1.5, EDGE)
    s.line([face(25, 37), face(48, 37)], EDGE)
    s.line([face(25, 31), face(43, 31)], DETAIL)
    s.line([face(10, 24), face(52, 24)], DETAIL)
    avatar_mark(s, face, 17, 14, .82)
    s.line([face(28, 16), face(48, 16)], EDGE)
    s.line([face(28, 11), face(43, 11)], DETAIL)
    bell_badge(s, face(62, 41), 12.7)
