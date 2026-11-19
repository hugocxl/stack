from scenes.redraws._w2 import sparkle, speech_bubble

DESCRIPTION = "A single thick speech bubble holds a large four-point sparkle."


def draw(s):
    def p(x, z):
        return x*.74, -x*.26, z

    speech_bubble(s, p, 107, 76, depth=9)
    sparkle(s, p, 53, 39, 28)
