from scenes.redraws._w2 import database_transfer

DESCRIPTION = "An arrow points inward toward the side of a cylindrical database."


def draw(s):
    database_transfer(s, inbound=True)
