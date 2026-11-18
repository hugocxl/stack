"""Illustrations for the shopping, payment, and fulfillment journey."""

from math import cos, radians, sin

from geometry import BOLD, DETAIL, EDGE, GUIDE, oval, rounded


def shopping_cart(s):
    # A rolling wire basket. Every rail is interpolated from the same taper,
    # so crossing rails meet the corner struts without dangling ends.
    bottom = [(11, 5, 12), (82, 5, 12), (82, 53, 12), (11, 53, 12)]
    rim = [(-2, -3, 55), (94, -3, 55), (94, 64, 55), (-2, 64, 55)]

    def lerp(a, b, rate):
        return tuple(u + (v - u) * rate for u, v in zip(a, b))

    def wire_wall(i, j):
        for height in (.28, .54, .76):
            s.line([lerp(bottom[i], rim[i], height), lerp(bottom[j], rim[j], height)], DETAIL)
        for along in (.24, .48, .72):
            s.line([lerp(bottom[i], bottom[j], along), lerp(rim[i], rim[j], along)], DETAIL)
        s.line([bottom[j], rim[j]], EDGE)
        s.line([rim[i], rim[j]], BOLD)

    for x, y in ((17, 8), (76, 8), (17, 53), (76, 53)):
        s.face([(u, y + 2, z) for u, z in oval(x, 6.8, 6, 6)[:-1]], EDGE)
        s.face([(u, y + 4, z) for u, z in oval(x, 6.8, 5.5, 5.5)[:-1]], EDGE)
    s.box(11, 5, 10, 71, 48, 2, 2)
    wire_wall(0, 1)
    wire_wall(3, 0)
    s.box(19, 8, 12, 28, 20, 27, 3, DETAIL)
    s.box(51, 16, 12, 24, 21, 37, 4, EDGE)
    wire_wall(1, 2)
    wire_wall(2, 3)
    s.line([rim[2], (111, 64, 72), (111, -3, 72), rim[1]], EDGE)
    s.box(108, 12, 69, 6, 37, 6, 2, BOLD)


def checkout(s):
    # Angled POS stand with a shallow display and matching card at its foot.
    s.box(15, 3, 0, 61, 45, 7, 7)
    s.solid(rounded(26, 7, 39, 32, 5), 7, 31,
            top=rounded(27, 9, 37, 23, 4), ink=DETAIL)
    panel = [(7, 6, 57), (82, 6, 57), (82, 61, 19), (7, 61, 19)]
    s.face([(x, y + 2, z - 5) for x, y, z in panel], EDGE)
    s.face(panel, BOLD)

    def on_screen(x, y):
        return (x, y, 57 - (y - 6) * 38 / 55)

    s.line([on_screen(x, y) for x, y in ((15, 14), (73, 14), (73, 44),
                                        (15, 44), (15, 14))], DETAIL)
    s.line([on_screen(x, y) for x, y in ((39, 29), (44, 34), (53, 23))], BOLD)
    for x in (31, 41, 51, 61):
        s.line([on_screen(x, 53), on_screen(x + 4, 53)], EDGE)
    s.box(72, 66, 0, 48, 30, 3, 4)
    s.line([(76, 74, 3), (116, 74, 3)], DETAIL)
    s.line([(78, 87, 3), (91, 87, 3)], DETAIL)


def order_shipped(s):
    for y, width in ((54,18),(65,26),(76,13)):
        s.line([(-width-9,y,8),(-9,y,8)],DETAIL)
    s.box(4, 6, 0, 91, 75, 52, 4, EDGE)
    s.box(3, 5, 51, 93, 77, 8, 5, BOLD)
    s.line([(37, 8, 59), (37, 79, 59)], DETAIL)
    s.line([(54, 8, 59), (54, 79, 59)], DETAIL)
    s.line([(37, 81, 50), (37, 81, 29), (42, 81, 32), (48, 81, 29),
            (54, 81, 32), (54, 81, 50)], DETAIL)
    s.line([(63, 26, 59), (85, 26, 59), (85, 51, 59), (63, 51, 59),
            (63, 26, 59)], EDGE)
    for x in (67, 70, 74, 80):
        s.line([(x, 33, 59), (x, 44, 59)], DETAIL)


