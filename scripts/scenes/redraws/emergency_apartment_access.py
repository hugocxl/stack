from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import coin, warning

DESCRIPTION = "An emergency triangle marks an apartment door with a key engaged in its lock."


def draw(s):
    s.box(-28, -14, 0, 56, 15, 79, 1)
    s.face([(-21, 1.1, 0), (21, 1.1, 0), (21, 1.1, 71), (-21, 1.1, 71)])
    s.line([(-13, 1.2, 10), (-13, 1.2, 64), (13, 1.2, 64), (13, 1.2, 10),
            (-13, 1.2, 10)], DETAIL)
    coin(s, 0, 1.45, 56, 1.65, depth=.4, ink=DETAIL)
    coin(s, 15, 2, 35, 4.5, depth=1.3)
    s.tube([(9, 4, 43), (17, 4, 43)], 1.3, EDGE)
    s.tube([(15, 3, 35), (15, 24, 35)], 1.55, EDGE)

    def bow(u, v):
        return 8 + u*.72, 26 - u*.28, 35 + v

    rim = [bow(u, v) for u, v in oval(0, 0, 9.5, 6.7)]
    hole = [bow(u, v) for u, v in oval(-2.5, 0, 3.7, 3.3)]
    s.face(rim, EDGE, openings=(hole,))
    warning(s, 24, 6, 57, 27)
