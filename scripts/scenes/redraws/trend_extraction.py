from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w2 import chart_line, outline

DESCRIPTION = "A smooth rising trend crosses a finer noisy signal on an oscilloscope screen."


def draw(s):
    s.box(0, -34, 0, 112, 34, 73, 6)
    outline(s, 7, 0, 9, 76, 55, 4, EDGE)
    for z in (29, 45):
        s.line([(11, 0, z), (79, 0, z)], DETAIL, dashed=True)
    for z in (29, 50):
        ring = [(x, 0, v) for x, v in oval(96, z, 6, 6)]
        s.face(ring, EDGE)
        s.line([(96, 0, z + 1), (98, 0, z + 5)], DETAIL)
    def point(x, z):
        return (x, 0, z)

    chart_line(s, point, [(13, 20), (17, 26), (21, 18), (26, 34), (31, 26),
                          (35, 29), (40, 40), (45, 26), (50, 45), (54, 38),
                          (61, 52), (66, 41), (72, 57), (77, 51)], DETAIL)
    chart_line(s, point, [(13, 20), (26, 25), (39, 31), (52, 38),
                          (65, 46), (77, 52)], BOLD)
