"""Shared objects and surface graphics for the education redraws."""

from shapely.geometry import Polygon
from shapely.ops import unary_union

from geometry import BOLD, DETAIL, EDGE, oval, project, rounded
from scenes.redraws._kit import _strokes


def upright(points, y=0):
    """Map coordinates on a printed face to the x-z plane."""
    return [(x, y, z) for x, z in points]


def loop(s, points, ink=EDGE, y=0):
    points_3d = upright(points, y)
    s.line([*points_3d, points_3d[0]], ink)


def rule(s, x, end, z, ink=DETAIL):
    s.line([(x, 0, z), (end, 0, z)], ink)


def paper(s, width, height):
    """Draw a single sheet with a folded upper-right corner."""
    cut = width - 13
    bottom = height - 13
    s.face(upright([(0, 0), (width, 0), (width, bottom), (cut, height), (0, height)]))
    s.line(upright([(cut, height), (cut, bottom), (width, bottom)]), DETAIL)


class Surface:
    """A plane whose artwork coordinates start at its lower-left corner."""

    def __init__(self, s, origin, rise=(0, 1), back=(0, -1, 0), across=(1, 0)):
        self.s = s
        self.origin = origin
        self.rise = rise
        self.back = back
        self.across = across

    def point(self, x, v, depth=0):
        ox, oy, oz = self.origin
        bx, by, bz = self.back
        dy, dz = self.rise
        ax, ay = self.across
        return (ox + x * ax + bx * depth, oy + x * ay + v * dy + by * depth,
                oz + v * dz + bz * depth)

    def viewer_axes(self, x, v):
        """Align a printed pictogram with screen-right and screen-up."""
        origin = project(self.point(x, v))
        right = project(self.point(x + 1, v))
        up = project(self.point(x, v + 1))
        ax, ay = right[0] - origin[0], right[1] - origin[1]
        bx, by = up[0] - origin[0], up[1] - origin[1]
        determinant = ax * by - ay * bx

        def align(u, w):
            return (x + (by * u + bx * w) / determinant,
                    v - (ay * u + ax * w) / determinant)

        return align

    def stroke(self, points, ink=DETAIL, *, closed=False, dashed=False):
        path = [self.point(*p) for p in points]
        self.s.line(path + path[:1] if closed else path, ink, dashed)

    def rect(self, x, v, w, h, r=2, ink=DETAIL):
        self.stroke(rounded(x, v, w, h, r), ink, closed=True)

    def oval(self, x, v, rx, ry, ink=EDGE):
        self.stroke(oval(x, v, rx, ry, count=36), ink)

    def rules(self, x, v, widths, gap=7, ink=DETAIL):
        for i, width in enumerate(widths):
            self.stroke([(x, v - gap * i), (x + width, v - gap * i)], ink)

    def plate(self, outline, depth, ink=EDGE):
        front = [project(self.point(*p)) for p in outline]
        rear = [project(self.point(*p, depth)) for p in outline]
        front_shape = Polygon(front)
        # Preserve concave notches and cut-outs in the silhouette.
        sides = [Polygon([front[i - 1], a, rear[i], rear[i - 1]])
                 for i, a in enumerate(front)]
        silhouette = unary_union([front_shape, Polygon(rear), *sides])
        rim = silhouette.boundary.difference(front_shape.boundary.buffer(.10))
        self.s.layers.append((rim, silhouette, ink))
        self.s.face([self.point(*p) for p in outline], ink)


def flat(s, x=0, y=70, z=5):
    return Surface(s, (x, y, z), rise=(-1, 0), back=(0, 0, -1))


def cover_cap(face, x, v, size, ink=EDGE):
    """Print a mortarboard with crown and tassel."""
    def stroke(points):
        face.stroke([(x + a * size, v + b * size) for a, b in points], ink)

    stroke([(-.52, .12), (0, .35), (.52, .12), (0, -.11), (-.52, .12)])
    stroke([(-.33, .03), (-.33, -.19), (-.17, -.29), (0, -.32),
            (.17, -.29), (.33, -.19), (.33, .03)])
    stroke([(.52, .12), (.52, -.21), (.58, -.33)])


