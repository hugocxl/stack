from geometry import EDGE
from scenes.redraws._w3 import Surface, profile_art

DESCRIPTION = "A thick cloud enclosure holds three discrete compartments, each marked with an account avatar."


def draw(s):
    cloud = Surface(s, (0, 0, 0), across=(.96, -.28))
    start = (18, 0)
    outline = [start]
    lobes = [
        ((-5, 0), (-6, 36), (16, 41)),
        ((22, 43), (31, 43), (36, 39)),
        ((38, 58), (48, 73), (66, 73)),
        ((81, 73), (92, 60), (94, 42)),
        ((109, 48), (129, 40), (129, 23)),
        ((130, 10), (121, 0), (108, 0)),
    ]
    for a, b, end in lobes:
        for i in range(1, 17):
            t = i / 16
            weights = ((1 - t) ** 3, 3 * (1 - t) ** 2 * t, 3 * (1 - t) * t ** 2, t ** 3)
            outline.append(tuple(sum(weight * coordinate for weight, coordinate in zip(weights, axis))
                                 for axis in zip(start, a, b, end)))
        start = end
    cloud.plate(outline, 12)
    for x in (13, 50, 87):
        cloud.rect(x, 7, 28, 28, 4, EDGE)
        profile_art(cloud, x + 14, 21, 13)
