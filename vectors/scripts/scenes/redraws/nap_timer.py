from geometry import DETAIL
from scenes.redraws._sf import alarm_clock, ground, plate, screen, squircle

DESCRIPTION = "A twin-bell alarm clock stands beside a soft rectangular pillow."


def draw(s):
    top = ground(-70, -10, 12)
    plate(s, top, squircle(70, 46, 16), 12, (0, 0, -1))
    s.line([top(35, 8), top(35, 38)], DETAIL)
    alarm_clock(s, screen(36, 0, 32), 26)
