"""Small isometric objects used in editorial and public-service scenes."""
from math import cos, pi, sin
from geometry import BOLD, DETAIL, EDGE, oval, rounded


class At:
    """Place a local object in world coordinates with a uniform scale."""
    def __init__(self, scene, x, y, z, scale=1):
        self.scene, self.origin, self.scale = scene, (x,y,z), scale

    def points(self, points):
        return [(a+x*self.scale,b+y*self.scale,c+z*self.scale) for x,y,z in points
                for a,b,c in [self.origin]]

    def line(self, points, ink=DETAIL, dashed=False):
        self.scene.line(self.points(points),ink,dashed=dashed)

    def face(self, points, ink=EDGE):
        self.scene.face(self.points(points),ink)

    def box(self, x,y,z,w,d,h,r=2,ink=EDGE):
        self.scene.box(*self.points([(x,y,z)])[0],*(v*self.scale for v in (w,d,h,r)),ink)

    def disk(self, x,y,z,rx,ry,h,ink=EDGE):
        self.scene.disk(*self.points([(x,y,z)])[0],*(v*self.scale for v in (rx,ry,h)),ink)

    def ring(self, x,y,z,rx,ry,h,wall,ink=EDGE):
        self.scene.ring(*self.points([(x,y,z)])[0],*(v*self.scale for v in (rx,ry,h,wall)),ink)

    def tube(self, points, radius, ink=EDGE):
        self.scene.tube(self.points(points),radius*self.scale,ink)

    def ellipse(self, x,y,z,rx,ry,ink=DETAIL,start=0,end=360):
        self.line([(a,b,z) for a,b in oval(x,y,rx,ry,start,end)],ink)


def ruled(s, xs, y, z, widths, step=6):
    for i,w in enumerate(widths):
        s.line([(xs,y+i*step,z),(xs+w,y+i*step,z)])


def closed(s, points, ink=DETAIL):
    s.line([*points,points[0]],ink)


def book(s):
    s.box(0,0,0,56,47,5,3)
    s.box(2,2,5,53,43,5,2,DETAIL)
    s.box(0,0,10,56,47,3,3,BOLD)
    s.line([(7,3,13),(7,44,13)])
    ruled(s,15,13,13,(27,21,14),7)


def article(s):
    s.box(0,0,0,56,47,4,3,BOLD)
    s.line([(8,8,4),(48,8,4)],EDGE)
    s.box(8,15,4,18,19,1,2,DETAIL)
    ruled(s,32,15,4,(15,12,15,10),5)
    ruled(s,8,38,4,(40,28),5)


def photo(s):
    s.box(0,0,0,54,45,4,3,BOLD)
    closed(s,[(a,b,4) for a,b in rounded(5,5,44,33,2)])
    s.line([(5,26,4),(17,13,4),(25,22,4),(34,16,4),(49,29,4)],EDGE)
    s.ellipse(39,13,4,3.5,3.5)


def reel(s):
    s.disk(26,24,0,24,21,9)
    s.ellipse(26,24,9,19,16)
    for i in range(5):
        a = i*2*pi/5
        s.ellipse(26+12*cos(a),24+10*sin(a),9,3,2.5,EDGE)
    s.disk(26,24,9,4,4,3,BOLD)
    s.tube([(50,22,5),(59,27,5),(60,37,5)],1.8,DETAIL)


def mic(s):
    s.disk(24,24,0,17,15,5)
    s.disk(24,24,5,3,3,25)
    s.box(15,16,27,18,15,30,7,BOLD)
    for z in (44,49,54):
        s.line([(19,31,z),(29,31,z)])
    s.tube([(13,24,40),(13,24,22),(35,24,22),(35,24,40)],1.8,DETAIL)


def archive(s):
    s.box(0,0,0,54,47,27,4)
    s.box(-1,-1,26,56,49,5,4,BOLD)
    s.box(16,46,13,22,3,7,2)
    s.line([(21,49,16),(32,49,16)])


