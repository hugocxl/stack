from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w3 import Surface

DESCRIPTION = "Three tabbed preset samples display heading, centered, and bulleted text, with the bulleted sample outlined."


def draw(s):
    gallery = Surface(s, (0, 0, 0), rise=(-.42, .91), back=(0, -.91, -.42),
                      across=(.60, -.80))
    for i, (x, depth, height) in enumerate(((0, 0, 67), (35, 0, 67), (70, -4, 72))):
        sample = Surface(s, gallery.point(x, 0, depth), rise=gallery.rise, back=gallery.back,
                         across=gallery.across)
        outline = [(0, 4), (3, 0), (28, 0), (31, 4), (31, height - 10),
                   (20, height - 10), (18, height), (4, height), (0, height - 4)]
        sample.plate(outline, 5, EDGE)
        if i == 0:
            sample.rules(6, 44, [19], ink=EDGE)
            sample.rules(6, 34, [19, 15, 12], gap=7)
        elif i == 1:
            for v, w in ((44, 13), (36, 20), (28, 15), (20, 11)):
                sample.rules(15.5 - w / 2, v, [w], ink=DETAIL)
        else:
            sample.rect(4, 11, 23, 44, 2, BOLD)
            for v, w in ((44, 13), (33, 12), (22, 10)):
                sample.oval(9, v, 1.1, 1.1, EDGE)
                sample.rules(13, v, [w - 2], ink=EDGE)
