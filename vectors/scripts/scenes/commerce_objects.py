"""Physical objects for commerce, the built environment, and food service."""

from math import cos, pi, sin

from geometry import BOLD, DETAIL, EDGE, oval

OBJECTS = {}


def motif(name, noun):
    def register(draw):
        OBJECTS[name] = noun, draw
        return draw
    return register


def bars(s, x, y, z, widths):
    for i, width in enumerate(widths):
        s.line([(x,y+i*5,z),(x+width,y+i*5,z)])


@motif("parcel","taped shipping carton")
def parcel(s):
    s.box(-21,-18,0,42,36,32,3)
    for x in (-3,5):
        s.line([(x,-17,32),(x,18,32),(x,18,24)], EDGE)
    s.frame(9,-7,32,9,11,1.4)


@motif("carton","open packing carton")
def carton(s):
    s.box(-22,-19,0,44,38,5,4)
    s.face([(-21,-18,5),(21,-18,5),(21,-18,23),(-21,-18,23)])
    s.face([(-21,-18,23),(21,-18,23),(18,-30,29),(-18,-30,29)])
    s.face([(-21,-18,5),(-21,18,5),(-21,18,23),(-21,-18,23)], DETAIL)
    s.face([(21,-18,5),(21,18,5),(21,18,23),(21,-18,23)])
    s.face([(-21,18,5),(21,18,5),(21,18,23),(-21,18,23)])
    s.face([(-21,18,23),(21,18,23),(17,31,19),(-17,31,19)])


@motif("crushed","carton with a torn corner")
def crushed(s):
    s.face([(-21,-18,0),(22,-18,0),(22,-18,38),(-21,-18,38)], DETAIL)
    s.face([(-21,-18,38),(22,-18,38),(22,1,38),(4,18,28),(-21,18,38)])
    s.face([(22,-18,0),(22,18,0),(22,18,15),(4,18,28),(22,1,38),(22,-18,38)])
    s.face([(-21,18,0),(22,18,0),(22,18,15),(4,18,28),(-21,18,38)])
    s.line([(4,18,28),(-3,18,23),(-9,18,26),(-16,18,18)], BOLD)


@motif("pallet","strapped shipping pallet")
def pallet(s):
    for y in (-19,0,19):
        s.box(-25,y-4,0,50,8,6,1.5)
    for x in (-23,-8,8,23):
        s.box(x-3,-23,6,6,46,4,1.2)
    s.box(-20,-19,10,40,38,23,2)
    s.line([(-20,3,33),(20,3,33),(20,3,10)], EDGE)
    s.line([(-20,-2,33),(20,-2,33),(20,-2,10)], EDGE)
    s.line([(0,19,11),(0,19,33)], DETAIL)


@motif("stock","shelf of occupied stock bins")
def stock(s):
    s.box(-27,-13,0,55,27,5,2)
    s.box(-27,-13,5,55,5,48,2,DETAIL)
    for x in (-26,24):
        s.box(x,-12,4,4,25,49,1.4)
    for z in (6,29):
        for x,y in ((-20,-4),(-4,-6),(11,-4)):
            if z==29 and x==11:
                continue
            s.box(x,y,z,11,14,16,2)
        s.box(-27,-12,z+19,55,26,4,2)


@motif("forklift","warehouse lift with raised forks")
def forklift(s):
    s.box(-24,-12,7,27,24,13,4)
    for x in (-17,0):
        for y in (-12,12):
            s.face([(a,y,b) for a,b in oval(x,7,6,6)])
    s.box(-13,-7,19,12,11,6,2)
    s.tube([(-23,-9,13),(-23,-9,39),(8,-9,39),(8,-9,13)],1.45)
    s.tube([(-23,9,13),(-23,9,39),(8,9,39),(8,9,13)],1.45)
    for y in (-7,7):
        s.box(11,y,4,4,3,32,1)
        s.box(13,y,13,19,3,3,1)


@motif("conveyor","roller conveyor")
def conveyor(s):
    for x in (-24,19):
        s.box(x,-14,0,4,28,20,1.6,DETAIL)
    for y in (-14,12):
        s.box(-27,y,18,55,3,5,1.3)
    for x in range(-22,24,7):
        s.tube([(x,-10,20),(x,11,20)],1.1,DETAIL)


