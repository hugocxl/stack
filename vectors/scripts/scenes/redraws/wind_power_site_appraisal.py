from geometry import DETAIL
from scenes.redraws._sf import turbine

DESCRIPTION = "A wind turbine stands inside a dashed survey boundary on open ground."


def draw(s):
    s.line([(-34, -28, 0), (34, -28, 0), (40, 22, 0), (-22, 34, 0), (-34, -28, 0)], DETAIL, dashed=True)
    for x, y in ((-34, -28), (34, -28), (40, 22), (-22, 34)):
        s.tube([(x, y, 0), (x, y, 8)], 1, DETAIL)
    turbine(s, 2, 2, 0, 100, 44)
