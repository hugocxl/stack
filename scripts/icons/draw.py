#!/usr/bin/env python3
"""Original rounded artwork. Authoring only: pip install -r scripts/icons/requirements.txt.

B = closed body, D = identifying detail; lines expanded with round caps/joins.
All delivered SVGs contain filled Bézier contours, with no runtime dependencies.
"""
import json
import math
import re
from pathlib import Path
import sys
import xml.etree.ElementTree as ET
import pathops as po
from fontTools.svgLib.path import parse_path
from fontTools.pens.svgPathPen import SVGPathPen

ROOT = Path(__file__).resolve().parents[2]
DRAWINGS = {}
STYLE_OVERRIDES = {}
# A second tone must describe a surface at a different depth, never an
# arbitrary half of a line. Linear drawings are opaque unless justified here.
DUOTONE_GLYPHS = {
    'layers': 'Receding lower plane behind the foreground sheet.',
}
SINGLE_TONE_SHAPES = {'chart-donut'}
CATEGORY = ''
BOOLEAN_REPAIRS=[]
def op(a,b,kind):
    """Reject numerically inconsistent Skia results before exporting artwork.

    Tangent round contours can produce catastrophic float-precision failures.
    Retry on the same 1e-4 grid used by the exported SVG, then on a 1e-3 grid.
    Area identities guard against silently dropping complete contours.
    """
    a,b=po.simplify(a),po.simplify(b)
    for precision in [None,4,3]:
        if precision is None: aa,bb=a,b
        else:
            def quantize(p):
                pen=SVGPathPen(None,ntos=lambda v:format(v,f'.{precision}f'))
                p.draw(pen)
                return path(pen.getCommands())
            aa,bb=quantize(a),quantize(b)
        try:
            result=po.op(aa,bb,kind)
        except po.PathOpsError:
            if precision == 3:
                raise
            continue
        if kind == po.PathOp.INTERSECTION:
            other=po.op(aa,bb,po.PathOp.UNION).area
            expected=aa.area+bb.area-other
        else:
            intersection=po.op(aa,bb,po.PathOp.INTERSECTION).area
            expected={po.PathOp.UNION:aa.area+bb.area-intersection,
                      po.PathOp.DIFFERENCE:aa.area-intersection,
                      po.PathOp.REVERSE_DIFFERENCE:bb.area-intersection,
                      po.PathOp.XOR:aa.area+bb.area-2*intersection}[kind]
        tolerance=.004+.00005*(aa.area+bb.area)
        if expected >= -tolerance and abs(result.area-expected)<=tolerance:
            if precision is not None: BOOLEAN_REPAIRS.append(precision)
            return result
    raise ValueError(f'Unstable boolean geometry: {kind}; {result.area} != {expected}')

def path(d):
    p = po.Path()
    if d: parse_path(d, p.getPen())
    return p

def union(*ps):
    r = po.Path()
    for p in ps:
        if p: r = op(r, p, po.PathOp.UNION)
    return r

# One weight, one roundness: measured from SF Symbols Regular on this grid.
# Every visible line, outline and detail uses STROKE; widths outside the
# visible range are clearance cutters and offset tools and stay as given.
STROKE = 1.1
RADIUS = 1.25
def weight(width):
    return STROKE if .75 <= width <= 1.55 else width

def stroke(d, width=STROKE):
    width = weight(width)
    p = path(d) if isinstance(d, str) else po.Path(d)
    # Stroke at authoring resolution so Skia's curve tolerance cannot
    # introduce visibly different widths at different orientations.
    resolution=32
    p=p.transform(resolution,0,0,resolution,0,0)
    p.stroke(width*resolution, po.LineCap.ROUND_CAP, po.LineJoin.ROUND_JOIN, 4)
    p.convertConicsToQuads(.02)
    p=p.transform(1/resolution,0,0,1/resolution,0,0)
    return po.simplify(p)

def rr(x=2,y=2,w=12,h=12,r=RADIUS):
    # A positive radius always means the family corner; 0 keeps a sharp cutter.
    r=min(RADIUS if r>0 else 0,w/2,h/2);k=r*.5522847498
    return path(f'M{x+r} {y}H{x+w-r}C{x+w-r+k} {y} {x+w} {y+r-k} {x+w} {y+r}V{y+h-r}C{x+w} {y+h-r+k} {x+w-r+k} {y+h} {x+w-r} {y+h}H{x+r}C{x+r-k} {y+h} {x} {y+h-r+k} {x} {y+h-r}V{y+r}C{x} {y+r-k} {x+r-k} {y} {x+r} {y}Z')

def soften(p,r=.28):
    # Round sharp convex corners in closed masses; preserve negative counters.
    inset=op(p,stroke(p,2*r),po.PathOp.DIFFERENCE)
    return union(inset,stroke(inset,2*r)) if inset else p

def mirror(p): return p.transform(-1,0,0,1,16,0)


def circle(x=8,y=8,r=6):
    return path(f'M{x-r} {y}a{r} {r} 0 1 0 {2*r} 0a{r} {r} 0 1 0 {-2*r} 0Z')

def line(*points, width=STROKE):
    return stroke('M'+'L'.join(f'{x} {y}' for x,y in points),width)

def lines(*ds): return union(*(stroke(d) for d in ds))
def dots(*points,r=.7): return union(*(circle(x,y,r) for x,y in points))
def poly(points): return soften(path('M'+'L'.join(f'{x} {y}' for x,y in points)+'Z'),.22)
def ring(x=8,y=8,r=6,width=STROKE):
    # Outer edge stays at r; the band is always the family weight.
    return stroke(circle(x,y,r-STROKE/2))
def transform(p,angle=0,scale=1,dx=0,dy=0):
    a=math.radians(angle); c=math.cos(a)*scale; s=math.sin(a)*scale
    return p.transform(c,s,-s,c,8-8*c+8*s+dx,8-8*s-8*c+dy)

def badge_body():
    """Shared, optically centered eight-point seal for every badge variant."""
    points = []
    for i in range(16):
        angle = -math.pi / 2 + i * math.pi / 8
        radius = 6.5 if i % 2 == 0 else 5.65
        points.append((8 + radius * math.cos(angle), 8 + radius * math.sin(angle)))
    return path('M' + 'L'.join(f'{x} {y}' for x, y in points) + 'Z')


def add(name,b,d=None,outline=True,tags=''):
    assert name not in DRAWINGS, name
    d = d or po.Path()
    if outline and name != 'settings': b=soften(b)
    extent=union(b,d,stroke(b,1.25) if outline else po.Path()).bounds
    x0,y0,x1,y1=extent
    if min(x0,y0)<.65 or max(x1,y1)>15.35:
        scale=min(1,14.7/(x1-x0),14.7/(y1-y0))
        dx=8-(x0+x1)/2;dy=8-(y0+y1)/2
        b=transform(b,scale=scale,dx=dx*scale,dy=dy*scale)
        d=transform(d,scale=scale,dx=dx*scale,dy=dy*scale)
    DRAWINGS[name] = (b,d,outline,CATEGORY,tags)

def shape(name,b,d=None,tags=''): add(name,b,d,True,tags)
def glyph(name,b,d,tags=''): add(name,b,d,False,tags)
def check(x=8,y=8,s=1): return line((x-2.6*s,y),(x-.6*s,y+2*s),(x+3*s,y-2.2*s))
def plus(x=8,y=8,s=1): return lines(f'M{x-2*s} {y}h{4*s}',f'M{x} {y-2*s}v{4*s}')
def cross(x=8,y=8,s=1): return lines(f'M{x-2*s} {y-2*s}l{4*s} {4*s}',f'M{x+2*s} {y-2*s}l{-4*s} {4*s}')
def arrow(angle=0, size=1, dx=0, dy=0, width=STROKE):
    shaft = line((8-5*size, 8), (8+5*size, 8), width=width)
    head = line((8+size, 8-4*size), (8+5*size, 8), (8+size, 8+4*size), width=width)
    return transform(union(shaft, head), angle, dx=dx, dy=dy)

CATEGORY='Navigation'
for name,angle in [('right',0),('down',90),('left',180),('up',270),('up-right',-45),('down-right',45),('down-left',135),('up-left',225)]:
    glyph('arrow-'+name,transform(line((3,8),(13,8)),angle),transform(line((9,4),(13,8),(9,12)),angle))
    # A diagonal chevron's corner is two coordinates of its bounding box.
    shift = 3 if angle % 90 else 0
    dx, dy = shift * math.cos(math.radians(angle)), shift * math.sin(math.radians(angle))
    glyph('chevron-'+name,transform(line((5,3),(10,8)),angle,dx=dx,dy=dy),
          transform(line((10,8),(5,13)),angle,dx=dx,dy=dy))
for name,angle in [('left',180),('right',0),('up',270),('down',90)]:
    shape('circle-arrow-'+name,circle(),arrow(angle, .62, width=1.25))
    glyph('chevrons-'+name,transform(line((2,4),(6,8),(2,12)),angle),transform(line((9,4),(13,8),(9,12)),angle))
glyph('chevrons-up-down',line((5,6),(8,3),(11,6)),line((5,10),(8,13),(11,10)))
glyph('chevrons-in',lines('M2 4l4 4-4 4'),lines('M14 4l-4 4 4 4'))
shape('home',path('M2 7L8 2 14 7V13Q14 14 13 14H3Q2 14 2 13Z'),stroke('M6 14V9H10V14'),'house dashboard start')
shape('compass',circle(),poly([(10.7,5.3),(9,9),(5.3,10.7),(7,7)]))
glyph('external-link',stroke('M9 2H14V7'),stroke('M14 2L7 9M6 3H3Q2 3 2 4V13Q2 14 3 14H12Q13 14 13 13V10'))
glyph('log-in',stroke('M9 2H13Q14 2 14 3V13Q14 14 13 14H9'),union(line((2,8),(10,8)),line((7,5),(10,8),(7,11))))
glyph('log-out',stroke('M7 2H3Q2 2 2 3V13Q2 14 3 14H7'),union(line((6,8),(14,8)),line((11,5),(14,8),(11,11))))
for name,reflect in [('undo',False),('redo',True)]:
    f=mirror if reflect else lambda p:p
    glyph(name,f(stroke('M3 6H9C12 6 14 7.5 14 10S12 13.5 10 13.5')),f(line((6,3),(3,6),(6,9))))
for name,reflect in [('refresh',False),('reset',True),('rotate-left',True),('rotate-right',False)]:
    f=mirror if reflect else lambda p:p
    glyph(name,f(stroke('M12.5 10.5A5.2 5.2 0 1 1 12.5 4.5')),f(line((9.2,4.5),(12.5,4.5),(12.5,1.2))))
glyph('swap-horizontal',lines('M2 4.5H14','M11 1.5l3 3-3 3'),lines('M14 11.5H2','M5 8.5l-3 3 3 3'))
glyph('swap-vertical',lines('M4.5 14V2','M1.5 5l3-3 3 3'),lines('M11.5 2V14','M8.5 11l3 3 3-3'))
glyph('shuffle',stroke('M1.65 4H3.5Q4.5 4 5.35 4.9L10.45 10.8Q11.4 12 12.6 12H14'
                       'M1.65 12H3.5Q4.5 12 5.35 11.1L10.45 5.2Q11.4 4 12.6 4H14'),
      lines('M11.7 1.7L14 4L11.7 6.3','M11.7 9.7L14 12L11.7 14.3'))
glyph('repeat',stroke('M3 10V5Q3 3 5 3H13M13 6V11Q13 13 11 13H3'),lines('M11 1l2 2-2 2','M5 11l-2 2 2 2'))

CATEGORY='Actions and status'
glyph('plus',line((8,3),(8,13)),line((3,8),(13,8)))
glyph('minus',line((3,8),(8,8)),line((8,8),(13,8)))
glyph('close',line((3,3),(13,13)),line((13,3),(3,13)))
glyph('check',line((2,8),(6,12)),line((6,12),(14,4)))
glyph('check-check',line((1,8),(4,11),(10,4)),line((7,10),(9,12),(15,5)))
for name,detail in [('check',check()),('x',cross()),('plus',plus()),('minus',line((5,8),(11,8))),('info',union(circle(8,5,.7),line((8,7.5),(8,11)))),('help',union(stroke('M6.2 6Q6.2 4.6 8 4.6Q9.8 4.6 9.8 6Q9.8 7 8 8V8.8',1.2),circle(8,11,.65))),('alert',union(line((8,4.5),(8,8.5)),circle(8,11,.7))),('ellipsis',dots((4.5,8),(8,8),(11.5,8)))]:
    shape('circle-'+name,circle(),detail)
for old,new in [('info','circle-info'),('info-fill','circle-info'),('exclamation-circle-fill','circle-alert'),('ellipsis-circle','circle-ellipsis'),('minus-circle','circle-minus'),('circle-check-fill','circle-check'),('circle-x-fill','circle-x')]:
    b,d,o,c,t = DRAWINGS[new]; add(old,b,d,o,t)
for name,detail in [('triangle-alert',union(line((8,6),(8,9)),circle(8,11.5,.65))),('triangle-alert-fill',union(line((8,6),(8,9)),circle(8,11.5,.65)))]:
    shape(name,path('M7.1 2.5Q8 1 8.9 2.5L14.3 12Q15.2 14 13 14H3Q.8 14 1.7 12Z'),detail)
