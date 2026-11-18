from scenes.redraws._w2 import database_transfer

DESCRIPTION = "An arrow points outward from the side of a cylindrical database."


def draw(s):
    database_transfer(s, inbound=False)
