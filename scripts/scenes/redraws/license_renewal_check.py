from geometry import DETAIL, EDGE, oval
from scenes.redraws._w4 import front_surface, standing_card
from scenes.redraws.provider_profile import portrait

DESCRIPTION = "A magnifying glass rests over the expiration calendar printed on a professional license card."


def draw(s):
    card = standing_card(s, 96, 63, angle=-28, lean=.40, depth=6)
    card.frame(9, 16, 31, 33, 3)
    portrait(card, 24.5, 32, .85)
    card.rows(48, 49, (33,), ink=EDGE)
    card.rows(48, 42, (25,))
    card.frame(51, 13, 22, 21, 2.5, EDGE)
    card.line([(51, 27), (73, 27)], DETAIL)
    for x in (55, 69):
        card.line([(x, 32), (x, 36)], EDGE)
    card.rows(56, 20, (10,))

    lens = front_surface(s, angle=-28, y=3, z=6, lean=.40)
    s.tube([lens.at(76, 14), lens.at(103, -1)], 3.1, EDGE)
    outer = [lens.at(u, v) for u, v in oval(63, 24, 18.5, 18.5)[:-1]]
    inner = [lens.at(u, v) for u, v in oval(63, 24, 15.8, 15.8)[:-1]]
    s.face(outer, openings=(inner,))
