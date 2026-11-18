from geometry import DETAIL, EDGE, oval
from scenes.redraws._w1 import software_package, upright_profile

DESCRIPTION = "A flatbed delivery truck carries one intact taped carton on its bed."


def draw(s):
    for x in (-37, 31):
        for y in (-15, 16):
            s.face([(a, y, b) for a, b in oval(x, 9, 9, 9, count=32)[:-1]], EDGE)
            s.line([(a, y, b) for a, b in oval(x, 9, 3.4, 3.4, count=24)], DETAIL)

    s.box(-52, -16, 11, 105, 32, 6, 1.5)
    software_package(s, -22, 0, 17, .73, show_code=False)

    cab = [(13, 17), (13, 49), (32, 49), (48, 33), (54, 31), (54, 17)]
    upright_profile(s, cab, 17, 34)
    s.face([(32, -17, 49), (48, -17, 33), (48, 17, 33), (32, 17, 49)], EDGE)
    s.line([(35, y, 46) for y in (-13, 13)] + [(45, 13, 36), (45, -13, 36), (35, -13, 46)], DETAIL)
    s.line([(a, 17, b) for a, b in ((18, 33), (18, 44), (30, 44), (41, 33), (18, 33))], EDGE)
    s.line([(19, 17, 28), (24, 17, 28)], DETAIL)
    s.face([(54, -17, 17), (54, 17, 17), (54, 17, 31), (54, -17, 31)], EDGE)
    for y in (-13, 7):
        s.line([(54, y, 25), (54, y + 6, 25)], DETAIL)
