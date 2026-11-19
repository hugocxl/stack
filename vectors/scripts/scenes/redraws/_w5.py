"""Shared objects and printed pictograms for the w5 redraws."""

from math import ceil, cos, radians, sin

from shapely.affinity import affine_transform
from shapely.geometry import MultiPoint, Polygon

from geometry import BOLD, DETAIL, EDGE, Scene, oval, project, rounded
from scenes.redraws._kit import badge, coin, glyph
from scenes.redraws.next_bus_countdown import side_window, wheel_side, windscreen


def upright_card(s, w, h, radius, depth, ink=EDGE):
    """Draw a rounded rectangle with its front face in the x-z plane at y=0."""
    outline = rounded(0, 0, w, h, radius)
    front = [(x, 0, z) for x, z in outline]
    back = [(x, -depth, z) for x, z in outline]
    hull = MultiPoint([project(point) for point in front + back]).convex_hull
    s.layers.append((hull.boundary, hull, ink))
    # Trace from the middle of the lower-right corner to the middle of the
    # upper-left corner, where the front face meets the visible thickness.
    s.line(front[4:23], ink)


def panel(s, outline, point, depth=3, ink=EDGE):
    """Extrude a convex outline behind a printed face."""
    front = [point(x, z) for x, z in outline]
    back = [(x, y - depth, z) for x, y, z in front]
    hull = MultiPoint([project(p) for p in front + back]).convex_hull
    seam = Polygon([project(p) for p in front]).boundary
    s.layers.append((hull.boundary.union(seam), hull, ink))


def rect(s, point, x, z, w, h, r=2, ink=EDGE):
    outline = rounded(x, z, w, h, r)
    s.line([point(a, b) for a, b in outline + outline[:1]], ink)


def bed_mark(s, point, x, z, k=1, ink=EDGE):
    def stroke(points):
        s.line([point(x + a*k, z + b*k) for a, b in points], ink)

    stroke([(-15, 8), (-15, -7)])
    stroke([(-15, -3), (15, -3), (15, -7)])
    stroke([(-13, -3), (-13, 2), (-11, 4), (-6, 4), (-4, 2), (-4, -3)])
    stroke([(-4, 1), (-2, 4), (11, 4), (15, 1), (15, -3)])


def hotel_door(s):
    s.box(0, -11, 0, 49, 16, 71, 2)
    rect(s, lambda x, z: (x, 5, z), 5, 2, 39, 64, 1.6)
    s.tube([(4, 9, 2), (4, 9, 67), (45, 9, 67), (45, 9, 2)], 1.7)
    s.box(12, 5, 43, 22, 3, 15, 2)
    bed_mark(s, lambda x, z: (x, 8, z), 23, 50, .53)
    s.box(32, 5, 24, 7, 4, 13, 1)
    s.line([(34, 9, 34), (37, 9, 34)], EDGE)
    s.tube([(35, 9, 28), (35, 12, 28), (27, 12, 28)], 1.05)


def train_mark(s, point, x, z, k=1, ink=EDGE):
    def stroke(points, weight=ink):
        s.line([point(x + a*k, z + b*k) for a, b in points], weight)

    stroke([(-7, 9), (7, 9), (10, 6), (10, -6), (7, -9),
            (-7, -9), (-10, -6), (-10, 6), (-7, 9)])
    stroke([(-7, 5), (7, 5), (7, -1), (-7, -1), (-7, 5)])
    for side in (-1, 1):
        stroke(oval(side*5, -5, 1.15, 1.15, count=14))
        stroke([(side*5, -9), (side*8, -12)])


def luggage(s):
    for x in (8, 35):
        s.box(x, 12, 0, 6, 7, 9, 2)
    s.box(0, 0, 6, 49, 23, 53, 6)
    rect(s, lambda x, z: (x, 23, z), 3.5, 10, 42, 45, 4, DETAIL)
    for x in (13, 24, 35):
        s.line([(x, 23, 17), (x, 23, 47)], DETAIL)
    s.tube([(15, 10, 58), (15, 10, 65), (17, 10, 68),
            (32, 10, 68), (34, 10, 65), (34, 10, 58)], 2)
    s.line([(49, 14, 13), (49, 14, 52)], DETAIL)


def luggage_tag(s):
    s.tube([(30, 10, 67), (36, 14, 64), (43, 19, 61)], .85)
    face = lambda x, z: (x, 20, z)
    outline = [(39, 59), (47, 63), (56, 57), (56, 40),
               (54, 38), (39, 38), (37, 40), (37, 55)]
    panel(s, outline, face, 2)
    s.line([face(x, z) for x, z in oval(45, 58, 1.6, 1.6, count=18)], DETAIL)
    return face


def bus(s, *, coach=False):
    length = 85 if coach else 74
    for x in (13, length - 14):
        s.tube([(x, 5, 7.5), (x, 35, 7.5)], 6.2)
        wheel_side(s, x, 35.5, 7.5)
    s.box(0, 4, 9, length, 31, 40 if coach else 36, 4)
    if coach:
        side_window(s, 5, 35, 30, 60, 15)
        for x in (25, 45):
            s.line([(x, 35, 30), (x, 35, 45)], EDGE)
        side_window(s, length - 15, 35, 18, 11, 26)
        windscreen(s, length, 7, 26, 25, 18)
    else:
        for x in (5, 21, 37):
            side_window(s, x, 35, 25, 13, 14)
        side_window(s, length - 20, 35, 14, 15, 25)
        s.line([(length - 12.5, 35, 14), (length - 12.5, 35, 39)], DETAIL)
        windscreen(s, length, 7, 23, 25, 14)
        windscreen(s, length, 11, 39, 17, 3.3)
    for y in (10, 29):
        s.line([(length, a, z) for a, z in oval(y, 17, 2.4, 1.7, count=20)], EDGE)
    s.line([(length, 15, 15), (length, 24, 15)], DETAIL)


def mountain_mark(s, point, x, z, k=1, ink=EDGE):
    ridge = [(-17, -5), (-6, 9), (3, -1), (9, 5), (17, -5)]
    snow = [(-10, 4), (-6, 2), (-2, 4)]
    s.line([point(x + a*k, z + b*k) for a, b in ridge], ink)
    s.line([point(x + a*k, z + b*k) for a, b in snow], DETAIL)


def backpack(s, *, open_top=False):
    for x in (8, 34):
        s.tube([(x, 7, 52), (x, 1, 47), (x, -1, 30),
                (x, 2, 12), (x, 10, 8)], 2.2)
    if not open_top:
        s.tube([(17, 13, 51), (17, 13, 57), (19, 13, 60),
                (25, 13, 60), (27, 13, 57), (27, 13, 51)], 1.6)
    if open_top:
        s.box(0, 5, 0, 44, 25, 29, 8)
        s.box(3, 6, 24, 38, 8, 15, 3)
        s.disk(13, 18, 23, 6.5, 6.5, 21)
        s.solid(oval(13, 18, 6.5, 6.5)[:-1], 44, 4,
                oval(13, 18, 3.9, 3.9)[:-1])
        s.disk(13, 18, 48, 4.1, 4.1, 4)
        s.tube([(22, 16, 34), (35, 16, 41)], 7.7)
        s.line([(a, 16, b) for a, b in oval(35, 41, 6.5, 7.3, count=30)], EDGE)
        s.line([(35, 16, 43.8), (37.3, 16, 42), (37, 16, 39),
                (34.2, 16, 38), (31.8, 16, 40.4), (32, 16, 43.7)], DETAIL)
        s.face([(1, 29, 26), (43, 29, 26), (43, 28, 33),
                (40, 27, 35), (5, 27, 35), (1, 28, 33)])
    else:
        s.solid(rounded(0, 5, 44, 25, 8), 0, 41, rounded(1, 6, 42, 23, 8))
        s.solid(rounded(1, 6, 42, 23, 8), 41, 12,
                rounded(6, 8, 32, 18, 7), crease=False)
        s.line([(3, 23, 42), (8, 28, 44), (35, 28, 44), (41, 23, 42)], DETAIL)
        s.line([(12, 28, 44), (12, 29, 39)], EDGE)
    s.box(5, 25, 6, 33, 10, 22, 5)
    s.line([(9, 35, 22.5), (34, 35, 22.5)], DETAIL)
    s.line([(14, 35, 22.5), (14, 35, 18.5)], DETAIL)


