from scenes.redraws._kit import badge
from scenes.redraws.restore_a_draft import written_draft

DESCRIPTION = "A partially written page on a spiral desk pad carries a refresh badge at its upper-right edge."


def draw(s):
    point = written_draft(s)
    badge(s, "refresh", *point(88, 73), 14)
