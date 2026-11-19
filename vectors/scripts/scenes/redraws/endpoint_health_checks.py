from geometry import BOLD, EDGE
from scenes.redraws._w1 import ethernet_port, pulse, router
from scenes.systems_shapes import bezel

DESCRIPTION = "A network endpoint displays a pulse trace beside its keyed Ethernet port."


def draw(s):
    router(s, 0, 0, width=78, depth=40, height=36)
    ethernet_port(s, 24, 20, 18, 13, 11)
    bezel(s, -32, 20, 7, 47, 21, EDGE, 2)
    s.line([(x - 28, 20, z + 17) for x, z in pulse(39, 9)], BOLD)
