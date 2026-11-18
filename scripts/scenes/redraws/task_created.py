from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w2 import closed_outline, profile_mark, rule, upright_face

DESCRIPTION = "A plus badge overlaps the status corner of a task card with a checkbox."


def task_card(s, point, *, owner=False, compact=False):
    """Draw the task tile in its full-size or diagram form."""
    upright_face(s, point, rounded(0, 0, 92, 71, 5), 3 if compact else 6)
    box_z = 30 if compact else 43
    closed_outline(s, point, rounded(12, box_z, 18, 18, 2), EDGE)
    rule(s, point, 41, box_z + 13, 33, EDGE)
    rule(s, point, 41, box_z + 3, 23, DETAIL)
    if owner:
        rule(s, point, 12, 28, 68, DETAIL)
        profile_mark(s, point, 20, 15, 10, EDGE)
        rule(s, point, 34, 15, 23, DETAIL)
    elif not compact:
        rule(s, point, 12, 28, 60, DETAIL)
        rule(s, point, 12, 16, 43, DETAIL)


def task_plane(x, z):
    return .72*x, -.28*x - .35*z, .87*z


def task_status(s, kind):
    def point(x, z):
        return .79*x, -.21*x - .58*z, .78*z

    task_card(s, point)
    badge(s, kind, *point(91, 67), 15)


def draw(s):
    task_status(s, "plus")
