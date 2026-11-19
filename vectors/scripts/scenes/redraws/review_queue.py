from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w2 import folded_sheet, rule

DESCRIPTION = "Three folded review sheets stand in a stepped stack with a plus badge on the incoming sheet."


def draw(s):
    def plane(x, z):
        return .42*x, -.58*x - .32*z, .93*z

    for offset in (0, 15, 30):
        def point(x, z):
            return plane(x + offset, z + 21 - offset*.7)

        folded_sheet(s, point, 63, 78, fold=11, depth=4)
        rule(s, point, 11, 59, 29, EDGE)
        rule(s, point, 11, 46, 41)
        rule(s, point, 11, 32, 32)
    badge(s, "plus", *point(62, 63), 13)
