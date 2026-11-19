from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w2 import closed_outline, rule
from scenes.redraws.task_created import task_card, task_plane

DESCRIPTION = "A clock badge overlaps the calendar field below a task card's checkbox and title."


def draw(s):
    task_card(s, task_plane, compact=True)
    closed_outline(s, task_plane, rounded(12, 9, 56, 15, 3), DETAIL)
    closed_outline(s, task_plane, rounded(17, 12, 10, 9, 1), EDGE)
    rule(s, task_plane, 17, 18, 10, EDGE)
    rule(s, task_plane, 34, 16, 18)
    badge(s, "clock", *task_plane(82, 21), 16)
