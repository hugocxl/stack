from geometry import BOLD, EDGE
from scenes.redraws._w2 import card, outline, variant


DESCRIPTION = "A split-test card shows matching panels marked A and B."


def draw(s):
    card(s, 110, 56)
    s.line([(55, 0, 0), (55, 0, 56)], EDGE)
    for name, center in (("A", 27.5), ("B", 82.5)):
        outline(s, center - 17, 0, 11, 34, 34)
        variant(s, name, center, 0, 17, 23, BOLD)