def book(s, w=70, h=80, depth=12):
    """A closed casebound book resting on its rear cover."""
    flat(s, 0, h, 2).plate(rounded(0, 0, w, h, 3), 2)
    pages = flat(s, 0, h, depth - 2)
    pages.plate(rounded(2, 2, w - 4, h - 4, 3), depth - 4)
    s.line([pages.point(w - 2, 5, (depth - 4) / 2),
            pages.point(w - 2, 2, (depth - 4) / 2),
            pages.point(5, 2, (depth - 4) / 2)], DETAIL)
    cover = flat(s, 0, h, depth)
    cover.plate(rounded(0, 0, w, h, 3), 2)
    cover.stroke([(8, 3), (8, h - 3)], DETAIL)
    return cover


def clipboard(s, w=88, h=87):
    """A sloped writing board on its lower edge and rear brace."""
    s.face([(12, 3, 0), (w - 12, 3, 0), (w - 12, 34, 36), (12, 34, 36)])
    board = Surface(s, (0, 66, 4), rise=(-.62, .78), back=(0, -.78, -.62))
    board.plate(rounded(0, 0, w, h, 5), 6)
    page = Surface(s, (0, 67, 4.8), rise=board.rise, back=board.back)
    page.plate(rounded(6, 5, w - 12, h - 13, 2), 1)
    page.rect(w / 2 - 15, h - 13, 30, 9, 3, EDGE)
    return page


def ticket_outline():
    waist = [(0, 15), (4, 17), (7, 21), (7, 27), (4, 31), (0, 33)]
    outline = [(2, 0), (100, 0), (102, 2)]
    outline += [(102 - x, v) for x, v in waist]
    outline += [(102, 46), (100, 48), (2, 48), (0, 46)]
    return outline + waist[::-1] + [(0, 2)]


def ticket(s, *, marks=True, depth=3):
    """A die-cut admission ticket with a perforated stub on its right."""
    face = Surface(s, (0, 0, 0))
    face.plate(ticket_outline(), depth)
    face.stroke([(74, 4), (74, 44)], EDGE, dashed=True)
    if marks:
        for x in (82, 86, 92, 96):
            face.stroke([(x, 13), (x, 32)], DETAIL)
    return face


def scholarship(s):
    """A mounted scholarship certificate with a mortarboard and ribbon seal."""
    face = Surface(s, (0, 0, 0))
    face.plate(rounded(0, 0, 107, 74, 4), 8)
    face.rect(6, 6, 95, 62, 2)
    cover_cap(face, 53, 53, 30)
    face.rules(21, 32, [49, 38, 43], gap=8)
    face.stroke([(78, 21), (77, 10), (82, 12), (86, 9), (85, 21)], EDGE)
    face.oval(82, 24, 8, 8, EDGE)
    return face


def question(face, x, v, size, ink=BOLD, *, aligned=False):
    """A question symbol, with a deliberately open counter."""
    place = face.viewer_axes(x, v) if aligned else lambda u, w: (x + u, v + w)

    def scaled(points):
        return [place(a * size, b * size) for a, b in points]

    face.stroke(scaled([(-.35, .25), (-.3, .42), (-.15, .53), (.09, .54),
                        (.29, .44), (.37, .27), (.32, .11), (.2, .02),
                        (.02, -.1), (.02, -.24)]), ink)
    face.stroke(scaled([(.02, -.43), (.02, -.51)]), ink)


def flashcard_stack(s):
    """A deck of rounded study cards with independent layers at the edges."""
    for x, y, z in ((0, 58, 2), (2, 57, 4), (0, 58, 6), (3, 55, 8)):
        face = flat(s, x, y, z)
        face.plate(rounded(0, 0, 88, 56, 5), 2)
    return face


