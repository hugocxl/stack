from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w4 import media_frame, paper

DESCRIPTION = "A citation card places three staggered attribution lines under a film thumbnail."


def draw(s):
    card = paper(s, 89, pitch=.65, run=.59, angle=-18, depth=6)
    card.slab(rounded(0, 0, 91, 89, 4), 6)
    media_frame(card, 12, 9, 67, 33, perforated=True)
    for v, width, ink in ((51, 28, EDGE), (63, 51, BOLD), (75, 37, DETAIL)):
        card.rows(13, v, (4,), ink=EDGE)
        card.rows(23, v, (width,), ink=ink)
