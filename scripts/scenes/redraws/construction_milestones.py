from geometry import EDGE
from scenes.redraws._kit import arrow
from scenes.redraws.building_code_review import timber_frame
from scenes.redraws.model_home_appointment import gabled_home

DESCRIPTION = "A single timeline connects a poured foundation, an exposed house frame, and a finished home."


def draw(s):
    stages = ((-14, 66), (0, 0), (14, -66))
    # One line passes through the three milestones below their footprints.
    arrow(s, [(5.5, 104.5, 0), (46.1, -86.9, 0)], EDGE, head=8)

    x, y = stages[0]
    s.box(x - 23, y - 16, 0, 46, 32, 5, .7)
    rim = [(-21, -14), (21, -14), (21, 14), (-21, 14)]
    inner = [(-15, -8), (15, -8), (15, 8), (-15, 8)]
    s.face([(x + u, y + v, 11) for u, v in rim],
           openings=([(x + u, y + v, 11) for u, v in inner],))
    s.face([(x - 21, y + 14, 5), (x + 21, y + 14, 5),
            (x + 21, y + 14, 11), (x - 21, y + 14, 11)])
    s.face([(x + 21, y - 14, 5), (x + 21, y + 14, 5),
            (x + 21, y + 14, 11), (x + 21, y - 14, 11)])

    x, y = stages[1]
    timber_frame(s, x, y, 0, .86, simplified=True)
    x, y = stages[2]
    gabled_home(s, x, y, 0, .88)
    for x, y in stages:
        s.disk(x + 23, y + 22, 0, 3.7, 3.7, 1.2)
