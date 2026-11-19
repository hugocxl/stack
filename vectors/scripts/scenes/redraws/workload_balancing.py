from geometry import DETAIL, EDGE
from scenes.redraws.task_created import task_card

DESCRIPTION = "An even balance scale holds a matching stack of task cards in each pan."


def draw(s):
    def point(x, z):
        return .5*x, -.5*x, z

    s.disk(0, 0, 0, 22, 17, 6, EDGE)
    s.tube([(0, 0, 6), (0, 0, 86)], 3, EDGE)

    for x in (-49, 49):
        a, b, _ = point(x, 0)
        apex = point(x, 81)
        s.line([apex, (a - 18, b + 16, 26)], EDGE)
        s.line([apex, (a + 18, b - 16, 26)], EDGE)
        s.disk(a, b, 21, 26, 23, 5, EDGE)

        # Only the front page edges show below the top task tile.
        s.box(a - 12, b - 10, 26, 24, 20, 6, 2, EDGE)
        s.line([(a - 10, b + 10, 29), (a + 10, b + 10, 29)], DETAIL)

        def tile(u, v):
            return a - 12 + 24*u/92, b + 10 - 20*v/71, 32 + 5*v/71

        task_card(s, tile, compact=True)

    s.tube([point(-52, 82), point(52, 82)], 2.5, EDGE)
    s.disk(0, 0, 85, 4, 4, 5, EDGE)
