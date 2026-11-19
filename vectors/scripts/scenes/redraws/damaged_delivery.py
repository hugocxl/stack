from geometry import BOLD, DETAIL, EDGE

DESCRIPTION = "A taped shipping carton has a buckled corner with a short jagged tear."


def draw(s):
    # The intact lid stops at the crushed corner. The two jagged walls form the dent.
    back_left = (-26, -21, 42)
    back_right = (26, -21, 42)
    front_left = (-26, 21, 42)
    side_break = (26, -1, 42)
    lip_break = (4, 21, 42)
    crushed_corner = (26, 21, 21)
    front_jag = [lip_break, (9, 21, 36), (13, 21, 37), (18, 21, 29), crushed_corner]
    side_jag = [side_break, (26, 7, 38), (26, 11, 39), (26, 16, 30), crushed_corner]

    s.face([back_left, back_right, side_break, lip_break, front_left], EDGE)
    s.face([front_left, *front_jag, (26, 21, 0), (-26, 21, 0)], EDGE)
    s.face([back_right, *side_jag, (26, 21, 0), (26, -21, 0)], EDGE)
    s.line([lip_break, (16, 11, 34), side_break], DETAIL)
    s.line([(18, 21, 29), (13, 21, 26), (9, 21, 28), (5, 21, 20)], BOLD)
    s.line([(26, 16, 30), (26, 11, 24), (26, 7, 25)], DETAIL)
    for x in (-10, -3):
        s.line([(x, -21, 42), (x, 21, 42), (x, 21, 34)], DETAIL)
