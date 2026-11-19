from geometry import EDGE, rounded
from scenes.redraws._kit import glyph
from scenes.redraws._w5 import currency_mark, folder_with_insert, panel, printed_stroke, ruled_amounts

DESCRIPTION = "Two itemized donation receipts with currency totals are filed inside a tabbed folder marked with a heart."


def draw(s):
    def receipts():
        back = lambda x, z: (x, -10, z)
        panel(s, rounded(25, 10, 39, 56, 1.7), back, 1.8)
        printed_stroke(s, back, [(43, 58), (59, 58)], EDGE)
        face = lambda x, z: (x, -5, z)
        teeth = [(x, 64 if i % 2 == 0 else 61)
                 for i, x in enumerate(range(53, 12, -6))]
        s.face([face(x, z) for x, z in [(11, 14), (53, 14), *teeth, (11, 62)]])
        ruled_amounts(s, face, ((54, 15), (47, 12)), 16, 48, width=8)
        currency_mark(s, face, 26, 40, 4.2)
        printed_stroke(s, face, [(33, 40), (46, 40)], EDGE)

    face = folder_with_insert(s, receipts, height=31)
    glyph(s, "heart", *face(36, 16), 13, EDGE)
