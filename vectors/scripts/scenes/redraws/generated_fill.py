from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import chart_line, photo_print

DESCRIPTION = "A dashed selection surrounds the reconstructed lower corner of a landscape print."


def draw(s):
    p = photo_print(s)
    # The lake continues from the original image into the repaired corner.
    for x, z, length in ((34, 25, 54), (65, 19, 21), (77, 30, 12)):
        chart_line(s, p, [(x, z), (x + length, z)], EDGE if x >= 67 else DETAIL)
    selection = [(59, 16), (97, 16), (97, 45), (59, 45), (59, 16)]
    chart_line(s, p, selection, BOLD, dash=(4, 3))
