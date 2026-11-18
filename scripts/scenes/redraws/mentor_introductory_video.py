from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface
from scenes.redraws.introduction_buddy import avatar

DESCRIPTION = "A mentor profile fills a video display with a play badge centered along its lower edge."


def mentor_card(s):
    """Return the printed display and draw the mentor profile above its footer."""
    face = Surface(s, (0, 0, 0), rise=(-.20, .98), back=(0, -.98, -.20))
    face.plate(rounded(0, 0, 88, 67, 6), 8)
    face.rect(6, 13, 76, 48, 4, EDGE)
    avatar(face, 44, 37, 43)
    return face


def draw(s):
    face = mentor_card(s)
    face.rules(11, 7, [22])
    face.rules(55, 7, [22])
    badge(s, "play", *face.point(44, 7, -3), 12)
