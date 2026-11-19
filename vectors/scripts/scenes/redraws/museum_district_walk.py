from geometry import BOLD, DETAIL, EDGE

DESCRIPTION = "An unfolded pocket map shows a dotted walking route between two columned museum landmarks."

FOLDS = ((0, 3), (26, 0), (55, 9), (84, 1))


def map_point(x, y):
    for (a, h0), (b, h1) in zip(FOLDS, FOLDS[1:]):
        if x <= b:
            return x, y, h0 + (x - a) * (h1 - h0) / (b - a)
    raise ValueError("Point exceeds the right edge of the folded map")


def folded_map(s):
    for (a, _), (b, _) in zip(FOLDS, FOLDS[1:]):
        s.face([map_point(a, 0), map_point(b, 0), map_point(b, 56), map_point(a, 56)])


def museum(s, x, y):
    def stroke(points, ink):
        s.line([map_point(x + a * .68 + b * .57, y - a * .54 + b * .57) for a, b in points], ink)

    stroke([(-9, -1), (0, -10), (9, -1), (-9, -1)], EDGE)
    stroke([(-9, 8), (9, 8)], EDGE)
    for a in (-5.5, 0, 5.5):
        stroke([(a, -.5), (a, 7.5)], EDGE)
    stroke([(-9, 10), (9, 10)], DETAIL)


def draw(s):
    folded_map(s)
    museum(s, 13, 14)
    museum(s, 69, 39)
    dots = [(13.5, 28), (16, 31), (19.5, 34), (23, 36), (27, 37), (31.5, 37),
            (36, 36), (40, 34), (44, 32), (48, 30), (52.5, 29), (57, 29), (61.5, 29.7)]
    for x, y in dots:
        s.line([map_point(x, y), map_point(x + 1.4, y + .15)], BOLD)
