from geometry import BOLD, DETAIL, EDGE

DESCRIPTION = "A notched rail ticket shows a streamlined train with three speed lines."


def ticket(s, w=84, d=47):
    # Matching notches in the long edges separate the stub from the ticket.
    notch = w - 19
    outline = [(3, 0), (notch - 4, 0), (notch - 3, 3), (notch, 4), (notch + 3, 3),
               (notch + 4, 0), (w - 3, 0), (w, 3), (w, d - 3),
               (w - 3, d), (notch + 4, d), (notch + 3, d - 3),
               (notch, d - 4), (notch - 3, d - 3), (notch - 4, d),
               (3, d), (0, d - 3), (0, 3)]
    s.face([(x, y, 0) for x, y in outline], DETAIL)
    s.face([(x, y, 2.5) for x, y in outline], EDGE)
    for x, y in ((w, 3), (w, d - 3), (0, d - 3)):
        s.line([(x, y, 0), (x, y, 2.5)], DETAIL)
    s.line([(notch, 6, 2.5), (notch, d - 6, 2.5)], DETAIL, dashed=True)


def bullet_train(s):
    z = 2.5
    s.line([(20, 30, z), (56, 30, z), (59, 28, z), (58, 25, z), (53, 20, z),
            (41, 15, z), (20, 15, z), (20, 30, z)], BOLD)
    s.line([(57, 24, z), (43, 24, z), (38, 19, z), (47, 19, z)], EDGE)
    for x in (24, 30):
        s.line([(x, 19, z), (x + 3, 19, z), (x + 3, 23, z), (x, 23, z), (x, 19, z)], DETAIL)


def draw(s):
    ticket(s)
    bullet_train(s)
    for y, x in ((17, 9), (22.5, 5), (28, 11)):
        s.line([(x, y, 2.5), (16, y, 2.5)], EDGE)
    for x in (72, 76):
        s.line([(x, 15, 2.5), (x, 31, 2.5)], DETAIL)
