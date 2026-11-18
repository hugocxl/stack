from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws.program_impact import community_house

DESCRIPTION = "A fitted solar panel follows the pitch of a house roof beside a check badge."


def draw(s):
    community_house(s)

    def roof(x, y, lift=0):
        return (x, y, 60 - y * 24 / 21 + lift)

    s.face([roof(-25, 3), roof(25, 3), roof(25, 18), roof(-25, 18)], EDGE)
    s.face([roof(-25, 3, 1.8), roof(25, 3, 1.8), roof(25, 18, 1.8), roof(-25, 18, 1.8)], EDGE)
    for x in (-15, -5, 5, 15):
        s.line([roof(x, 3, 1.8), roof(x, 18, 1.8)], DETAIL)
    s.line([roof(-25, 10.5, 1.8), roof(25, 10.5, 1.8)], DETAIL)
    badge(s, "check", 35, 3, 35, 11)
