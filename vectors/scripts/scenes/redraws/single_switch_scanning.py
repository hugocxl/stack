from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "A wedge-shaped scanning device has one round bezel switch and a bold focus frame around one option."


def draw(s):
    panel = Surface(s, (0, 54, 4), rise=(-.66, .76), back=(0, -.76, -.66))
    s.face([(104, 4, 0), (104, 54, 0), panel.point(104, 0),
            panel.point(104, 69), (104, 4, 47)])
    panel.plate(rounded(0, 0, 104, 69, 5), 5)
    panel.rect(7, 21, 90, 41, 3, EDGE)
    for x in (14, 41, 68):
        panel.rect(x, 30, 22, 22, 2, DETAIL)
        panel.rules(x + 5, 41, [12])
    panel.rect(37, 26, 30, 30, 3, BOLD)
    button = Surface(s, panel.point(0, 0, -2), rise=panel.rise, back=panel.back)
    button.plate(rounded(43, 3, 18, 14, 7), 2, EDGE)
