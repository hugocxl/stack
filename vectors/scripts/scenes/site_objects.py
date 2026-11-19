"""Physical subjects used in the site and workflow illustrations."""

from math import cos, pi, sin

from geometry import BOLD, DETAIL, EDGE, GUIDE, oval, rounded

OBJECTS = {}


def object_(name, noun):
    def register(draw):
        OBJECTS[name] = noun, draw
        return draw
    return register


class ObjectScene:
    """Place one locally authored subject at a position in a composition."""

    def __init__(self, scene, origin, scale, ink):
        self.scene = scene
        self.origin = origin
        self.scale = scale
        self.ink = ink

    def xyz(self, point):
        return tuple(origin + self.scale * offset for origin, offset in zip(self.origin, point))

    def line(self, points, ink=DETAIL, dashed=False):
        self.scene.line([self.xyz(point) for point in points], ink, dashed)

    def face(self, points, ink=None, *, openings=()):
        nested = [[self.xyz(point) for point in polygon] for polygon in openings]
        self.scene.face([self.xyz(point) for point in points], ink or self.ink, openings=nested)

    def tube(self, points, radius, ink=None):
        self.scene.tube([self.xyz(point) for point in points], radius * self.scale, ink or self.ink)

    def box(self, x, y, z, width, depth, height, radius=3, ink=None):
        self.scene.box(*self.xyz((x,y,z)), width*self.scale, depth*self.scale, height*self.scale,
                       radius*self.scale, ink or self.ink)

    def disk(self, x, y, z, rx, ry, height, ink=None):
        self.scene.disk(*self.xyz((x,y,z)), rx*self.scale, ry*self.scale, height*self.scale, ink or self.ink)

    def ring(self, x, y, z, rx, ry, height, wall=4, ink=None):
        self.scene.ring(*self.xyz((x,y,z)), rx*self.scale, ry*self.scale, height*self.scale,
                        wall*self.scale, ink or self.ink)

    def ellipse(self, x, y, z, rx, ry, ink=DETAIL):
        self.scene.ellipse(*self.xyz((x,y,z)), rx*self.scale, ry*self.scale, ink)

    def frame(self, x, y, z, width, depth, radius=3, ink=DETAIL, dashed=False):
        points = rounded(x,y,width,depth,radius)
        self.line([(*point,z) for point in [*points,points[0]]], ink, dashed)


def check(s,x,y,z,scale=1):
    s.line([(x+dx*scale,y+dy*scale,z) for dx,dy in ((-7,4),(-1,5),(-4,-8))], DETAIL)


@object_("sheet","folded sheet")
def sheet(s):
    s.face([(-25,-17,3),(13,-17,3),(25,-5,3),(25,17,3),(-25,17,3)])
    s.line([(13,-17,3),(13,-5,3),(25,-5,3)])
    for y,w in ((-7,25),(0,33),(7,21)):
        s.line([(-18,y,3),(-18+w,y,3)])


@object_("plain","blank sheet")
def plain(s):
    s.box(-24,-16,0,48,32,2,4)


@object_("profile","profile card")
def profile(s):
    s.box(-26,-17,0,52,34,3,4)
    s.ellipse(-13,0,3,7,7,EDGE)
    s.ellipse(-13,-1.5,3,2,2)
    s.line([(-16,3,3),(-13,1,3),(-10,3,3)])
    for i,w in enumerate((20,15,17)):
        s.line([(-1,-5+i*5,3),(w,-5+i*5,3)])


@object_("receipt","itemized slip")
def receipt(s):
    s.face([(-19,-22,4),(19,-22,4),(19,18,4),(14,22,4),(8,18,4),(2,22,4),
            (-4,18,4),(-10,22,4),(-16,18,4),(-19,22,4)])
    for y in (-12,-4,4,12):
        s.line([(-11,y,4),(5,y,4)])
        s.line([(10,y,4),(13,y,4)])


@object_("envelope","sealed envelope")
def envelope(s):
    s.box(-25,-16,0,50,32,5,4)
    s.line([(-22,-12,5),(0,5,5),(22,-12,5)])
    s.disk(0,4,5,4,4,1.5,DETAIL)


@object_("openmail","open envelope")
def openmail(s):
    s.face([(-25,-14,4),(0,-25,32),(25,-14,4)], EDGE)
    s.box(-25,-14,0,50,31,4,3)
    s.line([(-21,13,4),(0,-4,4),(21,13,4)])
    s.box(-16,-9,5,32,15,2,2,DETAIL)


@object_("folder","tabbed folder")
def folder(s):
    s.box(-25,-17,0,50,34,5,4)
    s.box(-21,-12,8,45,23,2.8,3,DETAIL)
    s.face([(-24,12,2),(24,12,2),(24,12,13),(1,12,13),(-3,12,17),(-18,12,17),(-24,12,13)])


@object_("drawer","open drawer")
def drawer(s):
    s.box(-23,-20,0,46,37,18,4,DETAIL)
    s.box(-19,-5,1,38,31,5,3)
    s.box(-19,19,6,38,7,8,3)
    s.line([(-7,26,10),(7,26,10)])


@object_("tray","open tray")
def tray(s):
    s.box(-28,-18,0,56,36,5,5)
    s.box(-28,-18,5,56,4,7,2,DETAIL)
    s.box(-28,-14,5,4,28,5,2)
    s.box(24,-14,5,4,28,5,2)
    s.box(-28,14,5,56,4,6,2)
    s.frame(-19,-10,5,38,19,3,GUIDE,True)


