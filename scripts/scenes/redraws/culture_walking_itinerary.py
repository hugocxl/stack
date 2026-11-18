from geometry import DETAIL, EDGE
from scenes.redraws.local_festival_routing import folded_map, map_path

DESCRIPTION = "A dotted walking path on a folded map leads to the pictogram of a columned landmark."


def draw(s):
    point = folded_map(s)
    map_path(s, point, [(7, 14), (17, 12), (22, 20), (31, 19), (36, 34),
                        (48, 39), (55, 32), (64, 25)], dashed=True)
    map_path(s, point, [(61, 33), (73, 44), (85, 33), (61, 33)], EDGE)
    map_path(s, point, [(61, 22), (85, 22)], EDGE)
    map_path(s, point, [(61, 19), (85, 19)], EDGE)
    for u in (65, 73, 81):
        map_path(s, point, [(u, 33), (u, 22)], EDGE)
    for block in ([(6, 34), (13, 40), (22, 38)], [(33, 47), (43, 50), (52, 49)],
                  [(36, 10), (43, 15), (53, 11)]):
        map_path(s, point, block, DETAIL)
