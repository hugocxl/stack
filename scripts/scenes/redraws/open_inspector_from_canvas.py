from geometry import BOLD, DETAIL, EDGE, GUIDE, rounded
from scenes.redraws._w3 import Surface, component_art, selection_handle

DESCRIPTION = "An editor canvas on a laptop shows a selected diamond beside three fields in its attached inspector."


def draw(s):
    s.box(0, -2, 0, 108, 46, 5, 4)
    deck = Surface(s, (0, 44, 5), rise=(-1, 0))
    deck.rect(43, 4, 23, 10, 3)
    for y in (22, 30):
        for x in range(16, 95, 12):
            deck.rules(x, y, [7])

    screen = Surface(s, (0, 0, 5), rise=(-.22, .98), back=(0, -.98, -.22))
    screen.plate(rounded(0, 0, 108, 76, 5), 6)
    screen.rect(5, 6, 98, 64, 2, EDGE)
    screen.stroke([(5, 59), (103, 59)], DETAIL)
    screen.rules(11, 64, [17])
    screen.stroke([(65, 6), (65, 59)], EDGE)
    screen.rules(73, 51, [19], ink=EDGE)
    for z in (15, 26, 37):
        screen.rect(73, z, 22, 7, 1, EDGE)
        screen.rules(77, z + 3.5, [7])
    screen.stroke([(19, 17), (51, 17), (51, 47), (19, 47)],
                  GUIDE, closed=True, dashed=True)
    for x in (19, 51):
        for z in (17, 47):
            selection_handle(screen, x, z, 4)
    component_art(screen, 35, 32, 23, 21, BOLD)
