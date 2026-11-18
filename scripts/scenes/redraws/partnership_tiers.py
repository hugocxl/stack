from geometry import EDGE, rounded

DESCRIPTION = "Three square podium blocks stack from a broad bottom tier to a small upper tier."


def draw(s):
    for width, z in ((88, 0), (64, 23), (40, 46)):
        corner = (88 - width) / 2
        s.solid(rounded(corner, corner, width, width, 3), z, 23, ink=EDGE)
