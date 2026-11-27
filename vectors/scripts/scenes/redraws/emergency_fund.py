from shapely.geometry import MultiPoint
from shapely.ops import unary_union

from geometry import DETAIL, EDGE, oval, project
from scenes.redraws._kit import warning
from scenes.redraws._sf import smooth

DESCRIPTION = "A round piggy bank with a coin slot on its back carries a warning triangle."


def draw(s):
    # Legs first, so the body hides where they meet it.
    for x, y in ((-20, -10), (-20, 12), (20, -10), (20, 12)):
        s.disk(x, y, 0, 5, 5, 12)
    # Body: rings across the long (x) axis, radius following an egg profile.
    profile = smooth([(-36, 2), (-30, 16), (-14, 24), (8, 25), (26, 20), (36, 10), (38, 2)], 5)
    rings = [[project((x, r*a, 32 + r*.92*b)) for a, b in oval(0, 0, 1, 1, count=48)] for x, r in profile]
    body = unary_union([MultiPoint(p + q).convex_hull for p, q in zip(rings, rings[1:])])
    s.layers.append((body.boundary, body, EDGE))
    # Snout: a short cylinder facing +x with two nostrils.
    snout = [(40, a, 30 + b) for a, b in oval(0, 0, 8, 7, count=36)]
    back = [(34, a, 30 + b) for a, b in oval(0, 0, 8, 7, count=36)]
    hull = MultiPoint([project(p) for p in snout + back]).convex_hull
    s.layers.append((hull.boundary, hull, EDGE))
    s.line(snout, EDGE)
    for y in (-3, 3):
        s.line([(40.1, y + a*.0, 30 + b) for a, b in oval(0, 0, 1.4, 1.8, count=12)][:1] +
               [(40.1, y + a, 30 + b) for a, b in oval(0, 0, 1.4, 1.8, count=12)], DETAIL)
    for y in (-12, 10):
        s.face([(18, y - 6, 50), (18, y + 6, 50), (22, y, 60)], EDGE)
    s.line([(-8, -1, 57.5), (10, -1, 57.5)], EDGE)
    s.line([(-8, 1, 57.5), (10, 1, 57.5)], EDGE)
    warning(s, -6, 28, 22, 26)
