from geometry import BOLD, oval
from scenes.redraws.bike_share import bicycle

DESCRIPTION = "A city bicycle has an open-end wrench resting beside its rear hub."


def draw(s):
    bicycle(s)
    # The angled open jaw faces the hub, while the handle reaches the ground.
    outline = [(14, 23), (9, 24), (4, 21), (2, 17), (-8, 7), (-8, 4),
               (-5, 2), (-2, 3), (7, 13), (12, 13), (16, 16), (17, 20),
               (12, 17), (9, 19), (10, 21)]
    s.face([(x, 6, z) for x, z in outline], BOLD,
           openings=[[(x, 6, z) for x, z in oval(-4, 5.6, 1.05, 1.05)[:-1]]])
