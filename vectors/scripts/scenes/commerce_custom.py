"""Compositions where the relationship between parts carries the meaning."""

from geometry import BOLD, DETAIL, EDGE, GUIDE
from scenes.commerce_objects import OBJECTS as SPECIALISTS
from scenes.site_objects import ObjectScene


def place(s, name, x, y, z=0, scale=1, ink=EDGE):
    SPECIALISTS[name][1](ObjectScene(s,(x,y,z),scale,ink))


def stock_scene(s, count, put_back=False):
    s.box(-37,-17,0,74,34,6,3)
    s.box(-37,-17,6,74,4,46,2,DETAIL)
    for x in (-37,34):
        s.box(x,-14,4,3,30,50,1.3)
    for z in (6,28):
        for x in (-23,0,23):
            occupied = count>0
            count -= 1
            if occupied:
                place(s,"parcel",x,8 if count==0 else 0,z,.41,BOLD if count==0 else EDGE)
            else:
                ObjectScene(s,(x,0,z),1,DETAIL).frame(-8,-7,0,16,14,1.5,GUIDE,dashed=True)
        s.box(-37,-14,z+19,74,30,3,2)
    if put_back:
        s.line([(23,1,28),(30,23,32),(36,39,34)],DETAIL,dashed=True)
        place(s,"parcel",38,44,36,.51,BOLD)


def low_stock(s):
    stock_scene(s,1)


def replenished(s):
    stock_scene(s,5,put_back=True)


def catalog_inventory(s):
    stock_scene(s,4)
    s.box(47,-12,4,6,20,48,2)
    for z,width in ((38,9),(30,6),(22,9),(14,4)):
        s.line([(53,-7,z),(53,-7+width,z)],EDGE)


def shipping_threshold(s):
    s.box(-33,-24,0,66,51,8,5)
    s.box(-27,-19,8,54,39,7,3)
    place(s,"parcel",-5,0,15,.78,BOLD)
    x,y=34,17
    s.tube([(x,y,5),(x,y,60)],1,DETAIL)
    for z in (14,24,34,44,54):
        s.line([(x,y,z),(x+5,y,z)],DETAIL)
    s.face([(x,y,55),(x+14,y,55),(x+10,y,49),(x,y,49)],EDGE)
    s.line([(x,y,39),(x-8,y,39)],BOLD)


def variants(s):
    for index,(x,y) in enumerate(((-42,13),(0,0),(42,-13))):
        s.box(x-15,y-13,0,30,26,11,4)
        s.line([(x+11,y+9,11),(x+11,y+9,18)],GUIDE,dashed=True)
        if index==0:
            s.box(x-15,y-13,17,30,26,3,4,BOLD)
            for j in (-7,-2,3,8):
                s.line([(x-10,y+j,20),(x+10,y+j,20)])
        elif index==1:
            s.box(x-15,y-13,17,30,26,6,4)
            s.disk(x,y,23,7,7,2,DETAIL)
        else:
            s.box(x-15,y-13,17,30,26,3,4)
            s.ring(x,y,20,8,8,3,2,DETAIL)


def port(s):
    s.line([(-50,-20,0),(-12,-20,0),(20,7,0),(57,7,0)],DETAIL)
    s.line([(-50,18,0),(-21,18,0),(11,43,0),(58,43,0)],DETAIL)
    place(s,"boat",-1,-2,0,1.23,BOLD)
    place(s,"container",8,-2,11,.62)
    s.box(35,15,0,37,29,7,3)
    for x in (44,57,66):
        s.disk(x,21,7,2,2,4,DETAIL)


def water_limit(s):
    place(s,"tank",-28,-1,0,1.08,BOLD)
    s.tube([(-7,4,10),(28,4,10)],2.8,DETAIL)
    place(s,"valve",32,4,1,.87)
    s.line([(56,4,10),(65,4,10),(65,4,0)],EDGE,dashed=True)
    s.ellipse(65,4,0,4,3,DETAIL)


def falling_emissions(s):
    s.box(-52,-21,0,104,42,4,5,DETAIL)
    xzs=[(-43,50),(-23,41),(-4,28),(16,23),(36,10)]
    for x,z in xzs:
        s.line([(x,1,4),(x,1,z)],GUIDE,dashed=True)
        s.disk(x,1,z,2.5,2.5,2,BOLD if x==36 else DETAIL)
    s.line([(x,1,z+2) for x,z in xzs],BOLD)
    s.line([(23,10,4),(47,10,4)],EDGE)


def isolation(s):
    s.box(-46,-29,0,92,58,4,5,DETAIL)
    place(s,"produce",-22,-1,4,.69)
    s.box(-1,-24,4,2.4,47,23,1.1,DETAIL)
    place(s,"jar",24,1,4,.76,BOLD)
    s.line([(15,18,4),(30,18,4)],EDGE)


def checkout_media(s):
    place(s,"terminal",-20,-3,0,1.13,BOLD)
    place(s,"cardpay",16,9,0,.77)
    place(s,"cardpay",32,22,3,.8)
    place(s,"coin",49,1,0,.42,DETAIL)


def lending_risk(s):
    s.box(-48,-20,0,96,40,5,4,DETAIL)
    s.disk(0,0,5,7.5,7.5,4,EDGE)
    s.tube([(0,0,9),(0,0,37)],2)
    s.tube([(-39,0,43),(38,0,33)],2.5,BOLD)
    for x,z in ((-28,41),(28,34)):
        s.line([(x,0,z),(x,0,z-19)],EDGE)
        s.disk(x,0,z-22,12,11,3)
    s.box(18,-11,5,21,22,6,2,DETAIL)
    s.line([(20,0,11),(37,0,11)],EDGE)


CUSTOM = {
    "product-inventory": ("Two shelves hold stock bins, with empty bays and a tally strip beside them.", catalog_inventory),
    "low-stock": ("One parcel remains among the empty bays of a stock shelf.", low_stock),
    "back-in-stock": ("A replenishment parcel lines up with the last open bay of a stock shelf.", replenished),
    "payment-methods": ("Two chipped cards and a milled coin sit beside a shared payment terminal.", checkout_media),
    "free-shipping-threshold": ("A parcel rests on a counter beside a graduated gauge with a flag at the threshold.", shipping_threshold),
    "product-variants": ("Three identical housings have interchangeable caps with different surface profiles.", variants),
    "international-shipping": ("A corrugated shipping container sits on a barge alongside a receiving dock.", port),
    "financial-risk": ("A travel stop limits the lower pan of a suspended balance.", lending_risk),
    "emissions-reduction": ("Five measurements descend across a chart toward a low target.", falling_emissions),
    "water-conservation": ("A hand valve limits the outflow of a connected water reservoir.", water_limit),
    "allergen-information": ("A divider keeps a marked jar isolated from the common ingredient tray.", isolation),
}
