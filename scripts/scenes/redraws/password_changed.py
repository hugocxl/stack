from geometry import BOLD, EDGE, rounded
from scenes.redraws._kit import _strokes, badge
from scenes.redraws._w5 import panel, rect

DESCRIPTION = "A recessed password field with a lock and four masked characters carries a check badge."


def draw(s):
    def face(u, v):
        return .83*u, -.17*u - .33*v, v

    panel(s, rounded(0, 0, 78, 35, 5), face, 7)
    rect(s, face, 6, 7, 65, 21, 3, EDGE)
    for stroke in _strokes("lock", 8.5):
        s.line([face(17 + u, 17 + v) for u, v in stroke], EDGE)
    (dot,) = _strokes("dot", 7.6)
    for x in (30, 39, 48, 57):
        s.line([face(x + u, 17 + v) for u, v in dot], BOLD)
    badge(s, "check", *face(74, 21), 12.5)
