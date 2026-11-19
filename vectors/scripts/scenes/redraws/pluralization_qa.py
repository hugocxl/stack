from geometry import EDGE, oval
from scenes.redraws._w3 import sheet

DESCRIPTION = "A proof sheet compares a single file with two files beneath a magnifier."


def draw(s):
    page = sheet(s, 108, 69, rise=(-.43, .9), depth=5)
    page.rules(12, 55, [35], ink=EDGE)
    page.stroke([(47, 11), (47, 47)])
    for x in (19, 60, 81):
        v = 25
        page.stroke([(x, v), (x + 14, v), (x + 14, v + 13),
                     (x + 9, v + 18), (x, v + 18)], EDGE, closed=True)
        page.stroke([(x + 9, v + 18), (x + 9, v + 13), (x + 14, v + 13)])
    page.rules(16, 18, [21])
    page.rules(60, 18, [35])

    center = page.viewer_axes(77, 32)

    def lens(x, v):
        return page.point(*center(x, v), -3)

    s.tube([lens(14, -16), lens(32, -35)], 3.7)
    outer = [lens(x, v) for x, v in oval(0, 0, 23, 23)[:-1]]
    inner = [lens(x, v) for x, v in oval(0, 0, 20, 20)[:-1]]
    s.face(outer, EDGE, openings=(inner,))