shape('octagon-alert',poly([(5,1.5),(11,1.5),(14.5,5),(14.5,11),(11,14.5),(5,14.5),(1.5,11),(1.5,5)]),union(line((8,4.5),(8,8.5)),circle(8,11,.7)))
shape('ban',circle(),line((4,4),(12,12)))
shape('checkbox',rr(),check())
shape('checkbox-fill',rr(),check())
shape('square',rr())
shape('circle',circle())
glyph('dot',circle(8,8,4),circle(8,8,1.5))
glyph('ellipsis',dots((3,8),(8,8),(13,8),r=1.1),circle(8,8,1.1))
glyph('ellipsis-vertical',dots((8,3),(8,8),(8,13),r=1.1),circle(8,8,1.1))
shape('search',circle(6.7,6.7,4.7),line((10.3,10.3),(14,14)))
STYLE_OVERRIDES['search'] = {'solid': union(ring(6.7,6.7,5.325,1.9),line((10.1,10.1),(14,14),width=1.65))}
for name,detail in [('zoom-in',plus(6.7,6.7,.75)),('zoom-out',line((4.9,6.7),(8.5,6.7)))]: shape(name,circle(6.7,6.7,4.7),union(line((10.3,10.3),(14,14)),detail))
shape('filter',path('M2 2H14L9.5 7.5V13L6.5 14V7.5Z'),line((5,4.5),(11,4.5)),'funnel refine')
glyph('sort-ascending',lines('M2 4H7','M2 8H6','M2 12H5'),lines('M12 13V3','M9 6l3-3 3 3'))
glyph('sort-descending',lines('M2 4H7','M2 8H6','M2 12H5'),lines('M12 3V13','M9 10l3 3 3-3'))
glyph('sliders',lines('M2 4H14','M2 8H14','M2 12H14'),union(circle(5,4,1.6),circle(11,8,1.6),circle(6,12,1.6)))
shape('toggle-on',rr(1.5,4,13,8,4),circle(10.5,8,2.3))
shape('toggle-off',rr(1.5,4,13,8,4),circle(5.5,8,2.3))
shape('save',path('M3 2H11L14 5V13Q14 14 13 14H3Q2 14 2 13V3Q2 2 3 2Z'),union(stroke('M5 2V6H10V2'),stroke('M5 14V10H11V14')))
shape('trash',rr(4,4,8,10,1),lines('M2.5 4H13.5','M6 2H10','M6.5 7V11','M9.5 7V11'),'delete remove bin')
archive_lid = rr(1.6,2.2,12.8,3.1)
shape('archive', union(rr(2.6,4.4,10.8,9.4),archive_lid),
      lines('M2.6 5.3H13.4', 'M6.2 8.25H9.8'))
for name,angle in [('download',90),('upload',270)]:
    glyph(name,stroke('M2 10V13Q2 14 3 14H13Q14 14 14 13V10'),arrow(angle, .78, dy=-1.9))
shape('download-circle-fill',circle(),arrow(90, .62, width=STROKE))
link_loop = stroke('M7.1 11.15L5.8 12.45A2.65 2.65 0 0 1 2.05 8.7L4.8 5.95Q6.55 4.2 8.05 5.6')
glyph('link', union(link_loop,transform(link_loop,180)),line((5.75,10.25),(10.25,5.75)))
link_end = stroke('M4 7.7L2.8 8.9A3.05 3.05 0 0 0 7.1 13.2L8.3 12')
glyph('unlink', union(link_end, transform(link_end, 180)),
      lines('M3.4 3.4L5.2 5.2', 'M10.8 10.8L12.6 12.6'))
shape('copy',union(rr(1.5,1.5,9,10,1.7),rr(5,5,9.5,9.5,1.7)),stroke(rr(5,5,9.5,9.5,1.7),1.25))
shape('clipboard',rr(3,3,10,11,1.5),union(rr(5.5,1.5,5,3,1),lines('M5.5 7H10.5','M5.5 10H9')))
shape('clipboard-check',rr(3,3,10,11,1.5),union(rr(5.5,1.5,5,3,1),check(8,9,.7)))

CATEGORY='Files and folders'
FILE=path('M4 1.5H9L13.5 6V13Q13.5 14.5 12 14.5H4Q2.5 14.5 2.5 13V3Q2.5 1.5 4 1.5Z')
FOLD=stroke('M9 1.5V6H13.5',1.2)
FOLDER=path('M2 3H6L8 5H14Q15 5 15 6V12Q15 14 13 14H3Q1 14 1 12V4Q1 3 2 3Z')
def zipper(x, top, bottom):
    # Two staggered teeth lead into a wider slider with a rounded pull.
    return union(stroke(f'M{x} {top}V{bottom-1.5}M{x-1.35} {top+.35}H{x}'
                        f'M{x} {top+1.8}h1.35', 1.1),
                 stroke(rr(x-1.1, bottom-2.05, 2.2, 2.05, .8), 1.1))

for name,detail in [('file',FOLD),('file-text',union(FOLD,lines('M5 8H11','M5 10.5H10'))),('file-plus',union(FOLD,plus(8,10,.7))),('file-minus',union(FOLD,line((5.5,10),(10.5,10)))),('file-check',union(FOLD,check(8,10,.65))),('file-x',union(FOLD,cross(8,10,.7))),('file-code',union(FOLD,stroke('M6.8 8.35L5.35 10L6.8 11.65M9.2 8.35L10.65 10L9.2 11.65',1.15))),('file-image',union(FOLD,circle(6,8,.7),line((4.5,12),(7,9.5),(9,11),(11,9)))),('file-table',union(FOLD,stroke('M5 8H11V12.65H5ZM5 10.3H11M8 8V12.65',1.05))),('file-symlink',union(FOLD,stroke('M5 12V10H10.5M8.5 8l2 2-2 2',1.1))),('file-lock',union(FOLD,rr(5.2,10.25,4.5,2.5,.6),stroke('M6.15 10.3V9.1A1.3 1.3 0 0 1 8.75 9.1V10.3',1.1))),('file-audio',union(FOLD, path('M6.95 11.1V7.4L9.7 8.05V9.35L8.1 8.9V11.45C8.1 13.1 4.65 13.75 4.65 12.25Q4.65 11 6.95 11.1Z'))),('file-video',union(FOLD,poly([(6,8),(10,10),(6,12)]))),('file-search',union(FOLD,ring(6.9,9.25,2.15,1.05),line((8.15,10.6),(9.75,12.1),width=1.15))),('file-heart',union(FOLD,path('M8 12.5L5.3 10C3.8 8.5 6.2 7.2 8 9C9.8 7.2 12.2 8.5 10.7 10Z'))),('file-zip',union(FOLD,zipper(7.2,7.5,12.6)))]: shape(name,FILE,detail)
for name,detail in [('folder',line((2,6),(14,6))),('folder-plus',plus(8,10,.8)),('folder-minus',line((5.5,10),(10.5,10))),('folder-check',check(8,10,.7)),('folder-x',cross(8,10,.7)),('folder-heart',path('M8 11.9L5 9.4C3.5 7.9 6 6.4 8 8.4C10 6.4 12.5 7.9 11 9.4Z')),('folder-lock',union(rr(6,9,4,3,1),stroke('M7 9V8A1 1 0 0 1 9 8V9',1))),('folder-search',union(ring(7.2,8.8,1.9,1.1),line((8.6,10.2),(10.2,11.8),width=1.1))),('folder-code',stroke('M6.25 7.6L4.45 9.4L6.25 11.2M9.75 7.6L11.55 9.4L9.75 11.2',1.25)),('folder-zip',zipper(8,6.9,12))]: shape(name,FOLDER,detail)
folder_back = path('M1.45 4Q1.45 3 2.55 3H5.7L7.7 4.8H11.9Q13 4.8 13 6V12.9H1.45Z')
folder_flap = soften(path('M3.45 7.15H14.6L12.8 13.25H1.45Z'))
shape('folder-open', union(folder_back, folder_flap), stroke(folder_flap, 1.25))
shape('folders',union(transform(FOLDER,0,.8,-1,-2),transform(FOLDER,0,.8,1,1.5)),stroke(transform(FOLDER,0,.8,1,1.5),1.25))
shape('pdf', rr(1.4, 2.3, 13.2, 11.4, 1.8),
      stroke('M3.5 10.65V5.35H4.45C6.35 5.35 6.35 8.3 4.45 8.3H3.5'
             'M7.05 5.35V10.65H7.65C10.1 10.65 10.1 5.35 7.65 5.35Z'
             'M10.9 10.65V5.35H12.55M10.9 7.95H12.25', 1.05))
for name,detail in [('spreadsheet',stroke('M2 6H14M6 2V14M10 6V14M2 10H14',1.2)),('slides',union(lines('M4 5H12','M4 8H7','M4 10.5H7'),rr(9,8,3,4,.5))),('word',stroke('M4.35 5.3L5.9 10.8L8 6.4L10.1 10.8L11.65 5.3',1.2)),('zip',union(stroke('M8 2V8.6M6.5 4H8M8 5.9H9.5M6.5 7.8H8', 1.15), stroke(rr(6.7, 8.7, 2.6, 3.4, 1), 1.1)))]: shape(name,rr(),detail)

reader = rr(1.55,1.45,12.9,13.1)
book_spread = path('M3.8 4.35Q6 3.5 8 4.8Q10 3.5 12.2 4.35V9.35Q10 8.75 8 10Q6 8.75 3.8 9.35Z')
shape('epub',reader,union(stroke(book_spread),stroke('M8 4.8V10M1.55 12.05H14.45')))
CATEGORY='Communication'
BUBBLE=path('M4 2H12Q14 2 14 4V10Q14 12 12 12H7L3 14V12Q2 12 2 10V4Q2 2 4 2Z')
for name,detail in [('message',line((5.05,7.2),(10.95,7.2))),('message-text',lines('M5 6H11','M5 9H9')),('message-plus',plus(8,7,.8)),('message-check',check(8,7,.7)),('message-heart',path('M8 10L5 7.5C3.5 6 6 4 8 6C10 4 12.5 6 11 7.5Z')),('message-dots',dots((5,7),(8,7),(11,7))),('comment-text',lines('M5 6H11','M5 9H9')),('conversation',lines('M5 6H11','M5 9H9')),('conversation-add',plus(8,7,.8))]: shape(name,BUBBLE,detail)
for name in ['mail','envelope']: shape(name,rr(1.5,3,13,10,2),line((2,4),(8,8.5),(14,4)))
open_envelope = path('M1.65 6.45L8 1.65L14.35 6.45V12.9Q14.35 14 13.15 14H2.85Q1.65 14 1.65 12.9Z')
open_folds = stroke('M1.65 6.45L8 10.5L14.35 6.45M1.65 14L6.25 9.5M14.35 14L9.75 9.5')
shape('mail-open',open_envelope,op(open_folds,open_envelope,po.PathOp.INTERSECTION))
shape('send',path('M2 2L14 7.2Q15 8 14 8.8L2 14 4 8Z'),line((4,8),(11,8)))
shape('inbox',rr(1.5,2,13,12,2),stroke('M1.5 9H5L6 11H10L11 9H14.5'))
BELL=path('M8 2A4 4 0 0 0 4 6V9L2 12H14L12 9V6A4 4 0 0 0 8 2Z')
shape('bell',BELL,union(line((6,14),(10,14)),line((8,1),(8,2))))
shape('bell-unread',op(BELL,circle(12.5,3,2.9),po.PathOp.DIFFERENCE),union(line((6,14),(10,14)),circle(12.5,3,1.65)))
shape('bell-off',BELL,union(line((6,14),(10,14)),line((2,2),(14,14))))
horn = path('M2.1 5.95H5.65L13.55 2.25V11.6L5.65 8.85H2.1Z')
grip = path('M3.65 8.65H6.55L7.65 13.5Q6.1 14.35 5 13.9Z')
shape('megaphone',union(horn,grip),line((3.95,8.85),(5.65,8.85)))
shape('phone-call',path('M3 1.5L6 4.5 4.5 7Q6 10 9 11.5L11.5 10 14.5 13Q13 16 10 14.5C6 13 3 10 1.5 6Q0 3 3 1.5Z'),stroke('M10 2Q14 2 14 6M10 5Q11 5 11 6',1.1))
shape('video-call',rr(1.5,4,9,8,2),path('M11 6L14.5 4V12L11 10Z'))
glyph('at-sign',stroke('M12.3 12.8C5.5 17.8-.2 11 2.2 5C4.5-.7 14.5 1 14.5 7.3C14.5 11 10 11.5 10 8.5V5'),stroke('M10 6C7 3 4 6 5 8.8C6 11.5 10 10.5 10 7',1.2))
glyph('rss',stroke('M2 2A12 12 0 0 1 14 14M2 7A7 7 0 0 1 9 14'),circle(3,13,1.4))

CATEGORY='People and accessibility'
head = circle(8,4.05,2.35)
shoulders = path('M2.65 14.05V12.75Q2.65 9 8 9Q13.35 9 13.35 12.75V14.05Z')
person = union(head,shoulders)
shape('user',person)
avatar_frame = circle()
shoulder_arc = op(stroke('M2.5 13.2Q8 5.6 13.5 13.2'),avatar_frame,po.PathOp.INTERSECTION)
shape('circle-user',avatar_frame,union(circle(8,5.9,1.8),shoulder_arc))
shape('users',union(circle(5,4.5,2.2),circle(11.5,5.5,1.8),path('M1 14V12Q1 8.5 5 8.5Q9 8.5 9 12V14ZM9 14V12Q9 10 11.5 10Q15 10 15 13V14Z')),line((9,12),(9,14)))
# Scale only the closed head and shoulder surfaces, then outline at native weight.
badge_person = transform(person,scale=.81,dx=-2.15,dy=.1)
for name, symbol in [('user-plus',plus(12.35,7.35,.77)),
                     ('user-check',check(12.3,7.35,.64)),
                     ('user-x',cross(12.35,7.35,.68))]:
    shape(name,badge_person,symbol)
shape('contact',rr(2,1.5,12,13,2),union(circle(8,6,2),stroke('M5 11Q8 8 11 11'),lines('M1 5H3','M1 11H3')))
glyph('accessibility',circle(8,2.5,1.5),lines('M2 6L8 7 14 6','M8 7V10','M8 10L4 14','M8 10L12 14'))
wheel = stroke('M4.8 7.8A3.65 3.65 0 1 0 9.65 11.6')
glyph('wheelchair',wheel,union(circle(7.2,2.25,1.35),
      stroke('M7.1 5.05V8.7H10.8L12.9 13.1H14.55')))
