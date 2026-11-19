from geometry import BOLD, DETAIL, EDGE, oval, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "A guitar stands behind the window of an instrument locker with a keyhole in its door."


def draw(s):
    s.box(0, 0, 0, 60, 31, 92, 3)
    door = Surface(s, (0, 32, 0))
    window = rounded(8, 9, 34, 73, 4)
    s.face([door.point(*p) for p in rounded(2, 3, 56, 86, 3)],
           openings=[[door.point(*p) for p in window]])
    guitar = [(22, 15), (16, 18), (13, 23), (13, 28), (17, 35), (16, 39),
              (17, 44), (21, 47), (23, 46), (24, 64), (22, 67), (23, 75),
              (30, 75), (31, 68), (28, 65), (28, 46), (32, 47), (36, 44),
              (37, 39), (34, 35), (38, 28), (38, 23), (35, 18), (29, 15)]
    door.stroke(guitar, BOLD, closed=True)
    door.oval(26, 35, 4, 4, EDGE)
    door.rules(21, 23, [10])
    door.rect(45, 34, 10, 21, 3, EDGE)
    keyhole = oval(50, 46, 2.7, 2.7, -48, 228, 18)
    door.stroke([*keyhole, (48, 39), (52, 39)], EDGE, closed=True)
    for z in (18, 72):
        door.rules(3, z, [4], ink=DETAIL)
