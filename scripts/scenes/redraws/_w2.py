"""Shared objects and chart primitives for the data and workflow redraws."""

from math import dist, pi, sin, sqrt

from shapely.geometry import LineString, MultiPoint, Polygon
from shapely.ops import unary_union

from geometry import BOLD, DETAIL, EDGE, oval, project, rounded
from scenes.redraws._kit import arrow, badge, glyph


def card(s, width, height, *, radius=5, depth=3):
    """Draw a card whose visible face is at y=0."""
    front = [(x, 0, z) for x, z in rounded(0, 0, width, height, radius)]
    back = [(x, -depth, z) for x, _, z in front]
    hull = MultiPoint([project(point) for point in front + back]).convex_hull
    s.layers.append((hull.boundary, hull, EDGE))
    s.line(front + front[:1], EDGE)


def outline(s, x, y, z, width, height, radius=3, ink=DETAIL):
    points = [(u, y, v) for u, v in rounded(x, z, width, height, radius)]
    s.line(points + points[:1], ink)


def magnifier(s, x, y, z, radius, *, direction=(.8, -.6)):
    """Draw a magnifier with an opening that leaves inspected lines visible."""
    dx, dz = direction
    s.tube(
        [(x + length*dx, y, z + length*dz) for length in (radius + 1.75, radius + 15)],
        2.6,
        EDGE,
    )
    rim = [(u, y, v) for u, v in oval(x, z, radius, radius)]
    opening = [(u, y, v) for u, v in oval(x, z, radius - 3, radius - 3)]
    ring = Polygon(list(map(project, rim)), [list(map(project, opening))])
    s.layers.append((ring.exterior, ring, BOLD))
    s.line(opening, DETAIL)


def variant(s, name, x, y, z, size, ink=EDGE, *, flat=False):
    """Trace an A or B variant on the face or the top of a tile."""
    def stroke(points):
        if flat:
            s.line([(x + u*size, y - v*size, z) for u, v in points], ink)
        else:
            s.line([(x + u*size, y, z + v*size) for u, v in points], ink)

    if name == "A":
        stroke([(-.36, 0), (0, 1), (.36, 0)])
        stroke([(-.23, .34), (.23, .34)])
    else:
        stroke([(-.3, 0), (-.3, 1), (.04, 1), (.22, .94), (.30, .81),
                (.30, .68), (.21, .55), (.04, .50), (-.3, .50)])
        stroke([(.04, .50), (.24, .44), (.34, .31), (.34, .17),
                (.24, .05), (.06, 0), (-.3, 0)])



def plan_magnifier(s, x, y, z, radius, *, direction):
    """An open magnifier held parallel to the inspected step's top face."""
    dx, dy = direction
    s.tube([(x + length*dx, y + length*dy, z) for length in (radius - 1, radius + 20)],
           2.7, EDGE)
    rim = [(u, v, z) for u, v in oval(x, y, radius, radius)]
    opening = [(u, v, z) for u, v in oval(x, y, radius - 3, radius - 3)]
    s.face(rim, BOLD, openings=(opening,))


def board(s, width, height, *, run=.18, rise=1, depth=8, base=0, level=False):
    """A solid chart board with a sloped face and a foot that sits flat."""
    def point(x, v):
        if level:
            return x / 2, -x / 2 - v * run, base + 4 + v * rise
        return x, -v * run, base + 4 + v * rise

    front = [point(0, 0), point(width, 0), point(width, height), point(0, height)]
    back = [(x, y - depth, z) for x, y, z in front[2:]]
    feet = [(x, y, base) for x, y, _ in back]
    toes = [(x, y, base) for x, y, _ in front[:2]]
    hull = MultiPoint([project(p) for p in front + back + feet + toes]).convex_hull
    s.layers.append((hull.boundary, hull, EDGE))
    s.line(front + front[:1], EDGE)
    s.line([front[1], toes[1]], EDGE)
    return point


