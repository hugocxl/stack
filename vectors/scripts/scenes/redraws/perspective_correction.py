from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import chart_line, upright_face

DESCRIPTION = "An architectural print shows a building with upright sides in front of its skewed dashed crop guide."


def draw(s):
    def point(x, z):
        return .91*x, -.09*x - .12*z, z

    corners = [(-25, 8), (62, -13), (88, 88), (-4, 106), (-25, 8)]
    chart_line(s, point, corners, DETAIL, dash=(5, 3))
    upright_face(s, point, [(0, 0), (86, 0), (86, 97), (0, 97)], 4)
    chart_line(s, point, [(8, 11), (8, 86), (78, 86), (78, 11), (8, 11)], EDGE)
    chart_line(s, point, [(16, 22), (26, 22), (26, 71), (58, 71),
                          (58, 22), (72, 22)], BOLD)
    chart_line(s, point, [(58, 71), (68, 65), (68, 22)], EDGE)
    for z in (58, 47, 36):
        chart_line(s, point, [(33, z), (51, z)], EDGE)
    chart_line(s, point, [(38, 22), (38, 31), (47, 31), (47, 22)], EDGE)
