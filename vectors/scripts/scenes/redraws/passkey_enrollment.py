from scenes.redraws._kit import badge
from scenes.redraws._w5 import passkey_credential

DESCRIPTION = "A contact-and-key credential carries a plus badge at its upper-right corner."


def draw(s):
    passkey_credential(s)
    badge(s, "plus", 65, -8, 44, 13)
