from math import cos, radians, sin

from shapely.geometry import LineString, MultiPoint, Polygon
from shapely.ops import unary_union

from geometry import BOLD, DETAIL, EDGE, oval, project, rounded, segments
from scenes.redraws._kit import _strokes, arrow
from scenes.redraws._w2 import face_magnifier, funnel as nav_funnel


def upright(s, outline, y, depth, ink=EDGE, *, angle=0):
    """Extrude an x-z outline toward the back, preserving any notches."""
    cos_angle, sin_angle = cos(radians(angle)), sin(radians(angle))

    def profile(at):
        return [
            project((x * cos_angle - at * sin_angle, x * sin_angle + at * cos_angle, z))
            for x, z in outline
        ]

    front = profile(y)
    back = profile(y - depth)
    sides = [
        Polygon((front[i - 1], front[i], back[i], back[i - 1]))
        for i in range(len(front))
    ]
    face = Polygon(front)
    body = unary_union([face, Polygon(back), *(side for side in sides if side.area)])
    s.layers.append((body.boundary, body, ink))
    rim = face.boundary.difference(body.boundary.buffer(.13))
    s.layers.append((rim, None, DETAIL))


def molar(x, z, scale=1):
    """Return the outline of a two-rooted molar in the x-z plane."""
    start = (-36, 8)
    curves = (
        ((-47, 27), (-39, 45), (-23, 45)),
        ((-12, 45), (-7, 36), (0, 36)),
        ((7, 36), (12, 45), (23, 45)),
        ((39, 45), (47, 27), (36, 8)),
        ((31, 0), (30, -10), (28, -19)),
        ((25, -33), (21, -44), (14, -44)),
        ((5, -44), (10, -15), (0, -11)),
        ((-10, -15), (-5, -44), (-14, -44)),
        ((-21, -44), (-25, -33), (-28, -19)),
        ((-30, -8), (-31, -2), start),
    )
    points = []
    for control1, control2, stop in curves:
        for step in range(10):
            t = step / 10
            p = 1 - t
            u, v = (
                p**3 * a + 3 * p**2 * t * b + 3 * p * t**2 * c + t**3 * d
                for a, b, c, d in zip(start, control1, control2, stop)
            )
            points.append((x + scale * u, z + scale * v))
        start = stop
    return points


class Surface:
    """Draw details in the local coordinates of a page or cover."""

    def __init__(self, scene, place):
        self.scene = scene
        self.at = place

    def line(self, points, ink=DETAIL, dashed=False):
        self.scene.line([self.at(u, v) for u, v in points], ink, dashed=dashed)

    def outline(self, points, ink=EDGE):
        self.line([*points, points[0]], ink)

    def oval(self, u, v, rx, ry, ink=DETAIL):
        self.line(oval(u, v, rx, ry), ink)

    def frame(self, u, v, width, height, radius=2, ink=DETAIL):
        self.outline(rounded(u, v, width, height, radius), ink)

    def rows(self, u, v, widths, step=7, ink=DETAIL):
        for i, width in enumerate(widths):
            row = v + i * step
            self.line([(u, row), (u + width, row)], ink)

    def slab(self, outline, depth, ink=EDGE):
        front = [project(self.at(u, v)) for u, v in outline]
        back = [(x, y + depth * .8660254) for x, y in front]
        face = Polygon(front)
        sides = [
            Polygon((front[i - 1], front[i], back[i], back[i - 1]))
            for i in range(len(front))
        ]
        body = unary_union([face, Polygon(back), *(side for side in sides if side.area > .001)])
        self.scene.layers.append((body.boundary, body, ink))
        rim = face.boundary.difference(body.boundary.buffer(.15))
        self.scene.layers.append((rim, None, DETAIL))


def paper(s, height, *, pitch=.55, run=.84, angle=0, depth=3):
    """A sheet rises from its near edge, with an optional turn across the floor."""
    c, q = cos(radians(angle)), sin(radians(angle))
    return Surface(s, lambda u, v: (u * c - v * run * q, u * q + v * run * c,
                                    depth + (height - v) * pitch))


def landscape(page, u, v, w, h, *, clip=None):
    border = rounded(u, v, w, h, 2)
    strokes = (
        (border + border[:1], DETAIL),
        ([(u, v + .78*h), (u + .30*w, v + .36*h), (u + .49*w, v + .66*h),
          (u + .65*w, v + .48*h), (u + w, v + .83*h)], EDGE),
        (oval(u + .74*w, v + .25*h, .085*h, .085*h), EDGE),
    )
    for points, ink in strokes:
        if clip is None:
            page.line(points, ink)
        else:
            for segment in segments(LineString(points).intersection(clip)):
                page.line(segment, ink)


