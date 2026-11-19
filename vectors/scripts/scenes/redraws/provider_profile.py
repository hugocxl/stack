from geometry import EDGE
from scenes.redraws._w4 import bezier_path, standing_card

DESCRIPTION = "A standing provider profile card shows a large portrait pictogram and three service lines."


def portrait(face, u, v, scale=1, ink=EDGE):
    """Print a featureless head-and-shoulders symbol inside a credential."""
    face.oval(u, v + 8*scale, 7.2*scale, 7.2*scale, ink)
    shoulders = bezier_path(
        (-14, -9),
        ((-12, 1), (12, 1), (14, -9)),
        ((9, -13), (-9, -13), (-14, -9)),
    )
    face.outline([(u + a*scale, v + b*scale) for a, b in shoulders[:-1]], ink)


def provider_card(s):
    """A rigid landscape credential with its integral lanyard opening."""
    card = standing_card(s, 101, 66, angle=-28, lean=.40, depth=6)
    card.frame(40, 55, 21, 5.5, 2.65, EDGE)
    return card


def draw(s):
    card = provider_card(s)
    card.frame(10, 10, 38, 38, 4)
    portrait(card, 29, 28, 1.02)
    card.rows(56, 40, (33,), ink=EDGE)
    card.rows(56, 29, (28, 33, 21), step=-7)
