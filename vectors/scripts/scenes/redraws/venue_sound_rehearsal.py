from geometry import DETAIL, EDGE
from scenes.redraws._w3 import Surface

DESCRIPTION = "A stage with tied-back curtains and steps has a loudspeaker mounted on its right proscenium post."


def draw(s):
    s.box(0, 0, 0, 102, 41, 10, 2)
    s.box(28, 40, 0, 46, 18, 4, 1)
    s.box(28, 40, 4, 46, 9, 3, 1)

    curtain = Surface(s, (0, 34, 10))
    for x, sign in ((11, 1), (91, -1)):
        outline = [(x, 0), (x + 23 * sign, 0), (x + 13 * sign, 24),
                   (x + 19 * sign, 39), (x + 34 * sign, 55), (x, 55)]
        curtain.plate(outline, 2)
        for offset in (5, 10):
            curtain.stroke([(x + (offset + 5) * sign, 2), (x + offset * sign, 24),
                            (x + (offset + 7) * sign, 39),
                            (x + (offset + 19) * sign, 54)], DETAIL)
        curtain.rules(min(x, x + 13 * sign), 24, [13], ink=EDGE)
    for x in (0, 89):
        s.box(x, 21, 10, 13, 16, 55, 1)
    s.box(-2, 19, 63, 106, 20, 12, 2)
    s.box(86, 37, 31, 24, 12, 30, 3)
    speaker = Surface(s, (86, 49, 31))
    speaker.oval(12, 10, 7.2, 7.2, EDGE)
    speaker.oval(12, 10, 3.1, 3.1, DETAIL)
    speaker.oval(12, 23, 3.5, 3.5, EDGE)