def video_device(s):
    """An open laptop whose display is the primary surface."""
    s.box(-4, 0, 0, 116, 46, 5, 4)
    base = flat(s, 0, 46, 5)
    base.rect(43, 3, 24, 11, 2)
    base.rect(9, 19, 90, 20, 3)
    for v in (25, 31):
        for x in (16, 28, 40, 52, 64, 76, 88):
            base.rules(x, v, [6])
    screen = Surface(s, (-2, 3, 5), rise=(-.21, .98), back=(0, -.98, -.21))
    screen.plate(rounded(0, 0, 112, 76, 5), 5)
    screen.rect(6, 7, 100, 61, 3, EDGE)
    screen.rules(54, 72, [4])
    return screen


def play(face, x, v, size, ink=BOLD, *, aligned=False):
    place = face.viewer_axes(x, v) if aligned else lambda u, w: (x + u, v + w)
    face.stroke([place(-size * .36, -size * .5), place(size * .54, 0),
                 place(-size * .36, size * .5)], ink, closed=True)


def microphone(face, x, v, size, ink=EDGE):
    face.rect(x - size * .22, v - size * .09, size * .44, size * .68, size, ink)
    face.stroke([(x - size * .36, v + size * .13), (x - size * .36, v - size * .05),
                 (x - size * .27, v - size * .2), (x, v - size * .28),
                 (x + size * .27, v - size * .2), (x + size * .36, v - size * .05),
                 (x + size * .36, v + size * .13)], ink)
    face.stroke([(x, v - size * .28), (x, v - size * .5)], ink)
    face.rules(x - size * .21, v - size * .5, [size * .42], ink=ink)


def video_camera(face, x, v, size, ink=EDGE):
    face.rect(x - size * .5, v - size * .3, size * .71, size * .6, size * .12, ink)
    face.stroke([(x + size * .21, v + size * .12), (x + size * .51, v + size * .29),
                 (x + size * .51, v - size * .29), (x + size * .21, v - size * .12)], ink)


def theater_seat(s, x=0, y=0):
    """An upholstered tip-up chair, with the two legs clear beneath it."""
    for side in (3, 36):
        s.box(x + side, y + 9, 0, 4, 19, 19, 1)
    s.box(x + 2, y + 3, 17, 39, 32, 8, 5)
    back = Surface(s, (x, y + 12, 20), rise=(-.24, .97), back=(0, -.97, -.24))
    back.plate(rounded(5, 2, 33, 37, 8), 7)
    back.rect(10, 9, 23, 24, 5)
    for side in (0, 39):
        s.box(x + side, y + 20, 17, 4, 6, 13, 1)
        s.box(x + side - 1, y + 12, 30, 6, 22, 4, 2)


def manual(s, w=77, h=92):
    """A reference manual standing on its lower edge with a broad spine."""
    face = Surface(s, (0, 0, 0))
    face.plate(rounded(0, 0, w, h, 4), 16)
    face.stroke([(9, 3), (9, h - 3)], EDGE)
    s.line([face.point(w - 3, h, 5), face.point(11, h, 5)], DETAIL)
    s.line([face.point(w - 3, h, 10), face.point(11, h, 10)], DETAIL)
    return face


