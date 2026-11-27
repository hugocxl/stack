"""Solid primitives for SF-grade redraws: extruded plates, turned solids and smooth profiles.

SF Symbols draw objects as a few confident volumes: a plate with a visible thickness, a
turned body with a smooth silhouette, a capsule. These helpers build those volumes in
scene space so a figure reads as one designed object rather than a stack of props.
"""
from math import cos, radians, sin

from shapely.geometry import MultiPoint, Polygon
from shapely.ops import unary_union

from geometry import DETAIL, EDGE, oval, project, rounded


def smooth(points, steps=6, closed=False):
    """Catmull-Rom through 2-D or 3-D points, so profiles have no visible facets."""
    pts = list(points)
    padded = [pts[-1], *pts, pts[0], pts[1]] if closed else [pts[0], *pts, pts[-1]]
    out = []
    for i in range(1, len(padded) - 2):
        p0, p1, p2, p3 = padded[i-1:i+3]
        for k in range(steps):
            t = k/steps
            out.append(tuple(.5*(2*b + (-a + c)*t + (2*a - 5*b + 4*c - d)*t*t + (-a + 3*b - 3*c + d)*t**3)
                             for a, b, c, d in zip(p0, p1, p2, p3)))
    return out if closed else out + [pts[-1]]


def plane(origin, across, up):
    """Map 2-D artwork (u right, v up) onto a plane in scene space."""
    ox, oy, oz = origin

    def at(u, v, w=0, normal=(0, 0, 0)):
        return (ox + u*across[0] + v*up[0] + w*normal[0],
                oy + u*across[1] + v*up[1] + w*normal[1],
                oz + u*across[2] + v*up[2] + w*normal[2])
    return at


# Planes that face the viewer's lower left (+y) and lower right (+x), and the ground.
def left_face(x=0, y=0, z=0):
    return plane((x, y, z), (1, 0, 0), (0, 0, 1))


def right_face(x=0, y=0, z=0):
    return plane((x, y, z), (0, -1, 0), (0, 0, 1))


def ground(x=0, y=0, z=0):
    return plane((x, y, z), (1, 0, 0), (0, 1, 0))


def plate(s, at, outline, depth, back, ink=EDGE, rim=True):
    """Extrude a 2-D outline on plane `at` by `depth` along the scene vector `back`.

    The silhouette is the hull of every side quad, so concave outlines keep their shape;
    the front outline is drawn so the face reads as a crisp edge, as in SF's cube.
    Returns a function mapping (u, v) to the front face.
    """
    front = [at(u, v) for u, v in outline]
    rear = [(x + back[0]*depth, y + back[1]*depth, z + back[2]*depth) for x, y, z in front]
    fp = [project(p) for p in front]
    rp = [project(p) for p in rear]
    parts = [Polygon(fp), Polygon(rp)]
    for i in range(len(fp)):
        quad = Polygon([fp[i-1], fp[i], rp[i], rp[i-1]])
        if quad.is_valid and quad.area > 1e-4:
            parts.append(quad)
    body = unary_union([p if p.is_valid else p.buffer(0) for p in parts])
    s.layers.append((body.boundary, body, ink))
    if rim:
        s.line(front + front[:1], ink)
    return lambda u, v: at(u, v)


def turned(s, profile, x=0, y=0, z=0, ink=EDGE, count=72, steps=6):
    """A solid of revolution about the vertical axis; profile is [(radius, height)]."""
    rings = [[project((x + px, y + py, z + h)) for px, py in oval(0, 0, max(r, .01), max(r, .01), count=count)]
             for r, h in smooth(profile, steps)]
    body = unary_union([MultiPoint(a + b).convex_hull for a, b in zip(rings, rings[1:])])
    s.layers.append((body.boundary, body, ink))
    return body


def lip(s, x, y, z, r, ink=DETAIL, start=-45, end=135):
    """The visible front arc of a horizontal rim."""
    s.line([(x + a, y + b, z) for a, b in oval(0, 0, r, r, start, end)], ink)


def capsule(w, h):
    return rounded(0, 0, w, h, min(w, h)/2)


def squircle(w, h, r):
    return rounded(0, 0, w, h, r)


def arc(cx, cy, r, a0, a1, n=24):
    return [(cx + r*cos(radians(a0 + (a1 - a0)*i/n)), cy + r*sin(radians(a0 + (a1 - a0)*i/n))) for i in range(n + 1)]


__all__ = ["DETAIL", "EDGE", "arc", "capsule", "ground", "left_face", "lip", "plane", "plate", "right_face",
           "smooth", "squircle", "turned"]


