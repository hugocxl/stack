from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge

DESCRIPTION = "A folded-corner log sheet has four ruled entries and a clock badge above the timestamp column."


def draw(s):
    s.face([(0, 0, 0), (60, 0, 0), (60, 0, 57), (47, 0, 70), (0, 0, 70)])
    s.line([(47, 0, 70), (47, 0, 57), (60, 0, 57)], EDGE)
    # The short entries form a dedicated timestamp column beside the log entries.
    s.line([(23, 0, 8), (23, 0, 48)], EDGE)
    for z, width in ((43, 24), (33, 19), (23, 25), (13, 21)):
        s.line([(8, 0, z), (17, 0, z)], EDGE)
        s.line([(29, 0, z), (29 + width, 0, z)], DETAIL)
    for z in (48, 38, 28, 18, 8):
        s.line([(7, 0, z), (54, 0, z)], DETAIL)

    badge(s, "clock", 12, 3, 68, 13)