for name,detail in [('smile',stroke('M5 9Q8 13 11 9')),('frown',stroke('M5 11Q8 7 11 11')),('meh',line((5,10),(11,10)))]: shape(name,circle(),union(dots((5.5,6),(10.5,6)),detail))
hand_body = path('M4.45 9V4.15C4.45 2.6 6.9 2.6 6.9 4.15V2.65C6.9 1 9.35 1 9.35 2.65V3.55'
                 'C9.35 1.95 11.8 1.95 11.8 3.55V5.1C11.8 3.55 14.2 3.55 14.2 5.1V9.25'
                 'C14.2 12.6 12.15 14.45 9.45 14.45Q6.8 14.45 4.95 12.2L1.8 8.4'
                 'C.7 6.95 2.3 5.65 3.4 6.9Z')
shape('hand',hand_body,lines('M6.9 4.15V7.05','M9.35 3.55V6.85','M11.8 5.1V7.55'))
shape('thumbs-up',path('M5 7L8 2Q10 1 10 4L9.5 6H13Q15 6 14 9L12.5 14H5Z'),rr(1.5,7,3.5,7,1))
shape('thumbs-down',transform(DRAWINGS['thumbs-up'][0],180),transform(DRAWINGS['thumbs-up'][1],180))

CATEGORY='Security'
SHIELD=path('M8 1.5Q11 3 14 3V7Q14 12 8 14.5Q2 12 2 7V3Q5 3 8 1.5Z')
for name,detail in [('shield',po.Path()),('shield-check',check()),('shield-x',cross()),('shield-alert',union(line((8,5),(8,8)),circle(8,10.5,.7))),('shield-keyhole',union(circle(8,6.5,1.5),line((8,7),(8,10.5))))]: shape(name,SHIELD,detail)
for name,shackle in [('lock','M4.5 7V5A3.5 3.5 0 0 1 11.5 5V7'),('lock-open','M4.5 7V5A3.5 3.5 0 0 1 11.5 5')]: shape(name,rr(2.5,7,11,7,1.8),union(stroke(shackle),circle(8,10,1),line((8,10),(8,12))))
shape('key',circle(5,5,3.5),union(circle(5,5,1),stroke('M7.5 7.5L14 14M11 11L13 9M13 13L15 11')))
glyph('fingerprint',stroke('M1.8 7.5A6.2 6.2 0 0 1 14.2 7.5Q14.2 11 13 13M3.8 10V7.5A4.2 4.2 0 0 1 12.2 7.5Q12.2 12 10.8 14',1.1),stroke('M5.5 13.5Q7.4 11 6.7 8A1.35 1.35 0 0 1 9.4 8Q10 11 8.5 14M1.8 10Q2.2 13 3 14',1.1))
shape('eye',path('M1.35 8Q8-2.5 14.65 8Q8 18.5 1.35 8Z'),ring(8,8,3))
DRAWINGS['eye-off'] = DRAWINGS['eye']
shape('scan',rr(4,4,8,8,2),lines('M1 5V1H5','M11 1H15V5','M1 11V15H5','M11 15H15V11','M6 8H10'))
shape('qr-code',union(rr(1.5,1.5,5,5,1),rr(9.5,1.5,5,5,1),rr(1.5,9.5,5,5,1)),union(rr(3,3,2,2,.3),rr(11,3,2,2,.3),rr(3,11,2,2,.3),lines('M10 10H14V14H12','M10 13V14')))
shape('badge-check',badge_body(),check(s=.82))

CATEGORY='Time and planning'
for name,detail in [('clock',line((8,4),(8,8),(11,10))),('alarm-clock',union(line((8,4),(8,8),(11,8)),lines('M2.25 3.45L4.15 1.55','M11.85 1.55L13.75 3.45','M2.95 14.2L4.35 12.5','M11.65 12.5L13.05 14.2')))]: shape(name,circle(8,8,5.8),detail)
history_return = stroke('M2.05 5.3A6.45 6.45 0 1 1 1.65 9.05M1.65 2.4V5.7H3.75')
shape('history',circle(8,8,3.8),union(history_return,stroke('M8 6.15V8.2L9.55 9.05')))
shape('timer',circle(8,9,5),union(line((8,9),(10,6.5)),lines('M6 1H10','M8 1V4','M12 4l1-1')))
shape('hourglass',path('M3 2H13Q13 6 9.5 8Q13 10 13 14H3Q3 10 6.5 8Q3 6 3 2Z'),lines('M3 2H13','M3 14H13','M6 5H10','M6 12l2-2 2 2'))
CAL=rr(2,3,12,11,2); CALTOP=lines('M5 1.5V4.5','M11 1.5V4.5','M2 6H14')
for name,detail in [('calendar',dots((5,9),(8,9),(11,9),(5,12),(8,12))),('calendar-days',dots((5,9),(8,9),(11,9),(5,12),(8,12),(11,12))),('calendar-check',check(8,10,.7)),('calendar-plus',plus(8,10,.8)),('calendar-x',cross(8,10,.7)),('calendar-clock',union(stroke(circle(8,10.05,2.5)),stroke('M8 8.95V10.1L9.05 10.65'))),('calendar-range',union(line((5,10),(11,10),width=1.1),dots((5,10),(11,10),r=1)))]: shape(name,CAL,union(CALTOP,detail))
shape('list-todo',rr(1.5,2,13,12,2),lines('M3.5 5l1 1 2-2','M9 5H12','M3.5 10l1 1 2-2','M9 10H12'))
shape('notebook',rr(3,1.5,10.5,13,1.5),lines('M1.5 4H4.5','M1.5 8H4.5','M1.5 12H4.5','M6.5 5H11','M6.5 8H10'))
shape('sticky-note',path('M2 2H14V10L10 14H2Z'),stroke('M10 14V10H14M5 5H11M5 8H9',1.2))
shape('flag',path('M3 2Q6 0 9 2T14 2V9Q11 11 8 9T3 9Z'),line((3,2),(3,14)))
shape('bookmark',path('M4 2H12V14L8 11 4 14Z'))
shape('bookmark-plus',path('M4 2H12V14L8 11 4 14Z'),plus(8,6,.7))
shape('pin',path('M5 2H11L10 6 13 9H3L6 6Z'),line((8,9),(8,14)))
shape('target',circle(),union(ring(8,8,3.5,1.25),circle(8,8,1.2)))
shape('trophy',path('M4 2H12V6Q12 10 8 11Q4 10 4 6Z'),stroke('M4 3H1V5Q1 8 4 8M12 3H15V5Q15 8 12 8M8 11V14M5 14H11'))

CATEGORY='Media'
for name,detail in [('play',poly([(6,4.5),(12,8),(6,11.5)])),('pause',lines('M6.3 5.3V10.7', 'M9.7 5.3V10.7')),('stop',rr(5,5,6,6,1))]: shape(name,circle(),detail)
for name,source in [('pause-circle-fill','pause'),('play-circle','play'),('stop-circle','stop')]:
    b,d,o,c,t=DRAWINGS[source];add(name,b,d,o,t)
glyph('skip-forward',poly([(2,3),(10,8),(2,13)]),line((13,3),(13,13)))
glyph('skip-back',poly([(14,3),(6,8),(14,13)]),line((3,3),(3,13)))
shape('volume',path('M2 6H5L9 2V14L5 10H2Z'),stroke('M12 4Q16 8 12 12M11 6Q13 8 11 10'))
shape('volume-off',path('M2 6H5L9 2V14L5 10H2Z'),cross(12.5,8,.6))
shape('microphone',rr(5,1.5,6,9,3),stroke('M2.5 7V8A5.5 5.5 0 0 0 13.5 8V7M8 13.5V15M5.5 15H10.5',1.2))
shape('microphone-off',rr(5,1.5,6,9,3),stroke('M2.5 7V8A5.5 5.5 0 0 0 13.5 8V7M8 13.5V15M2 2L14 14',1.2))
headband = stroke('M3.05 7.9V6.8A4.95 4.95 0 0 1 12.95 6.8V7.9')
earcups = union(rr(1.55,7.9,3.15,5.15),rr(11.3,7.9,3.15,5.15))
glyph('headphones',headband,earcups)
def notehead(x,y):
    return circle(0,0,1).transform(1.85,-.52,.2,1.3,x,y)

beam = stroke('M5.65 11.45V4.25L12.65 2.6V9.8M5.65 6.7L12.65 5.05')
heads = union(notehead(4.35,11.95),notehead(11.35,10.3))
glyph('music',beam,heads)
shape('image',rr(1.5,2,13,12,2),union(circle(5,5.5,1.3),line((2,12),(6.5,8),(9,10),(11,7.5),(14,11))))
shape('camera',path('M2 4H5L6 2H10L11 4H14V13H2Z'),union(ring(8,8.5,3,1.35),circle(12,6,.65)))
DRAWINGS['camera-off'] = DRAWINGS['camera']
shape('video',rr(1.55,2,12.9,12),union(poly([(6.65,5.45),(10.05,8),(6.65,10.55)]),
      lines('M4.45 2V14','M11.55 2V14')))
shape('film',rr(1.5,2,13,12,1),lines('M5 2V14','M11 2V14','M1.5 6H5','M1.5 10H5','M11 6H14.5','M11 10H14.5'))
shape('radio',rr(1.5,5,13,9,2),union(line((3,5),(12,1.5)),ring(5.5,9.5,2.2,1.2),lines('M10 8H12','M10 11H12')))
shape('tv',rr(1.5,4,13,9,2),lines('M5 1l3 3 3-3','M5 15H11'))
glyph('cast',stroke('M2 4V3Q2 2 3 2H13Q14 2 14 3V11Q14 12 13 12H11',1.35),union(stroke('M2 7A7 7 0 0 1 9 14M2 10A4 4 0 0 1 6 14',1.2),circle(2,14,.8)))
shape('airplay',rr(1.5,2,13,10,2),poly([(8,8),(13,14),(3,14)]))
glyph('waveform',lines('M2 6V10','M5 3V13','M8 1V15','M11 4V12','M14 6V10'),line((8,5),(8,11)))
disc_glint = stroke('M4.65 6.85Q5.3 5.25 6.85 4.65')
shape('disc',circle(),union(ring(8,8,1.55,1.05),disc_glint,transform(disc_glint,180)))
glyph('podcast',stroke('M3.4 11A6 6 0 1 1 12.6 11M5.2 8.9A3.5 3.5 0 1 1 10.8 8.9',1.1),union(circle(8,6,1.25),rr(6.7,8.5,2.6,6,1.3)))

CATEGORY='Layout'
WINDOW=rr(1.5,2,13,12,2)
for name,detail in [('app-window',union(line((1.5,5.5),(14.5,5.5)),dots((4,3.8),(6,3.8),r=.4))),('browser',lines('M1.5 6.65H14.5','M7.4 4.3H11.4')),('panel-left',stroke('M6 2V14')),('panel-right',stroke('M10 2V14')),('panel-top',stroke('M2 6H14')),('panel-bottom',stroke('M2 10H14')),('columns',stroke('M8 2V14')),('rows',stroke('M2 8H14')),('layout-dashboard',stroke('M8 2V14M2 9H8M8 6H14')),('layout-grid',stroke('M8 2V14M2 8H14')),('layout-sidebar',stroke('M6 2V14M2 6H6M2 9H6')),('table',stroke('M2 6H14M2 10H14M6 2V14M10 2V14',1.1))]: shape(name,WINDOW,detail)
glyph('maximize',lines('M2 6V2H6','M10 14H14V10'),lines('M10 2H14V6','M2 10V14H6'))
glyph('minimize',lines('M2 6H6V2','M10 14V10H14'),lines('M10 2V6H14','M2 10H6V14'))
glyph('fullscreen',lines('M1.5 5V1.5H5','M11 14.5H14.5V11'),lines('M11 1.5H14.5V5','M1.5 11V14.5H5'))
shape('picture-in-picture',WINDOW,rr(7.95,7.7,4.25,3.8))
top_sheet = path('M1.55 5.5L8 1.95L14.45 5.5L8 9.05Z')
lower_sheet = path('M1.55 9.35L8 12.9L14.45 9.35V11.15L8 14.7L1.55 11.15Z')
glyph('layers',lower_sheet,top_sheet)
STYLE_OVERRIDES['layers'] = {'stroke':union(stroke(top_sheet),stroke('M1.55 10.3L8 13.85L14.45 10.3'))}
shape('multiplexer',union(rr(1.5,1.5,9.5,9.5,2),rr(5,5,9.5,9.5,2)),union(stroke(rr(5,5,9.5,9.5,2),1.25),lines('M10 5V14.5','M5 10H14.5')))

CATEGORY='Editing and design'
shape('pencil',path('M2 10L10 2Q11 1 12 2L14 4Q15 5 14 6L6 14 1.5 14.5Z'),stroke('M9 3L13 7M2 10L6 14'))
shape('eraser',path('M2 8L8 2Q9 1 10 2L14 6Q15 7 14 8L8 14H5L2 11Q1 10 2 8Z'),stroke('M5 5L11 11M8 14H14'))
brush = path('M1.7 14.3Q2.8 13.1 2.6 11.65Q2.35 9.05 5.2 8.65L10.75 2.25'
             'C12.95 .1 15.9 3.25 13.75 5.35L7.3 10.95Q7.05 14.4 1.7 14.3Z')
ferrule = line((5.15,8.65),(7.35,10.85))
shape('paintbrush',brush,ferrule)
shape('palette',path('M8 1.5C0 1.5-1 13 6 14.5Q10 15 9 12Q8 10 11 10C17 11 16 1.5 8 1.5Z'),dots((5,5),(9,4),(12,6),(3.5,8)))
SWATCH=rr(2,2,4.5,12,1)
SWATCH_DIAGONAL=SWATCH.transform(.7071,.7071,-.7071,.7071,9.553,-.257)
swatch_front = rr(2,9.55,12,4.4)
swatch_rear = op(stroke(SWATCH),SWATCH_DIAGONAL,po.PathOp.DIFFERENCE)
swatch_edges = op(union(swatch_rear,stroke(SWATCH_DIAGONAL)),swatch_front,po.PathOp.DIFFERENCE)
shape('swatch',union(SWATCH,SWATCH_DIAGONAL,swatch_front),
      union(swatch_edges,stroke(swatch_front),circle(4.35,11.75,.65)))