def axes(s, point, *, x=12, y=12, width=98, height=54):
    s.line([point(x, y + height), point(x, y), point(x + width, y)], EDGE)
    for tick in (width / 4, width / 2, width * 3 / 4):
        s.line([point(x + tick, y), point(x + tick, y - 3)], DETAIL)


def chart_line(s, point, points, ink=BOLD, *, dash=None):
    """Trace a chart series with optional long, clearly separated dashes."""
    vertices = [point(x, v) for x, v in points]
    if dash is None:
        s.line(vertices, ink)
        return
    on, off = dash
    period = on + off
    phase = 0
    for start, end in zip(vertices, vertices[1:]):
        length = dist(project(start), project(end))
        if not length:
            continue
        offset = -phase
        while offset < length:
            lo, hi = max(0, offset), min(length, offset + on)
            if hi > lo:
                s.line([tuple(a + (b - a) * t / length for a, b in zip(start, end))
                        for t in (lo, hi)], ink)
            offset += period
        phase = (phase + length) % period


def chart_marker(s, point, x, v, radius=2.8, ink=EDGE):
    s.face([point(u, k) for u, k in oval(x, v, radius, radius, count=24)], ink)


def currency(s, point, x, v, size, ink=EDGE):
    """A dollar-shaped currency mark drawn directly on the chart."""
    stroke = [(5, 4), (2, 6), (-2, 6), (-5, 4), (-5, 2), (-3, .7),
              (3, -.7), (5, -2), (5, -4), (2, -6), (-2, -6), (-5, -4)]
    s.line([point(x + u * size, v + k * size) for u, k in stroke], ink)
    s.line([point(x, v + 8 * size), point(x, v - 8 * size)], ink)


def database(s, z, radius, height):
    """The three-tier database used in data transfers and diagrams."""
    s.solid(oval(0, 0, radius, radius)[:-1], z, height, crease=False)
    s.ellipse(0, 0, z + height, radius, radius, EDGE)
    for tier in (1, 2):
        s.ellipse(0, 0, z + tier*height/3, radius, radius, EDGE, start=-45, end=135)


def database_transfer(s, *, inbound):
    """The same three-tier database with a single reversible side arrow."""
    radius = 34
    database(s, 0, radius, 60)
    side = radius / sqrt(2)
    path = [(side + 4, -side - 4, 31), (side + 31, -side - 31, 31)]
    arrow(s, path[::-1] if inbound else path, BOLD, head=11)


def funnel(s):
    """One tapered funnel with a rolled mouth and a short outlet."""
    s.solid(oval(0, 0, 8, 8)[:-1], 0, 17, crease=False)
    s.solid(oval(0, 0, 8, 8)[:-1], 17, 43, top=oval(0, 0, 38, 38)[:-1],
            crease=False)
    s.ellipse(0, 0, 60, 38, 38, EDGE)
    s.ellipse(0, 0, 60, 34, 34, DETAIL)


def sampling_unit(s, x, y, z, *, selected):
    if selected:
        s.disk(x, y, z, 5.2, 5.2, 4, BOLD)
        s.ellipse(x, y, z + 4, 2.35, 2.35, EDGE)
    else:
        s.ellipse(x, y, z, 5.2, 5.2, DETAIL)


def paper(s, x, y, z, width, depth, *, fold=0, ink=EDGE):
    """A flat sheet with a visible edge and an optional folded corner."""
    corners = [(x, y), (x + width - fold, y)]
    if fold:
        corners.append((x + width, y + fold))
    corners.extend([(x + width, y + depth), (x, y + depth)])
    s.solid(corners, z, 1.8, ink=ink, crease=False)
    top = z + 1.8
    s.line([(u, v, top) for u, v in [*corners, corners[0]]], ink)
    if fold:
        s.line([(x + width - fold, y, top), (x + width - fold, y + fold, top),
                (x + width, y + fold, top)], DETAIL)
    return top


