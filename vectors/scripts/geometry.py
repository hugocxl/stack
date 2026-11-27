"""Orthographic line drawing with transparent hidden-line removal.

The line language follows SF Symbols drawn fine: one hairline weight that stays 1.05 px
at any size, round caps and joins, continuous (squircle) corners, hierarchy by opacity
rather than by weight, short rounded dashes, and a clearance gap wherever one part
passes in front of another. Gaps and dashes are measured in output units of the
480 x 360 canvas, so every figure carries the same rhythm whatever its scene scale.
"""
from math import cos, sin, radians
from shapely.geometry import LineString, MultiPoint, Polygon
from shapely.ops import substring, unary_union
from shapely.validation import explain_validity

# Hierarchical rendering: primary outlines and glyphs, secondary detail, tertiary guides.
BOLD = "1"
EDGE = ".9"
DETAIL = ".55"
GUIDE = ".32"

STROKE_WIDTH = "1.05"  # the single, non-scaling stroke weight of the collection, in px

# Output units on the 480 x 360 canvas.
STROKE = 1.6           # the stroke's width on the canvas at a typical 320 px display
OCCLUSION = .35        # hidden lines stop just short of the solid that hides them
CLEARANCE = 1.9        # extra stroke widths of air around a badge (SF badge knockout)
DASH = 3.5             # dash length before round caps, in stroke widths
DASH_GAP = 7.5         # dash period, in stroke widths
CREASE = 1           # the near top edge of a solid meets its silhouette, as in SF's cube
CANVAS = (480, 360)
ART = (310, 246)       # the artwork's bounding box, centred on the canvas


class Ink(str):
    """An opacity tier with a drawing modifier attached: a dashed line, a knockout mask,
    or a cut that breaks the stroke where another part passes over it."""
    def __new__(cls, value, *, dashed=False, knockout=0, cut=None):
        ink = super().__new__(cls, value)
        ink.dashed, ink.knockout, ink.cut = dashed, knockout, cut
        return ink


def knockout_layer(polygon, gap=CLEARANCE):
    """A mask with no outline that clears `gap` stroke widths around a part in front."""
    return (LineString(), polygon, Ink(EDGE, knockout=gap))


def interlace(scene, rings, crossings, ink=EDGE):
    """Draw rings that pass over and under each other, like the links of SF's link symbol.

    Each ring's outline breaks with SF clearance wherever its crossing mask lies on top.
    """
    scene.layers.append((LineString(), unary_union(rings), ink))
    for ring, crossing in zip(rings, crossings):
        scene.layers.append((ring.boundary, None, Ink(ink, cut=crossing)))


def project(point):
    x, y, z = point
    return ((x-y)*.8660254, (x+y)*.4330127-z*.8660254)


def oval(x, y, rx, ry, start=0, end=360, count=72):
    angles = [radians(start + (end-start)*i/count) for i in range(count+1)]
    return [(x+rx*cos(a), y+ry*sin(a)) for a in angles]


def rounded(x, y, w, d, r):
    """Rectangle with continuous corners, the squircle profile of Apple's icons.

    A corner of nominal radius r starts SMOOTH*r from the vertex and eases into the
    edge with no visible kink. When the corners meet, the shape becomes a capsule.
    """
    half = min(w, d)/2
    if r >= half*.96 or not CONTINUOUS[0]:
        r = half*.999
        return [
            p for cx, cy, a in [(x+w-r,y+r,-90), (x+w-r,y+d-r,0),
                                 (x+r,y+d-r,90), (x+r,y+r,180)]
            for p in oval(cx, cy, r, r, a, a+90, 12)
        ]
    reach = min(r*SMOOTH, half*.999)
    points = []
    corners = [((x+w, y), (1, 0), (0, 1)), ((x+w, y+d), (0, 1), (-1, 0)),
               ((x, y+d), (-1, 0), (0, -1)), ((x, y), (0, -1), (1, 0))]
    for (vx, vy), (ax, ay), (bx, by) in corners:
        # Incoming edge runs along +a toward the vertex, outgoing along +b away from it.
        start = (vx - ax*reach, vy - ay*reach)
        end = (vx + bx*reach, vy + by*reach)
        c1 = (vx - ax*reach*(1-PULL), vy - ay*reach*(1-PULL))
        c2 = (vx + bx*reach*(1-PULL), vy + by*reach*(1-PULL))
        for i in range(13):
            t = i/12
            k = [(1-t)**3, 3*(1-t)**2*t, 3*(1-t)*t**2, t**3]
            points.append(tuple(sum(w_*q[j] for w_, q in zip(k, (start, c1, c2, end))) for j in range(2)))
    return points