def publication(s, *, depth=6):
    """A low, folded newspaper with a common masthead and story grid."""
    page = paper(s, 99, pitch=.34, angle=-12, depth=depth)
    page.slab(rounded(0, 0, 75, 99, 2), depth)
    page.line([(2, 98), (73, 98)], DETAIL)
    page.rows(9, 13, (47,), ink=BOLD)
    page.rows(9, 21, (57,), ink=EDGE)
    landscape(page, 9, 32, 30, 29)
    page.rows(45, 35, (21, 17, 21, 15, 20), step=5.7)
    page.rows(9, 72, (55, 48, 54), step=7)
    return page


def magazine(s):
    """A saddle-stitched periodical with a cover photograph and masthead."""
    cover = paper(s, 99, pitch=.49, angle=8, depth=6)
    cover.slab(rounded(0, 0, 75, 99, 3), 6)
    cover.line([(5, 4), (5, 95)], DETAIL)
    cover.rows(13, 15, (49,), ink=BOLD)
    cover.rows(13, 23, (28,), ink=EDGE)
    landscape(cover, 12, 33, 53, 42)
    cover.rows(13, 85, (35, 23), step=7)
    return cover


def photograph(s, *, torn=False):
    """A photographic print with a wide bottom border and a landscape image."""
    page = paper(s, 72, pitch=.29, angle=10, depth=3)
    if torn:
        tear = [(91, 34), (77, 41), (80, 48), (65, 50), (67, 58), (56, 61), (54, 72)]
        outline = [(0, 0), (91, 0), *tear, (0, 72)]
        page.slab(outline, 3)
        landscape(page, 7, 7, 76, 54, clip=Polygon(outline))
        corner = [*reversed(tear), (91, 72)]
        fragment = Surface(s, lambda u, v: page.at(u + 7, v + 5))
        fragment.slab(corner, 3)
        landscape(fragment, 7, 7, 76, 54, clip=Polygon(corner))
    else:
        page.slab(rounded(0, 0, 91, 72, 3), 3)
        landscape(page, 7, 7, 76, 54)
    return page


def open_book(s, *, tabs=False):
    """A thick open book with curved leaves and a low central gutter."""
    left_edge = [(4, 14), (18, 16), (35, 15), (49, 12), (58, 8), (63, 7)]
    right_edge = [(63, 7), (68, 9), (76, 13), (89, 16), (106, 17), (122, 15)]
    s.box(0, 0, 0, 126, 76, 4, 3)
    pages = []
    for edges in (left_edge, right_edge):
        def place(u, v, edges=edges):
            for (a, low), (b, high) in zip(edges, edges[1:]):
                if u <= b:
                    z = low + (high - low) * (u - a) / (b - a)
                    return u, v, z + (73 - v) * .06
            raise ValueError("Point lies past the edge of the book")

        page = Surface(s, place)
        xs = [u for u, _ in edges]
        outline = [(u, 3) for u in xs] + [(u, 72) for u in reversed(xs)]
        s.face([*[place(u, 72) for u in xs], *[(u, 72, 4) for u in reversed(xs)]], DETAIL)
        outer = xs[0] if xs[0] < 63 else xs[-1]
        if outer > 63:
            s.face([place(outer, 3), place(outer, 72), (outer, 72, 4), (outer, 3, 4)], DETAIL)
        s.face([place(u, v) for u, v in outline])
        s.line([(u, 72, 4 + (place(u, 72)[2] - 4) * .48) for u in xs], DETAIL)
        pages.append(page)
    if tabs:
        for v in (12, 30, 48):
            s.face([(122, v, 12), (135, v + 2, 12), (135, v + 12, 12), (122, v + 12, 12)])
    return pages


def media_frame(page, u, v, w, h, *, perforated=False):
    page.frame(u, v, w, h, 3, EDGE)
    cx, cy = u + w/2, v + h/2
    scale = h*.26
    page.outline([(cx - scale*.66, cy - scale), (cx + scale, cy),
                  (cx - scale*.66, cy + scale)], BOLD)
    if perforated:
        for x in range(int(u) + 7, int(u + w) - 5, 9):
            page.rows(x, v + 4, (3,))
            page.rows(x, v + h - 4, (3,))


def file_sheet(s):
    page = paper(s, 91, pitch=.76, run=.69, angle=8, depth=4)
    page.slab([(0, 0), (53, 0), (70, 17), (70, 91), (0, 91)], 4)
    page.line([(53, 0), (53, 17), (70, 17)], EDGE)
    return page


def camera_emblem(page, u, v, w):
    outline = [(0, .20), (.23, .20), (.31, 0), (.66, 0), (.74, .20),
               (1, .20), (1, .75), (0, .75)]
    page.outline([(u + a*w, v + b*w) for a, b in outline])
    page.oval(u + .50*w, v + .44*w, .15*w, .15*w, EDGE)


