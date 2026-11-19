from geometry import DETAIL, rounded

DESCRIPTION = "A cafeteria floor plan has three self-service kiosks facing a long serving counter."


def draw(s):
    s.box(0, 0, 0, 71, 62, 3, 2, DETAIL)
    s.box(0, 0, 3, 71, 4, 17, 1)
    s.box(0, 3, 3, 4, 54, 17, 1)
    for x in (12, 29, 46):
        s.box(x + 1, 17, 3, 10, 9, 3, 1)
        s.box(x + 4, 20, 6, 4, 4, 10, .8)

        def screen(u, v):
            return (x + u, 18 + .35*v, 13 + v)

        s.face([screen(0, 0), screen(12, 0), screen(12, 12), screen(0, 12)])
        s.line([screen(2, 2), screen(10, 2), screen(10, 10),
                screen(2, 10), screen(2, 2)], DETAIL)
    s.line([(15, 32, 3), (53, 32, 3)], DETAIL, dashed=True)
    s.box(8, 43, 3, 54, 12, 9, 1.5)
    for x in (15, 31, 47):
        s.face([(u, v, 12) for u, v in rounded(x, 45, 10, 7, 1)], DETAIL)
