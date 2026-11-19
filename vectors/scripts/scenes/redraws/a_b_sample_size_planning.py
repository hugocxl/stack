from geometry import BOLD, EDGE
from scenes.redraws._w2 import variant

DESCRIPTION = "Two equally tall stacks of sample tiles carry the letters A and B on their top tiles."


def draw(s):
    for name, x, y in (("A", 0, 0), ("B", 45, -23)):
        for level in range(5):
            s.box(x, y, level * 5, 30, 30, 5, 3, EDGE)
        variant(s, name, x + 15, y + 24, 25, 18, BOLD, flat=True)
