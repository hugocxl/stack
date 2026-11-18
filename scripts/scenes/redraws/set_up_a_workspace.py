from scenes.redraws._kit import badge
from scenes.redraws._w1 import status_monitor, workspace_layout

DESCRIPTION = "A desktop monitor shows an empty workspace with a plus badge on its upper corner."


def draw(s):
    status_monitor(s)
    workspace_layout(s, -35, 0, 19, 70, 39, content="empty")
    badge(s, "plus", 44, -4, 59, 12)
