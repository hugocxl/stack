from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import publication

DESCRIPTION = "A strapped bundle of folded newspapers is secured with a lock badge."


def draw(s):
    page = publication(s, depth=19)
    for depth in (5, 10, 15):
        s.line([(x, y, z - depth) for x, y, z in
                (page.at(2, 99), page.at(73, 99), page.at(75, 96), page.at(75, 22))], DETAIL)
    s.face([page.at(41, 0), page.at(48, 0), page.at(48, 99), page.at(41, 99)], EDGE)
    s.face([page.at(41, 99), page.at(48, 99),
            *[(x, y, z - 19) for x, y, z in (page.at(48, 99), page.at(41, 99))]], EDGE)
    badge(s, "lock", *page.at(67, 68), 17)
