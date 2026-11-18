from geometry import DETAIL, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import landscape, paper

DESCRIPTION = "A matted landscape photo shows a faint repaired seam and a check badge on its frame."


def draw(s):
    print_ = paper(s, 82, pitch=.67, run=.52, angle=-27, depth=7)
    print_.slab(rounded(0, 0, 99, 82, 3), 7)
    print_.frame(5, 5, 89, 72, 2)
    landscape(print_, 12, 12, 75, 56)
    print_.line([(86, 26), (75, 39), (77, 47), (65, 51),
                 (67, 59), (57, 68)], DETAIL, dashed=True)
    badge(s, "check", *print_.at(98, 66), 17)