def school(s, *, doors_open=False):
    """A small school with a bell above the double entrance."""
    front = Surface(s, (0, 48, 0))
    s.face([(0, 0, 0), (108, 0, 0), (108, 0, 55), (0, 0, 55)])
    side = [(108, 0, 0), (108, 48, 0), (108, 48, 55), (108, 0, 55)]
    s.face(side)
    for y in (10, 31):
        s.face([(108, y, 22), (108, y + 11, 22), (108, y + 11, 43), (108, y, 43)], DETAIL)
    if doors_open:
        s.line([(63, 38, 36), (63, 38, 8), (67, 42, 3), (71, 48, 1)], DETAIL)

    entry = [front.point(x, v) for x, v in ((37, 1), (71, 1), (71, 36), (37, 36))]
    outline = [front.point(x, v) for x, v in ((0, 0), (108, 0), (108, 55),
               (54, 82), (0, 55))]
    s.face(outline, openings=[entry] if doors_open else [])
    for x in (8, 80):
        front.rect(x, 24, 20, 22, 1, EDGE)
        front.stroke([(x + 10, 24), (x + 10, 46)])
        front.stroke([(x, 35), (x + 20, 35)])

    s.face([(-4, -4, 55), (54, -4, 85), (54, 52, 85), (-4, 52, 55)])
    s.face([(54, -4, 85), (112, -4, 55), (112, 52, 55), (54, 52, 85)])
    s.line([(-4, 52, 55), (54, 52, 85), (112, 52, 55)], EDGE)

    front.stroke([(41, 50), (45, 54), (46, 62), (49, 67), (54, 69),
                  (59, 67), (62, 62), (63, 54), (67, 50)], BOLD, closed=True)
    front.oval(54, 46.8, 2.6, 2.6, EDGE)
    front.stroke([(54, 69), (54, 73)], EDGE)
    front.rules(33, 39, [42], ink=EDGE)
    s.box(31, 48, 0, 46, 9, 2, 1)

    if doors_open:
        for hinge, leaf, y in ((37, 25, 61), (71, 86, 54)):
            door = [(hinge, 48, 2), (leaf, y, 2), (leaf, y, 36), (hinge, 48, 36)]
            s.face(door)
            knob_x = (hinge + leaf * 4) / 5
            knob_y = (48 + y * 4) / 5
            s.line([(knob_x, knob_y, 14), (knob_x, knob_y, 19)], EDGE)
    else:
        front.rect(37, 1, 34, 35, 1, EDGE)
        front.stroke([(54, 1), (54, 36)], EDGE)
        for x in (49, 59):
            front.stroke([(x, 14), (x, 19)], EDGE)


def wheelchair(face, x, v, size, ink=BOLD):
    """The chair itself as an accessibility pictogram."""
    place = face.viewer_axes(x, v)
    face.stroke([place(a, b) for a, b in oval(-size * .13, -size * .08,
                                              size * .25, size * .25, count=36)], ink)
    face.stroke([place(a, b) for a, b in oval(size * .29, -size * .25,
                                              size * .075, size * .075, count=20)], ink)
    face.stroke([place(a * size, b * size) for a, b in
                 [(-.49, .40), (-.33, .40), (-.24, .17), (.21, .17),
                  (.35, -.14), (.48, -.14)]], ink)


def admission_marks(face):
    """Print a heading and short event details beside a ticket stub."""
    face.rules(15, 33, [43], ink=EDGE)
    face.rules(15, 22, [34, 26], gap=7)


def desk_calendar(s, w=85, h=75):
    """A ring-bound calendar with a triangular desktop stand."""
    front = Surface(s, (0, 36, 3), rise=(-.34, .94), back=(0, -.94, -.34))
    fold = front.point(w, h)
    s.face([(0, -20, 0), (w, -20, 0), fold, front.point(0, h)])
    s.face([(w, -20, 0), front.point(w, 0), fold])
    front.plate(rounded(0, 0, w, h, 3), 3)
    for x in (14, w - 14):
        s.tube([front.point(x, h - 8), front.point(x, h - 2, -2),
                front.point(x, h + 5, 1), front.point(x, h + 2, 6)], 1.3)
    front.rules(7, h - 28, [w - 14], ink=EDGE)
    return front


def course_card(s):
    """A thick course tile standing on its lower edge."""
    face = Surface(s, (0, 0, 0))
    face.plate(rounded(0, 0, 98, 67, 6), 10)
    face.rect(7, 30, 40, 29, 3, EDGE)
    cover_cap(face, 27, 44, 23)
    face.rules(54, 53, [32], ink=EDGE)
    face.rules(54, 43, [24, 29], gap=7)
    return face


