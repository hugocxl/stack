from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w5 import audit_sheet, rect

DESCRIPTION = "A punched event log has calendar-marked entries with a clock badge attached to the date column."


def draw(s):
    face = audit_sheet(s)
    for z, length in ((13, 14), (29, 18), (45, 20)):
        rect(s, face, 17, z - 3.5, 8, 7, 1, EDGE)
        s.line([face(17, z + 1), face(25, z + 1)], DETAIL)
        s.line([face(29, z), face(29 + length, z)], EDGE)
    badge(s, "clock", *face(49, 32), 13)