def broadcast_mic(s, *, labels=False):
    """A grille microphone and pivot yoke on a weighted desk stand."""
    s.disk(0, 0, 0, 25, 20, 5)
    s.disk(0, 0, 5, 8, 7, 4, DETAIL)
    s.tube([(0, 0, 9), (0, 0, 28)], 2.7, EDGE)
    s.tube([(-29, 5, 57), (-29, 5, 40), (-24, 5, 32), (-15, 5, 28),
            (15, 5, 28), (24, 5, 32), (29, 5, 40), (29, 5, 57)], 2.1, EDGE)
    if labels:
        for x, z, direction in ((-12, 82, -1), (11, 67, 1)):
            outer = x + direction * 45
            upright(s, [(x, z), (outer, z), (outer, z + 19), (x, z + 19)], -3, 2)
            s.line([(x + direction * 11, -3, z + 12), (outer - direction * 7, -3, z + 12)], EDGE)
            s.line([(x + direction * 11, -3, z + 6), (outer - direction * 15, -3, z + 6)], DETAIL)
    upright(s, rounded(-17, 32, 34, 72, 15), 11, 20)
    s.line([(-13, 11, 57), (13, 11, 57)], EDGE)
    for z, w in ((66, 19), (74, 23), (82, 23), (90, 18)):
        s.line([(-w/2, 11, z), (w/2, 11, z)], EDGE)


def closed_book(s, *, angle=-20, width=76, height=99, depth=14):
    """A hardback with a distinct spine and recessed page block."""
    cover = paper(s, height, angle=angle, pitch=.58, run=.70, depth=depth)
    cover.slab(rounded(0, 0, width, height, 3), depth)
    cover.slab(rounded(0, 0, width, height, 3), 2.7)
    cover.line([(7, 2), (7, height - 2)], EDGE)
    for z in (4.8, depth - 2.1):
        s.line([(x, y, pz - z) for x, y, pz in
                (cover.at(8, height), cover.at(width - 4, height))], DETAIL)
    return cover


def video_player(s):
    """A video player housing with a viewport and a recessed control rail."""
    panel = paper(s, 80, angle=-27, pitch=.92, run=.24, depth=8)
    panel.slab(rounded(0, 0, 115, 80, 5), 8)
    panel.frame(7, 7, 101, 47, 2, DETAIL)
    panel.line([(0, 59), (115, 59)], EDGE)
    panel.line([(27, 69), (81, 69)], DETAIL)
    panel.oval(53, 69, 3, 3, EDGE)
    play_mark(panel, 16, 69, 7, EDGE)
    return panel


def play_mark(page, u, v, radius, ink=BOLD):
    page.outline([(u - .55*radius, v - radius), (u + .95*radius, v),
                  (u - .55*radius, v + radius)], ink)


def proof_page(s, *, crop=False):
    """A thick print proof with a masthead and inset type."""
    page = paper(s, 101, pitch=.73, run=.49, angle=-16, depth=6)
    page.slab(rounded(0, 0, 82, 101, 3), 6)
    margin = 12 if crop else 10
    if crop:
        for u, du in ((11, -1), (71, 1)):
            for v, dv in ((11, -1), (90, 1)):
                page.line([(u + du*2, v), (u + du*7, v)], EDGE)
                page.line([(u, v + dv*2), (u, v + dv*7)], EDGE)
    page.rows(margin + 3, 20, (47,), ink=BOLD)
    page.rows(margin + 3, 29, (34,), ink=EDGE)
    return page


def magnifier(page, u, v, r, *, text=()):
    """A lens over the proof, with an optional enlarged passage inside it."""
    s = page.scene
    page.slab(rounded(u - 4, v + r - 1, 8, r*1.12, 3.4), 2)
    s.face([page.at(x, y) for x, y in oval(u, v, r, r)[:-1]], EDGE)
    page.oval(u, v, r - 3.2, r - 3.2, DETAIL)
    for offset, width, ink in text:
        page.rows(u - width/2, v + offset, (width,), ink=ink)


def photo_print(s, width, height, *, offset=(0, 0, 0), angle=-25, image=True):
    """A tilted photographic print with a landscape and heavier foot margin."""
    origin = paper(s, height, pitch=.83, run=.42, angle=angle, depth=4)
    page = Surface(s, lambda u, v: tuple(a + b for a, b in zip(origin.at(u, v), offset)))
    page.slab(rounded(0, 0, width, height, 3), 4)
    if image:
        inset = width*.075
        landscape(page, inset, inset, width - 2*inset, height - 2.9*inset)
    return page


def front_surface(s, *, angle=-20, y=0, z=0, lean=0):
    """Return a plane viewed from the front, with its top optionally leaning back."""
    c, q = cos(radians(angle)), sin(radians(angle))

    def place(u, v):
        depth = y - lean * v
        return (u*c - depth*q, u*q + depth*c, z + v)

    return Surface(s, place)


def standing_card(s, width, height, *, angle=-20, lean=.30, depth=5):
    face = front_surface(s, angle=angle, z=depth, lean=lean)
    face.slab(rounded(0, 0, width, height, 4), depth)
    return face


def capsule_mark(face, u, v, radius, ink=EDGE):
    """Draw a diagonal capsule with a seam across its centre."""
    c = .7071068

    def place(x, y):
        return u + (x-y)*c, v + (x+y)*c

    outline = rounded(-radius, -.43*radius, 2*radius, .86*radius, .43*radius)
    face.outline([place(x, y) for x, y in outline], ink)
    face.line([place(0, -.43*radius), place(0, .43*radius)], ink)


