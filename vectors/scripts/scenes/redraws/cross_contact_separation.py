from geometry import DETAIL, EDGE

DESCRIPTION = "A full-height divider on a prep board separates a fish from a carrot."


def draw(s):
    s.box(0, 0, 0, 97, 58, 6, 5)
    fish = lambda x, y: (15 - .72 * (y - 26), 38 + .72 * (x - 20), 7)
    shape = [(6, 20), (12, 17), (19, 16), (26, 18), (32, 21), (38, 16),
             (37, 27), (38, 36), (32, 32), (26, 35), (19, 37), (12, 34), (6, 30), (4, 25)]
    s.face([fish(x, y) for x, y in shape], EDGE)
    s.ellipse(*fish(11, 24), 1.6, 1.6, EDGE)
    s.line([fish(14, 20), fish(17, 25), fish(14, 32)], DETAIL)
    s.line([fish(24, 33), fish(23, 29), fish(28, 32)], DETAIL)
    s.box(50, 1, 6, 4, 56, 23, 1.1)
    carrot = lambda x, y: (x + 10, y, 7)
    root = [(53, 43), (58, 29), (65, 20), (70, 17), (74, 18),
            (77, 22), (75, 28), (69, 35), (61, 40)]
    s.face([carrot(x, y) for x, y in root])
    for points in ([(72, 18), (72, 10), (75, 7), (76, 15), (82, 10), (81, 15), (77, 21)],
                   [(63, 24), (66, 27)], [(58, 33), (61, 35)]):
        s.line([carrot(x, y) for x, y in points], EDGE if points[0] == (72, 18) else DETAIL)