def screen(x=0, y=0, z=0):
    """The plane that faces the viewer, so artwork on it stays upright and undistorted."""
    from scenes.redraws._kit import _U, _V
    return plane((x, y, z), _U, _V)


BACK = (0, -1, 0)   # thickness of a viewer-facing plate shows toward the upper right


def person(s, at, u, v, size, ink=EDGE):
    """The SF person glyph: a round head over rounded shoulders."""
    s.line([at(u + a, v + size*.28 + b) for a, b in oval(0, 0, size*.24, size*.24, count=40)], ink)
    s.line([at(u + a, v + b) for a, b in [*arc(0, -size*.52, size*.46, 168, 12, 24)]], ink)


def chevron_arrow(length, shaft, head):
    """Outline of a bold arrow pointing right, from its tail at the origin."""
    h = head
    return [(0, -shaft/2), (length - h, -shaft/2), (length - h, -h*.9), (length, 0),
            (length - h, h*.9), (length - h, shaft/2), (0, shaft/2)]


def doorway(s, w=56, h=88, t=8, depth=8):
    """A door frame standing on the floor, its opening facing the viewer's lower left."""
    frame = left_face(0, 0, 0)
    portal = [(-t, 0), (0, 0), (0, h), (w, h), (w, 0), (w + t, 0), (w + t, h + t), (-t, h + t)]
    plate(s, frame, portal, depth, (0, -1, 0))


def padlock(s, x=0, y=0, z=0, w=50, h=40, depth=14, shackle=None, open_=False, keyhole=True):
    """An SF padlock: a rounded body with a keyhole and a thick round shackle."""
    from geometry import BOLD
    r = shackle or w*.3
    lift = 12 if open_ else 0
    # The shackle stands in the body's mid-plane; draw it first so the body hides its feet.
    mid = (x + w/2, y - depth/2, z + h)
    pts = [(mid[0] - r, mid[1], mid[2] - 4)] if not open_ else []
    pts = [(mid[0] - r, mid[1], mid[2] - 4 + (lift if open_ else 0))]
    for i in range(0, 181, 10):
        a = radians(180 - i)
        pts.append((mid[0] + r*cos(a), mid[1], mid[2] + lift + r*.25 + r*sin(a)*1.05))
    pts.append((mid[0] + r, mid[1], mid[2] - 4 + lift))
    s.tube(pts, w*.075, EDGE)
    body = left_face(x, y, z)
    plate(s, body, squircle(w, h, 8), depth, (0, -1, 0))
    if keyhole:
        s.line([body(w/2 + a, h*.56 + b) for a, b in oval(0, 0, 4, 4, count=32)], BOLD)
        s.line([body(w/2, h*.48), body(w/2, h*.3)], BOLD)
    return body


def display(s, w=104, h=66, x=0, y=0, z=0, stand=True, depth=6):
    """A thin display on a round-footed stand; returns the front face mapping, origin lower left."""
    if stand:
        turned(s, [(18, 0), (18, 3), (16, 4)], x + w/2, y - depth/2, z, steps=2)
        s.tube([(x + w/2, y - depth/2 - 2, z + 4), (x + w/2, y - depth/2 - 2, z + 22)], 3.2, EDGE)
    lift = 20 if stand else 0
    face = left_face(x, y, z + lift)
    plate(s, face, squircle(w, h, 6), depth, (0, -1, 0))
    inner = [face(u + 5, v + 5) for u, v in squircle(w - 10, h - 10, 3)]
    s.line(inner + inner[:1], DETAIL)
    return lambda u, v: face(u, v)


def bubble(w, h, r=None, tail=(.22, 12, 10)):
    """A speech-bubble outline with a tail at its lower left, origin at the lower left."""
    r = r or min(w, h)*.3
    body = squircle(w, h, r)
    at, tw, th = tail
    x0 = w*at
    # Splice the tail into the bottom edge.
    out = []
    for i, (u, v) in enumerate(body):
        out.append((u, v))
    bottom = [i for i, (u, v) in enumerate(out) if abs(v) < 1e-6]
    # Bottom edge runs right-to-left in rounded(): insert after the point nearest x0 + tw.
    k = min(range(len(out)), key=lambda i: (abs(out[i][1]) > .5, abs(out[i][0] - (x0 + tw))))
    return out[:k+1] + [(x0 + tw, 0), (x0 - 2, -th), (x0, 0)] + out[k+1:]