@object_("rack","slotted rack")
def rack(s):
    s.box(-27,-18,0,54,36,6,4)
    for i in range(4):
        x = -23+i*13
        s.box(x,-15,6,3.8,30,15,1.8,DETAIL)


@object_("shelves","open cabinet")
def shelves(s):
    s.box(-26,-14,0,52,5,45,3,DETAIL)
    s.box(-26,-9,0,4,22,44,2)
    s.box(22,-9,0,4,22,44,2)
    for z in (0,20,40):
        s.box(-25,-9,z,50,21,3,2)


@object_("book","open book")
def book(s):
    s.box(-27,-19,0,54,38,3,3,DETAIL)
    s.face([(-26,-18,8),(-5,-18,7),(0,-17,3),(0,18,3),(-5,18,7),(-26,17,8)])
    s.face([(0,-17,3),(5,-18,7),(26,-18,10),(26,17,10),(5,18,7),(0,18,3)])
    for i in range(4):
        y = -10+i*6
        s.line([(-21,y,7.8),(-9,y,7.2)])
        s.line([(8,y,7.7),(16+i%2*4,y,8.8)])


@object_("bound","bound notebook")
def bound(s):
    s.box(-23,-20,0,46,40,13,4,DETAIL)
    s.box(-25,-21,13,50,42,3,4)
    s.line([(-16,-17,16),(-16,17,16)])
    for y in (-11,0,11):
        s.line([(-21,y,16),(-15,y,16)])


@object_("tabs","tabbed index")
def tabs(s):
    s.box(-26,-18,0,52,36,5,4)
    for i,w in enumerate((42,31,38)):
        y = -13+i*8
        s.box(-21,y,5,w,6,5+4*i,2)
        s.line([(-16,y+3,10+4*i),(-8,y+3,10+4*i)])


@object_("stack","staggered stack of cards")
def stack(s):
    for i in range(3):
        x = -26+3*i
        y = -19+2*i
        s.box(x,y,4*i,46,30,3,4,DETAIL if i<2 else s.ink)
    s.line([(-12,-7,11),(12,-7,11)])
    s.line([(-12,1,11),(4,1,11)])


@object_("browser","upright browser frame")
def browser(s):
    s.box(-27,-8,0,54,6,37,4)
    s.line([(-22,-2,28),(22,-2,28)])
    s.line([(-21,-2,32),(-18,-2,32)])
    s.line([(-14,-2,32),(-11,-2,32)])
    s.line([(-6,-2,32),(-3,-2,32)])
    for z,width in ((19,23),(14,17),(9,25)):
        s.line([(-18,-2,z),(-18+width,-2,z)])


@object_("panel","open interface panel")
def panel(s):
    s.box(-26,-5,0,52,6,44,4)
    s.line([(-21,1,34),(21,1,34)])
    s.face([(-20,1,7),(7,1,7),(7,1,29),(-20,1,29)], DETAIL)
    for z in (10,17,24):
        s.line([(12,1,z),(20,1,z)])


@object_("laptop","laptop")
def laptop(s):
    s.box(-26,-15,0,52,35,4,4)
    s.box(-26,-15,4,52,4,32,4)
    s.face([(-21,-11,9),(21,-11,9),(21,-11,30),(-21,-11,30)], DETAIL)
    for y in (-5,0,5):
        s.line([(-18,y,4),(18,y,4)])
    s.frame(-6,10,4,12,6,2)


@object_("phone","handheld device")
def phone(s):
    s.box(-12,-4,0,24,8,43,5)
    s.face([(-9,4,6),(9,4,6),(9,4,36),(-9,4,36)], DETAIL)
    s.line([(-4,4,39),(4,4,39)])


@object_("tablet","drawing tablet")
def tablet(s):
    s.box(-27,-17,0,54,34,5,5)
    s.frame(-21,-12,5,42,24,3)
    s.line([(-7,2,5),(-1,5,5),(9,-5,5)])
    s.line([(-9,-5,5),(3,-5,5)])


@object_("dock","recessed dock")
def dock(s):
    s.box(-26,-16,0,52,32,11,5)
    s.frame(-17,-10,11,34,20,3)
    s.line([(-10,2,11),(10,2,11)])
    s.line([(-8,6,11),(8,6,11)])


@object_("blank","inset blank faceplate")
def blank(s):
    s.box(-24,-16,0,48,32,7,5)
    for x in (-17,17):
        s.ellipse(x,0,7,2.4,2.4)


@object_("swatch","set of material swatches")
def swatch(s):
    for i,(x,y) in enumerate(((-19,-15),(-4,-9),(11,-3))):
        s.box(x,y,2*i,14,29,4,4,DETAIL if i<2 else s.ink)
        s.line([(x+4,y+20,2*i+4),(x+10,y+20,2*i+4)])


@object_("pin","map pin")
def pin(s):
    s.disk(0,0,0,12,12,3,DETAIL)
    s.tube([(0,0,3),(0,0,24)],1.5)
    s.face([(x,-1,z) for x,z in oval(0,32,11,11)[:-1]])
    s.line([(x,-1,z) for x,z in oval(0,32,4,4)])


@object_("map","folded map")
def map_(s):
    for points in (
        [(-26,-17,6),(-9,-17,1),(-9,17,1),(-26,17,6)],
        [(-9,-17,1),(8,-17,9),(8,17,9),(-9,17,1)],
        [(8,-17,9),(25,-17,3),(25,17,3),(8,17,9)],
    ):
        s.face(points)
    s.line([(-22,8,4.8),(-9,1,1),(8,5,9),(21,-7,4.4)])