@motif("container","corrugated freight container")
def container(s):
    s.box(-28,-15,0,56,30,26,2)
    for x in range(-24,25,6):
        s.line([(x,15,4),(x,15,22)],DETAIL)
    s.line([(28,0,3),(28,0,23)],EDGE)
    s.line([(28,-5,11),(28,-2,11)],DETAIL)
    s.line([(28,3,11),(28,6,11)],DETAIL)


@motif("flatbed","flatbed truck")
def flatbed(s):
    s.box(-27,-11,8,56,22,5,2)
    s.box(12,-11,13,17,22,21,4)
    s.line([(15,11,25),(26,11,25)])
    s.line([(29,-8,24),(29,8,24)])
    for x in (-20,18):
        for y in (-11,11):
            s.face([(a,y,b) for a,b in oval(x,7,6,6, count=36)])
            s.line([(a,y,b) for a,b in oval(x,7,2.5,2.5,count=24)])


@motif("boat","cargo barge")
def boat(s):
    hull=[(-28,-14),(-19,-19),(18,-19),(30,0),(18,19),(-19,19),(-28,14)]
    s.face([(x,y,9) for x,y in hull])
    s.face([(x,y,1) for x,y in hull],DETAIL)
    s.face([(-28,14,1),(-19,19,1),(18,19,1),(30,0,1),(30,0,9),(18,19,9),(-19,19,9),(-28,14,9)])
    s.box(-25,-10,9,14,20,14,3)
    s.line([(-11,-6,17),(-11,6,17)])


@motif("chiller","insulated cooler with a raised lid")
def chiller(s):
    s.box(-24,-20,0,48,40,22,5)
    s.frame(-18,-14,22,36,28,4)
    s.box(-10,-11,22,20,22,4,3,DETAIL)
    s.face([(-23,-19,22),(23,-19,22),(23,-27,45),(-23,-27,45)])
    for x in (-14,14):
        s.box(x-2,19,9,4,2,7,1)


@motif("gaugecase","caliper and calibrated jaw")
def gaugecase(s):
    s.tube([(-23,-8,4),(28,-8,4)],2)
    s.tube([(-23,-8,4),(-23,13,4),(-18,17,4)],2)
    s.box(4,-12,3,11,9,4,2)
    s.tube([(13,-10,4),(13,13,4),(8,17,4)],2)
    for x in (-14,-8,-2,19,25):
        s.line([(x,-7,6),(x,-2,6)],DETAIL)


@motif("cardpay","chipped payment card")
def cardpay(s):
    s.box(-25,-16,0,50,32,2,3)
    s.frame(-18,-10,2,9,8,1.6,EDGE)
    s.line([(-18,-6,2),(-9,-6,2)])
    bars(s, -18,5,2,(20,13))


@motif("terminal","payment terminal with reader slot")
def terminal(s):
    s.box(-23,-17,0,46,34,10,5)
    s.face([(-19,-13,16),(17,-13,16),(17,11,10),(-19,11,10)])
    s.line([(-12,-7,14),(10,-7,14),(10,3,12),(-12,3,12),(-12,-7,14)])
    s.line([(-14,14,10),(14,14,10)],EDGE)


@motif("wallet","open payment wallet")
def wallet(s):
    s.box(-25,-17,0,50,34,6,4)
    s.face([(-25,-17,4),(-25,-28,10),(25,-28,10),(25,-17,4)])
    s.frame(-20,-12,6,40,22,2)
    s.box(-16,-8,6,29,18,2,2,DETAIL)
    s.box(16,6,6,11,7,3,2)


@motif("coins","coin stacks")
def coins(s):
    for x,y,n in ((-12,-8,3),(12,-3,2),(-5,13,5)):
        for i in range(n):
            s.disk(x,y,2.5*i,8,8,2.5,EDGE if i==n-1 else DETAIL)
        s.ellipse(x,y,2.5*n,5.5,5.5,DETAIL)


@motif("coin","milled coin")
def coin(s):
    s.disk(0,0,0,18,18,4)
    s.ellipse(0,0,4,13,13)
    s.line([(-6,0,4),(6,0,4)],EDGE)


