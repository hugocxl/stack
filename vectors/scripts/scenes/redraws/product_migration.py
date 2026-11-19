from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws.private_preview import browser_window

DESCRIPTION = "A browser window sends data out through an outward arrow on its right edge."


def draw(s):
    view = browser_window(s, angle=-17)
    for v in (14, 26, 38):
        view.frame(12, v, 36, 8, 2, DETAIL)
        view.rows(16, v + 4, (3, 3), step=2, ink=EDGE)
        view.rows(24, v + 4, (18,))
    view.line([(53, 18), (62, 18), (71, 28), (90, 28)], EDGE)
    view.line([(53, 30), (65, 30), (71, 28)], EDGE)
    view.line([(53, 42), (62, 42), (71, 28)], EDGE)
    badge(s, "arrow", *view.at(101, 28), 18)
