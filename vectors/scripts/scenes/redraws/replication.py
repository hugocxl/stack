from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow
from scenes.systems_shapes import rectangle

DESCRIPTION = "A data tile branches into two identical copies."


def position(across, along, height):
    return along + across, along - across, height


def data_tile(s, x, y):
    s.box(x - 15, y - 13, 0, 30, 26, 8, 2)
    rectangle(s, x - 11, y - 9, 8, 22, 18, EDGE, 1)
    s.line([(x - 11, y - 3, 8), (x + 11, y - 3, 8)], EDGE)
    s.line([(x - 3, y - 3, 8), (x - 3, y + 9, 8)], DETAIL)
    s.line([(x - 11, y + 3, 8), (x + 11, y + 3, 8)], DETAIL)


def draw(s):
    split = position(0, -16, 4)
    s.line([position(0, -37, 4), split], EDGE)
    for side in (-1, 1):
        arrow(s, [split, position(19 * side, -16, 4), position(27 * side, 1, 4)],
              BOLD, head=7)
    for across, along in ((0, -46), (28, 18), (-28, 18)):
        x, y, _ = position(across, along, 0)
        data_tile(s, x, y)
