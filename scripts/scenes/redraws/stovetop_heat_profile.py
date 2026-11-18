from geometry import BOLD, DETAIL, EDGE, oval

DESCRIPTION = "A four-burner stovetop shows increasing heat through different numbers of concentric burner rings."


def draw(s):
    s.box(0, 0, 0, 70, 59, 8, 4)
    for x, y, rings in ((18, 15, 1), (51, 15, 2), (18, 43, 3), (51, 43, 4)):
        s.ellipse(x, y, 8, 12, 12, EDGE)
        for i in range(1, rings):
            s.ellipse(x, y, 8, 12 - 2.7*i, 12 - 2.7*i,
                      BOLD if rings == 4 and i == 1 else DETAIL)
    for x, angle in ((12, 110), (27, 65), (42, 40), (57, 0)):
        rim = [(x, 59, z) for x, z in oval(x, 4, 3.4, 2.7, count=32)]
        s.face(rim[:-1])
        end = oval(x, 4, 2.4, 1.9, angle, angle, 1)[0]
        s.line([(x, 59, 4), (end[0], 59, end[1])], DETAIL)
