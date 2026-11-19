from scenes.redraws._w5 import physical_key, trust_padlock

DESCRIPTION = "A notched key enters the keyway of a padlock with its shackle raised."


def draw(s):
    trust_padlock(s, open_shackle=True)
    key = lambda x, z: (24, 23 + (24 * .82 - x), 16 + z)
    physical_key(s, key, .82)
