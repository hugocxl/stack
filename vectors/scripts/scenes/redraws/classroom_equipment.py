from geometry import DETAIL, EDGE, rounded

DESCRIPTION = "A framed classroom whiteboard stands on two feet with a capped marker resting on its ledge."


def draw(s):
    for y in (15, 89):
        s.box(-12, y - 2, 0, 49, 7, 4, 2)
        s.box(5, y, 4, 7, 4, 42, 1)
    s.box(1, 4, 37, 12, 96, 56, 3)
    frame = [(14, y, z) for y, z in rounded(9, 42, 86, 46, 2)]
    s.line(frame + frame[:1], EDGE)
    s.line([(14, 82, 77), (14, 52, 77)], DETAIL)
    s.line([(14, 81, 69), (14, 60, 69)], DETAIL)
    s.box(11, 12, 35, 13, 79, 5, 1)
    s.tube([(19, 33, 42), (19, 57, 42)], 2)
    s.tube([(19, 29, 42), (19, 35, 42)], 2.4)
