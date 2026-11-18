from geometry import BOLD
from scenes.redraws._kit import badge
from scenes.redraws._w4 import front_surface, printed_glyph, upright

DESCRIPTION = "A folded-corner source file displays large angle brackets and an open-shackle badge."


def draw(s):
    angle = -24
    upright(s, [(0, 0), (69, 0), (69, 66), (51, 84), (0, 84)], 7, 6, angle=angle)
    file = front_surface(s, angle=angle, y=7)
    file.line([(51, 84), (51, 66), (69, 66)])
    file.line([(22, 57), (12, 45), (22, 33)], BOLD)
    printed_glyph(file, "slash", 35, 45, 16, BOLD)
    file.line([(47, 57), (57, 45), (47, 33)], BOLD)
    file.rows(14, 21, (36, 25), step=-7)
    badge(s, "unlock", *file.at(66, 66), 15)