@motif("speedometer","meter with a marked needle")
def speedometer(s):
    s.disk(0,0,0,24,24,7)
    s.line([(x,y,7) for x,y in oval(0,0,18,18,22,290)],DETAIL)
    for a in (45,95,145,195,245):
        angle=a*pi/180
        s.line([(14*cos(angle),14*sin(angle),7),(17*cos(angle),17*sin(angle),7)])
    s.tube([(0,0,7),(11,-7,7)],1,EDGE)
    s.disk(0,0,7,3,3,2)


@motif("dategrid","reservation board with date wells")
def dategrid(s):
    s.box(-26,-22,0,52,44,5,4)
    s.line([(-20,-12,5),(20,-12,5)],EDGE)
    for x in (-15,0,15):
        for y in (-5,7,16):
            s.frame(x-4,y-3,5,8,6,1.4,DETAIL)
    for x in (-15,15):
        s.disk(x,-16,5,2.4,2.4,4)


@motif("locker","pickup locker with an open compartment")
def locker(s):
    s.box(-22,-12,0,44,24,55,3)
    for x,z in ((-18,3),(-18,29),(2,29)):
        s.box(x,12,z,16,1.6,22,1.1,DETAIL)
        s.line([(x+12,13.6,z+11),(x+12,13.6,z+17)],EDGE)
    s.face([(3,13,3),(18,13,3),(18,13,25),(3,13,25)],EDGE)
    s.face([(18,13,3),(27,23,3),(27,23,25),(18,13,25)])


@motif("counter","reception counter with inset work surface")
def counter(s):
    s.box(-27,-13,0,54,26,24,4)
    s.box(-28,-14,24,56,28,4,3)
    s.frame(-20,-9,28,40,18,3)
    s.line([(-17,14,19),(17,14,19)])


@motif("fob","key on a room tag")
def fob(s):
    s.face([(-24,-7,3),(-10,-15,3),(5,-10,3),(5,10,3),(-10,15,3),(-24,7,3)])
    s.ellipse(-15,0,3,3.4,3.4)
    s.ring(0,0,3,7,7,2,1.4,EDGE)
    s.tube([(7,0,4),(27,0,4)],1.7)
    s.line([(21,0,4),(21,5,4),(26,5,4),(26,0,4)],EDGE)


@motif("house","gable-roof house")
def house(s):
    s.box(-20,-15,0,40,30,22,2)
    s.face([(-22,-17,22),(-22,0,37),(22,0,37),(22,-17,22)])
    s.face([(-22,0,37),(22,0,37),(22,17,22),(-22,17,22)])
    s.face([(22,-17,22),(22,17,22),(22,0,37)],DETAIL)
    s.line([(-6,15,2),(-6,15,13),(4,15,13),(4,15,2)],EDGE)
    s.line([(9,15,10),(17,15,10),(17,15,16),(9,15,16),(9,15,10)])


@motif("townhouse","two-storey dwelling")
def townhouse(s):
    s.box(-21,-17,0,42,34,40,2)
    s.box(-23,-18,40,46,36,4,2)
    for x in (-16,3):
        for z in (8,25):
            s.box(x,17,z,12,1.4,9,1.4,DETAIL)
    s.box(7,-8,44,11,11,4,1.5)


@motif("floorcut","open room cutaway")
def floorcut(s):
    s.box(-27,-22,0,54,44,4,2)
    s.box(-26,-21,4,52,3.5,19,1)
    s.box(-26,-18,4,3.5,37,18,1)
    for y,d in ((-18,16),(8,11)):
        s.box(2,y,4,3,d,9,1.2)
    s.box(12,-12,4,10,18,6,1.5,DETAIL)
    s.frame(-17,-11,4,13,20,2)


@motif("framehouse","framed house with exposed studs")
def framehouse(s):
    s.box(-23,-18,0,46,36,4,2)
    for x in (-21,-9,9,21):
        s.box(x-1,-15,4,2,2,27,1)
        s.box(x-1,15,4,2,2,27,1)
    for y in (-15,15):
        s.tube([(-23,y,30),(0,y,46),(23,y,30)],1.35)
        s.tube([(-22,y,31),(22,y,31)],1.25)
    s.tube([(0,-15,46),(0,15,46)],1.4)