def printed_glyph(face, kind, x, v, size, ink=EDGE):
    """Print a shared glyph on a surface that may be tilted or folded."""
    for stroke in _strokes(kind, size):
        face.stroke([(x + u, v + w) for u, w in stroke], ink)


def printed_check(face, x, v, size):
    printed_glyph(face, "check", x, v, size)


def pen_on(face, x, v, length=54, *, pencil=False):
    """A writing tool resting diagonally across a ruled surface, tip first."""
    tool = Surface(face.s, face.point(x, v, -2), rise=face.rise, back=face.back)

    def point(u, w):
        return (.68 * u - .73 * w, .73 * u + .68 * w)

    tip = [(0, 0)] if pencil else [(7, 2.5), (0, 0), (7, -2.5)]
    outline = [*tip, (12, -3.8), (length - 4, -3.8), (length, -2),
               (length, 2), (length - 4, 3.8), (12, 3.8)]
    tool.plate([point(u, w) for u, w in outline], 3)
    tool.stroke([point(12, -3.8), point(12, 3.8)], EDGE)
    if pencil:
        tool.stroke([point(length - 9, -3.8), point(length - 9, 3.8)], EDGE)
        tool.stroke([point(14, 1), point(length - 11, 1)])
    else:
        tool.stroke([point(length - 19, -3.8), point(length - 19, 3.8)], EDGE)
        tool.stroke([point(length - 3, 1), point(length - 15, 1)], EDGE)
        tool.stroke([point(2, 0), point(10, 0)], EDGE)


def sheet(s, w=74, h=87, *, origin=(0, 0, 0), rise=(-.29, .96), depth=4):
    """A short stack of papers with a turned corner on its top copy."""
    face = Surface(s, origin, rise=rise, back=(0, -rise[1], rise[0]))
    cut = 13
    face.plate([(0, 0), (w, 0), (w, h - cut), (w - cut, h), (0, h)], depth)
    face.stroke([(w - cut, h), (w - cut, h - cut), (w, h - cut)], EDGE)
    return face


def spiral_notebook(s, *, w=75, h=89):
    """A thick wire-bound notebook open to a single ruled page."""
    cover = Surface(s, (0, h, 4), rise=(-1, .14), back=(0, 0, -1))
    cover.plate(rounded(0, 0, w + 4, h, 4), 4)
    page = Surface(s, (0, h, 9), rise=cover.rise, back=cover.back)
    page.plate(rounded(3, 2, w - 1, h - 4, 3), 5)
    for v in (13, 28, 43, 58, 73):
        s.tube([page.point(8, v), page.point(2, v, -3),
                page.point(-3, v, -1), page.point(-3, v, 5), page.point(5, v, 8)], 1.1)
    return page


def classroom_desk(s, x, y, size=1):
    """A freestanding school desk with an open knee space below its writing top."""
    for dx, dy in ((3, 3), (24, 3), (3, 18), (24, 18)):
        s.tube([(x + dx * size, y + dy * size, size),
                (x + dx * size, y + dy * size, 19 * size)], size * 1.05)
    s.box(x + size, y + 2 * size, 17 * size, 26 * size, 11 * size, 5 * size, size)
    s.box(x, y, 22 * size, 28 * size, 22 * size, 3 * size, 2 * size)


def classroom_chair(s, x, y, size=1):
    """A school chair facing the desk behind it."""
    for dx, dy in ((3, 2), (13, 2), (3, 11), (13, 11)):
        s.tube([(x + dx * size, y + dy * size, size),
                (x + dx * size, y + dy * size, 10 * size)], size * .8)
    s.box(x, y, 10 * size, 16 * size, 13 * size, 3 * size, 2 * size)
    for dx in (3, 13):
        s.tube([(x + dx * size, y + 11 * size, 12 * size),
                (x + dx * size, y + 13 * size, 24 * size)], size * .85)
    s.box(x, y + 11 * size, 21 * size, 16 * size, 3 * size, 7 * size, 1.5 * size)