@object_("steps","low stair")
def steps(s):
    for i in range(4):
        x = -24+i*12
        s.box(x,-15,0,11.7,30,5+i*7,2,DETAIL if i<3 else s.ink)


@object_("ladder","portable ladder")
def ladder(s):
    for x in (-16,16):
        s.tube([(x,-18,0),(x,3,43)],2.4)
    for y,z in ((-12,12),(-6,22),(0,34)):
        s.tube([(-15,y,z),(15,y,z)],1.5,DETAIL)


@object_("threshold","open doorway")
def threshold(s):
    s.box(-27,-12,0,54,26,4,3,DETAIL)
    s.box(-22,-9,4,5,9,42,2.4)
    s.box(17,-9,4,5,9,42,2.4)
    s.box(-23,-9,46,46,9,6,3)
    s.face([(-17,-4,6),(2,13,8),(2,13,43),(-17,-4,44)], DETAIL)
    s.line([(-21,9,4),(20,9,4)])


@object_("roof","protective roof")
def roof(s):
    for x,y in ((-18,-12),(18,-12),(-18,12),(18,12)):
        s.box(x-2,y-2,0,4,4,23,1.3,DETAIL)
    s.face([(-23,-17,24),(23,-17,24),(23,0,40),(-23,0,40)])
    s.face([(-23,0,40),(23,0,40),(23,17,24),(-23,17,24)])


@object_("case","carrying case")
def case(s):
    s.box(-25,-18,0,50,36,15,5)
    s.box(-25,-18,15,50,36,4,5,DETAIL)
    s.tube([(-10,-3,19),(-10,-3,27),(10,-3,27),(10,-3,19)],2.4)
    for x in (-15,13):
        s.box(x,15,9,4,4,8,1.4,DETAIL)


@object_("starter","open welcome folio with a checked card")
def starter(s):
    s.face([(-27,-11,5),(27,-11,5),(27,-23,39),(-27,-23,39)],EDGE)
    s.box(-27,-11,0,54,36,5,4)
    s.box(-23,-6,5,23,24,3,3,DETAIL)
    s.face([(3,-5,6),(24,-5,6),(24,18,6),(3,18,6)],BOLD)
    check(s,14,10,6)
    s.line([(-18,-21,34),(17,-21,34)],GUIDE)
    s.line([(-18,-3,8),(-5,-3,8)])
    s.line([(-18,4,8),(-9,4,8)])
    s.line([(-18,11,8),(-7,11,8)])
    s.box(-27,24,5,54,3.5,5,2)


@object_("crate","crate with loose lid")
def crate(s):
    s.box(-23,-18,0,46,36,19,3)
    for y in (-10,0,10):
        s.line([(-20,y,19),(20,y,19)])
    s.face([(-23,-18,19),(-19,-24,33),(25,-24,33),(23,-18,19)], DETAIL)


@object_("cart","wire basket")
def cart(s):
    back = [(-25,-17,28),(25,-17,28),(18,-12,8),(-18,-12,8)]
    front = [(x,-y,z) for x,y,z in back]
    for points in (back,front):
        s.line([*points,points[0]], EDGE)
        for t in (-.6,0,.6):
            s.line([(24*t,points[0][1],27),(17*t,points[2][1],9)])
    for a,b in zip(back,front):
        s.line([a,b],EDGE)
    for x in (-14,14):
        s.face([(a,14,z) for a,z in oval(x,4,4,4)[:-1]], DETAIL)


@object_("bin","storage bin")
def bin_(s):
    s.box(-24,-17,0,48,34,5,4)
    s.box(-24,-17,5,48,4,17,2,DETAIL)
    s.face([(-24,-13,5),(-24,17,5),(-24,17,14),(-24,-13,22)])
    s.face([(24,-13,5),(24,17,5),(24,17,14),(24,-13,22)])
    s.box(-24,13,5,48,4,9,2)


@object_("tool","T-handled driver")
def tool(s):
    s.tube([(-22,0,4),(16,0,4)],2.9,DETAIL)
    s.box(10,-12,0,12,24,8,3)
    s.line([(15,-7,8),(15,7,8)])


@object_("stylus","drawing stylus")
def stylus(s):
    s.tube([(-19,-10,3),(19,11,3)],2.3)
    s.face([(-19,-12,3),(-19,-8,3),(-26,-15,3)],DETAIL)
    s.line([(9,5,4),(15,8,4)])


@object_("clip","spring clip")
def clip(s):
    s.tube([(-18,-7,3),(13,-7,3),(20,0,4),(13,7,5),(-12,7,5),(-14,2,5),(12,2,5)],1.8)


@object_("clamp","bench clamp")
def clamp(s):
    s.box(-24,-13,0,48,26,6,4)
    s.box(-21,-11,6,10,22,20,3)
    s.box(6,-11,6,10,22,15,3,DETAIL)
    s.tube([(15,0,12),(29,0,12)],2.1)
    s.tube([(30,0,7),(30,0,17)],1.6)


@object_("press","stamping press")
def press(s):
    s.box(-24,-17,0,48,34,6,4)
    for x in (-19,15):
        s.box(x,-12,6,4,5,33,1.5,DETAIL)
    s.box(-24,-15,37,48,28,8,4)
    s.disk(0,0,19,5,5,18,DETAIL)
    s.disk(0,0,15,12,8,4)


@object_("marker","adjustable marker")
def marker(s):
    s.disk(0,0,0,12,10,4,DETAIL)
    s.tube([(0,0,4),(0,0,38)],1.8)
    s.face([(0,0,38),(17,0,33),(0,0,27)])


