from geometry import EDGE
from scenes.redraws.task_created import task_card, task_plane

DESCRIPTION = "A spring clip grips the stepped top edges of three stacked task cards."


def draw(s):
    for offset in (14, 7, 0):
        def point(x, z):
            a, b, c = task_plane(x, z)
            return a + offset*.32, b - offset, c + offset*.52

        task_card(s, point)

    # A metal jaw wraps from behind the last card to the face of the first.
    x, y, z = task_plane(35, 71)
    s.tube([(x + 5, y - 12, z + 4), (x + 7, y - 12, z + 18),
            (x + 9, y - 12, z + 22), (x + 17, y - 14, z + 22),
            (x + 19, y - 15, z + 19), (x + 20, y - 16, z + 4)], 1.35)
    s.face([(x, y - 14, z + 8), (x + 24, y - 20, z + 8),
            (x + 24, y - 6, z), (x, y, z)], EDGE)
    s.face([(x, y, z), (x + 24, y - 6, z), (x + 24, y - 2, z - 8),
            (x, y + 4, z - 8)], EDGE)
    s.tube([(x + 5, y + 2, z - 5), (x + 7, y + 1, z + 9),
            (x + 9, y, z + 13), (x + 17, y - 2, z + 13),
            (x + 19, y - 2, z + 10), (x + 20, y - 2, z - 5)], 1.35)