def dumbbell_mark(face, u, v, radius, ink=EDGE):
    for x in (u - radius, u + .56*radius):
        face.frame(x, v - .47*radius, .44*radius, .94*radius, .10*radius, ink)
    for y in (v - .10*radius, v + .10*radius):
        face.line([(u - .56*radius, y), (u + .56*radius, y)], ink)


def camera_mark(face, u, v, scale=1, ink=EDGE):
    face.frame(u - 12*scale, v - 8*scale, 24*scale, 16*scale, 3*scale, ink)
    face.line([(u + x*scale, v + y*scale) for x, y in
               ((12, -3), (22, -8), (22, 8), (12, 3))], ink)


def stethoscope_mark(face, u, v, scale=1, ink=EDGE):
    def stroke(points):
        face.line([(u + x*scale, v + y*scale) for x, y in points], ink)

    stroke([(-10, 12), (-12, 12), (-12, 4), (-10, 0), (-6, -3),
            (0, -3), (4, 0), (6, 4), (6, 12), (4, 12)])
    stroke([(-3, -3), (-3, -9), (0, -14), (5, -16), (11, -16),
            (15, -12), (15, -6)])
    face.oval(u + 15*scale, v - 3*scale, 3.4*scale, 3.4*scale, ink)


def knee_mark(face, u, v, scale=1, ink=EDGE):
    """Print the ends of the femur and tibia with their kneecap."""
    parts = [
        [(-8, 21), (2, 21), (1, 12), (5, 7), (5, 2), (3, -1), (-1, 0),
         (-4, 2), (-8, 1), (-11, 4), (-11, 8), (-8, 13)],
        [(-9, -4), (-4, -4), (1, -7), (0, -10), (-5, -13), (-9, -21),
         (-19, -17), (-13, -11), (-13, -7)],
    ]
    for part in parts:
        face.outline([(u + x*scale, v + y*scale) for x, y in part], ink)
    face.oval(u + 10*scale, v - 1*scale, 3.3*scale, 5.3*scale, ink)


def medical_folder(s, *, sheet_tabs=()):
    """A single standing file folder, open just enough to expose a record."""
    def flap(offset, lean):
        return front_surface(s, angle=-13, z=4, y=offset, lean=lean)

    back = flap(-11, .12)
    back.slab([(0, 0), (92, 0), (92, 62), (43, 62), (37, 73),
               (5, 73), (0, 68)], 4)
    offsets = sheet_tabs or ((8, 65, 72),)
    for index, (u, height, width) in enumerate(offsets):
        sheet = flap(-8 + index*3, .035)
        sheet.slab(rounded(u, 4, width, height - 4, 2), 2, DETAIL)
        sheet.rows(u + 6, height - 8, (width - 14,), ink=DETAIL)

    front = flap(5, -.12)
    floor = [plane.at(u, 0) for plane, u in ((back, 0), (back, 92), (front, 92), (front, 0))]
    s.face([(x, y, z - 4) for x, y, z in floor], DETAIL)
    front.slab([(0, 0), (92, 0), (92, 53), (85, 57), (49, 57), (43, 49),
                (4, 49), (0, 46)], 4)
    return front


def desktop_display(s, *, width=100, height=65, angle=-15):
    """Draw a display with its own stand and return the glass surface."""
    foot = front_surface(s, angle=angle, y=1)
    x, y, _ = foot.at(width/2, 0)
    s.box(x - 18, y - 12, 0, 36, 24, 4, 4)
    s.box(x - 6, y - 4, 4, 12, 8, 27, 2)
    upright(s, rounded(0, 22, width, height, 5), 9, 7, angle=angle)
    face = front_surface(s, angle=angle, y=9, z=22)
    face.frame(5, 6, width - 10, height - 12, 3, DETAIL)
    return face


def telehealth_display(s):
    face = desktop_display(s)
    face.line([(5, 50), (95, 50)], DETAIL)
    for x in (11, 16, 21):
        face.oval(x, 54.5, .85, .85)
    face.line([(5, 17), (95, 17)], DETAIL)
    camera_mark(face, 32, 11.5, .28)
    face.frame(68, 8, 15, 6, 3)
    return face


def pharmacy_bottle(s, x, y, z, scale=1):
    """Draw a capped pharmacy vial and return its label surface."""
    s.disk(x, y, z, 16*scale, 16*scale, 43*scale)
    s.disk(x, y, z+43*scale, 13*scale, 13*scale, 4*scale, DETAIL)
    s.disk(x, y, z+47*scale, 17*scale, 17*scale, 10*scale)
    for level in (9, 35):
        s.ellipse(x, y, z+level*scale, 16*scale, 16*scale, DETAIL, -43, 133)
    for angle in (8, 25, 42, 59, 76, 93):
        a = x + 17*scale*cos(radians(angle))
        b = y + 17*scale*sin(radians(angle))
        s.line([(a, b, z+47.4*scale), (a, b, z+53.4*scale)], DETAIL)

    return Surface(s, lambda u, v: (x+(11.3+.707*u)*scale,
                                      y+(11.3-.707*u)*scale, z+v*scale))


