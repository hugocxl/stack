from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w3 import microphone, video_camera, video_device

DESCRIPTION = "A laptop webinar window shows an active presenter microphone above three attendee camera tiles."


def draw(s):
    screen = video_device(s)
    screen.rect(12, 27, 88, 35, 3, DETAIL)
    microphone(screen, 49, 44, 25, BOLD)
    for dx in (13, 20):
        screen.stroke([(49 + dx, 51), (52 + dx, 47), (52 + dx, 42), (49 + dx, 38)], EDGE)
    for x in (12, 42, 72):
        screen.rect(x, 12, 27, 11, 2)
        video_camera(screen, x + 13.5, 17.5, 9)
