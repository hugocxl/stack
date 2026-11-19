from scenes.redraws._w5 import backpack

DESCRIPTION = "An open hiking daypack holds a capped bottle and a rolled jacket above its front pocket."


def draw(s):
    backpack(s, open_top=True)