def folded_point(x, z):
    folds = ((0, 3), (25, -3), (50, 9), (75, 2))
    for (a, y0), (b, y1) in zip(folds, folds[1:]):
        if x <= b:
            return x, y0 + (y1 - y0) * (x - a) / (b - a) - .32*z, z
    raise ValueError("Map coordinate crosses the outer edge")


def standing_map(s):
    for a, b in ((0, 25), (25, 50), (50, 75)):
        panel(s, [(a, 0), (b, 0), (b, 43), (a, 43)], folded_point, 1.5)


def map_stroke(s, points, ink=DETAIL, **style):
    """Insert a vertex where a printed path crosses each fold."""
    vertices = [points[0]]
    for (a, z), (b, h) in zip(points, points[1:]):
        folds = [f for f in (25, 50) if min(a, b) < f < max(a, b)]
        for x in sorted(folds, reverse=b < a):
            vertices.append((x, z + (h - z) * (x - a) / (b - a)))
        vertices.append((b, h))
    s.line([folded_point(x, z) for x, z in vertices], ink, **style)


def pin_outline(x, z, r):
    return [*oval(x, z, r, r, -32, 212, 38),
            (x - .38*r, z - 1.3*r), (x, z - 1.82*r), (x + .38*r, z - 1.3*r)]


def location_pin(s, point, x, z, r, *, hole=True):
    panel(s, pin_outline(x, z, r), point, max(1.5, r*.19))
    if hole:
        s.line([point(a, b) for a, b in oval(x, z, r*.39, r*.39, count=26)], EDGE)


def ticket_face(s):
    """A notched ticket leans on its long edge."""
    face = lambda x, z: (x, -z*.54, z)
    outline = [(0, 3), (3, 0), (66, 0), (69, 4), (72, 0), (87, 0),
               (90, 3), (90, 37), (87, 40), (72, 40), (69, 36),
               (66, 40), (3, 40), (0, 37)]
    front = [face(x, z) for x, z in outline]
    back = [(x, y - 2, z) for x, y, z in front]
    s.face(back, DETAIL)
    s.face(front)
    s.line([face(69, 6), face(69, 34)], DETAIL, dashed=True)
    return face


def plane_mark(s, point, x, z, k=1, ink=EDGE):
    outline = [(0, 14), (2.4, 11), (2.7, 3.8), (14, -3.8), (14, -7),
               (2.6, -3.7), (2.3, -10), (6, -13), (6, -15),
               (0, -13), (-6, -15), (-6, -13), (-2.3, -10), (-2.6, -3.7),
               (-14, -7), (-14, -3.8), (-2.7, 3.8), (-2.4, 11), (0, 14)]
    s.line([point(x + a*k, z + b*k) for a, b in outline], ink)


def desk_calendar(s):
    """A ring-bound calendar set on a triangular folding stand."""
    face = lambda x, z: (x, 12 - .41*z, z)
    left, right = (0, 12, 0), (62, 12, 0)
    rear_left, rear_right = (0, -30, 0), (62, -30, 0)
    top_left, top_right = face(0, 54), face(62, 54)
    s.face([rear_left, rear_right, top_right, top_left], DETAIL)
    s.face([rear_right, right, top_right])
    panel(s, rounded(0, 0, 62, 54, .8), face, 2.7)
    s.line([face(0, 41), face(62, 41)], EDGE)
    for x in (13, 49):
        s.tube([(x, -14, 50), (x, -16, 55), (x, -14, 58),
                (x, -9, 58), (x, -6, 54), (x, -7, 49)], 1.3)
    return face


def clipboard(s, w=48, h=64):
    """A thick clipboard rests on its lower edge with a slight backward lean."""
    back = lambda x, z: (x, -z*.38, z)
    face = lambda x, z: (x, 1.1 - z*.38, z)
    panel(s, rounded(0, 0, w, h, 3), back, 5.5)
    panel(s, rounded(4, 4, w - 8, h - 9, 1.1), face, 1.1, DETAIL)
    panel(s, rounded(w*.29, h - 10, w*.42, 8, 1.5),
          lambda x, z: (x, 3 - z*.38, z), 2)
    return face


def car_mark(s, point, x, z, k=1, ink=EDGE):
    outline = [(-15, -4), (-15, 1), (-12, 3), (-8, 8), (5, 8), (11, 3),
               (15, 1), (15, -4), (12, -4), (12, -7), (8, -7), (8, -4),
               (-8, -4), (-8, -7), (-12, -7), (-12, -4), (-15, -4)]
    s.line([point(x + a*k, z + b*k) for a, b in outline], ink)
    s.line([point(x - 11*k, z + 3*k), point(x + 11*k, z + 3*k)], DETAIL)


def charger(s, x=0, y=0, scale=1, *, connected=False):
    def p(a, b, z):
        return x + a*scale, y + b*scale, z*scale

    s.box(*p(0, 0, 0), 22*scale, 16*scale, 55*scale, 2.7*scale)
    rect(s, lambda a, z: p(a, 16, z), 3, 34, 16, 15, 1.5)
    a, b, z = p(11, 16, 41.5)
    glyph(s, "bolt", a, b, z, 6*scale, EDGE)
    rect(s, lambda a, z: p(a, 16, z), 7, 22, 8, 8, 1.8)
    if connected:
        s.box(*p(8, 16, 24), 6*scale, 3*scale, 4*scale, .8*scale)
        return p(11, 19, 26)
    s.tube([p(22, 8, 37), p(27, 8, 34), p(29, 9, 26), p(29, 10, 11),
            p(27, 12, 6), p(23, 14, 6), p(20, 16.5, 11), p(19, 17, 21),
            p(14, 17, 26)], 1.1*scale)


def bell_mark(s, point, x, z, k=1, ink=EDGE):
    def stroke(points, weight=ink):
        s.line([point(x + a*k, z + b*k) for a, b in points], weight)

    stroke([(-15, -5), (-12, -2), (-11, 3), (-7, 8), (-3, 10),
            (3, 10), (7, 8), (11, 3), (12, -2), (15, -5),
            (15, -8), (-15, -8), (-15, -5), (15, -5)])
    stroke([(-3.5, 10), (-3, 14), (3, 14), (3.5, 10)])


def van(s):
    for x in (15, 59):
        s.tube([(x, 5, 8), (x, 34, 8)], 6.4)
        wheel_side(s, x, 34.4, 8)
    profile = [(0, 9), (0, 39), (4, 44), (49, 44), (57, 40),
               (65, 28), (73, 25), (75, 21), (75, 9)]
    for (a, z), (b, h) in zip(profile[1:-1], profile[2:]):
        s.face([(a, 4, z), (b, 4, h), (b, 34, h), (a, 34, z)], EDGE)
    arches = [(a, 34, z) for x in (59, 15) for a, z in oval(x, 9, 9.2, 9.2, 0, 180, 30)]
    s.face([*[(x, 34, z) for x, z in profile], *arches])
    s.face([(75, 4, 9), (75, 4, 21), (75, 34, 21), (75, 34, 9)])
    s.face([(48, 34, 37), (55, 34, 37), (61, 34, 28), (48, 34, 28)])
    rect(s, lambda x, z: (x, 34, z), 18, 22, 25, 16, 1.5, DETAIL)
    s.line([(42, 34, 22), (42, 34, 13)], DETAIL)
    s.face([(57.5, 7, 39.25), (64, 7, 29.5), (64, 31, 29.5), (57.5, 31, 39.25)])
    for y in (8, 26):
        s.line([(75, y, 16), (75, y + 4, 16)], EDGE)