def clipboard(s):
    """A top-reading survey sheet on a low, clipped backing board."""
    s.box(0, 0, 0, 92, 99, 5, 5)
    top = paper(s, 6, 7, 5, 80, 85)
    s.box(29, 0, 5, 34, 13, 7, 4)
    s.line([(37, 7, 12), (55, 7, 12)], DETAIL)
    s.line([(16, 22, top), (53, 22, top)], EDGE)
    return top


def level_face(x, z, y=0):
    """Map horizontal diagram coordinates to a viewer-level vertical plane."""
    return (x * .5, y - x * .5, z)


def laptop(s, width=112, height=67):
    """An open laptop with a large screen and room for a diagram."""
    s.box(0, -6, 4, width, 6, height + 4, 4)
    s.box(0, 0, 0, width, 31, 4, 4)
    for inset in (9, 15):
        s.line([(10, inset, 4), (width - 10, inset, 4)], DETAIL)
    footprint = [(width*.38, 20, 4), (width*.62, 20, 4),
                 (width*.62, 27, 4), (width*.38, 27, 4)]
    s.line(footprint + footprint[:1], DETAIL)
    outline(s, 5, 0, 9, width - 10, height - 5, 3)
    return lambda x, z: (x, 0, z)


def pack(s, x, y, z, width, depth, height=11):
    """A grounded stack of bound pages with a folded-corner cover."""
    s.box(x, y, z, width, depth, height, 3)
    s.line([(x + 4, y + depth, z + height*.46),
            (x + width - 3, y + depth, z + height*.46)], DETAIL)
    top = paper(s, x, y, z + height, width, depth, fold=12)
    s.line([(x + 9, y + 16, top), (x + width*.58, y + 16, top)], EDGE)
    return top


def plot_point(x, z):
    """An open chart face turned slightly off the viewer."""
    return (x * .65, -x * .35, z)


def rule(s, point, x, z, length, ink=DETAIL):
    s.line([point(x, z), point(x + length, z)], ink)


def response_curve():
    """Cumulative adoption with a quiet lead-in and a clear plateau."""
    return [(0, 0), (19, 0), (30, 1), (41, 4), (50, 10), (58, 22),
            (65, 38), (73, 52), (83, 59), (96, 62), (108, 62)]


def grid_table(s, *, preview=False):
    """A thick, freestanding data-table body and its ruled cells."""
    def point(x, z):
        return x, 0, z

    width, height = 103, 74
    s.box(0, -18, 0, width, 18, height, 4)
    for z in (19, 35, 51, 64):
        rule(s, point, 9, z, 85)
    for x in (35, 64):
        s.line([(x, 0, 9), (x, 0, 64)], DETAIL)
    for x, length in ((15, 11), (44, 10), (72, 12)):
        s.line([(x, 0, 68), (x + length, 0, 68)], EDGE)
    for row, z in enumerate((12, 27, 43, 58)):
        for column, x in enumerate((17, 44, 73)):
            if preview and (row, column) == (1, 1):
                continue
            length = 9 + (row * 3 + column * 2) % 7
            rule(s, point, x, z, length)
    return point


def browser_page(s, width, height, *, depth=9):
    """A grounded browser display with one address bar."""
    s.box(0, -depth, 0, width, depth, height, 4)
    s.line([(1, 0, height - 15), (width - 1, 0, height - 15)], EDGE)
    for x in (8, 15, 22):
        chart_marker(s, lambda u, v: (u, 0, v), x, height - 7, 1.2, DETAIL)
    outline(s, 32, 0, height - 11, width - 42, 7, 2, DETAIL)
    return lambda x, z: (x, 0, z)


def search_display(s, width, height):
    """A browser display seated in its desktop dock."""
    s.box(17, -25, -8, width - 34, 39, 9, 5)
    return browser_page(s, width, height, depth=13)


