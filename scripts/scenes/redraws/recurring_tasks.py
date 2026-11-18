from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w2 import closed_outline, rule
from scenes.redraws.task_created import task_card, task_plane

DESCRIPTION = "A circular recurrence badge sits at the upper corner of a task card with a three-item checklist."


def draw(s):
    task_card(s, task_plane, compact=True)
    for z, length in ((17, 42), (6, 32)):
        closed_outline(s, task_plane, rounded(17, z, 8, 8, 1.3), EDGE)
        rule(s, task_plane, 33, z + 4, length, DETAIL)
    badge(s, "refresh", *task_plane(90, 63), 17)
