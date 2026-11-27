from geometry import EDGE
from scenes.redraws._sf import chevron_arrow, left_face, plate, plane

DESCRIPTION = "A bold arrow passes inward through an open doorway."


def draw(s):
    w, h, t = 56, 88, 8
    # The door leaf has swung inward on the far jamb, behind the frame.
    leaf = plane((w, -6, 0), (-.34, -.94, 0), (0, 0, 1))
    plate(s, leaf, [(0, 0), (w - 4, 0), (w - 4, h - 2), (0, h - 2)], 3, (-.94, .34, 0))
    # The arrow's head is already inside: draw it before the frame that hides it.
    shaft = plane((w/2, 78, 38), (0, -1, 0), (0, 0, 1))
    outline = chevron_arrow(108, 12, 22)
    plate(s, shaft, [(u, v) for u, v in outline if u >= 77] + [(77, 6), (77, -6)], 6, (-1, 0, 0), rim=False)
    # The frame stands on the floor with its opening toward the viewer's lower left.
    frame = left_face(0, 0, 0)
    portal = [(-t, 0), (0, 0), (0, h), (w, h), (w, 0), (w + t, 0), (w + t, h + t), (-t, h + t)]
    plate(s, frame, portal, 8, (0, -1, 0))
    plate(s, shaft, [(0, -6), (78, -6), (78, 6), (0, 6)], 6, (-1, 0, 0))