@motif("terrain","terraced plot of land")
def terrain(s):
    for i,(x,y,w,d) in enumerate(((-27,-21,54,42),(-24,-20,45,36),(-19,-18,34,28))):
        s.box(x,y,4*i,w,d,4,5,DETAIL if i<2 else EDGE)
    s.line([(-13,-13,12),(-3,-8,12),(2,4,12),(6,6,12)],DETAIL)


@motif("tripod","survey tripod with a sighting scope")
def tripod(s):
    for x,y in ((-16,-13),(-12,15),(17,11)):
        s.tube([(x,y,0),(0,0,30)],1.3)
    s.disk(0,0,30,6,6,5)
    s.box(-12,-5,35,24,10,6,3)


@motif("windowpair","double-pane window section")
def windowpair(s):
    for y in (-8,8):
        s.face([(-23,y,0),(23,y,0),(23,y,42),(-23,y,42)],openings=[[(-17,y,6),(17,y,6),(17,y,36),(-17,y,36)]])
        s.line([(0,y,6),(0,y,36)],DETAIL)
    for x,z in ((-21,1),(21,1),(21,42),(-21,42)):
        s.line([(x,-8,z),(x,8,z)])


@motif("heater","wall-mounted radiator")
def heater(s):
    for x in range(-20,22,8):
        s.box(x,-4,5,5,8,34,2)
    s.tube([(-23,2,10),(27,2,10),(29,7,3)],1.7,DETAIL)
    s.tube([(-22,2,34),(25,2,34)],1.7)


@motif("material","layered tile samples")
def material(s):
    s.box(-24,-16,0,39,29,4,2,DETAIL)
    s.box(-7,-21,4,32,32,5,2)
    s.box(-16,1,10,40,21,6,2)
    for x in range(-12,20,5):
        s.line([(x,7,16),(x+3,15,16)],DETAIL)


@motif("solar","inclined solar collector")
def solar(s):
    s.box(-24,-16,0,48,32,4,2)
    s.tube([(-19,10,4),(-19,-7,23),(19,-7,23),(19,10,4)],1.6)
    s.face([(-24,-17,29),(24,-17,29),(24,15,12),(-24,15,12)])
    for x in (-16,-8,0,8,16):
        s.line([(x,-15,28),(x,13,13)],DETAIL)
    for y in (-7,3):
        z=29-(y+17)*17/32
        s.line([(-22,y,z),(22,y,z)],DETAIL)


@motif("wind","three-bladed wind turbine")
def wind(s):
    s.disk(0,0,0,13,11,5,DETAIL)
    s.tube([(0,0,5),(0,0,48)],2)
    s.box(-4,-6,47,8,13,7,3)
    for angle in (pi/2,7*pi/6,11*pi/6):
        dx,dz=cos(angle),sin(angle)
        s.face([(dx*4,7,50+dz*4),(dx*24-dz*2,7,50+dz*24+dx*2),
                (dx*24+dz*2,7,50+dz*24-dx*2),(dx*6+dz*4,7,50+dz*6-dx*4)])
    s.face([(x,7,z) for x,z in oval(0,50,4,4,count=36)])


@motif("batteryarray","battery bank with terminal row")
def batteryarray(s):
    s.box(-23,-17,0,46,34,7,3)
    for x in (-13,0,13):
        s.box(x-5,-12,7,10,24,24,2)
        for y in (-8,7):
            s.disk(x,y,31,2.2,2.2,3)
    s.line([(-17,17,4),(17,17,4)],DETAIL)


@motif("tank","marked water reservoir")
def tank(s):
    s.disk(0,0,0,21,19,30)
    s.ring(0,0,30,21,19,4,3)
    for z in (7,14,21):
        s.line([(11,16,z),(17,12,z)],DETAIL)
    s.disk(0,0,34,4,4,2,DETAIL)


@motif("valve","hand valve with a flanged pipe")
def valve(s):
    s.tube([(-29,0,9),(28,0,9)],5.6)
    for x in (-20,20):
        s.face([(x,y,z) for y,z in oval(0,9,8,8,count=36)])
    s.box(-8,-8,5,17,16,11,3)
    s.tube([(0,0,16),(0,0,29)],1.7)
    s.ring(0,0,29,13,13,3,2.8)
    s.line([(-10,0,32),(10,0,32)],EDGE)


