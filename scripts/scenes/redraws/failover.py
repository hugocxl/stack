from scenes.redraws._w1 import arc_arrow, server_unit

DESCRIPTION = "A curved arrow switches from one rack server to its matching standby server."


def draw(s):
    server_unit(s, 18, -10)
    server_unit(s, -35, 23)
    arc_arrow(s, (-15, 9, 25), (39, -20, 28), 23)