def baggage_scale(s, *, limit=False):
    """A platform scale supports the same upright case used in the baggage figures."""
    s.box(-5, -4, -14, 59, 51, 5, 3)
    s.face([(-5, -4, -1), (54, -4, -1), (54, 25, -1), (-5, 25, -1)])
    s.face([(54, -4, -9), (54, -4, -1), (54, 25, -1), (54, 47, -9)])
    s.face([(-5, 25, -1), (54, 25, -1), (54, 47, -9), (-5, 47, -9)])
    s.box(-2, -1, -1, 53, 26, 1, 2)
    dial = lambda x, y: (x, y, -1 - (y - 25)*8/22)
    s.line([dial(a, b) for a, b in oval(22, 41, 17, 12, 169, 371, 32)], EDGE)
    for x, y, a, b in ((10, 38, 7, 37), (13, 34, 11, 32),
                        (19, 33, 18, 30), (25, 33, 26, 30), (31, 34, 33, 32),
                        (34, 38, 37, 37)):
        s.line([dial(x, y), dial(a, b)], DETAIL)
    s.line([dial(22, 40), dial(28, 33)], EDGE)
    if limit:
        s.line([dial(31, 37), dial(35, 30)], BOLD)
    luggage(s)


def mapped_route(s):
    """Draw a continuous route across the creases of the shared folded map."""
    standing_map(s)
    map_stroke(s, [(11, 12), (19, 18), (32, 18), (40, 12),
                   (51, 16), (56, 26), (65, 29)], BOLD)
    for road in ([(5, 29), (19, 28), (30, 34), (44, 34)],
                 [(31, 5), (40, 5), (51, 9), (70, 10)],
                 [(53, 37), (62, 34), (71, 35)]):
        map_stroke(s, road, DETAIL)


def open_guide(s):
    """Open a two-page guide at its spine and rest its lower corners on the ground."""
    def left(x, z):
        return x, -z*.71 - x*.22, z + x*.07

    def right(x, z):
        return x, -z*.71 + (x - 40)*.23 - 8.8, z + (80 - x)*.07

    for a, b, point in ((0, 40, left), (40, 80, right)):
        outline = [point(a, 0), point(b, 0), point(b, 48), point(a, 48)]
        cover = [(x, y - 3.4, z - 2) for x, y, z in outline]
        s.face(cover)
        s.face(outline)
    return left, right


def closed_guide(s):
    """A pocket guide stands on its lower binding edge."""
    cover = lambda x, z: (x, -z*.30, z)
    panel(s, [(0, 0), (50, 0), (50, 65), (0, 65)], cover, 10)
    s.line([cover(6, 2), cover(6, 63)], DETAIL)
    s.line([(50, -4.5 - z*.30, z) for z in (2, 63)], DETAIL)
    return cover


def hotel_bed(s):
    for x, y in ((4, 5), (46, 5), (4, 61), (46, 61)):
        s.box(x, y, 0, 5, 5, 9, 1.3)
    s.box(0, 0, 6, 55, 71, 9, 4)
    s.box(0, 0, 14, 55, 5, 27, 3)
    s.box(2, 5, 15, 51, 64, 8, 4)
    for x in (6, 29):
        s.box(x, 9, 23, 20, 15, 4.2, 4)
    # The blanket wraps around the foot of the mattress.
    s.box(1, 29, 18, 53, 41, 6, 3)
    s.box(1, 29, 24, 53, 8, 2, 1)
    s.line([(6, 40, 24), (6, 64, 24)], DETAIL)
    s.line([(49, 40, 24), (49, 64, 24)], DETAIL)


def folded_sheet(s, w=54, h=64, *, lean=.4, fold=13):
    """A curled-corner document with a back layer for support and thickness."""
    face = lambda x, z: (x, -z * lean, z)
    outline = [(0, 0), (w, 0), (w, h - fold), (w - fold, h), (0, h)]
    panel(s, [(0, 0), (w, 0), (w, h), (0, h)],
          lambda x, z: (x, -4 - z * lean, z), 2.5)
    panel(s, outline, face, 1.5)
    s.face([face(w - fold, h), face(w - fold, h - fold), face(w, h - fold)], EDGE)
    return face


def key_mark(s, point, x, z, scale=1, *, angle=0, ink=EDGE):
    """A bow and two teeth share one continuous engraved key outline."""
    ca, sa = cos(radians(angle)), sin(radians(angle))

    def at(u, v):
        return point(x + (u * ca - v * sa) * scale, z + (u * sa + v * ca) * scale)

    bow = oval(0, 0, 7.5, 7.5, 24, 336, 36)
    s.line([at(u, v) for u, v in [*bow, (24, -3.05), (24, 3.05),
            (20, 3.05), (20, 0), (17, 0), (17, 3.05), bow[0]]], ink)
    s.line([at(u, v) for u, v in oval(-1.3, 0, 2.5, 2.5, count=30)], ink)


def avatar_mark(s, point, x, z, scale=1, ink=EDGE):
    """A contact icon with a featureless head and a shallow shoulder arc."""
    s.line([point(x + u * scale, z + v * scale)
            for u, v in oval(0, 4, 3.5, 3.5, count=26)], ink)
    s.line([point(x + u * scale, z + v * scale)
            for u, v in oval(0, -5.5, 7.5, 4.5, 0, 180, 18)], ink)


def redaction(s, point, x, z, width, height):
    """An opaque-looking bar made of parallel strokes in the current ink."""
    a = project(point(x, z))
    b = project(point(x, z + height))
    count = ceil(abs(b[1] - a[1]) * 5)
    for i in range(count + 1):
        row = z + height * i / count
        s.line([point(x, row), point(x + width, row)], BOLD)


def passkey_credential(s):
    """An identity token with an engraved contact-and-key pictogram."""
    face = lambda x, z: (x, -z * .21, z)
    panel(s, rounded(0, 0, 66, 45, 4), face, 6)
    rect(s, face, 5, 5, 56, 35, 3, DETAIL)
    avatar_mark(s, face, 20, 22, 1.43)
    key_mark(s, face, 37, 27, .9, angle=-24)


def identity_card(s):
    """A thick ID card stands on its lower edge with a recessed portrait frame."""
    face = lambda x, z: (x, -z * .15, z)
    panel(s, rounded(0, 0, 71, 49, 4.5), face, 5.5)
    rect(s, face, 7, 8, 28, 32, 3, DETAIL)
    return face


def identity_details(s, face):
    avatar_mark(s, face, 21, 23, 1.52)
    for z, length in ((27, 21), (18, 15)):
        s.line([face(42, z), face(42 + length, z)], DETAIL)


def device(s, x=0, y=0, w=38, h=66, *, tablet=False):
    """A handheld screen standing on its thick, rounded lower edge."""
    face = lambda u, v: (x + u, y - .12 * v, v)
    panel(s, rounded(0, 0, w, h, 5), face, 5.5 if tablet else 6.5)
    rect(s, face, 4, 7, w - 8, h - 16, 3.4, EDGE)
    s.line([face(w / 2 - 4, h - 4.7), face(w / 2 + 4, h - 4.7)], DETAIL)
    s.line([face(w / 2 - 5, 3.3), face(w / 2 + 5, 3.3)], DETAIL)
    return face


def shield_mark(s, face, x, z, size, ink=EDGE):
    """An engraved device-security emblem."""
    outline = [(0, .52), (.46, .35), (.43, -.04), (.29, -.29),
               (0, -.51), (-.29, -.29), (-.43, -.04), (-.46, .35), (0, .52)]
    s.line([face(x + u * size, z + v * size) for u, v in outline], ink)


def device_profile(s, face, x, z, scale=1):
    avatar_mark(s, face, x, z, scale)
    for d, w in ((-11, 18), (-16, 12)):
        s.line([face(x - w * scale / 2, z + d * scale),
                face(x + w * scale / 2, z + d * scale)], DETAIL)


def signature(s, face, x, z):
    """A single looping signature above its rule, with no letterforms."""
    s.line([face(x - 2, z), face(x + 30, z)], DETAIL)
    stroke = [(0, 2), (4, 4), (8, 9), (9, 12), (7, 12), (4, 8), (3, 4),
              (5, 2), (9, 3), (13, 7), (14, 5), (12, 3), (14, 2), (18, 4),
              (21, 7), (22, 6), (21, 3), (24, 4), (27, 5)]
    s.line([face(x + u, z + v) for u, v in stroke], EDGE)
    return x + 27, z + 5


