from math import cos, radians, sin

from shapely.affinity import rotate, translate
from shapely.geometry import LineString, Point
from shapely.ops import transform, unary_union

from geometry import BOLD, DETAIL, EDGE, oval, project, rounded
from scenes.new_states import invite_sent
from scenes.redraws._kit import arrow, glyph
from scenes.site_objects import phone
from scenes.systems_shapes import bezel, rectangle, ring_upright


def lightning(s, x, y, z, size):
    """Outline a lightning bolt on an upright face."""
    points = (
        (.37, 1), (-.74, -.15), (-.06, -.15), (-.35, -1),
        (.74, .25), (.06, .25), (.37, 1),
    )
    s.line([(x + u * size, y, z + v * size) for u, v in points], BOLD)


def fingerprint(s, x, y, z, size):
    """Draw the ridges that identify the owner of a card or file."""
    def ridge(points):
        s.line([(x + u * size, y, z + v * size) for u, v in points], EDGE)

    ridge(oval(0, -.02, 1, 1.12, -48, 200, 30))
    ridge([*oval(.02, .07, .68, .68, -55, 180, 24),
           (-.65, -.23), (-.7, -.46), (-.77, -.67)])
    ridge([(-.14, -.99), (.11, -.73), (.27, -.4), (.34, -.07),
           *oval(.01, .12, .33, .3, 0, 180, 16),
           (-.34, -.13), (-.47, -.49), (-.61, -.8)])


def software_package(s, x, y, z, scale=1, *, show_code=True):
    """Draw a sealed carton with a printed code symbol."""
    def point(a, b, c):
        return x + a * scale, y + b * scale, z + c * scale

    s.face([point(a, b, 36) for a, b in [(-29, -21), (29, -21), (29, 21), (-29, 21)]], EDGE)
    s.face([point(29, b, c) for b, c in [(-21, 0), (21, 0), (21, 36), (-21, 36)]], EDGE)
    s.face([point(a, 21, c) for a, c in [(-29, 0), (29, 0), (29, 36), (-29, 36)]], EDGE)
    for tape_x in (-5, 5):
        s.line([point(tape_x, -21, 36), point(tape_x, 21, 36), point(tape_x, 21, 30)], DETAIL)
    if not show_code:
        return
    for stroke in ([(-13, 22), (-22, 15), (-13, 8)], [(-4, 7), (4, 23)], [(13, 22), (22, 15), (13, 8)]):
        s.line([point(a, 21, c) for a, c in stroke], EDGE)


def web_globe(s, x, y, z, radius, ink=EDGE):
    """Draw a web-address globe stamped on a front face."""
    for width in (radius, radius * .43):
        s.line([(a, y, b) for a, b in oval(x, z, width, radius, count=32)], ink)
    s.line([(x - radius, y, z), (x + radius, y, z)], ink)


def status_monitor(s):
    """Draw a dashboard monitor with a rear-mounted stand."""
    s.box(-17, -11, 0, 34, 21, 3, 3)
    s.box(-6, -7, 3, 12, 8, 16, 1.5)
    s.box(-39, -8, 14, 78, 8, 49, 4)
    bezel(s, -35, 0, 19, 70, 39, EDGE, 2)


def dashboard_rows(s, rows, x=-27, y=0, width=45):
    for z, length in rows:
        s.line([(a, y, b) for a, b in oval(x, z, 1.8, 1.8, count=14)], EDGE)
        s.line([(x + 8, y, z), (x + 8 + length, y, z)], DETAIL)
        s.line([(x + width, y, z), (x + width + 6, y, z)], DETAIL)


def pulse(width, height):
    """Scale the vertices of a single ECG-like pulse."""
    return [(u * width, v * height) for u, v in
            ((0, 0), (.29, 0), (.38, .28), (.45, -.25), (.53, .9),
             (.63, -.65), (.72, 0), (1, 0))]


def server_tower(s):
    """Draw a server chassis with two slotted removable bays."""
    s.box(-24, -29, 0, 48, 29, 63, 3)
    for z in (8, 20):
        bezel(s, -18, 0, z, 36, 8, EDGE, 1)
        s.line([(-12, 0, z + 4), (3, 0, z + 4)], DETAIL)
        s.line([(12, 0, z + 4), (13.6, 0, z + 4)], EDGE)


def platter(s, x, y, z, radius, height):
    s.solid(oval(x, y, radius, radius)[:-1], z, height, crease=False)
    s.ellipse(x, y, z + height, radius, radius, EDGE)


def database(s, x, y, radius, bottom=0, pitch=10):
    """Draw a database cylinder as three stacked platters."""
    for level in range(3):
        platter(s, x, y, bottom + level * pitch, radius, pitch)


def clipboard(s):
    """Draw a checklist board resting on its bottom edge and a rear stand."""
    s.face([(-25, -2, 28), (25, -2, 28), (25, -19, 0), (-25, -19, 0)], EDGE)
    s.box(-29, -4, 0, 58, 4, 52, 2)
    bezel(s, -25, 0, 3, 50, 45, DETAIL, 1)
    s.box(-10, -4, 45, 20, 7, 8, 2)


def task_rows(s, *rows, y=0):
    """Draw checkbox and rule pairs on a task card."""
    for x, z, width in rows:
        bezel(s, x, y, z, 5, 5, EDGE, .6)
        s.line([(x + 10, y, z + 2.5), (x + 10 + width, y, z + 2.5)], EDGE)


def pipe_junction(s):
    """Draw a welded pair of pipes that narrows into one outlet."""
    branches = []
    for x in (-23, 23):
        cable_sleeve(s, x, -32, -23, 12, 11, 2)
        branches.append(([(x, -24, 12), (x, -12, 12), (x * .95, -5, 12),
                          (x * .76, 1, 12), (x * .39, 8, 12), (0, 14, 12)], 8))
    branches.append(([(0, 23, 12), (0, 36, 12)], 5))
    taper = Point(project((0, 14, 12))).buffer(8).union(
        Point(project((0, 29, 12))).buffer(5)
    ).convex_hull
    shell = unary_union([taper, *(
        LineString(list(map(project, points))).buffer(radius, cap_style="flat")
        for points, radius in branches
    )])
    s.layers.append((shell.boundary, shell, EDGE))
    cable_sleeve(s, 0, 31, 40, 12, 7, 2.5)


