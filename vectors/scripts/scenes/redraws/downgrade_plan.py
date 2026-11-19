from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w5 import panel, printed_stroke, tier_bars

DESCRIPTION = "A standing subscription card shows ascending plan tiers with a downward-arrow badge beside them."


def draw(s):
    face = lambda x, z: (x, -.33 * z, z)
    panel(s, rounded(0, 0, 57, 62, 5), face, 7)
    printed_stroke(s, face, [(10, 50), (43, 50)], EDGE)
    printed_stroke(s, face, [(10, 43), (32, 43)], DETAIL)
    tier_bars(s, face, 11, 9, (10, 18, 26))
    badge(s, "down", *face(50, 22), 10.5)