def gear(r, teeth=10, depth=None):
    """A gear outline with flat-topped teeth, centred on the origin."""
    depth = depth or r*.2
    pts = []
    step = 360/teeth
    for i in range(teeth):
        a = i*step
        for da, rr in ((-.30, r - depth), (-.18, r), (.18, r), (.30, r - depth)):
            pts.append((rr*cos(radians(a + da*step)), rr*sin(radians(a + da*step))))
        for k in (1, 2):
            t = a + (.30 + .4*k/3)*step
            pts.append(((r - depth)*cos(radians(t)), (r - depth)*sin(radians(t))))
    return pts


def puzzle(size, knobs=(True, False, False, False)):
    """A jigsaw piece: square with a round knob on the right edge (others flat)."""
    s_ = size
    k = s_*.17
    pts = [(0, 0), (s_, 0), (s_, s_*.32)]
    if knobs[0]:
        pts += [(s_ + k*.4 + k*cos(radians(a))*1.05, s_/2 + k*sin(radians(a))*1.05) for a in range(-130, 131, 15)]
    pts += [(s_, s_*.68), (s_, s_), (0, s_)]
    return pts


def house(s, x=0, y=0, z=0, w=60, d=50, h=34, roof=26, overhang=4):
    """A gabled house with its ridge along x; returns the front (+y) wall mapping (u along x, v up)."""
    s.box(x, y, z, w, d, h, 1.5)
    o, top, mid = overhang, z + h + roof, y + d/2
    slope = roof/(d/2)
    eave = z + h - o*slope*.5
    s.face([(x, mid, top), (x + w, mid, top), (x + w, y - o, eave), (x, y - o, eave)], EDGE)
    s.face([(x + w, y, z + h), (x + w, y + d, z + h), (x + w, mid, top)], EDGE)
    s.face([(x, mid, top), (x + w, mid, top), (x + w, y + d + o, eave), (x, y + d + o, eave)], EDGE)
    return left_face(x, y + d, z)


def map_pin(s, x, y, z, r=16, ink=EDGE):
    """A viewer-facing map pin with thickness, its tip at (x, y, z)."""
    at = screen(x, y, z)
    pts = [(0, 0)]
    for a in range(-35, 216, 8):
        pts.append((r*cos(radians(a)), r*2.1 + r*sin(radians(a))))
    plate(s, at, pts, r*.3, BACK, ink)
    s.line([at(u, v) for u, v in oval(0, r*2.1, r*.42, r*.42, count=32)], ink)
    return at


def headset(s, mic=True, R=34, cz=24):
    """SF headphones in profile: a padded band over two thick earcups, with a boom mic."""
    band = [(R*cos(radians(a)), 0, cz + R*1.08*sin(radians(a))) for a in range(0, 181, 5)]
    left_cup = right_face(-R - 4, 8, cz - 22)
    plate(s, left_cup, squircle(16, 30, 8), 9, (1, 0, 0))
    s.tube(band, 3.6, EDGE)
    if mic:
        boom = smooth([(-R + 2, 2, cz - 10), (-R + 6, 14, cz - 22), (-R + 18, 22, cz - 28), (-R + 30, 24, cz - 28)], 6)
        s.tube(boom, 1.6, EDGE)
        s.tube([boom[-1], (boom[-1][0] + 7, boom[-1][1], boom[-1][2])], 3.2, EDGE)
    right_cup = right_face(R + 4, 8, cz - 22)
    plate(s, right_cup, squircle(16, 30, 8), 9, (-1, 0, 0))
    inner = [right_cup(u + 4, v + 5) for u, v in squircle(8, 20, 4)]
    s.line(inner + inner[:1], DETAIL)


class Face2D:
    """Adapter so 2-D glyph helpers that call face.line([(u, v), ...]) can print on any plane."""
    def __init__(self, s, at):
        self.s, self.at = s, at

    def line(self, points, ink=DETAIL, dashed=False):
        self.s.line([self.at(u, v) for u, v in points], ink, dashed)


def coin_face(s, at, r, depth=None, mark="$"):
    """A viewer-facing coin with a rim and a printed currency sign."""
    from geometry import BOLD
    plate(s, at, oval(0, 0, r, r, count=72)[:-1], depth or r*.22, BACK)
    s.line([at(u, v) for u, v in oval(0, 0, r*.8, r*.8, count=72)], DETAIL)
    currency(s, at, r*.42, BOLD, mark)


