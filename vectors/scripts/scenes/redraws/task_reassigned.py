from scenes.redraws._kit import badge
from scenes.redraws.task_created import task_card, task_plane

DESCRIPTION = "A right-arrow badge attaches to the owner row of a task card."


def draw(s):
    task_card(s, task_plane, owner=True)
    badge(s, "arrow", *task_plane(90, 15), 15)
