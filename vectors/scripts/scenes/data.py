from math import cos, exp, sin, pi
from geometry import BOLD, EDGE, DETAIL, oval


def growth(s):
    for x,h in [(0,13),(26,23),(52,38),(78,59),(104,86)]:
        s.box(x,0,0,20,33,h,3,BOLD if x==104 else EDGE)
    s.line([(0,45,1),(125,45,1)])
    for x in range(10,115,26):
        s.line([(x,45,1),(x,50,1)])


def analytics(s):
    s.box(0,0,0,124,90,8,6)
    for y in (12,39,66):
        s.line([(8,y,8),(115,y,8)])
    heights = [[16,39,60],[27,48,41],[15,23,34]]
    for j,row in enumerate(heights):
        for i,h in enumerate(row):
            x,y = 14+i*37,14+j*25
            s.box(x,y,8,19,12,h,3,BOLD if (i,j)==(2,0) else EDGE)


def forecast(s):
    s.box(0,0,0,150,64,5,5,DETAIL)
    for x in (18,43,67,94,121,145):
        s.line([(x,51,5),(x,57,5)])
    s.line([(10,53,5),(145,53,5)])
    s.line([(77,32,5),(77,32,45)],EDGE,dashed=True)
    actual = [(11,32,19),(29,32,29),(45,32,24),(61,32,40),(77,32,46)]
    s.tube(actual,1.25,BOLD)
    for i,z in enumerate((26,62,96)):
        s.line([(77,32,46),(92,32,49),(113,32,(z+49)/2),(141,32,z)],EDGE,dashed=True)
        s.disk(141,32,z,2.8,2.8,3,BOLD if i==1 else DETAIL)


def monitoring(s):
    s.box(4,4,0,117,46,6,5)
    s.box(0,12,6,125,9,91,5)
    for i,altitude in enumerate((29,53,77)):
        s.line([(10,21,altitude),(115,21,altitude)],DETAIL,dashed=True)
        points = []
        for k in range(65):
            x = 10+k*1.64
            a = (k-26-i*5)/9
            z = altitude + (12+2*i)*sin(a*2)*exp(-a*a)
            points.append((x,21,z))
        s.line(points,BOLD if i==1 else EDGE)


def heatmap(s):
    grid = [[0,1,2,1,0],[1,3,4,2,1],[2,4,5,3,1],[1,2,3,2,0],[0,1,1,0,0]]
    s.box(-4,-4,0,115,115,5,6)
    for y,row in enumerate(grid):
        for x,level in enumerate(row):
            h = 2+level**1.6*2.2
            s.box(x*22,y*22,5,18,18,h,2,BOLD if level==5 else EDGE if level>1 else DETAIL)


def segments(s):
    for i,(a,b,h,shift) in enumerate([(197,351,12,0),(9,116,17,21),(126,188,12,0)]):
        angle = (a+b)*pi/360
        x,y = shift*cos(angle), shift*sin(angle)
        base = [(x,y),*oval(x,y,50,50,a,b,38)]
        s.solid(base,0,h,ink=BOLD if i==1 else EDGE)


def experiments(s):
    for x,y,heights in [(0,0,[16,24,36]),(73,0,[17,31,53])]:
        s.box(x,y,0,53,75,6,5)
        for i,h in enumerate(heights):
            s.disk(x+26,y+14+i*23,6,8,8,h,BOLD if h==53 else EDGE)
            s.ellipse(x+26,y+14+i*23,6+h,3.9,3.9)


def conversion(s):
    s.disk(52,52,0,6,6,7,BOLD)
    s.line([(52,52,8),(52,52,23)],dashed=True)
    for z,r in ((26,15),(55,31),(87,50)):
        s.ring(52,52,z,r,r,5,4,BOLD if z==87 else EDGE)


def funnel_analysis(s):
    s.box(0,0,0,124,104,5,7)
    for i,count in enumerate((6,4,2)):
        y = 13+i*30
        s.box(10,y,5,104,19,3,4)
        for j in range(count):
            s.disk(23+j*15,y+9.5,8,4,4,5,BOLD if (i,j)==(2,1) else EDGE)


def audit_trail(s):
    s.box(0,0,0,145,33,5,6)
    s.line([(12,16,5),(133,16,5)],EDGE)
    for x in (17,39,63,88,124):
        s.disk(x,16,5,4,4,3,BOLD if x==88 else EDGE)
    s.line([(88,16,8),(88,16,34)],dashed=True)
    s.box(71,5,35,35,22,5,3,BOLD)
    s.line([(77,12,40),(99,12,40)])
    s.line([(77,18,40),(93,18,40)])


FIGURES = [
    (growth,"Growth","An ascending series of columns traces steady growth."),
    (analytics,"Analytics","Three rows of raised bars compare a set of measurements."),
    (forecast,"Forecasting","One observed trend splits into three projected outcomes."),
    (monitoring,"Monitoring","Three offset traces show a pulse across a bank of channels."),
    (heatmap,"Heat map","A concentrated peak rises from a grid of measurements."),
    (segments,"Segmentation","Three wedges separate into distinct cohorts."),
    (experiments,"A/B testing","Two groups of samples sit on separate test platforms."),
    (conversion,"Conversion","Three apertures narrow to a single output."),
    (funnel_analysis,"Cohort retention","Fewer samples remain on each successive shelf."),
    (audit_trail,"Activity history","An event lifts from its place on the timeline."),
]