@object_("dial","index dial")
def dial(s):
    s.disk(0,0,0,20,20,7)
    for i in range(9):
        a = pi*(.18+i*.17)
        s.line([(16*cos(a),16*sin(a),7),(13*cos(a),13*sin(a),7)])
    s.tube([(0,0,7),(9,-8,7)],1.4,DETAIL)
    s.disk(0,0,7,3,3,3)


@object_("bell","service bell")
def bell(s):
    s.disk(0,0,0,20,20,4,DETAIL)
    foot = oval(0,0,17,17)[:-1]
    top = oval(0,0,7,7)[:-1]
    s.scene.solid([s.xyz((*p,0))[:2] for p in foot], s.xyz((0,0,4))[2], 13*s.scale,
                  top=[s.xyz((*p,0))[:2] for p in top], ink=s.ink)
    s.disk(0,0,17,2,2,5,DETAIL)
    s.disk(0,0,22,5,5,3)


@object_("timer","hourglass")
def timer(s):
    s.disk(0,0,0,17,14,3)
    s.face([(-13,0,3),(-5,0,12),(-2,0,16),(-5,0,19),(-13,0,31),(13,0,31),(5,0,19),(2,0,16),(5,0,12),(13,0,3)], DETAIL)
    s.line([(0,0,14),(0,0,7)],GUIDE,True)
    s.line([(-7,0,5),(0,0,8),(7,0,5)])
    s.disk(0,0,31,17,14,3)


@object_("clock","small clock")
def clock(s):
    s.box(-15,-8,0,30,17,4,4,DETAIL)
    s.tube([(0,0,4),(0,0,19)],2,DETAIL)
    s.face([(a,0,z) for a,z in oval(0,25,15,15)[:-1]])
    s.line([(0,0,34),(0,0,25),(7,0,22)],EDGE)
    for x,z in ((0,13),(12,25),(-12,25)):
        s.line([(x,0,z),(x+1.7,0,z)])


@object_("latch","sliding latch")
def latch(s):
    s.box(-26,-12,0,52,24,5,4)
    s.box(-20,-7,5,20,14,7,3,DETAIL)
    s.tube([(-11,0,12),(18,0,12)],2.8)
    s.box(14,-7,5,7,14,7,3,DETAIL)
    s.disk(-9,0,12,4,4,4)


@object_("key","notched key")
def key(s):
    s.ring(-13,0,2,11,11,3,3.4)
    s.face([(-5,-3,4),(23,-3,4),(23,6,4),(18,6,4),(18,3,4),(13,3,4),(13,6,4),(8,6,4),(8,3,4),(-5,3,4)])


@object_("lock","padlock")
def lock(s):
    path = [(-11,0,18),*[(x,0,z) for x,z in oval(0,29,11,12,180,0,22)],(11,0,18)]
    s.tube(path,2.7)
    s.box(-19,-11,0,38,22,22,4)
    s.line([(x,11,z) for x,z in oval(0,13,3,3)],DETAIL)
    s.line([(0,11,10),(0,11,6)])


@object_("reader","credential reader")
def reader(s):
    s.box(-24,-15,0,48,30,11,5)
    s.frame(-18,-10,11,27,18,3)
    s.line([(14,-3,11),(19,-3,11)])
    s.line([(14,2,11),(19,2,11)])


@object_("print","fingerprint reader")
def print_(s):
    s.box(-19,-19,0,38,38,8,6)
    for rx in (5,8,11):
        s.line([(x,y,8) for x,y in oval(0,0,rx,rx*.7,35,320,48)])


@object_("socket","hollow socket")
def socket(s):
    s.box(-22,-18,0,44,36,6,4,DETAIL)
    s.ring(0,0,6,15,12,6,3.8)
    s.line([(12,0,12),(17,0,12)])


@object_("plug","terminal plug")
def plug(s):
    s.tube([(-30,4,3),(-20,4,5),(-14,0,6)],2.1,DETAIL)
    s.box(-17,-10,0,34,20,13,4)
    for y in (-5,4):
        s.box(17,y,4,10,3,4,1)


@object_("slider","linear slider")
def slider(s):
    s.box(-26,-14,0,52,28,7,4)
    s.frame(-19,-3,7,37,6,2)
    s.box(-3,-9,7,13,18,6,3)
    for i in range(5):
        x = -17+i*7
        s.line([(x,8,7),(x,11,7)])


@object_("switch","rocker switch")
def switch(s):
    s.box(-24,-15,0,48,30,6,5)
    s.frame(-17,-10,6,34,20,4)
    s.face([(-14,-7,10),(14,-7,16),(14,7,16),(-14,7,10)])
    s.line([(-5,0,12),(5,0,14)],DETAIL)


@object_("keys","shortcut key bank")
def keys(s):
    s.box(-26,-15,0,52,30,6,4)
    for x,y,h in ((-20,-9,4),(-7,-9,11),(6,-9,5),(-20,4,5),(-7,4,5),(6,4,7)):
        s.box(x,y,6,11,9,h,2,DETAIL if h<10 else s.ink)


@object_("vials","specimen vials")
def vials(s):
    s.box(-24,-12,0,48,24,4,4)
    for x,h in ((-14,22),(0,29),(14,18)):
        s.disk(x,0,4,5,5,h,DETAIL)
        s.disk(x,0,4+h,5.8,5.8,3)


