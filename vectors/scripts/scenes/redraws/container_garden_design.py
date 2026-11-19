from geometry import DETAIL, rounded
from scenes.redraws._w5 import seedling

DESCRIPTION = "A deep rectangular planter contains three evenly spaced seedlings."


def draw(s):
    s.solid(rounded(3, 3, 64, 31, 4), 0, 19,
            top=rounded(0, 0, 70, 37, 4), crease=False)
    s.face([(x, y, 19) for x, y in rounded(0, 0, 70, 37, 4)],
           openings=[[(x, y, 19) for x, y in rounded(4, 4, 62, 29, 3)]])
    s.line([(7, 35.5, 12), (65, 35.5, 12)], DETAIL)
    s.line([(9, 8, 18.9), (61, 8, 18.9)], DETAIL)
    for x, y, h in ((14, 14, 23), (35, 19, 29), (56, 23, 22)):
        seedling(s, x, y, 19, h)
