from shapely.geometry import LineString, Polygon

from geometry import DETAIL, EDGE, oval, project

DESCRIPTION = "A rolled floor plan rises from an archival tube and unfurls to show its room outlines."


def draw(s):
    s.solid(oval(0, 0, 17, 17)[:-1], 0, 53, crease=False)
    s.ellipse(0, 0, 3, 17, 17, DETAIL, start=-45, end=135)
    s.solid(oval(0, 0, 19, 19)[:-1], 53, 6, crease=False)
    s.ellipse(0, 0, 59, 19, 19, EDGE)
    s.ellipse(0, 0, 59, 15, 15, DETAIL)

    s.solid(oval(0, 0, 11, 11)[:-1], 58, 42, crease=False)
    s.ellipse(0, 0, 100, 7, 7, DETAIL, start=54, end=345)

    def paper(u, z):
        return 4 + u, 10 - .36*u, z

    flap = [paper(0, 61), paper(51, 58), paper(51, 97), paper(0, 100)]
    end = list(map(project, flap))
    s.layers.append((LineString(end), Polygon(end), EDGE))

    def plan(points):
        s.line([paper(u, z) for u, z in points], EDGE)

    plan([(13, 68), (43, 66), (43, 88), (13, 90), (13, 68)])
    plan([(25, 89), (25, 80), (43, 79)])
    plan([(25, 74), (25, 67)])

    # The near half of the lip covers the paper at the mouth of the tube.
    near = oval(0, 0, 19, 19, -45, 135)
    inner = oval(0, 0, 15, 15, -45, 135)
    band = [project((x, y, 59)) for x, y in near + inner[::-1]]
    s.layers.append((LineString([project((x, y, 59)) for x, y in near]),
                     Polygon(band), EDGE))
    s.ellipse(0, 0, 59, 15, 15, DETAIL, start=-45, end=135)
