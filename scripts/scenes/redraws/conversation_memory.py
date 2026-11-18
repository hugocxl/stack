from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import rule, speech_bubble

DESCRIPTION = "A ribbon bookmarks the oldest of three messages in a chat thread."


def draw(s):
    def point(x, z):
        return .76*x, -.24*x, z

    for x, z, width in ((8, 3, 66), (36, 36, 63), (0, 70, 82)):
        def bubble(u, v):
            return point(x + u, z + v)

        speech_bubble(s, bubble, width, 29, tail=.73 if x == 36 else .20, depth=4)
        rule(s, bubble, 10, 18, 35, EDGE)
        rule(s, bubble, 10, 10, 26, DETAIL)

    ribbon = [(59, 104), (74, 104), (74, 83), (66.5, 88), (59, 83)]
    s.face([point(x, z) for x, z in ribbon], BOLD)
