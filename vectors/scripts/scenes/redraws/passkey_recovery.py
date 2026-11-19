from scenes.redraws._kit import badge
from scenes.redraws._w5 import passkey_credential

DESCRIPTION = "A contact-and-key credential carries a curved return-arrow badge at its upper-right corner."


def draw(s):
    passkey_credential(s)
    badge(s, "refresh", 65, -8, 44, 13)
