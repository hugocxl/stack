from scenes.redraws._w2 import speech_bubble
from scenes.redraws.task_assignment import profile_id

DESCRIPTION = "Three upright profile cards sit side by side inside one speech bubble."


def draw(s):
    def point(x, z):
        return .57*x, -.43*x, z

    speech_bubble(s, point, 116, 62, depth=7)
    for x, z in ((13, 14), (45, 19), (77, 14)):
        profile_id(s, point, x, z, 26, 32)
