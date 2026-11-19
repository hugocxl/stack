from geometry import BOLD, DETAIL, oval, rounded
from scenes.redraws._w5 import food_bag_shell, panel, printed_stroke, rect

DESCRIPTION = "An open insulated delivery bag has an exposed lining and a water-drop cleaning patch on its front."


def draw(s):
    lid = lambda x, z: (x, 1 - .56 * (z - 31), z)
    panel(s, rounded(0, 30, 49, 28, 4), lid, 3)
    rect(s, lid, 4, 34, 41, 19, 3, DETAIL)
    s.tube([(15, 0, 34), (15, -1, 44), (19, -1, 47),
            (30, -1, 47), (34, -1, 44), (34, 0, 34)], 1.8)
    front = food_bag_shell(s, 49, 34, 31, open_top=True)
    printed_stroke(s, front, [(1.8, 28), (47.2, 28)], DETAIL)
    printed_stroke(s, front, [(44, 28), (44, 24)], DETAIL)
    # The sewn patch carries a pictogram the shared state kit does not currently provide.
    rect(s, front, 13, 4, 22, 20, 3, DETAIL)
    drop = [(24, 21), *oval(24, 12, 5, 5, 153, 387, 25), (24, 21)]
    printed_stroke(s, front, drop, BOLD)