def gear(s, x, y, radius, phase):
    """Draw a thick toothed wheel with a central bore."""
    rim = []
    for tooth in range(9):
        for step, scale in ((0, .83), (8, 1), (21, 1), (29, .83)):
            angle = radians(phase + tooth * 40 + step)
            rim.append((x + radius * scale * cos(angle), y + radius * scale * sin(angle)))
    for a, b in zip(rim, rim[1:] + rim[:1]):
        if b[1] - a[1] > b[0] - a[0]:
            s.face([(*a, 0), (*b, 0), (*b, 4), (*a, 4)], EDGE)
    s.face([(*point, 4) for point in rim], EDGE)
    s.ellipse(x, y, 4, radius * .3, radius * .3, EDGE)
    s.ellipse(x, y, 4, radius * .49, radius * .49, DETAIL)


def upright_profile(s, outline, y, depth, ink=EDGE, *, side=False, openings=()):
    """Extrude a clockwise profile in the x-z plane toward the viewer."""
    def point(x, y, z):
        return (y, x, z) if side else (x, y, z)

    edges = list(zip(outline, outline[1:] + outline[:1]))
    visible = [b[0] - a[0] > b[1] - a[1] + .001 for a, b in edges]
    for start, (a, _) in enumerate(edges):
        if not visible[start] or visible[start - 1]:
            continue
        chain = [a]
        index = start
        while visible[index % len(edges)]:
            chain.append(edges[index % len(edges)][1])
            index += 1
        strip = [point(x, y - depth, z) for x, z in chain]
        strip += [point(x, y, z) for x, z in reversed(chain)]
        s.face(strip, ink)
    s.face([point(x, y, z) for x, z in outline], ink,
           openings=[[point(x, y, z) for x, z in hole] for hole in openings])


def cable_sleeve(s, x, back, front, z, radius, wall):
    """Draw an extruded round sleeve with the rim facing the viewer."""
    outline = oval(x, z, radius, radius, 360, 0, 48)[:-1]
    upright_profile(s, outline, front, front - back)
    s.line([(a, front, b) for a, b in oval(x, z, radius - wall, radius - wall)], EDGE)


def tunnel_link(s):
    """Draw a network conduit with a flanged opening at its visible end."""
    cable_sleeve(s, 0, -42, -32, 22, 22, 4)
    cable_sleeve(s, 0, -35, 30, 22, 17, 3)
    cable_sleeve(s, 0, 25, 34, 22, 22, 4)
    s.line([(0, 30, 22), (0, 52, 22)], DETAIL, dashed=True)


def server_unit(s, x, y, width=42, depth=31, height=24):
    """Draw a rack-mount server with two front slots and status lamps."""
    s.box(x, y - depth, 0, width, depth, height, 2.5)
    for z in (height * .28, height * .63):
        bezel(s, x + width * .14, y, z - 2, width * .53, 4, EDGE, 1)
        s.line([(x + width * .77, y, z), (x + width * .84, y, z)], EDGE)


def laptop(s, x, y, w=72, h=48, depth=35):
    """Draw a laptop and return its screen's front plane."""
    s.box(x, y - 5, 0, w, depth, 4, 3)
    s.box(x, y - 5, 4, w, 5, h, 3)
    bezel(s, x + 4, y, 8, w - 8, h - 8, DETAIL, 2)
    for offset in (7, 12):
        s.line([(x + 9, y + offset, 4), (x + w - 9, y + offset, 4)], DETAIL)
    rectangle(s, x + w * .34, y + 17, 4, w * .32, 8, DETAIL, 1.5)
    return y


def prompt(s, x, y, z, size=6, ink=EDGE):
    """Draw the chevron and cursor of a command prompt."""
    s.line([(x, y, z + size), (x + size, y, z), (x, y, z - size)], ink)
    s.line([(x + size * 1.6, y, z - size), (x + size * 2.8, y, z - size)], ink)


def code_brackets(s, point, size, ink=EDGE):
    """Draw a code symbol on a surface parameterized by point(u, v)."""
    for stroke in (((-.49, .39), (-.96, 0), (-.49, -.39)),
                   ((-.18, -.6), (.18, .6)),
                   ((.49, .39), (.96, 0), (.49, -.39))):
        s.line([point(u * size, v * size) for u, v in stroke], ink)


def browser_header(s, x, y, z, width):
    """Draw browser chrome with two controls and an address bar."""
    s.line([(x, y, z - 6), (x + width, y, z - 6)], DETAIL)
    for position in (5, 10):
        s.line([(x + position, y, z), (x + position + 1.2, y, z)], EDGE)
    bezel(s, x + 16, y, z - 1.5, width - 21, 3, DETAIL, 1)


def request_card(s, x, y, w=57, h=40):
    """Draw a standing request card with a command prompt on its face."""
    s.box(x, y - 4, 0, w, 4, h, 2)
    prompt(s, x + 8, y, h - 14, 4)
    for z, length in ((13, .55), (7, .42)):
        s.line([(x + 8, y, z), (x + 8 + w * length, y, z)], DETAIL)


def branch(s, x, y, z, size):
    """Draw a source-control fork with its three commits."""
    marks = [(x, z - size), (x, z + size), (x + size, z + size * .65)]
    s.line([(x, y, z - size * .8), (x, y, z + size * .8)], EDGE)
    s.line([(x, y, z - size * .48), (x + size * .53, y, z - size * .35),
            (x + size, y, z + size * .45)], EDGE)
    for a, b in marks:
        s.line([(u, y, v) for u, v in oval(a, b, size * .2, size * .2, count=20)], EDGE)


def file_card(s, x, y, w=48, h=60, depth=5):
    """Draw a standing file with a folded top corner."""
    fold = w * .27
    outline = [(x, 0), (x, h), (x + w - fold, h), (x + w, h - fold), (x + w, 0)]
    upright_profile(s, outline, y, depth)
    s.line([(x + w - fold, y, h), (x + w - fold, y, h - fold),
            (x + w, y, h - fold)], EDGE)


