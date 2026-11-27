from scenes.redraws._kit import badge
from scenes.redraws.product_inventory import draw as rack

DESCRIPTION = "A stocked shelving rack carries a refresh badge as its stock is rotated."


def draw(s):
    rack(s)
    badge(s, "refresh", 92, 30, 62, 12)
