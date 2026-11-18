from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w4 import Surface, paper

DESCRIPTION = "An audio mastering console has four faders and a raised stereo output meter."


def draw(s):
    desk = paper(s, 81, pitch=.25, run=.86, angle=2, depth=12)
    desk.slab(rounded(0, 0, 108, 81, 6), 12)

    def meter_placement(u, v):
        x, y, z = desk.at(u, 28)
        return x, y - v*.22, z + v

    meter = Surface(s, meter_placement)
    meter.slab(rounded(6, 0, 96, 32, 4), 4)
    meter.frame(13, 7, 82, 18, 2, DETAIL)
    for v, end in ((11, 76), (19, 88)):
        for u in range(17, 92, 8):
            meter.rows(u, v, (5,), ink=BOLD if u < end else DETAIL)
            if u < end:
                meter.rows(u, v + 2.3, (5,), ink=EDGE)
    for u, v in ((18, 58), (36, 48), (54, 65), (72, 53)):
        desk.line([(u, 38), (u, 73)], DETAIL)
        desk.slab(rounded(u - 6, v - 3, 12, 6, 2), 2, EDGE)
    desk.oval(92, 55, 8, 8, EDGE)
    desk.line([(92, 55), (96, 51)], EDGE)