def arc_arrow(s, start, end, rise, head=7):
    """Draw a smooth, raised transfer arrow between objects."""
    points = []
    for step in range(21):
        t = step / 20
        x, y, z = (a + (b - a) * t for a, b in zip(start, end))
        points.append((x, y, z + rise * 4 * t * (1 - t)))
    arrow(s, points, BOLD, head=head)


def envelope(s, x, y, z, width=54, height=35, *, addressed=False):
    """Draw a sealed envelope upright on its long edge."""
    s.box(x, y - 5, z, width, 5, height, 2)
    center = x + width / 2
    if addressed:
        for side in (-1, 1):
            s.line([(center + side * (width / 2 - 3), y, z + height - 4),
                    (center + side * 13, y, z + height * .58)], EDGE)
        mark_z = z + height * .49
        ring_upright(s, center - .5, y, mark_z, 4.25, BOLD)
        outer = oval(center, mark_z, 10.4, 10.4, -60, -366, 38)
        tail = [(center + 9, mark_z - 3.45), (center + 5.8, mark_z - 4),
                (center + 3.75, mark_z - 2.4), (center + 3.75, mark_z + 4.6)]
        s.line([(u, y, v) for u, v in [*outer, *tail]], BOLD)
    else:
        s.line([(x + 3, y, z + height - 4), (center, y, z + height * .39),
                (x + width - 3, y, z + height - 4)], EDGE)
    for side in (1, -1):
        edge = x + width / 2 + side * (width / 2 - 4)
        inner = x + width / 2 + side * width * .23
        s.line([(edge, y, z + 4), (inner, y, z + height * .54)], DETAIL)


def conveyor(s, x, y, width, depth):
    """Draw a belt around two end rollers with a gap under the return."""
    for foot in (x + 9, x + width - 14):
        s.box(foot, y - depth + 5, 0, 5, depth - 10, 12, 1)
    s.box(x, y - depth, 10, width, depth, 9, 4)
    bezel(s, x + 4, y, 12, width - 8, 5, DETAIL, 2.4)


def package_machine(s, x, y, depth):
    """Draw the hood and open throat of a conveyor-fed machine."""
    left, right = x - 16, x + 16
    back = y - depth
    middle = y - depth / 2
    s.face([(left, back, 61), (right, back, 61),
            (right, y, 61), (left, y, 61)], EDGE)
    s.face([(left, y, 19), (left, y, 61),
            (right, y, 61), (right, y, 19)], EDGE)
    arch = [(back, 19), (back, 61), (y, 61), (y, 19),
            (middle + 9, 19), (middle + 9, 42), (middle - 9, 42), (middle - 9, 19)]
    s.face([(right, a, b) for a, b in arch], EDGE)
    s.line([(right, middle - 5, 51), (right, middle + 5, 51)], DETAIL)


def firmware_chip(s):
    """Draw the pin-legged chip used for firmware and memory operations."""
    for x in (-22, -11, 0, 11, 22):
        for side in (-1, 1):
            s.tube([(x, side * 20, 8), (x, side * 26, 6),
                    (x, side * 29, 1)], 1.8, EDGE)
    s.box(-30, -22, 3, 60, 44, 12, 4)
    rectangle(s, -23, -16, 15, 46, 32, DETAIL, 2)



def memory_chip(s):
    """Draw the chip with two exposed memory banks."""
    firmware_chip(s)
    for x in (-18, 3):
        rectangle(s, x, -9, 15, 15, 18, DETAIL, 1.5)


def seal(s, x, y, z, radius):
    """Draw a scalloped embossed seal with two ribbon ends."""
    ribbon = [(-.65, -.4), (-.92, -1.55), (-.48, -1.38), (-.21, -1.65),
              (0, -.95), (.21, -1.65), (.48, -1.38), (.92, -1.55), (.65, -.4)]
    s.face([(x + u * radius, y, z + v * radius) for u, v in ribbon], EDGE)
    rim = []
    for index, (u, v) in enumerate(oval(0, 0, radius, radius, count=64)[:-1]):
        factor = 1 + .08 * cos(index * radians(45))
        rim.append((x + u * factor, y, z + v * factor))
    s.face(rim, EDGE)
    s.line([(u, y, v) for u, v in oval(x, z, radius * .63, radius * .63)], DETAIL)


def certificate(s, x, y, z, width=68, height=48):
    """Draw a thick presentation certificate with an inset border and ribbon seal."""
    s.box(x, y - 5, z, width, 5, height, 1.6)
    bezel(s, x + 4, y, z + 4, width - 8, height - 8, DETAIL, 2)
    for level, length, ink in ((.73, .48, EDGE), (.56, .38, DETAIL), (.44, .30, DETAIL)):
        a = x + width * .16
        s.line([(a, y, z + height * level), (a + width * length, y, z + height * level)], ink)
    seal(s, x + width * .73, y, z + height * .36, height * .16)


def container_cube(s):
    """Draw a capped intermodal container cube with ribs and a front emblem plate."""
    s.box(-30, -25, 0, 60, 50, 5, 1)
    s.box(-29, -24, 5, 58, 48, 43, 2)
    s.box(-30, -25, 46, 60, 50, 5, 1)
    for y in (-16, -8, 0, 8, 16):
        s.line([(29, y, 10), (29, y, 42)], DETAIL)
    bezel(s, -21, 24, 11, 42, 29, EDGE, 2)
    code_brackets(s, lambda u, v: (u - 5, v - 2, 51), 10)


def connector(s, x, y, z):
    """Draw a keyed plug pointing toward the back with a cable leaving its grip."""
    s.box(x - 8, y - 13, z + 2, 16, 11, 10, 1)
    s.box(x - 12, y - 7, z, 24, 18, 14, 2)
    for offset in (-6, 0, 6):
        s.line([(x + offset, y - 3, z + 14), (x + offset, y + 7, z + 14)], DETAIL)
    s.tube([(x, y + 11, z + 7), (x, y + 20, z + 7),
            (x + 5, y + 27, z + 7), (x + 15, y + 30, z + 7)], 2.6)


