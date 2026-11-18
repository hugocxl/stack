from geometry import BOLD, DETAIL, EDGE, oval

DESCRIPTION = "A dotted route crosses a folded gallery floor plan and ends at a sculpture pictogram."

FOLD_WIDTH = 30
FOLD_HEIGHT = 64


def fold_point(panel, u, v):
    """Place a point on a map fold, measured from its lower-left corner."""
    x, y, depth = panel
    return (x + u, y + depth * u / FOLD_WIDTH - .36 * v, .93 * v)


def folded_map(s):
    """Three accordion folds resting on their bottom edges."""
    panels = [(0, 0, 4), (30, 4, -17), (60, -13, 4)]
    for panel in reversed(panels):
        s.face([fold_point(panel, u, v) for u, v in
                ((0, 0), (FOLD_WIDTH, 0), (FOLD_WIDTH, FOLD_HEIGHT), (0, FOLD_HEIGHT))])
    return panels


def mark(s, panel, points, ink=EDGE, *, dashed=False):
    s.line([fold_point(panel, u, v) for u, v in points], ink, dashed)


def draw(s):
    panels = folded_map(s)
    room_walls = [
        [[(5, 33), (5, 56), (24, 56), (24, 42), (14, 42)], [(5, 14), (5, 26), (13, 26)]],
        [[(5, 40), (5, 55), (25, 55), (25, 31)], [(6, 22), (6, 9), (24, 9), (24, 20), (17, 20)]],
        [[(4, 40), (4, 56), (26, 56), (26, 26), (23, 26)], [(9, 8), (26, 8), (26, 18)]],
    ]
    route = [[(10, 16), (18, 16), (18, 34), (30, 34)],
             [(0, 34), (13, 34), (13, 27), (30, 27)],
             [(0, 27), (14, 27), (14, 32)]]
    for panel, rooms, segment in zip(panels, room_walls, route):
        for wall in rooms:
            mark(s, panel, wall, DETAIL)
        mark(s, panel, segment, BOLD, dashed=True)
    mark(s, panels[0], oval(9, 16, 2, 2, count=18), EDGE)
    mark(s, panels[-1], [(7, 34), (22, 34), (22, 38), (7, 38), (7, 34)], EDGE)
    mark(s, panels[-1], [(9, 38), (14, 51), (20, 38)], BOLD)
    mark(s, panels[-1], [(14, 51), (16, 38)], DETAIL)
