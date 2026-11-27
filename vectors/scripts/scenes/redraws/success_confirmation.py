from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._kit import _strokes
from scenes.redraws._sf import BACK, plate, screen

DESCRIPTION = "A thick circular seal faces the viewer with a single bold checkmark."


def draw(s):
    at = screen()
    plate(s, at, oval(0, 0, 44, 44, count=96)[:-1], 9, BACK)
    s.line([at(u, v) for u, v in oval(0, 0, 36, 36, count=96)], DETAIL)
    for stroke in _strokes("check", 25):
        s.line([at(u, v) for u, v in stroke], BOLD)
