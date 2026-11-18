from geometry import EDGE, oval
from scenes.redraws._w5 import bed_mark, rect

DESCRIPTION = "A hotel-room door bears a bed plaque and a large toothed key engaged in its lock."


def draw(s):
    s.box(0, -10, 0, 51, 16, 70, 1.5)
    face = lambda x, z: (x, 6, z)
    rect(s, face, 4, 1, 43, 65, 1.6)
    s.box(10, 6, 45, 29, 2.5, 16, 2)
    bed_mark(s, lambda x, z: (x, 8.5, z), 24.5, 53, .65)
    s.tube([(38, 6, 36), (38, 9, 36), (29, 9, 36)], 1.5)
    s.face([face(x, z) for x, z in oval(39, 27, 4.2, 4.2, count=28)[:-1]])
    # The key starts in the lock and projects out from the door.
    key = lambda u, v: (39 + u*.23, 6 + u, 27 + v)
    s.face([key(u, v) for u, v in [(0, -1), (0, 2), (23, 2), (23, -2),
                                     (14, -2), (14, -5), (10, -5), (10, -2),
                                     (6, -2), (6, -4), (3, -4), (3, -1)]], EDGE)
    s.face([key(u, v) for u, v in oval(28, 0, 8.5, 7.5, count=36)[:-1]],
           openings=[[key(u, v) for u, v in oval(28, 0, 4.4, 3.5, count=24)[:-1]]])