STYLE_OVERRIDES['swatch'] = {'stroke':union(swatch_edges,stroke(swatch_front),stroke(circle(4.35,11.75,1.05)))}
glyph('crop',stroke('M4 1V12H15'),stroke('M1 4H12V15'))
shape('ruler',transform(rr(1.5,5,13,6,1),-45),transform(lines('M4 5V7','M7 5V8','M10 5V7'),-45))
glyph('scissors',union(ring(4,4,2.5,1.35),ring(4,12,2.5,1.35)),lines('M6 5.5L14 13','M6 10.5L14 3'))
nib = path('M2.1 13.95L4.2 5.3L9.15 2.05L13.95 6.85L10.75 11.9Z')
shape('pen-tool',nib,union(circle(7.85,8.15,1.15),line((2.1,13.95),(7.35,8.65))))
dropper = path('M1.75 14.1L2.85 10.05L9.75 3.15C12.55 .35 15.7 3.5 12.9 6.3L6 13.2Z')
collar = line((7.25,4.55),(11.5,8.8))
shape('pipette', dropper, collar)
STYLE_OVERRIDES['pipette'] = {'solid': op(union(dropper, stroke(dropper)), collar, po.PathOp.DIFFERENCE)}
bold_body = path('M3.1 1.65H8.65C13.15 1.65 14 6.1 11.2 7.65'
                 'C14.85 9.1 13.95 14.35 9.25 14.35H3.1Z')
bold_counters = path('M5.9 4.1V6.65H8.25C10.75 6.65 10.75 4.1 8.25 4.1Z'
                     'M5.9 9.05V11.9H8.8C11.45 11.9 11.45 9.05 8.8 9.05Z')
glyph('bold',op(bold_body,bold_counters,po.PathOp.DIFFERENCE),po.Path())
glyph('italic',lines('M7 2H13','M3 14H9'),line((10,2),(6,14)))
glyph('underline',stroke('M3 2V7A5 5 0 0 0 13 7V2'),line((2,14),(14,14)))
glyph('strikethrough',stroke('M11.8 3.45C9.4 1.3 4.3 1.75 4.3 4.7C4.3 8.15 11.9 7.35 11.9 11.1C11.9 14.2 6.6 14.9 3.65 12.4'),line((1.7,8),(14.3,8)))
glyph('font',line((2,13),(8,2),(14,13)),line((4.55,8.95),(11.45,8.95)))
for name,align in [('align-left','left'),('align-center','center'),('align-right','right'),('align-justify','justify')]:
    ds=[]
    for i,w in enumerate([12,8,12,8]):
        if align=='justify':w=12
        x=2 if align in ['left','justify'] else 14-w if align=='right' else (16-w)/2
        ds.append(line((x,3+i*3),(x+w,3+i*3)))
    glyph(name,union(ds[0],ds[2]),union(ds[1],ds[3]))
glyph('list',dots((2,4),(2,8),(2,12)),lines('M5 4H14','M5 8H14','M5 12H14'))
glyph('list-ordered',stroke('M1.65 3.95L3 2.7V6.5M1.55 9.85C1.8 8.2 4.65 8.5 3.85 10.25Q3.4 11.25 1.6 13.2H4.05',1.15),
      lines('M6.75 4.65H14','M6.75 11.1H14'))
glyph('indent',lines('M2 2H14','M2 14H14','M9 6H14','M9 10H14'),line((2,5),(5,8),(2,11)))
glyph('outdent',lines('M2 2H14','M2 14H14','M9 6H14','M9 10H14'),line((5,5),(2,8),(5,11)))
glyph('wrap',lines('M2 3H14','M2 13H6'),stroke('M2 7H11A3 3 0 0 1 11 13H9M11 10L8 13 11 15'))
quote_bowl = circle(3.95,6.25,2.75)
quote_tail = stroke('M6.15 6.25C6.15 9.3 4.65 11.8 2.55 12.85')
comma = union(quote_bowl,quote_tail)
comma_outline = union(ring(3.95,6.25,2.75),quote_tail)
glyph('quote',comma,transform(comma,dx=7.7))
STYLE_OVERRIDES['quote'] = {'stroke':union(comma_outline,transform(comma_outline,dx=7.7))}
glyph('hash',lines('M6 2L4 14','M12 2L10 14'),lines('M2 6H14','M1 10H13'))
shape('text-cursor',rr(1.5,4,8,8,1),lines('M10 2H14','M12 2V14','M10 14H14'))
shape('text-select',rr(2,2,12,12,1),lines('M5 5H11','M8 5V11','M6 11H10'))

CATEGORY='Technology and development'
shape('terminal',WINDOW,lines('M4 6l3 3-3 3','M9 12H12'))
shape('terminal-stack',union(transform(WINDOW,0,.8,-1,-1.5),transform(WINDOW,0,.8,1,1.5)),union(stroke(transform(WINDOW,0,.8,1,1.5),1.2),lines('M6 8l2 2-2 2','M10 12H12')))
shape('code-block',WINDOW,stroke('M5.65 6.3L4.05 8L5.65 9.7M10.35 6.3L11.95 8L10.35 9.7M8.85 5.4L7.15 10.6',1.2))
glyph('code',lines('M5 4L1 8 5 12','M11 4L15 8 11 12'),line((9,2),(7,14)))
glyph('braces',stroke('M6 2H5Q4 2 4 4V6Q4 8 2 8Q4 8 4 10V12Q4 14 6 14'),stroke('M10 2H11Q12 2 12 4V6Q12 8 14 8Q12 8 12 10V12Q12 14 10 14'))
glyph('command', stroke('M5.65 5.65H3.65A2 2 0 1 1 5.65 3.65V12.35'
                        'A2 2 0 1 1 3.65 10.35H12.35A2 2 0 1 1 10.35 12.35V3.65'
                        'A2 2 0 1 1 12.35 5.65Z',1.3), po.Path())
shape('cpu',rr(4,4,8,8,1.5),union(rr(6.5,6.5,3,3,.5),lines('M5 1V4M8 1V4M11 1V4M5 12V15M8 12V15M11 12V15M1 5H4M1 8H4M1 11H4M12 5H15M12 8H15M12 11H15',)))
shape('database',path('M2 4C2 0 14 0 14 4V12C14 16 2 16 2 12Z'),stroke('M2 4C2 8 14 8 14 4M2 8C2 12 14 12 14 8'))
shape('server-rack',rr(2,1.5,12,13,2),union(lines('M2 6H14','M2 10H14'),dots((5,4),(5,8),(5,12)),lines('M9 4H11','M9 8H11','M9 12H11')))
shape('cloud',path('M4.2 13C-.2 13 .2 6.5 4.2 6.5C4.3 .7 12.7 .5 13 6.5C17 7 16.5 13 12.3 13Z'))
shape('cloud-upload',DRAWINGS['cloud'][0],arrow(270, .45, dy=.8, width=1.2))
shape('cloud-download',DRAWINGS['cloud'][0],arrow(90, .45, dy=.8, width=1.2))
shape('monitor',rr(1.5,2,13,9,1.5),lines('M8 11V14','M5 14H11','M2 8H14'))
laptop_screen = rr(3.15,2.35,9.7,8.55)
laptop_base = path('M3.15 10.9H12.85L14.45 13.45H1.55Z')
shape('laptop',union(laptop_screen,laptop_base),line((3.15,10.9),(12.85,10.9)))
STYLE_OVERRIDES['laptop'] = {'solid':union(stroke(laptop_screen),laptop_base,stroke(laptop_base))}
shape('phone',rr(4,1,8,14,2),union(line((6.5,3),(9.5,3)),line((7,13),(9,13))))
shape('phone-android',rr(4,1,8,14,1.5),union(circle(8,3,.5),dots((6,13),(8,13),(10,13),r=.4)))
shape('simulator',rr(4,1,8,14,2),union(poly([(6.5,5.5),(10,8),(6.5,10.5)]),line((7,13),(9,13))))
shape('tablet',rr(2.5,1,11,14,2),circle(8,12.5,.65))
shape('keyboard',rr(1,4,14,9,1.5),union(dots(*[(x,y) for x in [3.5,6.5,9.5,12.5] for y in [6.5,9]],r=.55),line((5,11),(11,11))))
shape('mouse',rr(4,1,8,14,4),line((8,3.5),(8,6)))
shape('watch',rr(4,4,8,8,2),union(lines('M5 4V1H11V4','M5 12V15H11V12'),line((8,6),(8,8),(10,9))))
printer_chassis = rr(1.55,5.2,12.9,6.4)
output_sheet = rr(4.25,9.55,7.5,4.8)
printer = union(printer_chassis,output_sheet,rr(4.15,1.65,7.7,4.8))
printer_seams = union(line((3.4,5.2),(12.6,5.2)), stroke(output_sheet),stroke(circle(11.85,7.35,1.05)))
shape('printer',printer,printer_seams)
usb_body = rr(4.15,6.45,7.7,7.8)
usb_plug = rr(4.95,1.85,6.1,5.4)
contacts = lines('M6.7 3.9V4.55', 'M9.3 3.9V4.55')
shape('usb',union(usb_body,usb_plug),union(line((4.95,6.45),(11.05,6.45)),contacts))
shape('hard-drive',rr(1.5,3,13,10,2),union(line((2,9),(14,9)),dots((11,11),(13,11),r=.5)))
shape('battery',rr(1,4,12,8,1.5),union(rr(3,6,6,4,.5),line((15,6.5),(15,9.5))))
shape('battery-charging',rr(1,4,12,8,1.5),union(poly([(8,4.8),(4,8.5),(7,8.5),(5.5,11.5),(10,7.5),(7,7.5)]),line((15,6.5),(15,9.5))))
glyph('wifi',stroke('M1 5Q8-1 15 5M3.5 8Q8 4 12.5 8M6 11Q8 9 10 11'),circle(8,13,1))
glyph('bluetooth',stroke('M7 1.5V14.5L12 10.5 3 3.5'),stroke('M7 1.5L12 5.5 3 12.5'))
shape('network',union(rr(5.5,1,5,4,1),rr(1,11,5,4,1),rr(10,11,5,4,1)),stroke('M8 5V8H3.5V11M8 8H12.5V11'))
shape('git-branch',union(circle(4,3,1.5),circle(4,13,1.5),circle(12,3,1.5)),stroke('M4 4.5V11.5M12 4.5V5Q12 9 4 9',1.25))
shape('git-merge',union(circle(3.5,3,1.5),circle(3.5,13,1.5),circle(12.5,3,1.5)),stroke('M3.5 4.5V11.5M12.5 4.5V5Q12.5 8.5 6.5 8.5M8.5 6.5L6.5 8.5 8.5 10.5',1.2))
shape('git-pull-request',union(circle(4,3,1.5),circle(4,13,1.5),circle(12,13,1.5)),stroke('M4 4.5V11.5M12 11.5V6Q12 3 9 3M10 1L8 3 10 5',1.25))
shape('git-commit',circle(8,8,3),lines('M1 8H5','M11 8H15'))
shape('bug',rr(4,4,8,10,4),lines('M8 5V13','M5 4L3 2','M11 4L13 2','M4 7H1','M12 7H15','M4 10H1','M12 10H15','M5 13L3 15','M11 13L13 15'))
shape('bot',rr(2,4,12,10,3),union(line((8,1),(8,4)),dots((5.5,8),(10.5,8),r=1),line((6,11),(10,11))))
agent_back = rr(1.45,2.6,8.6,7.5)
agent_front = rr(5.3,6.1,9.1,8)
agent_face = union(dots((7.8,9.1),(11.9,9.1),r=.6),line((8.4,11.65),(11.3,11.65)))
antenna = line((5.75,1.35),(5.75,2.6))
shape('agents',union(agent_back,agent_front),union(stroke(agent_front),agent_face,antenna))
shape('brain',path('M8 3C4-1 1 3 2 6C-1 8 1 12 4 12C4 16 8 15 8 13C8 15 12 16 12 12C15 12 17 8 14 6C15 3 12-1 8 3Z'),stroke('M8 3V13M4 5Q4 7 6 7M12 9Q10 9 10 11'))
shape('extension',path('M2 3H6C4.5-.5 11.5-.5 10 3H13V6C16.5 4.5 16.5 11.5 13 10V13H10C11.5 9.5 4.5 9.5 6 13H2V10C5.5 11.5 5.5 4.5 2 6Z'))
wrench = path('M12.3 1.8L9.55 4.65L11.5 6.6L14.35 3.8C15.7 7.05 13.3 10.2 10.1 9.5'
              'L5.25 14.05C3.1 15.95 .65 13.1 2.3 11.4L7.15 6.55C6.45 3.15 9.25 .85 12.3 1.8Z')
shape('wrench',wrench,circle(3.9,12.55,.75))
GEAR_TOOTH=path('M8 8L6.201388 3.657766Q6.75 3.45 6.75 2.95V1.7Q6.75 1.25 7.2 1.25H8.8Q9.25 1.25 9.25 1.7V2.95Q9.25 3.45 9.798612 3.657766Z')
GEAR=union(*(transform(GEAR_TOOTH,i*45) for i in range(8)))
shape('settings',op(GEAR,circle(8,8,2.4),po.PathOp.DIFFERENCE))
glyph('power',stroke('M4.1 3.8A5.8 5.8 0 1 0 11.9 3.8'),line((8,1.5),(8,7.5)))
glyph('spinner',stroke('M13 11A5.8 5.8 0 1 1 8 2.2',1.35),stroke('M8 2.2A5.8 5.8 0 0 1 13.8 8',1.35))
for name,n in [('gauge-low',-65),('gauge-medium',0),('gauge-high',25),('gauge-max',65)]:
    length = 2.55 if abs(n) == 65 else 4
    end=(8+length*math.sin(math.radians(n)),10-length*math.cos(math.radians(n)))
    shape(name,path('M2 13A7 7 0 1 1 14 13Z'),union(line((8,10),end),circle(8,10,1),lines('M3 8H4','M12 8H13')))
