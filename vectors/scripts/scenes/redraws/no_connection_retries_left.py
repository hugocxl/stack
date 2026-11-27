from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import printed_glyph
from scenes.redraws.attempt_limit_reached import retry_ring

DESCRIPTION = "A thick circular retry arrow surrounds a Wi-Fi mark and carries an X badge at its open tail."


def draw(s):
    retry = retry_ring(s, start=-127, end=-440)
    printed_glyph(retry, "wifi", 0, 0, 23, EDGE)
    badge(s, "x", *retry.point(-24, -27), 13)
