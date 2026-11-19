from scenes.redraws._w1 import intake_arrow, profile_card, screen_point

DESCRIPTION = "A curved return arrow turns back toward the portrait on a profile card."


def draw(s):
    profile_card(s, -31, 6, 0)
    anchor = (-15, 6, 26)
    offsets = [(-1, 20), (-9, 22), (-18, 20), (-24, 14), (-26, 6),
               (-24, -2), (-18, -6), (-10, -6)]
    intake_arrow(s, [screen_point(*anchor, u, v) for u, v in offsets], 8)