def folio(s):
    s.box(0,0,0,57,45,6,4,DETAIL)
    s.box(2,5,6,52,36,3,3)
    s.box(3,7,9,50,35,2,3)
    s.box(29,1,0,19,8,3,3,BOLD)
    s.line([(6,33,11),(51,33,11)],EDGE)


def camera(s):
    s.box(0,3,0,55,32,28,5)
    s.box(27,7,28,19,16,5,3)
    s.box(8,10,28,9,8,3,2,DETAIL)
    for y,r,ink in ((35,11,DETAIL),(39,11,BOLD),(40,6,EDGE)):
        s.face([(a,y,b) for a,b in oval(27,14,r,r)[:-1]],ink)


def screen(s):
    s.box(14,14,0,28,21,5,3)
    s.box(24,19,5,8,10,15,2)
    s.box(0,13,18,56,8,35,4,BOLD)
    r=rounded(5,22,46,27,2)
    closed(s,[(x,21,z) for x,z in r])
    s.line([(11,21,28),(20,21,33),(27,21,30),(39,21,40)],EDGE)


def press(s):
    s.box(0,0,0,56,45,6,4)
    s.box(0,0,6,56,8,37,3)
    s.box(0,5,32,56,30,11,3,BOLD)
    s.box(5,18,8,46,43,2,3)
    ruled(s,12,30,10,(30,21,28),6)


def pencil(s):
    s.tube([(4,21,3),(48,21,3)],2.8,BOLD)
    s.face([(0,21,3),(7,18,3),(7,24,3)],EDGE)
    s.box(44,18,0,10,6,6,2)
    s.line([(11,21,6),(43,21,6)],DETAIL)


def calendar(s):
    s.box(0,0,0,55,44,6,4)
    for i in (11,43):
        s.tube([(i,8,5),(i,3,11),(i,0,7)],2,EDGE)
    for x in (11,22,33,44):
        s.line([(x,12,6),(x,37,6)])
    for y in (12,20,28,36):
        s.line([(6,y,6),(49,y,6)])
    s.box(23,21,6,9,7,5,2,BOLD)


def ticket(s):
    outer = [(0,0,2),(48,0,2),(56,7,2),(56,36,2),(0,36,2),(0,25,2),
             (4,21,2),(0,17,2)]
    s.face(outer,BOLD)
    s.line([(39,3,2),(39,33,2)],dashed=True)
    ruled(s,8,10,2,(23,19,23),7)


def badge(s):
    s.box(0,0,0,52,37,3,4,BOLD)
    s.ellipse(14,15,3,5,5,EDGE)
    s.ellipse(14,24,3,9,5,DETAIL,180,360)
    ruled(s,29,11,3,(15,11,16),6)
    s.box(18,1,3,15,4,2,1.3,DETAIL)


def podium(s):
    s.box(7,5,0,43,36,6,3)
    s.box(22,11,6,12,17,28,3)
    s.face([(5,7,41),(51,7,41),(51,37,34),(5,37,34)],BOLD)
    s.tube([(36,11,41),(36,11,54),(33,15,57)],1.2,DETAIL)


def auditorium(s):
    for row in range(3):
        for col in range(4):
            if row==2 and col==1:
                continue
            x, y = col*15,row*15
            s.box(x,y,0,11,13,6,2)
            s.box(x,y,6,11,4,7,1.5,BOLD if (row,col)==(1,1) else DETAIL)


def medal(s):
    s.disk(25,23,0,17,17,5,BOLD)
    s.ellipse(25,23,5,11,11)
    s.line([(20,22,5),(24,27,5),(31,18,5)],EDGE)
    s.face([(15,37,4),(34,37,4),(36,53,1),(25,47,1),(14,53,1)])


def easel(s):
    s.tube([(8,36,0),(25,23,50),(43,36,0)],2,EDGE)
    s.tube([(25,23,38),(25,9,0)],2,DETAIL)
    s.box(2,32,20,48,4,26,3,BOLD)
    s.line([(8,36,26),(20,36,37),(32,36,28),(42,36,38)])


