from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import software_package, upright_profile

DESCRIPTION = "A narrow release branch reaches a raised test flask before the main path reaches a software package."


def draw(s):
    arrow(s, [(-48, 5, 17), (19, 5, 17)], BOLD, head=9)
    arrow(s, [(-27, 5, 17), (-17, 5, 28), (-17, 5, 48), (-1, 5, 48)],
          EDGE, head=5)

    flask = [(0, 37), (-2, 41), (5, 55), (5, 62), (3, 62), (3, 66),
             (17, 66), (17, 62), (15, 62), (15, 55), (22, 41), (20, 37)]
    upright_profile(s, flask, 5, 6)
    s.line([(1, 5, 46), (18, 5, 46)], EDGE)
    for x, z, radius in ((7, 42, 1.4), (13, 50, 1.6)):
        s.line([(u, 5, v) for u, v in oval(x, z, radius, radius, count=14)], DETAIL)
    software_package(s, 48, 1, 5, .59)
