from geometry import BOLD
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import envelope

DESCRIPTION = "Three envelopes ride a continuous message stream that ends in a forward arrow."


def draw(s):
    arrow(s, [(-65, 12, 37), (-38, 10, 34), (-18, 7, 28),
              (0, 5, 23), (19, 3, 18), (37, 1, 12),
              (56, -2, 7), (67, -5, 5)], BOLD, head=10)
    for x, y, z in ((22, 2, 4), (-15, 6, 15), (-53, 11, 26)):
        envelope(s, x, y, z, width=30, height=22)
