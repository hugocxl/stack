from geometry import BOLD, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import paper

DESCRIPTION = "A spoken-audio waveform runs across a clip with a play badge at its leading edge."


def draw(s):
    clip = paper(s, 52, pitch=.89, run=.35, angle=-25, depth=8)
    clip.slab(rounded(0, 0, 139, 52, 10), 8)
    clip.line([(20, 26), (129, 26)], EDGE)
    heights = (5, 9, 18, 32, 21, 11, 5, 12, 23, 34, 22, 10, 5, 15, 24, 13, 5)
    for u, h in zip(range(27, 130, 6), heights):
        clip.line([(u, 26 - h/2), (u, 26 + h/2)], BOLD)
    badge(s, "play", *clip.at(9, 25), 17)