@object_("hub","distribution hub")
def hub(s):
    s.disk(0,0,0,21,18,5)
    for x,y in ((-10,0),(7,-8),(7,8)):
        s.tube([(x*.4,y*.4,5),(x,y,5)],1.5,DETAIL)
        s.disk(x,y,5,3.5,3.5,4,DETAIL)


@object_("bellcap","protective bell cover")
def bellcap(s):
    s.disk(0,0,0,22,18,5,DETAIL)
    for y in (-8,8):
        roof = [(x,y,z) for x,z in oval(0,5,19,22,180,0,24)]
        s.tube(roof,2.1)


@object_("wheel","reel wheel")
def wheel(s):
    s.ring(0,0,0,19,19,5,3)
    s.disk(0,0,0,5,5,5,DETAIL)
    for i in range(4):
        a=i*pi/2
        s.line([(4*cos(a),4*sin(a),5),(15*cos(a),15*sin(a),5)], EDGE)


@object_("tape","tape dispenser")
def tape(s):
    s.box(-22,-15,0,44,30,5,4)
    s.ring(-8,0,5,10,9,8,3)
    s.face([(-8,-6,12),(19,-6,9),(19,6,9),(-8,6,12)],DETAIL)
    s.box(16,-7,5,7,14,4,2)


@object_("cartridge","cartridge")
def cartridge(s):
    s.box(-24,-15,0,48,30,12,4)
    for y in (-7,0,7):
        s.line([(-15,y,12),(4,y,12)])
    s.box(13,-7,3,15,14,5,2,DETAIL)


@object_("chute","intake chute")
def chute(s):
    s.box(-25,-16,0,50,32,5,4)
    s.face([(-22,-11,8),(-22,13,8),(17,13,28),(17,-11,28)])
    s.box(15,-13,7,7,29,23,3,DETAIL)


@object_("ruler","stepped gauge")
def ruler(s):
    s.box(-26,-8,0,52,16,5,3)
    for i in range(7):
        x = -21+i*7
        s.line([(x,-5,5),(x,(-1 if i%2 else 3),5)])
    s.box(10,-2,5,5,9,13,2)


@object_("channel","two-rail channel")
def channel(s):
    s.box(-26,-18,0,52,36,5,4)
    for y in (-15,10):
        s.box(-24,y,5,48,5,8,2,DETAIL)
    s.line([(-20,0,5),(21,0,5)],GUIDE,True)


@object_("peg","alignment peg")
def peg(s):
    s.disk(0,0,0,11,11,4,DETAIL)
    s.disk(0,0,4,7,7,24)
    s.ellipse(0,0,28,3,3)


@object_("stencil","open cutting stencil")
def stencil(s):
    outside = [(*p,4) for p in rounded(-27,-18,54,36,4)]
    opening = [(*p,4) for p in rounded(-15,-8,30,16,5)]
    s.face(outside,openings=(opening,))
    s.ellipse(-21,11,4,2,2)
    s.ellipse(21,-11,4,2,2)


@object_("sample","notched sample block")
def sample(s):
    s.box(-22,-13,0,44,26,10,5)
    s.frame(-14,-7,10,27,14,3)
    s.line([(8,-4,10),(15,-4,10),(15,4,10)])


@object_("rough","unfinished block")
def rough(s):
    s.box(-20,-14,0,40,28,16,2,DETAIL)
    for i in range(5):
        x = -15 + i*6
        s.line([(x,-10,16),(x+5,2,16),(x+4,9,16)])


@object_("bolt","exposed fastener")
def bolt(s):
    s.disk(0,0,0,5,5,19,DETAIL)
    for z in (4,8,12):
        s.line([(-4,2,z),(4,-2,z+3)])
    s.disk(0,0,18,11,9,5)
    s.line([(-7,0,23),(7,0,23)])
    s.line([(0,-5,23),(0,5,23)])


@object_("weight","calibration weight")
def weight(s):
    s.disk(0,0,0,15,15,4,DETAIL)
    s.box(-11,-11,4,22,22,15,4)
    s.tube([(-5,0,19),(-5,0,25),(5,0,25),(5,0,19)],1.7)


@object_("loom","material spool")
def loom(s):
    s.disk(0,0,0,19,15,5)
    s.disk(0,0,5,12,10,17,DETAIL)
    s.disk(0,0,22,19,15,5)
    s.ellipse(0,0,27,5,5)


@object_("wire","coiled connector lead")
def wire(s):
    s.ring(-7,0,1,15,14,3,2.7)
    s.tube([(5,7,3),(13,11,3),(18,9,3)],1.4,DETAIL)
    s.box(16,3,0,10,11,6,2)


@object_("beam","braced span")
def beam(s):
    for x in (-18,18):
        s.box(x-3,-9,0,6,18,19,2.5,DETAIL)
    s.box(-25,-11,19,50,22,6,3)
    s.line([(-17,-8,25),(17,-8,25)])
    s.line([(-17,8,25),(17,8,25)])


@object_("target","concentric locator plate")
def target(s):
    s.box(-23,-17,0,46,34,4,4,DETAIL)
    for r in (6,11,15):
        s.ellipse(0,0,4,r,r,EDGE if r==6 else DETAIL)
    s.disk(0,0,4,2.5,2.5,3)


@object_("lens","inspection loupe")
def lens(s):
    s.tube([(9,8,5),(22,18,5)],3,DETAIL)
    s.ring(-3,-1,3,16,16,5,3.1)
    s.line([(x,y,8) for x,y in oval(-3,-1,10.5,10.5,130,188,14)],GUIDE)


