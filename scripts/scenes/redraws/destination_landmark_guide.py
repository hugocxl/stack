from geometry import BOLD, DETAIL
from scenes.redraws._w5 import folded_point, location_pin, map_stroke, standing_map

DESCRIPTION = "An accordion-fold city map shows an Eiffel Tower location pin on its street grid."


def draw(s):
    standing_map(s)
    for street in (
        [(4, 10), (26, 10), (44, 16), (71, 17)],
        [(4, 25), (21, 25), (35, 31), (59, 31), (71, 37)],
        [(13, 4), (14, 16), (18, 25), (18, 39)],
        [(28, 4), (29, 17), (27, 28), (30, 39)],
        [(56, 4), (57, 16), (55, 28), (62, 40)],
        [(66, 4), (66, 17), (71, 23)],
    ):
        map_stroke(s, street, DETAIL)

    def marker(x, z):
        # A single rigid marker stands just ahead of the paper folds.
        return x, 8 - z * .32, z

    location_pin(s, marker, 43, 36, 15, hole=False)
    tower = [(33.5, 27), (37, 32), (39.5, 37), (41.2, 42),
             (42.1, 46), (43.9, 46), (44.8, 42), (46.5, 37),
             (49, 32), (52.5, 27), (48.2, 27), (47.1, 29.8),
             (45.2, 31.6), (43, 32.2), (40.8, 31.6), (38.9, 29.8),
             (37.8, 27), (33.5, 27)]
    s.line([marker(x, z) for x, z in tower], BOLD)
    s.line([marker(36, 34), marker(50, 34)], DETAIL)
    s.line([marker(38.6, 40), marker(47.5, 40)], DETAIL)
    s.line([marker(43, 46), marker(43, 49)], DETAIL)
