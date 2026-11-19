from geometry import BOLD, Scene, rounded
from scenes.redraws._kit import _screen, badge
from scenes.redraws._w5 import bell_mark, panel

DESCRIPTION = "Three overlapping notification cards share a large bell emblem on the front card."


def bell_emblem(s, face, x, z, scale):
    bell_mark(s, face, x, z, scale, BOLD)
    s.line([face(x + u*scale, z + v*scale)
            for u, v in ((-3.5, -10), (-2, -12.5), (2, -12.5), (3.5, -10))], BOLD)


def bell_badge(s, center, radius):
    # Keep the kit's facing rim and use the same bell emblem as the cards.
    rim = Scene()
    badge(rim, "exclaim", *center, radius)
    s.layers.extend(layer for layer in rim.layers if layer[2] != BOLD)
    bell_emblem(s, lambda u, v: _screen(*center, u, v), 0, -.5, radius*.043)


def draw(s):
    outline = rounded(0, 0, 66, 43, 4)
    for shift in (2, 1, 0):
        def face(u, v):
            return .72*u + 5*shift, -.28*u - .23*v - 4*shift, v + 2.8*shift

        panel(s, outline, face, 3.5)
    bell_emblem(s, face, 32, 21, 1.18)