def index_cards(s):
    """Draw three standing index cards with exposed staggered tabs."""
    for x, depth, height, tab in ((-41, -15, 48, -29), (-39, -7, 44, -7), (-37, 0, 40, 19)):
        profile = [(x, 0), (x, height), (tab, height), (tab + 3, height + 7),
                   (tab + 11, height + 7), (tab + 14, height), (x + 74, height), (x + 74, 0)]
        upright_profile(s, profile, depth, 4)
    for z, length in ((28, 40), (19, 33), (10, 27)):
        s.line([(-21, 0, z), (-21 + length, 0, z)], DETAIL)


def hard_drive(s, *, network=False):
    """Draw an external drive with a circular platter window and a front socket."""
    s.box(-34, -28, 0, 68, 56, 15, 4)
    if network:
        ethernet_port(s, -14.5, 28, 7, 19, 10)
    else:
        bezel(s, -22, 28, 4, 15, 6, EDGE, 1.4)
    s.line([(20, 28, 7), (26, 28, 7)], DETAIL)
    s.ellipse(-8, -1, 15, 21, 21, EDGE)
    s.ellipse(-8, -1, 15, 5, 5, DETAIL)


def ethernet_port(s, x, y, z, width=15, height=11, ink=EDGE):
    """Draw a keyed opening on the front face of a network device."""
    outline = ((-.49, -.49), (-.49, .2), (-.27, .2), (-.27, .49),
               (.27, .49), (.27, .2), (.49, .2), (.49, -.49), (-.49, -.49))
    s.line([(x + u * width, y, z + v * height) for u, v in outline], ink)


def terminal_console(s):
    """Draw a deep desktop terminal with a recessed display and lower case seam."""
    s.box(-39, -29, 0, 78, 29, 55, 4)
    bezel(s, -33, 0, 9, 66, 40, EDGE, 2)
    s.line([(-31, 0, 5), (31, 0, 5)], DETAIL)


def schema_table(s, x, y, columns):
    """Draw one upright schema table with a header and a field grid."""
    s.box(x, y - 8, 0, 47, 8, 45, 2)
    bezel(s, x + 4, y, 5, 39, 35, EDGE, 1)
    s.line([(x + 4, y, 30), (x + 43, y, 30)], EDGE)
    for height in (13, 21):
        s.line([(x + 4, y, height), (x + 43, y, height)], DETAIL)
    for column in range(1, columns):
        cell = x + 4 + 39 * column / columns
        s.line([(cell, y, 5), (cell, y, 30)], EDGE)
    s.line([(x + 9, y, 35), (x + 22, y, 35)], DETAIL)


def router(s, x, y, width=40, depth=26, height=16):
    """Draw a network appliance with a rear-mounted antenna."""
    antenna = (x + width * .31, y - depth * .32)
    s.box(x - width / 2, y - depth / 2, 0, width, depth, height, 3)
    s.disk(*antenna, height, 3.6, 3.6, 3)
    s.tube([(*antenna, height + 3), (*antenna, height + 22)], 1.6, EDGE)


def barcode(s, x, y, z, width, height):
    """Print a barcode on an upright label."""
    bezel(s, x, y, z, width, height, DETAIL, 1)
    for offset, thickness in ((.12, .025), (.22, .055), (.36, .025),
                              (.46, .049), (.60, .029), (.70, .055), (.86, .026)):
        a = x + width * offset
        s.face([(a, y, z + height * .2), (a + width * thickness, y, z + height * .2),
                (a + width * thickness, y, z + height * .8), (a, y, z + height * .8)], EDGE)


def carrier_van(s, x, y, z, size, ink=EDGE):
    """Print a delivery van pictogram on an upright surface."""
    def strokes(points):
        s.line([(x + u * size, y, z + v * size) for u, v in points], ink)

    strokes([(.11, .28), (0, .28), (0, .64), (.56, .64), (.56, .28),
             (.32, .28)])
    strokes([(.56, .60), (.77, .60), (.96, .43), (.96, .28), (.88, .28)])
    strokes([(.57, .28), (.68, .28)])
    strokes([(.66, .48), (.81, .48)])
    for wheel in (.21, .78):
        strokes(oval(wheel, .25, .098, .098, count=24))


def carrier_plane(s, x, y, z, size):
    """Print an air freight pictogram on an upright surface."""
    profile = ((0, .36), (.19, .30), (.39, .36), (.21, .56), (.30, .63),
               (.60, .44), (.94, .54), (1, .46), (.81, .32), (.60, .26),
               (.43, .08), (.32, .08), (.39, .22), (.11, .21), (0, .36))
    s.line([(x + u * size, y, z + v * size) for u, v in profile], EDGE)


def price_tag(s, x, y, z, size, length=1):
    """Draw a thick merchandise tag and return its eyelet location."""
    width, height = size * length, size * .57
    neck = size * .23
    outline = [(x, z + height * .5), (x + neck, z + height),
               (x + width, z + height), (x + width, z),
               (x + neck, z)]
    upright_profile(s, outline, y, size * .075)
    eye_x, eye_z = x + neck * .84, z + height * .5
    s.line([(a, y, b) for a, b in oval(eye_x, eye_z, size * .048, size * .048, count=16)], EDGE)
    return eye_x, y, eye_z


def open_carton_back(s, left, right, back, front, rim):
    """Draw the far walls and their hinged flaps before inserting the contents."""
    s.face([(left, back, 0), (right, back, 0), (right, front, 0), (left, front, 0)], DETAIL)
    s.face([(left, back, rim), (right, back, rim), (right - 4, back - 14, rim + 9),
            (left + 4, back - 14, rim + 9)], EDGE)
    s.face([(left, back, 0), (right, back, 0), (right, back, rim), (left, back, rim)], EDGE)
    s.face([(left, back, rim), (left, front, rim), (left - 14, front - 4, rim + 5),
            (left - 14, back + 4, rim + 5)], EDGE)
    s.face([(left, back, 0), (left, front, 0), (left, front, rim), (left, back, rim)], DETAIL)


def open_carton_front(s, left, right, back, front, rim, *, flap_depth=13, flap_drop=8):
    """Close the silhouette with the near walls and fold their flaps outward."""
    s.face([(right, back, 0), (right, front, 0), (right, front, rim), (right, back, rim)], EDGE)
    s.face([(right, back, rim), (right, front, rim), (right + flap_depth, front - 4, rim - flap_drop),
            (right + flap_depth, back + 4, rim - flap_drop)], EDGE)
    s.face([(left, front, 0), (right, front, 0), (right, front, rim), (left, front, rim)], EDGE)
    s.face([(left, front, rim), (right, front, rim), (right - 4, front + flap_depth, rim - flap_drop),
            (left + 4, front + flap_depth, rim - flap_drop)], EDGE)