def desk_calendar(s, *, reserved=None):
    """A wire-bound desk calendar with a five-column, three-week date grid."""
    face = front_surface(s, angle=-19, z=5, lean=.48)
    left, right = face.at(0, 0), face.at(94, 0)
    a, b, _ = face.at(0, 79)
    rear_left = (a - 5, b - 12, 0)
    rear_right = (rear_left[0] + right[0] - left[0],
                  rear_left[1] + right[1] - left[1], 0)
    s.face([left, right, rear_right, rear_left], DETAIL)
    s.face([right, rear_right, face.at(94, 79)])
    face.slab(rounded(0, 0, 94, 81, 3.5), 5)
    face.line([(0, 57), (94, 57)], EDGE)
    for u in (17, 77):
        s.tube([face.at(u, 74), face.at(u, 84), face.at(u - 1, 89),
                (face.at(u, 87)[0] - 3, face.at(u, 87)[1] - 8, face.at(u, 86)[2])], 1.7)
    for column, u in enumerate(range(8, 77, 17)):
        for row, v in enumerate((8, 24, 40)):
            if reserved is None or (column, row) not in reserved:
                face.frame(u, v, 12, 11, 1.7)
    return face


def clinic_clipboard(s):
    """A clipboard with a raised metal clip and a separately edged sheet."""
    board = paper(s, 98, angle=-30, pitch=.73, run=.54, depth=9)
    board.slab(rounded(0, 0, 72, 98, 4), 9)
    board.slab(rounded(5, 9, 62, 82, 2), 2, DETAIL)
    board.slab(rounded(20, 1, 32, 13, 3), 4)
    board.line([(27, 7), (45, 7)], DETAIL)
    return board


def printed_glyph(surface, kind, u, v, size, ink=EDGE, *, down=False):
    """Place a shared glyph on an inclined page or product face."""
    for stroke in _strokes(kind, size):
        surface.line([(u + a, v - b if down else v + b) for a, b in stroke], ink)


def sample_vial(s, place):
    """A capped sample tube aligned along the third coordinate of place."""
    def collar(profiles):
        points = [project(place(u, v, h)) for h, r in profiles
                  for u, v in oval(0, 0, r, r, count=40)]
        hull = MultiPoint(points).convex_hull
        s.layers.append((hull.boundary, hull, EDGE))

    collar(((0, 5), (3, 8.5), (43, 8.5)))
    for h in (11, 29):
        s.line([place(u, v, h) for u, v in oval(0, 0, 8.5, 5, 0, 180, 24)], DETAIL)
    for h, width in ((17, 7), (23, 10)):
        s.line([place(u, 8.5, h) for u in (-width/2, width/2)], EDGE)
    collar(((39, 9), (41, 10.5), (49, 10.5), (51, 9)))
    s.line([place(u, v, 51) for u, v in oval(0, 0, 9, 9)], DETAIL)
    for u in (-5, 0, 5):
        v = (10.5**2 - u**2)**.5
        s.line([place(u, v, 42), place(u, v, 48)], DETAIL)


def bed_pictogram(page, u, v, scale=1):
    """Print a side elevation of a made bed on a top-to-bottom page."""
    def stroke(points, ink=EDGE):
        page.line([(u + x*scale, v + y*scale) for x, y in points], ink)

    stroke([(0, 21), (0, 0)])
    stroke([(0, 15), (39, 15), (39, 21)])
    stroke([(39, 15), (39, 11), (36, 8), (5, 8), (5, 15)])
    stroke([(16, 8), (16, 15)], DETAIL)
    stroke([(4, 8), (4, 5), (7, 3), (13, 3), (15, 5), (15, 8)])


def wrench_mark(face, u, v, size, ink=EDGE):
    """Print an open-jaw wrench with a diagonal handle."""
    outline = [(-18, -19), (-22, -16), (-21, -11), (-2, 7), (-5, 13),
               (-3, 20), (3, 24), (4, 15), (10, 12), (16, 18), (17, 11),
               (13, 5), (6, 3), (-12, -17), (-16, -20)]
    face.outline([(u + x*size, v + y*size) for x, y in outline], ink)


def hotel_keycard(s):
    """A room card with its magnetic stripe and a large key emblem."""
    card = paper(s, 66, pitch=.59, run=.75, angle=12, depth=5)
    card.slab(rounded(0, 0, 101, 66, 5), 5)
    card.line([(1, 16), (100, 16)], EDGE)
    card.line([(0, 25), (101, 25)], DETAIL)
    card.oval(31, 44, 11, 10, EDGE)
    card.oval(30, 44, 4, 4, DETAIL)
    card.line([(41, 41), (74, 41), (74, 50), (68, 50), (68, 46),
               (62, 46), (62, 52), (57, 52), (57, 47), (41, 47)], EDGE)
    return card


