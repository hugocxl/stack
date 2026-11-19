from geometry import BOLD, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "A thick rounded speech bubble contains an upright lowercase beta symbol."


def cubic(start, control1, control2, end):
    points = []
    for step in range(1, 13):
        t = step / 12
        u = 1 - t
        points.append(tuple(u**3 * a + 3*u*u*t * b + 3*u*t*t * c + t**3 * d
                            for a, b, c, d in zip(start, control1, control2, end)))
    return points


def draw(s):
    bubble = Surface(s, (0, 0, 0), across=(.95, -.31))
    outline = [*rounded(0, 0, 83, 55, 12), (17, 0), (13, -15), (37, 0)]
    bubble.plate(outline, 7)
    align = bubble.viewer_axes(43, 28)

    # The upper and lower bowls meet the same continuous descending stem.
    stem = [(-11, -17), (-7, 7)]
    top = (3, 16)
    join = (-4, 2)
    lower = (0, -12)
    beta = [*stem, *cubic(stem[-1], (-6, 13), (-3, 16), top),
            *cubic(top, (15, 16), (15, 3), join),
            *cubic(join, (18, 4), (19, -12), lower),
            *cubic(lower, (-5, -12), (-7, -10), (-9.7, -9.2))]
    bubble.stroke([align(x, z) for x, z in beta], BOLD)
