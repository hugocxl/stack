from scenes.redraws._sf import chevron_arrow, left_face, plate, plane

DESCRIPTION = "A bold arrow leaves through an open doorway toward the viewer."


def draw(s):
    w, h, t = 56, 88, 8
    leaf = plane((w, -6, 0), (-.34, -.94, 0), (0, 0, 1))
    plate(s, leaf, [(0, 0), (w - 4, 0), (w - 4, h - 2), (0, h - 2)], 3, (-.94, .34, 0))
    shaft = plane((w/2, -30, 38), (0, 1, 0), (0, 0, 1))
    plate(s, shaft, [(0, -6), (31, -6), (31, 6), (0, 6)], 6, (1, 0, 0), rim=False)
    frame = left_face(0, 0, 0)
    portal = [(-t, 0), (0, 0), (0, h), (w, h), (w, 0), (w + t, 0), (w + t, h + t), (-t, h + t)]
    plate(s, frame, portal, 8, (0, -1, 0))
    outline = chevron_arrow(112, 12, 24)
    plate(s, shaft, [(30, -6)] + outline[1:-1] + [(30, 6)], 6, (1, 0, 0))
