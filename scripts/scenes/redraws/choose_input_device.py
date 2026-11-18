from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import badge
from scenes.systems_shapes import bezel

DESCRIPTION = "A microphone input picker shows two microphone rows with a check badge beside the selected row."


def draw(s):
    s.face([(35, 0, 0), (35, 0, 48), (35, -19, 0)], EDGE)
    s.box(-37, -6, 0, 74, 6, 48, 2)
    for height, scale, active in ((31, 1.45, True), (11, .85, False)):
        ink = EDGE if active else DETAIL
        bezel(s, -30, 0, height - 7 * scale, 60, 14 * scale, ink, 2)
        bezel(s, -21 - 2 * scale, 0, height - scale, 4 * scale, 7 * scale, ink, 2 * scale)
        cradle = oval(-21, height, 3.6 * scale, 3.8 * scale, 180, 360, 15)
        s.line([(x, 0, z) for x, z in cradle], ink)
        stem = height - 5.4 * scale
        s.line([(-21, 0, height - 3.8 * scale), (-21, 0, stem)], ink)
        if active:
            s.line([(-23.5, 0, stem), (-18.5, 0, stem)], ink)
        s.line([(-12, 0, height), (15 if active else 10, 0, height)], ink)
    badge(s, "check", 34, 0, 34, 11)
