from scenes.redraws._kit import badge

DESCRIPTION = "A long boardroom table has two office chairs and a clock badge attached to its near end."


def office_chair(s, x, y, *, facing_near, arms=False):
    """A chair faces in the positive or negative y direction."""
    back_y = y if facing_near else y + 21
    s.box(x + 3, y + 3, 0, 3, 3, 20, .4)
    s.box(x + 22, y + 3, 0, 3, 3, 20, .4)
    s.box(x + 3, y + 16, 0, 3, 3, 20, .4)
    s.box(x + 22, y + 16, 0, 3, 3, 20, .4)
    s.box(x, y, 20, 28, 24, 4, 3)
    s.box(x + 1, back_y, 24, 26, 3, 20, 1.3)
    if arms:
        for u in (x + 1, x + 25):
            s.tube([(u, y + 12, 24), (u, y + 12, 33),
                    (u, y + 19, 33)], 1.2)


def draw(s):
    office_chair(s, 48, -25, facing_near=True)
    for x in (21, 78):
        s.box(x, 8, 0, 5, 25, 31, 1)
    s.box(0, 0, 31, 102, 41, 5, 3)
    office_chair(s, 25, 44, facing_near=False)
    badge(s, "clock", 102, 23, 36, 15)
