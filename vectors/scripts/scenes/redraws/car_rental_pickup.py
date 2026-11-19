from geometry import BOLD, oval
from scenes.redraws.car_park_height_limit import car

DESCRIPTION = "A rental car has a large toothed key resting diagonally against its roofline."


def draw(s):
    car(s)

    def point(u, v, depth=0):
        return 37 + .66*u + .75*v, 21 - .30*u + depth, 38 + .75*u - .66*v

    bow = oval(0, 0, 8, 8, 25, 335, 42)
    outline = [*bow, (32, -3.38), (35, -.3), (32, 3.38),
               (28, 3.38), (28, 6.6), (24, 6.6), (24, 3.38),
               (20, 3.38), (20, 6.6), (16, 6.6), (16, 3.38)]
    hole = oval(-1, 0, 3.4, 3.4, count=29)[:-1]
    s.face([point(u, v, -2.1) for u, v in outline],
           openings=[[point(u, v, -2.1) for u, v in hole]])
    s.face([point(u, v) for u, v in outline], BOLD,
           openings=[[point(u, v) for u, v in hole]])
