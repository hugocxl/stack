from geometry import BOLD
from scenes.redraws._kit import _screen, _strokes, badge
from scenes.redraws.message_delivered import message

DESCRIPTION = "A rounded message bubble carries a double-check badge on its lower-right corner."


def draw(s):
    x, y, z = message(s)
    radius = 13
    badge(s, "check", x, y, z, radius)
    (check,) = _strokes("check", radius * .62)
    s.line([_screen(x, y, z, u + 3.9, v, back=-.01)
            for u, v in check[1:]], BOLD)
