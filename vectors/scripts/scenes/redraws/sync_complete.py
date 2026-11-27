from math import cos, radians, sin

from geometry import BOLD
from scenes.redraws._kit import _strokes
from scenes.redraws._sf import BACK, plate, screen

DESCRIPTION = "Two thick curved arrows chase each other around a check mark."


def arrow_arc(a0, a1, r=40, w=9, head=13):
    outer = [((r + w/2)*cos(radians(a)), (r + w/2)*sin(radians(a))) for a in range(a0, a1 + 1, 4)]
    inner = [((r - w/2)*cos(radians(a)), (r - w/2)*sin(radians(a))) for a in range(a1, a0 - 1, -4)]
    t = radians(a1)
    tip_a = radians(a1 + 16)
    tip = (r*cos(tip_a), r*sin(tip_a))
    wing_o = ((r + head)*cos(t), (r + head)*sin(t))
    wing_i = ((r - head)*cos(t), (r - head)*sin(t))
    return outer + [wing_o, tip, wing_i] + inner


def sync_arrows(s, center, rx, ry=None, head=None):
    """Two thick curved arrows chasing each other around a viewer-facing centre."""
    at = screen(*center)
    w = rx*.22
    for a0, a1 in ((20, 150), (200, 330)):
        plate(s, at, arrow_arc(a0, a1, rx, w, w*1.45), w*.6, BACK)


def draw(s):
    at = screen()
    sync_arrows(s, (0, 0, 0), 40)
    for stroke in _strokes("check", 18):
        s.line([at(u, v) for u, v in stroke], BOLD)