def eye(face, x, v, size):
    """The observing eye pictogram, centered in a ticket stub."""
    contour = [(-1, 0), (-.63, .4), (-.27, .61), (0, .65),
               (.27, .61), (.63, .4), (1, 0), (.63, -.4),
               (.27, -.61), (0, -.65), (-.27, -.61), (-.63, -.4)]
    face.stroke([(x + a * size, v + b * size) for a, b in contour], EDGE, closed=True)
    face.oval(x, v, size * .31, size * .31, EDGE)


def vial_art(face, x, v, size, ink=EDGE):
    """A capped specimen tube with a rounded base and a liquid line."""
    shape = [(-.28, .39), (-.28, -.29), (-.21, -.45), (0, -.5),
             (.21, -.45), (.28, -.29), (.28, .39)]
    face.stroke([(x + a * size, v + b * size) for a, b in shape], ink)
    face.rect(x - .34 * size, v + .37 * size, .68 * size, .16 * size, size * .04, ink)
    face.rules(x - .27 * size, v - .08 * size, [.54 * size], ink=ink)


def podium_art(face, x, v, size, ink=EDGE):
    """A front-on lectern with a gooseneck microphone."""
    outline = [(-.48, .15), (.48, .15), (.38, -.02), (.25, -.02),
               (.25, -.48), (.38, -.48), (.38, -.56), (-.38, -.56),
               (-.38, -.48), (-.25, -.48), (-.25, -.02), (-.38, -.02)]
    face.stroke([(x + a * size, v + b * size) for a, b in outline], ink, closed=True)
    face.stroke([(x + a * size, v + b * size) for a, b in
                 ((.19, .15), (.19, .42), (.09, .53), (-.15, .53))], ink)


def photo_art(face, x, v, w, h, *, event=False):
    """Print a framed photograph with stage curtains or a landscape."""
    face.rect(x, v, w, h, 2, EDGE)
    if event:
        for dx, direction in ((0, 1), (w, -1)):
            face.stroke([(x + dx + direction * a * w, v + b * h) for a, b in
                         ((.27, 1), (.22, .73), (.08, .52), (.12, .25), (.2, 0))])
        podium_art(face, x + w / 2, v + h * .44, h * .55)
    else:
        face.stroke([(x + a * w, v + b * h) for a, b in
                     ((0, .15), (.27, .53), (.48, .28), (.68, .65), (1, .18))], EDGE)
        face.oval(x + .25 * w, v + .75 * h, .06 * w, .09 * h)


def speech_outline(x, v, w, h):
    """A compact speech balloon with an integrated lower-left tail."""
    return [(x + a * w, v + b * h) for a, b in ((0, .2), (0, .88), (.06, 1),
            (.94, 1), (1, .88), (1, .2), (.94, .1), (.34, .1),
            (.15, -.15), (.15, .1), (.06, .1))]


def credential(s, *, origin=(0, 0, 0), w=91, h=62, slot=False):
    """A printed academic credential with an embossed seal."""
    face = Surface(s, origin)
    face.plate(rounded(0, 0, w, h, 5), 5)
    if slot:
        face.rect(w / 2 - 8, h - 10, 16, 4, 2, EDGE)
    center_x, center_v = w * .25, h * .46
    radius = min(w * .15, h * .21)
    face.oval(center_x, center_v, radius, radius, EDGE)
    cover_cap(face, center_x, center_v, radius * 1.25)
    face.rules(w * .48, h * .60, [w * .35], ink=EDGE)
    face.rules(w * .48, h * .42, [w * .31, w * .33], gap=h * .11)
    return face


def accessibility_phone(s):
    """A smartphone on its lower edge with a screen, earpiece and side rocker."""
    face = Surface(s, (0, 0, 0), rise=(-.46, .89), back=(0, -.89, -.46))
    face.plate(rounded(0, 0, 47, 86, 8), 8)
    face.rect(4, 7, 39, 71, 5, EDGE)
    face.rules(18, 82, [11], ink=EDGE)
    face.rules(18, 3.5, [11])
    s.line([face.point(47, v, 4) for v in (58, 70)], DETAIL)
    return face


