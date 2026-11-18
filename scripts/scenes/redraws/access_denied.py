from geometry import EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws.page_moved import Surface

DESCRIPTION = "A closed door in its frame carries an X badge above the doorknob."


def draw(s):
    s.box(0, 0, 0, 13, 64, 90, 3)
    door = Surface(s, (13, 64, 2), side=True)
    door.frame(5, 1, 54, 82, 2, EDGE)
    door.frame(11, 42, 42, 34, 3)
    door.frame(11, 9, 42, 26, 3)
    knob = Surface(s, (15, 64, 2), side=True)
    knob.plate(oval(50, 39, 3.5, 3.5, count=20)[:-1], 2)
    badge(s, "x", *door.point(54, 66), 13)
