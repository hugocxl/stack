from geometry import EDGE, oval
from scenes.redraws._w3 import sheet

DESCRIPTION = "A specimen sheet displays six large letterforms from different writing systems in a two-row grid."

# Each item is a small, hand-drawn letterform in a common specimen frame.
SPECIMENS = (
    (((-5, -7), (0, 7), (5, -7)), ((-3, -2), (3, -2))),
    (tuple(oval(0, 0, 5, 7, -43, 43, 9)),
     tuple(oval(0, 0, 5, 7, 42, 319, 22)), ((-5, -7), (-2, -7)), ((2, -7), (5, -7))),
    (((-6, 4), (5, 4)), ((-2, 7), (-3, 0), (-2, -5), (0, -6)),
     ((4, 1), (2, -3), (-2, -6), (-6, -5), (-6, -2), (-4, 0),
      (0, 1), (4, 0), (6, -3), (5, -6), (2, -8))),
    (((-6, 5), (6, 5)), ((2, 5), (2, -7)),
     ((2, 0), (-2, 2), (-5, 0), (-4, -3), (-1, -3), (2, 0),
      (5, 1), (7, -1), (5, -5))),
    (((-5, 6), (6, -7)), ((-1, 1), (-5, -1), (-6, -7)),
     ((2, -2), (5, 1), (5, 6))),
    (((5, -1), (5, 2), (2, 4), (-1, 3), (-1, 0), (2, -2),
      (5, -1), (-1, 0), (-5, -1), (-5, -7)),),
)


def draw(s):
    page = sheet(s, 93, 73, rise=(-.56, .83), depth=6)
    for x in (33, 61):
        page.stroke([(x, 10), (x, 55)])
    page.stroke([(9, 33), (84, 33)])
    for index, strokes in enumerate(SPECIMENS):
        place = page.viewer_axes(19 + index % 3 * 28, 47 - index // 3 * 25)
        for stroke in strokes:
            page.stroke([place(x * 1.2, v * 1.2) for x, v in stroke], EDGE)
