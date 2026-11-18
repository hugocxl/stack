from geometry import DETAIL, rounded
from scenes.redraws._w5 import avatar_mark, dataset_table, panel

DESCRIPTION = "A dataset table has a clipped-on tile bearing a contact pictogram at its top corner."


def draw(s):
    face = dataset_table(s)
    x, y, z = face(57, 40)
    tile = lambda u, v: (x + u, y + 3, z + v)
    panel(s, rounded(-9, -8, 23, 28, 4), tile, 3)
    avatar_mark(s, tile, 2.5, 3.5, 1.08)
    s.tube([tile(-3.5, 20), tile(-3.5, 23), tile(8.5, 23), tile(8.5, 20)],
           .8, DETAIL)
