from geometry import BOLD, EDGE, rounded
from scenes.redraws._w4 import Surface, attached_panel, landscape
from scenes.redraws.external_link_handoff import browser

DESCRIPTION = "An article window has a raised scroll thumb partway down the right-hand track."


def draw(s):
    article = browser(s, 83, 90, angle=-7, lean=.23)
    article.rows(11, 66, (37,), ink=EDGE)
    article.rows(11, 58, (29,))
    photo = Surface(s, lambda u, v: article.at(11 + u, 49 - v))
    landscape(photo, 0, 0, 47, 21)
    article.rows(11, 18, (45, 39), step=-8)
    article.frame(70, 6, 7, 65, 3.5, EDGE)
    thumb = attached_panel(article, .8)
    thumb.slab(rounded(69, 33, 9, 19, 4.5), 3, BOLD)