def service_profile(s, *, profile_lines=True):
    """A provider credential with a trade pictogram and a short profile."""
    card = standing_card(s, 101, 69, angle=-28, lean=.40, depth=6)
    card.frame(39, 58, 23, 5, 2.45, EDGE)
    card.frame(9, 15, 39, 35, 4, DETAIL)
    wrench_mark(card, 29, 32, .62)
    card.rows(58, 46, (30,), ink=EDGE)
    if profile_lines:
        card.rows(58, 36, (24, 29), step=-8)
    return card


def reception_counter(s, *, clinic=False):
    """A reception desk with a chair behind the counter and service equipment."""
    s.box(45, -4, 4, 23, 26, 9, 3)
    s.tube([(56, 8, 7), (56, 8, 25)], 2.4)
    s.box(44, -10, 24, 25, 7, 32, 5)
    s.box(0, 22, 0, 85, 20, 43, 3)
    s.box(69, 1, 0, 16, 39, 43, 3)
    s.box(-3, 18, 42, 91, 27, 6, 3)
    s.box(66, -3, 42, 22, 28, 6, 3)
    if clinic:
        s.box(15, 24, 48, 23, 12, 3, 2)
        s.box(22, 24, 50, 8, 6, 11, 2)
        s.box(9, 22, 58, 35, 6, 23, 3)
        s.line([(14, 28, 62), (39, 28, 62)], DETAIL)
    else:
        s.disk(23, 29, 48, 11, 10, 3)
        s.solid(oval(23, 29, 9, 8)[:-1], 51, 6, oval(23, 29, 5, 4)[:-1])
        s.disk(23, 29, 57, 2, 2, 2, DETAIL)
    return Surface(s, lambda u, v: (u, 42.1, v))


def side_wheel(s, x, y, z, radius):
    """A vehicle wheel with a visible tire and hub on its y-normal face."""
    upright(s, oval(x, z, radius, radius)[:-1], y, 5)
    s.line([(u, y, v) for u, v in oval(x, z, radius*.47, radius*.47)], DETAIL)


def support_mark(face, u, v, scale=1, ink=EDGE):
    """Print a headset with ear pads and a short microphone boom."""
    face.line([(u + a*scale, v + b*scale)
               for a, b in oval(0, 0, 10, 12, 0, 180, count=24)], ink)
    for side in (-1, 1):
        face.frame(u + (10*side - 2.6)*scale, v - 5*scale,
                   5.2*scale, 8*scale, 1.6*scale, ink)
    face.line([(u + 10*scale, v - 5*scale),
               (u + 7*scale, v - 8*scale), (u + 3*scale, v - 8*scale)], ink)


def service_ticket(s, *, offset=0, workshop=False):
    """Draw a standing notched ticket and its printed service or workshop mark."""
    ticket = front_surface(s, angle=-25, y=offset, z=5, lean=.55)
    outline = [(0, 5), (5, 0), (70, 0), (73, 5), (77, 0), (101, 0),
               (107, 6), (107, 20), (101, 23), (99, 27), (101, 31),
               (107, 34), (107, 49), (101, 55), (77, 55), (73, 50),
               (70, 55), (5, 55), (0, 50), (0, 34), (6, 31), (8, 27),
               (6, 23), (0, 20)]
    ticket.slab(outline, 5)
    ticket.line([(73, 8), (73, 47)], EDGE, dashed=True)
    if workshop:
        wrench_mark(ticket, 27, 28, .55)
    else:
        support_mark(ticket, 27, 27, 1.05)
    ticket.rows(47, 34, (15, 11, 14), step=-7)
    return ticket


def speech_bubble(s, *, width=92, height=56, angle=-24, y=0, z=0, depth=6, u0=0, tail_at=.13):
    """Extrude a rounded speech bubble with its tail built into the outline."""
    plane = front_surface(s, angle=angle, y=y, z=z)
    face = Surface(s, lambda u, v: plane.at(u + u0, v))
    frame = rounded(0, 0, width, height, min(width, height)*.24)
    # The bottom edge runs from the final rounded corner to the first.
    frame.extend(((width*(tail_at + .05), 0), (width*tail_at, -height*.25),
                  (width*(tail_at + .20), 0)))
    face.slab(frame, depth)
    return face


def headset(s):
    """Draw a support headset with its microphone capsule at the boom tip."""
    outer = oval(0, 24, 35, 41, 180, 0, 36)
    inner = oval(0, 24, 29, 34, 0, 180, 36)
    upright(s, outer + inner, 0, 8)
    for x in (-32, 32):
        upright(s, rounded(-10, 2, 20, 26, 9), x + 7, 14, angle=-90)
        s.line([(x + 7, y, z) for y, z in oval(0, 15, 6, 8, count=32)], DETAIL)
    s.tube([(32, 9, 12), (30, 14, 8), (24, 18, 5), (14, 20, 5)], 1.6)
    s.tube([(14, 20, 5), (8, 20, 5)], 3)


