from scenes.redraws._kit import badge
from scenes.redraws.community_forum import balloon

DESCRIPTION = "A speech balloon with three typing dots carries a pause badge on its upper corner."


def draw(s):
    face = balloon(s, (0, 0, 0), 97, 58, depth=7)
    for x in (28, 46, 64):
        face.oval(x, 28, 3.1, 3.1)
    badge(s, "pause", 93, 2, 51, 15)
