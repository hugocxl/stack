from scenes.redraws._kit import badge
from scenes.redraws._w1 import dashboard_rows, status_monitor
from scenes.systems_shapes import bezel
from geometry import EDGE

DESCRIPTION = "A status dashboard lists three service rows beneath a large operational check badge."


def draw(s):
    status_monitor(s)
    bezel(s, -28, 0, 43, 34, 8, EDGE, 4)
    dashboard_rows(s, ((36, 32), (30, 27), (24, 34)))
    badge(s, "check", 34, 0, 56, 15)
