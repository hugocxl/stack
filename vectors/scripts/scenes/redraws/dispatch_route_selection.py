from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws.local_festival_routing import folded_map, map_path

DESCRIPTION = "Two routes cross a folded street map, and a check badge marks the selected route at its endpoint."


def draw(s):
    point = folded_map(s)
    map_path(s, point, [(11, 20), (23, 39), (39, 46), (56, 35), (73, 41)], DETAIL, dashed=True)
    map_path(s, point, [(11, 20), (28, 16), (40, 25), (57, 18), (73, 41)], BOLD)
    map_path(s, point, [(4, 32), (13, 36), (23, 30)], DETAIL)
    map_path(s, point, [(61, 8), (73, 12), (84, 10)], DETAIL)
    s.face([point(a, b) for a, b in oval(11, 20, 3.6, 3.6, count=32)], EDGE)
    badge(s, "check", *point(74, 44), 12)
