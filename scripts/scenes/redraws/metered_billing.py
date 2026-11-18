from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import glyph
from scenes.redraws._w5 import currency_mark, folded_sheet, lens_outline, printed_stroke, rect, ruled_amounts

DESCRIPTION = "A utility bill pairs a meter dial with a usage-times-rate line above its itemized total."


def draw(s):
    face = folded_sheet(s, 61, 72, lean=.44, fold=12)
    lens_outline(s, face, 19, 54, 10)
    printed_stroke(s, face, oval(19, 52, 6.3, 7.6, 20, 160, 20))
    printed_stroke(s, face, [(16, 50), (22, 56)], EDGE)
    printed_stroke(s, face, [(34, 55), (46, 55)], EDGE)
    printed_stroke(s, face, [(34, 49), (51, 49)], DETAIL)

    for x, height in ((11, 4.5), (16, 7), (21, 10)):
        rect(s, face, x, 29, 2.8, height, .6)
    glyph(s, "x", *face(32, 34), 5.5, EDGE)
    currency_mark(s, face, 46, 34, 6.5)
    printed_stroke(s, face, [(8, 24), (52, 24)], DETAIL)
    ruled_amounts(s, face, ((17, 21), (9, 16)), 9, 51)
