from scenes.redraws._kit import badge
from scenes.redraws._w1 import status_monitor, workspace_layout

DESCRIPTION = "A desktop workspace shows two member avatars in its title bar beside a check badge."


def draw(s):
    status_monitor(s)
    workspace_layout(s, -35, 0, 19, 70, 39, content="team")
    badge(s, "check", 44, -4, 59, 12)
