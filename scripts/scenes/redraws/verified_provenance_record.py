from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w5 import panel, parcel_mark, rect

DESCRIPTION = "A wide certificate has a framed source parcel, two record lines, and a check badge beside the source record."


def draw(s):
    face = lambda x, z: (x, -.31 * z, z)
    panel(s, rounded(0, 0, 74, 53, 3), face, 5)
    rect(s, face, 5, 5, 64, 43, 2, DETAIL)
    rect(s, face, 10, 12, 30, 26, 1.5, DETAIL)
    parcel_mark(s, face, 25, 25, .79)
    for z, length, ink in ((35, 18, EDGE), (28, 13, DETAIL), (21, 10, DETAIL)):
        s.line([face(44, z), face(44 + length, z)], ink)
    badge(s, "check", *face(65, 17), 13)