def stock_shelf(s, *, empty=()):
    """Draw a two-tier stock shelf, leaving selected positions vacant."""
    s.box(-35, -13, 0, 70, 34, 5, 1.5)
    s.box(-34, -13, 5, 68, 4, 56, 1.2, DETAIL)
    s.box(-35, -12, 5, 4, 32, 56, 1)
    for row, floor in enumerate((5, 33)):
        for column, x in enumerate((-26, -7, 12)):
            if (row, column) in empty:
                continue
            height = (17, 13, 18)[column]
            s.box(x, -5, floor, 14, 21, height, 1.4)
            s.line([(x + 5, -4, floor + height), (x + 5, 16, floor + height),
                    (x + 5, 16, floor + height - 5)], DETAIL)
        s.box(-34, -11, floor + 24, 68, 33, 4, 1)
    s.box(31, -12, 5, 4, 34, 56, 1)


def waybill(s, width=63, height=65):
    """Draw a standing shipping label with an upright barcode and address block."""
    s.box(-width / 2, -6, 0, width, 6, height, 3)
    left = -width / 2 + 7
    barcode(s, left, 0, 8, width - 14, 15)
    s.line([(left, 0, 31), (-left, 0, 31)], DETAIL)
    for z, length in ((42, 25), (49, 33), (57, 19)):
        s.line([(left, 0, z), (left + length, 0, z)], EDGE)


def caliper(s, left, right, y, shoulder, contact):
    """Span a part with a fixed jaw and a sliding jaw aimed at its sides."""
    y_back = y - 4
    s.box(left - 7, y_back, shoulder, right - left + 28, 4, 8, 1)
    for x in range(left + 3, right + 17, 5):
        s.line([(x, y, shoulder + 8), (x, y, shoulder + 5)], DETAIL)
    for x, sign in ((left, -1), (right, 1)):
        jaw = [(x, contact), (x + sign * 7, contact + 6),
               (x + sign * 7, shoulder + 5), (x + sign * 2, shoulder + 5),
               (x + sign * 2, contact + 5)]
        if sign < 0:
            jaw.reverse()
        upright_profile(s, jaw, y + 1, 3.5)
    s.box(right - 7, y_back - 1, shoulder - 2, 16, 7, 12, 1.4)
    s.line([(right - 3, y + 2, shoulder + 2), (right + 4, y + 2, shoulder + 2)], DETAIL)


def insulated_cooler(s):
    """Draw a molded shipping cooler with a recessed lid and an end handle."""
    s.box(-32, -22, 0, 64, 44, 37, 5)
    s.box(-34, -24, 37, 68, 48, 8, 4)
    rectangle(s, -28, -18, 45, 56, 36, DETAIL, 4)
    for x in (-23, 20):
        s.box(x, 22, 32, 5, 3, 8, 1)
    for z in (23, 29):
        s.line([(32, -8, z), (32, 8, z)], EDGE)
    for y in (-8, 8):
        s.line([(32, y, 23), (32, y, 29)], EDGE)


def flatbed_truck(s, tail, y, direction):
    """Draw a compact flatbed with its open end at tail and its deck at z=20."""
    def x(distance):
        return tail + distance * direction

    def block(a, b, bottom, height, radius):
        s.box(min(x(a), x(b)), y - 13, bottom, abs(b - a), 26, height, radius)

    for distance in (10, 44):
        s.face([(a, y - 13, z) for a, z in oval(x(distance), 8, 7, 7, count=28)], DETAIL)
    block(0, 53, 14, 6, 1.5)
    # Low headboard and the cab stop the flat deck at the same point.
    block(30, 33, 20, 9, 1)
    block(33, 53, 20, 22, 4)
    door = [(x(a), y + 13, z) for a, z in ((37, 37), (48, 37), (50, 30), (37, 30))]
    s.line(door + door[:1], EDGE)
    s.line([(x(38), y + 13, 26), (x(42), y + 13, 26)], DETAIL)
    if direction > 0:
        window = [(x(53), y + a, z) for a, z in ((-9, 29), (9, 29), (9, 36), (-9, 36))]
        s.line(window + window[:1], EDGE)
        for a in (-8, 8):
            s.line([(x(53), y + a - 2, 23), (x(53), y + a + 2, 23)], DETAIL)
    for distance in (10, 44):
        wheel_x = x(distance)
        s.face([(a, y + 14, z) for a, z in oval(wheel_x, 8, 8, 8, count=36)], EDGE)
        s.line([(a, y + 14, z) for a, z in oval(wheel_x, 8, 3, 3, count=24)], DETAIL)


def roller_bridge(s, left, right, y, surface=20):
    """Draw a short roller section with its load surface flush with adjacent decks."""
    for offset in (-11, 9):
        s.box(left, y + offset, surface - 6, right - left, 2, 5, .7)
    for x in range(left + 3, right - 1, 5):
        s.tube([(x, y - 8, surface - 1.6), (x, y + 8, surface - 1.6)], 1.35, EDGE)


def panel_coin(s, x, y, z, radius, ink=EDGE):
    """Print a plain coin with an inset ring on an upright surface."""
    for ratio in (1, .66):
        s.line([(a, y, b) for a, b in oval(x, z, radius * ratio, radius * ratio, count=24)], ink)


def intake_arrow(s, points, head, *, branch=()):
    """Give an intake arrow clearance where it passes the far carton rim."""
    first = len(s.layers)
    if branch:
        s.line(branch, BOLD)
    arrow(s, points, BOLD, head=head)
    clearance = unary_union([path.buffer(1.7) for path, _, _ in s.layers[first:]])
    s.layers.insert(first, (LineString(), clearance, BOLD))


