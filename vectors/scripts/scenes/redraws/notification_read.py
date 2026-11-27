from shapely.geometry import MultiPoint
from shapely.ops import unary_union

from geometry import DETAIL, EDGE, oval, project
from scenes.redraws._kit import _screen, badge

DESCRIPTION = "A flared notification bell carries a check badge on its lower-right rim."


def _smooth(points, steps=6):
    """Catmull-Rom through the profile, so the bell's curve has no visible facets."""
    padded = [points[0], *points, points[-1]]
    out = []
    for i in range(1, len(padded) - 2):
        p0, p1, p2, p3 = padded[i-1:i+3]
        for k in range(steps):
            t = k/steps
            out.append(tuple(.5*(2*b + (-a + c)*t + (2*a - 5*b + 4*c - d)*t*t + (-a + 3*b - 3*c + d)*t**3)
                             for a, b, c, d in zip(p0, p1, p2, p3)))
    return out + [points[-1]]


def notification_bell(s):
    """The SF bell: a tall rounded crown, a waist that sweeps out into a flared lip,
    a short stem on top and the clapper showing just below the lip."""
    # (radius, height) from the lip up to the crown; overlapping bands keep the flare
    # and the rounded shoulders in the silhouette.
    def radius(z):
        if z < 46:
            # Sides that widen steadily downward, then sweep out into the lip.
            return 18.5 + .12*(46 - z) + (7.5*((36 - z)/23)**2.6 if z < 36 else 0)
        t = min(1, (z - 46)/16.4)
        return 18.5*(1 - t*t)**.5 + .4                  # a round crown
    heights = [13 + i*.5 for i in range(0, 99)]
    circles = [[project((x, y, z)) for x, y in oval(0, 0, radius(z), radius(z), count=64)]
               for z in heights]
    bands = [MultiPoint(lower + upper).convex_hull for lower, upper in zip(circles, circles[1:])]
    silhouette = unary_union(bands)
    clapper = [project((x, y, z)) for radius, z in ((3.4, 1.6), (6, 4.2), (6.4, 6.4), (5.2, 9))
               for x, y in oval(0, 0, radius, radius, count=32)]
    striker = MultiPoint(clapper).convex_hull
    s.layers.append((striker.boundary, striker, EDGE))
    s.disk(0, 0, 61.6, 3.4, 3.4, 4.2)
    s.layers.append((silhouette.boundary, silhouette, EDGE))
    # The lip's rolled edge, on the visible front of the flare.
    s.ellipse(0, 0, 15.6, 27.4, 27.4, DETAIL, -45, 135)


def draw(s):
    notification_bell(s)
    badge(s, "check", *_screen(0, 0, 0, 33, 9), 12.6)
