from geometry import EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w3 import Surface, sheet

DESCRIPTION = "A folded-corner settings file shows three slider controls and an arrow pointing out from its right edge."


def draw(s):
    edge = Surface(s, (0, 0, 0), rise=(-.38, .92))
    x, y, z = edge.point(59, 18)
    arrow(s, [(x, y, z), (x + 23, y - 23, z)], EDGE, head=11)
    page = sheet(s, 63, 79, rise=(-.38, .92), depth=5)
    for z, knob in ((53, 24), (38, 40), (23, 30)):
        page.rules(11, z, [41], ink=EDGE)
        s.face([page.point(x, v) for x, v in
                ((knob - 3, z - 5), (knob + 3, z - 5),
                 (knob + 3, z + 5), (knob - 3, z + 5))], EDGE)
