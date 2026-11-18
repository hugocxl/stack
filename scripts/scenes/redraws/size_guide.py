from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import upright_profile

DESCRIPTION = "A T-shirt has a double-ended measuring line and ruler ticks across its width."


def draw(s):
    shoulder = oval(0, 64, 12, 9, 180, 360, count=22)
    shirt = [(-28, 0), (-28, 37), (-41, 31), (-53, 47), (-33, 61), *shoulder,
             (33, 61), (53, 47), (41, 31), (28, 37), (28, 0)]
    upright_profile(s, shirt, 0, 4)
    s.line([(-49, 0, 44), (-39, 0, 33)], DETAIL)
    s.line([(49, 0, 44), (39, 0, 33)], DETAIL)
    s.line([(-25, 0, 4), (25, 0, 4)], DETAIL)

    for end in (-24, 24):
        arrow(s, [(0, 0, 25), (end, 0, 25)], BOLD, head=6)
    for x in (-12, 0, 12):
        s.line([(x, 0, 25), (x, 0, 20)], EDGE)
