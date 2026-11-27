from geometry import BOLD
from scenes.redraws._sf import BACK, plate, screen, squircle

DESCRIPTION = "Two thick cards overlap, one printed with a Latin A and the other with a Chinese character."


def draw(s):
    at = screen()
    back = lambda u, v: at(u + 6, v + 8)
    plate(s, back, squircle(66, 66, 14), 7, BACK)
    k = lambda u, v: back(u + 40, v + 40)
    # 文: a dot, a long bar, and two crossing sweeps.
    for stroke in ([(0, 16), (0, 11)], [(-14, 8), (14, 8)], [(-9, 4), (-2, -6), (12, -16)], [(9, 4), (2, -6), (-12, -16)]):
        s.line([k(u, v) for u, v in stroke], BOLD)
    front = lambda u, v: at(u - 62, v - 40)
    plate(s, front, squircle(66, 66, 14), 7, BACK)
    a = lambda u, v: front(u + 33, v + 33)
    s.line([a(-14, -16), a(0, 18), a(14, -16)], BOLD)
    s.line([a(-8, -4), a(8, -4)], BOLD)
