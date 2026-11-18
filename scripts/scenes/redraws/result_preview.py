from geometry import EDGE
from scenes.redraws._w2 import face_magnifier
from scenes.redraws._w4 import Surface, attached_panel, landscape, standing_card

DESCRIPTION = "A large magnifier straddles the corner of the image thumbnail on a single search result card."


def draw(s):
    result = standing_card(s, 100, 56, angle=-8, lean=.37, depth=7)
    image = Surface(s, lambda u, v: result.at(u + 9, 47 - v))
    landscape(image, 0, 0, 39, 35)
    result.rows(59, 43, (27,), ink=EDGE)
    result.rows(59, 31, (30, 25, 19), step=-8)
    lens = attached_panel(result, 3)
    face_magnifier(s, lens.at, 17, 13, 15, direction=(-.72, -.69))
