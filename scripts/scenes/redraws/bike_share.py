from geometry import DETAIL, EDGE, oval

DESCRIPTION = "A step-through city bicycle carries a wire front basket and a small fleet plate."


def bike_point(x, y, z):
    return x, y - x * .28, z


def bicycle(s):
    def line(points, ink=EDGE):
        s.line([bike_point(*point) for point in points], ink)

    def tube(points, radius):
        s.tube([bike_point(*point) for point in points], radius)

    def panel(points, ink=EDGE):
        s.face([bike_point(*point) for point in points], ink)

    for x in (20, 85):
        s.face([bike_point(a, 0, z) for a, z in oval(x, 19, 19, 19)[:-1]],
               openings=[[bike_point(a, 0, z) for a, z in oval(x, 19, 15.7, 15.7)[:-1]]])
        for a, z in ((x - 13, 26), (x + 13, 26), (x, 4)):
            line([(x, 1, 19), (a, 1, z)], DETAIL)

    tube([(20, 1, 19), (44, 2, 42), (52, 2, 17), (20, 1, 19)], 1.15)
    tube([(51, 3, 19), (70, 3, 24), (77, 3, 42)], 2.1)
    tube([(85, 4, 19), (76, 4, 40), (72, 4, 53)], 1.45)
    tube([(44, 3, 42), (42, 3, 50)], 1.15)

    panel([(33, 4, 50), (38, 8, 52), (50, 7, 52), (53, 2, 51), (43, 0, 50)])
    tube([(65, 1, 57), (71, 2, 56), (72, 4, 53), (76, 11, 57), (70, 15, 59)], 1.25)

    s.face([bike_point(a, 5, z) for a, z in oval(51, 17, 4.6, 4.6)[:-1]])
    tube([(52, 6, 17), (56, 7, 11), (61, 9, 11)], 1.1)

    # The basket base sits on a short bracket fixed to the fork.
    tube([(77, 1, 39), (85, 1, 38), (89, 1, 41)], 1)
    panel([(83, -5, 40), (97, -5, 40), (100, -8, 53), (81, -8, 53)])
    panel([(83, -5, 40), (83, 6, 40), (81, 10, 53), (81, -8, 53)])
    panel([(83, 6, 40), (97, 6, 40), (100, 10, 53), (81, 10, 53)])
    panel([(97, -5, 40), (97, 6, 40), (100, 10, 53), (100, -8, 53)])
    for x in (86, 91, 96):
        line([(84 + (x - 83) * .8, 6, 41), (x, 10, 53)], DETAIL)
    line([(82, 8, 47), (99, 8, 47), (99, -6, 47)], DETAIL)


def draw(s):
    bicycle(s)
    s.face([bike_point(x, 6, z) for x, z in ((32, 28), (40, 28), (42, 33), (34, 33))], DETAIL)
