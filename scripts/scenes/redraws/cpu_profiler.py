from geometry import BOLD
from scenes.redraws._w1 import firmware_chip

DESCRIPTION = "A utilization trace steps across the inset face of a pin-legged processor."


def draw(s):
    firmware_chip(s)
    trace = [(-18, 6), (-11, 6), (-11, -2), (-4, -2), (-4, 3),
             (3, 3), (3, -10), (10, -10), (10, -5), (18, -5)]
    s.line([(x, y, 15) for x, y in trace], BOLD)
