from geometry import EDGE
from scenes.redraws._kit import _screen, _strokes, badge

DESCRIPTION = "Three Wi-Fi arcs carry a check badge at their base."


def draw(s):
    for stroke in _strokes("wifi", 47):
        s.line([_screen(0, 0, 0, u, v) for u, v in stroke], EDGE)
    badge(s, "check", *_screen(0, 0, 0, 0, -29), 15)
