from geometry import EDGE, oval
from scenes.redraws._w4 import upright

DESCRIPTION = "A reporter microphone stands at a covered location on a folded street map."


def draw(s):
    # The folded panels join edge to edge, with two valleys touching the ground.
    folds = ((0, 16), (32, 0), (64, 16), (96, 0))
    for (x, z), (end, top) in zip(folds, folds[1:]):
        s.face([(x, 0, z), (end, 0, top), (end, 73, top), (x, 73, z)])
        for y in (17, 34, 52):
            s.line([(x + 3, y, z + (top-z)*3/32),
                    (end - 3, y + 4, top + (z-top)*3/32)])
        for step in (12, 22):
            height = z + (top-z)*step/32
            s.line([(x + step, 7, height), (x + step, 61, height)])
    s.line([(x, y, abs(x - 32)*.5 + .3) for x, y in oval(32, 42, 9, 7)], EDGE)
    upright(s, [(32, 2), (25, 14), (24, 44), (38, 44), (37, 14)], 43, 6)
    s.box(21, 36, 33, 21, 14, 12, 2)
    upright(s, [(21, 46), (19, 52), (20, 61), (25, 67), (32, 70), (39, 67),
                (44, 61), (45, 53), (42, 46)], 46, 13)
    for z, width in ((51, 14), (57, 19), (63, 13)):
        s.line([(32 - width/2, 46, z), (32 + width/2, 46, z)])