def agreement(s, *, service=False):
    """Shared signed contract with a curled corner and a ruled signature."""
    face = folded_sheet(s, 61, 67, lean=.36, fold=12)
    if service:
        s.line([face(a, b) for a, b in oval(21, 46, 10, 10, 10, 170, 24)], EDGE)
        s.line([face(15, 46), face(27, 46)], DETAIL)
        s.line([face(21, 46), face(26, 53)], EDGE)
        s.line([face(35, 51), face(48, 51)], DETAIL)
        s.line([face(35, 45), face(46, 45)], DETAIL)
    else:
        s.line([face(9, 53), face(33, 53)], EDGE)
    for z, length in ((37, 41), (31, 37), (25, 42)):
        s.line([face(9, z), face(9 + length, z)], DETAIL)
    return face, signature(s, face, 11, 10)


def trust_padlock(s, *, open_shackle=False, keyway=True, shackle_height=18):
    """A compact padlock with a tubular shackle and a front keyway."""
    lift = 16 if open_shackle else 0
    arc = oval(24, 28 + lift, 15, shackle_height, 180, 36 if open_shackle else 0, 36)
    depth = 19 if open_shackle else 12
    shackle = [(9, depth, 23), *[(x, depth, z) for x, z in arc]]
    if not open_shackle:
        shackle.append((39, depth, 23))
    s.tube(shackle, 3.5)
    s.box(0, 0, 0, 48, 23, 27, 4.5)
    if keyway:
        face = lambda x, z: (x, 23, z)
        head = oval(24, 16, 3.6, 3.6, -43, 223, 24)
        contour = [*head, (22.2, 9), (25.8, 9), head[0]]
        s.line([face(x, z) for x, z in contour], EDGE)


def physical_key(s, point, scale=1):
    """One continuous key blank, with an open bow and two cut teeth."""
    bow = oval(0, 0, 8.5, 8.5, 24, 336, 36)
    contour = [*bow, (24, -3.45), (24, 3.45), (20, 3.45), (20, .1),
               (17, .1), (17, 3.45)]
    outline = [point(x * scale, z * scale) for x, z in contour]
    hole = [point(x * scale, z * scale)
            for x, z in oval(-1.2, 0, 3.25, 3.25, count=28)]
    s.face(outline, EDGE, openings=[hole])


def hardback(s, w, h, *, depth=11):
    """A closed standing binder with a bound spine and a narrow page block."""
    s.box(0, -depth, 0, w, 2, h, 1)
    s.box(2, -depth + 1, 2, w - 4, depth - 2, h - 4, 1.2)
    s.box(0, -2.2, 0, w, 2.2, h, 1)
    face = lambda x, z: (x, 0, z)
    s.line([face(7, 0), face(7, h)], EDGE)
    return face


def lens_outline(s, face, x, z, radius, ink=EDGE):
    s.line([face(u, v) for u, v in oval(x, z, radius, radius, count=48)], ink)


def recovery_key(s, state):
    """A thick metal key with its state tucked into the outer edge of the bow."""
    def point(u, v, offset=0):
        return .85 * v, u, 14 - .15 * u - .55 * v + offset

    physical_key(s, lambda u, v: point(u, v, -3.2), 2.05)
    physical_key(s, point, 2.05)
    badge(s, state, 12, -13, 19, 10)


def field_form(s):
    """A landscape clipboard with two labeled input fields."""
    face = clipboard(s, 68, 54)
    s.line([face(10, 35), face(26, 35)], EDGE)
    rect(s, face, 10, 22, 47, 9, 1.5, EDGE)
    s.line([face(10, 17), face(22, 17)], DETAIL)
    rect(s, face, 10, 7, 47, 6, 1, DETAIL)
    s.line([face(15, 10), face(34, 10)], DETAIL)
    return face


def field_dots(s, face):
    for x in (15, 21, 27, 33):
        s.line([face(x, 26.5), face(x + 1.3, 26.5)], EDGE)


def filing_form(s):
    """A folded-corner filing form with two fill-in rows and a signature."""
    face = folded_sheet(s, 57, 67, lean=.49, fold=12)
    s.line([face(9, 53), face(29, 53)], EDGE)
    for z, width in ((38, 33), (26, 38)):
        rect(s, face, 9, z, width, 7, 1, DETAIL)
        s.line([face(13, z + 3.5), face(25, z + 3.5)], DETAIL)
    signature(s, face, 10, 10)
    return face


def access_form(s):
    """A portrait clipboard with a large key heading."""
    face = clipboard(s, 51, 68)
    key_mark(s, face, 16, 44, 1, angle=11)
    return face


def security_token(s):
    """An upright fob with a lanyard eyelet and a masked code display."""
    face = lambda x, z: (x, -.25 * z, z)
    panel(s, rounded(0, 0, 39, 60, 13), face, 7)
    lens_outline(s, face, 19.5, 52, 3.4)
    rect(s, face, 6, 29, 27, 15, 2.3)
    for x in (11, 17, 23, 28):
        s.line([face(x, 35), face(x + 2, 35)], EDGE)
    lens_outline(s, face, 19.5, 16, 4.5, DETAIL)
    return face


def credential_rows(s, face, x, z, *, count=2):
    """Draw the username and masked-password inputs of a sign-in screen."""
    for row in range(count):
        bottom = z - row * 10
        rect(s, face, x, bottom, 25, 6, 1.4, DETAIL)
        if row == 0:
            s.line([face(x + 4, bottom + 3), face(x + 17, bottom + 3)], EDGE)
        else:
            for offset in (4, 8, 12, 16):
                s.line([face(x + offset, bottom + 3), face(x + offset + 1, bottom + 3)], EDGE)


def audit_sheet(s):
    """A standing log sheet with a punched binding margin and three ruled entries."""
    face = folded_sheet(s, 56, 69, lean=.36, fold=12)
    s.line([face(12, 7), face(12, 61)], DETAIL)
    s.line([face(19, 55), face(39, 55)], EDGE)
    for z in (13, 29, 45):
        lens_outline(s, face, 6, z - 3, 1.45, DETAIL)
        s.line([face(16, z - 6), face(49, z - 6)], DETAIL)
    return face


def dataset_table(s, *, selected=None):
    """A thick table with a heading band and three data rows."""
    s.box(0, 0, 0, 66, 13, 47, 3)
    face = lambda x, z: (x, 13, z)
    if selected is None:
        rect(s, face, 7, 7, 51, 33, 1.5)
    else:
        top = selected + 8
        for frame in (((7, selected), (7, 7), (58, 7), (58, selected)),
                      ((7, top), (7, 40), (58, 40), (58, top))):
            s.line([face(x, z) for x, z in frame], EDGE)
        rect(s, face, 4, selected, 57, 8, 1.1, EDGE)
    for z in (15, 23, 32):
        if selected is None or z not in (selected, selected + 8):
            s.line([face(7, z), face(58, z)], EDGE if z == 32 else DETAIL)
    for x in (25, 41):
        s.line([face(x, 7), face(x, 40)], DETAIL)
    for z in (11, 19, 27):
        for x, length in ((12, 6), (30, 5), (46, 5)):
            s.line([face(x, z), face(x + length, z)], DETAIL)
    return face


def parcel_mark(s, face, x, z, scale=1, *, broken=False):
    """A taped shipping box printed in a photo or source record."""
    def at(points, ink=EDGE):
        s.line([face(x + a * scale, z + b * scale) for a, b in points], ink)

    at([(-14, 6), (-1, 13), (14, 7), (14, -5), (0, -13), (-14, -6), (-14, 6),
        (0, -1), (14, 7)])
    at([(0, -1), (0, -13)])
    at([(-6, 10), (8, 4)])
    if broken:
        at([(8, 4), (5, 1), (9, -1), (6, -5)])
    else:
        at([(8, 4), (8, -3)])


def photo_print(s, x=0, y=0, z=0, *, width=62, height=48):
    """A standing picture print with a wide lower border."""
    face = lambda u, v: (x + u, y - .28 * v, z + v)
    panel(s, [(0, 0), (width, 0), (width, height), (0, height)], face, 2.6)
    rect(s, face, 5, 8, width - 10, height - 13, 1.5)
    return face