def test_sheet(s):
    s.box(0,0,0,50,48,3,3,BOLD)
    for y in (11,23,35):
        s.ellipse(9,y,3,3,3,EDGE)
        s.line([(17,y,3),(43,y,3)])
    s.line([(6,23,3),(8,26,3),(13,20,3)],BOLD)


def goggles(s):
    for x in (15,41):
        s.box(x-12,10,0,24,23,10,8)
        s.ellipse(x,21,10,8,7,BOLD)
    s.tube([(23,22,3),(27,19,9),(30,21,3)],2,EDGE)
    s.tube([(2,21,4),(-4,15,4),(2,0,4),(54,0,4),(59,15,4),(52,21,4)],1.2,DETAIL)


def records(s):
    s.box(0,0,0,54,44,5,3)
    s.box(6,4,6,45,40,4,3,BOLD)
    ruled(s,13,20,10,(32,25,30),7)
    s.line([(12,12,10),(23,12,10)],EDGE)
    s.line([(17,7,10),(17,17,10)],EDGE)


def pills(s):
    s.box(0,5,0,51,39,3,4)
    for y in (15,29):
        for x in (11,25,39):
            s.disk(x,y,3,5,5,3,BOLD if (x,y)==(25,29) else EDGE)


def bottle(s):
    s.disk(24,23,0,13,13,32)
    s.disk(24,23,32,10,10,10)
    s.disk(24,23,42,8,8,9,BOLD)
    s.ellipse(24,23,15,13,13,DETAIL,0,90)
    s.ellipse(24,23,27,13,13,DETAIL,0,90)


def dumbbell(s):
    s.tube([(8,23,12),(52,23,12)],3.1)
    for x in (10,47):
        s.box(x-6,10,0,12,26,26,5,BOLD if x==47 else EDGE)
        s.line([(x-3,36,12),(x+3,36,12)])


def bed(s):
    for x,y in ((4,4),(4,37),(50,4),(50,37)):
        s.box(x,y,0,5,5,8,1.5)
    s.box(0,0,8,57,44,7,4)
    s.box(2,2,15,53,40,5,5,BOLD)
    s.box(6,4,20,15,34,4,4,DETAIL)
    s.line([(25,3,20),(25,42,20)])


def watch(s):
    s.box(19,-4,0,16,53,3,3)
    s.box(10,9,3,34,28,9,7,BOLD)
    s.ellipse(27,23,12,9,8)
    s.line([(27,23,12),(27,16,12)],EDGE)
    s.line([(27,23,12),(33,25,12)],EDGE)


def specimen(s):
    s.disk(16,18,0,9,9,30)
    s.disk(16,18,28,10,10,5,BOLD)
    s.disk(38,27,0,9,9,22)
    s.disk(38,27,20,10,10,5)
    s.ellipse(38,27,11,9,9,DETAIL,0,90)


def bowl(s):
    s.disk(27,23,0,15,13,4)
    s.disk(27,23,4,22,18,8)
    s.ring(27,23,12,25,21,5,3,BOLD)
    s.tube([(29,20,15),(49,6,26),(60,1,27)],1.6,DETAIL)


def bench(s):
    for x in (5,45):
        s.box(x,7,0,5,29,17,2)
    s.box(0,6,16,56,29,6,4,BOLD)
    s.box(1,7,22,54,6,17,2)
    s.line([(4,21,22),(53,21,22)])


def mat(s):
    s.box(0,4,0,55,35,3,5,BOLD)
    for y in (12,21,30):
        s.line([(7,y,3),(47,y,3)])
    s.disk(40,13,3,8,8,5,DETAIL)


def scale(s):
    s.disk(27,23,0,24,22,7)
    s.disk(27,23,7,21,19,3,BOLD)
    s.ellipse(27,20,10,10,9,EDGE)
    s.line([(27,20,10),(32,14,10)],EDGE)


