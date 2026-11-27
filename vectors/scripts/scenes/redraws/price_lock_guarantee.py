from geometry import BOLD
from scenes.redraws._kit import badge
from scenes.redraws._sf import Face2D, currency, padlock

DESCRIPTION = "A padlock printed with a currency sign carries a check badge for a locked price."


def draw(s):
    body = padlock(s, -30, 0, 0, w=60, h=48, depth=16, keyhole=False)
    currency(s, lambda u, v: body(30 + u, 24 + v), 12, BOLD)
    badge(s, "check", 30, 0, 4, 14)
