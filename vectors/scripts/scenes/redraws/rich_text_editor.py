from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "A word processor shows a bold, slanted, and bulleted formatting toolbar above its text and insertion mark."


def draw(s):
    editor = Surface(s, (0, 0, 0), across=(.97, -.24))
    editor.plate(rounded(0, 0, 108, 82, 5), 10)
    editor.rect(7, 54, 94, 21, 3, EDGE)
    for x in (36, 66):
        editor.stroke([(x, 55), (x, 74)])
    for v in (60, 64.5, 69):
        editor.rules(14, v, [15], ink=BOLD)
    for x in (43, 49, 55):
        editor.stroke([(x, 59), (x + 6, 70)], EDGE)
    for v in (60, 65, 70):
        editor.oval(75, v, 1.1, 1.1, EDGE)
        editor.rules(81, v, [12], ink=EDGE)

    editor.rules(13, 42, [55], ink=BOLD)
    editor.rules(13, 31, [75, 66, 39], gap=9)
    editor.stroke([(56, 7), (56, 19)], EDGE)
