from scenes.infrastructure import server_rack
from scenes.redraws._kit import badge

DESCRIPTION = "A legacy server rack with stacked drive bays carries an upward arrow badge on its top corner."


def draw(s):
    server_rack(s)
    badge(s, "up", 80, 20, 91, 17)
