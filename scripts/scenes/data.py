from math import cos, sin, pi
from geometry import BOLD, EDGE, DETAIL, oval


def growth(s):
    for x,h in [(0,13),(26,23),(52,38),(78,59),(104,86)]:
        s.box(x,0,0,20,33,h,3,BOLD if x==104 else EDGE)
    s.line([(0,45,1),(125,45,1)])
    for x in range(10,115,26):
        s.line([(x,45,1),(x,50,1)])


def analytics(s):
    s.box(0,0,0,124,90,8,6)
    heights = [[14,28,40,60],[16,42,45,27],[11,24,37,44]]
    for j,row in enumerate(heights):
        for i,h in enumerate(row):
            x,y = 14+i*27,12+j*25
            s.box(x,y,8,14,13,h,3,BOLD if (i,j)==(1,1) else EDGE)


def forecast(s):
    for y in range(0,77,19):
        s.line([(0,y,0),(132,y,0)])
    for x in range(0,133,22):
        s.line([(x,0,0),(x,76,0)])
    actual = [(0,34,13),(20,34,20),(37,34,18),(56,34,40),(69,34,47)]
    s.line(actual,BOLD)
    for i,z in enumerate((35,63,93)):
        s.line([(69,34,47),(84,34,49),(106,34,z-5),(132,34,z)],EDGE if i==1 else DETAIL,True)
    for x,y,z in actual:
        s.line([(x,y,0),(x,y,z)],dashed=True)
        s.disk(x,y,z,2.5,2.5,2,EDGE)
    s.disk(132,34,63,3,3,3,BOLD)


def monitoring(s):
    for i,y in enumerate((0,31,62)):
        s.box(0,y,0,125,25,5,4)
        points = []
        for k in range(65):
            x = 8+k*1.7
            a = (k-26-i*5)/9
            z = 4 + 28*(1+.1*i)*sin(a*2)*2.71828**(-a*a)
            points.append((x,y+12,17+z))
        s.line(points,BOLD if i==1 else EDGE)
        for x in (20,57,92):
            s.line([(x,y+12,5),(x,y+12,18)],dashed=True)


def heatmap(s):
    grid = [[0,1,1,2,1,0],[1,2,3,4,2,1],[1,3,5,4,3,1],[1,2,4,3,2,1],[0,1,2,1,1,0]]
    s.box(-4,-4,0,119,100,5,6)
    for y,row in enumerate(grid):
        for x,level in enumerate(row):
            h = 4+level**1.6*2.2
            s.box(x*19,y*19,5,15,15,h,2,BOLD if level==5 else EDGE if level>1 else DETAIL)


def segments(s):
    for i,(a,b,h,shift) in enumerate([(5,120,23,0),(125,224,18,12),(229,355,12,0)]):
        angle = (a+b)*pi/360
        x,y = shift*cos(angle), shift*sin(angle)
        base = [(x,y),*oval(x,y,50,50,a,b,38)]
        s.solid(base,0,h,ink=BOLD if i==1 else EDGE)


def experiments(s):
    for x,y,heights in [(0,0,[16,23,45]),(60,24,[21,35,74])]:
        s.box(x,y,0,52,75,6,5)
        for i,h in enumerate(heights):
            s.disk(x+24,y+14+i*22,6,8,8,h,BOLD if h>70 else EDGE)
            s.ellipse(x+24,y+14+i*22,6+h,3.9,3.9)


def conversion(s):
    for p in [(52,52),(28,52),(52,28)]:
        s.line([(*p,20),(*p,87)],dashed=True)
    for z,r in [(0,11),(18,20),(39,30),(64,43),(91,55)]:
        s.ring(52,52,z,r,r,6,3,BOLD if z==91 else EDGE)


def funnel_analysis(s):
    for i,(w,d,z) in enumerate([(110,27,0),(87,25,24),(62,22,48),(41,18,72)]):
        y = i*22
        x = (110-w)/2
        s.box(x,y,z,w,d,6,4,BOLD if i==3 else EDGE)
        for j in range(7-i*2):
            s.disk(x+12+j*(w-24)/max(1,6-i*2),y+d/2,z+6,3,3,5)


def audit_trail(s):
    s.box(0,0,0,138,25,5,6)
    for x,h in [(10,21),(33,30),(58,43),(83,25),(112,56)]:
        s.box(x,8,5,13,10,h,2,BOLD if x==112 else EDGE)
        s.dots(x+4,11,h+5,2,1,4)
    s.line([(16,13,26),(39,13,35),(64,13,48),(89,13,30),(118,13,61)])


FIGURES = [
    (growth,"Growth","An ascending series of columns traces steady growth."),
    (analytics,"Analytics","Three rows of raised bars compare a set of measurements."),
    (forecast,"Forecasting","One observed trend splits into three projected outcomes."),
    (monitoring,"Monitoring","Three offset traces show a pulse across a bank of channels."),
    (heatmap,"Heat map","A concentrated peak rises from a grid of measurements."),
    (segments,"Segmentation","Three wedges separate into distinct cohorts."),
    (experiments,"A/B testing","Two groups of samples sit on separate test platforms."),
    (conversion,"Conversion","Five apertures narrow to a single outlet."),
    (funnel_analysis,"Cohort retention","Fewer samples remain on each successive shelf."),
    (audit_trail,"Activity history","A line connects dated events along a common rail."),
]
