from geometry import EDGE
from scenes.redraws._kit import glyph
from scenes.redraws._w4 import camera_mark, standing_card
from scenes.redraws.find_a_clinic import medical_cross

DESCRIPTION = "A telehealth survey tablet shows a video camera and medical cross above a row of rating stars and two response lines."


def draw(s):
    tablet = standing_card(s, 88, 73, angle=5, lean=.43, depth=8)
    tablet.frame(5, 8, 78, 60, 3)
    camera_mark(tablet, 31, 56, .70)
    medical_cross(tablet, 62, 56, 5)
    tablet.line([(10, 44), (78, 44)])
    for u in (16, 30, 44, 58, 72):
        glyph(s, "star", *tablet.at(u, 35), 7, EDGE)
    tablet.rows(14, 18, (46, 56), step=7)