def section(s, point, x, z, widths):
    """One heading followed by short text rules."""
    for index, width in enumerate(widths):
        rule(s, point, x, z - 7*index, width, EDGE if index == 0 else DETAIL)


def document_node(s, x, z, width=28, height=33, *, emphasis=False):
    """A folded-corner document node in a face-on link diagram."""
    def point(u, v):
        return level_face(x + u, z + v)

    fold = width*.27
    outline_points = [(0, 0), (width, 0), (width, height - fold),
                      (width - fold, height), (0, height)]
    s.face([point(u, v) for u, v in outline_points], EDGE)
    s.line([point(width - fold, height), point(width - fold, height - fold),
            point(width, height - fold)], DETAIL)
    rule(s, point, 5, height*.50, width - 11, BOLD if emphasis else EDGE)
    rule(s, point, 5, height*.25, width - 15)


def front_marks(s, x, y, z, kind, scale=1, ink=EDGE):
    """A text-free acquisition or data-category icon printed on a face."""
    def point(u, v):
        return (x + u * scale, y, z + v * scale)

    if kind == "mail":
        outline(s, x - 7*scale, y, z - 4*scale, 14*scale, 9*scale, 1, ink)
        s.line([point(-6, 4), point(0, 0), point(6, 4)], ink)
    elif kind == "search":
        chart_marker(s, point, -1.5, 1.4, 4.3, ink)
        s.line([point(2, -2), point(6, -6)], ink)
    elif kind == "link":
        outline(s, x - 7*scale, y, z - 3*scale, 8*scale, 6*scale, 2, ink)
        outline(s, x - scale, y, z - 3*scale, 8*scale, 6*scale, 2, ink)


def profile_mark(s, point, x, z, size, ink=EDGE):
    """The abstract head and shoulders pictogram printed on an ID or column header."""
    chart_marker(s, point, x, z + size*.38, size*.29, ink)
    shoulders = [(-.62, -.62), (-.57, -.42), (-.41, -.25), (-.19, -.18),
                 (.19, -.18), (.41, -.25), (.57, -.42), (.62, -.62), (-.62, -.62)]
    s.line([point(x + u * size, z + v * size) for u, v in shoulders], ink)


def standing_notebook(s, width, height):
    """A spiral notebook propped open on its rigid back cover."""
    def point(x, z):
        return x, -.28*z, z

    back = [(0, -41, 1), (width, -41, 1), point(width, height), point(0, height)]
    s.face(back, EDGE)
    s.face([point(0, 0), point(width, 0), point(width, height), point(0, height)], EDGE)
    for x in (width*.15, width*.38, width*.62, width*.85):
        s.tube([point(x, height - 5), (x, -.28*height + 1, height + 2),
                (x, -.28*height - 5, height + 5), (x, -.28*height - 8, height - 2)], 1.5)
    s.line([point(2, height - 11), point(width - 2, height - 11)], DETAIL)
    return point


def ground_plot(s, width, height):
    """Open plot with the horizontal axis attached to a low ruled foot."""
    p = plot_point
    corners = [p(0, 0), p(width, 0), (width*.65, -width*.35 + 8, 0), (0, 8, 0)]
    s.solid([(x, y) for x, y, _ in corners], 0, 5, crease=False)
    axes(s, p, x=0, y=5, width=width, height=height)
    return p


def desktop_monitor(s, width, height):
    """A monitor with a screen bezel, centered neck, and low stand."""
    s.box(width*.28, -22, 0, width*.44, 39, 5, 5)
    s.box(width*.44, -8, 5, width*.12, 5, 19, 2)
    s.box(0, -9, 20, width, 9, height, 5)
    outline(s, 5, 0, 26, width - 10, height - 11, 2)
    return lambda x, z: (x, 0, z)


def front_bar(s, point, x, z, length, height, ink=EDGE):
    s.face([point(x, z), point(x + length, z),
            point(x + length, z + height), point(x, z + height)], ink)


