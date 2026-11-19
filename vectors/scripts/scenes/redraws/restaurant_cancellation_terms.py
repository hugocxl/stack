from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w5 import folded_sheet, place_setting, printed_stroke

DESCRIPTION = "A folded-corner reservation policy sheet has a place-setting header and an x badge."


def draw(s):
    face = folded_sheet(s, w=47, h=66, lean=.27, fold=11)
    place_setting(s, face, 20, 51, 7.5)
    printed_stroke(s, face, [(8, 38), (39, 38)], EDGE)
    for z, end in ((32, 37), (26, 33), (20, 37), (14, 28)):
        printed_stroke(s, face, [(8, z), (end, z)], DETAIL)
    badge(s, "x", *face(44, 29), 10.5)