def currency_mark(face, u, v, scale=1, ink=EDGE):
    """Print a currency sign on an amount field."""
    outline = [(5, 6), (2, 8), (-3, 8), (-6, 5), (-3, 1),
               (3, -1), (6, -4), (4, -7), (-1, -8), (-6, -6)]
    face.line([(u + a*scale, v + b*scale) for a, b in outline], ink)
    face.line([(u, v - 10*scale), (u, v + 10*scale)], ink)


def bezier_path(start, *sections, count=10):
    """Sample a continuous path of cubic Bézier sections in local or world coordinates."""
    points = [start]
    for control1, control2, end in sections:
        for step in range(1, count + 1):
            t = step / count
            keep = 1 - t
            points.append(tuple(keep**3*a + 3*keep**2*t*b + 3*keep*t**2*c + t**3*d
                                for a, b, c, d in zip(start, control1, control2, end)))
        start = end
    return points


def handset_outline():
    """Return the profile of an arched receiver with two broad end caps."""
    return bezier_path(
        (-41, -13),
        ((-43, 14), (-25, 28), (0, 28)),
        ((25, 28), (43, 14), (41, -13)),
        ((41, -18), (38, -20), (33, -20)),
        ((28, -20), (24, -20), (20, -20)),
        ((17, -20), (15, -17), (15, -13)),
        ((15, -9), (16, -4), (20, -2)),
        ((18, 7), (8, 11), (0, 11)),
        ((-8, 11), (-18, 7), (-20, -2)),
        ((-16, -4), (-15, -9), (-15, -13)),
        ((-15, -17), (-17, -20), (-20, -20)),
        ((-25, -20), (-30, -20), (-33, -20)),
        ((-38, -20), (-41, -18), (-41, -13)),
        count=8,
    )[:-1]


def phone_receiver(s, *, x=0, y=0, z=0, angle=-24, on_base=False):
    """Draw the same handset loose or resting in a desk phone cradle."""
    outline = handset_outline()
    if on_base:
        top = Surface(s, lambda u, v: (x + u, y - v, z + 8))
        top.slab(outline, 8)
    else:
        upright(s, [(u + x, v + z) for u, v in outline], y, 13, angle=angle)
        plane = front_surface(s, angle=angle, y=y)
        top = Surface(s, lambda u, v: plane.at(x + u, z + v))
    for side in (-1, 1):
        top.line([(side * 39, -1), (side * 32, 2), (side * 24, 0),
                  (side * 20, -2)], DETAIL)


def product_window(s):
    """Draw a desktop preview with browser chrome and a side navigation rail."""
    face = desktop_display(s, width=108, height=69, angle=-26)
    face.line([(5, 54), (103, 54)], EDGE)
    for x in (11, 17, 23):
        face.oval(x, 58.5, 1.05, 1.05, EDGE)
    face.line([(29, 6), (29, 54)], DETAIL)
    for v in (43, 33, 23):
        face.rows(11, v, (11,), ink=EDGE if v == 43 else DETAIL)
    return face


def dashboard_chart(face, u, v, width, height):
    """Print a compact rising three-column chart inside one module."""
    face.frame(u, v, width, height, 3, EDGE)
    for i, ratio in enumerate((.22, .42, .61)):
        x = u + width * (.19 + i * .23)
        h = height * ratio
        bottom = v + height * .18
        face.outline([(x, bottom), (x + width * .10, bottom),
                      (x + width * .10, bottom + h), (x, bottom + h)], EDGE)


def attached_panel(face, offset=3):
    """Put an overlay one short step in front of a window in the same orientation."""
    return Surface(face.scene, lambda u, v: tuple(
        coordinate + shift for coordinate, shift in zip(face.at(u, v), (offset, offset, offset))
    ))


def credential_mark(face, u, v, width, height):
    """Draw an employee credential with its lanyard slot and identification lines."""
    face.frame(u, v, width, height, 2.5, EDGE)
    face.frame(u + .30*width, v + .78*height, .40*width, .10*height, 1.2, EDGE)
    face.rows(u + .22*width, v + .34*height, (.55*width, .42*width),
              step=-.14*height)


def product_laptop(s):
    """Draw an open product laptop and return the screen surface."""
    upright(s, rounded(0, 4, 83, 62, 5), 1, 6)
    screen = Surface(s, lambda u, v: (u, 1, v))
    screen.frame(5, 10, 73, 51, 3)
    screen.line([(5, 51), (78, 51)], DETAIL)
    s.box(0, 0, 0, 83, 40, 5, 5)
    keyboard = Surface(s, lambda u, v: (u, v, 5))
    keyboard.frame(8, 6, 67, 13, 2, DETAIL)
    keyboard.rows(11, 12.5, (61,))
    keyboard.frame(30, 23, 23, 10, 2)
    return screen


