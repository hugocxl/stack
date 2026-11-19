from geometry import DETAIL, EDGE, oval
from scenes.redraws._w5 import panel, rect

DESCRIPTION = "An evidence drive has a tamper seal across its casing and a custody tag threaded through the seal."


def draw(s):
    s.box(0, 0, 0, 67, 52, 10, 5)
    port = lambda y, z: (66.95, y, z)
    rect(s, port, 9, 2.4, 13, 4.6, 1.2, DETAIL)
    top = lambda x, y: (x, y, 10.2)
    rect(s, top, 5, 5, 57, 41, 4, DETAIL)
    s.ellipse(22, 23, 10.3, 11, 11, EDGE)
    s.ellipse(22, 23, 10.3, 2.7, 2.7, DETAIL)
    s.line([(22, 26, 10.3), (29, 32, 10.3), (34, 30, 10.3)], DETAIL)
    s.face([(45, 22, 10.5), (57, 22, 10.5), (57, 52.2, 10.5),
            (45, 52.2, 10.5)], EDGE)
    s.face([(45, 52.2, 10.5), (57, 52.2, 10.5), (57, 52.2, 3),
            (45, 52.2, 3)], EDGE)
    s.line([(51, 52.2, 3.8), (51, 52.2, 9.5)], DETAIL, dashed=True)

    tag = lambda x, z: (x + 53, 49 + (19 - z) * .72, z)
    panel(s, [(0, 16), (6, 23), (25, 23), (25, 3), (6, 3), (0, 9)],
          tag, 1.7)
    s.line([tag(x, z) for x, z in oval(5, 13, 2.1, 2.1, count=20)], EDGE)
    for z in (8, 13, 18):
        s.line([tag(11, z), tag(20, z)], DETAIL)
    s.tube([(51, 47, 10.7), (51, 47, 14), (54, 48, 17), tag(5, 13)], 1.1, EDGE)
