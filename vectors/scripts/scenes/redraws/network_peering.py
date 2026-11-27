from geometry import EDGE
from scenes.redraws._sf import server

DESCRIPTION = "Two matching routers are joined directly by one cable."


def router(s, x, y):
    for dx in (8, 34):
        s.tube([(x + dx, y + 6, 14), (x + dx, y + 6, 40)], 1.6, EDGE)
    server(s, x, y, 0, 46, 32, 16)


def draw(s):
    router(s, -86, -16)
    s.tube([(-40, 0, 8), (40, 0, 8)], 2.4, EDGE)
    router(s, 40, -16)
