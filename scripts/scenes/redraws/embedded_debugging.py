from geometry import EDGE
from scenes.redraws._w1 import code_brackets, firmware_chip

DESCRIPTION = "A magnifying glass frames three exposed legs of a coded microcontroller."


def draw(s):
    firmware_chip(s)
    code_brackets(s, lambda u, v: (u - 6, -v - 5, 15), 10, EDGE)
    s.tube([(-5, 35, 18), (-23, 53, 18)], 3.3, EDGE)
    s.ring(4, 24, 16, 16, 14, 3, wall=2.8, ink=EDGE)
