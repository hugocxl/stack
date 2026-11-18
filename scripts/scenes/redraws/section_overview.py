from geometry import EDGE
from scenes.redraws._w4 import desktop_display, folder_emblem, support_mark

DESCRIPTION = "A help center index on a desktop screen groups its topics into three cards under a headset heading."


def draw(s):
    face = desktop_display(s, width=123, height=81, angle=-26)
    support_mark(face, 18, 62, .65)
    face.rows(31, 62, (46,), ink=EDGE)
    face.line([(7, 50), (116, 50)])
    for u in (10, 46, 82):
        face.frame(u, 13, 30, 29, 3, EDGE)
        folder_emblem(face, u + 9, 26, 12, 10)
        face.rows(u + 7, 20, (16,))
