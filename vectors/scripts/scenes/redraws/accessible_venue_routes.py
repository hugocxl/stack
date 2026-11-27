from geometry import DETAIL, EDGE

DESCRIPTION = "A long gentle ramp in front and a short flight of steps to the side both reach the same raised landing."


def draw(s):
    H = 24
    s.box(0, -20, 0, 44, 40, H, 1.5)
    # Steps climb to the landing from the right.
    for i, h in enumerate((18, 12, 6)):
        s.box(44 + i*11, -20, 0, 11, 40, h, .8)
    # The ramp descends from the front edge of the landing toward the viewer.
    s.face([(44, 20, 0), (44, 96, 0), (44, 20, H)], EDGE)
    s.face([(0, 20, H), (44, 20, H), (44, 96, 0), (0, 96, 0)], EDGE)
    for x in (0, 44):
        s.line([(x, 96, 3), (x, 20, H + 3)], DETAIL)
    s.line([(4, 92, .6), (40, 92, .6)], DETAIL)
