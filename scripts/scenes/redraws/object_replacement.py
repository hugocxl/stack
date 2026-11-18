from geometry import DETAIL, EDGE, oval
from scenes.redraws._w2 import chart_line, face_arrow, landscape_frame, pine

DESCRIPTION = "An arrow points from a faint round tree silhouette to an outlined pine inside the same photograph."


def draw(s):
    point = landscape_frame(s)
    chart_line(s, point, [(8, 24), (102, 24)], DETAIL)
    chart_line(s, point, [(8, 28), (17, 35), (24, 30)], DETAIL)
    chart_line(s, point, [(87, 36), (93, 40), (102, 33)], DETAIL)
    crown = oval(30, 46, 12, 13, -75, 255, 24)
    old_tree = [(27, 24), (33, 24), *crown, (27, 24)]
    chart_line(s, point, old_tree, DETAIL, dash=(3, 2))
    pine(s, point, 72, 32)
    face_arrow(s, point, [(44, 41), (57, 41)], EDGE, head=6)
