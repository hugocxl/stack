"""Shared state modifiers for redraws, so every figure speaks the same visual vocabulary.

A badge is a coin that faces the viewer with one upright glyph on it, like an SF Symbols
badge. Draw it last so it sits in front of the object it qualifies.
"""
from math import cos, radians, sin

from shapely.geometry import MultiPoint

from geometry import BOLD, DETAIL, EDGE, knockout_layer, project

GLYPHS = ("check", "x", "plus", "minus", "clock", "exclaim", "arrow", "back", "down", "up", "slash", "pause", "dot",
          "bolt", "refresh", "lock", "unlock", "heart", "star", "play", "moon", "wifi")


def _ring(x, y, z, r, count=48):
    return [(x + r*cos(radians(360*i/count)), y, z + r*sin(radians(360*i/count))) for i in range(count)]


def coin(s, x, y, z, r, depth=2.4, ink=EDGE):
    """An upright disc in the x-z plane. Returns the y of its visible face."""
    back, front = _ring(x, y - depth, z, r), _ring(x, y, z, r)
    hull = MultiPoint([project(p) for p in back + front]).convex_hull
    s.layers.append(knockout_layer(hull))
    s.layers.append((hull.boundary, hull, ink))
    s.line(front + front[:1], ink)
    return y


def _strokes(kind, g):
    """Glyph strokes in a unit frame: u to the right, v up, scaled by g."""
    ring = lambda r, a0=0, a1=360, n=24: [(r*cos(radians(a0 + (a1-a0)*i/n)), r*sin(radians(a0 + (a1-a0)*i/n))) for i in range(n+1)]
    shackle = [(u, v + .35) for u, v in ring(.3, 0, 180, 12)]
    shapes = {
        "check": [[(-.72, .02), (-.22, -.5), (.75, .55)]],
        "x": [[(-.62, -.62), (.62, .62)], [(-.62, .62), (.62, -.62)]],
        "plus": [[(-.75, 0), (.75, 0)], [(0, -.75), (0, .75)]],
        "minus": [[(-.75, 0), (.75, 0)]],
        "clock": [[(0, .72), (0, 0), (.5, -.3)]],
        "exclaim": [[(0, .8), (0, -.25)], [(0, -.62), (0, -.72)]],
        "arrow": [[(-.75, 0), (.75, 0)], [(.3, .45), (.75, 0), (.3, -.45)]],
        "back": [[(.75, 0), (-.75, 0)], [(-.3, .45), (-.75, 0), (-.3, -.45)]],
        "down": [[(0, .75), (0, -.75)], [(-.45, -.3), (0, -.75), (.45, -.3)]],
        "up": [[(0, -.75), (0, .75)], [(-.45, .3), (0, .75), (.45, .3)]],
        "slash": [[(-.68, -.68), (.68, .68)]],
        "pause": [[(-.28, -.6), (-.28, .6)], [(.28, -.6), (.28, .6)]],
        "dot": [ring(.22)],
        "bolt": [[(.12, .82), (-.42, -.05), (.05, -.05), (-.12, -.82), (.42, .05), (-.05, .05), (.12, .82)]],
        "refresh": [ring(.62, 120, 400), [(.05, .82), (-.31, .54), (.02, .25)]],
        "lock": [[(-.48, -.62), (.48, -.62), (.48, .08), (-.48, .08), (-.48, -.62)], [(.3, .08), *shackle, (-.3, .08)]],
        "unlock": [[(-.48, -.62), (.48, -.62), (.48, .08), (-.48, .08), (-.48, -.62)], [(.3, .08), *[(u, v + .12) for u, v in shackle]]],
        "heart": [[(16*sin(radians(a))**3/21, (13*cos(radians(a)) - 5*cos(radians(2*a)) - 2*cos(radians(3*a)) - cos(radians(4*a)))/21 + .1) for a in range(0, 361, 10)]],
        "star": [[((.78 if i % 2 == 0 else .32)*cos(radians(90 + 36*i)), (.78 if i % 2 == 0 else .32)*sin(radians(90 + 36*i))) for i in range(11)]],
    }
    shapes["play"] = [[(-.3, -.55), (-.3, .55), (.58, 0), (-.3, -.55)]]
    shapes["moon"] = [[*ring(.68, 60, 300), *[(.34 + .48*cos(radians(a)), .48*sin(radians(a))) for a in range(240, 119, -10)], (.34, .59)]]
    shapes["wifi"] = [[(u, v - .5) for u, v in ring(r, 45, 135, 10)] for r in (.35, .7, 1.05)] + [[(u, v - .5) for u, v in ring(.08)]]
    if kind not in shapes:
        raise ValueError(f"Unknown glyph {kind}; use one of {GLYPHS}")
    return [[(u*g, v*g) for u, v in stroke] for stroke in shapes[kind]]


