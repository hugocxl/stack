from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w2 import closed_outline, face_arrow, rule, upright_face
from scenes.redraws.task_assignment import profile_id

DESCRIPTION = "A transfer arrow bridges adjacent shift blocks on a two-row staff roster."


def draw(s):
    def point(x, z):
        return .73*x, -.27*x - .30*z, .87*z

    upright_face(s, point, rounded(0, 0, 132, 78, 5), 8)
    rule(s, point, 0, 60, 132, EDGE)
    rule(s, point, 0, 31, 132, DETAIL)
    for x in (38, 66, 94, 116):
        s.line([point(x, 6), point(x, 27)], DETAIL)
        s.line([point(x, 54), point(x, 59)], DETAIL)
    for x in (45, 73, 101):
        rule(s, point, x, 69, 10, EDGE)
    profile_id(s, point, 11, 33, 19, 23)
    profile_id(s, point, 11, 5, 19, 23)
    closed_outline(s, point, rounded(40, 40, 24, 11, 3), EDGE)
    closed_outline(s, point, rounded(96, 40, 22, 11, 3), EDGE)
    closed_outline(s, point, rounded(68, 13, 24, 11, 3), EDGE)
    face_arrow(s, point, [(64, 45.5), (96, 45.5)], BOLD, head=8)
