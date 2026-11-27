from geometry import BOLD, EDGE, oval
from scenes.redraws._sf import left_face, plate, squircle

DESCRIPTION = "A square sign on two posts shows four arrows pointing in to a gathering point."


def draw(s):
    for x in (-24, 24):
        s.tube([(x, -3, 0), (x, -3, 40)], 2.2, EDGE)
    face = left_face(-36, 0, 36)
    plate(s, face, squircle(72, 72, 8), 5, (0, -1, 0))
    c = 36
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        tip = (c + dx*10, c + dy*10)
        tail = (c + dx*31, c + dy*31)
        s.line([face(*tail), face(*tip)], BOLD)
        px, py = -dy, dx
        s.line([face(tip[0] + dx*8 + px*8, tip[1] + dy*8 + py*8), face(*tip), face(tip[0] + dx*8 - px*8, tip[1] + dy*8 - py*8)], BOLD)
    s.line([face(c + a, c + b) for a, b in oval(0, 0, 4.5, 4.5, count=24)], BOLD)
