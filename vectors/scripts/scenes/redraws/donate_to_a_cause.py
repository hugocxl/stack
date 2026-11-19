from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import glyph
from scenes.redraws._w1 import upright_profile
from scenes.systems_shapes import rectangle

DESCRIPTION = "A coin halfway through the top slot drops into a donation box bearing a heart."


def draw(s):
    s.box(-30, -22, 0, 60, 44, 35, 4)
    s.box(-32, -24, 35, 64, 48, 5, 4)
    rectangle(s, -15, -3.2, 40, 30, 6.4, EDGE, 2)
    upright_profile(s, oval(0, 40, 11.5, 11.5, 180, 0, 36), 1.4, 2.2)
    s.line([(x, 1.4, z) for x, z in oval(0, 40, 8, 8, 13, 167, 28)], DETAIL)
    glyph(s, "heart", 0, 22, 18, 15, EDGE)
