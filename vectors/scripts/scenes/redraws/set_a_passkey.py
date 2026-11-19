from scenes.redraws._w1 import account_key

DESCRIPTION = "A notched key shows a fingerprint engraved in its round bow."


def draw(s):
    account_key(s, -19, 0, 16, passkey=True)
