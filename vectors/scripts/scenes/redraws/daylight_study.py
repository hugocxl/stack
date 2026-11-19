from geometry import DETAIL, EDGE, GUIDE

DESCRIPTION = "A diagonal shaft of daylight passes through one pane of a window and meets the floor."


def draw(s):
    def frame(y):
        return [(0, y, 12), (69, y, 12), (69, y, 84), (0, y, 84)]

    def panes(y):
        return [[(l, y, b), (r, y, b), (r, y, t), (l, y, t)]
                for l, r in ((7, 32), (37, 62)) for b, t in ((19, 46), (51, 77))]

    s.face(frame(0), DETAIL, openings=panes(0))
    s.face([(69, 0, 12), (69, 7, 12), (69, 7, 84), (69, 0, 84)])
    s.face([(0, 0, 84), (69, 0, 84), (69, 7, 84), (0, 7, 84)])
    s.face(frame(7), EDGE, openings=panes(7))
    s.box(-3, -2, 9, 75, 14, 5, 1)

    aperture = [(9, 8, 22), (30, 8, 22), (30, 8, 44), (9, 8, 44)]
    light = [(x - .8*z, y + 1.25*z, 0) for x, y, z in aperture]
    for index in (1, 3):
        s.line([aperture[index], light[index]], DETAIL)
    s.line([aperture[0], light[0]], GUIDE, dashed=True)
    s.line(light + light[:1], EDGE)