def map_fold(s):
    panels=[[(0,3,8),(18,0,0),(18,42,0),(0,46,8)],
            [(18,0,0),(39,5,11),(39,47,11),(18,42,0)],
            [(39,5,11),(57,2,3),(57,44,3),(39,47,11)]]
    for panel in panels:
        s.face(panel,EDGE)
    s.line([(5,30,6),(18,26,0),(26,19,4),(39,28,11),(53,15,5)],BOLD)


def suitcase(s):
    s.box(0,4,0,54,41,22,6)
    s.box(0,4,23,54,41,5,6,BOLD)
    s.tube([(15,22,28),(15,22,36),(39,22,36),(39,22,28)],2,EDGE)
    for x in (7,42):
        s.box(x,43,18,6,4,8,1.5)


def vehicle(s):
    for x,y in ((9,7),(45,7),(9,34),(45,34)):
        s.face([(a,y,z) for a,z in oval(x,6,5,5)[:-1]],DETAIL)
    s.box(0,8,6,55,27,13,4)
    s.box(14,10,19,27,23,13,6,BOLD)
    s.line([(20,33,26),(35,33,26)])
    s.line([(46,35,13),(51,35,13)],EDGE)


def landmark(s):
    s.box(0,0,0,55,44,5,4)
    s.box(5,7,5,45,30,8,3,DETAIL)
    s.box(11,10,13,33,23,28,3)
    s.face([(7,35,41),(48,35,41),(27,35,52)],BOLD)
    for x in (17,27,37):
        s.line([(x,33,16),(x,33,36)])


def room(s):
    s.face([(1,2,0),(54,2,0),(54,2,39),(1,2,39)])
    s.face([(1,2,0),(1,44,0),(1,44,39),(1,2,39)])
    s.box(0,0,0,55,46,4,3)
    s.box(13,10,4,36,27,9,4,BOLD)
    s.box(14,11,13,11,25,4,3,DETAIL)
    s.line([(27,11,13),(27,36,13)])


def mountain(s):
    s.box(0,0,0,57,47,4,3)
    s.face([(6,41,4),(26,25,34),(35,14,18),(49,39,4)],BOLD)
    s.line([(18,32,21),(25,30,18),(30,22,25)])
    s.line([(7,43,4),(20,37,4),(31,42,4),(47,34,4)],EDGE)


def stop(s):
    s.box(0,4,0,55,36,5,4)
    s.box(4,8,5,5,23,35,2)
    s.box(46,8,5,5,23,35,2)
    s.box(1,6,38,53,30,6,4,BOLD)
    s.box(12,15,5,31,10,9,3)


def charger(s):
    s.box(8,6,0,37,34,5,4)
    s.box(14,10,5,25,19,37,4,BOLD)
    s.line([(21,29,33),(30,29,33),(30,29,25),(21,29,25),(21,29,33)],EDGE)
    s.tube([(36,22,33),(52,22,28),(53,22,8),(42,22,8),(41,22,19)],1.4,DETAIL)


def rack(s):
    s.box(0,3,0,59,39,5,4)
    for x in (8,28,48):
        points=[(x,13,5),*[(x,y,z) for y,z in oval(22,13,9,10,180,0,18)],(x,31,5)]
        s.tube(points,1.4,BOLD if x==28 else EDGE)


def stage(s):
    s.box(0,3,0,57,42,6,4)
    s.box(0,4,6,57,6,34,3)
    s.box(0,4,39,57,27,5,3,BOLD)
    for x in (10,27,45):
        s.disk(x,22,36,3,3,3,DETAIL)


def sculpture(s):
    s.box(4,3,0,47,40,5,4)
    s.box(11,9,5,34,29,18,3)
    s.face([(14,23,23),(27,18,54),(42,25,23)],BOLD)
    s.face([(27,18,54),(42,25,23),(27,34,28)],EDGE)


