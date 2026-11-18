from geometry import EDGE
from scenes.redraws._w3 import Surface

DESCRIPTION = "An open workbook pairs three shape-indexed questions with their matching completed answers."


def draw(s):
    # The pages meet at a lowered gutter, with their covers supporting the outside edges.
    right = Surface(s, (0, 9, 7), rise=(-.83, .56), back=(0, 0, -1))
    left = Surface(s, (-39, 9, 16), rise=right.rise, back=right.back)

    def page_point(face, x, v, slope):
        a, b, c = face.point(x, v)
        return (a, b, c + x * slope)

    def page_cover(face, slope):
        outline = [(0, 0), (39, 0), (39, 73), (0, 73)]
        s.face([page_point(face, x, v, slope) for x, v in outline])
        s.line([page_point(face, x, v, slope) for x, v in ((2, 4), (37, 4))])

    page_cover(left, -9 / 39)
    page_cover(right, 9 / 39)
    s.line([(-39, 9, 12), (0, 9, 3), (39, 9, 12),
            (39, 9 - 73 * .83, 12 + 73 * .56)], EDGE)
    for side, slope in ((left, -9 / 39), (right, 9 / 39)):
        def stroke(points, ink=EDGE):
            s.line([page_point(side, x, v, slope) for x, v in points], ink)

        stroke([(7, 61), (30, 61)])
        for index, v in enumerate((47, 34, 21)):
            if index == 0:
                token = [(7, v - 2), (12, v - 2), (12, v + 3), (7, v + 3)]
            elif index == 1:
                token = [(9.5, v - 3), (13, v), (9.5, v + 3), (6, v)]
            else:
                token = [(8, v - 2), (12, v - 2), (10, v + 3)]
            stroke(token + token[:1])
            if side is left:
                stroke([(17, v + 2), (31, v + 2)])
                stroke([(17, v - 3), (26, v - 3)])
            else:
                width = (14, 11, 16)[index]
                stroke([(17, v - 2), (17, v + 3), (17 + width, v + 3),
                        (17 + width, v - 2), (17, v - 2)])
                stroke([(19, v + .5), (15 + width, v + .5)])
