from geometry import EDGE, rounded
from scenes.redraws._w3 import Surface, interface_monitor, printed_glyph, visibility_art

DESCRIPTION = "A desktop display previews a moon-themed webpage with rounded cards and an eye control in its title bar."


def draw(s):
    screen = interface_monitor(s, w=116, h=80)
    screen.rules(6, 60, [104], ink=EDGE)
    screen.rules(12, 68, [11], ink=EDGE)
    screen.rect(30, 65, 39, 6, 2)
    printed_glyph(screen, "moon", 32, 36, 21)
    for x, v in ((48, 46), (23, 53)):
        screen.stroke([(x - 2, v), (x + 2, v)])
        screen.stroke([(x, v - 2), (x, v + 2)])
    screen.rules(53, 47, [40], ink=EDGE)
    screen.rules(53, 37, [32, 25], gap=6)
    for x in (15, 47, 79):
        screen.rect(x, 11, 24, 11, 5, EDGE)

    control = Surface(s, screen.point(87, 60, -4), across=screen.across)
    control.plate(rounded(0, 0, 33, 23, 5), 3)
    visibility_art(control, 16.5, 11.5, 10)
