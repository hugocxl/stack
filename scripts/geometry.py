"""Orthographic line drawing with transparent hidden-line removal."""
from math import cos, sin, radians
from shapely.geometry import LineString, MultiPoint, Polygon
from shapely.ops import unary_union

BOLD = "1"
EDGE = ".76"
DETAIL = ".43"
GUIDE = ".34"


def project(point):
    x, y, z = point
    return ((x-y)*.8660254, (x+y)*.4330127-z*.8660254)


def oval(x, y, rx, ry, start=0, end=360, count=72):
    angles = [radians(start + (end-start)*i/count) for i in range(count+1)]
    return [(x+rx*cos(a), y+ry*sin(a)) for a in angles]


def rounded(x, y, w, d, r):
    r = min(r, w/2, d/2) * .999
    return [
        p for cx, cy, a in [(x+w-r,y+r,-90), (x+w-r,y+d-r,0),
                             (x+r,y+d-r,90), (x+r,y+r,180)]
        for p in oval(cx, cy, r, r, a, a+90, 8)
    ]


class Scene:
    def __init__(self):
        self.layers = []

    def line(self, points, ink=DETAIL, dashed=False):
        if dashed:
            phase = 0
            for a, b in zip(points, points[1:]):
                length = sum((u-v)**2 for u, v in zip(a,b))**.5
                start = -phase
                while start < length:
                    end = min(start+2.4,length)
                    if end > max(start,0):
                        p, q = max(start,0)/length, end/length
                        self.line([tuple(u+(v-u)*t for u,v in zip(a,b)) for t in (p,q)], ink)
                    start += 6
                phase = (phase+length) % 6
            return
        xy = list(map(project, points))
        if len(xy) >= 2:
            self.layers.append((LineString(xy), None, ink))

    def face(self, points, ink=EDGE, *, openings=()):
        polygon = Polygon(
            list(map(project, points)),
            [list(map(project, opening)) for opening in openings],
        )
        if polygon.is_valid and polygon.area > .01:
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
            # Keep only the near portion of the top edge, inset from the silhouette.
            cx = sum(x for x,_ in top)/len(top)
            cy = sum(y for _,y in top)/len(top)
            inset = [(cx+(x-cx)*.965,cy+(y-cy)*.965,z+h-.05) for x,y in top]
            visible = [((b[1]-a[1])-(b[0]-a[0])) > .001 for a,b in zip(top,top[1:]+top[:1])]
            for i, segment in enumerate(visible):
                if segment and not visible[i-1]:
                    chain = [inset[i]]
                    while visible[i % len(top)]:
                        i += 1
                        chain.append(inset[i % len(top)])
                    self.line(chain)

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

    def traced_lines(self):
        covered = Polygon()
        visible = []
        for path, polygon, ink in reversed(self.layers):
            uncovered = path.difference(covered)
            if not uncovered.is_empty:
                visible.append((uncovered, ink))
            if polygon is not None:
                covered = unary_union([covered, polygon.buffer(.13)])
        return reversed(visible)


def segments(geometry):
    if geometry.geom_type in ("LineString","LinearRing"):
        if geometry.length > .5:
            yield geometry.coords
    elif hasattr(geometry,"geoms"):
        for part in geometry.geoms:
            yield from segments(part)


def paths_for(scene):
    strokes = [(list(coords), ink) for path, ink in scene.traced_lines() for coords in segments(path)]
    xs, ys = zip(*(p for stroke,_ in strokes for p in stroke))
    lo_x, hi_x, lo_y, hi_y = min(xs), max(xs), min(ys), max(ys)
    scale = min(310/(hi_x-lo_x), 246/(hi_y-lo_y))
    offset_x, offset_y = 240-(lo_x+hi_x)*scale/2, 180-(lo_y+hi_y)*scale/2
    groups = {ink: [] for ink in (GUIDE, DETAIL, EDGE, BOLD)}
    for coords, ink in strokes:
        points = " ".join(f"{x*scale+offset_x:.2f},{y*scale+offset_y:.2f}" for x,y in coords)
        groups[ink].append("M" + points)
    return '\n'.join(
        f'  <path vector-effect="non-scaling-stroke" stroke-opacity="{ink}" d="{" ".join(paths)}"/>'
        for ink, paths in groups.items() if paths
    )