@object_("projector","tabletop projector")
def projector(s):
    s.box(-24,-16,0,48,32,14,5)
    s.line([(x,16,z) for x,z in oval(6,7,7,5)],EDGE)
    for x in (-17,-13,-9):
        s.line([(x,-7,14),(x,7,14)])


@object_("screen","empty display")
def screen(s):
    s.box(-25,-8,0,50,14,4,4,DETAIL)
    s.box(-24,-5,4,48,6,35,4)
    s.face([(-19,1,8),(19,1,8),(19,1,34),(-19,1,34)],DETAIL)


@object_("microphone","desk microphone")
def microphone(s):
    s.disk(0,0,0,13,10,4,DETAIL)
    s.tube([(0,0,4),(0,0,22)],2)
    s.box(-7,-7,20,14,14,20,6)
    for z in (29,32,35):
        s.line([(-4,7,z),(4,7,z)])


@object_("headset","headset")
def headset(s):
    arch = [(x,0,z) for x,z in oval(0,15,20,24,180,0,26)]
    s.tube(arch,2.1)
    for x in (-20,20):
        s.box(x-4,-6,4,8,12,15,3,DETAIL)
    s.tube([(19,4,13),(17,12,10),(10,14,10)],1.25,DETAIL)


@object_("tag","looped tag")
def tag(s):
    s.face([(-20,-13,3),(11,-13,3),(22,-5,3),(22,5,3),(11,13,3),(-20,13,3)])
    s.ellipse(13,0,3,2.5,2.5,EDGE)
    s.tube([(15,0,4),(23,-3,4),(28,0,4),(25,5,4)],1,DETAIL)
    s.line([(-11,-2,3),(2,-2,3)])


@object_("token","profiled token")
def token(s):
    s.disk(0,0,0,17,17,4)
    s.ellipse(0,0,4,12,12)
    check(s,1,2,4,.86)


@object_("check","completion card")
def check_(s):
    s.box(-22,-14,0,44,28,4,4)
    check(s,0,1,4,1.3)


@object_("warning","warning plate")
def warning(s):
    s.face([(-18,0,0),(18,0,0),(0,0,31)])
    s.line([(0,0,20),(0,0,11)],EDGE)
    s.line([(0,0,6),(0,0,5)],EDGE)


@object_("stop","folding barrier")
def stop(s):
    for x in (-19,19):
        s.box(x-3,-8,0,6,16,5,2,DETAIL)
        s.box(x-2,-4,5,4,8,22,2,DETAIL)
    s.box(-24,-3,20,48,8,8,3)
    for x in (-16,-4,8):
        s.line([(x,5,21),(x+5,5,27)])


@object_("cone","striped safety cone")
def cone(s):
    s.box(-15,-15,0,30,30,4,4,DETAIL)
    foot = oval(0,0,11,11)[:-1]
    top = oval(0,0,2.7,2.7)[:-1]
    s.scene.solid([s.xyz((*p,0))[:2] for p in foot], s.xyz((0,0,4))[2], 27*s.scale,
                  top=[s.xyz((*p,0))[:2] for p in top], ink=s.ink)
    s.ellipse(0,0,15,7.4,7.4)


@object_("battery","battery cell")
def battery(s):
    s.box(-25,-12,0,49,24,11,5)
    s.box(24,-5,2,6,10,7,2,DETAIL)
    for i in range(3):
        s.box(-17+i*10,-6,11,7,12,2,2,DETAIL)


@object_("fuse","fuse cartridge")
def fuse(s):
    s.tube([(-23,0,6),(23,0,6)],5)
    for x in (-16,16):
        s.line([(x,-4,6),(x,0,11),(x,4,6)],DETAIL)
    s.line([(-9,0,11),(-2,0,11),(3,0,10),(11,0,10)],DETAIL)


@object_("bench","marked work surface")
def bench(s):
    s.box(-26,-20,0,52,40,6,4)
    for x in (-20,20):
        s.line([(x,-13,6),(x,13,6)],GUIDE,True)
    for y in (-12,12):
        s.line([(-20,y,6),(20,y,6)],GUIDE,True)


@object_("table","small worktable")
def table(s):
    for x,y in ((-19,-11),(19,-11),(-19,11),(19,11)):
        s.box(x-2,y-2,0,4,4,16,2,DETAIL)
    s.box(-26,-17,16,52,34,5,5)


@object_("seat","bench stool")
def seat(s):
    s.disk(0,0,0,12,12,3,DETAIL)
    s.disk(0,0,3,3,3,14,DETAIL)
    s.disk(0,0,17,14,12,4)


@object_("stamp","rubber stamp")
def stamp(s):
    s.box(-17,-12,0,34,24,6,4)
    s.disk(0,0,6,5,5,11,DETAIL)
    s.disk(0,0,17,10,10,6)


@object_("packet","bound packet")
def packet(s):
    s.box(-24,-15,0,48,30,11,4)
    s.line([(-23,-3,11),(23,-3,11)])
    s.line([(-23,4,11),(23,4,11)])
    s.line([(-6,-12,11),(-6,12,11)])
    s.line([(2,-12,11),(2,12,11)])


@object_("mailbox","open mail slot")
def mailbox(s):
    s.box(-24,-13,0,48,26,27,4)
    s.face([(-17,13,8),(17,13,8),(17,13,18),(-17,13,18)],DETAIL)
    s.face([(-17,13,8),(17,13,8),(17,27,6),(-17,27,6)])


