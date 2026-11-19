from geometry import EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._w2 import face_arrow, folded_sheet, rule

DESCRIPTION = "A backward-curving arrow wraps around the clock badge on a stepped stack of document revisions."


def draw(s):
    def front(x, z):
        return .64*x, -.36*x - .56*z, .82*z

    for offset in (20, 10, 0):
        def revision(x, z):
            a, b, c = front(x, z)
            return a - offset*.23, b - offset*.22, c + offset

        folded_sheet(s, revision, 72, 84, fold=12, depth=4)
    rule(s, front, 11, 65, 38, EDGE)
    for z, length in ((50, 29), (38, 30), (26, 26), (14, 33)):
        rule(s, front, 11, z, length)

    cx, cy, cz = front(78, 43)

    def orbit(x, z):
        return cx + x*.57735027, cy - x*.57735027, cz + z*1.15470054

    face_arrow(s, orbit, oval(0, 0, 24, 24, -68, 155, 44), EDGE, head=7)
    badge(s, "clock", cx, cy, cz, 17)
