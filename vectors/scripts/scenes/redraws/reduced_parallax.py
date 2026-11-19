from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import arrow, badge
from scenes.redraws._w3 import Surface

DESCRIPTION = "A slash badge overlaps a motion arrow beneath the foreground and background ridges of a deep landscape window."


def draw(s):
    rear = Surface(s, (0, -9, 0))
    frame = rounded(0, 0, 88, 70, 4)
    rear.plate(frame, 2)
    rear.stroke([(0, 27), (24, 49), (42, 34), (61, 55), (86, 31)], DETAIL)
    rear.oval(40, 53, 4, 4, DETAIL)

    front = Surface(s, (0, 0, 0))
    s.line([rear.point(4, 70), front.point(4, 70)], EDGE)
    s.line([rear.point(88, 4), front.point(88, 4)], EDGE)
    opening = [front.point(*p) for p in
               [(7, 19), (26, 36), (43, 24), (62, 39), (81, 24), (81, 63), (7, 63)]]
    s.face([front.point(x, v) for x, v in frame], EDGE, openings=[opening])
    arrow(s, [front.point(20, 10), front.point(63, 10)], EDGE, head=6)
    badge(s, "slash", *front.point(78, 9, -1), 13)