def policy_book(s, *, draft=False):
    """A standing policy binder with a ruled cover sheet."""
    face = hardback(s, 57, 67)
    if draft:
        border = rounded(11, 6, 41, 55, 2)
        s.line([face(x, z) for x, z in border + border[:1]], EDGE, dashed=True)
    s.line([face(16, 52), face(43, 52)], EDGE)
    return face


def tabbed_folder(s, x, y, z, scale=1):
    """A folder with a tabbed rear cover, paper edge, and front pocket."""
    def point(u, v, depth=0):
        return x + u * scale, y + depth * scale, z + v * scale

    back = [(0, 0), (41, 0), (41, 30), (20, 30), (16, 36), (2, 36), (0, 33)]
    s.face([point(u, v, -9) for u, v in back])
    s.face([point(u, v, -5) for u, v in ((3, 1), (38, 1), (38, 28), (3, 28))])
    s.face([point(41, 0, -9), point(41, 0), point(41, 23), point(41, 30, -9)])
    front = [(0, 0), (41, 0), (41, 22), (39, 24), (2, 24), (0, 22)]
    s.face([point(u, v) for u, v in front])
    return point


def printed_stroke(s, face, points, ink=DETAIL):
    s.line([face(x, z) for x, z in points], ink)


def currency_mark(s, face, x, z, radius, *, euro=False, ink=EDGE):
    """A dollar or euro sign engraved on an object face."""
    if euro:
        strokes = [
            oval(.2, 0, .72, .95, 53, 307, 28),
            [(-.76, .22), (.24, .22)],
            [(-.76, -.16), (.13, -.16)],
        ]
    else:
        strokes = [
            [(.56, .62), (.3, .78), (-.24, .78), (-.55, .59), (-.55, .27),
             (-.28, .08), (.31, -.08), (.55, -.28), (.55, -.57), (.25, -.77),
             (-.29, -.77), (-.58, -.61)],
            [(0, 1), (0, -1)],
        ]
    for points in strokes:
        printed_stroke(s, face, [(x + u * radius, z + v * radius) for u, v in points], ink)


def bank_mark(s, face, x, z, scale=1):
    """The outline of a pediment, columns, and foundation."""
    strokes = [
        [(-10, 3), (0, 9), (10, 3), (-10, 3)],
        [(-9, -5), (9, -5)],
        [(-11, -7.5), (11, -7.5)],
        *[[(u, 1.5), (u, -5)] for u in (-6, 0, 6)],
    ]
    for points in strokes:
        printed_stroke(s, face, [(x + u * scale, z + v * scale) for u, v in points], EDGE)


def payment_card(s, x=0, y=0, z=0, *, bank=False, back=False):
    """A rounded card with a chip or bank emblem on its exposed side."""
    face = lambda u, v: (x + u, y - .20 * v, z + v)
    panel(s, rounded(0, 0, 68, 43, 5), face, 4.5)
    if bank:
        bank_mark(s, face, 16, 27, .84)
    else:
        rect(s, face, 9, 21, 16, 12, 2)
        printed_stroke(s, face, [(9, 27), (14, 27), (14, 33)], DETAIL)
        printed_stroke(s, face, [(20, 21), (20, 27), (25, 27)], DETAIL)
    if back:
        printed_stroke(s, face, [(32, 33), (57, 33)], DETAIL)
    else:
        printed_stroke(s, face, [(9, 10), (23, 10)], DETAIL)
        printed_stroke(s, face, [(28, 10), (39, 10)], DETAIL)
    return face


def ruled_amounts(s, face, rows, x, right, *, width=12):
    """Align item strokes and shorter amount strokes in two columns."""
    for z, length in rows:
        printed_stroke(s, face, [(x, z), (x + length, z)])
        printed_stroke(s, face, [(right - width, z), (right, z)], EDGE)


def invoice(s, *, in_envelope=False, lift=0):
    """A folded-corner invoice with three item rows and a total rule."""
    if in_envelope:
        face = lambda x, z: (x + 13, -z * .35, z + 13 + lift)
        outline = [(0, -10), (52, -10), (52, 55), (43, 64), (0, 64)]
        panel(s, outline, face, 2)
        s.face([face(43, 64), face(43, 55), face(52, 55)], EDGE)
    else:
        face = folded_sheet(s, 54, 67, lean=.46, fold=11)
    printed_stroke(s, face, [(8, 56), (28, 56)], EDGE)
    ruled_amounts(s, face, ((45, 18), (36, 24), (27, 15)), 8, 44)
    printed_stroke(s, face, [(8, 20), (44, 20)], EDGE)
    return face


def money_coin(s, x, y, z, radius, *, euro=False):
    """A thick upright currency coin with an engraved rim."""
    coin(s, x, y, z, radius, depth=radius * .21)
    face = lambda u, v: (u, y + .02, v)
    lens_outline(s, face, x, z, radius * .81, DETAIL)
    currency_mark(s, face, x, z, radius * .54, euro=euro)


def tier_bars(s, face, x, z, heights):
    for i, height in enumerate(heights):
        rect(s, face, x + i * 9, z, 5.5, height, .7)


def billfold(s, *, note=True):
    """An upright leather billfold with an open slot and a snap strap."""
    s.box(0, 0, 0, 65, 14, 37, 4)
    if note:
        bill = lambda x, z: (x, 13 - .18 * (z - 35), z)
        panel(s, rounded(5, 21, 53, 34, 2), bill, 1.8)
        rect(s, bill, 9, 26, 45, 25, 1, DETAIL)
        currency_mark(s, bill, 30, 43, 6.3)
    s.box(0, 15, 0, 65, 9, 34, 4)
    front = lambda x, z: (x, 24, z)
    printed_stroke(s, front, [(4, 29), (52, 29)], DETAIL)
    panel(s, rounded(46, 14, 20, 12, 4), lambda x, z: (x, 25, z), 2)
    lens_outline(s, lambda x, z: (x, 25, z), 53, 20, 2.1, DETAIL)
    return front


def coin_stack(s, x, y, z, radius, count):
    for i in range(count):
        s.disk(x, y, z + i * 3.4, radius, radius, 3.4)
    top = z + count * 3.4
    s.ellipse(x, y, top, radius * .78, radius * .78, DETAIL)
    return top


def shared_cash_box(s):
    """An open cash box with matching coins on either side of its divider."""
    s.box(0, 0, 0, 67, 45, 5, 3)
    lid = lambda x, z: (x, -.38 * (z - 12), z)
    panel(s, rounded(0, 12, 67, 39, 3), lid, 4)
    rect(s, lid, 5, 17, 57, 29, 2, DETAIL)
    s.box(0, 0, 4, 4, 45, 11, 1)
    coin_stack(s, 16, 26, 5, 9, 4)
    coin_stack(s, 49, 26, 5, 9, 4)
    s.box(31, 4, 5, 3, 37, 9, 1)
    s.box(63, 0, 4, 4, 45, 11, 1)
    s.box(0, 41, 4, 67, 4, 11, 1.5)
    s.box(26, 45, 6, 15, 2.8, 6, 1.8)


def card_terminal(s, *, report=False, cash=False):
    """A sloped countertop reader with a keypad and an integrated printer slot."""
    upper = lambda x, y: (x, y, 19 - .21 * y)
    s.box(0, 0, 0, 48, 62, 6.5, 4)
    s.face([(48, 0, 4), (48, 62, 4), upper(48, 62), upper(48, 0)])
    s.face([(0, 62, 4), (48, 62, 4), upper(48, 62), upper(0, 62)])
    s.face([upper(x, y) for x, y in rounded(0, 0, 48, 62, 3)])
    rect(s, upper, 7, 10, 34, 17, 2, EDGE)
    if cash:
        currency_mark(s, upper, 24, 18.5, 6, ink=BOLD)
    else:
        printed_stroke(s, upper, [(13, 17), (33, 17)], DETAIL)
    for y in (34, 42, 50):
        for x in (11, 21, 31):
            rect(s, upper, x, y, 6, 4.3, 1.3, DETAIL)
    s.line([upper(11, 57), upper(37, 57)], EDGE)
    if report:
        face = lambda x, z: (x, 5 - .38 * z, upper(0, 5)[2] + z)
        teeth = [(x, 42 if i % 2 == 0 else 39)
                 for i, x in enumerate(range(42, 5, -4))]
        s.face([face(x, z) for x, z in [(6, 0), (42, 0), *teeth]], EDGE)
        printed_stroke(s, face, [(11, 33), (25, 33)], EDGE)
        ruled_amounts(s, face, ((25, 10), (18, 13), (11, 8)), 11, 37, width=7)
        s.line([face(5, 0), face(43, 0)], EDGE)
    return upper