def reader_page(s):
    """A stiff folio with a turned paper corner and a spine visible behind it."""
    face = sheet(s, 76, 79, rise=(-.47, .88), depth=9)
    face.rules(11, 64, [29], ink=EDGE)
    return face


def transcript_folio(s):
    """A wide bound transcript with a narrow column for speaker labels."""
    face = sheet(s, 91, 75, rise=(-.38, .92), depth=8)
    face.stroke([(32, 9), (32, 65)], EDGE)
    for v, width, lines in ((44, 15, (43, 34)), (32, 12, (39,)),
                            (20, 15, (41, 29))):
        face.rules(9, v, [width], ink=EDGE)
        face.rules(40, v, lines, gap=5)
    face.stroke([(7, 51), (83, 51)], DETAIL)
    return face


def speaker_art(face, x, v, size, ink=EDGE):
    """A loudspeaker cone and two radiating sound arcs, upright to the viewer."""
    place = face.viewer_axes(x, v)
    cone = [(-.60, -.17), (-.37, -.17), (-.09, -.42),
            (-.09, .42), (-.37, .17), (-.60, .17)]
    face.stroke([place(a * size, b * size) for a, b in cone], ink, closed=True)
    for r in (.32, .56):
        face.stroke([place((a - .11) * size, b * size)
                     for a, b in oval(0, 0, r, r, -49, 49, 14)], ink)


def keycap(s, x, y, size):
    """A tapered keycap with a slightly inset rounded crown."""
    foot = rounded(x, y, size, size, 6)
    top = rounded(x + 3, y + 3, size - 6, size - 6, 5)
    s.solid(foot, 0, 8, top, crease=False)
    s.face([(a, b, 8) for a, b in top], EDGE)


def vibration_marks(face, radii, strengths):
    """Screen-facing vibration waves with open space around the phone's case."""
    for x, start, end, sign in ((-1, 143, 218, -1), (48, -37, 38, 1)):
        position = face.viewer_axes(x + 5 * sign, 45)
        for r, ink in zip(radii, strengths):
            face.stroke([position(a, b)
                         for a, b in oval(0, 0, r, r * 1.4, start, end, 22)], ink)


def audio_description_art(face, x, v, size, ink=EDGE):
    """An eye followed by sound waves, the shared visual for narrated imagery."""
    place = face.viewer_axes(x, v)
    almond = [(-.61, 0), (-.44, .17), (-.23, .27), (0, .30),
              (.23, .27), (.44, .17), (.61, 0), (.44, -.17),
              (.23, -.27), (0, -.30), (-.23, -.27), (-.44, -.17)]
    face.stroke([place(a * size, b * size) for a, b in almond], ink, closed=True)
    face.stroke([place(a, b) for a, b in oval(0, 0, size * .17, size * .17)], ink)
    for r in (.31, .53):
        face.stroke([place(a, b) for a, b in
                     oval(size * .45, 0, size * r, size * r, -56, 56, 14)], ink)


def browser_window(s, w=110, h=76, *, origin=(0, 0, 0)):
    """A browser on its lower edge with a raised frame and address bar."""
    face = Surface(s, origin, across=(.96, -.28))
    face.plate(rounded(0, 0, w, h, 5), 7)
    face.rules(0, h - 15, [w], ink=EDGE)
    for x in (7, 13):
        face.oval(x, h - 7.5, 1.3, 1.3, EDGE)
    face.rect(w * .25, h - 11, w * .50, 7, 3)
    return face


def interface_phone(s, origin=(0, 0, 0), *, scale=1):
    """A handset standing on its lower edge, with a screen bezel and earpiece."""
    face = Surface(s, origin, rise=(-.34 * scale, .94 * scale), back=(0, -.94, 0),
                   across=(.97 * scale, -.24 * scale))
    face.plate(rounded(0, 0, 46, 83, 8), 7 * scale)
    face.rect(4, 7, 38, 66, 4, EDGE)
    face.rules(18, 78, [10], ink=EDGE)
    return face


