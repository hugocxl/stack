from geometry import BOLD, DETAIL, EDGE, GUIDE
from scenes.redraws._kit import arrow
from scenes.redraws.museum_district_walk import folded_map, map_point

DESCRIPTION = "A folded trail map shows a solid detour arrow bending around a blocked segment of the dashed trail."


def draw(s):
    folded_map(s)
    for route in ([(9, 35), (26, 34), (39, 34)], [(47, 34), (55, 35), (75, 34)]):
        s.line([map_point(x, y) for x, y in route], EDGE, dashed=True)

    # The printed barrier crosses the original trail at its break.
    s.line([map_point(x, y) for x, y in
            ((40.5, 28.5), (45.5, 28.5), (45.5, 40), (40.5, 40), (40.5, 28.5))], EDGE)
    for y in (29.2, 32.5, 35.8):
        s.line([map_point(41, y), map_point(45, y + 2.5)], DETAIL)

    detour = [(9, 35), (18, 33), (24, 26), (26, 21), (32, 15), (39, 13), (47, 13),
              (52, 15), (55, 18), (61, 24), (66, 30), (75, 34)]
    arrow(s, [map_point(x, y) for x, y in detour], BOLD, head=6)
    for x, y, size in ((15, 16, 3), (68, 14, 4), (27.5, 46, 4), (61, 45, 3)):
        s.line([map_point(x - size, y + 2), map_point(x, y - 3), map_point(x + size, y + 2)], GUIDE)
