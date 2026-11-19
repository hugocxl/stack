from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface

DESCRIPTION = "An accordion-fold festival map with a winding route carries a download badge on its outer panel."


def draw(s):
    def point(x, z):
        panel = min(int(x // 30), 2)
        fraction = (x - 30 * panel) / 30
        return x, 13 * (fraction if panel == 1 else 1 - fraction), z

    # Alternate the crease depth so the map stands on its lower edge.
    for x in (0, 30, 60):
        s.face([point(x + u, v) for u, v in ((0, 0), (30, 0), (30, 65), (0, 65))])
        for path in (((4, 57), (19, 46), (27, 47)), ((9, 3), (12, 16), (24, 22), (27, 30))):
            s.line([point(x + u, v) for u, v in path], DETAIL)
    route = [point(x, z) for x, z in ((5, 33), (20, 26), (30, 38), (45, 47),
                                    (60, 38), (72, 42), (83, 52))]
    s.line(route, EDGE, dashed=True)
    Surface(s, route[0]).oval(0, 0, 3, 3, EDGE)
    badge(s, "down", 88, 2, 25, 13)
