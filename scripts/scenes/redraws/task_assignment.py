from geometry import EDGE, rounded
from scenes.redraws._w2 import closed_outline, profile_mark, upright_face
from scenes.redraws.task_created import task_card, task_plane

DESCRIPTION = "A small profile ID clips onto the owner row of a task card."


def profile_id(s, point, x, z, width, height):
    """A physical ID tab with a printed profile seal."""
    upright_face(s, point, rounded(x, z, width, height, 3), 3)
    closed_outline(s, point, rounded(x + width*.33, z + height*.8, width*.34, 3, 1.5), EDGE)
    profile_mark(s, point, x + width/2, z + height*.42, width*.35)


def draw(s):
    task_card(s, task_plane, owner=True)
    profile_id(s, task_plane, 72, -2, 29, 32)
