from geometry import EDGE
from scenes.redraws.expired_member_access import member_emblem, membership_pass

DESCRIPTION = "A membership card has a ribbon-wrapped gift box attached at its right corner."


def draw(s):
    face = membership_pass(s)
    member_emblem(face, 24, 35, 14)
    face.rules(45, 42, [28], ink=EDGE)
    face.rules(45, 31, [20, 26], gap=8)
    s.box(71, 1, 15, 30, 24, 24, 1.5)
    s.box(69, -1, 37, 34, 28, 7, 1.5)
    for x in (83, 90):
        s.line([(x, 27, 16), (x, 27, 43), (x, 0, 44)], EDGE)
    for side in (-1, 1):
        s.line([(86, 13, 44), (86 + side * 12, 13, 55),
                (86 + side * 15, 13, 53), (86 + side * 15, 13, 48),
                (86, 13, 44)], EDGE)
