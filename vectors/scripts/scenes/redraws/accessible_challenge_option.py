from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface, speaker_art

DESCRIPTION = "A visual verification puzzle includes a dedicated loudspeaker key for its audio challenge."


def draw(s):
    card = Surface(s, (0, 0, 0), rise=(-.36, .93), back=(0, -.93, -.36))
    card.plate(rounded(0, 0, 107, 72, 6), 11)
    card.rules(10, 60, [36], ink=EDGE)
    card.rect(9, 10, 59, 41, 4, EDGE)
    for x, v in ((13, 33), (42, 33), (13, 14), (42, 14)):
        card.rect(x, v, 21, 14, 2)
    card.oval(23.5, 40, 4.5, 4.5, EDGE)
    card.rect(49, 36, 7, 8, 1, EDGE)
    card.stroke([(19, 17), (28, 17), (24, 24)], EDGE, closed=True)
    card.stroke([(48, 21), (52, 25), (57, 21), (52, 17)], EDGE, closed=True)
    button = Surface(s, card.point(0, 0, -3), rise=card.rise, back=card.back)
    button.plate(rounded(71, 14, 29, 33, 5), 3, EDGE)
    speaker_art(button, 85.5, 30, 20, BOLD)
