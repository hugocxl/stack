from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w1 import code_brackets, connector, ethernet_port

DESCRIPTION = "A keyed cable plug enters a socket beneath the code symbol on an API port."


def draw(s):
    s.box(-28, -22, 0, 56, 22, 49, 4)
    code_brackets(s, lambda u, v: (u, 0, 35 + v), 13, BOLD)
    ethernet_port(s, 0, 0, 13, 26, 18, EDGE)
    connector(s, 0, 10, 6)
    for x in (-6, 6):
        s.line([(x, 0, 20), (x, 3, 20)], DETAIL)
