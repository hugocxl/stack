from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w2 import chart_line, standing_notebook

DESCRIPTION = "A notebook records a matrix of outlined data cells with a dashed staircase of missing values."


def draw(s):
    p = standing_notebook(s, 114, 95)
    missing = {(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3)}
    for row in range(4):
        for col in range(5):
            x, z = 9 + 20*col, 64 - 17*row
            outline = rounded(x, z, 15, 12, 1)
            if (row, col) in missing:
                chart_line(s, p, outline + outline[:1], EDGE, dash=(3.2, 2.1))
            else:
                s.face([p(a, b) for a, b in outline], EDGE)
                s.line([p(x + 4, z + 6), p(x + 11, z + 6)], DETAIL)
