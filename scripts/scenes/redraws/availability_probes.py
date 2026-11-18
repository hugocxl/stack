from geometry import BOLD
from scenes.redraws._kit import coin
from scenes.redraws._w1 import pulse, server_tower

DESCRIPTION = "A round health readout on a server tower shows a pulse trace above its drive bays."


def draw(s):
    server_tower(s)
    y = coin(s, 0, 2, 46, 13)
    s.line([(x - 11, y + .01, 45 + z) for x, z in pulse(22, 10)], BOLD)
