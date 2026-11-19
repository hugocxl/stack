from geometry import EDGE
from scenes.redraws._w3 import video_camera, video_device

DESCRIPTION = "A laptop displays two rows of auditorium seats with a remote camera tile in the corner."


def draw(s):
    screen = video_device(s)
    for row, columns in ((42, (25, 48, 71)), (19, (17, 40))):
        for x in columns:
            screen.rect(x, row + 6, 18, 12, 3, EDGE)
            screen.stroke([(x - 1, row + 9), (x - 3, row + 9), (x - 3, row + 4),
                           (x, row), (x + 18, row), (x + 21, row + 4),
                           (x + 21, row + 9), (x + 19, row + 9)], EDGE)
    screen.rect(70, 13, 30, 23, 3, EDGE)
    video_camera(screen, 85, 24, 17)
