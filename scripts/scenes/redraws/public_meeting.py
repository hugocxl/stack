from scenes.redraws._w1 import lectern
from scenes.redraws._w3 import classroom_chair

DESCRIPTION = "A town-hall lectern faces two compact rows of chairs."


def draw(s):
    lectern(s, 1, -30, .94)
    for y in (2, 27):
        for x in (-28, 6):
            classroom_chair(s, x, y, 1.1)
