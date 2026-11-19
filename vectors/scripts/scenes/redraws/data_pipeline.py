from geometry import BOLD, EDGE
from scenes.redraws._kit import arrow
from scenes.systems_shapes import bezel

DESCRIPTION = "Two inline arrows connect three processing modules in a single continuous flow."


def draw(s):
    stages = [(-42, 15, 10), (0, 0, 10), (42, -15, 10)]
    for start, end in zip(stages, stages[1:]):
        tip = tuple(a + (b - a) * .57 for a, b in zip(start, end))
        s.line([start, end], EDGE)
        arrow(s, [start, tip], BOLD, head=8)
    for x, y, _ in reversed(stages):
        s.box(x - 10, y - 10, 0, 20, 20, 32, 2.5)
        bezel(s, x - 6, y + 10, 12, 12, 11, EDGE, 1.5)