def subscription_control(s, *, settings=False):
    """A standing recurring-payment controller with a dial and switch bank."""
    face = lambda x, z: (x, -z * .22, z)
    panel(s, rounded(0, 0, 79, 52, 6), face, 14)
    coin(s, 24, face(24, 27)[1] + 5, 27, 16, depth=5)
    glyph(s, "refresh", 24, face(24, 27)[1] + 5, 27, 15, EDGE)
    currency_mark(s, face, 58, 36, 7, ink=EDGE)
    if settings:
        for z, knob in ((22, 56), (12, 64)):
            rect(s, face, 45, z - 3.5, 26, 7, 3.5, DETAIL)
            lens_outline(s, face, knob, z, 2.9, EDGE)
    else:
        printed_stroke(s, face, [(49, 20), (66, 20)], DETAIL)
    return face


def invoice_total(s, face, *, x=23, z=10, end=44, ink=BOLD):
    currency_mark(s, face, x, z, 5.5, ink=ink)
    printed_stroke(s, face, [(x + 8, z), (end, z)], ink)


def folder_with_insert(s, insert, *, width=72, height=37):
    """Draw the rear cover, insert, and front pocket in depth order."""
    back = lambda x, z: (x, -13, z)
    front = lambda x, z: (x, 1, z)
    shape = [(0, 0), (width, 0), (width, height + 5), (31, height + 5),
             (26, height + 15), (4, height + 15), (0, height + 10)]
    s.face([back(x, z) for x, z in shape])
    insert()
    s.face([back(width, 0), back(width, height + 5),
            front(width, height - 2), front(width, 0)])
    s.face([front(x, z) for x, z in [(0, 0), (width, 0),
                                    (width, height - 2), (width - 3, height),
                                    (3, height), (0, height - 2)]])
    return front


def open_ledger(s):
    """A thick accounting book stands open on the lower edge of its covers."""
    def left(x, y):
        return x, (y - 62) * .40 - x * .30, (62 - y) * .88

    def right(x, y):
        return x, (y - 62) * .40 - (84 - x) * .30, (62 - y) * .88

    for start, end, page in ((0, 42, left), (42, 84, right)):
        corners = [(start, 0), (end, 0), (end, 62), (start, 62)]
        cover = [(x, y - 7, z) for x, y, z in (page(x, y) for x, y in corners)]
        s.face(cover)
        inset = [(start + (2 if start == 0 else 0), 2),
                 (end - (2 if end == 84 else 0), 2),
                 (end - (2 if end == 84 else 0), 60),
                 (start + (2 if start == 0 else 0), 60)]
        sheet = [page(x, y) for x, y in inset]
        rear = [(x, y - 5.5, z) for x, y, z in sheet]
        s.face([sheet[0], sheet[1], rear[1], rear[0]], EDGE)
        if end == 84:
            s.face([sheet[1], sheet[2], rear[2], rear[1]], EDGE)
        s.face(sheet, EDGE)
    return left, right


def ledger_rows(s, page, x, *, rows=(21, 28, 35)):
    printed_stroke(s, page, [(x + 19, 15), (x + 19, 42)], DETAIL)
    for y in rows:
        printed_stroke(s, page, [(x, y), (x + 14, y)], DETAIL)
        printed_stroke(s, page, [(x + 23, y), (x + 30, y)], EDGE)


def calendar_header(s, face, x, z, scale=1):
    rect(s, face, x, z, 16 * scale, 12 * scale, 1.3 * scale)
    printed_stroke(s, face, [(x, z + 7 * scale), (x + 16 * scale, z + 7 * scale)], DETAIL)
    for offset in (4, 12):
        printed_stroke(s, face, [(x + offset * scale, z + 9 * scale),
                                  (x + offset * scale, z + 15 * scale)], EDGE)


def receipt_face(s):
    """A continuous receipt stands on its curled foot."""
    face = lambda x, z: (x, -.38 * (z - 9), z)
    teeth = [(x, 71 if i % 2 == 0 else 67)
             for i, x in enumerate(range(56, -1, -7))]
    s.face([face(x, z) for x, z in [(0, 9), (56, 9), *teeth]])
    roll = oval(6.2, 6, 6.9, 6, count=42)
    hull = MultiPoint([project((x, y, z)) for x in (0, 56) for y, z in roll]).convex_hull
    s.layers.append((hull.boundary, hull, EDGE))
    s.line([(56, y, z) for y, z in roll], EDGE)
    s.line([(56, y, z) for y, z in oval(6.2, 6, 4.1, 3.4, 45, 328, 28)], DETAIL)
    return face


def receipt_total(s, face, z, *, right=47, ink=BOLD):
    currency_mark(s, face, right - 21, z, 4.8, ink=ink)
    printed_stroke(s, face, [(right - 13, z), (right, z)], EDGE)


def expense_receipt(s):
    face = receipt_face(s)
    printed_stroke(s, face, [(8, 57), (30, 57)], EDGE)
    ruled_amounts(s, face, ((44, 16), (35, 23), (26, 14)), 8, 47)
    printed_stroke(s, face, [(8, 21), (46, 21)], EDGE)
    receipt_total(s, face, 15, right=44, ink=EDGE)
    return face


def cutlery(s, face, x, z, scale=1, ink=EDGE):
    """Draw a fork on the left and a table knife on the right."""
    strokes = [
        [(-7, 7), (-7, 3), (-5, 1), (-3, 3), (-3, 7)],
        [(-5, 7), (-5, -7)],
        [(5, -7), (5, 7), (7, 5), (7, 0), (5, 0)],
    ]
    for stroke in strokes:
        printed_stroke(s, face, [(x + u * scale, z + v * scale) for u, v in stroke], ink)


def place_setting(s, face, x, z, radius, *, utensils=True):
    for factor, ink in ((1, EDGE), (.69, DETAIL)):
        printed_stroke(s, face, oval(x, z, radius * factor, radius * factor, count=36), ink)
    if utensils:
        scale = radius / 8
        for stroke in (
            [(-14, 7), (-14, 3), (-12, 1), (-10, 3), (-10, 7)],
            [(-12, 7), (-12, -7)],
            [(12, -7), (12, 7), (14, 5), (14, 0), (12, 0)],
        ):
            printed_stroke(s, face, [(x + u * scale, z + v * scale) for u, v in stroke], EDGE)


def cloche_mark(s, face, x, z, scale=1):
    printed_stroke(s, face, oval(x, z, 9 * scale, 6 * scale, 0, 180, 24), EDGE)
    printed_stroke(s, face, [(x - 11 * scale, z), (x + 11 * scale, z)], EDGE)
    printed_stroke(s, face, [(x, z + 6 * scale), (x, z + 8.5 * scale)], EDGE)


def course_rows(s, face, x, z, widths, *, prices=False):
    for i, width in enumerate(widths):
        row = z - i * 9
        printed_stroke(s, face, [(x, row), (x + width, row)], EDGE)
        if prices:
            printed_stroke(s, face, [(x + 27, row), (x + 33, row)], EDGE)


def food_bag_shell(s, width, depth, height, *, open_top=False):
    """A gusseted takeaway bag or an open, reinforced thermal bag."""
    front = lambda x, z: (x, depth - .08 * (height - z), z)
    back = lambda x, z: (x, .08 * (height - z), z)
    inset = 3 if open_top else 5
    s.face([back(inset, 0), back(width - inset, 0), back(width, height), back(0, height)])
    s.face([back(inset, 0), front(inset, 0), front(0, height), back(0, height)])
    s.face([back(inset, 0), back(width - inset, 0), front(width - inset, 0), front(inset, 0)], DETAIL)
    s.face([back(width - inset, 0), front(width - inset, 0), front(width, height), back(width, height)])
    if open_top:
        printed_stroke(s, back, [(1, height - 4), (width - 1, height - 4)], DETAIL)
    else:
        printed_stroke(s, lambda y, z: (width - inset * (1 - z / height), y, z),
                       [(depth * .5, 3), (depth * .5, height - 1)], DETAIL)
    s.face([front(inset, 0), front(width - inset, 0), front(width, height), front(0, height)])
    return front