@object_("rail","roller rail")
def rail(s):
    s.box(-26,-14,0,52,28,4,4,DETAIL)
    for x in (-18,-7,4,15):
        s.box(x,-11,4,5,22,4,2)
    for y in (-14,10):
        s.box(-26,y,4,52,4,8,2,DETAIL)


@object_("notch","keyed base")
def notch(s):
    s.box(-24,-16,0,48,32,7,4)
    s.line([(-14,-7,7),(8,-7,7),(8,-3,7),(15,-3,7),(15,7,7),(-14,7,7),(-14,-7,7)],EDGE)


@object_("matrix","compatibility board with sockets and mismatched plugs")
def matrix(s):
    s.box(-30,-22,0,60,44,5,5)
    for x in (-17,0,17):
        for y in (-10,9):
            s.frame(x-5,y-4,5,10,8,2,DETAIL)
    s.box(-22,-14,5,10,8,5,2,DETAIL)
    s.disk(0,-10,8,4,4,3,BOLD)
    s.box(12,-14,5,10,8,5,2,DETAIL)
    s.face([(-13,9,8),(-23,14,8),(-23,4,8)],EDGE)
    s.box(12,5,5,10,8,5,2,DETAIL)


@object_("cabinet","tool cabinet")
def cabinet(s):
    s.box(-22,-16,0,44,32,38,4)
    for z in (7,19,30):
        s.line([(-16,16,z),(16,16,z)])
        s.line([(-6,16,z+4),(6,16,z+4)],EDGE)


@object_("branch","branching trace")
def branch(s):
    s.box(-25,-18,0,50,36,4,4,DETAIL)
    s.line([(-19,2,4),(-5,2,4),(5,-8,4),(17,-8,4)],EDGE)
    s.line([(-5,2,4),(6,9,4),(16,9,4)],EDGE)
    for x,y in ((-19,2),(17,-8),(16,9)):
        s.disk(x,y,4,2.8,2.8,3)


@object_("route","marked route strip")
def route(s):
    s.box(-27,-13,0,54,26,4,4,DETAIL)
    s.line([(-21,4,4),(-7,4,4),(4,-4,4),(21,-4,4)],EDGE)
    for x,y in ((-21,4),(-7,4),(21,-4)):
        s.disk(x,y,4,3,3,2.6)


@object_("unmarked","empty timeline strip")
def unmarked(s):
    s.box(-27,-13,0,54,26,4,4,DETAIL)
    s.line([(-21,0,4),(21,0,4)],EDGE)
    for x in (-20,0,20):
        s.line([(x,-3,4),(x,3,4)],GUIDE)


@object_("chart","measurement chart")
def chart(s):
    s.box(-26,-10,0,52,20,5,4,DETAIL)
    for i,h in enumerate((8,13,20,27)):
        s.box(-21+i*10,-6,5,7,12,h,1.6,DETAIL if i<3 else s.ink)


@object_("scale","calibration balance")
def scale(s):
    s.box(-12,-12,0,24,24,5,4,DETAIL)
    s.tube([(0,0,5),(0,0,29)],2.4)
    s.tube([(-25,0,27),(25,0,34)],1.8)
    for x,z in ((-22,14),(22,21)):
        s.line([(x,0,z+13),(x,-8,z),(x,8,z),(x,0,z+13)])
        s.disk(x,0,z-2,10,10,2,DETAIL)


@object_("partition","fitted divider")
def partition(s):
    s.box(-25,-17,0,50,34,5,4)
    s.box(-24,-13,5,48,5,28,2)
    for x in (-18,0,18):
        s.line([(x,-8,30),(x,-8,9)])


@object_("mesh","raised filter screen")
def mesh(s):
    outline = [(*p,8) for p in rounded(-26,-17,52,34,5)]
    s.line([*outline,outline[0]],EDGE)
    for x in range(-18,19,9):
        s.line([(x,-13,8),(x,13,8)])
    for y in range(-10,11,5):
        s.line([(-22,y,8),(22,y,8)])
    for x,y in ((-21,-12),(21,-12),(-21,12),(21,12)):
        s.line([(x,y,0),(x,y,7)],GUIDE)


@object_("floorplan","architectural cutaway")
def floorplan(s):
    s.box(-27,-17,0,54,34,5,4,DETAIL)
    for x,y,w,d,h in ((-23,-13,46,3,19),(-23,-10,3,23,12),(-3,-10,3,17,18),(20,-9,3,20,9)):
        s.box(x,y,5,w,d,h,1.4)
    s.frame(3,-5,12,12,8,1)


@object_("lamp","task lamp")
def lamp(s):
    s.disk(0,2,0,12,11,4,DETAIL)
    s.tube([(0,2,4),(0,2,20),(7,-2,32),(14,-2,32)],1.8)
    s.disk(14,-2,27,8,6,5)
    s.ellipse(14,-2,26,6,5)


@object_("badge","check badge")
def badge(s):
    s.face([(0,-1,34),(15,-1,29),(13,-1,12),(0,-1,3),(-13,-1,12),(-15,-1,29)])
    s.line([(-7,-1,21),(-2,-1,15),(7,-1,26)],EDGE)


@object_("seatmap","seating positions")
def seatmap(s):
    s.box(-25,-17,0,50,34,4,4,DETAIL)
    for i,(x,y) in enumerate(((-12,-8),(0,-8),(12,-8),(-12,7),(0,7),(12,7))):
        s.disk(x,y,4,4.5,4.5,5 if i==4 else 2,EDGE if i==4 else DETAIL)


@object_("cover","sliding protective shell")
def cover(s):
    s.box(-26,-17,0,52,34,15,8)
    s.frame(-17,-9,15,33,18,5)
    s.line([(-7,17,7),(7,17,7)])


