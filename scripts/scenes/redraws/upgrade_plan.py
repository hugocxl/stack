from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w5 import currency_mark, panel, printed_stroke, tier_bars

DESCRIPTION = "A standing subscription card shows rising plan tiers with an upward-arrow badge beside the highest tier."


def draw(s):
    face = lambda x, z: (x, -.33 * z, z)
    panel(s, rounded(0, 0, 57, 62, 5), face, 7)
    currency_mark(s, face, 15, 49, 6)
    printed_stroke(s, face, [(24, 50), (44, 50)], EDGE)
    printed_stroke(s, face, [(24, 43), (39, 43)], DETAIL)
    tier_bars(s, face, 11, 9, (10, 18, 26))
    badge(s, "up", *face(53, 39), 11.5)
