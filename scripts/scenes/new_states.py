"""First-run, empty, interruption, and confirmation illustrations."""

from math import cos, pi, sin

from shapely.geometry import MultiPoint

from geometry import BOLD, DETAIL, EDGE, GUIDE, oval, project, rounded


def empty_workspace(s):
    # An open presentation folder, with its empty pocket facing the viewer.
    s.face([(0, 12, 6), (0, 0, 51), (29, 0, 51), (38, 0, 60),
            (67, 0, 60), (74, 0, 51), (106, 0, 51), (106, 12, 6)], EDGE)
    s.box(0, 12, 0, 106, 65, 6, 5)
    s.line([(10, 20, 6), (97, 20, 6), (97, 62, 6)], GUIDE, dashed=True)
    s.face([(0, 12, 6), (0, 77, 6), (0, 87, 25), (0, 25, 31)], EDGE)
    s.face([(106, 12, 6), (106, 77, 6), (106, 87, 25), (106, 25, 31)], EDGE)
    s.face([(0, 77, 6), (106, 77, 6), (106, 87, 25), (68, 87, 25),
            (62, 87, 20), (44, 87, 20), (38, 87, 25), (0, 87, 25)], BOLD)


def no_search_results(s):
    # The search control is complete. The results panel beneath it is vacant.
    s.box(0, 0, 0, 105, 8, 74, 5)
    bar = rounded(10, 53, 85, 11, 4)
    s.line([(x, 8, z) for x, z in [*bar, bar[0]]], EDGE)
    s.line([(x, 8, z) for x, z in oval(19, 59, 2.8, 2.8)], EDGE)
    s.line([(21, 8, 57), (24, 8, 55)], EDGE)
    frame = rounded(11, 10, 83, 35, 3)
    s.line([(x, 8, z) for x, z in [*frame, frame[0]]], GUIDE, dashed=True)
    s.tube([(53, 55, 10), (82, 64, 10)], 3, DETAIL)
    s.ring(34, 48, 7, 22, 22, 5, 3.5, BOLD)


def no_notifications(s):
    # A single spun shell avoids seams between latitudes of the dome.
    s.disk(50, 50, 0, 46, 46, 8, DETAIL)
    circles = []
    for sample in range(21):
        angle = pi * sample / 40
        radius = 7 + 34 * cos(angle)
        height = 9 + 47 * sin(angle)
        circles.extend(project((x, y, height)) for x, y in oval(50, 50, radius, radius))
    dome = MultiPoint(circles).convex_hull
    s.layers.append((dome.boundary, dome, BOLD))
    s.disk(50, 50, 56, 4.3, 4.3, 8, DETAIL)
    s.disk(50, 50, 64, 8.6, 8.6, 5, EDGE)


def page_not_found(s):
    # A browser sheet whose right edge stops at a missing quarter.
    silhouette = [(0, 0, 0), (115, 0, 0), (115, 39, 0), (93, 39, 0),
                  (87, 44, 0), (81, 39, 0), (74, 45, 0), (74, 74, 0), (0, 74, 0)]
    s.face([(x, y + 1, z - 5) for x, y, z in silhouette], DETAIL)
    s.face(silhouette, BOLD)
    s.line([(0, 14, 0), (115, 14, 0)], EDGE)
    s.dots(8, 7, 0, nx=3, ny=1, gap=6, ink=EDGE)
    for y, width in ((30, 50), (39, 44), (53, 31), (63, 40)):
        s.line([(11, y, 0), (width + 11, y, 0)], DETAIL)
    s.line([(115, 42, 0), (115, 74, 0), (77, 74, 0)], GUIDE, dashed=True)


def offline_mode(s):
    # The connection breaks at the visibly separated plug and socket, with both
    # cable runs leading back out of the frame.
    for z in (10, 15):
        s.line([(-37, 38, z), (-23, 38, z), (-18, 36, z), (-12, 30, z),
                (5, 30, z)], DETAIL if z == 10 else EDGE)
        s.line([(132, 30, z), (146, 30, z), (152, 27, z), (164, 16, z),
                (178, 16, z)], DETAIL if z == 10 else EDGE)
    s.box(0, 22, 6, 19, 16, 14, 4)
    s.box(13, 12, 0, 37, 36, 27, 6, BOLD)
    for y in (19, 32):
        s.box(50, y, 8, 12, 8, 11, 2, EDGE)
    s.box(122, 21, 6, 16, 18, 14, 4)
    s.box(90, 12, 2, 12, 36, 23, 4, EDGE)
    s.box(100, 12, 0, 26, 36, 27, 6, BOLD)
    s.line([(66, 30, 13), (87, 30, 13)], GUIDE, dashed=True)


