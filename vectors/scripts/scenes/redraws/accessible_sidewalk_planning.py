from geometry import DETAIL, EDGE

DESCRIPTION = "A sidewalk corner dips into a wide curb ramp with a tactile paving pad at the crossing."


def draw(s):
    H = 10
    s.box(-70, -40, 0, 48, 50, H, 1.5)
    s.box(22, -40, 0, 48, 50, H, 1.5)
    # The ramp drops from the walk to the road between the two curb blocks.
    s.face([(-22, -40, H), (22, -40, H), (22, -10, H), (-22, -10, H)], EDGE)
    s.face([(22, -10, H), (22, 10, 0), (22, 10, 0)], EDGE)
    s.face([(-22, -10, H), (22, -10, H), (22, 10, 0), (-22, 10, 0)], EDGE)
    s.face([(22, -10, H), (22, 10, 0), (22, -10, 0)], EDGE)
    for i in range(6):
        for j in range(3):
            s.ellipse(-17 + i*6.8, 15 + j*5.5, 0, 1.6, 1.6, EDGE)
    s.line([(-70, 34, 0), (70, 34, 0)], DETAIL, dashed=True)
