from geometry import BOLD, EDGE, oval
from scenes.redraws.page_moved import Surface

DESCRIPTION = "A two-bay server carries a restart arrow that travels around an open circular path."


def draw(s):
    s.box(0, 0, 0, 84, 48, 52, 4)
    server = Surface(s, (0, 48, 0))
    for z in (6, 29):
        server.frame(6, z, 72, 16, 2, EDGE)
        server.line([(13, z + 8), (42, z + 8)], EDGE)
        for x in (58, 68):
            server.loop(oval(x, z + 8, 2.4, 2.4, count=12)[:-1], EDGE)
    indicator = Surface(s, (84, 11, 52), screen=True)
    indicator.plate(oval(0, 0, 20, 20, count=48)[:-1], 0)
    indicator.line(oval(0, 0, 12, 12, 120, 200, 18), EDGE, dashed=True)
    indicator.arrow(oval(0, 0, 12, 12, 200, 430, 42), BOLD, head=5)