def planned_maintenance(s):
    # An offset pair of traffic cones on a strip of lane marking.
    s.line([(4, 18, 0), (40, 18, 0)], DETAIL)
    s.line([(58, 18, 0), (84, 18, 0)], DETAIL)
    s.line([(106, 18, 0), (132, 18, 0)], DETAIL)
    s.line([(5, 65, 0), (131, 65, 0)], GUIDE, dashed=True)
    for x, y, z_scale, ink in [(98, 20, .78, EDGE), (39, 50, 1, BOLD)]:
        s.box(x - 22, y - 22, 0, 44, 44, 5, 5, ink)
        s.solid(oval(x, y, 16, 16)[:-1], 5, 53 * z_scale,
                top=oval(x, y, 4, 4)[:-1], ink=ink)
        for h, radius in ((20, 12.6), (30, 10.4)):
            s.ellipse(x, y, 5 + h * z_scale, radius, radius, DETAIL, -45, 135)


def invite_sent(s):
    # Open envelope behind the invitation with diagonal folds in front.
    s.face([(0, 28, 18), (47, 0, 50), (94, 28, 18), (94, 72, 0),
            (0, 72, 0)], EDGE)
    s.face([(10, 42, 12), (84, 42, 12), (84, 16, 62), (10, 16, 62)], BOLD)
    s.line([(20, 21.2, 52), (70, 21.2, 52)], EDGE)
    s.line([(20, 25.4, 44), (51, 25.4, 44)], DETAIL)
    s.line([(20, 29.5, 36), (59, 29.5, 36)], DETAIL)
    s.face([(0, 30, 18), (47, 56, 4), (94, 30, 18), (94, 72, 0),
            (0, 72, 0)], EDGE)
    s.line([(0, 70, .8), (39, 53, 6)], DETAIL)
    s.line([(94, 70, .8), (55, 53, 6)], DETAIL)


def upload_complete(s):
    s.box(0, 0, 0, 99, 72, 15, 8)
    s.box(13, 13, 15, 73, 45, 2, 5, DETAIL)
    s.line([(20, 51, 17), (46, 51, 17)], DETAIL)
    s.line([(72, 51, 17), (77, 51, 17)], BOLD)
    for x, y in ((17, 16), (81, 54)):
        s.line([(x, y, 17), (x, y, 39)], GUIDE, dashed=True)
    s.box(14, 12, 40, 72, 47, 2, 4, BOLD)
    # The check is proportioned in projection so its two arms stay distinct.
    s.line([(35, 46, 42), (51, 50, 42), (43, 18, 42)], BOLD)


def setup_complete(s):
    # A commissioning lever is locked into its finished position.
    s.box(3, 14, 0, 114, 63, 10, 7)
    s.disk(42, 46, 10, 26, 26, 7, EDGE)
    s.disk(42, 46, 17, 14, 14, 22, DETAIL)
    s.face([(37, 42, 36), (47, 42, 36), (68, 20, 79), (58, 20, 79)], BOLD)
    s.disk(63, 20, 75, 11, 10, 12, BOLD)
    s.line([(68, 46, 10), (98, 46, 10)], DETAIL)
    s.disk(95, 46, 10, 9, 9, 4, EDGE)
    s.line([(90, 45, 14), (94, 49, 14), (100, 42, 14)], BOLD)


FIGURES = [
    (empty_workspace, "Empty workspace", "An open presentation folder awaits its first file."),
    (no_search_results, "No search results", "A loupe sits in front of a completely empty results panel."),
    (no_notifications, "No notifications", "A desk bell is still with its plunger raised."),
    (page_not_found, "Page not found", "An interrupted browser sheet marks the outline of a missing corner."),
    (offline_mode, "Offline mode", "A plug and its socket sit apart at the end of two cables."),
    (planned_maintenance, "Planned maintenance", "Two traffic cones reserve a lane for maintenance work."),
    (invite_sent, "Invite sent", "A card rises from the folds of an open envelope."),
    (upload_complete, "Upload complete", "A checked file floats above a receiving dock."),
    (setup_complete, "Setup complete", "A commissioning lever locks in beside a checked indicator."),
]
