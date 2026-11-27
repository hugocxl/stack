from math import cos, radians, sin

from geometry import DETAIL
from scenes.redraws._sf import ground, plate

DESCRIPTION = "Two thick jigsaw pieces slide together, one knob meeting its matching socket."

S, K = 52, 9


def knob(sign, base):
    return [(base + sign*(K*.35 + K*cos(radians(a))), S/2 + K*sin(radians(a))) for a in range(-130, 131, 12)]


def draw(s):
    left = [(0, 0), (S, 0), (S, S*.32)] + knob(1, S)[::1] + [(S, S*.68), (S, S), (0, S)]
    socket = [(K*.35 + K*cos(radians(a)), S/2 + K*sin(radians(a))) for a in range(130, -131, -12)]
    right = [(0, 0), (S, 0), (S, S), (0, S), (0, S*.68)] + socket + [(0, S*.32)]
    plate(s, ground(-S - 6, -S/2, 8), left, 8, (0, 0, -1))
    plate(s, ground(6, -S/2, 8), right, 8, (0, 0, -1))
