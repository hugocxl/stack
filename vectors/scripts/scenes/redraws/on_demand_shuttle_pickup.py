from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws.next_bus_countdown import side_window, wheel_side

DESCRIPTION = "A four-window passenger shuttle carries the outline of a map pin on its sliding door."


def draw(s):
    y = 30
    for x in (14, 66):
        wheel_side(s, x, y - 1, 8)

    roof = [(0, 34), (4, 43), (53, 43), (61, 40), (72, 26), (80, 23), (81, 10)]
    for (a, z), (b, w) in zip(roof, roof[1:]):
        s.face([(a, 0, z), (b, 0, w), (b, y, w), (a, y, z)])
    arches = [(a, y, z) for x in (66, 14) for a, z in oval(x, 10, 9, 9, 0, 180, 20)]
    s.face([(0, y, 10), *[(x, y, z) for x, z in roof], *arches])
    for x, w in ((5, 12), (20, 12), (35, 13)):
        side_window(s, x, y, 26, w, 12)
    s.face([(52, y, 26), (68, y, 26), (59, y, 38), (52, y, 38)])
    s.line([(34, y, 13), (34, y, 39)], DETAIL)
    s.line([(50, y, 13), (50, y, 39)], DETAIL)
    s.line([(37, y, 24), (40, y, 24)], DETAIL)
    s.face([(63.35, 4, 37), (70.42, 4, 28), (70.42, 26, 28), (63.35, 26, 37)])
    s.line([(80.5, 4, 16), (80.5, 10, 16)], DETAIL)
    s.line([(80.5, 20, 16), (80.5, 26, 16)], DETAIL)

    # Printed service emblem, centred on the sliding door.
    drop = oval(42, 19.8, 4.15, 4.15, -29, 209, 32)
    s.line([(42, y, 13.1), *[(x, y, z) for x, z in drop], (42, y, 13.1)], BOLD)
    s.line([(x, y, z) for x, z in oval(42, 20.3, 1.1, 1.1, count=20)], EDGE)
