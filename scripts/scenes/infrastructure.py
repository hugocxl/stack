from math import sin, pi
from geometry import BOLD, EDGE, DETAIL


def server_rack(s):
    s.box(0,0,0,84,63,9,6)
    for z in [13,33,53,75]:
        reach = 20 if z==53 else 0
        s.box(4,2,z,76,59+reach,15,4,BOLD if reach else EDGE)
        for i in range(6):
            x = 13+i*5
            s.line([(x,61+reach,z+5),(x+2,61+reach,z+5)])
        s.line([(61,61+reach,z+5),(69,61+reach,z+5)])


def cloud(s):
    start = (19,28)
    outline = [start]
    for a,b,end in [
        ((-5,28),(-6,60),(16,66)), ((23,68),(28,67),(34,65)),
        ((36,83),(47,95),(59,95)), ((73,95),(83,83),(86,67)),
        ((101,73),(118,61),(117,48)), ((117,34),(108,28),(96,28)),
    ]:
        for i in range(1,17):
            t = i/16
            weights = ((1-t)**3,3*(1-t)**2*t,3*(1-t)*t*t,t**3)
            outline.append(tuple(sum(w*v for w,v in zip(weights,coords)) for coords in zip(start,a,b,end)))
        start = end
    for y in (0,12,24,36,47):
        s.face([(x,y,z) for x,z in outline], BOLD if y==47 else EDGE)
    for x,dy in [(17,58),(54,78),(94,61)]:
        s.line([(x,45,27),(x,45,7),(x,dy,7)],dashed=True)
        s.disk(x,dy,0,7,7,6)


def storage(s):
    for z in (0,13,27,42):
        s.disk(40,40,z,43,43,10)
        s.ellipse(40,40,z+10,33,33)
    s.line([(40,40,51),(40,40,64)],dashed=True)
    s.disk(40,40,64,43,43,7,BOLD)
    for r in (13,25,34):
        s.ellipse(40,40,71,r,r)
    s.disk(40,40,71,7,7,5)


def backup(s):
    s.box(0,3,0,91,74,16,7)
    s.box(8,9,16,75,62,4,4)
    for x in (27,65):
        s.ring(x,36,20,14,14,6,4)
    s.line([(27,49,24),(34,61,24),(59,61,24),(65,49,24)])
    s.box(105,15,0,40,61,13,5,BOLD)
    s.line([(113,52,13),(135,52,13)])
    s.line([(83,28,20),(108,28,20)],dashed=True)


def load_balancing(s):
    s.box(45,-10,0,38,28,27,5,BOLD)
    s.dots(59,-2,27,3,3)
    for i,x in enumerate((0,45,90)):
        s.line([(64,18,10),(64,37,10),(x+19,37,10),(x+19,68,10)],EDGE)
        s.box(x,68,0,38,32,16+i*5,5)
        s.dots(x+12,78,16+i*5,3,3)


def edge_network(s):
    s.box(0,0,0,108,103,5,7)
    nodes = [(15,17,4),(69,13,6),(46,49,13),(12,76,6),(86,76,8)]
    for x,y,h in nodes:
        s.line([(x,y,5),(46,49,5)])
    for x,y,h in nodes:
        s.disk(x,y,5,7+(h==13)*3,7+(h==13)*3,h,BOLD if h==13 else EDGE)
    for r in (14,20,26):
        s.ellipse(46,49,5,r,r,DETAIL,198,338)


def queues(s):
    s.box(0,0,0,143,32,6,5)
    for x,h in [(9,14),(28,17),(47,13),(66,19),(85,22)]:
        s.box(x,6,6,15,20,h,3,BOLD if x==85 else EDGE)
    s.box(109,-7,0,7,11,44,2)
    s.box(109,29,0,7,11,44,2)
    s.box(108,-7,42,9,47,7,3)
    s.box(124,6,6,14,20,9,3)


def data_pipeline(s):
    segments = [(0,0,24,49),(38,16,19,39),(76,28,15,31),(114,37,11,24)]
    for (x,z,_,_), (next_x,next_z,_,_) in zip(segments,segments[1:]):
        for y in (18,24,30):
            s.line([(x+19,y,z+12),(next_x+1,y,next_z+7)],EDGE)
    for i,(x,z,w,d) in enumerate(segments):
        s.box(x,(49-d)/2,z,21,d,w,4,BOLD if i==2 else EDGE)
        s.dots(x+7,(49-d)/2+6,z+w,2,4,4)


def failover(s):
    s.ellipse(94,68,0,31,31,DETAIL,25,320)
    s.box(1,7,0,47,47,18,5)
    s.box(70,44,0,47,47,18,5)
    s.line([(45,25,19),(83,25,19),(83,55,19)],dashed=True)
    s.box(4,10,24,41,41,26,5)
    s.box(73,47,21,41,41,37,5,BOLD)
    s.dots(86,59,58,4,4)


def bandwidth(s):
    s.box(0,0,0,18,104,27,5)
    s.box(126,0,0,18,104,27,5)
    for i in range(7):
        y = 10+i*14
        points = [(18+108*k/40, y+7*sin(pi*k/40)*sin(i*.5), 12+37*sin(pi*k/40)) for k in range(41)]
        s.line(points,BOLD if i==3 else EDGE)
    s.dots(7,11,27,2,9,9)
    s.dots(132,11,27,2,9,9)


FIGURES = [
    (server_rack,"Server capacity","One blade slides out of a four-unit server rack."),
    (cloud,"Cloud services","A layered cloud rises above three connected endpoints."),
    (storage,"Storage","A platter floats above a stack of disks."),
    (backup,"Backups","A reel cartridge sits beside a second copy."),
    (load_balancing,"Load balancing","A single intake distributes requests across three workers."),
    (edge_network,"Edge network","A surface links four peripheral nodes to one hub."),
    (queues,"Request queue","Requests line up to pass through a single gate."),
    (data_pipeline,"Data pipeline","Four linked processing stages narrow the incoming stream."),
    (failover,"Failover","A standby unit is ready beside the primary system."),
    (bandwidth,"Bandwidth","Parallel fibers carry traffic between two terminal blocks."),
]
