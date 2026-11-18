from geometry import DETAIL, EDGE, GUIDE, rounded
from scenes.redraws._w4 import upright

DESCRIPTION = "A disinfectant trigger sprayer sits beside the seat of a reclining dental chair."


def draw(s):
    s.disk(51, 13, 0, 28, 18, 5)
    s.disk(47, 13, 5, 11, 9, 24)
    upright(s, [(11, 70), (18, 76), (52, 43), (87, 43), (111, 26),
                (106, 18), (84, 33), (48, 33)], 31, 33)
    s.line([(50, 31, 41), (86, 31, 41), (109, 31, 25)], DETAIL)
    upright(s, rounded(0, 73, 22, 13, 5), 26, 23)
    s.tube([(44, 34, 43), (48, 36, 55), (76, 36, 55)], 2.8, EDGE)

    # The nozzle points toward the cushion from beside the chair.
    for start, end in (((65, 72, 39), (69, 68, 39)),
                       ((72, 64, 39), (78, 57, 40)),
                       ((66, 70, 42), (70, 67, 44))):
        s.line([start, end], GUIDE)
    s.disk(53, 79, 0, 9.5, 9.5, 26)
    s.disk(53, 79, 26, 6, 6, 7, DETAIL)
    upright(s, [(44, 33), (44, 41), (62, 41), (63, 36),
                (57, 36), (55, 29), (51, 29), (52, 36)], 83, 8)
    s.ellipse(53, 79, 13, 9.5, 9.5, DETAIL, -32, 120)
