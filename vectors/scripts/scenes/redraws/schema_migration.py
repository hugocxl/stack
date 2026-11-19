from scenes.redraws._w1 import arc_arrow, schema_table

DESCRIPTION = "A migration arrow connects a two-field schema table to a revised three-field table."


def draw(s):
    schema_table(s, -53, 12, 2)
    schema_table(s, 7, -9, 3)
    arc_arrow(s, (-27, 8, 44), (30, -13, 44), 22, head=9)
