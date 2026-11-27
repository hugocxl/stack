from scenes.redraws._kit import badge
from scenes.redraws._w5 import physical_key

DESCRIPTION = "A single notched key carries a refresh badge beside its round bow."


def draw(s):
    def point(u, v, z):
        return .94*u + .342*v, -.342*u + .94*v, z

    physical_key(s, lambda u, v: point(u, v, 0), 1.5)
    badge(s, "refresh", *point(4, -16, 4), 13)
