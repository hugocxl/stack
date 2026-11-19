from geometry import DETAIL, oval
from scenes.redraws._kit import badge
from scenes.redraws._w5 import pipe_section

DESCRIPTION = "A flanged irrigation valve has a spoked handwheel and a circular swap-arrow badge."


def draw(s):
    pipe_section(s, 0, 69, 15, 13, 6, bore=3.8)
    pipe_section(s, 10, 17, 15, 13, 10.5)
    s.box(18, 4, 2.5, 33, 22, 23, 7)
    pipe_section(s, 51, 58, 15, 13, 10.5)
    for y, z in ((9, 13), (15, 20), (21, 13), (15, 6)):
        s.line([(58, a, b) for a, b in oval(y, z, 1, 1, count=16)], DETAIL)
    s.disk(34, 15, 25, 7, 7, 3.5)
    s.tube([(34, 15, 28), (34, 15, 42)], 2.1)
    wheel = lambda points: [(x, y, 43) for x, y in points]
    s.face(wheel(oval(34, 15, 16, 14)[:-1]),
           openings=[wheel(oval(34, 15, 13, 11)[:-1])])
    for a, b in (((21, 15), (47, 15)), ((34, 4), (34, 26))):
        s.tube(wheel([a, b]), 1)
    s.disk(34, 15, 43, 3.2, 3.2, 2.2)
    badge(s, "refresh", 61, 9, 43, 11.5)
