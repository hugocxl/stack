from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w3 import Surface, component_art

DESCRIPTION = "A vernier caliper closes its jaws against opposite edges of a diamond-marked sample tile."


def draw(s):
    caliper = Surface(s, (0, 0, 0), rise=(-.61, .79), back=(0, -.79, -.61),
                      across=(.94, -.34))
    fixed = [(0, 66), (119, 66), (121, 64), (121, 51), (19, 51), (19, 15),
             (7, 15), (1, 30), (0, 42)]
    caliper.plate(fixed, 6)
    for x in range(23, 119, 7):
        caliper.stroke([(x, 66), (x, 59 if x % 2 else 62)], DETAIL)

    tile = Surface(s, caliper.point(19, 11, -1), rise=caliper.rise, back=caliper.back,
                   across=caliper.across)
    tile.plate(rounded(0, 0, 47, 33, 2), 7)
    component_art(tile, 23.5, 17, 20, 17, EDGE)

    jaw = Surface(s, caliper.point(0, 0, -4), rise=caliper.rise, back=caliper.back,
                  across=caliper.across)
    jaw.plate([(62, 48), (62, 69), (90, 69), (90, 48), (83, 48),
               (80, 26), (73, 15), (66, 15), (66, 48)], 5)
    jaw.rules(67, 55, [18], ink=EDGE)
    for x in (69, 74, 79, 84):
        jaw.stroke([(x, 55), (x, 59)], DETAIL)
    jaw.oval(76, 63, 3, 3, EDGE)
