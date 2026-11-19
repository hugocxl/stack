from geometry import EDGE
from scenes.redraws.membership_renewal import member_pass

DESCRIPTION = "Three staggered membership passes fan out behind the front card, which carries a house emblem."


def draw(s):
    member_pass(s, (21, -15, 12), width=62, height=47, lean=.52)
    member_pass(s, (11, -8, 5), width=78, height=56, lean=.38)
    face = member_pass(s)
    face.oval(27, 30, 17, 17)
    face.stroke([(16, 30), (27, 40), (38, 30)], EDGE)
    face.stroke([(19, 32), (19, 21), (35, 21), (35, 32)], EDGE)
    face.stroke([(25, 21), (25, 27), (30, 27), (30, 21)], EDGE)
    face.rules(53, 34, [25], ink=EDGE)
    face.rules(53, 24, [18])
