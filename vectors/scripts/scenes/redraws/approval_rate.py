from math import cos, radians, sin

from geometry import BOLD, DETAIL
from scenes.redraws._kit import _strokes
from scenes.redraws._sf import BACK, plate, screen

DESCRIPTION = "A thick progress ring is filled three quarters of the way around a bold check mark."


def band(a0, a1, r, w):
    return ([((r + w/2)*cos(radians(a)), (r + w/2)*sin(radians(a))) for a in range(a0, a1 + 1, 3)] +
            [((r - w/2)*cos(radians(a)), (r - w/2)*sin(radians(a))) for a in range(a1, a0 - 1, -3)])


def draw(s):
    at = screen()
    s.line([at(44*cos(radians(a)), 44*sin(radians(a))) for a in range(0, 361, 3)], DETAIL)
    plate(s, at, band(-180, 90, 44, 14), 7, BACK)
    for stroke in _strokes("check", 18):
        s.line([at(u, v) for u, v in stroke], BOLD)
