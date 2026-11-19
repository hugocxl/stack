from geometry import EDGE
from scenes.redraws.task_created import task_card

DESCRIPTION = "Right-angle connectors run from one task tile to two downstream task tiles."


def diagram_plane(x, z):
    return .59*x, -.41*x - .21*z, .96*z


def task_node(s, x, z, width, height, *, plane=diagram_plane):
    def point(u, v):
        return plane(x + width*u/92, z + height*v/71)
    task_card(s, point, compact=True)


def draw(s):
    point = diagram_plane
    s.line([point(55, 53), point(75, 53)], EDGE)
    s.line([point(75, 24), point(75, 82)], EDGE)
    s.line([point(75, 24), point(101, 24)], EDGE)
    s.line([point(75, 82), point(101, 82)], EDGE)
    task_node(s, 0, 30, 56, 46)
    task_node(s, 101, 0, 54, 46)
    task_node(s, 101, 58, 54, 46)