def nav_window(s, *, x=0, y=0, z=0, width=110, height=76, angle=-29):
    """A browser window with a visible back edge and compact browser chrome."""
    base = front_surface(s, angle=angle, y=y, z=z + 6, lean=.09)
    face = Surface(s, lambda u, v: base.at(u + x, v))
    face.slab(rounded(0, 0, width, height, 4), 6)
    face.line([(1, height - 16), (width - 1, height - 16)], EDGE)
    for u in (8, 14, 20):
        face.oval(u, height - 8, 1, 1, EDGE)
    face.frame(30, height - 11.5, width - 39, 7, 3.5)
    return face


def search_control(face, u, v, width, height, *, query=0, icon=True):
    """An input capsule with an optional printed search lens and query line."""
    face.frame(u, v, width, height, height/2, EDGE)
    if icon:
        search_mark(face, u + height*.49, v + height*.56, height*.21)
    if query:
        face.rows(u + height*1.02, v + height*.5, (query,), ink=DETAIL)


def search_mark(face, u, v, radius, ink=EDGE):
    """Print a magnifying glass on a control face."""
    face.oval(u, v, radius, radius, ink)
    face.line([(u + radius*.71, v - radius*.71),
               (u + radius*1.60, v - radius*1.60)], ink)


def raised_lens(face, u, v, radius, *, direction=(.72, -.69)):
    """An open magnifier seated over a page or a window."""
    above = attached_panel(face, 3)
    face_magnifier(face.scene, above.at, u, v, radius, direction=direction)


def nav_phone(s, *, width=66, height=96, angle=-28):
    """A thick handheld screen resting on its lower edge."""
    base = front_surface(s, angle=angle, z=6, lean=.22)
    base.slab(rounded(0, 0, width, height, 8), 6)
    base.frame(4, 5, width - 8, height - 10, 5, DETAIL)
    base.line([(width*.39, height - 9), (width*.61, height - 9)], EDGE)
    return base


def nav_result_rows(face, u, v, widths, *, step=15):
    """Result titles with small thumbnail outlines and short secondary lines."""
    for i, width in enumerate(widths):
        y = v - i * step
        face.frame(u, y - 6, 8, 9, 1.7, DETAIL)
        face.rows(u + 13, y + 1, (width,), ink=EDGE)
        face.rows(u + 13, y - 4, (width*.58,))


def link_emblem(face, u, v, size):
    """Draw two interlocked links stamped on an article or dashboard."""
    def projected(points):
        return [project(face.at(u + (x-y)*size*.7071, v + (x+y)*size*.7071))
                for x, y in points]

    links = []
    for x in (-1.02, -.33):
        exterior = projected(rounded(x, -.33, 1.35, .66, .33))
        opening = projected(rounded(x + .15, -.18, 1.05, .36, .18))
        links.append(Polygon(exterior, [opening]))
    # The two loops pass over and under each other on opposite sides.
    halves = [Polygon(projected([(-2, 0), (2, 0), (2, y), (-2, y)]))
              for y in (-1, 1)]
    strokes = [link.boundary.difference(other.intersection(half).buffer(.13))
               for link, other, half in zip(links, reversed(links), halves)]
    face.scene.layers.append((unary_union(strokes), unary_union(links), EDGE))


def folder_emblem(face, u, v, width, height, *, solid=False):
    """A tabbed folder profile in local coordinates."""
    outline = [(u, v), (u + width, v), (u + width, v + height*.78),
               (u + width*.50, v + height*.78), (u + width*.39, v + height),
               (u, v + height)]
    if solid:
        face.slab(outline, 5)
    else:
        face.outline(outline, EDGE)
    face.line([(u, v + height*.57), (u + width, v + height*.57)], DETAIL)


def filter_key(s, draw_mark):
    """Seat a small pictogram tile across the near-right rim of a funnel."""
    face = front_surface(s, angle=-30, y=12, z=44)
    face.slab(rounded(18, 0, 34, 32, 6), 4)
    draw_mark(face, 35, 16)


def nav_article(s):
    """An upright, bound article with three section headings."""
    face = standing_card(s, 78, 108, angle=-27, lean=.27, depth=8)
    face.line([(7, 3), (7, 105)], DETAIL)
    face.rows(15, 94, (49,), ink=EDGE)
    face.rows(15, 86, (31,))
    return face


def article_sections(face):
    for v, width in ((69, 29), (45, 31), (21, 25)):
        face.rows(15, v, (width,), ink=EDGE)
        face.rows(15, v - 6, (36, 29), step=-5)


def nav_path(face, points, ink=EDGE, head=6):
    """Draw a shared motion arrow through a surface's local coordinates."""
    arrow(face.scene, [face.at(u, v) for u, v in points], ink, head)


def nav_thumbnail(face, u, v, width, height):
    """Place the landscape pictogram on a surface whose vertical axis rises."""
    thumbnail = Surface(face.scene, lambda x, y: face.at(u + x, v + height - y))
    landscape(thumbnail, 0, 0, width, height)
