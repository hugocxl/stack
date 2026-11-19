from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface, play

DESCRIPTION = "A video frame anchors a boxed subtitle inside its lower safe area."


def video_frame(s, origin=(0, 0, 0), *, safe_area=False):
    face = Surface(s, origin, rise=(-.3, .95), back=(0, -.95, -.3),
                   across=(.94, -.34))
    face.plate(rounded(0, 0, 115, 70, 6), 10)
    face.rect(6, 6, 103, 58, 3, EDGE)
    play(face, 57, 46, 16, EDGE, aligned=True)
    if safe_area:
        for x, dx in ((14, 1), (101, -1)):
            for v, dv in ((13, 1), (57, -1)):
                face.stroke([(x, v + dv * 7), (x, v), (x + dx * 8, v)], EDGE)
    face.rect(26, 16, 63, 16, 3, EDGE)
    face.rules(33, 26, [48, 35], gap=5, ink=BOLD)
    return face


def draw(s):
    video_frame(s, safe_area=True)
