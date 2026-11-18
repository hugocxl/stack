from geometry import DETAIL, EDGE
from scenes.redraws._w4 import bed_pictogram, clinic_clipboard

DESCRIPTION = "A sleep-study clipboard displays a bed pictogram above the ruled fields of its intake form."


def draw(s):
    form = clinic_clipboard(s)
    bed_pictogram(form, 16, 23, 1.02)
    form.line([(12, 51), (60, 51)], EDGE)
    for v in (60, 70, 80):
        form.frame(13, v, 9, 5, 1, DETAIL)
        form.rows(28, v + 4, (29,))