shape('logs',WINDOW,union(dots((4,5),(4,8),(4,11),r=.5),lines('M6 5H12','M6 8H10','M6 11H11')))
shape('diff',rr(1.5,2,13,12,2),union(plus(8,5,.7),line((6,11),(10,11))))
glyph('fold-vertical',lines('M2 8H14'),lines('M5 2l3 3 3-3','M5 14l3-3 3 3'))
shape('cursor',path('M3.1 1.8L13.5 8.5L9 9.2L11.2 13.15L9.1 14.35L6.85 10.3L3.65 13.5Z'))
shape('themes',circle(),path('M8 2A6 6 0 0 1 8 14Z'))
shape('lightbulb',path('M5 11C5 9 2.5 8 2.5 6A5.5 5.5 0 0 1 13.5 6C13.5 8 11 9 11 11Z'),lines('M5.5 13H10.5','M6.5 15H9.5','M8 11V7','M6 6l2 1 2-1'))
STAR=path('M8 1.5L10 5.7 14.5 6.3 11.2 9.5 12 14 8 11.8 4 14 4.8 9.5 1.5 6.3 6 5.7Z')
shape('star',STAR)
def sparkle(x,y,r):
    shoulder = .18*r
    return path(f'M{x} {y-r}Q{x+shoulder} {y-shoulder} {x+r} {y}'
                f'Q{x+shoulder} {y+shoulder} {x} {y+r}Q{x-shoulder} {y+shoulder} {x-r} {y}'
                f'Q{x-shoulder} {y-shoulder} {x} {y-r}Z')

shape('sparkles',sparkle(5.95,9.55,4.6),sparkle(11.95,4.1,2.65))
shape('zap',path('M9 1L2 9H7L6 15 14 6H9Z'))

CATEGORY='Charts and analytics'
chart_columns = union(*(rr(x,y,2.15,11.55-y) for x,y in ((4.25,7.15),(8.15,3.1),(12.05,5.3))))
for name,detail in [('chart-bar',chart_columns),('chart-line',line((3,11),(6,7),(9,9),(13,4))),('chart-area',poly([(4.55,11.5),(4.55,9.3),(6.8,6.1),(9.1,7.8),(13.45,3.4),(13.45,11.5)])),('trending-up',lines('M2 12L6 8 9 10 14 3','M10 3H14V7')),('trending-down',lines('M2 4L6 8 9 6 13 11.5','M9 11.5H13V7.5'))]: glyph(name,lines('M2 2V14H14'),detail)
pie = path('M7 2A5.9 5.9 0 1 0 14 9H7Z')
quarter = path('M9.3 1.7A6 6 0 0 1 14.3 6.7H9.3Z')
shape('chart-pie', union(pie, quarter))
shape('chart-donut',ring(8,8,6,2.5),path('M8 2A6 6 0 0 1 14 8H10.5A2.5 2.5 0 0 0 8 5.5Z'))
shape('activity',WINDOW,line((1.5,8),(5,8),(7,4),(9,12),(11,8),(14.5,8)))
shape('workflow',union(poly([(8,1),(11,4),(8,7),(5,4)]),rr(1,11,5,4,1),rr(10,11,5,4,1)),stroke('M8 7V9H3.5V11M8 9H12.5V11'))
compare_end = union(ring(3.45,12.25,2.05,1.1),
                    stroke('M3.45 10.25V5.6Q3.45 3.65 5.45 3.65H7.2M5.3 1.75L7.2 3.65L5.3 5.55',1.25))
glyph('git-compare',compare_end,transform(compare_end,180))

CATEGORY='Finance and commerce'
shape('credit-card',rr(1.5,3,13,10,2),lines('M1.5 6H14.5','M4 10H7','M10 10H12'))
wallet_front = rr(1.65,5.35,12.7,8.75)
wallet_back = path('M2.45 5.55L10.75 1.85Q11.65 1.5 11.65 2.55V5.55Z')
wallet_clasp = rr(9.6,8.05,4.75,3.15)
shape('wallet',union(wallet_front,wallet_back),
      union(line((2.45,5.35),(12.85,5.35)),stroke(wallet_clasp)))
shape('banknote',rr(1,3,14,10,1),union(ring(8,8,2.3,1.2),dots((3.5,8),(12.5,8))))
# Cylindrical stacks share the same elliptical ends. Only the exposed
# part of the taller rear stack contributes interior lines.
def coin_stack(x, y, width, height):
    rx, ry = width / 2, 1.65
    return path(f'M{x} {y}a{rx} {ry} 0 1 1 {width} 0v{height}'
                f'a{rx} {ry} 0 0 1 {-width} 0Z')

front_coins = coin_stack(1.6, 8.5, 7.8, 3.3)
rear_coins = coin_stack(6.5, 4.4, 7.9, 4.6)
coin_rims = stroke('M6.5 4.4a3.95 1.65 0 0 0 7.9 0M6.5 6.8a3.95 1.65 0 0 0 7.9 0', 1.1)
coin_seams = union(op(coin_rims, front_coins, po.PathOp.DIFFERENCE),
                   stroke(front_coins, 1.25), stroke('M1.6 8.5a3.9 1.65 0 0 0 7.8 0', 1.15))
shape('coins', union(front_coins, rear_coins), coin_seams)
# The overlap line only cuts the rear stack. Across both faces the rim
# follows one ellipse and stays clear of the outside wall.
coin_front = union(front_coins, stroke(front_coins, 1.25))
coin_back = union(rear_coins, stroke(rear_coins, 1.25))
back_rims = stroke('M7.7 5.55Q10.45 6.8 13.2 5.55M10.8 8.4Q12.1 8.4 13.2 7.9', 1.15)
front_rim = stroke('M2.8 9.65Q5.5 11 8.2 9.65', 1.15)
STYLE_OVERRIDES['coins'] = {'solid': union(
    op(coin_back, union(back_rims, coin_front, stroke(coin_front, 2)), po.PathOp.DIFFERENCE),
    op(coin_front, front_rim, po.PathOp.DIFFERENCE))}
shape('receipt',path('M3 1.55L5 2.85L7 1.55L9 2.85L11 1.55L13 2.85V14.45L11 13.15'
                     'L9 14.45L7 13.15L5 14.45L3 13.15Z'),
      lines('M5.45 5.45H10.55','M5.45 8H10.55','M7.8 10.6H10.55'))
bag = path('M3.65 5.7H12.35L13.55 13.55Q13.65 14.3 12.75 14.3H3.25Q2.35 14.3 2.45 13.55Z')
handle = stroke('M5.55 7.75V4.05A2.45 2.45 0 0 1 10.45 4.05V7.75')
shape('shopping-bag',bag,handle)
STYLE_OVERRIDES['shopping-bag'] = {'solid':op(union(bag,stroke(bag),handle),
    union(circle(5.55,7.75,.7),circle(10.45,7.75,.7)),po.PathOp.DIFFERENCE)}
shape('shopping-cart',path('M3 4H15L13 10H5Z'),union(stroke('M1 1.5H2.5L5 10'),circle(6,13.5,1.2),circle(12,13.5,1.2)))
shape('basket',path('M1.65 6.35H14.35L12.65 13.6H3.35Z'),
      lines('M4.05 6.35L7.4 2.7Q8 2 8.6 2.7L11.95 6.35', 'M6.1 8.85V11.15', 'M9.9 8.85V11.15'))
AWNING=path('M3 2H13L14.5 6Q14.5 8 12.3 8Q10.2 8 10.2 6Q10.2 8 8 8Q5.8 8 5.8 6Q5.8 8 3.7 8Q1.5 8 1.5 6Z')
shape('store',union(rr(2.5,6,11,8.5,1),AWNING),union(stroke(AWNING,1.1),stroke('M6.3 14V10H9.7V14',1.1),lines('M6.5 2L5.8 6','M9.5 2L10.2 6')))
shape('tag',path('M2 2H8L14 8Q15 9 14 10L10 14Q9 15 8 14L2 8Z'),circle(5,5,1))
shape('gift',rr(2,6,12,8,1),union(stroke('M8 6V14M1 6H15V9H1ZM8 6C1 6 3 0 6 2L8 6C15 6 13 0 10 2Z',1.2)))
package_field = path('M1.65 4.75L8 1.65L14.35 4.75V11.45L8 14.4L1.65 11.45Z')
package_lid = path('M1.65 4.75L8 1.65L14.35 4.75L8 8.05Z')
tape = op(line((4.75,3.2),(11.2,6.4)),package_lid,po.PathOp.INTERSECTION)
shape('package',package_field,union(tape,stroke('M1.65 4.75L8 8.05L14.35 4.75M8 8.05V14.4')))
shape('barcode', rr(1.5,3,13,10),
      lines('M4 5.35V10.65', 'M6.3 5.35V10.65', 'M9.5 5.35V10.65', 'M12 5.35V10.65'))
shape('percent',circle(),union(line((5.55,10.9),(10.45,5.1),width=1.25),circle(5.7,5.7,.9),circle(10.3,10.3,.9)))
shape('dollar', circle(), stroke('M10.3 5.55C8.3 4.2 5.6 4.95 5.6 6.45'
                                'C5.6 8.45 10.4 7.65 10.4 9.7C10.4 11.35 7.55 12 5.55 10.55M8 3.95V12.05'))
shape('euro', circle(), stroke('M10.55 5.05C7.8 3.45 6.1 5.35 6.1 8C6.1 10.8 7.9 12.5 10.55 10.95M4.85 6.85H9.05M4.85 9.15H8.7', 1.2))
shape('pound', circle(), stroke('M5.55 11.15H10.6M5.3 8.15H9.25M6.6 11.15V6.65Q6.6 3.65 9.95 4.95', 1.2))

CATEGORY='Work and education'
shape('briefcase',rr(1.5,5,13,9,2),stroke('M5 5V2H11V5M1.5 8Q8 12 14.5 8M8 9V11'))
building = path('M3 2.9Q3 1.65 4.25 1.65H11.75Q13 1.65 13 2.9V14.35H9.9V11.1H6.1V14.35H3Z')
windows = union(*(rr(x,y,2.35,2.35) for x in (4.75,8.9) for y in (3.25,6.55)))
shape('building',building,union(windows,line((3,9.95),(13,9.95))))
shape('landmark',path('M1 6L8 1.5 15 6Z'),lines('M1 14H15','M3 8V12','M8 8V12','M13 8V12'))
shape('presentation',rr(1.5,2,13,9,1),lines('M8 11V15','M5 15L8 12 11 15','M4 8L7 5 9 7 12 4'))
shape('book',rr(2.85,1.65,10.3,12.7),
      stroke('M2.85 11.45H13.15M5.4 1.85V11.45M7.6 5.55H10.85'))
shape('book-open',path('M8 3Q4 1 1.5 2V13Q4 12 8 14Q12 12 14.5 13V2Q12 1 8 3Z'),line((8,3),(8,14)))
shape('graduation-cap',path('M1 6L8 2 15 6 8 10Z'),stroke('M4 8V11Q8 15 12 11V8M15 6V11'))
shape('award',circle(8,6,4.5),union(path('M5 10L3 15 8 13 13 15 11 10Z'),circle(8,6,1.5)))
shape('medal',circle(8,10,4.5),union(path('M3 1H6L8 5 10 1H13L10 6H6Z'),circle(8,10,1.5)))
shape('lightbulb-on',DRAWINGS['lightbulb'][0],union(DRAWINGS['lightbulb'][1],lines('M1 2L2 3','M14 3L15 2')))
shape('flask',path('M5 1H11V3H10V7L14 13Q15 15 12 15H4Q1 15 2 13L6 7V3H5Z'),union(line((5,10),(11,10)),dots((7,12),(10,13),r=.5)))
shape('test-tube',path('M4.5 1.5H11.5V10.5A3.5 3.5 0 0 1 4.5 10.5Z'),lines('M3.5 1.5H12.5','M4.5 8H11.5','M9 4.5H11'))
orbit = stroke('M8 1.55A2.75 6.45 0 1 0 8 14.45A2.75 6.45 0 1 0 8 1.55Z')
glyph('atom',union(orbit,transform(orbit,60),transform(orbit,-60)),circle(8,8,.7))
rocket_body = path('M5.3 10.7C4.7 5.7 8.4 1.65 14.25 1.65C14.3 7.65 10.45 11.3 5.3 10.7Z')
rear_fins = path('M5.8 5.95Q2.4 6.4 1.95 10.1L5.3 9.5Z'
                 'M10.1 10.2Q9.55 13.7 5.85 14.1L6.55 10.75Z')
exhaust = path('M3.95 11.85Q1.9 11.8 1.55 14.45Q4.25 14.1 4.15 12.05Z')
rocket_field = union(rocket_body,rear_fins)
port = ring(10.45,5.5,1.65)
shape('rocket',rocket_field,union(stroke(rocket_body),port,exhaust))
STYLE_OVERRIDES['rocket'] = {'solid':union(op(union(rocket_field,stroke(rocket_field)),circle(10.45,5.5,1.2),po.PathOp.DIFFERENCE),exhaust)}
glyph('infinity',stroke('M8 8C0-3-3 18 8 8'),stroke('M8 8C19-3 16 18 8 8'))

