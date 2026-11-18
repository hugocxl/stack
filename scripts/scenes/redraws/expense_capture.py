from geometry import BOLD
from scenes.redraws._w5 import expense_receipt, printed_stroke

DESCRIPTION = "Four close camera corners frame an itemized receipt with a curled foot and a currency total."


def draw(s):
    expense_receipt(s)
    for x, dx in ((-9, 1), (64, -1)):
        for z, dz in ((-10, 1), (78, -1)):
            y = 7 if dz == 1 else -6
            corner = lambda u, v: (u, y - .34 * v, v)
            printed_stroke(s, corner, [(x, z + dz * 12), (x, z), (x + dx * 12, z)], BOLD)
