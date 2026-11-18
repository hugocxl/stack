from geometry import BOLD, EDGE
from scenes.editorial_objects import At, pencil
from scenes.redraws._w2 import chart_line, clipboard, rule

DESCRIPTION = "A pencil touches the last colon-separated property row on a clipped JSON response draft."


def draw(s):
    top = clipboard(s)

    def point(x, row):
        return x, row, top

    brace = [(25, 30), (21, 30), (19, 32), (19, 35), (16, 38),
             (19, 41), (19, 44), (21, 46), (25, 46)]
    chart_line(s, point, brace, BOLD)
    chart_line(s, point, [(41 - x, row + 33) for x, row in brace], BOLD)
    for row, width in ((43, 12), (54, 17), (65, 14)):
        rule(s, point, 29, row, width, EDGE)
        for y in (row - 1.8, row + 1.8):
            rule(s, point, 50, y, 1, EDGE)
        rule(s, point, 56, row, 15 if row < 65 else 12, EDGE)
    scale = .86
    pencil(At(s, 68, 65 - 21*scale, top - 3*scale, scale))
