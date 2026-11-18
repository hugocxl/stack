from geometry import BOLD, EDGE, DETAIL


def collaboration(s):
    for x,y,h in [(35,0,48),(0,36,36),(73,38,56),(36,75,30)]:
        s.box(x,y,0,33,33,h,4)
        s.dots(x+11,y+10,h,3,3)
    s.box(33,33,16,39,39,12,4,BOLD)
    s.box(42,42,28,21,21,6,4)


def automation(s):
    for y in (0,38):
        s.box(0,y,0,123,6,6,2)
    for i in range(9):
        x = 5+i*14
        s.box(x,5,3,5,34,6,2)
    s.box(76,-4,0,10,6,57,2)
    s.box(76,42,0,10,6,57,2)
    s.box(76,-4,54,10,52,9,3)
    s.box(75,14,42,12,15,13,3)
    for x,h in [(11,14),(40,22),(72,20),(100,16)]:
        s.box(x,10,9,19,23,h,4,BOLD if x==72 else EDGE)
        s.dots(x+5,15,9+h,3,2)


def handoff(s):
    s.box(1,0,0,62,49,9,5)
    s.box(57,45,0,63,49,9,5)
    s.box(1,0,9,6,49,15)
    s.box(114,45,9,6,49,15)
    s.box(8,4,22,50,41,5,3)
    s.box(67,50,16,45,38,5,3)
    for x,y,z in [(19,15,27),(76,59,21)]:
        for j,w in enumerate((20,14,18)):
            s.line([(x,y+j*5,z),(x+w,y+j*5,z)])
    s.line([(49,24,24),(84,37,24),(86,58,24)],dashed=True)
    s.box(37,29,45,49,40,5,3,BOLD)
    for j,w in enumerate((21,28,17)):
        s.line([(45,39+j*6,50),(45+w,39+j*6,50)])


def planning(s):
    s.box(0,0,0,118,85,9,6)
    for i,x in enumerate((9,44,80)):
        s.box(x,8,9,28,68,2,4)
        for j,(y,h) in enumerate(((15,8),(37,11),(58,6))[:3-i]):
            z = 11 + (13 if i==0 and j==1 else 0)
            s.box(x+3,y,z,22,15,h,3,BOLD if z>11 else EDGE)
            s.line([(x+8,y+5,z+h),(x+19,y+5,z+h)])


def scheduling(s):
    s.box(0,0,0,108,79,9,5)
    for x in range(15,106,15):
        s.line([(x,7,9),(x,71,9)])
    for y in range(7,72,13):
        s.line([(7,y,9),(102,y,9)])
    for x,y,w,h in [(15,9,42,6),(47,22,40,8),(31,35,42,15),(60,48,38,7),(16,61,26,5)]:
        s.box(x,y,9,w,9,h,3,BOLD if h==15 else EDGE)


def version_history(s):
    for i,(x,y,z) in enumerate([(0,0,0),(6,4,13),(13,9,26),(21,18,43),(37,19,63)]):
        s.box(x,y,z,85,65,5,4,BOLD if i==4 else EDGE)
        for k,width in enumerate((43,32,50)):
            s.line([(x+12,y+13+k*10,z+5),(x+12+width,y+13+k*10,z+5)])
        s.box(x+63,y+4,z+5,13,6,2,2)


def search(s):
    s.box(0,0,0,108,80,6,5)
    for j,width in enumerate([73,58,63,35,49,58,35]):
        s.line([(14,10+j*9,6),(14+width,10+j*9,6)])
    s.face([(77,47,16),(112,53,16),(113,63,16),(76,57,16)])
    s.ring(55,43,15,25,25,7,4,BOLD)


def branching(s):
    for points in [[(-2,11,0),(58,11,0),(85,42,0),(128,42,0)],
                   [(-2,11,0),(38,11,0),(65,-15,0),(124,-15,0)],
                   [(-2,11,0),(58,11,0),(85,73,0),(118,73,0)]]:
        s.line(points,EDGE)
    for x,y,h in [(65,-15,12),(100,-15,19),(12,11,8),(40,11,14),(85,42,22),(119,42,33),(85,73,13),(118,73,17)]:
        s.disk(x,y,0,8,8,h,BOLD if h==33 else EDGE)


def inbox(s):
    s.box(0,0,0,108,86,7,5)
    s.box(0,0,7,108,5,36,2)
    for i,(y,h) in enumerate([(12,52),(26,49),(41,59),(57,37)]):
        s.box(13,y,10,83,4,h,2,BOLD if i==2 else EDGE)
        s.line([(23,y+4,h+1),(64,y+4,h+1)])
        s.line([(23,y+4,h-6),(52,y+4,h-6)])
    s.box(0,4,7,7,76,28,3)
    s.box(101,4,7,7,76,28,3)
    s.box(0,79,6,108,7,16,3)


def publish(s):
    for i,(x,z) in enumerate([(0,0),(27,14),(54,28),(81,42)]):
        s.box(x,9,z,24,70,14,4)
        s.line([(x+12,17,z+14),(x+12,70,z+14)])
    s.box(84,25,72,47,35,7,4,BOLD)
    s.dots(97,34,79,4,4,4)
    for x,y in [(86,27),(128,58)]:
        s.line([(x,y,57),(x,y,72)],dashed=True)


FIGURES = [
    (collaboration,"Collaboration","Four stations share a central platform."),
    (automation,"Automation","A conveyor feeds parts through an overhead machine."),
    (handoff,"Handoff","A document travels between two stations."),
    (planning,"Project planning","A priority card rises above a board of work in progress."),
    (scheduling,"Scheduling","Raised time blocks occupy different rows on a calendar."),
    (version_history,"Version history","Successive document revisions fan out from the original."),
    (search,"Search","A loupe isolates a passage on a lined sheet."),
    (branching,"Version control","Three parallel branches trace back to a single starting point."),
    (inbox,"Inbox","One piece of mail stands above the rest in a letter tray."),
    (publish,"Publishing","A finished piece lifts off the top step of a production sequence."),
]
