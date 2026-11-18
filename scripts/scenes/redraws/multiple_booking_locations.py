from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws.local_festival_routing import folded_map, map_path

DESCRIPTION = "Three location pins are printed across a folded map, with the center pin outlined in bold."


def draw(s):
    point = folded_map(s)
    map_path(s, point, [(4, 12), (28, 16), (42, 10), (60, 13), (83, 10)], DETAIL)
    map_path(s, point, [(3, 44), (19, 47), (30, 43), (39, 47)], DETAIL)
    map_path(s, point, [(50, 38), (64, 42), (81, 41)], DETAIL)
    for x, z, rx, ink in ((15, 31, 8, EDGE), (44, 36, 11, BOLD), (73, 29, 8, EDGE)):
        outline = [*oval(x, z, rx, 8, -30, 210, count=32), (x, z - 14)]
        s.face([point(a, b) for a, b in outline], ink)
        s.line([point(a, b) for a, b in oval(x, z, rx*.37, 2.9, count=32)], ink)
    s.line([point(a, b) for a, b in oval(44, 18, 7, 1.8, count=32)], EDGE)