def store_pickup(s):
    # Three locker doors and a parcel projecting from the fourth compartment.
    s.box(1, 3, 0, 93, 52, 98, 4, EDGE)
    for x, z in ((5, 5), (5, 50), (50, 50)):
        s.box(x, 55, z, 40, 3, 40, 1.5, DETAIL)
        s.line([(x + 32, 58, z + 24), (x + 32, 58, z + 16)], EDGE)
    s.line([(50, 55, 5), (90, 55, 5), (90, 55, 45), (50, 55, 45),
            (50, 55, 5)], EDGE)
    s.box(56, 54, 6, 24, 32, 23, 2, BOLD)
    s.line([(66, 57, 29), (66, 83, 29)], DETAIL)
    s.face([(90, 56, 5), (118, 71, 5), (118, 71, 45), (90, 56, 45)], EDGE)
    s.line([(114, 69, 21), (114, 69, 29)], DETAIL)


def product_return(s):
    # Open carton with its lowered flaps and a broad path returning to it.
    s.ellipse(48, 44, 0, 74, 64, EDGE, -79, 191)
    angle = radians(191)
    tip = (48 + 74 * cos(angle), 44 + 64 * sin(angle), 0)
    arrowbase = (tip[0] - 13 * sin(angle), tip[1] - 13 * cos(angle), 0)
    s.line([(arrowbase[0] + 7, arrowbase[1], 0), tip,
            (arrowbase[0] - 7, arrowbase[1], 0)], EDGE)
    s.box(16, 13, 0, 66, 60, 6, 4)
    s.face([(16, 13, 6), (82, 13, 6), (82, 13, 35), (16, 13, 35)], EDGE)
    s.face([(16, 13, 35), (82, 13, 35), (79, -7, 48), (19, -7, 48)], EDGE)
    s.face([(16, 13, 6), (16, 73, 6), (16, 73, 35), (16, 13, 35)], DETAIL)
    s.face([(82, 13, 6), (82, 73, 6), (82, 73, 35), (82, 13, 35)], EDGE)
    s.face([(82, 13, 35), (82, 73, 35), (101, 67, 39), (101, 19, 39)], EDGE)
    s.face([(16, 73, 6), (82, 73, 6), (82, 73, 35), (16, 73, 35)], BOLD)
    s.face([(16, 73, 35), (82, 73, 35), (77, 95, 27), (21, 95, 27)], BOLD)


def gift_card(s):
    # Thick sleeve with a lifted gift card, marked by folded ribbon loops.
    s.box(0, 8, 0, 101, 62, 11, 7)
    s.box(11, 15, 11, 80, 45, 3, 4, DETAIL)
    s.line([(43, 6, 11), (43, 66, 11)], DETAIL)
    s.line([(52, 6, 11), (52, 66, 11)], DETAIL)
    for x, y in ((11, 22), (94, 71)):
        s.line([(x, y, 14), (x, y, 40)], GUIDE, dashed=True)
    s.box(6, 13, 40, 90, 54, 3, 6, BOLD)
    for points in [
        [(51, 38, 43), (29, 21, 43), (23, 25, 43), (24, 32, 43),
         (35, 38, 43), (51, 38, 43)],
        [(51, 38, 43), (64, 22, 43), (73, 23, 43), (75, 28, 43),
         (67, 36, 43), (51, 38, 43)],
        [(51, 38, 43), (33, 51, 43), (29, 50, 43)],
        [(51, 38, 43), (64, 52, 43), (68, 52, 43)],
    ]:
        s.line(points, EDGE)


def receipt(s):
    s.box(5, 3, 0, 85, 49, 28, 7)
    s.box(15, 12, 28, 65, 17, 2, 3, DETAIL)
    s.line([(20, 22, 30), (74, 22, 30)], EDGE)
    curve = [(22, 30), (30, 34), (39, 40), (47, 45), (56, 47),
             (64, 44), (72, 38), (80, 30), (89, 23), (98, 20), (107, 21)]
    edge = [(22, y, z) for y, z in curve] + [(70, y, z) for y, z in reversed(curve)]
    s.face(edge, BOLD)
    for i, (y, z) in enumerate(curve[2:-1], start=2):
        s.line([(30, y, z), (47 + 3 * (i % 3), y, z)], DETAIL)
        if i % 2:
            s.line([(59, y, z), (63, y, z)], DETAIL)


