from geometry import rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface, photo_art

DESCRIPTION = "A single bordered photograph of a stage and lectern carries a check badge on its lower corner."


def draw(s):
    photo = Surface(s, (0, 0, 0), rise=(-.38, .93), back=(0, -.93, -.38))
    photo.plate(rounded(0, 0, 92, 78, 3), 4)
    photo_art(photo, 7, 18, 78, 53, event=True)
    badge(s, "check", *photo.point(86, 17), 15)
