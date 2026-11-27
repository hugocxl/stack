from geometry import DETAIL, EDGE, GUIDE

DESCRIPTION = "A product carton is measured along its width, depth and height by three dimension lines."


def dim(s, a, b, offset):
    (ax, ay, az), (bx, by, bz) = a, b
    ox, oy, oz = offset
    p, q = (ax + ox, ay + oy, az + oz), (bx + ox, by + oy, bz + oz)
    s.line([a, (ax + ox*1.25, ay + oy*1.25, az + oz*1.25)], GUIDE)
    s.line([b, (bx + ox*1.25, by + oy*1.25, bz + oz*1.25)], GUIDE)
    s.line([p, q], DETAIL)
    for e in (p, q):
        s.line([(e[0] - ox*.25, e[1] - oy*.25, e[2] - oz*.25), (e[0] + ox*.25, e[1] + oy*.25, e[2] + oz*.25)], DETAIL)


def draw(s):
    W, D, H = 62, 44, 46
    s.box(0, 0, 0, W, D, H, 2)
    for x in (W/2 - 5, W/2 + 5):
        s.line([(x, 0, H), (x, D, H), (x, D, H - 12)], DETAIL)
    dim(s, (0, D, 0), (W, D, 0), (0, 12, 0))
    dim(s, (W, 0, 0), (W, D, 0), (12, 0, 0))
    dim(s, (0, D, 0), (0, D, H), (-9, 9, 0))
