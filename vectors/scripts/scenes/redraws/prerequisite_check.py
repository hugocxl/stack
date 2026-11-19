from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import clipboard, cover_cap, printed_check

DESCRIPTION = "A slanted course clipboard shows a mortarboard, three completed prerequisites and a prominent check badge."


def draw(s):
    page = clipboard(s, w=76, h=93)
    cover_cap(page, 32, 65, 28)
    for v, width in ((47, 37), (32, 30), (17, 34)):
        printed_check(page, 20, v, 7.5)
        page.rules(31, v, [width], ink=EDGE)
    badge(s, "check", 76, 28, 56, 15)
