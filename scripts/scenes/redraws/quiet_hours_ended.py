from geometry import EDGE, oval
from scenes.redraws._kit import _screen
from scenes.redraws.notification_read import notification_bell

DESCRIPTION = "A flared notification bell rings between two curved motion lines."


def draw(s):
    notification_bell(s)
    for start, end in ((-26, 38), (142, 206)):
        arc = oval(0, 33, 40, 21, start, end, 22)
        s.line([_screen(0, 0, 0, u, v) for u, v in arc], EDGE)