def payment_failed(s):
    # A card presented at the edge of an unreadable chip, marked by an
    # interrupted circuit and a small alert pillar.
    s.box(0, 10, 0, 109, 62, 5, 7, EDGE)
    s.line([(51, 24, 5), (98, 24, 5)], DETAIL)
    s.line([(51, 33, 5), (84, 33, 5)], DETAIL)
    s.box(15, 23, 5, 24, 21, 2, 4, BOLD)
    for y in (29, 36):
        s.line([(16, y, 7), (23, y, 7)], DETAIL)
        s.line([(32, y, 7), (38, y, 7)], DETAIL)
    s.line([(27, 23, 7), (27, 44, 7)], DETAIL)
    # Upright triangle faces the camera, with a compact exclamation cutline.
    s.face([(79, 58, 6), (125, 58, 6), (102, 58, 48)], BOLD)
    s.line([(102, 58, 22), (102, 58, 34)], EDGE)
    s.line([(102, 58, 15), (102, 58, 16.5)], EDGE)


def product_comparison(s):
    # A physical comparison on a two-pan balance.
    s.box(40, 33, 0, 62, 40, 7, 7)
    s.box(66, 45, 7, 10, 16, 67, 3)
    s.tube([(7,51,81),(135,51,64)],3.1)
    for x,y,z in ((17,51,36),(123,51,22)):
        s.line([(x,y,z+44),(x-21,y,z),(x+21,y,z),(x,y,z+44)],DETAIL)
        s.disk(x,y,z-4,25,22,4,EDGE if x==17 else BOLD)
    s.box(6,41,36,22,20,18,4)
    s.disk(123,51,22,11,11,21)
    s.disk(71,51,73,6,6,4,BOLD)


def package_tracking(s):
    # Waypoints etched across a folded route map, with one active checkpoint.
    s.face([(0, 9, 9), (38, 0, 0), (38, 65, 0), (0, 74, 9)], DETAIL)
    s.face([(38, 0, 0), (77, 9, 13), (77, 74, 13), (38, 65, 0)], EDGE)
    s.face([(77, 9, 13), (119, 1, 0), (119, 66, 0), (77, 74, 13)], EDGE)
    s.line([(12, 54, 6), (38, 49, 0), (57, 40, 6.3), (77, 43, 13),
            (93, 36, 8), (108, 21, 3.4)], EDGE)
    for x, y, z in ((12, 54, 6), (57, 40, 6.3), (108, 21, 3.4)):
        s.disk(x, y, z, 3, 3, 2, DETAIL)
    s.line([(93, 36, 8), (93, 36, 54)], GUIDE, dashed=True)
    s.box(78, 23, 54, 30, 26, 20, 3, BOLD)
    for x in (90, 95):
        s.line([(x, 24, 74), (x, 48, 74)], DETAIL)


FIGURES = [
    (shopping_cart, "Shopping cart", "A rolling basket holds two selected products."),
    (checkout, "Checkout", "An angled checkout terminal accepts a card."),
    (order_shipped, "Order shipped", "A taped carton with a shipping label is on its way."),
    (store_pickup, "Store pickup", "A parcel protrudes from an opened pickup locker."),
    (product_return, "Product return", "An open carton sits inside a returning route."),
    (gift_card, "Gift card", "A ribbon-marked card lifts from a fitted sleeve."),
    (receipt, "Receipt", "An itemized strip curls up from a countertop printer."),
    (payment_failed, "Payment failed", "An alert rises beside a card with an interrupted chip."),
    (product_comparison, "Product comparison", "Two different products sit on a comparison balance."),
    (package_tracking, "Package tracking", "A parcel hovers over its current waypoint on a folded map."),
]
