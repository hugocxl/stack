from math import sin, pi
from geometry import BOLD, EDGE, DETAIL


def server_rack(s):
    s.box(0,0,0,84,63,8,5)
    s.box(0,0,8,84,7,88,4)
    s.box(0,5,8,5,58,88,3)
    s.box(79,5,8,5,58,88,3)
    for z in (11,31,51,71):
        reach = 23 if z==51 else 0
        s.box(7,7,z,70,53+reach,15,3,BOLD if reach else EDGE)
        for i in range(6):
            x = 13+i*5
            s.line([(x,60+reach,z+5),(x+2,60+reach,z+5)])
        s.line([(61,60+reach,z+5),(69,60+reach,z+5)])
    s.box(0,0,90,84,63,7,5)


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
    for x,dy in [(17,58),(54,78),(94,61)]:
        s.line([(x,45,27),(x,45,7),(x,dy,7)],dashed=True)
        s.disk(x,dy,0,7,7,6)
    for y in (7,25,45):
        s.face([(x,y,z) for x,z in outline], BOLD if y==45 else EDGE)


def storage(s):
    for z in (0,13,27,42):
        s.disk(40,40,z,43,43,10)
    s.line([(40,40,51),(40,40,64)],dashed=True)
    s.disk(40,40,64,43,43,7,BOLD)
    s.ellipse(40,40,71,31,31)
    s.disk(40,40,71,7,7,5)


def backup(s):
    s.line([(64,32,10),(77,32,10),(88,45,10),(102,45,10)],dashed=True)
    for i,(x,y) in enumerate(((0,0),(94,23))):
        s.box(x,y,0,74,52,11,5,BOLD if i else EDGE)
        s.box(x+5,y+5,11,64,32,2,3,DETAIL)
        for offset in (22,52):
            s.ring(x+offset,y+21,13,10,10,3,3,DETAIL)
        s.line([(x+19,y+44,11),(x+55,y+44,11)])


def load_balancing(s):
    s.box(0,0,0,143,99,5,6)
    s.tube([(71,27,9),(71,50,9),(71,73,9)],1.8,EDGE)
    s.tube([(71,50,9),(28,50,9),(26,54,9),(26,73,9)],1.8,DETAIL)
    s.tube([(71,50,9),(114,50,9),(116,54,9),(116,73,9)],1.8,DETAIL)
    s.box(48,7,5,46,23,21,5,BOLD)
    s.dots(63,14,26,4,3)
    for x in (10,55,100):
        s.box(x,71,5,32,20,12,4)
        s.line([(x+9,82,17),(x+23,82,17)])


def edge_network(s):
    s.box(0,0,0,108,103,5,7)
    nodes = [(15,17,4),(69,13,6),(46,49,13),(12,76,6),(86,76,8)]
    for x,y,h in nodes:
        s.line([(x,y,5),(46,49,5)])
    for x,y,h in nodes:
        s.disk(x,y,5,7+(h==13)*3,7+(h==13)*3,h,BOLD if h==13 else EDGE)


def queues(s):
    s.box(0,0,0,143,32,6,5)
    for x,h in [(9,14),(28,17),(47,13),(66,19),(85,22)]:
        s.box(x,6,6,15,20,h,3,BOLD if x==85 else EDGE)
    s.box(109,-7,0,7,11,44,2)
    s.box(109,29,0,7,11,44,2)
    s.box(108,-7,42,9,47,7,3)
    s.box(124,6,6,14,20,9,3)


def data_pipeline(s):
    # One exposed conduit gives the stages a physically continuous path.
    s.tube([(0,85,26),(151,10,26)],3.2,EDGE)
    for x,y,d,h in ((13,76,42,45),(48,59,36,40),(83,42,30,37),(118,25,24,33)):
        s.box(x,y-d/2,0,13,d,h,3,BOLD if x==83 else EDGE)
        s.line([(x+6,y-d/2+5,h),(x+6,y+d/2-5,h)])


def failover(s):
    s.box(0,0,0,117,76,7,6)
    s.box(10,8,7,39,35,25,5,DETAIL)
    s.box(68,8,7,39,35,25,5,BOLD)
    s.dots(80,19,32,4,3)
    s.line([(30,42,7),(30,55,7),(58,61,7)],dashed=True)
    s.tube([(87,41,9),(87,55,9),(58,61,9)],1.8,BOLD)
    s.disk(58,61,7,7,7,4)
    s.tube([(58,61,14),(72,58,27)],2)


def bandwidth(s):
    s.box(0,0,0,22,99,19,5)
    s.box(121,0,0,22,99,19,5)
    for i in range(5):
        y = 12+i*18
        for x in (11,132):
            s.disk(x,y,19,4,4,4,DETAIL)
        points = [(11+121*k/40, y, 24+41*sin(pi*k/40)) for k in range(41)]
        s.tube(points,1.45,BOLD if i==2 else DETAIL)


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
