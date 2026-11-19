from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w3 import Surface, audio_description_art, play

DESCRIPTION = "One mixing console pairs a program fader with a narration fader marked by an eye and sound waves."


def draw(s):
    mixer = Surface(s, (0, 49, 5), rise=(-.7, .72), back=(0, -.72, -.7))
    mixer.plate(rounded(0, 0, 102, 72, 7), 13)
    mixer.stroke([(50, 9), (50, 63)], DETAIL)
    play(mixer, 26, 56, 14, EDGE, aligned=True)
    audio_description_art(mixer, 74, 56, 15, EDGE)
    for x, v in ((26, 19), (76, 32)):
        mixer.rect(x - 2, 10, 4, 34, 2, EDGE)
        for tick in (13, 24, 35, 43):
            mixer.rules(x - 14, tick, [5], ink=DETAIL)
        knob = Surface(s, mixer.point(0, 0, -2), rise=mixer.rise, back=mixer.back)
        knob.plate(rounded(x - 11, v - 4, 22, 8, 2), 2, BOLD if x == 76 else EDGE)
