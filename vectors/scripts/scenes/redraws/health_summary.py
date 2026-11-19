from geometry import BOLD
from scenes.redraws._w1 import dashboard_rows, pulse, status_monitor

DESCRIPTION = "A status monitor shows one pulse trace above three compact service rows."


def draw(s):
    status_monitor(s)
    s.line([(x - 28, 0, z + 46) for x, z in pulse(55, 8)], BOLD)
    dashboard_rows(s, ((36, 24), (30, 33), (24, 27)))
