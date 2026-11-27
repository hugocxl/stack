from geometry import DETAIL
from scenes.redraws._sf import doorway, ground, plane, plate, squircle

DESCRIPTION = "An open door swings out toward a welcome mat at the threshold."


def draw(s):
    w, h = 56, 88
    doorway(s, w, h)
    # The leaf swings out toward the viewer on the left jamb.
    leaf = plane((0, 0, 0), (.26, .97, 0), (0, 0, 1))
    plate(s, leaf, [(0, 1), (w - 3, 1), (w - 3, h - 2), (0, h - 2)], 3, (.97, -.26, 0))
    s.tube([leaf(w - 10, 42), leaf(w - 10, 42)], 1.2)
    # A mat lies flat in front of the threshold.
    mat = ground(2, 22, 0)
    plate(s, mat, squircle(52, 30, 5), 2.2, (0, 0, -1))
    inner = [mat(u + 4, v + 4) for u, v in squircle(44, 22, 3)]
    s.line(inner + inner[:1], DETAIL)
