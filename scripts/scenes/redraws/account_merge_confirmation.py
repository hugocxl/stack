from scenes.redraws._w1 import intake_arrow, profile_card, screen_point

DESCRIPTION = "Two overlapping profile cards share a curved arrow pointing into the front card."


def draw(s):
    profile_card(s, -43, -11, 4)
    profile_card(s, -21, 9, 0)
    offsets = [(-18, 14), (-11, 23), (-1, 27), (9, 25),
               (17, 18), (22, 8), (23, -1), (22, -8)]
    intake_arrow(s, [screen_point(0, 0, 42, u, v) for u, v in offsets], 10)
