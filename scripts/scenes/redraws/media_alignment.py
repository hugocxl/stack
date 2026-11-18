from geometry import BOLD, EDGE
from scenes.redraws._w3 import browser_window, photo_art, printed_glyph

DESCRIPTION = "A landscape thumbnail and a video thumbnail share a vertical leading-edge guide in one layout frame."


def draw(s):
    frame = browser_window(s, 94, 94)
    photo_art(frame, 25, 49, 49, 22)
    frame.rect(25, 12, 36, 25, 2, EDGE)
    printed_glyph(frame, "play", 43, 24, 12)
    frame.stroke([(19, 7), (19, 75)], BOLD)
    for z in (37, 71):
        frame.rules(19, z, [6], ink=EDGE)
