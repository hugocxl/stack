from geometry import DETAIL, EDGE
from scenes.redraws._w3 import speech_outline
from scenes.redraws.local_festival_routing import folded_map, map_path

DESCRIPTION = "A walking path connects three speech-bubble story stops on a folded neighborhood map."


def draw(s):
    point = folded_map(s)
    map_path(s, point, [(5, 7), (10.25, 20.5), (21, 17), (33, 19), (37.25, 26.5),
                        (51, 19), (61, 21), (66, 31), (69.25, 41.5)], dashed=True)
    for x, v in ((8, 22), (35, 28), (67, 43)):
        bubble = speech_outline(x, v, 15, 10)
        map_path(s, point, [*bubble, bubble[0]], EDGE)
        map_path(s, point, [(x + 4, v + 6), (x + 11, v + 6)], EDGE)
    for block in ([(3, 42), (11, 48), (22, 46)], [(47, 10), (51, 5), (64, 5)],
                  [(32, 45), (37, 49), (49, 47)]):
        map_path(s, point, block, DETAIL)