def tree_crown(s, x, y, z, size, *, outline=False):
    """Draw a broadleaf canopy as a single lobed silhouette."""
    profile = [(-.58, .09), (-.83, .22), (-.97, .49), (-.9, .75),
               (-.7, .96), (-.51, 1), (-.37, 1.27), (-.08, 1.39),
               (.22, 1.34), (.41, 1.14), (.65, 1.13), (.9, .94),
               (1, .68), (.94, .38), (.73, .16), (.41, .08)]
    points = [(x + a * size, y, z + b * size) for a, b in profile]
    if outline:
        s.face(points, EDGE)
    else:
        upright_profile(s, [(a, b) for a, _, b in points], y, size * .38)
    s.line([(x, y, z - .55 * size), (x, y, z + .71 * size)], EDGE)
    s.line([(x - .42 * size, y, z + .55 * size), (x, y, z + .24 * size),
            (x + .42 * size, y, z + .61 * size)], DETAIL)


def wheelie_bin(s, x, y, z=0, scale=1, *, contents=None):
    """Draw a lidded municipal bin, opening the lid when contents are supplied."""
    def p(a, b, c):
        return (x + a * scale, y + b * scale, z + c * scale)

    def footprint(left, back, width, depth, radius):
        return [(a, b) for a, b, _ in
                (p(a, b, 0) for a, b in rounded(left, back, width, depth, radius))]

    if contents is not None:
        s.face([p(a, b, c) for a, b, c in
                [(-22, -28, 81), (22, -28, 81), (22, -17, 49), (-22, -17, 49)]], EDGE)
        s.line([p(-18, -26, 75), p(18, -26, 75)], DETAIL)
    wheel = oval(-11, 7, 7, 7, count=32)[:-1]
    for side in (-17, 19):
        s.face([p(side, a, b) for a, b in wheel], EDGE)
    s.solid(footprint(-15, -13, 30, 26, 4), z + 6 * scale, 43 * scale,
            footprint(-20, -17, 40, 34, 4))
    s.face([p(20, a, b) for a, b in wheel], EDGE)
    s.line([p(20, a, b) for a, b in oval(-11, 7, 2.7, 2.7, count=20)], DETAIL)
    s.tube([p(-13, -18, 49), p(-13, -24, 52), p(13, -24, 52),
            p(13, -18, 49)], 1.65 * scale)
    if contents is None:
        s.solid(footprint(-22, -18, 44, 38, 4), z + 49 * scale, 4.5 * scale)
    else:
        rim = [(*xy, z + 49 * scale) for xy in footprint(-22, -18, 44, 38, 4)]
        opening = [(*xy, z + 49 * scale) for xy in footprint(-18, -14, 36, 30, 3)]
        s.face(rim, EDGE, openings=[opening])
        contents(s, x, y, z, scale)
        s.face([p(-22, 20, 46), p(22, 20, 46), p(22, 20, 49), p(-22, 20, 49)], EDGE)
    for a in (-9, 9):
        s.line([p(a, 17, 43), p(a * .8, 14, 15)], DETAIL)


def solar_cells(s, point, *, columns=4, rows=2):
    """Frame and divide a panel face defined by a normalized coordinate map."""
    s.face([point(0, 0), point(1, 0), point(1, 1), point(0, 1)], EDGE)
    for i in range(1, columns):
        u = i / columns
        s.line([point(u, 0), point(u, 1)], DETAIL)
    for j in range(1, rows):
        v = j / rows
        s.line([point(0, v), point(1, v)], DETAIL)


def solar_stand(s, x=0, y=0, scale=1, *, shade=False):
    """Draw the tilted collector face and its pair of triangular supports."""
    def p(a, b, z):
        return (x + a * scale, y + b * scale, z * scale)

    for a in (-23, 23):
        s.tube([p(a, -17, 43), p(a, -17, 4), p(a, 17, 4),
                p(a, 18, 17)], 2 * scale)
    for a in (-23, 23):
        s.box(*p(a - 4, -22, 0), 8 * scale, 43 * scale, 4 * scale, scale)
    left, right, back, front = -33, 33, -24, 24
    s.face([p(right, back, 45), p(right, front, 13),
            p(right, front, 17), p(right, back, 49)], EDGE)
    s.face([p(left, front, 13), p(right, front, 13),
            p(right, front, 17), p(left, front, 17)], EDGE)

    def cell(u, v):
        return p(left + 66 * u, back + 48 * v, 49 - 32 * v)

    solar_cells(s, cell)
    if shade:
        for offset in (.36, .50, .64, .78, .92):
            end = min(1, (1 - offset) / .5)
            s.line([cell(0, offset), cell(end, offset + end * .5)], DETAIL)
        s.line([cell(0, .22), cell(1, .72)], BOLD)


def meter_reader(s):
    """Draw a utility meter with conduit, display and lower terminal cover."""
    s.tube([(0, -4, 0), (0, -4, 17)], 4)
    s.box(-26, -14, 12, 52, 31, 56, 5)
    bezel(s, -20, 17, 35, 40, 19, EDGE, 3)
    s.line([(-20, 17, 28), (20, 17, 28)], DETAIL)
    for x in (-14, 14):
        s.line([(a, 17, b) for a, b in oval(x, 20, 2, 2, count=18)], DETAIL)


def meter_register(s, *, y=17):
    """Draw an analog register with a scale and a reading pointer."""
    s.line([(a, y, b) for a, b in oval(0, 37, 15, 12, 28, 152, 28)], EDGE)
    for x, z in ((-10, 44), (-5.5, 47), (0, 48), (5.5, 47), (10, 44)):
        s.line([(x, y, z), (.78 * x, y, 37 + .8 * (z - 37))], DETAIL)
    s.line([(0, y, 39), (6, y, 46)], BOLD)


def rain_barrel(s, *, capped):
    """Draw a lidded or open rain collector with molded hoops and a low tap."""
    base, rim = 22, 25
    s.solid(oval(0, 0, base, base)[:-1], 0, 53,
            top=oval(0, 0, rim, rim)[:-1], crease=False)
    for z, radius in ((9, 22.6), (42, 24.3)):
        s.ellipse(0, 0, z, radius, radius, EDGE, start=-43, end=133)
    s.disk(0, 0, 51, 26, 26, 4)
    s.ellipse(0, 0, 55, 21.5, 21.5, EDGE)
    if not capped:
        s.ellipse(0, 0, 54, 19, 19, DETAIL, start=137, end=316)
    s.tube([(-5, 24, 15), (-5, 32, 15), (-5, 32, 10)], 2.1)
    s.line([(-8, 28, 19), (-2, 28, 19)], EDGE)
    s.line([(-5, 28, 19), (-5, 28, 16)], EDGE)


