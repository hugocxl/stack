from geometry import DETAIL, EDGE
from scenes.redraws._w4 import folder_emblem, front_surface, raised_lens

DESCRIPTION = "A magnifying glass rests against the indexed folders peeking out of an open archival file box."


def draw(s):
    width, depth, height = 84, 58, 31
    s.face([(0, 0, 0), (width, 0, 0), (width, 0, height), (0, 0, height)])
    s.face([(0, 0, 0), (0, depth, 0), (0, depth, height), (0, 0, height)])
    for y, level in ((7, 55), (20, 50), (33, 45)):
        face = front_surface(s, angle=0, y=y, z=6)
        folder_emblem(face, 6 + (y - 7)*.28, 0, 65, level, solid=True)
    s.face([(width, 0, 0), (width, depth, 0), (width, depth, height), (width, 0, height)])
    s.face([(0, depth, 0), (width, depth, 0), (width, depth, height), (0, depth, height)])
    front = front_surface(s, angle=0, y=depth)
    front.frame(29, 12, 25, 9, 2, DETAIL)
    front.rows(34, 16.5, (15,), ink=EDGE)
    raised_lens(front, 57, 46, 17)
