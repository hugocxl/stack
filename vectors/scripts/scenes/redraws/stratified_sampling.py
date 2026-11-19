from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w2 import chart_marker, level_face

DESCRIPTION = "Three layers in a sampling jar each yield a matching token."


def draw(s):
    s.disk(0, 0, 0, 33, 33, 67)
    s.ellipse(0, 0, 67, 33, 33, EDGE)
    s.disk(0, 0, 67, 31, 31, 8)
    s.ellipse(0, 0, 75, 24, 24, DETAIL)
    for z in (22, 42):
        s.ellipse(0, 0, z, 33, 33, DETAIL, start=-45, end=135)
    for z, shape in ((11, "circle"), (31, "square"), (50, "triangle")):
        for x in (-16, 0, 16, 57):
            point = level_face
            height = z + (4 if x == 57 else 0)
            if shape == "circle":
                chart_marker(s, point, x, height, 4.5, BOLD if x == 57 else EDGE)
            else:
                vertices = ((-4, -4), (4, -4), (4, 4), (-4, 4)) if shape == "square" else ((-5, -4), (5, -4), (0, 5))
                s.face([point(x + u, height + v) for u, v in vertices], BOLD if x == 57 else EDGE)
        arrow(s, [level_face(43, z + 4), level_face(51, z + 4)], EDGE, head=3.5)