def apple_mark(s, face, x, z, scale=1, ink=EDGE):
    body = [(0, 5), (-3, 6.5), (-6, 6.2), (-8, 3.3), (-8, -.2), (-6.2, -4.5),
            (-3.5, -7), (0, -6), (3.7, -7), (6.4, -4.6), (8.1, -.5), (8, 3.2),
            (6.4, 6.1), (3.3, 6.4), (0, 5)]
    stem = [(0, 5), (0, 8), (-1.4, 10)]
    leaf = [(0, 7), (1.6, 10), (5, 11), (4, 8.5), (0, 7)]
    for outline in (body, stem, leaf):
        printed_stroke(s, face, [(x + u * scale, z + v * scale) for u, v in outline], ink)


def bound_planner(s, width, height, *, desk=False):
    """A ring-bound planner on a desk stand or on the edge of its thick backing."""
    slope = .41 if desk else .72
    face = lambda x, z: (x, 13 - slope * z, z)
    rim = rounded(0, 0, width, height, 2)
    if desk:
        rear = [(0, -32, 0), (width, -32, 0)]
        s.face([*rear, face(width, height), face(0, height)], DETAIL)
        s.face([rear[1], face(width, 0), face(width, height)])
    else:
        panel(s, rounded(-1, 0, width + 2, height - 1, 3), face, 8)
    panel(s, rim, face, 2.6)
    for x in (width * .19, width * .81):
        _, y, z = face(x, height)
        s.tube([(x, y - 2.5, z - 3), (x, y - 4, z + 1), (x, y - 1, z + 4),
                (x, y + 3, z + 3), (x, y + 5, z - 2)], 1.15)
    return face


def calendar_grid(s, face, x, z, step_x, step_z, columns, rows):
    rect(s, face, x, z, step_x * columns, step_z * rows, .5, EDGE)
    for col in range(1, columns):
        u = x + col * step_x
        printed_stroke(s, face, [(u, z), (u, z + step_z * rows)], DETAIL)
    for row in range(1, rows):
        v = z + row * step_z
        printed_stroke(s, face, [(x, v), (x + step_x * columns, v)], DETAIL)


def handled_food_bag(s, x=0, y=0, z=0, *, scale=1, emblem=True):
    """Set the shared takeaway bag on a surface without changing its proportions."""
    bag = Scene()
    bag.tube([(13, 4, 43), (13, 4, 52), (17, 4, 57),
              (27, 4, 57), (31, 4, 52), (31, 4, 43)], 1.25, DETAIL)
    front = food_bag_shell(bag, 44, 23, 45)
    bag.tube([(13, 22, 41), (13, 22, 51), (17, 22, 56),
              (27, 22, 56), (31, 22, 51), (31, 22, 41)], 1.5)
    printed_stroke(bag, front, [(4, 6), (40, 6)], DETAIL)
    if emblem:
        cloche_mark(bag, front, 20.5, 17.5, .9)
    place_scene(s, bag, x, y, z, scale)


def place_scene(s, part, x, y, z, scale):
    """Scale and translate the projected geometry of a reusable object."""
    u, v = project((x, y, z))
    transform = (scale, 0, 0, scale, u, v)
    for path, cover, ink in part.layers:
        s.layers.append((affine_transform(path, transform),
                         affine_transform(cover, transform) if cover is not None else None, ink))


def food_speech(s, x, y, z, *, question=False):
    """A speech balloon with its tail directed down toward the subject."""
    face = lambda u, v: (x + u, y, z + v)
    shape = [(-12, 0), (-15, 3), (-15, 15), (-12, 18), (12, 18),
             (15, 15), (15, 3), (12, 0), (0, 0), (-9, -7), (-8, 0)]
    s.face([face(u, v) for u, v in shape])
    if question:
        printed_stroke(s, face, [(-4, 11), (-3, 14), (1, 15), (4, 13),
                                 (4, 11), (0, 8), (0, 6)], BOLD)
        s.line([face(0, 3), face(0, 2.2)], BOLD)
    else:
        for u in (-6, 0, 6):
            s.line([face(u - .65, 9), face(u + .65, 9)], BOLD)


def seedling(s, x, y, z, height):
    """A stem and two paired leaves facing the viewer."""
    def point(u, v):
        return (x + u, y, z + v)

    s.line([point(0, 0), point(0, height * .8)], EDGE)
    for direction, level in ((-1, .50), (1, .80)):
        leaf = [(0, 0), (2, 4), (6, 7), (11, 8), (10, 4), (7, 1), (4, -.6)]
        s.face([point(direction * u * height / 23, level * height + v * height / 23)
                for u, v in leaf])


def crop_furrow(s):
    """A single raised crop row that leaves room alongside for a route or sensor."""
    s.solid(rounded(0, 2, 69, 23, 8), 0, 4, top=rounded(2, 4, 65, 19, 7), crease=False)
    s.line([(6, 19, 4), (62, 19, 4)], DETAIL)
    for x, h in ((12, 23), (33, 25), (54, 23)):
        seedling(s, x, 12, 4, h)


def dining_table(s, *, picnic=False):
    """A thick tabletop on four legs, with fixed seats on the picnic variant."""
    if picnic:
        for x in (10, 57):
            for y, offset in ((-3, 15), (48, -15)):
                s.face([(x, y, 0), (x, y+5, 0),
                        (x, y+offset+5, 29), (x, y+offset, 29)])
            s.box(x-3, -7, 12, 6, 62, 4, 1)
        for y in (-9, 45):
            s.box(1, y, 15, 68, 10, 4, 2)
    else:
        for x, y in ((7, 6), (57, 6), (7, 35), (57, 35)):
            s.box(x, y, 0, 5, 5, 29, 1)
    s.box(1, 1, 28, 68, 45, 5, 3)


def cupboard_shell(s, width, depth, height, *, shelves=()):
    """An open-front cabinet with a back and optionally fixed horizontal shelves."""
    s.box(0, 0, 0, width, 4, height, 1)
    s.box(0, 3, 0, 4, depth - 3, height, 1)
    for z in (0, *shelves):
        s.box(3, 3, z, width - 6, depth - 3, 3, 1)


def cupboard_trim(s, width, depth, height):
    s.box(width - 4, 3, 0, 4, depth - 3, height, 1)
    s.box(0, 0, height - 3, width, depth, 3, 1)


def pantry_jar(s, x, y, z, radius, height, *, label=False):
    shoulder = oval(x, y, radius, radius)[:-1]
    lid = oval(x, y, radius * .81, radius * .81)[:-1]
    s.solid(shoulder, z, height - 7, crease=False)
    s.solid(shoulder, z + height - 7, 4, top=lid, crease=False)
    s.disk(x, y, z + height - 3, radius * .86, radius * .86, 4)
    if label:
        def band(a0, a1, at):
            return [(u, v, at) for u, v in oval(x, y, radius, radius, a0, a1, 20)]

        top = band(0, 90, z + (height - 7) * .85)
        bottom = band(0, 90, z + (height - 7) * .18)
        s.face(top + bottom[::-1])
        s.line(band(20, 72, z + (height - 7) * .65), EDGE)
        s.line(band(24, 56, z + (height - 7) * .38), DETAIL)


