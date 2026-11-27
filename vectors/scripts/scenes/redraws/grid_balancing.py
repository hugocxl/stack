from geometry import EDGE
from scenes.redraws._sf import bolt, turned

DESCRIPTION = "A balance scale holds its two pans level on a post printed with a lightning bolt."


def draw(s):
    turned(s, [(18, 0), (18, 5), (14, 7)], steps=2)
    s.box(-5, -5, 7, 10, 10, 62, 1.5)
    bolt(s, lambda u, v: (u, 5.05, 38 + v), 9)
    s.tube([(-46, 0, 70), (46, 0, 70)], 2.4, EDGE)
    for x in (-46, 46):
        turned(s, [(.4, 36), (13, 38), (16, 42)], x, 0, 0, steps=3)
        for dx, dy in ((15, 0), (0, 15), (-11, 11)):
            s.line([(x, 0, 70), (x + dx, dy, 42)], EDGE)
