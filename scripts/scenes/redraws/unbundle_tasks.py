from math import cos, radians, sin

from geometry import EDGE, rounded
from scenes.redraws._w2 import face_arrow, rule, upright_face
from scenes.redraws.task_dependencies import task_node

DESCRIPTION = "Two arrows lead from a clipped stack to matching task cards that fan apart."


def draw(s):
    def point(x, z):
        return .66*x, -.34*x - .23*z, .92*z

    upright_face(s, point, rounded(0, 23, 57, 62, 4), 8)
    rule(s, point, 6, 28, 44)
    rule(s, point, 6, 32, 44)
    task_node(s, 0, 36, 57, 55, plane=point)
    upright_face(s, point, rounded(18, 82, 21, 14, 3), 4)
    rule(s, point, 23, 88, 11)

    for start_z, next_z, end_x, end_z in ((58, 75, 113, 79), (58, 33, 103, 19)):
        face_arrow(s, point, [(57, start_z), (84, next_z), (end_x, end_z)], EDGE, head=7)

    for center_x, center_z, tilt in ((137, 78, 13), (135, 22, -14)):
        angle = radians(tilt)

        def fanned(x, z):
            return point(center_x + x*cos(angle) - z*sin(angle),
                         center_z + x*sin(angle) + z*cos(angle))

        task_node(s, -23, -22, 51, 44, plane=fanned)
