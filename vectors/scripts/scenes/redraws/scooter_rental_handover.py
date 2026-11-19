from geometry import BOLD, DETAIL, oval

DESCRIPTION = "A kick scooter has a key inserted into the lock on its steering stem."


def draw(s):
    for x in (8, 56):
        s.face([(a, 6, z) for a, z in oval(x, 8, 8, 8)[:-1]])
        s.line([(a, 6, z) for a, z in oval(x, 8, 3.7, 3.7)], DETAIL)
    s.box(7, 0, 9, 42, 12, 4, 3)
    s.tube([(16, 6, 12), (15, 6, 15), (8, 6, 17), (3, 6, 13)], 1.15)
    s.tube([(41, 6, 11), (49, 6, 19), (55, 6, 23)], 1.7)
    s.tube([(56, 6, 8), (54, 6, 31), (48, 6, 68)], 2)
    s.tube([(48, -8, 68), (48, 21, 68)], 1.8)
    for y in (-8, 15):
        s.tube([(48, y, 68), (48, y + 6, 68)], 2.8)
    s.box(49, 5, 41, 6, 6, 8, 1)
    s.tube([(53, 11, 45), (58, 12, 42), (61, 12, 42)], 1, DETAIL)
    s.face([(a, 12, z) for a, z in oval(64, 41, 5.5, 4.7, count=28)[:-1]], BOLD,
           openings=[[(a, 12, z) for a, z in oval(65, 41, 2, 1.8, count=20)[:-1]]])
