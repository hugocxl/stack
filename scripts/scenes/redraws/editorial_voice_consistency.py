from geometry import EDGE
from scenes.redraws._w2 import open_volume, rule

DESCRIPTION = "An open style guide displays the same rhythm of short and long text strokes on facing pages."


def draw(s):
    left, right = open_volume(s)
    for point, start, direction in ((left, 46, -1), (right, 10, 1)):
        rule(s, point, start - (23 if direction < 0 else 0), 52, 23, EDGE)
        for row, pattern in ((36, (13, 6, 9)), (25, (8, 16)), (14, (14,))):
            x = start
            for length in pattern:
                rule(s, point, min(x, x + direction*length), row, length)
                x += direction*(length + 4)
