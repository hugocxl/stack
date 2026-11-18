from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import badge, coin

DESCRIPTION = "An upward badge sits beside a deadbolt cylinder with a key inserted in its keyway."


def deadbolt(s, *, inserted):
    """Draw the same round keyed hardware with or without the inserted key."""
    coin(s, 0, 9, 36, 32, depth=10)
    coin(s, 0, 13, 36, 21, depth=4)
    for z in (8.5, 63.5):
        s.line([(u, 9.1, v) for u, v in oval(0, z, 1.5, 1.5)], DETAIL)
    keyway = [(-2.2, 29), (2.2, 29), (2.2, 35), (4, 39), (2, 43),
              (-2, 43), (-4, 39), (-2.2, 35), (-2.2, 29)]
    s.line([(u, 13.2, v) for u, v in keyway], EDGE)
    if inserted:
        s.face([(0, 13, 37), (0, 38, 37), (0, 38, 31), (0, 13, 32)], EDGE)
        rim = [(0, u, v) for u, v in oval(49, 34, 14, 10)]
        opening = [(0, u, v) for u, v in oval(54, 34, 3.8, 3.8)]
        s.face(rim, EDGE, openings=(opening,))


def draw(s):
    deadbolt(s, inserted=True)
    badge(s, "up", 28, 8, 65, 14)
