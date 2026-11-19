from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w5 import folded_point, map_stroke, mountain_mark, standing_map

DESCRIPTION = "A folded trail map shows a dotted walking route that ends at a panoramic lookout pictogram."


def draw(s):
    standing_map(s)
    map_stroke(s, [(5, 7), (16, 8), (24, 14), (35, 12), (45, 18),
                   (43, 26), (50, 30), (56, 26)], BOLD, dashed=True)
    s.line([folded_point(x, z) for x, z in oval(6, 7, 2, 2, count=18)], EDGE)
    mountain_mark(s, folded_point, 63, 32, .53)
    map_stroke(s, [(54, 27), (57, 24), (69, 24), (72, 27)], EDGE)
    for x in (58, 68):
        map_stroke(s, [(x, 24), (x, 20)], DETAIL)
