from geometry import DETAIL, EDGE, oval
from scenes.redraws._sf import ground, plate, squircle

DESCRIPTION = "A three-by-three grid of thick tiles repeats the same ringed motif."


def draw(s):
    size, gap = 30, 5
    for i in range(3):
        for j in range(3):
            x, y = -48 + i*(size + gap), -48 + j*(size + gap)
            top = ground(x, y, 6)
            plate(s, top, squircle(size, size, 5), 6, (0, 0, -1))
            c = size/2
            s.line([top(c + a, c + b) for a, b in oval(0, 0, 9, 9, count=40)], EDGE)
            s.line([top(c + a, c + b) for a, b in oval(0, 0, 3.4, 3.4, count=24)], DETAIL)