CONTINUOUS = [True]   # build.py falls back to circular corners where a scene splices into an arc
SMOOTH = 1.42   # how far a continuous corner reaches along each edge, in radii
PULL = .64      # how close the Bezier handles sit to the vertex (circle is .552)


class Scene:
    def __init__(self):
        self.layers = []

    def line(self, points, ink=DETAIL, dashed=False):
        xy = list(map(project, points))
        if len(xy) >= 2:
            self.layers.append((LineString(xy), None, Ink(ink, dashed=True) if dashed else ink))

    def face(self, points, ink=EDGE, *, openings=()):
        outline = list(map(project, points))
        polygon = Polygon(
            outline,
            [list(map(project, opening)) for opening in openings],
        )
        if not polygon.is_valid and MultiPoint(outline).convex_hull.area > .01:
            raise ValueError(f"Invalid projected face: {explain_validity(polygon)}")
        if polygon.area > .01:
            self.layers.append((polygon.boundary, polygon, ink))

    def tube(self, points, radius, ink=EDGE):
        """Draw a constant-radius rod or cable from its projected centerline."""
        centerline = LineString(list(map(project, points)))
        polygon = centerline.buffer(radius, quad_segs=12)
        self.layers.append((polygon.boundary, polygon, ink))

    def solid(self, foot, z, h, top=None, ink=EDGE, crease=True):
        top = top if top is not None else foot
        projected = [project((x,y,v)) for ring,v in [(foot,z),(top,z+h)] for x,y in ring]
        hull = MultiPoint(projected).convex_hull
        self.layers.append((hull.boundary, hull, ink))
        if crease and h > 2:
            # Keep only the near portion of the top edge; it runs into the silhouette.
            cx = sum(x for x,_ in top)/len(top)
            cy = sum(y for _,y in top)/len(top)
            inset = [(cx+(x-cx)*CREASE,cy+(y-cy)*CREASE,z+h) for x,y in top]
            visible = [((b[1]-a[1])-(b[0]-a[0])) > .001 for a,b in zip(top,top[1:]+top[:1])]
            for i, segment in enumerate(visible):
                if segment and not visible[i-1]:
                    chain = [inset[i]]
                    while visible[i % len(top)]:
                        i += 1
                        chain.append(inset[i % len(top)])
                    self.line(chain, ink)

    def box(self, x, y, z, w, d, h, r=3, ink=EDGE):
        self.solid(rounded(x,y,w,d,r), z, h, ink=ink)

    def disk(self, x, y, z, rx, ry, h, ink=EDGE):
        self.solid(oval(x,y,rx,ry)[:-1], z, h, ink=ink)

    def ellipse(self, x, y, z, rx, ry, ink=DETAIL, start=0, end=360):
        self.line([(a,b,z) for a,b in oval(x,y,rx,ry,start,end)], ink)

    def ring(self, x, y, z, rx, ry, h, wall=4, ink=EDGE):
        outer = oval(x,y,rx,ry)[:-1]
        inner = oval(x,y,rx-wall,ry-wall)[:-1]
        points = [project((a,b,k)) for k in (z,z+h) for a,b in outer]
        hull = MultiPoint(points).convex_hull
        opening = Polygon([project((a,b,z+h)) for a,b in inner])
        bottom = Polygon([project((a,b,z)) for a,b in inner])
        hole = opening.intersection(bottom)
        self.layers.append((hull.boundary, hull.difference(hole), ink))
        self.ellipse(x,y,z+h,rx-wall,ry-wall)
        self.layers.append((hole.boundary, None, GUIDE))

    def dots(self, x, y, z, nx=4, ny=4, gap=4, ink=DETAIL):
        for i in range(nx):
            for j in range(ny):
                a, b = x+i*gap, y+j*gap
                self.line([(a,b,z),(a+1.5,b,z)], ink)

    def traced_lines(self, scale=2.0):
        """Visible strokes, front to back. `scale` converts output units to scene units."""
        covered = Polygon()
        visible = []
        for path, polygon, ink in reversed(self.layers):
            if getattr(ink, "cut", None) is not None:
                path = path.difference(ink.cut.buffer((OCCLUSION + CLEARANCE*STROKE)/scale, quad_segs=12))
            if not path.is_empty:
                uncovered = path.difference(covered)
                if not uncovered.is_empty:
                    visible.append((uncovered, ink))
            if polygon is not None and not polygon.is_empty:
                gap = OCCLUSION + getattr(ink, "knockout", 0)*STROKE
                covered = unary_union([covered, polygon.buffer(gap/scale, quad_segs=12)])
        return reversed(visible)

    def extent(self):
        geometry = unary_union([p for p, _, _ in self.layers if not p.is_empty] +
                               [m for _, m, _ in self.layers if m is not None and not m.is_empty])
        return geometry.bounds