CATEGORY='Health and fitness'
HEART=path('M8 14L2.7 8.7C-1.2 4.8 4.3 .2 8 4C11.7 .2 17.2 4.8 13.3 8.7Z')
shape('heart',HEART)
pulse = line((1.75,8),(4.55,8),(6.1,5.65),(8.05,10.45),(9.9,8),(14.25,8))
shape('heart-pulse',HEART,op(pulse,HEART,po.PathOp.INTERSECTION))
shape('medical-cross',rr(),plus(8,8,1.5))
shape('first-aid',rr(1.5,4,13,10,2),union(plus(8,9,1),stroke('M5 4V1.5H11V4')))
capsule = path('M4.65 5A3.35 3.35 0 0 1 11.35 5V11A3.35 3.35 0 0 1 4.65 11Z')
capsule_seam = op(line((4.65,8),(11.35,8)),capsule,po.PathOp.INTERSECTION)
shape('pill',transform(capsule,42),transform(capsule_seam,42))
glyph('stethoscope',stroke('M2 2V6A4 4 0 0 0 10 6V2M2 2H3M9 2H10'),union(ring(13,8.5,1.6,1.1),stroke('M6 10V11.5Q6 14.5 9.5 14.5T13 11.5V10')))
shape('thermometer',path('M6 3A2 2 0 0 1 10 3V9A3.5 3.5 0 1 1 6 9Z'),union(line((8,5),(8,11)),circle(8,11.5,1.3)))
shape('bandage',transform(rr(1,4,14,8,3),-45),union(transform(rr(5,5.5,6,5,1),-45),transform(dots((3,7),(3,9),(13,7),(13,9),r=.45),-45)))
hospital_field = path('M1.55 7.4H4.2V1.7H11.8V7.4H14.45V14.2H1.55Z')
shape('hospital',hospital_field,union(plus(8,5.1,.72),stroke('M6.45 14.2V10.2H9.55V14.2')))
weight_plates = union(rr(1.35,5.55,2.45,4.9),rr(4.4,3.65,2.55,8.7))
dumbbell_ends = union(weight_plates,mirror(weight_plates))
glyph('dumbbell',transform(dumbbell_ends,-28),transform(line((3.5,8),(12.5,8)),-28))
shape('weight',path('M5 6.5H11L14 13Q14.6 14.5 12.5 14.5H3.5Q1.4 14.5 2 13Z'),stroke('M5.5 6.5V4A2.5 2.5 0 0 1 10.5 4V6.5'))
forefoot = path('M5.65 10.1H2.25C1.65 8.85 1.4 7.15 1.7 5.6'
                'C2.15 3.4 4.6 2.7 6 4.2C7.4 5.65 6.9 7.2 6.2 8.55Z')
heel = path('M2.45 11.4H5.6L5.5 12.9C5.35 14.85 2.8 14.85 2.6 13.05Z')
footprint = transform(union(forefoot,heel),-12,dx=.55)
glyph('footprints',footprint,transform(mirror(footprint),dy=-2.65))
bed_frame = path('M2 8L3.2 4Q3.5 3 4.7 3H11.3Q12.5 3 12.8 4L14 8V12H2Z')
pillows = union(rr(4, 5, 3.2, 1.8, .65), rr(8.8, 5, 3.2, 1.8, .65))
shape('bed', bed_frame, union(pillows, lines('M2 10H14', 'M2 12V13.9', 'M14 12V13.9')))
shape('moon',path('M10.7 1.8A6.4 6.4 0 1 0 14.2 10.7A5.2 5.2 0 0 1 10.7 1.8Z'))
shape('apple',path('M8 5C1 1 0 9 4 13C5.5 15 6.5 13.5 8 13.5S10.5 15 12 13C16 9 15 1 8 5Z'),stroke('M8 5Q8 1 11 1'))
shape('droplet',path('M8 1C6 5 2 7 2 10A6 6 0 0 0 14 10C14 7 10 5 8 1Z'),stroke('M5 10Q5 12 7 12'))
lung_l = path('M5.65 4.6C4.05 4.55 2.55 7.6 1.85 11.5Q1.15 14.7 3.55 14'
              'L5.65 13Q6.6 12.55 6.55 10.9L6.35 5.55Q6.3 4.65 5.65 4.6Z')
airway = stroke('M8 1.55V5.55M5.15 8.85L8 5.55L10.85 8.85')
shape('lungs',union(lung_l,mirror(lung_l)),airway)

CATEGORY='Maps and travel'
PIN=path('M8 15C4 10 2 8 2 6A6 6 0 0 1 14 6C14 8 12 10 8 15Z')
pin_drop = path('M8 14.5C6.35 12.65 2.8 9.05 2.8 6.5A5.2 5.2 0 0 1 13.2 6.5C13.2 9.05 9.65 12.65 8 14.5Z')
shape('map-pin', pin_drop, ring(8,6.45,2.25))
shape('map',path('M1.5 3L6 1.5 10 3 14.5 1.5V13L10 14.5 6 13 1.5 14.5Z'),lines('M6 1.5V13','M10 3V14.5'))
shape('navigation',path('M14.2 1.8L9.3 14.2L7.2 8.8L1.8 6.7Z'))
shape('globe', circle(), stroke('M2 8H14M8 2C4.5 5 4.5 11 8 14C11.5 11 11.5 5 8 2Z'
                                'M3.45 4.1Q8 7.1 12.55 4.1M3.45 11.9Q8 8.9 12.55 11.9'))
route_line = stroke('M4.45 3.25H10.65A2.45 2.45 0 0 1 10.65 8.15H5.35'
                    'A2.45 2.45 0 0 0 5.35 13.05H11.35')
glyph('route',route_line,union(circle(3.2,3.25,1.55),circle(12.6,13.05,1.55)))
car_field = path('M3 6.6L4.7 2.65H11.3L13 6.6L14.25 7.7V12H1.75V7.7Z')
windshield = path('M3.9 6.6L5.2 3.45H10.8L12.1 6.6Z')
car_lamps = dots((4.35,9.3),(11.65,9.3),r=.7)
car_feet = lines('M2.5 12V13.7','M13.5 12V13.7')
shape('car', car_field, union(line((3,6.6),(13,6.6)), car_lamps, car_feet))
STYLE_OVERRIDES['car'] = {'solid': op(union(car_field,stroke(car_field),car_feet),
                                    union(windshield,car_lamps),po.PathOp.DIFFERENCE)}
truck_box = rr(1.45,3.25,8.25,6.35)
cab = path('M9.7 5.8H12.1L14.5 8.85V9.6H9.7Z')
tires = union(ring(4.15,12.1,1.8),ring(11.95,12.1,1.8))
shape('truck',union(truck_box,cab),union(tires,stroke('M9.7 5.8V9.6M9.7 7.9H13.65')))
shape('bus', rr(2.55,1.7,10.9,11.2), union(
    stroke('M2.55 6.7H13.45M2.55 9.85H13.45M5.6 1.7V6.7M10.4 1.7V6.7'
           'M4.4 12.9V14.5M11.6 12.9V14.5'),dots((5.1,8.25),(10.9,8.25),r=.53)))
shape('train',rr(3,1,10,12,3),union(stroke('M3 6H13M8 1V6M5 13L3 15M11 13L13 15'),dots((5.5,9.5),(10.5,9.5),r=.8)))
glyph('bicycle',union(ring(3.95,10.95,3.2),ring(12.05,10.95,3.2)),
      stroke('M3.95 10.95L6.9 5.55H10.75L7.85 10.95H3.95M7.85 10.95L5.95 4H4.45'
             'M12.05 10.95L10.2 2.55H12.8'))
plane_body = path('M6.55 3.55Q6.55 1.35 8 1.35Q9.45 1.35 9.45 3.55V6.35'
                  'L14.55 9.45V11.55L9.35 9.65V12.05L11.1 13.95V14.35L8 13.45'
                  'L4.9 14.35V13.95L6.65 12.05V9.65L1.45 11.55V9.45L6.55 6.35Z')
shape('plane',plane_body)
hull = path('M1.65 8.6L8 6.55L14.35 8.6L12.45 11.55H3.55Z')
cabin = path('M4.3 7.7V3.65H11.7V7.7L8 6.55Z')
wave = stroke('M1.7 14.1Q3.25 12.85 4.85 14.1T8 14.1Q9.55 12.85 11.15 14.1T14.3 14.1')
shape('ship',union(hull,cabin),union(stroke('M1.65 8.6L8 6.55L14.35 8.6M8 3.65V6.55'),stroke('M6.9 3.65V1.65H9.1V3.65'),wave))
shape('suitcase',rr(2.65,4.15,10.7,9.45),stroke(
    'M5.95 4.15V1.8H10.05V4.15M5.55 6.5V11.25M10.45 6.5V11.25M4.65 13.6V14.7M11.35 13.6V14.7'))
ticket = path('M1.55 3H14.45V5.95C11.1 6.15 11.1 9.85 14.45 10.05V13H1.55'
              'V10.05C4.9 9.85 4.9 6.15 1.55 5.95Z')
shape('ticket',ticket,lines('M9.7 5.2V6.25','M9.7 9.75V10.8'))
tent_shell = poly([(8,2.4),(14.55,13.7),(1.45,13.7)])
shape('tent', tent_shell, stroke('M8 2.4V7.3M4.55 13.7L8 7.3L11.45 13.7'
                               'M4.15 9.05L8 7.3L11.85 9.05'))
shape('mountain',poly([(1.45,13.8),(6.05,2.65),(9.3,8.45),(11.1,5.25),(14.55,13.8)]),
      stroke('M4.2 7.05L5.65 8.25L6.8 6.85L7.95 7.05'))
shape('signpost',poly([(1.5,3),(11.5,3),(14.5,6),(11.5,9),(1.5,9)]),lines('M7 1V3','M7 9V15'))
shape('parking',rr(),stroke('M6 12V4H9A2 2 0 0 1 9 8H6',1.5))
shape('fuel',rr(2,2,8,12,1),union(rr(4,4,4,4,.5),stroke('M10 6H12V12Q15 15 15 11V6L12 3')))

CATEGORY='Weather and nature'
shape('sun',circle(8,8,3.5),lines('M8 1V2','M8 14V15','M1 8H2','M14 8H15','M3 3l1 1','M12 12l1 1','M3 13l1-1','M12 4l1-1'))
shape('sunrise',path('M3 12A5 5 0 0 1 13 12Z'),lines('M1 12H15','M3 14.5H13','M8 1.3V4.8','M5.7 3.6L8 1.3 10.3 3.6','M1 8H2','M14 8H15'))
shape('sunset',path('M3 12A5 5 0 0 1 13 12Z'),lines('M1 12H15','M3 14.5H13','M8 1.3V4.8','M5.7 2.5L8 4.8 10.3 2.5','M1 8H2','M14 8H15'))
for name,detail in [('cloud-rain',lines('M4 12L3 15','M8 12L7 15','M12 12L11 15')),('cloud-snow',dots((4,13),(8,14),(12,13))),('cloud-lightning',stroke('M8.75 10.4L6.5 12.65H9.35L7.4 14.75')),('cloud-fog',lines('M2.65 11.55H13.35','M4.2 14.15H11.8'))]:
    # Make room beneath the cloud for the two fog bands or the bolt.
    if name in {'cloud-fog','cloud-lightning'}:
        cloud = path('M4.1 8.95C.65 8.95 .6 4.5 4.05 4.45C4.9 .3 11.05 .45 11.85 4.5C15.65 4.7 15.55 8.95 12 8.95Z')
    else:
        cloud = transform(DRAWINGS['cloud'][0],0,.85,0,-2)
    shape(name,cloud,detail)
snow_axis = line((8, 1.35), (8, 14.65))
snow_fork = line((6.4, 2.1), (8, 3.65), (9.6, 2.1))
crystal = stroke(path('M8 4.25L11.2476 6.125V9.875L8 11.75L4.7524 9.875V6.125Z'))
glyph('snowflake', union(*(transform(snow_axis, i*60) for i in range(3))),
      union(crystal, *(transform(snow_fork, i*60) for i in range(6))))
glyph('wind',stroke('M1 5H10Q14 5 13 2Q12 0 10 2M1 8H13Q16 8 15 11Q14 13 12 11'),stroke('M2 11H7Q10 11 9 14Q8 16 6 14'))
canopy = path('M1.55 8.65A6.45 6.45 0 0 1 14.45 8.65Q12.25 6.9 10.15 8.65'
              'Q8 6.9 5.85 8.65Q3.75 6.9 1.55 8.65Z')
umbrella_handle = stroke('M8 7.9V12.4C8 14.85 11.75 14.85 11.75 12.4')
shape('umbrella',canopy,union(umbrella_handle,line((8,1.35),(8,2.2))))
STYLE_OVERRIDES['umbrella'] = {'solid':union(canopy,stroke(canopy),umbrella_handle,line((8,1.35),(8,2.2)))}
glyph('rainbow',stroke('M1.5 13V9A6.5 6.5 0 0 1 14.5 9V13',1.2),stroke('M4 13V9A4 4 0 0 1 12 9V13M6.5 13V9A1.5 1.5 0 0 1 9.5 9V13',1.2))
shape('leaf',path('M2 13C0 3 8 1 14 2C15 10 10 16 2 13Z'),stroke('M2 13L11 5M6 9V5M6 9H10'))
shape('tree',path('M8 1L14 7H11L15 12H1L5 7H2Z'),line((8,10),(8,15)))
petal_quarter = 'C9.05 3.2 11.7 1.55 13.35 3.2C15 4.85 13.7 7.05 11.6 8'
petal = path('M8 8V4.4' + petal_quarter + 'Z')
flower_body = union(*(transform(petal,angle) for angle in (0,90,180,270)))
shape('flower', flower_body, ring(8,8,1.95))
sprout_leaves = path('M8 9.25C4.35 9.3 2.4 7.15 2.15 4.55C5.6 4.55 7.75 6.35 8 9.25Z'
                     'M8 9.25C8.25 5.4 10.25 3.25 13.85 2.85C13.65 6.45 11.5 8.75 8 9.25Z')
shape('sprout',sprout_leaves,line((8,9.25),(8,14.05)))
flame = path('M8.25 1.55C8.1 5.15 3.2 6.25 2.85 10.15C2.3 15.7 12.75 16 13.15 10.3'
             'Q13.45 7.15 11.4 4.85Q11.45 7.25 9.65 7.85Q8.5 5.75 8.25 1.55Z')
