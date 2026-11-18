from geometry import BOLD, oval
from scenes.redraws._kit import arrow
from scenes.redraws._w5 import physical_key

DESCRIPTION = "A single notched key has a curved replacement arrow wrapping around its open bow."


def draw(s):
    def point(u, v, z):
        return .94*u + .342*v, -.342*u + .94*v, z

    physical_key(s, lambda u, v: point(u, v, 0), 1.5)
    physical_key(s, lambda u, v: point(u, v, 3), 1.5)
    orbit = oval(-1, 0, 20, 20, 32, 329, 54)
    arrow(s, [point(u, v, 3) for u, v in orbit], BOLD, head=6.5)