def glyph(s, kind, x, y, z, r, ink=BOLD):
    """Draw a glyph of radius r on the x-z plane at depth y (for marks printed on a side face)."""
    for stroke in _strokes(kind, r):
        s.line([(x + u, y + .01, z + v) for u, v in stroke], ink)


# Unit vectors spanning the plane that faces the viewer, scaled so they project to one screen unit.
_U = (1/1.7320508, -1/1.7320508, 0)
_V = (-1/2.5980762, -1/2.5980762, 2/2.5980762)


def _screen(x, y, z, u, v, back=0):
    return (x + u*_U[0] + v*_V[0] - back, y + u*_U[1] + v*_V[1] - back, z + u*_U[2] + v*_V[2] - back)


def badge(s, kind, x, y, z, r=12):
    """State badge: a coin that faces the viewer, so its glyph stays upright and undistorted.

    (x, y, z) is the badge centre in scene space; r is its radius in projected units. Draw it last.
    """
    ring = [(r*cos(radians(a)), r*sin(radians(a))) for a in range(0, 360, 8)]
    rim = [_screen(x, y, z, u, v, back=r*.14) for u, v in ring]
    face = [_screen(x, y, z, u, v) for u, v in ring]
    hull = MultiPoint([project(p) for p in rim + face]).convex_hull
    s.layers.append(knockout_layer(hull))
    s.layers.append((hull.boundary, hull, EDGE))
    s.line(face + face[:1], EDGE)
    for stroke in _strokes(kind, r*.62):
        s.line([_screen(x, y, z, u, v, back=-.01) for u, v in stroke], BOLD)


def _soft_triangle(x, y, z, size, r):
    """Upright triangle with rounded corners, as in SF's exclamationmark.triangle."""
    h = size*.87
    corners = [(x - size/2, z), (x + size/2, z), (x, z + h)]
    points = []
    for i, (cu, cv) in enumerate(corners):
        (pu, pv), (nu, nv) = corners[i-1], corners[(i+1) % 3]
        a = ((pu-cu), (pv-cv)); b = ((nu-cu), (nv-cv))
        la, lb = (a[0]**2 + a[1]**2)**.5, (b[0]**2 + b[1]**2)**.5
        a, b = (a[0]/la, a[1]/la), (b[0]/lb, b[1]/lb)
        start, end = (cu + a[0]*r, cv + a[1]*r), (cu + b[0]*r, cv + b[1]*r)
        for k in range(9):
            t = k/8
            points.append(((1-t)**2*start[0] + 2*(1-t)*t*cu + t**2*end[0],
                           (1-t)**2*start[1] + 2*(1-t)*t*cv + t**2*end[1]))
    return [(u, y, v) for u, v in points]


def warning(s, x, y, z, size=26):
    """Upright warning triangle with an exclamation mark, facing the viewer's lower left."""
    h = size*.87
    tri = _soft_triangle(x, y, z, size, size*.16)
    back = [(a, b - 2.4, c) for a, b, c in tri]
    hull = MultiPoint([project(p) for p in back + tri]).convex_hull
    s.layers.append(knockout_layer(hull))
    s.layers.append((hull.boundary, hull, EDGE))
    s.line(tri + tri[:1], EDGE)
    s.line([(x, y + .01, z + h*.66), (x, y + .01, z + h*.4)], BOLD)
    s.line([(x, y + .01, z + h*.2), (x, y + .01, z + h*.19)], BOLD)


def arrow(s, points, ink=EDGE, head=5):
    """A flat path arrow on the ground or any plane, ending in an open chevron at the last point."""
    s.line(points, ink)
    (ax, ay, az), (bx, by, bz) = points[-2], points[-1]
    length = ((bx-ax)**2 + (by-ay)**2 + (bz-az)**2) ** .5
    ux, uy, uz = (bx-ax)/length, (by-ay)/length, (bz-az)/length
    # Perpendicular within the ground plane unless the segment is vertical.
    px, py, pz = (-uy, ux, 0) if abs(uz) < .9 else (1, 0, 0)
    # SF arrows end in a right-angled chevron: each leg leaves the tip at 45 degrees.
    leg = head*.8
    s.line([(bx - leg*ux + leg*px, by - leg*uy + leg*py, bz - leg*uz + leg*pz),
            (bx, by, bz),
            (bx - leg*ux - leg*px, by - leg*uy - leg*py, bz - leg*uz - leg*pz)], ink)


__all__ = ["BOLD", "DETAIL", "EDGE", "GLYPHS", "arrow", "badge", "coin", "glyph", "warning"]
