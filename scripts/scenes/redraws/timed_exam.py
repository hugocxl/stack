from geometry import BOLD, EDGE, oval
from scenes.redraws._w3 import printed_check, sheet

DESCRIPTION = "A running sand hourglass stands in front of a marked exam sheet."


def draw(s):
    exam = sheet(s, 55, 71, origin=(-11, 7, 0), rise=(-.18, .98))
    exam.rules(10, 59, [29], ink=EDGE)
    for v in (43, 31, 19):
        exam.rect(10, v - 4, 8, 8, 1, EDGE)
        printed_check(exam, 14, v, 4)
        exam.rules(24, v, [18])

    x, y = 65, 20
    s.disk(x, y, 0, 22, 22, 6)
    for dx, dy in ((-16, -12), (14, -13)):
        s.tube([(x + dx, y + dy, 5), (x + dx, y + dy, 79)], 1.7)
    for direction, z in ((1, 8), (-1, 77)):
        s.solid(oval(x, y, 15 if direction == 1 else 3,
                     15 if direction == 1 else 3, count=40)[:-1],
                min(z, z + direction * 32), 32,
                top=oval(x, y, 3 if direction == 1 else 15,
                         3 if direction == 1 else 15, count=40)[:-1],
                ink=EDGE, crease=False)
    s.ellipse(x, y, 67, 10.5, 10.5, BOLD)
    s.line([(x, y, 43), (x, y, 22)], EDGE, dashed=True)
    s.ellipse(x, y, 15, 10, 10, EDGE)
    s.tube([(x - 12, y + 16, 5), (x - 12, y + 16, 79)], 1.7)
    s.disk(x, y, 77, 22, 22, 6)
