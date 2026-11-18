from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import arrow
from scenes.redraws._w5 import panel
from scenes.redraws.hotel_search import magnifier

DESCRIPTION = "A cross-border route passes through the lens of a magnifier on a regional map."


def draw(s):
    face = lambda x, z: (x, -.63 * z, z)
    panel(s, [(0, 0), (76, 0), (76, 55), (0, 55)], face, 3)
    boundary = [(39, 3), (33, 13), (39, 23), (37, 35), (43, 43), (40, 52)]
    s.line([face(x, z) for x, z in boundary], EDGE, dashed=True)
    for coast in (
        [(5, 10), (15, 11), (16, 17), (11, 25), (11, 34), (21, 36),
         (24, 44), (33, 48)],
        [(47, 8), (56, 12), (59, 21), (67, 20), (70, 25), (70, 36),
         (63, 41), (67, 47)],
    ):
        s.line([face(x, z) for x, z in coast], DETAIL)
    route = [(20, 27), (29, 27), (38, 30), (52, 30), (63, 30)]
    arrow(s, [face(x, z) for x, z in route], EDGE, head=6)
    s.face([face(x, z) for x, z in oval(20, 27, 2.1, 2.1, count=24)[:-1]])
    magnifier(s, *face(38, 30), 12)