@motif("sensor","pole-mounted monitoring sensor")
def sensor(s):
    s.disk(0,0,0,12,12,4)
    s.tube([(0,0,4),(0,0,37)],1.6)
    s.box(-9,-6,33,18,12,14,3)
    for z in (37,41,44):
        s.line([(-5,6,z),(5,6,z)],DETAIL)


@motif("collectionbin","collection bin with a hinged lid")
def collectionbin(s):
    s.box(-16,-14,4,32,28,36,3)
    s.box(-17,-15,40,34,30,4,3)
    s.tube([(-7,12,44),(-7,12,48),(7,12,48),(7,12,44)],1.1)
    s.box(-10,14,11,20,1.2,9,2,DETAIL)
    for y in (-9,9):
        s.face([(a,y,b) for a,b in oval(-11,4,4,4,count=32)],DETAIL)


@motif("plantrow","raised garden bed with seedlings")
def plantrow(s):
    s.box(-25,-18,0,50,36,5,4)
    for x,y,height in ((-15,-9,13),(0,-9,10),(15,-9,13),(-15,8,18),(0,8,14),(15,8,18)):
        s.line([(x,y,5),(x,y,height)],EDGE)
        s.face([(x,y,height-4),(x-7,y,height),(x-9,y,height+6),(x-3,y,height+3),(x,y,height)])
        s.face([(x,y,height-2),(x+7,y,height+2),(x+9,y,height+6),(x+3,y,height+5),(x,y,height)])


@motif("tree","young tree on a planting mound")
def tree(s):
    s.disk(0,0,0,18,15,4,DETAIL)
    s.tube([(0,0,4),(0,0,28)],1.7)
    s.face([(-18,0,21),(-14,0,34),(0,0,48),(13,0,39),(18,0,27),(2,0,20)])
    s.line([(0,0,22),(0,0,41)],DETAIL)
    s.line([(-8,0,31),(0,0,26),(9,0,34)],DETAIL)


@motif("street","street cross-section")
def street(s):
    s.box(-28,-19,0,56,38,6,3)
    for y in (-19,12):
        s.box(-28,y,6,56,7,4,2)
    s.line([(-24,0,6),(24,0,6)],EDGE,dashed=True)


@motif("fountain","catchment basin")
def fountain(s):
    s.ring(0,0,0,25,20,10,5)
    s.disk(0,0,0,18,13,3,DETAIL)
    s.tube([(0,0,3),(0,0,23)],2)
    for scale in (-1,1):
        s.line([(scale*14*t,0,23-18*t*t) for t in (k/12 for k in range(13))],DETAIL)


@motif("platter","place setting with a plate")
def platter(s):
    s.disk(-3,0,0,19,18,3)
    s.ellipse(-3,0,3,13,12,DETAIL)
    s.line([(-26,-15,1),(-26,13,1)],EDGE)
    for x in (18,21,24):
        s.line([(x,-12,1),(x,-2,1),(21,1,1),(21,14,1)],DETAIL if x!=21 else EDGE)


@motif("bowl","serving bowl with a broad rim")
def bowl(s):
    s.disk(0,0,0,12,12,3,DETAIL)
    s.face([(x,0,z) for x,z in [(-12,3),(-19,7),(-24,16),(24,16),(19,7),(12,3)]])
    s.ring(0,0,16,24,21,3,3.5)
    s.ellipse(0,0,17,17,15,DETAIL)


@motif("cup","handled measuring cup")
def cup(s):
    s.tube([(17,-1,21),(25,-1,21),(27,-1,17),(25,-1,12),(17,-1,12)],1.5)
    s.disk(0,0,0,17,16,23)
    s.ellipse(0,0,23,13,12,DETAIL)
    for z in (7,13,19):
        s.line([(-4,15.4,z),(4,15.4,z)],EDGE)


@motif("mealbox","divided takeaway carrier")
def mealbox(s):
    s.box(-24,-20,0,48,40,9,5)
    s.face([(-23,-18,9),(23,-18,9),(23,-26,35),(-23,-26,35)])
    s.frame(-20,-14,9,25,29,3)
    s.frame(8,-14,9,12,29,2)
    s.disk(-8,0,9,7,7,5,DETAIL)
    s.ellipse(-8,0,14,4,4,DETAIL)