def turbine(s, x, y, z, size):
    """Draw a tapered wind turbine with an upright three-blade rotor."""
    s.solid(oval(x, y - .15 * size, .075 * size, .075 * size)[:-1], z,
            .97 * size, top=oval(x, y - .15 * size, .034 * size,
                                 .034 * size)[:-1], crease=False)
    s.box(x - .065 * size, y - .25 * size, z + .94 * size,
          .13 * size, .25 * size, .12 * size, .045 * size)
    blade = ((.055, -.041), (.23, -.092), (.49, -.066), (.65, -.016),
             (.69, .02), (.48, .043), (.22, .043), (.055, .038))
    for angle in (66, 186, 306):
        c, t = cos(radians(angle)), sin(radians(angle))
        s.face([(x + size * (u*c - v*t), y, z + size * (1 + u*t + v*c))
                for u, v in blade], EDGE)
    s.face([(a, y, b) for a, b in oval(x, z + size, .081 * size,
                                      .081 * size, count=28)[:-1]], EDGE)


def lectern(s, x=0, y=0, scale=1):
    """Draw a public lectern speaking toward the front and its gooseneck microphone."""
    def p(a, b, z):
        return (x + a * scale, y + b * scale, z * scale)

    def block(a, b, z, w, d, h, r):
        s.box(*p(a, b, z), w * scale, d * scale, h * scale, r * scale)

    block(-17, -12, 0, 34, 24, 4, 2)
    block(-14, -9, 4, 28, 18, 41, 1)
    near = [p(-21, 14, 50), p(21, 14, 50)]
    far = [p(-21, -14, 42), p(21, -14, 42)]
    s.face([far[1], near[1], p(21, 14, 46), p(21, -14, 38)], EDGE)
    s.face([*near, p(21, 14, 46), p(-21, 14, 46)], EDGE)
    s.face([*far, *reversed(near)], EDGE)
    s.line([p(-5, 8, 48.3), p(-5, 8, 57), p(-7, 5, 62),
            p(-11, -1, 64)], EDGE)
    s.tube([p(-12, -3, 64), p(-16, -8, 65)], 1.8 * scale)


def droplet(s, point, ink=EDGE):
    """Draw a single water drop through a normalized face mapping."""
    outline = [(0, .67), (.15, .4), (.34, .12), (.46, -.13),
               (.47, -.31), (.39, -.48), (.22, -.59), (0, -.63),
               (-.22, -.59), (-.39, -.48), (-.47, -.31),
               (-.46, -.13), (-.34, .12), (-.15, .4)]
    s.face([point(u, v) for u, v in outline], ink)


def screen_point(x, y, z, u, v):
    """Map screen-right and screen-up offsets to an upright, viewer-facing plane."""
    return (x + u / 1.73205 - v / 2.59808,
            y - u / 1.73205 - v / 2.59808,
            z + 2 * v / 2.59808)


def portrait_mark(s, x, y, z, r, ink=EDGE, *, ring=True):
    """Print a circular avatar with a blank head and shoulder outline."""
    if ring:
        s.line([(a, y, b) for a, b in oval(x, z, r, r, count=36)], ink)
    s.line([(a, y, b) for a, b in oval(x, z + .30 * r, .29 * r, .31 * r, count=24)], ink)
    shoulders = oval(x, z - .94 * r, .63 * r, .8 * r, 36, 144, 22)
    s.line([(a, y, b) for a, b in shoulders], ink)


def profile_card(s, x, y, z, *, rows=((32, 23), (23, 18), (14, 21))):
    """Stand a thick identity card on its long edge."""
    s.box(x, y - 6, z, 68, 6, 45, 2)
    portrait_mark(s, x + 19, y, z + 23, 12)
    for height, width in rows:
        s.line([(x + 38, y, z + height), (x + 38 + width, y, z + height)], DETAIL)


def chain_links(s, x=0, y=0, z=35, scale=1):
    """Draw a pair of interlocked oval links with an alternating center crossing."""
    def link(u, v):
        axis = rotate(LineString([(-10, 0), (10, 0)]), 32, origin=(0, 0))
        axis = translate(axis, u, v)
        outer, inner = (axis.buffer(radius, quad_segs=18) for radius in (12, 5.8))
        return outer, inner

    def vertices(shape):
        return [screen_point(x, y, z, u * scale, v * scale)
                for u, v in list(shape.exterior.coords)[:-1]]

    left, left_gap = link(-15, -9)
    right, right_gap = link(15, 9)
    s.face(vertices(left), EDGE, openings=[vertices(left_gap)])
    s.face(vertices(right), EDGE, openings=[vertices(right_gap)])
    # Move the lower crossing of the left link in front of the right one.
    crossing = Point(4, -8).buffer(7)
    left_band = left.difference(left_gap)
    mask = left_band.intersection(crossing)
    visible_edge = left_band.boundary.intersection(crossing)

    center_x, center_y = project((x, y, z))

    def projected(shape):
        return transform(lambda u, v: (center_x + u * scale, center_y - v * scale), shape)

    s.layers.append((projected(visible_edge), projected(mask), EDGE))


def standing_folder(s, *, documents=False):
    """Draw a tabbed project folder on its long edge with an open front lip."""
    outline = [(-34, 0), (-34, 45), (-12, 45), (-7, 39),
               (34, 39), (34, 0)]
    upright_profile(s, outline, -7, 3)
    if documents:
        for x, y, high in ((-23, -5, 49), (-24, -2, 44), (-25, 1, 39)):
            s.box(x, y, 5, 50, 2, high, 1)
        for z, x in ((36, 10), (41, 16)):
            s.line([(-15, -3, z), (x, -3, z)], DETAIL)
    s.face([(-34, -7, 0), (34, -7, 0), (34, 8, 0), (-34, 8, 0)], DETAIL)
    s.face([(34, -7, 0), (34, -7, 39), (34, 12, 30), (34, 8, 0)], EDGE)
    s.face([(-34, 8, 0), (-34, 12, 30), (34, 12, 30), (34, 8, 0)], EDGE)
    s.line([(-29, 11.6, 27), (29, 11.6, 27)], DETAIL)


