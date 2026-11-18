from geometry import EDGE
from scenes.redraws._w2 import face_arrow
from scenes.redraws.task_dependencies import task_node

DESCRIPTION = "A forked arrow leads from one parent task tile down to two matching child tiles."


def draw(s):
    def point(x, z):
        return .54*x, -.46*x - .16*z, .94*z

    s.line([point(69, 85), point(69, 63)], EDGE)
    for x in (27, 111):
        face_arrow(s, point, [(69, 63), (x, 48), (x, 41)], EDGE, head=6)
    task_node(s, 41, 85, 56, 41, plane=point)
    task_node(s, 0, 0, 54, 36, plane=point)
    task_node(s, 84, 0, 54, 36, plane=point)
