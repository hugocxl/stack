from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w1 import pulse, status_monitor
from scenes.systems_shapes import bezel

DESCRIPTION = "An uptime monitor displays a test pulse and a small flask in its screen header."


def draw(s):
    status_monitor(s)
    s.line([(-29, 0, 44), (29, 0, 44)], DETAIL)
    s.line([(-28, 0, 51), (-1, 0, 51)], DETAIL)
    flask = [(15, 56), (22, 56), (22, 51.5), (27, 46),
             (26, 45), (11, 45), (10, 46), (15, 51.5), (15, 56)]
    s.line([(x, 0, z) for x, z in flask], EDGE)
    bezel(s, -30, 0, 24, 60, 15, DETAIL, 1)
    s.line([(x - 26, 0, 30 + z) for x, z in pulse(52, 7)], BOLD)
