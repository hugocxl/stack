from geometry import DETAIL, EDGE, GUIDE
from scenes.redraws.model_home_appointment import gabled_home

DESCRIPTION = "Two homes occupy opposite lots with their driveways connected to one continuous subdivision street."


def draw(s):
    for y in (-9, 9):
        s.line([(-51, y, 0), (53, y, 0)], EDGE)
    s.line([(-49, 0, 0), (51, 0, 0)], DETAIL, dashed=True)

    for x, y, end in ((-21.7, -20, -9), (21, 20, 9)):
        for edge in (-4, 4):
            s.line([(x + edge, y, 0), (x + edge, end, 0)], DETAIL)

    for points in (
        [(-44, -9), (-44, -49), (3, -49), (3, -9)],
        [(-3, 9), (-3, 49), (46, 49), (46, 9)],
    ):
        s.line([(x, y, 0) for x, y in points], GUIDE)

    gabled_home(s, -15, -32, 0, .67)
    gabled_home(s, 20, 32, 0, .67, entry_visible=False)
