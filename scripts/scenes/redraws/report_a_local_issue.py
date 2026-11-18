from geometry import DETAIL, EDGE, oval
from scenes.editorial_objects import camera

DESCRIPTION = "A compact camera overlaps the square foot of a striped roadwork cone."


def draw(s):
    s.box(-23, -14, 0, 54, 51, 5, 3)
    s.solid(oval(4, 10, 19, 19)[:-1], 5, 56,
            top=oval(4, 10, 4, 4)[:-1], crease=False)
    for z, radius in ((24, 14), (34, 11.3), (46, 8.1), (54, 5.9)):
        s.ellipse(4, 10, z, radius, radius, EDGE, start=-45, end=135)
    s.ellipse(4, 10, 61, 3.1, 3.1, DETAIL)

    class CameraPlacement:
        def box(self, x, y, z, w, d, h, r, ink=EDGE):
            s.box(22 + .7*x, -19 + .7*y, .7*z,
                  .7*w, .7*d, .7*h, .7*r, ink)

        def face(self, points, ink):
            s.face([(22 + .7*x, -19 + .7*y, .7*z) for x, y, z in points], ink)

    camera(CameraPlacement())
