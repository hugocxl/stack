from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws.community_forum import balloon

DESCRIPTION = "Two report lines sit inside a speech balloon with a check badge on its upper corner."


def draw(s):
    face = balloon(s, (0, 0, 0), 97, 58, depth=7)
    face.rules(19, 36, [49, 37], gap=13, ink=EDGE)
    badge(s, "check", 93, 2, 51, 15)