def currency(s, at, size, ink, mark="$"):
    if mark == "$":
        sv = smooth([(.55, .5), (.2, .75), (-.35, .62), (-.5, .3), (-.2, .05), (.3, -.08), (.55, -.38), (.3, -.7), (-.25, -.75), (-.6, -.5)], 5)
        s.line([at(u*size, v*size) for u, v in sv], ink)
        s.line([at(0, -1.05*size), at(0, 1.05*size)], ink)
    elif mark == "€":
        s.line([at(.55*size*cos(radians(a)) + .1*size, .75*size*sin(radians(a))) for a in range(40, 321, 15)], ink)
        for v in (.15, -.15):
            s.line([at(-.75*size, v*size), at(.15*size, v*size)], ink)


def coin_stack(s, x, y, z, r, count, h=4.2):
    for i in range(count):
        s.disk(x, y, z + i*h, r, r, h)
    top = z + count*h
    s.ellipse(x, y, top, r*.72, r*.72, DETAIL)
    return top


def tree(s, x, y, z, h=46, r=18, trunk=2.6):
    """An SF tree: a straight trunk under a full rounded crown."""
    s.tube([(x, y, z), (x, y, z + h*.55)], trunk, EDGE)
    turned(s, [(.4, h*.38), (r*.8, h*.44), (r, h*.62), (r*.92, h*.8), (r*.55, h*.95), (.4, h)], x, y, z, steps=4)


def payment_card(s, x=-43, y=0, z=0, w=86, h=54):
    """A standing payment card with a chip and a number line."""
    face = left_face(x, y, z)
    plate(s, face, squircle(w, h, 6), 3, (0, -1, 0))
    chip = [face(10 + u, 24 + v) for u, v in squircle(14, 11, 2.5)]
    s.line(chip + chip[:1], EDGE)
    s.line([face(10, 12), face(46, 12)], DETAIL)
    s.line([face(52, 12), face(64, 12)], DETAIL)
    return face


def bolt(s, at, size, ink=None):
    from geometry import BOLD
    pts = [(.15, 1), (-.5, -.08), (-.02, -.08), (-.15, -1), (.5, .12), (.02, .12), (.15, 1)]
    s.line([at(u*size, v*size) for u, v in pts], ink or BOLD)


def carton(s, x=0, y=0, z=0, w=60, d=44, h=40, tape=True):
    """A closed shipping carton with a centre tape strip; returns its front (+y) face."""
    s.box(x, y, z, w, d, h, 1.5)
    if tape:
        for k in (-4, 4):
            s.line([(x + w/2 + k, y, z + h), (x + w/2 + k, y + d, z + h), (x + w/2 + k, y + d, z + h - 10)], DETAIL)
    return left_face(x, y + d, z)


def open_carton(s, x=0, y=0, z=0, w=64, d=46, h=36, flap=.55):
    """An open carton: back walls, contents slot, then front walls and four splayed flaps.

    Returns a callback to draw the front; call it after drawing the contents."""
    s.face([(x, y, z), (x + w, y, z), (x + w, y, z + h), (x, y, z + h)], EDGE)
    s.face([(x, y, z), (x, y + d, z), (x, y + d, z + h), (x, y, z + h)], EDGE)
    s.face([(x, y, z + h), (x + w, y, z + h), (x + w, y - d*flap*.7, z + h + d*flap*.7), (x, y - d*flap*.7, z + h + d*flap*.7)], EDGE)
    s.face([(x, y, z + h), (x, y + d, z + h), (x - w*flap*.5, y + d, z + h + w*flap*.4), (x - w*flap*.5, y, z + h + w*flap*.4)], EDGE)

    def front():
        s.face([(x + w, y, z), (x + w, y + d, z), (x + w, y + d, z + h), (x + w, y, z + h)], EDGE)
        s.face([(x, y + d, z), (x + w, y + d, z), (x + w, y + d, z + h), (x, y + d, z + h)], EDGE)
        s.face([(x + w, y, z + h), (x + w, y + d, z + h), (x + w + w*flap*.5, y + d, z + h - w*flap*.25), (x + w + w*flap*.5, y, z + h - w*flap*.25)], EDGE)
        s.face([(x, y + d, z + h), (x + w, y + d, z + h), (x + w, y + d + d*flap*.6, z + h - d*flap*.3), (x, y + d + d*flap*.6, z + h - d*flap*.3)], EDGE)
    return front


