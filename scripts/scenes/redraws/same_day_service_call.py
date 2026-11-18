from scenes.redraws._kit import badge
from scenes.redraws.on_site_arrival_alert import service_van

DESCRIPTION = "A wrench-marked service van carries a clock badge beside the front of its roof."


def draw(s):
    service_van(s)
    badge(s, "clock", 61, 6, 55, 13)
