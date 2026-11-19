from geometry import BOLD
from scenes.redraws._w2 import face_arrow
from scenes.redraws.task_created import task_card, task_plane

DESCRIPTION = "A hooked left arrow points back toward the profile on a task card’s owner row."


def draw(s):
    task_card(s, task_plane, owner=True)
    face_arrow(s, task_plane, [(84, 7), (84, 12), (82, 16), (79, 19),
                               (74, 20), (67, 20), (59, 20)], BOLD, head=6)