def segments(geometry):
    if geometry.geom_type in ("LineString","LinearRing"):
        if geometry.length > .5:
            yield geometry.coords
    elif hasattr(geometry,"geoms"):
        for part in geometry.geoms:
            yield from segments(part)


def dashes(coords, scale):
    """Split a visible run into short round-capped dashes measured in output units."""
    line = LineString(coords)
    on, period = DASH*STROKE/scale, DASH_GAP*STROKE/scale
    count = max(1, round((line.length + period - on)/period))
    period = (line.length - on)/(count - 1) if count > 1 else period
    for i in range(count):
        start = i*period
        piece = substring(line, start, min(start + on, line.length))
        if piece.geom_type == "LineString" and piece.length > 0:
            yield list(piece.coords)


def fit(strokes):
    xs, ys = zip(*(p for stroke, _ in strokes for p in stroke))
    lo_x, hi_x, lo_y, hi_y = min(xs), max(xs), min(ys), max(ys)
    scale = min(ART[0]/(hi_x-lo_x), ART[1]/(hi_y-lo_y))
    return scale, CANVAS[0]/2-(lo_x+hi_x)*scale/2, CANVAS[1]/2-(lo_y+hi_y)*scale/2


def _key(point):
    return tuple(map(float, point.split(",")))


def canonical(points):
    """Print the same outline the same way: rings start at their smallest vertex and every
    run takes the direction that sorts first."""
    if len(points) > 3 and points[0] == points[-1]:
        options = []
        for ring in (points[:-1], points[-2::-1]):
            start = min(range(len(ring)), key=lambda i: _key(ring[i]))
            options.append(ring[start:] + ring[:start] + ring[start:start + 1])
    else:
        options = [points, points[::-1]]
    return min(options, key=lambda run: [_key(p) for p in run])


def merged(runs):
    """Join runs that meet end to end where exactly two run ends share a point.

    GEOS may split one outline into two runs at an arbitrary vertex on one CPU and not on
    another; joining them makes the printed paths independent of where that split fell."""
    runs = [list(run) for run in runs]
    while True:
        ends = {}
        for i, run in enumerate(runs):
            if run[0] != run[-1]:
                for side in (0, -1):
                    ends.setdefault(run[side], []).append((i, side))
        pair = next((v for v in sorted(ends.items()) if len(v[1]) == 2 and v[1][0][0] != v[1][1][0]), None)
        if pair is None:
            return runs
        (i, si), (j, sj) = pair[1]
        a = runs[i] if si == -1 else runs[i][::-1]
        b = runs[j] if sj == 0 else runs[j][::-1]
        runs = [run for k, run in enumerate(runs) if k not in (i, j)] + [a + b[1:]]


def paths_for(scene):
    lo_x, lo_y, hi_x, hi_y = scene.extent()
    scale = min(ART[0]/(hi_x-lo_x), ART[1]/(hi_y-lo_y))
    for _ in range(2):
        # Gaps are set in output units, so trace at the scale the artwork will be drawn.
        traced = list(scene.traced_lines(scale))
        strokes = [(list(coords), ink) for path, ink in traced for coords in segments(path)]
        estimate = scale
        scale, offset_x, offset_y = fit(strokes)
        if abs(scale - estimate) < estimate*.01:
            break
    groups = {ink: [] for ink in (GUIDE, DETAIL, EDGE, BOLD)}
    solid = {ink: [] for ink in groups}
    for coords, ink in strokes:
        pieces = dashes(coords, scale) if getattr(ink, "dashed", False) else [coords]
        for piece in pieces:
            if len(piece) > 1:
                run = [f"{x*scale+offset_x:.2f},{y*scale+offset_y:.2f}" for x, y in piece]
                # Rounding can fold a near-duplicate vertex onto its neighbour; drop it.
                run = [p for i, p in enumerate(run) if i == 0 or p != run[i - 1]]
                if len(run) < 2:
                    continue
                (groups if getattr(ink, "dashed", False) else solid)[ink].append(run)
    for ink, runs in solid.items():
        groups[ink].extend(merged(runs))
    groups = {ink: ["M" + " ".join(canonical(run)) for run in runs] for ink, runs in groups.items()}
    # GEOS may start a ring at a different vertex, or list rings in a different order, on
    # another CPU; canonical rings in sorted order keep the built SVGs identical everywhere.
    return '\n'.join(
        f'  <path vector-effect="non-scaling-stroke" stroke-opacity="{ink}" d="{" ".join(sorted(paths))}"/>'
        for ink, paths in groups.items() if paths
    )