ember = path('M7.7 9.15C7.35 10.4 6.25 10.95 6.25 12.05C6.25 13.75 9.65 13.75 9.65 12.1Q9.65 10.8 7.7 9.15Z')
shape('flame', flame, stroke(ember))
RECYCLE_ARM=stroke('M5 4L7 1.7Q8 1 8.7 2.2L11 6M8 5.3L11 6 11.5 3',1.15)
glyph('recycle',union(RECYCLE_ARM,transform(RECYCLE_ARM,120)),transform(RECYCLE_ARM,240))
shape('paw',path('M4 11Q8 5 12 11Q15 16 10 14Q8 13 6 14Q1 16 4 11Z'),union(circle(2,6,1.5),circle(6,3,1.5),circle(10,3,1.5),circle(14,6,1.5)))
shape('fish',path('M10.65 7.25Q11.15 7.8 11.65 7.3L14.35 4.8V11.2L11.65 8.7'
                  'Q11.15 8.2 10.65 8.75C7.3 14.5 1.6 12.4 1.6 8C1.6 3.6 7.3 1.5 10.65 7.25Z'),
      union(circle(3.9,7.4,.65),stroke('M5.15 4.45Q7.45 8 5.15 11.55')))

CATEGORY='Home and food'
shape('coffee',rr(2,5,9,8,2),stroke('M11 6H13Q17 9 11 11M1 15H13M4 1V3M8 1V3'))
shape('cup',path('M3 2H13L11 14H5Z'),line((4,5),(12,5)))
knife_blade = path('M13.3 1.75V8.4H10.3Q10.3 4.35 13.3 1.75Z')
knife_handle = line((13.3,8.4),(13.3,14.25))
fork = stroke('M2.1 1.75V5Q2.1 7 4.15 7T6.2 5V1.75M4.15 1.75V14.25')
glyph('utensils',fork,union(knife_blade,stroke(knife_blade),knife_handle))
STYLE_OVERRIDES['utensils'] = {'stroke': union(fork, stroke(knife_blade),knife_handle)}
pizza_slice = path('M1.6 3.7Q8 .4 14.4 3.7L8 14.15Z')
pizza_crust = op(stroke('M1.65 6.3Q8 3.35 14.35 6.3'),pizza_slice,po.PathOp.INTERSECTION)
shape('pizza', pizza_slice, union(pizza_crust,dots((6.25,7.3),(9.6,6.85),(8,10.55),r=.7)))
shape('cake',rr(2,7,12,7,1),union(stroke('M2 10Q4 12 6 10Q8 12 10 10Q12 12 14 10M5 7V4M11 7V4'),circle(5,2,.8),circle(11,2,.8)))
shape('wine',path('M4 1.5H12V6A4 4 0 0 1 4 6Z'),stroke('M8 10V14M5 14H11M4 5H12'))
shape('bottle',path('M6 1H10V5L12 8V14H4V8L6 5Z'),lines('M6 3H10','M4 10H12'))
shape('chef-hat',path('M4 9C-1 9 0 3 4 3Q8-2 12 3C16 3 17 9 12 9V14H4Z'),stroke('M4 11H12M7 8V10M10 7V10'))
sofa_body = union(rr(2.4,3.3,11.2,8,2), rr(1.5,7.3,13,5.2,1.25))
sofa_seam = stroke('M1.5 8.8Q1.5 7.3 3 7.3T4.5 8.8V10H11.5V8.8'
                   'Q11.5 7.3 13 7.3T14.5 8.8', 1.2)
shape('sofa', sofa_body, union(sofa_seam, lines('M8 3.3V10', 'M3 12.5V14', 'M13 12.5V14')))
shape('lamp',path('M5 2H11L14 9H2Z'),lines('M8 9V14','M5 14H11'))
shape('door-open',path('M3 3L11 1V15L3 13Z'),union(stroke('M11 3H14V13H11'),circle(8.5,8,.65)))
key_head = circle(5.35,5.4,3.5)
key_bit = path('M6.7 8.15L8.15 6.7L14.3 12.85V14.2H11.15V11.95H8.95V10.2Z')
shape('key-round', union(key_head,key_bit), stroke(circle(5.15,5.2,1.5)))
shape('plug',rr(4,5,8,5,2),stroke('M5.5 1V5M10.5 1V5M8 10V15'))
fan_blade = path('M7.6 7.45C6.35 6.8 5.25 5.2 6.35 4.25C7.75 3.05 9.8 4.1 9.2 5.7Q8.8 6.8 8.45 7.55Z')
fan_blades = union(*(transform(fan_blade,i*120) for i in range(3)),circle(8,8,.85))
shape('fan',circle(),fan_blades)
shape('gamepad',path('M4 4H12Q14 4 15 11Q16 15 12 13L10 11H6L4 13Q0 15 1 11Q2 4 4 4Z'),union(plus(5,8,.65),dots((10.5,7),(12.5,9),r=.7)))
shape('puzzle',DRAWINGS['extension'][0])
glyph('music-note',DRAWINGS['music'][0],DRAWINGS['music'][1])
shape('bell-ring',BELL,union(line((6,14),(10,14)),lines('M1 3L2 2','M14 2L15 3')))

CATEGORY='Editing and design'
clip_wire = path('M9.55 4.55V10.4A1.35 1.35 0 0 1 6.85 10.4V4.5A2.55 2.55 0 0 1 11.95 4.5V10.4'
                 'A3.75 3.75 0 0 1 4.45 10.4V4.4')
glyph('paperclip',stroke(transform(clip_wire,38)),po.Path())
CATEGORY='Technology and development'
shape('ssh', rr(1.5, 2.8, 13, 10.4, 1.8),
      union(stroke('M4 6.3L5.9 8.2L4 10.1', 1.25),
            stroke('M8 10L11.8 6.2M8.8 6.2H11.8V9.2', 1.2)))
CATEGORY='Actions and status'
shape('refresh-circle-fill', circle(), stroke('M10.7 9.5A3.05 3.05 0 1 1 10.5 6.15M8.3 6.15H10.5V4.3', 1.25))

CATEGORY='Actions and status'
glyph('menu',lines('M2 3H14','M2 13H14'),line((2,8),(14,8)))
CATEGORY='Technology and development'
for name,level in [('battery-full',8),('battery-low',2),('battery-empty',0)]:
    shape(name,rr(1,4,12,8,1.5),union(rr(3,6,level,4,.5) if level else po.Path(),line((15,6.5),(15,9.5))))
glyph('wifi-off',DRAWINGS['wifi'][0],union(DRAWINGS['wifi'][1],line((2,2),(14,14))))
DRAWINGS['bluetooth-off'] = DRAWINGS['bluetooth']
shape('cloud-off',DRAWINGS['cloud'][0],line((2,2),(14,14)))
shape('git-fork',union(circle(3,3,1.7),circle(13,3,1.7),circle(8,13,1.7)),stroke('M3 5V6Q3 8 8 8Q13 8 13 6V5M8 8V11'))
CATEGORY='Files and folders'
for name,angle in [('folder-upload',270),('folder-download',90)]:shape(name, path('M1.6 4Q1.6 3 2.7 3H6L8 5H13.3Q14.4 5 14.4 6.1V12.5Q14.4 14 13 14H3Q1.6 14 1.6 12.5Z'), arrow(angle, .48, dy=1.45, width=1.25))
for name,angle in [('file-upload',270),('file-download',90)]:shape(name,FILE,union(FOLD,arrow(angle, .43, dx=-.45, dy=2.05, width=1.2)))
CATEGORY='Communication'
for name,detail in [('mail-check',check(8,9.8,.55)),('mail-plus',plus(8,9.8,.6))]:
    shape(name,rr(1.5,3,13,10,2),union(line((2,4),(8,6.3),(14,4)),detail))
shape('bell-plus',BELL,union(plus(8,7,.7),line((6,14),(10,14))))
CATEGORY='Media'
shape('image-plus',DRAWINGS['image'][0],union(line((2,12),(6,8),(10,12)),plus(11,5,.65)))
for name,angle in [('fast-forward',0),('rewind',180)]:
    glyph(name,transform(poly([(1.5,3),(8,8),(1.5,13)]),angle),transform(poly([(8,3),(14.5,8),(8,13)]),angle))
CATEGORY='Security'
shape('scan-face',rr(3.8,3.8,8.4,8.4),union(
    lines('M1.5 4.8V1.5H4.8','M11.2 1.5H14.5V4.8','M1.5 11.2V14.5H4.8',
          'M11.2 14.5H14.5V11.2','M6.15 9.1Q8 10.55 9.85 9.1'),
    dots((6.25,6.5),(9.75,6.5),r=.55)))
shape('shield-lock',SHIELD,union(rr(5.5,7,5,4,1),stroke('M6.5 7V5.5A1.5 1.5 0 0 1 9.5 5.5V7',1.1)))
CATEGORY='Editing and design'
glyph('text-size',lines('M1 4H9','M5 4V13'),lines('M10 8H15','M12.5 8V13'))
for name,mark in [('heading-1',stroke('M12 6L14 4V13')),('heading-2',stroke('M11 6Q11 3 14 4Q16 5 13 8L11 12H15'))]:
    glyph(name,lines('M2 3V13','M8 3V13','M2 8H8'),mark)
CATEGORY='Time and planning'
shape('bookmark-check',path('M4 2H12V14L8 11 4 14Z'),check(8,6,.55))
shape('calendar-heart',CAL,union(CALTOP,path('M8 12.5L5 10C3.5 8 6 7 8 9C10 7 12.5 8 11 10Z')))
CATEGORY='Finance and commerce'
shape('yen', circle(), stroke('M5.05 4.8L8 9.25L10.95 4.8M8 9.25V12'
                              'M5.7 6.9H10.3M5.7 10.05H10.3'))

# Original coverage additions share the same authoring geometry and exports.
from expansion import register as register_expansion
register_expansion(globals())

# Format glyph corrections found during the individual legacy-art review.
# Retain the existing brand-container treatment and attribution.
BRAND_REFINEMENTS={
    # Scale the retained GraphQL foreground once; preserve every source node and edge.
    'graphql':transform(path('M7.99 2.88 A0.91 0.91 0 0 1 8.85 4.09 L10.9 5.26 Q11.15 5.07 11.46 5.07 A0.91 0.91 0 0 1 11.82 6.83 L11.82 9.17 A0.91 0.91 0 1 1 10.9 10.73 L8.85 11.91 A0.91 0.91 0 0 1 7.99 13.12 A0.91 0.91 0 0 1 7.12 11.91 L5.07 10.73 Q4.83 10.92 4.51 10.93 A0.91 0.91 0 0 1 4.16 9.17 L4.16 6.83 A0.91 0.91 0 1 1 5.07 5.26 L7.12 4.09 A0.91 0.91 0 0 1 7.99 2.88 M5.38 10.3 L5.34 10.39 L7.35 11.55 A0.91 0.91 0 0 1 8.62 11.55 L10.63 10.39 L10.6 10.3 Z M8.23 4.67 A0.95 0.95 0 0 1 7.75 4.67 L5.08 9.3 Q5.35 9.52 5.41 9.86 L10.57 9.86 Q10.62 9.52 10.9 9.3 Z M5.34 5.61 A0.9 0.9 0 0 1 4.59 6.89 L4.59 9.11 L4.69 9.11 L7.37 4.46 L7.35 4.45 Z M8.6 4.46 L11.29 9.11 L11.39 9.11 L11.39 6.89 A0.91 0.91 0 0 1 10.63 5.61 L8.62 4.45 Z'),scale=1.27),
    # Retain the C++ hexagon with a wider C aperture and pixel-legible plus counters.
    'cpp':op(transform(path('M12.44 5.44C12.37 5.32 12.27 5.2 12.16 5.14L8.39 2.97C8.18 2.84 7.82 2.84 7.61 2.97L3.84 5.14C3.62 5.27 3.44 5.58 3.44 5.83V10.17C3.44 10.3 3.49 10.44 3.56 10.56C3.64 10.68 3.73 10.8 3.84 10.86L7.61 13.03C7.82 13.16 8.18 13.16 8.39 13.03L12.16 10.86C12.27 10.8 12.36 10.68 12.44 10.56C12.51 10.44 12.56 10.3 12.56 10.17V5.83C12.56 5.7 12.51 5.56 12.44 5.44Z'),scale=1.35),union(stroke('M8.1 5.2287A3.2 3.2 0 1 0 8.1 10.7713',1.45),stroke('M8.35 8H10.05M9.2 6.6V9.4M11.75 8H13.45M12.6 6.6V9.4',1)),po.PathOp.DIFFERENCE),
    'svg':stroke('M5.5 5.5Q2.5 4.5 2.5 6.5Q2.5 7.5 4 8Q6 8.5 5 10Q4 11.5 2 10M6.5 5.5L8 10.5 9.5 5.5M14 6Q11 4.5 11 8Q11 11.5 14 10V8.5H12.7',.8),
    'html':op(poly([(3.5,3),(12.5,3),(11.2,12),(8,13),(4.8,12)]),stroke('M10.3 5H6L5.7 8H10L9.6 10.5 8 11 6.2 10.5',1.05),po.PathOp.DIFFERENCE),
    'yml':stroke('M3 4.5L5 7.5 7 4.5M5 7.5V11.5M9 5H13M9 8H13M9 11H12',1.1),
}


def svg_path(p):
    pen=SVGPathPen(None,ntos=lambda v:format(v,'.4f').rstrip('0').rstrip('.') if v else '0')
    p.draw(pen)
    return pen.getCommands()

def svg(layers):
    rows=['<svg fill="none" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">']
    for p,opacity in layers:
        if not p:continue
        rows.append(f'  <path d="{svg_path(p)}" fill="currentColor"'+(f' opacity="{opacity}"' if opacity!=1 else '')+'/>')
    return '\n'.join(rows+['</svg>',''])


def svg_comparison_key(text):
    """Ignore only the order of identical closed contours in recipe checks.

    Skia can emit disjoint contours in a different order on Linux/x86 and
    macOS/ARM. Filled closed contours have the same winding result in either
    order. Keep every command, coordinate, winding direction, layer order and
    attribute byte exact. Canonical distributed SVG bytes remain unchanged.
    """
    def sort_closed_contours(match):
        data=match.group(1)
        contours=re.findall(r'M[^M]*',data)
        if not contours or ''.join(contours)!=data or any(not c.endswith('Z') for c in contours):
            return match.group(0)
        return ' d="'+''.join(sorted(contours))+'"'
    return re.sub(r' d="([^"]*)"',sort_closed_contours,text)


