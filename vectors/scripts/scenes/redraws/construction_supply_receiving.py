from scenes.redraws._kit import badge
from scenes.redraws.construction_delivery_staging import timber_pallet

DESCRIPTION = "A check badge marks the delivery label of a pallet loaded with strapped construction timbers."


def draw(s):
    timber_pallet(s)
    badge(s, "check", 88, 6, 41, 13)
