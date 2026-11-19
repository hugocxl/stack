from scenes.new_states import invite_sent
from scenes.redraws._kit import _screen, arrow

DESCRIPTION = "A lined invitation rises from an open envelope with a send arrow at its upper edge."


def draw(s):
    invite_sent(s)
    anchor = (75, 17, 60)
    arrow(s, [_screen(*anchor, 0, 0), _screen(*anchor, 31, 0)], head=13)
