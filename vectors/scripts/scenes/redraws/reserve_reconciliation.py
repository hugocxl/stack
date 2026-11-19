from geometry import DETAIL, oval
from scenes.redraws._kit import badge
from scenes.redraws._w5 import coin_stack

DESCRIPTION = "A balance scale holds two equal coin stacks at the same height and carries a check badge at its pivot."


def draw(s):
    s.disk(0, 0, 0, 16, 10, 5)
    s.box(-2.8, -3, 4, 5.6, 6, 58, 1.9)
    s.tube([(-29, 0, 57), (29, 0, 57)], 2.7)
    for x in (-29, 29):
        s.tube([(x, 0, 57), (x - 13, 4, 24)], 1.1, DETAIL)
        s.tube([(x, 0, 57), (x + 13, 4, 24)], 1.1, DETAIL)
        s.solid(oval(x, 4, 10, 7)[:-1], 18, 6,
                top=oval(x, 4, 15, 10)[:-1])
        coin_stack(s, x, 4, 24, 7.5, 3)
    badge(s, "check", 3, 1, 60, 10.5)
