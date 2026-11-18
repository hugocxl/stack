from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface, photo_art

DESCRIPTION = "A tabbed portfolio folio holds a visible sample print beneath a clock badge."


def draw(s):
    back = Surface(s, (0, 0, 0), rise=(-.37, .93), back=(0, -.93, -.37))
    back.plate([(0, 0), (100, 0), (100, 72), (47, 72), (42, 81),
                (5, 81), (0, 74)], 5)
    print_face = Surface(s, back.point(0, 0, -4), rise=back.rise, back=back.back)
    print_face.plate(rounded(11, 8, 76, 58, 3), 4)
    photo_art(print_face, 19, 34, 49, 25)
    cover = Surface(s, back.point(0, 0, -8), rise=back.rise, back=back.back)
    cover.plate([(0, 0), (100, 0), (100, 34), (64, 34), (59, 29),
                 (42, 29), (37, 34), (0, 34)], 4)
    cover.rect(12, 9, 34, 12, 2)
    cover.rules(18, 15, [19], ink=EDGE)
    badge(s, "clock", *cover.point(97, 50), 16)
