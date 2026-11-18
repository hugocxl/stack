from scenes.redraws._w5 import physical_key

DESCRIPTION = "A metal key has an open round bow and a visibly toothed bit."


def draw(s):
    def point(u, v, offset=0):
        return u, -.12 * u + .74 * v, 12 - .41 * v + offset

    physical_key(s, lambda u, v: point(u, v, -3.5), 2)
    physical_key(s, point, 2)
    s.line([point(17, -2), point(42, -2)])
