from geometry import EDGE
from scenes.redraws._kit import badge

DESCRIPTION = "Three stacks of modules step up from one to three high, with an up-arrow badge."


def draw(s):
    size, gap = 26, 4
    for i, count in enumerate((1, 2, 3)):
        x = i*(size + gap) - 40
        y = -i*(size + gap)*.0
        for k in range(count):
            s.box(x, y, k*(size + 2), size, size, size, 3)
    badge(s, "up", 50, 6, 84, 13)
