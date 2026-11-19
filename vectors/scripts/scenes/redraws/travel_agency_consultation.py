from geometry import BOLD, DETAIL, EDGE, oval

DESCRIPTION = "A thick speech bubble contains a folded map with a route between two waypoints."


def draw(s):
    outline = [(0, 18), (0, 53), (5, 59), (65, 59), (71, 53), (71, 18),
               (65, 12), (27, 12), (13, 0), (13, 12), (5, 12)]
    s.face([(x, -5, z) for x, z in outline], DETAIL)
    s.face([(x, 0, z) for x, z in outline])
    face = lambda x, z: (x, 0, z)

    border = [(10, 24), (25, 28), (43, 23), (61, 30), (61, 47),
              (43, 41), (25, 46), (10, 42), (10, 24)]
    s.line([face(x, z) for x, z in border], EDGE)
    for x, lo, hi in ((25, 28, 46), (43, 23, 41)):
        s.line([face(x, lo), face(x, hi)], DETAIL)
    s.line([face(x, z) for x, z in ((16, 34), (25, 38), (34, 31),
                                   (43, 30), (48, 36), (54, 38))], BOLD)
    for x, z in ((16, 34), (54, 38)):
        s.face([face(a, b) for a, b in oval(x, z, 1.9, 1.9, count=16)[:-1]], EDGE)
