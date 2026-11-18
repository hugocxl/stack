from geometry import EDGE, rounded
from scenes.redraws._w3 import Surface, photo_art

DESCRIPTION = "A landscape picture has one attached description strip along its lower edge."


def draw(s):
    picture = Surface(s, (0, 0, 0), rise=(-.43, .90), back=(0, -.90, -.43))
    picture.plate(rounded(0, 0, 100, 78, 6), 9)
    photo_art(picture, 8, 32, 84, 38)
    caption = Surface(s, picture.point(0, 0, -2), rise=picture.rise, back=picture.back)
    caption.plate(rounded(7, -3, 86, 26, 5), 4, EDGE)
    caption.rules(17, 15, [63, 44], gap=9, ink=EDGE)
