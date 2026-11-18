from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w5 import coin_stack, lens_outline, panel, rect

DESCRIPTION = "A partly open safe reveals a stack of coins behind its thick combination door."


def draw(s):
    s.box(0, -38, 0, 64, 34, 59, 5)
    front = lambda x, z: (x, 0, z)
    outer = rounded(0, 0, 64, 59, 4)
    inner = rounded(8, 7, 48, 45, 2.5)
    s.face([front(x, z) for x, z in outer], EDGE,
           openings=[[front(x, z) for x, z in inner]])
    rect(s, lambda x, z: (x, -4, z), 10, 8, 44, 43, 2.2, DETAIL)
    coin_stack(s, 39, -4, 9, 8, 5)
    for z in (13, 45):
        s.tube([(6, 1, z - 4), (6, 1, z + 4)], 2.7)
    door = lambda x, z: (6 + x * .20, 2 + .96 * x, z)
    panel(s, rounded(0, 5, 48, 49, 3), door, 6)
    lens_outline(s, door, 29, 32, 10.5, EDGE)
    lens_outline(s, door, 29, 32, 5.6, DETAIL)
    s.line([door(29, 34), door(29, 40)], EDGE)
    s.tube([door(29, 20), door(29, 13)], 2)
