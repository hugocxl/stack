from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w3 import Surface, selection_handle

DESCRIPTION = "A raised tile aligns to a ruled grid, and a corner handle marks the grid intersection it snaps to."


def draw(s):
    grid = Surface(s, (0, 68, 0), rise=(-.95, .31), back=(0, -.31, -.95))
    grid.rect(0, 0, 84, 84, 0, EDGE)
    for inset in (14, 28, 42, 56, 70):
        grid.stroke([(inset, 0), (inset, 84)], DETAIL)
        grid.stroke([(0, inset), (84, inset)], DETAIL)
    grid.stroke([(56, 28), (84, 28)], BOLD)
    grid.stroke([(70, 14), (70, 42)], BOLD)

    tile = Surface(s, grid.point(0, 0, -7), rise=grid.rise, back=grid.back)
    tile.plate([(28, 28), (70, 28), (70, 70), (28, 70)], 7, EDGE)
    selection_handle(tile, 70, 28, 6)