@object_("ticket","ticket stub")
def ticket(s):
    pts = [(-24,-10,3),(25,-10,3),(25,-3,3),(21,0,3),(25,3,3),(25,10,3),(-24,10,3),(-24,3,3),(-20,0,3),(-24,-3,3)]
    s.face(pts)
    s.line([(8,-8,3),(8,8,3)],GUIDE,True)
    s.line([(-14,-3,3),(2,-3,3)])
    s.line([(-14,3,3),(-1,3,3)])


@object_("stampwheel","notched selector wheel")
def stampwheel(s):
    s.disk(0,0,0,21,21,7)
    for i in range(8):
        angle = i*pi/4
        x,y = 15*cos(angle),15*sin(angle)
        s.ellipse(x,y,7,2.2,2.2)
    s.disk(0,0,7,7,7,5,DETAIL)


@object_("layer","raised frame")
def layer(s):
    out = [(*p,5) for p in rounded(-26,-17,52,34,4)]
    hole = [(*p,5) for p in rounded(-20,-12,40,24,3)]
    s.face(out,openings=(hole,))
    s.line([(-18,11,4),(17,11,4)],DETAIL)


@object_("punch","hole punch")
def punch(s):
    s.box(-22,-14,0,44,28,5,4,DETAIL)
    s.box(-20,-11,5,10,22,21,2,DETAIL)
    s.face([(-20,-11,26),(21,-11,20),(21,11,20),(-20,11,26)])
    s.disk(13,0,5,3.5,3.5,12,DETAIL)


@object_("gear","toothed drive wheel")
def gear(s):
    rim = []
    for j in range(32):
        radius = 17 if j%4 in (0,3) else 20
        a = j*pi/16
        rim.append((radius*cos(a),radius*sin(a),4))
    hole = [(*p,4) for p in oval(0,0,6,6)[:-1]]
    s.face(rim,openings=(hole,))
    s.ellipse(0,0,4,12,12)


@object_("pencil","marking pencil")
def pencil(s):
    s.tube([(-16,-6,3),(20,8,3)],1.9)
    s.face([(-22,-10,3),(-15,-8,3),(-17,-4,3)],DETAIL)
    s.line([(11,5,3),(17,8,3)],DETAIL)


@object_("bubble","speech panel")
def bubble(s):
    s.face([(-24,0,9),(-16,0,9),(-18,0,2),(-8,0,9),(24,0,9),(24,0,34),(-24,0,34)])
    for z,w in ((27,31),(21,27),(15,16)):
        s.line([(-18,0,z),(-18+w,0,z)])


@object_("window","open sash")
def window(s):
    out = [(x,0,z) for x,z in rounded(-25,1,50,38,4)]
    hole = [(x,0,z) for x,z in rounded(-20,6,40,28,3)]
    s.face(out,openings=(hole,))
    s.face([(-18,0,7),(-18,0,32),(7,-10,29),(7,-10,8)],DETAIL)
    s.line([(-22,4,3),(22,4,3)])


@object_("dualpanel","hinged light and dark panels")
def dualpanel(s):
    s.box(-22,-17,0,44,34,4,4,DETAIL)
    outer = [(x,0,z) for x,z in rounded(-22,5,44,36,4)]
    opening = [(x,0,z) for x,z in rounded(-17,10,34,26,3)]
    s.face(outer,EDGE,openings=(opening,))
    s.face([(-22,2,5),(-22,2,40),(12,14,40),(12,14,5)])
    for z in (16,22,29):
        s.line([(-16,4.1,z),(6,11.9,z)],DETAIL)
    s.tube([(-22,1,7),(-22,1,38)],1.3,DETAIL)
    for x,z in ((14,23),(18,37)):
        s.line([(a,0,b) for a,b in oval(x,z,2,2)],GUIDE)


@object_("embed","media player fitted between paragraph rules")
def embed(s):
    s.box(-29,-7,0,58,7,45,4)
    s.line([(-23,0,36),(23,0,36)],DETAIL)
    s.line([(-23,0,7),(14,0,7)],DETAIL)
    s.line([(-23,0,4),(8,0,4)],DETAIL)
    s.box(-20,0,11,40,3,21,3,BOLD)
    s.face([(-4,3,17),(-4,3,26),(5,3,22)],EDGE)
    s.line([(-16,3,14),(15,3,14)],DETAIL)


@object_("sign","stand with blank sign")
def sign(s):
    s.box(-14,-8,0,28,16,4,4,DETAIL)
    s.tube([(0,0,4),(0,0,19)],2,DETAIL)
    s.box(-23,-4,18,46,5,17,3)
    s.line([(-15,1,27),(15,1,27)])


@object_("port","connector housing")
def port(s):
    s.box(-24,-16,0,48,32,14,5)
    for x in (-15,-2,11):
        s.face([(x,16,5),(x+7,16,5),(x+7,16,10),(x,16,10)],DETAIL)
    s.line([(-14,-8,14),(16,-8,14)])


@object_("lensframe","framed inspection window")
def lensframe(s):
    s.box(-23,-11,0,46,22,4,4,DETAIL)
    s.tube([(-16,0,4),(-16,0,22)],1.8)
    s.tube([(16,0,4),(16,0,22)],1.8)
    out = [(x,0,z) for x,z in rounded(-21,17,42,24,4)]
    hole = [(x,0,z) for x,z in rounded(-16,21,32,16,2)]
    s.face(out, openings=(hole,))
