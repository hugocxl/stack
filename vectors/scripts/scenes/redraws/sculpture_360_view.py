from geometry import EDGE, oval
from scenes.redraws._kit import arrow

DESCRIPTION = "An orbit arrow wraps around the plinth beneath a standing ring sculpture."


def ring_sculpture(s, x, y, z, *, scale=1):
    """A standing abstract ring with its lower arc seated on a square plinth."""
    s.box(x - 20 * scale, y - 17 * scale, z, 40 * scale, 34 * scale,
          12 * scale, 2 * scale)
    path = [
        (x + u * scale, y + u * scale * .28, z + v * scale)
        for u, v in oval(0, 35, 15, 20, count=64)
    ]
    s.tube(path, 4.3 * scale, EDGE)


def draw(s):
    orbit = [(x, y, 2) for x, y in oval(0, 0, 39, 35, 215, 487, 70)]
    arrow(s, orbit, head=8)
    ring_sculpture(s, 0, 0, 0)
