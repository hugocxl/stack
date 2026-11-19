from scenes.redraws._kit import badge
from scenes.redraws.keyed_entry_upgrade import deadbolt

DESCRIPTION = "A circular replacement arrow badges a deadbolt with its keyway clearly exposed."


def draw(s):
    deadbolt(s, inserted=False)
    badge(s, "refresh", 28, 8, 65, 14)
