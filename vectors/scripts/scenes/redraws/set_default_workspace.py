from scenes.redraws._kit import badge
from scenes.redraws._w1 import status_monitor, workspace_layout

DESCRIPTION = "A desktop workspace shows a check badge beside the selected entry in its sidebar."


def draw(s):
    status_monitor(s)
    workspace_layout(s, -35, 0, 19, 70, 39, content="default")
    badge(s, "check", -42, 0, 38, 12)
