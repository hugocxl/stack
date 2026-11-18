from geometry import BOLD, EDGE, rounded
from scenes.redraws._w4 import landscape, paper

DESCRIPTION = "A mounted contact sheet shows six photographs with the lower middle frame outlined."


def draw(s):
    sheet = paper(s, 77, pitch=.68, run=.61, angle=-15, depth=6)
    sheet.slab(rounded(0, 0, 112, 77, 3), 6)
    for row, v in enumerate((9, 44)):
        for column, u in enumerate((9, 42, 75)):
            if (row + column) % 2:
                sheet.frame(u, v, 27, 25)
                sheet.oval(u + 8, v + 8, 2, 2, EDGE)
                sheet.line([(u, v + 22), (u + 12, v + 14), (u + 18, v + 18),
                            (u + 27, v + 10)], EDGE)
            else:
                landscape(sheet, u, v, 27, 25)
    sheet.frame(39, 41, 33, 31, 3, BOLD)