def components(p):
    """Connected filled components, keeping counters with their outer contour."""
    contours=list(po.simplify(p).contours)
    outer=[c for c in contours if not c.clockwise]
    for hole in (c for c in contours if c.clockwise):
        parents=[i for i,c in enumerate(outer) if op(c,hole,po.PathOp.INTERSECTION).area >= hole.area*.999]
        if parents:
            i=min(parents,key=lambda i:outer[i].area)
            outer[i]=op(outer[i],hole,po.PathOp.DIFFERENCE)
    return outer

def stacked_solid(back,front,detail=None):
    rear=union(back,stroke(back,1.25));fore=union(front,stroke(front,1.25))
    clearance=union(fore,stroke(fore,1.5))
    if detail:
        inset=op(fore,stroke(fore,1.8),po.PathOp.DIFFERENCE)
        fore=op(fore,op(detail,inset,po.PathOp.INTERSECTION),po.PathOp.DIFFERENCE)
    return union(op(rear,clearance,po.PathOp.DIFFERENCE),fore)

def main():
    check_mode='--check' in sys.argv
    failed=[]
    def write(p,text):
        target=ROOT/p
        if check_mode:
            if not target.exists() or svg_comparison_key(target.read_text())!=svg_comparison_key(text):
                failed.append(str(p))
        else:
            target.parent.mkdir(parents=True,exist_ok=True);target.write_text(text)
    catalog=[]
    for name,(b,d,outline,category,tags) in sorted(DRAWINGS.items()):
        outer=stroke(b,1.25) if outline else po.Path()
        # Filled bodies carry the secondary tone; contours and identifying
        # details share the primary tone. Union prevents opacity stacking.
        boundary=op(outer,d,po.PathOp.DIFFERENCE) if outer else po.Path()
        two_tones = (outline and name not in SINGLE_TONE_SHAPES) or name in DUOTONE_GLYPHS
        if outline and two_tones:
            duo=[(op(b,union(boundary,d),po.PathOp.DIFFERENCE),.24),(union(boundary,d),1)]
        elif two_tones:
            duo=[(op(b,d,po.PathOp.DIFFERENCE),.4),(d,1)]
        else:
            duo=[(union(b,d,outer),1)]
        mono=union(outer,d) if outline else union(b,d)
        # Large closed detail regions need their own contour in Stroke; a
        # filled basket or folder flap would otherwise hide the interior.
        if name in {'folder-open','video-call','picture-in-picture'}:
            mono=union(outer,stroke(d,1.1))
        elif name in {'layers','skip-forward','skip-back','fast-forward','rewind'}:
            mono=union(stroke(b,1.25),stroke(d,1.25))
        elif name == 'qr-code':
            mono=union(outer,d)

        if outline:
            filled=union(b,outer)
            # Structural details remain attached. Only interior details become
            # counters; never XOR a handle, stem, wheel or connector off its body.
            interior=op(filled,stroke(filled,1.8),po.PathOp.DIFFERENCE)
            structural=[];counters=[]
            for component in components(d):
                exterior=op(component,filled,po.PathOp.DIFFERENCE)
                if exterior.area > component.area*.12:
                    structural.append(component)
                else: counters.append(component)
            cut=op(union(*counters),interior,po.PathOp.INTERSECTION)
            solid=union(op(filled,cut,po.PathOp.DIFFERENCE),*structural)
        else: solid=union(b,d)
        if name in {'skip-forward','skip-back'}:
            mono=union(stroke(b,1.15),d)
        if name in {'fast-forward','rewind'}:
            mono=union(stroke(b,1.05),stroke(d,1.05))
        if name in {'thumbs-up','thumbs-down'}:
            mono=union(outer,stroke(d))
            wrist=line((5.05,7.3),(5.05,13.85))
            if name == 'thumbs-down': wrist=transform(wrist,180)
            solid=op(union(b,outer,d),wrist,po.PathOp.DIFFERENCE)
        if name == 'film':
            sprockets=union(*(rr(x,y,1.65,1.95) for x in (2.5,11.85) for y in (3,7.05,11.1)))
            solid=op(union(b,outer),sprockets,po.PathOp.DIFFERENCE)
        if name == 'layout-grid':
            solid=union(*(rr(x,y,5.75,5.45,1) for x in (1.5,8.75) for y in (1.9,8.65)))
        if name == 'chart-area':
            mono=union(b,stroke(d,1.05))
        if name == 'chart-bar':
            # Keep outlined columns clear of both axes at small sizes.
            mono=union(b,stroke(chart_columns))
        if name == 'fan': mono=union(outer,stroke(d,1.05))

        if name == 'chart-donut':
            # Preserve the central aperture and quarter-sector divisions.
            annulus=op(circle(8,8,6),circle(8,8,3.3),po.PathOp.DIFFERENCE)
            solid=op(annulus,lines('M8 1.5V4.7','M11.3 8H14.5'),po.PathOp.DIFFERENCE)
            # Sector color is data encoding, not surface depth. Keep the
            # divisions explicit as gaps instead of splitting a ring's tone.
            duo=[(solid,1)]
            mono=union(stroke(circle(8,8,6),1.1),stroke(circle(8,8,3.3),1.1),op(lines('M8 1.5V4.7','M11.3 8H14.5'),annulus,po.PathOp.INTERSECTION))
        if name in {'battery','battery-full','battery-low','battery-empty','battery-charging'}:
            # Charge is positive ink in every style, including Solid.
            solid=union(outer,d)
        if name in {'user-plus','user-check','user-x'}:
            # A badge floats beside the person; it must not fuse to a shoulder.
            clearance=union(d,stroke(d,1.8))
            duo=[(op(p,clearance,po.PathOp.DIFFERENCE),a) for p,a in duo[:-1]]+[(union(op(outer,clearance,po.PathOp.DIFFERENCE),d),1)]
            mono=union(op(outer,clearance,po.PathOp.DIFFERENCE),d)
            solid=union(op(union(b,outer),clearance,po.PathOp.DIFFERENCE),d)
        if name == 'headphones':
            mono=union(b,stroke(d,1.1))
        if name == 'lungs':
            field=union(b,outer)
            solid=union(op(field,d,po.PathOp.DIFFERENCE),op(d,field,po.PathOp.DIFFERENCE))
        if name == 'hourglass':
            solid=op(union(b,outer),union(rr(5.4,4,5.2,1.4,.5),poly([(6,12),(8,10),(10,12)])),po.PathOp.DIFFERENCE)
        if name == 'printer':
            cuts=union(line((4.5,5.2),(11.5,5.2)),rr(5.05,10.45,5.9,3.1),circle(12,7.3,.55))
            solid=op(union(b,outer),cuts,po.PathOp.DIFFERENCE)
        if name == 'gift':
            # The ribbon joins an exterior bow; it must still cut through the box.
            solid=op(solid,stroke('M8 6V13.6M2.2 9H13.8',1.15),po.PathOp.DIFFERENCE)
        if name == 'construction':
            # Both hazard stripes remain counters, independently of the legs.
            solid=op(union(b,outer,lines('M4 10V14','M12 10V14')),
                     op(lines('M4 5L7 10','M9 5L12 10'),interior,po.PathOp.INTERSECTION),po.PathOp.DIFFERENCE)
        if name == 'sofa':
            solid=op(union(b,outer,d),union(sofa_seam, line((8,3.3),(8,10))),po.PathOp.DIFFERENCE)
        if name == 'users':
            # Separate the rear torso from the foreground person, not a tiny slit.
            solid=op(solid,stroke('M9 11.5V14.7',1.25),po.PathOp.DIFFERENCE)
        if name == 'folder-open':
            solid=stacked_solid(folder_back,folder_flap)
            mono=union(outer,d)
        if name == 'airplay':
            foreground=poly([(8,8),(13,14),(3,14)])
            clearance=union(foreground,stroke(foreground,1.5))
            # The casting triangle sits in front of the display in every
            # style. A narrow aperture keeps the lower bezel from crossing it.
            duo=[(op(p,clearance,po.PathOp.DIFFERENCE),a) for p,a in duo]+[(foreground,1)]
            mono=union(op(outer,clearance,po.PathOp.DIFFERENCE),foreground)
            solid=union(op(union(b,outer),clearance,po.PathOp.DIFFERENCE),foreground)
        if name in {'clipboard', 'clipboard-check'}:
            solid=op(solid,stroke('M5 2.9V4.1Q5 5.1 6 5.1H10Q11 5.1 11 4.1V2.9',1.05),po.PathOp.DIFFERENCE)
        if name in {'notebook', 'contact'}:
            bindings = [4,8,12] if name == 'notebook' else [5,11]
            slots = union(*(line((2.7,y+1.1),(4.45,y+1.1),width=1.05) for y in bindings))
            solid=op(solid,slots,po.PathOp.DIFFERENCE)
        if name == 'archive':
            solid=op(union(b,outer),d,po.PathOp.DIFFERENCE)
        if name == 'agents':
            solid=union(stacked_solid(agent_back,agent_front,agent_face),antenna)
        if name == 'copy':
            solid=stacked_solid(rr(1.5,1.5,9,10,1.7),rr(5,5,9.5,9.5,1.7))
        if name == 'folders':
            solid=stacked_solid(transform(FOLDER,0,.8,-1,-2),transform(FOLDER,0,.8,1,1.5))
        if name == 'terminal-stack':
            solid=stacked_solid(transform(WINDOW,0,.8,-1,-1.5),transform(WINDOW,0,.8,1,1.5),lines('M6 8l2 2-2 2','M10 12H12'))
        if name == 'multiplexer':
            solid=stacked_solid(rr(1.5,1.5,9.5,9.5,2),rr(5,5,9.5,9.5,2),lines('M10 5V14.5','M5 10H14.5'))
        if name == 'swatch':
            rear=op(SWATCH,union(SWATCH_DIAGONAL,stroke(SWATCH_DIAGONAL,1.8)),po.PathOp.DIFFERENCE)
            fan=union(rear,SWATCH_DIAGONAL)
            front=rr(2,9.5,12,4.5,1)
            solid=union(op(fan,union(front,stroke(front,1.8)),po.PathOp.DIFFERENCE),op(front,circle(4.25,11.75,.65),po.PathOp.DIFFERENCE))
        if name == 'store':
            scallops=stroke('M1.5 6Q1.5 8 3.7 8Q5.8 8 5.8 6Q5.8 8 8 8Q10.2 8 10.2 6Q10.2 8 12.3 8Q14.5 8 14.5 6')
            reveal=op(scallops,rr(2.05,5.4,11.9,3.6,0),po.PathOp.INTERSECTION)
            solid=op(union(b,outer),union(reveal,rr(6.3,10,3.4,5.5)),po.PathOp.DIFFERENCE)
        if name in {'camera-off','microphone-off','bell-off','cloud-off','bluetooth-off','wifi-off','eye-off','ear-off'}:
            slash=line((2,2),(14,14))
            clearance=line((2,2),(14,14),width=3.2 if name in {'bluetooth-off','camera-off','eye-off'} else 2.65)
            duo=[(op(p,clearance,po.PathOp.DIFFERENCE),a) for p,a in duo]+[(slash,1)]
            mono=union(op(mono,clearance,po.PathOp.DIFFERENCE),slash)
            solid=union(op(solid,clearance,po.PathOp.DIFFERENCE),slash)
        overrides=STYLE_OVERRIDES.get(name,{})
        duo=overrides.get('duotone',duo)
        solid=overrides.get('solid',solid)
        mono=overrides.get('stroke',mono)
        two_tones=any(p and 0<alpha<1 for p,alpha in duo)
        write(Path('icons')/(name+'.svg'),svg(duo))
        for style,layers in {
            'solid':[(solid,1)],
            'stroke':[(mono,1)],
        }.items():
            write(Path('icons/styles')/style/(name+'.svg'),svg(layers))
        catalog.append(dict(name=name,category=category,tags=tags.split(),origin='original',styles=['duotone','solid','stroke'],defaultTone='duotone' if two_tones else 'monochrome'))
    brands=json.loads((ROOT/'scripts/icons/brands.json').read_text())
    actual={p.stem for p in (ROOT/'icons').glob('*.svg')}
    unknown=actual-set(DRAWINGS)-set(brands)
    if unknown:failed.append('Uncategorized artwork: '+', '.join(sorted(unknown)))
    for name in brands:
        file=ROOT/'icons'/(name+'.svg')
        if name in BRAND_REFINEMENTS:
            frame=path('M8 0C1.42 0 0 1.42 0 8S1.42 16 8 16S16 14.58 16 8S14.58 0 8 0Z')
            write(file.relative_to(ROOT),svg([(frame,.2),(BRAND_REFINEMENTS[name],1)]))
        r=ET.parse(file).getroot()
        if not any(0<float(n.get('opacity','1'))<1 for n in r.iter()):
            failed.append('Unreviewed single-tone icon: '+file.stem)
        catalog.append(dict(name=file.stem,category='Brands',tags=[],origin='legacy',styles=['duotone'],defaultTone='duotone'))
    by_name = {item['name']: item for item in catalog}
    hues = json.loads((ROOT/'scripts/icons/default-hues.json').read_text())
    for hue, names in hues.items():
        for name in names:
            item = by_name[name]
            if 'defaultColor' in item:
                raise ValueError(f'Duplicate default color for {name}')
            item['defaultColor'] = hue
    write(Path('catalog.json'),json.dumps(sorted(catalog,key=lambda i:i['name']),indent=2)+'\n')
    if failed:sys.exit('\n'.join(failed))
    print(f'{len(DRAWINGS)} original drawings; {len(catalog)} total icons')
def register_full_catalog():
    """Register original recipes for the pinned full-coverage expansion.

    Kept explicit so isolated native-review snapshots can register one group.
    """
    from full import design, product, technology, world
    import sf_home, sf_media, sf_accessibility
    for module in (design, product, technology, world, sf_home, sf_media, sf_accessibility):
        module.register(globals())

if __name__=='__main__':
    register_full_catalog()
    main()
