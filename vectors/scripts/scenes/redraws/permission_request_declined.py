from scenes.redraws._kit import badge
from scenes.redraws.permission_requested import access_pass

DESCRIPTION = "An upright access pass with a lanyard slot and a keyhole carries an X badge."


def draw(s):
    face = access_pass(s)
    badge(s, "x", *face.point(57, 58), 13)