def harvest_crate(s, x=0, y=0, z=0, *, scale=1):
    """An open wooden produce crate with fruit nestled behind the front slat."""
    part = Scene()
    part.box(0, 0, 0, 59, 34, 4, 2)
    part.box(0, 0, 4, 59, 4, 18, 1)
    part.box(0, 3, 4, 4, 30, 18, 1)
    for a, b, r in ((13, 12, 9), (30, 10, 8), (46, 13, 9), (21, 23, 9), (40, 22, 9)):
        part.solid(oval(a, b, r, r)[:-1], 12, 10,
                   top=oval(a, b, r * .90, r * .90)[:-1], crease=False)
        part.solid(oval(a, b, r * .90, r * .90)[:-1], 22, 4,
                   top=oval(a, b, r * .55, r * .55)[:-1], crease=False)
        part.line([(a, b, 26), (a+1, b, 30), (a+4, b, 31)], EDGE)
    part.box(55, 3, 4, 4, 31, 18, 1)
    part.box(0, 30, 4, 59, 4, 18, 1)
    part.line([(3, 34, 9), (56, 34, 9)], DETAIL)
    part.line([(3, 34, 19), (56, 34, 19)], DETAIL)
    place_scene(s, part, x, y, z, scale)


def food_loupe(s, x, y, z, radius, *, handle_y=-.35, handle_start=.81):
    """A transparent, tilted magnifying lens above the sample."""
    def point(a, b):
        return a, b, z - .48 * (b - y)

    def rim(r):
        return [point(a, b) for a, b in oval(x, y, r, r, count=48)[:-1]]

    s.tube([point(x + handle_start * radius, y + .44 * handle_y * radius),
            point(x + 1.85 * radius, y + handle_y * radius)], radius * .13)
    s.face(rim(radius), openings=[rim(radius * .85)])


def pipe_section(s, start, end, y, z, radius, *, bore=0):
    """Draw a pipe or coupling along the x axis, with its circular end visible."""
    rim = oval(y, z, radius, radius, count=44)[:-1]
    front = Polygon([project((end, a, b)) for a, b in rim])
    hull = MultiPoint([project((x, a, b)) for x in (start, end) for a, b in rim]).convex_hull
    s.layers.append((hull.boundary.union(front.boundary), hull, EDGE))
    if bore:
        s.line([(end, a, b) for a, b in oval(y, z, bore, bore, count=32)], DETAIL)


def smooth_loop(points, steps=6):
    """Sample a closed Catmull–Rom spline through silhouette landmarks."""
    result = []
    for i, _ in enumerate(points):
        a, b, c, d = (points[j % len(points)] for j in range(i - 1, i + 3))
        for j in range(steps):
            t = j / steps
            result.append(tuple(
                .5 * (2*v + (-u+w)*t + (2*u-5*v+4*w-q)*t*t
                      + (-u+3*v-3*w+q)*t*t*t)
                for u, v, w, q in zip(a, b, c, d)
            ))
    return result


def clamshell(s, x=0, y=0, *, scale=1, opened=False):
    """A molded single-serving container with its hinge along the rear edge."""
    part = Scene()
    if opened:
        lid = lambda u, v: (u, 2 - .38*v, 12 + v)
        panel(part, rounded(0, 0, 48, 28, 5), lid, 2.5)
        rect(part, lid, 5, 4, 38, 20, 4, DETAIL)
    part.solid(rounded(4, 4, 40, 25, 5), 0, 10,
               top=rounded(0, 0, 48, 34, 5), crease=False)
    part.box(0, 0, 10, 48, 34, 2.8, 4)
    if opened:
        part.disk(14, 15, 13, 7, 8, 3)
        part.ellipse(14, 15, 16, 4, 4.5, DETAIL, 25, 215)
        for u, v in ((27, 10), (34, 13), (32, 22)):
            part.disk(u, v, 13, 4, 3, 2)
    else:
        part.solid(rounded(0, 0, 48, 34, 5), 13, 9,
                   top=rounded(4, 4, 40, 25, 5), crease=False)
        part.face([(a, b, 22) for a, b in rounded(4, 4, 40, 25, 5)], DETAIL)
        for v in (10, 16, 22):
            part.line([(10, v, 22), (38, v, 22)], DETAIL)
    part.box(16, 33, 8.5, 16, 4, 4.5, 1.25)
    place_scene(s, part, x, y, 0, scale)


def food_table(s, x=0, y=0, *, scale=1, parasol=False):
    """A dining table with two place settings and an optional center umbrella."""
    part = Scene()
    if parasol:
        part.tube([(34, 23, 0), (34, 23, 29)], 1.8)
        part.disk(34, 23, 0, 7, 7, 2.5)
    dining_table(part)
    top = lambda u, v: (u, v, 33)
    for u, v in ((17, 29), (52, 29)):
        place_setting(part, top, u, v, 7.1)
    if parasol:
        part.tube([(34, 23, 33), (34, 23, 76)], 1.75)
        ribs = [(u, v, 68) for u, v in oval(34, 23, 37, 31, 0, 315, 7)]
        peak = (34, 23, 88)
        # Fan-shaped gores rise to the cap, with the near ribs defining the canopy.
        for a, b in sorted(zip(ribs, ribs[1:] + ribs[:1]),
                           key=lambda pair: sum(p[0]+p[1] for p in pair)):
            part.face([peak, a, b])
        part.tube([peak, (34, 23, 91)], 1.45)
    place_scene(s, part, x, y, 0, scale)


def sealed_delivery_envelope(s):
    """A sealed envelope on its lower edge with a printed delivery label."""
    face = lambda x, z: (x, -.66*z, z)
    panel(s, rounded(0, 0, 70, 43, 3), face, 4.4)
    printed_stroke(s, face, [(2, 41), (29, 24.5), (34, 23),
                             (39, 24.5), (68, 41)], EDGE)
    for points in ([(2, 3), (23, 19)], [(68, 3), (52, 15)]):
        printed_stroke(s, face, points, DETAIL)
    rect(s, face, 24, 6, 24, 11, 1, DETAIL)
    for z, end in ((13.5, 44.5), (9.5, 39)):
        printed_stroke(s, face, [(27, z), (end, z)], EDGE)


def zip_file(s):
    """An upright archive file with a visible pull and spaced zipper teeth."""
    face = folded_sheet(s, 55, 65, lean=.61)
    rect(s, face, 28, 41, 8, 11, 2)
    rect(s, face, 30, 34, 4, 10, 1.2)
    for z in (12, 17, 22, 27, 32):
        s.line([face(32, z), face(37, z)], EDGE)
        s.line([face(27, z + 2.5), face(32, z + 2.5)], EDGE)
    s.line([face(32, 11), face(32, 34)], DETAIL)
    s.line([face(32, 52), face(32, 63)], EDGE)
    return face


def ruled_file(s):
    face = folded_sheet(s, 48, 54, lean=.56, fold=11)
    for z, end in ((38, 30), (29, 37), (20, 33)):
        printed_stroke(s, face, [(9, z), (end, z)], DETAIL)
    return face


def inbox_base(s):
    """The rear wall and floor of an inbox tray, before the contents go in."""
    s.box(0, 0, 0, 63, 40, 4, 2)
    s.box(1, 1, 4, 61, 3, 14, 1)


def inbox_front(s):
    """Finish an inbox tray with raised sides and a center finger notch."""
    s.face([(0, 1, 3), (0, 40, 3), (0, 40, 15), (0, 1, 18)])
    s.face([(63, 1, 3), (63, 40, 3), (63, 40, 15), (63, 1, 18)])
    s.face([(0, 40, 3), (63, 40, 3), (63, 40, 15), (43, 40, 15),
            (38, 40, 9), (25, 40, 9), (20, 40, 15), (0, 40, 15)])


def basket_apple(s, x, y, z, size):
    """A lobed apple with a short stem and leaf, nested among other produce."""
    shape = smooth_loop([(0, .67), (-.45, .81), (-.79, .64), (-.94, .2),
                         (-.77, -.32), (-.4, -.76), (0, -.73),
                         (.36, -.77), (.73, -.38), (.93, .14), (.79, .61),
                         (.43, .8)])
    face = lambda u, v: (x + u*size, y - .29*v*size, z + v*size)
    points = [face(u, v) for u, v in shape]
    s.face(points)
    s.tube([face(0, .68), face(-.06, 1.02)], size*.066)
    leaf = [(0, .86), (.25, 1.1), (.57, 1.13), (.4, .93), (.22, .87)]
    s.face([face(u, v) for u, v in smooth_loop(leaf)])
