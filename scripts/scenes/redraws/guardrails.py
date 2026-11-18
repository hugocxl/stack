from geometry import BOLD, EDGE
from scenes.redraws._kit import arrow

DESCRIPTION = "A continuous route arrow bends between two parallel guardrails."


def draw(s):
    centerline = [(0, 0), (19, 0), (29, 2), (40, 10), (50, 12), (70, 12)]
    for side in (-18, 18):
        rail = [(x, y + side, 7) for x, y in centerline]
        for x, y, _ in (rail[0], rail[2], rail[-1]):
            s.tube([(x, y, 0), (x, y, 7)], 1.15, EDGE)
        s.tube(rail, 1.5, EDGE)
    route = [(x, y, 0) for x, y in centerline[1:-1]]
    arrow(s, [(4, 0, 0), *route, (64, 12, 0)], BOLD, 8)
