from geometry import BOLD, EDGE, DETAIL, rounded


def collaboration(s):
    # Three places around one worktable. The foreground chair obscures the leg.
    s.box(44,-12,0,22,24,6,5)
    s.box(50,-6,6,10,11,6,2)
    s.box(42,-13,12,26,24,4,4)
    s.box(42,-14,16,26,5,25,3)
    s.disk(55,50,0,13,13,5)
    s.disk(55,50,5,5,5,27)
    s.disk(55,50,32,53,33,6,BOLD)
    for x,y,w,d in ((44,27,21,12),(16,48,13,16),(78,53,16,11)):
        s.box(x,y,38,w,d,2,2,DETAIL)
        s.line([(x+4,y+4,40),(x+w-4,y+4,40)])
    s.box(60,82,0,25,24,5,4)
    s.box(67,89,5,11,11,6,2)
    s.box(58,82,11,28,25,4,4)
    s.box(58,101,16,28,6,25,3)
    s.box(115,46,0,20,25,5,4)
    s.box(120,53,5,10,11,6,2)
    s.box(112,45,11,25,27,4,4)
    s.box(132,45,16,6,27,25,3)


def automation(s):
    for y in (0,38):
        s.box(0,y,0,123,6,6,2)
    for i in range(7):
        x = 5+i*18
        s.box(x,5,4,8,34,5,3,DETAIL)
    s.box(76,-4,0,10,6,57,2)
    s.box(76,42,0,10,6,57,2)
    s.box(76,-4,54,10,52,9,3)
    s.box(75,14,42,12,15,13,3)
    for x,h in ((12,13),(39,20),(68,18),(101,14)):
        s.box(x,10,9,16,23,h,4,BOLD if x==68 else EDGE)
        s.dots(x+4,16,9+h,2,2)


def handoff(s):
    # Keep the landing area empty so the moving document reads in isolation.
    for x,y in ((0,0),(95,43)):
        s.box(x,y,0,47,52,7,5)
        s.box(x,y,7,47,5,10,2)
        s.box(x,y+47,7,47,5,10,2)
        rim = rounded(x+8,y+9,31,34,4)
        s.line([(*p,7) for p in [*rim,rim[0]]],dashed=True)
    for shift in (-12,12):
        s.line([(42,26+shift,12),(56,30+shift,37),(86,53+shift,37),(96,69+shift,12)],dashed=True)
    s.box(53,22,36,42,40,4,4,BOLD)
    for j,w in enumerate((18,27,21)):
        s.line([(60,31+j*7,40),(60+w,31+j*7,40)])


def planning(s):
    s.box(0,0,0,118,85,9,6)
    for i,x in enumerate((9,44,80)):
        s.box(x,8,9,28,68,2,4,DETAIL)
        for j,(y,h) in enumerate(((15,8),(37,11),(58,6))[:3-i]):
            z = 11 + (21 if i==0 and j==1 else 0)
            if z>11:
                s.line([(x+7,y+10,11),(x+7,y+10,z)],dashed=True)
            s.box(x+3,y,z,22,15,h,3,BOLD if z>11 else EDGE)
            s.line([(x+8,y+5,z+h),(x+19,y+5,z+h)])


def scheduling(s):
    s.box(0,0,0,108,79,9,5)
    for x in range(13,101,22):
        s.line([(x,7,9),(x,71,9)])
    for y in range(7,72,13):
        s.line([(7,y,9),(102,y,9)])
    for x,y,w,h in [(13,9,44,5),(57,22,44,5),(35,35,44,14),(79,48,22,5),(13,61,44,5)]:
        s.box(x,y,9,w,9,h,3,BOLD if h==15 else EDGE)


def version_history(s):
    for i,(x,y,z) in enumerate([(0,0,0),(6,4,13),(13,9,26),(21,18,43),(37,19,63)]):
        s.box(x,y,z,85,65,5,4,BOLD if i==4 else EDGE)
        for k,width in enumerate((43,32,50)):
            s.line([(x+12,y+13+k*10,z+5),(x+12+width,y+13+k*10,z+5)])
        s.box(x+63,y+4,z+5,13,6,2,2)


def search(s):
    s.box(0,0,0,96,78,5,5)
    for j,width in enumerate((67,54,66,48,62,37)):
        s.line([(12,12+j*10,5),(12+width,12+j*10,5)])
    s.tube([(68,45,16),(103,45,16),(115,51,13)],4)
    s.ring(48,40,13,25,25,7,4,BOLD)
    s.ellipse(48,40,20,18,18,DETAIL,178,252)


def branching(s):
    # Parallel tracks branch from and rejoin the main line.
    s.box(0,0,0,146,76,6,7)
    s.tube([(12,17,7),(134,17,7)],2.2)
    lane = []
    for x in range(36,126,2):
        t = (x-36)/88
        u = min(t*3,(1-t)*3,1)
        lane.append((x,17+37*u*u*(3-2*u),7))
    s.tube(lane,2.2,BOLD)
    for x,y in ((14,17),(43,17),(80,17),(110,17),(134,17),(64,54),(100,54)):
        s.disk(x,y,6,5,5,5,BOLD if (x,y)==(100,54) else EDGE)


def inbox(s):
    s.box(0,0,0,108,86,7,5)
    s.box(0,0,7,108,5,36,2)
    for i,(y,h) in enumerate([(12,52),(26,49),(41,59),(57,37)]):
        s.box(13,y,10,83,4,h,2,BOLD if i==2 else EDGE)
        s.line([(23,y+4,h+1),(64,y+4,h+1)])
        s.line([(23,y+4,h-6),(52,y+4,h-6)])
    s.box(0,4,7,5,76,20,3)
    s.box(103,4,7,5,76,20,3)
    s.box(0,80,6,108,6,12,3)


def publish(s):
    # A platen is raised over an open stack, with a finished proof emerging.
    s.box(0,0,0,103,64,10,6)
    s.box(0,0,10,103,10,50,4)
    s.box(0,6,44,103,42,16,5)
    for i in range(3):
        s.box(16,15,11+i*5,71,42,4,3)
    s.box(22,37,27,65,59,4,4,BOLD)
    for j,w in enumerate((41,33,38)):
        s.line([(33,57+j*8,31),(33+w,57+j*8,31)])


FIGURES = [
    (collaboration,"Collaboration","Three chairs gather around a shared worktable."),
    (automation,"Automation","A conveyor feeds parts through an overhead machine."),
    (handoff,"Handoff","A document travels between two stations."),
    (planning,"Project planning","A priority card rises above a board of work in progress."),
    (scheduling,"Scheduling","Raised time blocks occupy different rows on a calendar."),
    (version_history,"Version history","Successive document revisions fan out from the original."),
    (search,"Search","A loupe isolates a passage on a lined sheet."),
    (branching,"Version control","A branch leaves the main track and rejoins it downstream."),
    (inbox,"Inbox","One piece of mail stands above the rest in a letter tray."),
    (publish,"Publishing","A finished proof emerges from a raised platen."),
]