@motif("lunchbag","insulated food bag")
def lunchbag(s):
    s.box(-19,-15,0,38,30,31,5)
    s.tube([(-9,0,31),(-9,0,40),(9,0,40),(9,0,31)],1.5)
    s.line([(-15,15,23),(15,15,23)],EDGE)
    s.box(-9,15,7,18,2,10,2,DETAIL)


@motif("jar","sealed pantry jar")
def jar(s):
    s.disk(0,0,0,17,16,31)
    s.disk(0,0,31,15,14,4)
    s.line([(-8,14,16),(8,14,16)])
    s.ellipse(0,0,35,11,10,DETAIL)


@motif("produce","basket of rounded vegetables")
def produce(s):
    s.box(-25,-16,0,50,32,12,4)
    for i,(x,y,r) in enumerate(((-11,-5,7),(6,-5,7),(13,8,6),(-8,8,7))):
        s.disk(x,y,12,r,r,10,DETAIL)
        s.line([(x,y,22),(x+3,y-2,25)],EDGE)
    s.box(-25,13,4,50,3,10,2)


@motif("stove","countertop hob")
def stove(s):
    s.box(-24,-20,0,48,40,8,4)
    for x in (-11,11):
        for y in (-9,9):
            s.ellipse(x,y,8,7,7,EDGE)
            s.ellipse(x,y,8,4,4,DETAIL)
    for x in (-14,-5,5,14):
        s.line([(x-1.4,20,4),(x+1.4,20,4)],EDGE)


@motif("fridge","refrigerator with open door")
def fridge(s):
    s.box(-18,-15,0,36,30,57,4)
    for z in (8,25,40):
        s.box(-14,14,z,28,3,3,1.4,DETAIL)
    s.face([(-20,14,4),(-35,27,4),(-35,27,54),(-20,14,54)])
    s.line([(-31,24,20),(-31,24,34)],DETAIL)


@motif("knife","chef knife with a cutting board")
def knife(s):
    s.box(-25,-16,0,50,32,5,5)
    s.face([(-17,8,5),(-12,-4,5),(12,-7,5),(12,4,5),(-17,8,5)])
    s.tube([(9,-5,5),(22,-5,5)],2.3)


@motif("seating","set dining table")
def seating(s):
    for x in (-14,14):
        s.box(x-2,-9,0,4,18,22,1.3)
    s.box(-22,-17,22,44,34,4,3)
    for x in (-10,10):
        s.ellipse(x,0,26,6,6,DETAIL)
        s.line([(x+8,-4,26),(x+8,4,26)],EDGE)


@motif("donationbox","community collection box with coin slot")
def donationbox(s):
    s.box(-24,-18,0,48,36,27,4)
    s.frame(-10,-2,27,20,4,2,EDGE)
    s.box(-13,18,9,26,2,10,2,DETAIL)
    s.line([(-8,20,13),(8,20,13)],EDGE)


@motif("assembly","speaker dais and tiered seating")
def assembly(s):
    s.box(-12,-19,0,24,18,12,3)
    s.box(-7,-12,12,14,7,13,2)
    for y,count in ((9,3),(21,5)):
        for i in range(count):
            x=10*(i-(count-1)/2)
            s.box(x-3,y,0,6,6,5,1.2,DETAIL)
            s.box(x-3,y+4,5,6,2,5,1.2)


@motif("position","survey flag on a marked footing")
def position(s):
    s.disk(0,0,0,12,12,4,DETAIL)
    s.tube([(0,0,4),(0,0,34)],1.1)
    s.face([(0,0,34),(19,0,29),(0,0,24)])


@motif("silo","grain silo with domed roof")
def silo(s):
    s.disk(0,0,0,16,16,40)
    s.ring(0,0,40,16,16,4,2.3)
    s.disk(0,0,44,11,11,4)
    for x in (-5,1):
        s.line([(x,15,3),(x,15,35)],DETAIL)
    for z in range(5,35,6):
        s.line([(-5,15,z),(1,15,z)],DETAIL)
