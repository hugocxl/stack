from geometry import EDGE

DESCRIPTION = "A bold floor arrow turns into the aisle between two rows of warehouse racks."


def rack(s, x, y):
    """A two-level rack running along y, loaded with cartons."""
    for dy in (0, 77):
        for dx in (0, 21):
            s.box(x + dx, y + dy, 0, 3, 3, 60, .6)
    for z in (0, 28):
        s.box(x, y, z + 3, 24, 80, 3, 1)
        for dy in (6, 30, 54):
            s.box(x + 3, y + dy, z + 6, 18, 18, 16, 1.5)


def draw(s):
    rack(s, -62, -40)
    rack(s, 38, -40)
    s.face([(-8, -36, .2), (8, -36, .2), (8, 30, .2), (16, 30, .2), (0, 50, .2), (-16, 30, .2), (-8, 30, .2)], EDGE)
