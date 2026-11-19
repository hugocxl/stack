from scenes.redraws._w1 import exchange_arrows, workspace_layout
from scenes.systems_shapes import bezel

DESCRIPTION = "Two overlapping workspace windows with sidebars share opposing arrows between their title bars."


def draw(s):
    for x, y, z in ((-44, -7, 22), (-23, 8, 0)):
        s.box(x, y - 5, z, 62, 5, 42, 3)
        bezel(s, x + 3, y, z + 3, 56, 36, radius=1)
        workspace_layout(s, x + 3, y, z + 3, 56, 36, content="default")
    exchange_arrows(s, 29, 0, 52, 27)
