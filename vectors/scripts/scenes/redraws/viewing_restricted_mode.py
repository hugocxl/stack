from geometry import EDGE, oval, rounded
from scenes.redraws._kit import badge
from scenes.redraws.page_moved import Surface

DESCRIPTION = "A content viewer shows a landscape preview with a lock badge over its playback controls."


def draw(s):
    window = Surface(s, (7, 0, 0), side=True)
    window.plate(rounded(0, 0, 106, 70, 6), 7)
    window.frame(8, 20, 90, 42, 3, EDGE)
    window.line([(9, 25), (35, 48), (51, 34), (66, 42), (96, 24)], EDGE)
    window.loop(oval(78, 51, 4.2, 4.2, count=20)[:-1])
    window.loop([(11, 7), (11, 15), (18, 11)], EDGE)
    window.line([(25, 11), (92, 11)], EDGE)
    window.loop(oval(46, 11, 2.8, 2.8, count=20)[:-1])
    badge(s, "lock", *window.point(97, 11), 14)
