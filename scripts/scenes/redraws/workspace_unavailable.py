from geometry import EDGE, oval, rounded
from scenes.redraws._kit import badge
from scenes.redraws.page_moved import Surface

DESCRIPTION = "A desktop workspace with file, editor, and inspector panes carries an X badge on its title bar."


def draw(s):
    window = Surface(s, (10, 0, 0), side=True, lean=.24)
    window.plate(rounded(0, 0, 110, 73, 5), 7)
    window.line([(0, 57), (110, 57)], EDGE)
    for x in (9, 17, 25):
        window.loop(oval(x, 65, 1.45, 1.45, count=12)[:-1])
    for x in (26, 83):
        window.line([(x, 0), (x, 57)], EDGE)
    for z in (43, 34, 25, 16):
        window.line([(7, z), (18, z)])
    for x, z, width in ((36, 43, 26), (41, 34, 33), (41, 25, 24), (36, 16, 20)):
        window.line([(x, z), (x + width, z)])
    window.frame(90, 28, 13, 18, 2)
    badge(s, "x", *window.point(105, 69), 13)