def microphone_pair(s):
    for x,y,h in ((8,8,29),(36,26,36)):
        s.disk(x+5,y,0,9,8,4)
        s.disk(x+5,y,4,2,2,h-9)
        s.box(x,y-4,h-5,10,9,16,4,BOLD if x==36 else EDGE)
        s.line([(x+2,y+5,h+7),(x+8,y+5,h+7)])


def dialogue(s):
    shape=[(2,15,5),(13,15,5),(14,15,0),(23,15,5),(53,15,5),
           (57,15,9),(57,15,29),(53,15,33),(2,15,33),(-2,15,29),(-2,15,9)]
    s.face(shape,BOLD)
    for z,w in ((25,37),(18,31),(12,22)):
        s.line([(7,15,z),(7+w,15,z)])


def seat(s):
    s.box(12,7,0,35,33,6,5)
    s.box(23,15,6,14,14,13,3)
    s.box(9,7,19,40,33,7,4,BOLD)
    s.box(9,7,25,40,7,24,4)
    s.line([(14,14,42),(43,14,42)])


def key(s):
    s.ring(15,21,0,12,12,4,4,BOLD)
    s.box(24,17,0,32,7,4,3)
    s.box(46,23,0,5,8,4,2)
    s.box(52,23,0,4,5,4,1.5)


def beacon(s):
    s.disk(27,23,0,17,16,5)
    s.disk(27,23,5,10,10,20)
    s.disk(27,23,25,8,8,9,BOLD)
    for r in (13,21):
        s.ellipse(27,23,29,r,r,DETAIL,20,115)


def pin(s):
    s.ellipse(27,24,0,16,12,DETAIL)
    s.tube([(27,24,3),(27,24,30)],1.7)
    s.disk(27,24,29,10,9,8,BOLD)
    s.ellipse(27,24,37,4,3.5)


OBJECTS = {
    "book": ("a hardbound volume",book), "article": ("a typeset article",article),
    "photo": ("a framed photograph",photo), "reel": ("a film reel",reel),
    "mic": ("a broadcast microphone",mic), "archive": ("an archival box",archive),
    "folio": ("a tabbed folio",folio), "camera": ("a camera with a projecting lens",camera),
    "screen": ("a small display",screen), "press": ("a platen and proof",press),
    "pencil": ("a drafting pencil",pencil), "calendar": ("a marked calendar",calendar),
    "ticket": ("a clipped ticket",ticket), "badge": ("a credential card",badge),
    "podium": ("a speaker's lectern",podium), "seats": ("a bank of seats",auditorium),
    "medal": ("a ribbon medallion",medal), "easel": ("an easel",easel),
    "test": ("a marked answer sheet",test_sheet), "goggles": ("protective goggles",goggles),
    "records": ("a medical record",records), "pills": ("a blister pack",pills),
    "bottle": ("a capped bottle",bottle), "dumbbell": ("a dumbbell",dumbbell),
    "bed": ("a low bed",bed), "watch": ("a wrist tracker",watch),
    "sample": ("two sample vials",specimen), "bowl": ("a bowl and spoon",bowl),
    "bench": ("a slatted bench",bench), "mat": ("an exercise mat",mat),
    "scale": ("a measuring scale",scale), "map": ("a folded route map",map_fold),
    "case": ("a latching suitcase",suitcase), "vehicle": ("a compact vehicle",vehicle),
    "landmark": ("a columned landmark",landmark), "room": ("a cutaway room",room),
    "mountain": ("a mountain relief",mountain), "stop": ("a transit shelter",stop),
    "charger": ("a charging pedestal",charger), "rack": ("a three-hoop rack",rack),
    "stage": ("a raised stage",stage), "sculpture": ("a sculpture on a plinth",sculpture),
    "mics": ("two microphones",microphone_pair), "dialogue": ("a speech panel",dialogue),
    "seat": ("a chair",seat), "key": ("a cut key",key),
    "beacon": ("a raised beacon",beacon), "pin": ("a waypoint pin",pin),
}