def column_row(s, heights):
    """Chart columns standing in one row with a common visible foot."""
    for i, height in enumerate(heights):
        x, y = 26*i, -14*i
        s.box(x, y, 3, 19, 19, height, 1.8)

    count = len(heights) - 1
    foot = [(-5, 2), (26*count + 26, -14*count + 2),
            (26*count + 28, -14*count + 23), (-5, 23)]
    s.solid(foot, 0, 3, ink=EDGE, crease=False)


def upright_face(s, point, outline_points, depth, ink=EDGE):
    """Extrude a convex outline behind its visible face."""
    front = [point(x, z) for x, z in outline_points]
    back = [(x - depth*.25, y - depth*.75, z) for x, y, z in front]
    hull = MultiPoint([project(p) for p in front + back]).convex_hull
    s.layers.append((hull.boundary, hull, ink))
    s.line(front + front[:1], ink)


def target_face(s):
    """A round target on a splayed floor stand."""
    def point(x, z):
        return .72*x, -.28*x, z

    s.tube([(14, -29, 2), (0, -9, 49), (-23, 2, 2)], 2.5)
    s.tube([(22, -9, 2), (0, -9, 49)], 2.5)
    upright_face(s, point, oval(0, 59, 41, 41)[:-1], 8)
    for radius in (31, 21, 11):
        s.line([point(x, z) for x, z in oval(0, 59, radius, radius)], EDGE)
    return point


def closed_outline(s, point, points, ink=EDGE):
    vertices = [point(x, z) for x, z in points]
    s.line(vertices + vertices[:1], ink)


def speech_bubble(s, point, width, height, *, tail=.22, depth=5, ink=EDGE):
    """A rounded dialog bubble with a tail cut into its lower silhouette."""
    radius = min(width, height)*.16
    start = width*tail
    tail_width = min(width, height)*.23
    outline_points = rounded(0, 0, width, height, radius)
    outline_points += [(start, 0), (start - tail_width*.2, -tail_width*.8),
                       (start + tail_width, 0)]
    front = [point(x, z) for x, z in outline_points]
    if not depth:
        s.face(front, ink)
        return
    back = [(x - .22*depth, y - .78*depth, z) for x, y, z in front]
    front = [project(vertex) for vertex in front]
    back = [project(vertex) for vertex in back]
    face = Polygon(front)
    sides = [MultiPoint((a, b, c, d)).convex_hull
             for a, b, c, d in zip(back, back[1:] + back[:1],
                                    front[1:] + front[:1], front)]
    outline = unary_union([face, Polygon(back), *sides])
    s.layers.append((outline.boundary, outline, ink))
    seam = LineString(front + front[:1]).difference(outline.boundary.buffer(.12))
    s.layers.append((seam, None, DETAIL))


def sparkle(s, point, x, z, radius, ink=BOLD):
    """Four-point generation mark printed on a graphic."""
    points = [(0, 1), (.19, .24), (.82, 0), (.19, -.24),
              (0, -1), (-.19, -.24), (-.82, 0), (-.19, .24)]
    s.face([point(x + u*radius, z + v*radius) for u, v in points], ink)


def photo_print(s, *, footer=12):
    """An upright bordered landscape print with space below the image."""
    point = landscape_frame(s, footer=footer)
    chart_marker(s, point, 76, footer + 46, 7.3, EDGE)
    chart_line(s, point, [(8, footer + 17), (31, footer + 43), (59, footer + 12)], EDGE)
    chart_line(s, point, [(49, footer + 23), (69, footer + 31),
                         (102, footer + 11)], EDGE)
    return point


