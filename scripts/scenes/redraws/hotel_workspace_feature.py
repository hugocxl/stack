from geometry import DETAIL, oval

DESCRIPTION = "A hotel writing desk has a drawer and an angled task lamp mounted at its back corner."


def draw(s):
    for y in (2, 29):
        s.box(60, y, 0, 4.5, 5, 39, 1.1)
    s.box(3, 4, 0, 22, 31, 39, 1.3)
    s.line([(4, 35, 28), (24, 35, 28)], DETAIL)
    s.tube([(10, 35, 33), (10, 37, 33), (18, 37, 33), (18, 35, 33)], .9, DETAIL)
    s.box(0, 0, 38, 69, 38, 4.5, 2)
    s.disk(12, 7, 42.5, 5, 4, 2)
    s.tube([(12, 7, 44), (12, 7, 60), (19, 7, 74),
            (33, 7, 74), (38, 9, 70)], 1.6)
    s.solid(oval(40, 10, 10.5, 8.5)[:-1], 63, 8,
            oval(38, 9, 4, 3.2)[:-1], crease=False)
    s.ellipse(40, 10, 63, 9.7, 7.7, DETAIL, 3, 88)
