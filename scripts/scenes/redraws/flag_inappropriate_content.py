from geometry import BOLD, EDGE
from scenes.redraws._w3 import Surface
from scenes.redraws.peer_feedback import conversation

DESCRIPTION = "A raised report flag attaches to the top corner of a speech bubble."


def draw(s):
    bubble = Surface(s, (0, 0, 0))
    conversation(bubble, 0, 6, 78, 50, depth=7)
    s.tube([(67, 3, 48), (67, 3, 88)], 1.5, EDGE)
    flag = Surface(s, (67, 3, 0))
    flag.plate([(0, 67), (12, 71), (25, 68), (37, 72),
                (30, 79), (37, 89), (25, 85), (12, 88), (0, 84)], 1.6, BOLD)
