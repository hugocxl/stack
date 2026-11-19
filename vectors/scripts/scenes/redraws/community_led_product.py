from geometry import BOLD, EDGE
from scenes.redraws._w4 import speech_bubble, standing_card

DESCRIPTION = "A three-milestone roadmap pairs its highlighted priority with a member speech bubble."


def draw(s):
    road = standing_card(s, 106, 68, angle=-13, lean=.38, depth=8)
    road.rows(11, 56, (36,), ink=EDGE)
    road.line([(10, 15), (95, 15)], EDGE)
    for milestone in (19, 46, 77):
        road.line([(milestone, 11), (milestone, 19)], EDGE)
    for u, v, width in ((19, 42, 22), (77, 20, 19)):
        road.frame(u, v, width, 7, 3, EDGE)
    road.frame(46, 27, 28, 11, 4, BOLD)
    road.rows(52, 32.5, (16,))
    comment = speech_bubble(s, width=38, height=24, angle=-13, y=1, z=62, u0=72, tail_at=.10)
    for x in (11, 19, 27):
        comment.oval(x, 12, 1.3, 1.3, EDGE)
