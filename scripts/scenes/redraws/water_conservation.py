from geometry import EDGE
from scenes.redraws._w1 import droplet

DESCRIPTION = "A closed faucet holds one droplet beneath its downward spout."


def draw(s):
    s.disk(-23, 0, 0, 16, 15, 5)
    s.tube([(-23, 0, 7), (-23, 0, 29), (-21, 0, 38),
            (-15, 0, 46), (-6, 0, 50), (9, 0, 50), (18, 0, 46),
            (23, 0, 39), (23, 0, 34)], 6)
    s.disk(23, 0, 29, 7.5, 7.5, 5)
    s.tube([(-19, 0, 47), (-19, 0, 60)], 3)
    s.box(-33, -4, 59, 30, 8, 5, 3)
    droplet(s, lambda u, v: (23 + 10*u, -10*u, 15 + 17*v), EDGE)