def filmstrip(s, *, gap=3):
    """Two framed exposures cut into the same thick filmstrip."""
    def point(x, z):
        return .72*x, -.28*x - .19*z, z

    width = 118
    frames = [(10, 15, 48 - gap/2, 38), (58 + gap/2, 15, 50 - gap/2, 38)]
    openings = [rounded(*frame, 2) for frame in frames]
    for x in (11, 30, 49, 68, 87, 106):
        for z in (6, 58):
            openings.append(rounded(x - 4, z, 8, 5, 1))
    outline_points = rounded(0, 0, width, 69, 4)
    # The slightly inset openings keep their upper and lower perforations legible.
    s.face([point(x, z) for x, z in outline_points], EDGE,
           openings=([point(x, z) for x, z in opening] for opening in openings))
    left, right = point(4, 0), point(114, 0)
    s.line([left, (left[0], left[1] - 3, -3),
            (right[0], right[1] - 3, -3), right], DETAIL)
    return point


def lens_outline(s, point, x, z, radius, ink=EDGE):
    """A magnifier glyph on a chart or search surface."""
    chart_marker(s, point, x, z, radius, ink)
    s.line([point(x + radius*.72, z - radius*.72),
            point(x + radius*1.65, z - radius*1.65)], ink)


def question_mark(s, point, x, z, size):
    """Punctuation printed inside a question bubble."""
    hook = [(-.48, .4), (-.43, .60), (-.24, .73), (.06, .75), (.32, .68),
            (.49, .53), (.51, .32), (.43, .15), (.23, .01), (.06, -.12), (0, -.31)]
    s.line([point(x + u*size, z + v*size) for u, v in hook], BOLD)
    chart_marker(s, point, x, z - .58*size, size*.08, BOLD)


def folded_sheet(s, point, width, height, *, fold=15, depth=4):
    """A paper packet with a folded top corner."""
    outline_points = [(0, 0), (width, 0), (width, height - fold),
                      (width - fold, height), (0, height)]
    upright_face(s, point, outline_points, depth)
    chart_line(s, point, [(width - fold, height), (width - fold, height - fold),
                          (width, height - fold)], DETAIL)


def model_layers(s, point, x, z, count):
    """Stacked layer outlines printed on model controls."""
    for i in range(count):
        h = z + 4*i
        closed_outline(s, point, [(x - 8, h), (x, h + 3), (x + 8, h), (x, h - 3)],
                       EDGE if i == count - 1 else DETAIL)


class SurfaceStrokes:
    """Map shared two-dimensional strokes onto the visible surface of an object."""
    def __init__(self, scene, point, *, from_ground=False):
        self.scene = scene
        self.point = point
        self.vertical_axis = 1 if from_ground else 2

    def line(self, vertices, ink):
        self.scene.line([self.point(p[0], p[self.vertical_axis]) for p in vertices], ink)


def face_arrow(s, point, points, ink=BOLD, *, head=6):
    """Use the shared arrow strokes in a surface's local coordinates."""
    arrow(SurfaceStrokes(s, point, from_ground=True),
          [(x, z, 0) for x, z in points], ink, head=head)


def landscape_frame(s, *, footer=12, ink=EDGE):
    """A thick print with an inset image area and an optional caption margin."""
    def point(x, z):
        return .78*x, -.22*x - .17*z, z

    upright_face(s, point, rounded(0, 0, 110, 70 + footer, 4), 4)
    closed_outline(s, point, rounded(8, footer, 94, 62, 2), ink)
    return point


def woodland(s, point):
    """A low landscape backdrop that leaves room to isolate a foreground tree."""
    chart_marker(s, point, 81, 61, 6, DETAIL)
    chart_line(s, point, [(8, 37), (20, 47), (29, 39)], DETAIL)
    chart_line(s, point, [(72, 37), (84, 46), (102, 33)], DETAIL)
    rule(s, point, 8, 24, 94, DETAIL)


PINE = [(0, 29), (10, 13), (5, 13), (15, 0), (3, 0), (3, -8),
        (-3, -8), (-3, 0), (-15, 0), (-5, 13), (-10, 13)]


def pine(s, point, x, z):
    s.face([point(x + u, z + v) for u, v in PINE], EDGE)


