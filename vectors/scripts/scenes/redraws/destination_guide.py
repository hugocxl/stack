from geometry import DETAIL, EDGE
from scenes.redraws._sf import ground, map_pin, plate, squircle

DESCRIPTION = "A thick closed guidebook lies flat with a map pin standing on its cover."


def draw(s):
    w, d, h = 70, 92, 12
    cover = ground(-w/2, -d/2, h)
    plate(s, cover, squircle(w, d, 5), h, (0, 0, -1))
    s.line([(w/2 - 2, -d/2 + 6, h*.5), (w/2 - 2, d/2 - 6, h*.5)], DETAIL)
    s.line([(-w/2 + 6, d/2 - 2, h*.5), (w/2 - 6, d/2 - 2, h*.5)], DETAIL)
    s.line([cover(u, v) for u, v in [(10, 18), (26, 40), (40, 30), (60, 62)]], DETAIL, dashed=True)
    s.line([cover(8, d - 12), cover(w - 8, d - 12)], DETAIL)
    map_pin(s, 0, 4, h, 16)