def shirt(s, x=0, y=0, z=0, size=1.0):
    """A T-shirt standing like a flat garment on display; returns its face mapping."""
    k = size
    outline = [(14, 0), (46, 0), (46, 44), (56, 38), (62, 50), (46, 62), (38, 62), (35, 58), (25, 58), (22, 62),
               (14, 62), (-2, 50), (4, 38), (14, 44)]
    face = left_face(x, y, z)
    at = lambda u, v: face(u*k, v*k)
    plate(s, at, outline, 3, (0, -1, 0))
    s.line([at(u, v) for u, v in smooth([(25, 58), (30, 54), (35, 58)], 4)], DETAIL)
    return at


def cart(s, x=0, y=0, z=0):
    """A shopping cart: open tapered basket, push handle, chassis and four wheels."""
    corners = [(x + 6, y + 8), (x + 56, y + 8), (x + 56, y + 34), (x + 6, y + 34)]
    for cx, cy in corners:
        s.disk(cx, cy, z, 4.5, 4.5, 3)
    s.tube([(cx, cy, z + 7) for cx, cy in corners + corners[:1]], 1.3, EDGE)
    for cx, cy in corners:
        s.tube([(cx, cy, z + 3), (cx, cy, z + 24)], 1.3, EDGE)
    top = [(x - 4, y), (x + 66, y), (x + 66, y + 42), (x - 4, y + 42)]
    foot = [(x + 4, y + 6), (x + 58, y + 6), (x + 58, y + 36), (x + 4, y + 36)]
    Z0, Z1 = z + 24, z + 54
    P = lambda a, b, h: (a, b, h)
    s.face([P(*top[0], Z1), P(*top[1], Z1), P(*foot[1], Z0), P(*foot[0], Z0)], EDGE)
    s.face([P(*top[0], Z1), P(*top[3], Z1), P(*foot[3], Z0), P(*foot[0], Z0)], EDGE)

    def front():
        s.face([P(*top[1], Z1), P(*top[2], Z1), P(*foot[2], Z0), P(*foot[1], Z0)], EDGE)
        s.face([P(*top[3], Z1), P(*top[2], Z1), P(*foot[2], Z0), P(*foot[3], Z0)], EDGE)
        for t in (.33, .66):
            a = [top[3][0] + (top[2][0] - top[3][0])*t, top[3][1]]
            b = [foot[3][0] + (foot[2][0] - foot[3][0])*t, foot[3][1]]
            s.line([P(*a, Z1), P(*b, Z0)], DETAIL)
        s.line([P(top[3][0] + 2, top[3][1], Z1 - 12), P(top[2][0] - 2, top[2][1], Z1 - 12)], DETAIL)
        s.tube([(x - 4, y, Z1), (x - 14, y, Z1 + 8), (x - 14, y + 42, Z1 + 8), (x - 4, y + 42, Z1)], 1.6, EDGE)
    return front


def turbine(s, x=0, y=0, z=0, h=90, blade=34):
    """A wind turbine: tapered tower, nacelle and three blades facing the viewer."""
    s.tube([(x, y, z), (x, y, z + h)], 2.4, EDGE)
    s.box(x - 5, y - 9, z + h - 4, 10, 14, 8, 3)
    hub = screen(x, y + 6, z + h)
    for a in (90, 210, 330):
        c, q = cos(radians(a)), sin(radians(a))
        blade_pts = [(c*3 - q*2.2, q*3 + c*2.2), (c*blade*.35 - q*4, q*blade*.35 + c*4), (c*blade, q*blade), (c*3 + q*2.2, q*3 - c*2.2)]
        s.face([hub(u, v) for u, v in smooth(blade_pts, 3, closed=True)], EDGE)
    s.face([hub(u, v) for u, v in oval(0, 0, 4, 4, count=20)[:-1]], EDGE)


def vase(s, x=0, y=0, z=0, k=1.0):
    """A turned museum vase: foot, full belly, narrow neck and flared lip."""
    prof = [(10, 0), (10, 2), (8, 4), (16, 12), (22, 24), (21, 36), (14, 46), (8, 52), (8, 58), (12, 62), (12, 64)]
    turned(s, [(r*k, h*k) for r, h in prof], x, y, z, steps=4)
    lip(s, x, y, z + 64*k, 9.5*k, DETAIL, -180, 180)


def question(s, at, size, ink=None):
    from geometry import BOLD
    pts = [(-.45, .5), (-.3, .82), (0, .95), (.32, .85), (.45, .55), (.3, .25), (0, .05), (0, -.3)]
    s.line([at(u*size, v*size) for u, v in smooth(pts, 4)], ink or BOLD)
    s.line([at(0, -.62*size), at(0, -.66*size)], ink or BOLD)
