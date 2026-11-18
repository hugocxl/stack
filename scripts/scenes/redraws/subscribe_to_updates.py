from shapely.geometry import MultiPoint
from shapely.ops import unary_union

from geometry import EDGE, oval, project
from scenes.redraws._kit import badge

DESCRIPTION = "A plus badge overlaps the shoulder of a notification bell with a flared rim and clapper."


def bell_radius(height):
    """Sample a smooth crown and a skirt that flares into the lip."""
    profile = [(13, 42), (17, 41.5), (22, 38), (30, 33), (41, 30),
               (53, 28), (63, 24), (70, 18), (75, 11), (77, 0)]
    for i, ((lo, a), (hi, b)) in enumerate(zip(profile, profile[1:])):
        if lo <= height <= hi:
            prev_h, prev_r = profile[max(0, i - 1)]
            next_h, next_r = profile[min(i + 2, len(profile) - 1)]
            slope_a = (b - prev_r)/(hi - prev_h) * (hi - lo)
            slope_b = (next_r - a)/(next_h - lo) * (hi - lo)
            t = (height - lo)/(hi - lo)
            return (1 - t)**2 * ((1 + 2*t)*a + t*slope_a) + t*t * ((3 - 2*t)*b + (t - 1)*slope_b)
    return 0


def draw(s):
    s.face([(.5*x, -.5*x, z) for x, z in oval(0, -21, 9.7, 11.2)[:-1]], EDGE)
    # At each latitude, the apparent outline lies on the tangent of the spun shell.
    # A convex ring slice preserves the rounded silhouette at the lip and crown.
    rings = [[project((x, y, z)) for x, y in oval(0, 0, bell_radius(z), bell_radius(z), count=48)]
             for z in range(13, 78)]
    shell = unary_union([MultiPoint(a + b).convex_hull for a, b in zip(rings, rings[1:])])
    s.layers.append((shell.boundary, shell, EDGE))
    s.ellipse(0, 0, 16, 40, 40, EDGE, -45, 135)
    s.disk(0, 0, 77, 6, 6, 5, EDGE)
    badge(s, "plus", 23, -20, 62, 15)
