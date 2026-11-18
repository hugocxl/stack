from geometry import DETAIL, EDGE
from scenes.redraws._kit import warning

DESCRIPTION = "A warning triangle marks one block on a folded neighborhood street map."


def draw(s):
    panels = ((-48, -7), (-18, 7), (14, -7), (47, 7))
    for i, ((left, back), (right, front)) in enumerate(zip(panels, panels[1:])):
        def point(x, z):
            return left + x * (right - left), back + x * (front - back), z

        s.face([point(0, 0), point(1, 0), point(1, 54), point(0, 54)], EDGE)
        for z in (16, 20, 35, 39):
            s.line([point(0, z), point(1, z)], DETAIL)
        route = (.58, .35, .58)[i]
        for x in (route, route + .15):
            for low, high in ((3, 16), (20, 35), (39, 51)):
                s.line([point(x, low), point(x, high)], DETAIL)
        for z in (5, 24, 43):
            if i == 1 and z == 24:
                continue
            s.line([point(.13, z), point(.41, z), point(.41, z + 5),
                    point(.27, z + 9), point(.13, z + 5), point(.13, z)], EDGE)

    warning(s, 1, 4, 18, 28)