def organization_card(s):
    """Print an office tower and directory lines on a standing company card."""
    s.box(-37, -6, 0, 74, 6, 51, 3)
    s.line([(-29, 0, 10), (-29, 0, 32), (-24, 0, 32), (-24, 0, 41),
            (-8, 0, 41), (-8, 0, 10), (-29, 0, 10)], EDGE)
    for x in (-20, -12):
        for z in (24, 31):
            s.line([(x, 0, z), (x, 0, z + 3)], EDGE)
    s.line([(-20, 0, 10), (-20, 0, 17), (-13, 0, 17), (-13, 0, 10)], EDGE)
    for z, width in ((34, 25), (24, 20), (14, 23)):
        s.line([(1, 0, z), (1 + width, 0, z)], DETAIL)


def setup_checklist(s, *, optional=False):
    """Draw three large task rows on the standing clipboard."""
    clipboard(s)
    for index, (z, width) in enumerate(((37, 24), (24, 21), (11, 27))):
        dashed = optional and index == 1
        frame = rounded(-21, z - 4.5, 9, 9, 1)
        s.line([(x, 0, v) for x, v in frame + frame[:1]], EDGE, dashed=dashed)
        s.line([(-8, 0, z), (-8 + width, 0, z)], DETAIL, dashed=dashed)
    glyph(s, "check", -16.5, 0, 37, 4.7)


def workspace_layout(s, x, y, z, w, h, *, content="empty"):
    """Draw a workspace title bar and sidebar within the given screen area."""
    header = z + h - 12
    sidebar = x + w * .32
    s.line([(x, y, header), (x + w, y, header)], EDGE)
    s.line([(sidebar, y, header), (sidebar, y, z)], EDGE)
    s.line([(x + 5, y, header + 6), (x + 12, y, header + 6)], DETAIL)
    if content == "empty":
        return

    for row in range(3):
        level = header - 7 - 6 * row
        if content == "default" and row == 0:
            bezel(s, x + 2, y, level - 2.5, sidebar - x - 4, 5, EDGE, 1)
        s.line([(x + 5, y, level), (sidebar - 5 - (row % 2) * 3, y, level)], DETAIL)

    main = sidebar + 5
    if content in ("personal", "team"):
        portrait_mark(s, x + w - 11, y, header + 6, 4.8)
        if content == "team":
            portrait_mark(s, x + w - 24, y, header + 6, 4.8)
            middle = (main + x + w - 4) / 2
            bezel(s, main, y, z + 11, middle - main - 2, header - z - 16, DETAIL, 1)
            bezel(s, middle + 2, y, z + 11, x + w - middle - 6, header - z - 16, DETAIL, 1)
        else:
            bezel(s, main, y, z + 12, x + w - main - 5, header - z - 17, DETAIL, 1)
        s.line([(main, y, z + 6), (x + w - 12, y, z + 6)], DETAIL)


def smartphone(s):
    """Draw the library handset with its front camera in the top bezel."""
    phone(s)
    ring_upright(s, -7, 4, 39, 1.05, EDGE)


def invitation(s):
    """Draw the library invitation and return its badge anchor."""
    invite_sent(s)
    return (91, 36, 17)


def code_rows(s, x, y, z, *, count=3, step=12):
    """Print spaced recovery-code groups without literal characters."""
    for row in range(count):
        height = z - row * step
        for group in (x, x + 20):
            for index in range(3):
                left = group + index * 5.5
                bezel(s, left, y, height, 2.9, 4.5, EDGE, .5)


def session_door(s, *, entering):
    """Draw a thick door frame and an arrow passing over the threshold."""
    s.box(-29, -10, 0, 58, 10, 4, 1)
    s.box(-29, -10, 4, 6, 10, 58, 1)
    s.box(23, -10, 4, 6, 10, 58, 1)
    s.box(-29, -10, 62, 58, 10, 6, 1)

    def leaf(u, z, thickness=0):
        return 23 - 9 * u - thickness, -10 - 42 * u, z

    s.face([leaf(u, 60, depth) for u, depth in ((0, 0), (1, 0), (1, 2.5), (0, 2.5))], EDGE)
    s.face([leaf(1, z, depth) for z, depth in ((5, 0), (60, 0), (60, 2.5), (5, 2.5))], EDGE)
    s.face([leaf(u, z) for u, z in ((0, 5), (1, 5), (1, 60), (0, 60))], EDGE)
    s.tube([leaf(.72, 30), leaf(.87, 30)], 1.15)
    near, far = (-8, 45, 34), (-8, -19, 34)
    direction = [near, far] if entering else [far, near]
    # Separate the foreground path from the jamb where their projections cross.
    path = LineString([project(point) for point in direction])
    s.layers.append((LineString(), path.buffer(1.45), BOLD))
    arrow(s, direction, BOLD, head=12)


def account_key(s, x, y, z, scale=1, *, passkey=False):
    """Draw a notched key with a round bow, optionally engraved with a fingerprint."""
    angle = radians(23)

    def point(u, v):
        return (x + scale * (u * cos(angle) - v * sin(angle)),
                z + scale * (u * sin(angle) + v * cos(angle)))

    bow = oval(0, 0, 16, 16, 340, 20, 38)
    shaft = [(49, 5.5), (53, 2), (53, -6), (46, -6), (46, -10),
             (39, -10), (39, -5.5), (32, -5.5), (32, -9), (25, -9), (25, -5.5)]
    hole = oval(0, 0, 7, 7, count=30)[:-1]
    upright_profile(s, [point(u, v) for u, v in [*bow, *shaft]], y, 3 * scale,
                    openings=[] if passkey else [[point(u, v) for u, v in hole]])
    if passkey:
        fingerprint(s, x, y, z, 10 * scale)


def exchange_arrows(s, x, y, z, length):
    """Draw two opposed screen-aligned arrows for switching."""
    for sign in (1, -1):
        points = [screen_point(x, y, z, -sign * length / 2, sign * 5),
                  screen_point(x, y, z, sign * length / 2, sign * 5)]
        intake_arrow(s, points, 7)