def draft_notebook(s):
    """A spiral desk pad whose back cover supports it at a slight lean."""
    width, height = 86, 91

    def point(x, z):
        return .78*x, -.22*x - .21*z, z

    left, right = point(0, height), point(width, height)
    s.face([(0, -37, 0), (right[0], -.22*width - 37, 0), right, left], EDGE)
    upright_face(s, point, rounded(0, 0, width, height, 2), 3)
    for x in (14, 33, 53, 72):
        a, b, c = point(x, height)
        ring = oval(b - 2.2, c - 1.4, 4.2, 6.5, -57, 229, 24)
        s.tube([(a, y, z) for y, z in ring], .9)
    return point


def desk_sheet(s, width, height, *, fold=14, depth=7):
    """A thick document tilted back from its bottom edge."""
    def point(x, z):
        return .67*x, -.33*x - .42*z, .83*z

    folded_sheet(s, point, width, height, fold=fold, depth=depth)
    return point


def caret(s, point, x, z):
    chart_line(s, point, [(x, z - 5), (x, z + 7)], BOLD)


def code_window(s, rows):
    """A laptop editor with source lines indented relative to an angle-bracket header."""
    point = laptop(s, 116, 78)
    chart_line(s, point, [(21, 65), (14, 60), (21, 55)], EDGE)
    chart_line(s, point, [(26, 65), (33, 60), (26, 55)], EDGE)
    for x, z, length, ink in rows:
        rule(s, point, x, z, length, ink)
    return point


def open_volume(s):
    """Two leaves join at a recessed book gutter, with the cover showing below."""
    def leaf(side):
        def point(x, z):
            u = side*x
            return (.71*u, -.29*u - .58*z, .76*z + 5*sin(pi*x/56))
        return point

    left, right = leaf(-1), leaf(1)
    for point in (left, right):
        cover = [(x, -5) for x in range(0, 60, 7)] + [(59, -5), (59, 72)]
        cover += [(x, 72) for x in range(56, -1, -7)]
        upright_face(s, point, cover, 5)
    for point in (left, right):
        outline_points = [(x, 0) for x in range(0, 57, 7)]
        outline_points += [(x, 68) for x in range(56, -1, -7)]
        s.face([point(x, z) for x, z in outline_points], EDGE)
        chart_line(s, point, [(x, -2.4) for x in range(0, 57, 7)], DETAIL)
    s.line([left(0, 0), left(0, 69)], EDGE)
    return left, right


def audio_deck(s, *, height=62):
    """A wedge-shaped desktop audio editor with a recessed display."""
    def point(x, z):
        return .26*x - .30*z, -.74*x - .42*z, .78*z

    outline_points = rounded(0, 0, 134, height, 5)
    front = [point(x, z) for x, z in outline_points]
    back = []
    for x, y, z in front:
        taper = 1 - .65*z/(height*.78)
        back.append((x - 23*taper, y - 7*taper, z))
    hull = MultiPoint([project(p) for p in front + back]).convex_hull
    s.layers.append((hull.boundary, hull, EDGE))
    closed_outline(s, point, outline_points, EDGE)
    closed_outline(s, point, rounded(7, 7, 120, height - 14, 4), DETAIL)
    return point


def recorder_trace(s, point, start, z, step, samples, ink=EDGE):
    chart_line(s, point, [(start + step*i, z + value) for i, value in enumerate(samples)], ink)


def printed_glyph(s, point, kind, x, z, size, ink=BOLD):
    """Print a shared glyph directly on a visible surface."""
    glyph(SurfaceStrokes(s, point), kind, x, 0, z, size, ink)


