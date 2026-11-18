from geometry import EDGE, oval, rounded
from scenes.redraws._w3 import Surface, cover_cap

DESCRIPTION = "A magnifier overlaps the applicant rows on a scholarship application with a mortarboard letterhead."


def draw(s):
    page = Surface(s, (0, 45, 2), rise=(-.42, .91), back=(0, -.91, -.42))
    page.plate(rounded(0, 0, 77, 93, 3), 7)
    cover_cap(page, 24, 72, 29)
    page.rules(43, 76, [23], ink=EDGE)
    page.rules(43, 66, [17])
    page.rules(10, 54, [57], ink=EDGE)
    for v in (45, 33, 21):
        page.rect(10, v - 3, 7, 6, 1, EDGE)
        page.rules(25, v, [38 if v != 33 else 31])
    lens = Surface(s, (0, 49, 4), rise=page.rise, back=page.back)
    s.tube([lens.point(69, 35), lens.point(84, 21)], 3)
    outside = [lens.point(x, v) for x, v in oval(54, 46, 20, 19, count=48)[:-1]]
    inside = [lens.point(x, v) for x, v in oval(54, 46, 16, 15, count=48)[:-1]]
    s.face(outside, EDGE, openings=[inside])
