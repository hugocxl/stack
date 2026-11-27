from geometry import BOLD, DETAIL
from scenes.redraws._sf import BACK, plate, screen, squircle

DESCRIPTION = "Three video panels stack back to front, the front one showing a play symbol."


def draw(s):
    at = screen()
    w, h = 104, 66
    for k in (2, 1, 0):
        dx, dy = k*12, k*12
        plate(s, lambda u, v, dx=dx, dy=dy: at(u - w/2 + dx, v - h/2 + dy), squircle(w, h, 10), 5, BACK)
    tri = [(-10, -14), (-10, 14), (15, 0), (-10, -14)]
    s.line([at(u, v) for u, v in tri], BOLD)