def desk_calendar(s, *, active=(1, 1)):
    """A ring-bound tent calendar with one prominently outlined date."""
    def point(x, z):
        return .83*x, -.17*x - .43*z, .91*z

    width, height = 97, 86
    left, right = point(0, height), point(width, height)
    rear_left = (0, -60, 0)
    rear_right = (right[0], -60 - .17*width, 0)
    s.face([rear_left, rear_right, right, left], EDGE)
    upright_face(s, point, rounded(0, 0, width, height, 4), 3)
    for x in (22, 74):
        a, b, c = point(x, 81)
        s.tube([(a, y, z) for y, z in oval(b - 2, c + 4, 4, 8, -48, 240, 24)], 1.45)
    rule(s, point, 3, 67, 91, EDGE)
    for row, z in enumerate((21, 49)):
        for column, x in enumerate((23, 49, 75)):
            selected = (column, row) == active
            size = 21 if selected else 14
            closed_outline(s, point, rounded(x - size/2, z - size/2, size, size, 2),
                           EDGE if selected else DETAIL)
    return point


def face_magnifier(s, point, x, z, radius, *, direction=(.72, -.69)):
    """An open lens with a handle seated against its rim."""
    dx, dz = direction
    end = radius + 12
    s.tube([point(x + length*dx, z + length*dz) for length in (radius + .5, end)],
           1.85, EDGE)
    outer = [point(u, v) for u, v in oval(x, z, radius, radius)]
    inner = [point(u, v) for u, v in oval(x, z, radius - 2.6, radius - 2.6)]
    s.face(outer, EDGE, openings=(inner,))


def request_card(s, point, width, height, *, print_rows=True):
    """A thick tabbed task card, with two short rules below its title."""
    tab = [(0, 0), (width, 0), (width, height - 10), (width*.46, height - 10),
           (width*.39, height), (0, height)]
    front = [point(x, z) for x, z in tab]
    back = [(x - 1, y - 4, z + 1) for x, y, z in front]
    projected_front, projected_back = (list(map(project, face)) for face in (front, back))
    edges = [MultiPoint([a, b, c, d]).convex_hull
             for a, b, c, d in zip(projected_front, projected_front[1:] + projected_front[:1],
                                    projected_back, projected_back[1:] + projected_back[:1])]
    body = unary_union([Polygon(projected_front), Polygon(projected_back), *edges])
    s.layers.append((body.boundary, body, EDGE))
    closed_outline(s, point, tab, EDGE)
    if print_rows:
        rule(s, point, width*.15, height*.59, width*.57, EDGE)
        rule(s, point, width*.15, height*.38, width*.68)
        rule(s, point, width*.15, height*.19, width*.44)


def identification_card(s, point, *, width=52, height=69, seal=True):
    """A clipped ID card with a name strip and an abstract seal."""
    upright_face(s, point, rounded(0, 0, width, height, 5), 3.5)
    closed_outline(s, point, rounded(width*.36, height - 11, width*.28, 4, 2), EDGE)
    if seal:
        chart_marker(s, point, width*.5, height*.56, width*.17, EDGE)
        closed_outline(s, point, [(width*.50, height*.62), (width*.56, height*.56),
                                  (width*.50, height*.50), (width*.44, height*.56)], DETAIL)
    rule(s, point, width*.22, height*.27, width*.56, EDGE)
    rule(s, point, width*.31, height*.16, width*.38, DETAIL)


def merge_diagram(s, *, checked=False):
    """A version graph with a diverging branch and a shared foreground commit."""
    a, b, c = (0, 20, 0), (26, 20, 0), (73, 20, 0)
    top = (36, -15, 0)
    main = [a, b, c, (97, 20, 0)]
    branch = [b, (34, 20, 0), (34, -15, 0), top, (61, -15, 0), (61, 20, 0), c]
    s.line(main, EDGE)
    s.line(branch, BOLD)
    for x, y, z in (a, b, top, (57, -15, 0), (97, 20, 0)):
        s.disk(x, y, z, 5.6, 5.6, 4, EDGE)
    if checked:
        badge(s, "check", *c, 12)
    else:
        s.disk(*c, 8, 8, 6, BOLD)
