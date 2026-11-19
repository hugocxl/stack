from geometry import EDGE
from scenes.redraws._kit import _strokes, badge
from scenes.redraws._w5 import clipboard, rect

DESCRIPTION = "A clipboard holds a three-row completed checklist and a large check badge."


def draw(s):
    face = clipboard(s, 60, 64)
    (check,) = _strokes("check", 4.4)
    for height, end in ((42, 47), (28, 43), (14, 38)):
        rect(s, face, 10, height - 4.6, 9.2, 9.2, 1, EDGE)
        s.line([face(14.6 + u, height + v) for u, v in check], EDGE)
        s.line([face(25, height), face(end, height)])
    badge(s, "check", *face(57, 22), 14)
