from geometry import BOLD, DETAIL, oval
from scenes.redraws._w4 import upright

DESCRIPTION = "A notched reservation ticket carries a wheelchair accessibility pictogram beside its perforated stub."


def draw(s):
    notch_left = oval(0, 30, 8, 8, 90, -90, 16)
    notch_right = oval(90, 30, 8, 8, -90, -270, 16)
    ticket = [(0, 0), (90, 0), *notch_right, (90, 60), (0, 60), *notch_left]
    upright(s, ticket, 0, 3)
    s.line([(67, 0, 5), (67, 0, 55)], DETAIL, dashed=True)
    for x in (72, 75, 79):
        s.line([(x, 0, 34), (x, 0, 50)], DETAIL)

    s.line([(x, 0, z) for x, z in oval(30, 21, 11, 11, 92, 344, 32)], BOLD)
    s.line([(x, 0, z) for x, z in oval(33, 48, 3.5, 3.5, count=24)], BOLD)
    s.line([(32, 0, 40), (35, 0, 27), (46, 0, 27), (52, 0, 15), (58, 0, 17)], BOLD)
    s.line([(34, 0, 34), (44, 0, 34)], BOLD)