def preview_page(face, x, v, w, h, *, narrow=False):
    """Show the same masthead, hero image, and text in wide or narrow columns."""
    header = h - 3
    face.rules(x, v + header, [w * .42], ink=EDGE)
    face.rules(x + w * .80, v + header, [w * .20])
    face.rules(x, v + header - 5, [w])
    if narrow:
        photo_art(face, x, v + h * .42, w, h * .33)
        face.rules(x, v + h * .30, [w * .79], ink=EDGE)
        face.rules(x, v + h * .19, [w, w * .65], gap=h * .11)
    else:
        photo_art(face, x, v + 3, w * .54, h * .67)
        face.rules(x + w * .63, v + h * .62, [w * .32], ink=EDGE)
        face.rules(x + w * .63, v + h * .44, [w * .37, w * .27, w * .32], gap=h * .14)


def design_layer(s, origin=(0, 0, 0), *, ink=EDGE):
    """A rigid design sheet propped up on its lower edge, with one inset tile."""
    face = Surface(s, origin, rise=(-.76, .65), back=(0, -.65, -.76))
    face.plate(rounded(0, 0, 85, 63, 4), 4, ink)
    face.rect(11, 11, 63, 41, 3, ink)
    return face


def profile_art(face, x, v, size, ink=EDGE):
    """Print an account avatar with no facial features."""
    place = face.viewer_axes(x, v)
    face.stroke([place(a, b) for a, b in oval(0, size * .23, size * .21, size * .21)], ink)
    face.stroke([place(a, b - size * .36) for a, b in
                 oval(0, 0, size * .43, size * .34, 0, 180, 28)], ink)


def typeset_a(face, x, v, size, ink=BOLD):
    """Print the cap-height sample used to compare type sizes."""
    face.stroke([(x, v), (x + size * .36, v + size), (x + size * .72, v)], ink)
    face.rules(x + size * .14, v + size * .35, [size * .44], ink=ink)


def component_art(face, x, v, w, h, ink=EDGE):
    """Draw the diamond used for a single component on an editor surface."""
    face.stroke([(x, v + h / 2), (x + w / 2, v), (x, v - h / 2), (x - w / 2, v)],
                ink, closed=True)


def selection_handle(face, x, v, size=6):
    """Draw a corner control over the edge it grips."""
    outline = rounded(x - size / 2, v - size / 2, size, size, 1)
    face.s.face([face.point(u, w) for u, w in outline], EDGE)


def strike_through(face, x, v, size):
    """Lay the shared slash glyph over an existing screen-facing mark."""
    place = face.viewer_axes(x, v)
    for stroke in _strokes("slash", size):
        face.stroke([place(u, w) for u, w in stroke], BOLD)


def visibility_art(face, x, v, size, *, hidden=False):
    """Print the eye control with an optional shared slash through it."""
    place = face.viewer_axes(x, v)
    almond = [(-1, 0), (-.68, .33), (-.35, .52), (0, .58), (.35, .52), (.68, .33),
              (1, 0), (.68, -.33), (.35, -.52), (0, -.58), (-.35, -.52), (-.68, -.33)]
    face.stroke([place(u * size, w * size) for u, w in almond], EDGE, closed=True)
    face.stroke([place(u, w) for u, w in oval(0, 0, size * .27, size * .27)], EDGE)
    if hidden:
        strike_through(face, x, v, size * 1.24)


def interface_monitor(s, *, w=112, h=74):
    """A desktop monitor with a raised display frame and a central pedestal."""
    s.box(w * .28, -17, 0, w * .41, 30, 4, 4)
    s.box(w * .45, -10, 4, w * .08, 6, 24, 1)
    face = Surface(s, (0, 0, 21), across=(.97, -.18))
    face.plate(rounded(0, 0, w, h, 5), 8)
    face.rect(5, 6, w - 10, h - 11, 2, EDGE)
    return face
