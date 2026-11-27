from scenes.redraws._kit import badge
from scenes.redraws._sf import server

DESCRIPTION = "Two identical server stacks stand side by side, and an arrow badge switches traffic to the second."


def draw(s):
    for x in (-62, 12):
        for k in range(3):
            server(s, x, -17, k*20)
    badge(s, "arrow", -1, 17, 40, 12)
