from scenes.redraws._kit import _screen, badge, warning

DESCRIPTION = "A thick warning plate carries an up-arrow badge at its upper right corner."


def draw(s):
    warning(s, 0, 0, 0, 84)
    badge(s, "up", *_screen(0, 0, 0, 34, 50), 13)
