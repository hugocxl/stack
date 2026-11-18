from scenes.redraws._w1 import gear

DESCRIPTION = "A large toothed drive wheel meshes with two smaller gears."


def draw(s):
    for x, y, radius, phase in ((-21, -24, 15, 15), (24, -21.5, 15, 18), (0, 6, 24, 15)):
        gear(s, x, y, radius, phase)
