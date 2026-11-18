from math import hypot

from geometry import BOLD, oval
from scenes.redraws._kit import _screen, _strokes, badge

DESCRIPTION = "Two arrows form a synchronization loop with a check badge attached to its lower arc."


def sync_arrows(s, center, rx, ry, head):
    """Turn the kit's forward arrowhead along two opposing arcs."""
    _, chevron = _strokes("arrow", head)
    for start, end in ((114, 252), (294, 432)):
        arc = oval(0, 0, rx, ry, start, end, 32)
        (ax, ay), (bx, by) = arc[-2:]
        length = hypot(bx - ax, by - ay)
        tx, ty = (bx - ax)/length, (by - ay)/length
        s.line([_screen(*center, u, v) for u, v in arc], BOLD)
        s.line([_screen(*center, bx + (u - .75*head)*tx - v*ty,
                              by + (u - .75*head)*ty + v*tx)
                for u, v in chevron], BOLD)


def draw(s):
    sync_arrows(s, (0, 0, 0), 33, 29, 14)
    badge(s, "check", *_screen(0, 0, 0, 23, -21), 12.7)
