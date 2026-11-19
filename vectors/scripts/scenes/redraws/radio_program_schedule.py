from geometry import EDGE, oval, rounded
from scenes.redraws._w4 import paper

DESCRIPTION = "A wide schedule card has a broadcast-wave header above three time-slot rows."


def draw(s):
    schedule = paper(s, 74, pitch=.60, run=.61, angle=-24, depth=7)
    schedule.slab(rounded(0, 0, 112, 74, 5), 7)
    schedule.oval(25, 20, 2.2, 2.2, EDGE)
    for radius in (7, 13):
        for start in (-49, 131):
            schedule.line(oval(25, 20, radius, radius, start, start + 98, count=14), EDGE)
    schedule.rows(46, 16, (48, 34), step=8, ink=EDGE)
    schedule.line([(7, 34), (105, 34)], EDGE)
    for v, width in ((42, 44), (53, 57), (64, 37)):
        schedule.rows(12, v, (6,), ink=EDGE)
        schedule.rows(23, v, (6,), ink=EDGE)
        schedule.rows(40, v, (width,))
        schedule.line([(9, v + 5), (101, v + 5)])
