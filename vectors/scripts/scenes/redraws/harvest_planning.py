from geometry import BOLD, DETAIL
from scenes.redraws._w5 import calendar_grid, desk_calendar, printed_stroke, rect, smooth_loop

DESCRIPTION = "A standing farm calendar highlights a harvest week with a wheat sprig across its row."


def draw(s):
    face = desk_calendar(s)
    calendar_grid(s, face, 6, 4, 7.15, 7, 7, 1)
    calendar_grid(s, face, 6, 30, 7.15, 4.5, 7, 2)
    rect(s, face, 6, 11, 50.05, 19, .7, BOLD)
    printed_stroke(s, face, [(15, 15), (24, 19), (34, 21), (46, 23)], BOLD)
    leaf = smooth_loop([(0, 0), (-4, 3), (-6, 7), (-1, 6), (2, 3)])
    for x, z in ((25, 19), (32, 20.6), (39, 22)):
        for side in (-1, 1):
            printed_stroke(s, face, [(x + u + (1 - side)*.8, z + side*v*.74)
                                     for u, v in leaf + leaf[:1]], BOLD)
