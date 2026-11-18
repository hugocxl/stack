from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws.exhibition_map import folded_map, mark

DESCRIPTION = "A bold route on a folded map ends at a clock-tower landmark."


def draw(s):
    panels = folded_map(s)
    route = [[(6, 12), (11, 24), (20, 24), (30, 37)],
             [(0, 37), (12, 29), (19, 29), (30, 21)],
             [(0, 21), (14, 21), (14, 29)]]
    for panel, segment in zip(panels, route):
        mark(s, panel, segment, BOLD)
    mark(s, panels[0], oval(6, 11, 2.4, 2.4, count=18), EDGE)
    for x, v, panel in [(10, 39, panels[0]), (17, 45, panels[1])]:
        mark(s, panel, [(x - 6, v + 9), (x + 2, v + 3), (x + 9, v + 8)], DETAIL)
        mark(s, panel, [(x - 3, v + 14), (x + 2, v + 11)], DETAIL)
    tower = panels[-1]
    mark(s, tower, [(6, 29), (6, 46), (3, 46), (14, 59), (25, 46),
                    (22, 46), (22, 29), (6, 29)], EDGE)
    mark(s, tower, [(6, 46), (22, 46)], EDGE)
    mark(s, tower, [(12, 29), (12, 34), (16, 34), (16, 29)], DETAIL)
    mark(s, tower, oval(14, 40, 4, 4, count=20), EDGE)
    mark(s, tower, [(14, 42), (14, 40), (16, 40)], BOLD)
