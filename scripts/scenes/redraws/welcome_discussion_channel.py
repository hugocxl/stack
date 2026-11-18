from geometry import BOLD, EDGE
from scenes.redraws.community_forum import balloon

DESCRIPTION = "A speech balloon contains an open doorway with an outlined welcome mat."


def draw(s):
    face = balloon(s, (0, 0, 0), 94, 65, depth=7)
    face.stroke([(31, 19), (31, 54), (59, 54), (59, 19)], BOLD)
    face.stroke([(31, 54), (45, 48), (45, 15), (31, 19)], closed=True, ink=BOLD)
    face.stroke([(41, 34), (41, 30)], BOLD)
    face.stroke([(49, 17), (62, 17), (66, 8), (45, 8)], EDGE, closed=True)
