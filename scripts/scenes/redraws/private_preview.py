from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import Surface, front_surface, landscape, upright

DESCRIPTION = "A thick browser preview frames a landscape thumbnail and carries an attached lock badge."


def browser_window(s, angle):
    upright(s, rounded(0, 0, 98, 66, 5), 10, 9, angle=angle)
    view = front_surface(s, angle=angle, y=10)
    view.line([(0, 53), (98, 53)], EDGE)
    for u in (10, 16, 22):
        view.oval(u, 60, 1.3, 1.3, EDGE)
    return view


def draw(s):
    view = browser_window(s, angle=3)
    image = Surface(s, lambda u, v: view.at(u, 46 - v))
    landscape(image, 12, 0, 65, 37)
    badge(s, "lock", *view.at(95, 49), 15)
