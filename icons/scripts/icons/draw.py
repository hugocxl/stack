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
            # The area identity needs a second operation, which can fail on
            # the same tangent contours; retry it on the coarser grids too.
            if kind == po.PathOp.INTERSECTION:
                other=po.op(aa,bb,po.PathOp.UNION).area
                expected=aa.area+bb.area-other
            else:
                intersection=po.op(aa,bb,po.PathOp.INTERSECTION).area
                expected={po.PathOp.UNION:aa.area+bb.area-intersection,
                          po.PathOp.DIFFERENCE:aa.area-intersection,
                          po.PathOp.REVERSE_DIFFERENCE:bb.area-intersection,
                          po.PathOp.XOR:aa.area+bb.area-2*intersection}[kind]
        except po.PathOpsError:
            if precision == 3:
                raise
            continue
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
STROKE = 1.04
RADIUS = 1.2
def weight(width):
    return STROKE if .75 <= width <= 1.55 else width

def stroke(d, width=STROKE, exact=False):
    # exact=True keeps the given width for measurement and clearance tools;
    # visible artwork always goes through the single family weight.
    width = width if exact else weight(width)
    p = path(d) if isinstance(d, str) else po.Path(d)
    # Stroke at authoring resolution so Skia's curve tolerance cannot
    # introduce visibly different widths at different orientations.
    resolution=32
    p=p.transform(resolution,0,0,resolution,0,0)
    p.stroke(width*resolution, po.LineCap.ROUND_CAP, po.LineJoin.ROUND_JOIN, 4)
    p.convertConicsToQuads(.02)
    p=p.transform(1/resolution,0,0,1/resolution,0,0)
    return po.simplify(p)

def rr(x=2,y=2,w=12,h=12,r=RADIUS,exact=False):
    # A positive radius means the family corner; 0 keeps a sharp cutter. A
    # radius meant as a full pill (capsule, toggle, microphone) stays a pill.
    # exact=True keeps a deliberate SF container radius (app tile ~2.6,
    # window ~1.9) or a small inner radius for compact details.
    pill=min(w,h)/2
    if exact: r=min(r,pill)
    else: r=pill if r>=.9*pill else min(RADIUS if r>0 else 0,pill)
    k=r*.5522847498
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
    """Shared SF seal (checkmark.seal): an eight-point star with rounded
    points and shallow valleys, about 14.4 u across with its outline."""
    points = []
    for i in range(16):
        angle = -math.pi/2 + i*math.pi/8
        radius = 6.75 if i % 2 == 0 else 5.75
        points.append((8 + radius*math.cos(angle), 8 + radius*math.sin(angle)))
    star = path('M' + 'L'.join(f'{x:.4f} {y:.4f}' for x, y in points) + 'Z')
    # SF rounds the points generously; the valleys stay crisp.
    return soften(star, .75)


# SF-style badges: a filled disc with the mark knocked out, set into the base
# symbol behind a clearance gap. Applied to every style after the base is
# composed (see main), so the base drawing stays a plain shape() or glyph().
# Search terms kept from earlier releases when a redraw rewrote an icon's tags.
KEPT_TAGS = {"archive-arrow-down":["arrow","down"],"archive-arrow-up":["arrow","up"],"building-complex-plus":["building"],"cctv-off":["cctv"],"mail-exclamation-point":["exclamation-point"],"mail-question-mark":["question-mark"],"screen-share-off":["screen-share"],"touchpad-off":["touchpad"],"user-exclamation-point":["exclamation-point"],"user-round-arrow-left":["arrow-left"],"user-round-exclamation-point":["exclamation-point"],"user-round-group":["round"]}
BADGES = {}
BADGE_GAP = .9
def badge_mark(kind, cx, cy, r):
    s = r/3.25
    return {
        'plus': lines(f'M{cx-1.7*s} {cy}H{cx+1.7*s}', f'M{cx} {cy-1.7*s}V{cy+1.7*s}'),
        'minus': line((cx-1.7*s,cy),(cx+1.7*s,cy)),
        'check': line((cx-1.55*s,cy+.1*s),(cx-.45*s,cy+1.2*s),(cx+1.6*s,cy-1.3*s)),
        'x': lines(f'M{cx-1.25*s} {cy-1.25*s}L{cx+1.25*s} {cy+1.25*s}', f'M{cx+1.25*s} {cy-1.25*s}L{cx-1.25*s} {cy+1.25*s}'),
        'alert': union(line((cx,cy-1.75*s),(cx,cy+.35*s)), circle(cx,cy+1.55*s,.62)),
        'dot': po.Path(),
        'gear': union(stroke(circle(cx,cy,1.05*s)),*(line((cx+1.55*s*math.cos(k*math.pi/3),cy+1.55*s*math.sin(k*math.pi/3)),(cx+1.95*s*math.cos(k*math.pi/3),cy+1.95*s*math.sin(k*math.pi/3))) for k in range(6))),
        'search': union(stroke(circle(cx-.4*s,cy-.4*s,1.15*s)),line((cx+.5*s,cy+.5*s),(cx+1.55*s,cy+1.55*s))),
        'play': poly([(cx-1.1*s,cy-1.55*s),(cx+1.65*s,cy),(cx-1.1*s,cy+1.55*s)]),
        'expand': union(line((cx-1.45*s,cy+1.45*s),(cx+1.45*s,cy-1.45*s)),line((cx-.1*s,cy-1.45*s),(cx+1.45*s,cy-1.45*s),(cx+1.45*s,cy+.1*s))),
        'ellipsis': dots((cx-1.45*s,cy),(cx,cy),(cx+1.45*s,cy),r=.55*s),
        'arrow-up': union(line((cx,cy+1.75*s),(cx,cy-1.6*s)), line((cx-1.5*s,cy-.15*s),(cx,cy-1.65*s),(cx+1.5*s,cy-.15*s))),
        'arrow-down': union(line((cx,cy-1.75*s),(cx,cy+1.6*s)), line((cx-1.5*s,cy+.15*s),(cx,cy+1.65*s),(cx+1.5*s,cy+.15*s))),
        'clock': stroke(f'M{cx} {cy-1.75*s}V{cy}H{cx+1.4*s}'),
    }[kind]

def badge(name, kind='plus', cx=11.85, cy=11.85, r=3.25, gap=BADGE_GAP):
    """Attach an SF-style badge to an already registered drawing."""
    assert name in DRAWINGS, name
    disc = op(circle(cx,cy,r), badge_mark(kind,cx,cy,r), po.PathOp.DIFFERENCE)
    BADGES[name] = (disc, circle(cx,cy,r+gap))

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
# SF checkmark: a short, steep left arm meets a long right arm (about 1:2).
def check(x=8,y=8,s=1): return line((x-2.75*s,y+.25*s),(x-.8*s,y+2.6*s),(x+2.75*s,y-2.6*s))
def plus(x=8,y=8,s=1): return lines(f'M{x-2*s} {y}h{4*s}',f'M{x} {y-2*s}v{4*s}')
def cross(x=8,y=8,s=1): return lines(f'M{x-2*s} {y-2*s}l{4*s} {4*s}',f'M{x+2*s} {y-2*s}l{-4*s} {4*s}')
# SF arrow proportions: chevron head with 45-degree arms of 0.4 of the length.
def arrow(angle=0, size=1, dx=0, dy=0, width=STROKE):
    shaft = line((8-5*size, 8), (8+5*size, 8), width=width)
    head = line((8+size, 8-4*size), (8+5*size, 8), (8+size, 8+4*size), width=width)
    return transform(union(shaft, head), angle, dx=dx, dy=dy)

def ellipse(cx,cy,rx,ry): return circle(0,0,1).transform(rx,0,0,ry,cx,cy)
def fillet(p,r=.5):
    # Morphological closing: round the concave joins between united parts.
    grown=union(p,stroke(p,2*r,exact=True))
    return op(grown,stroke(grown,2*r,exact=True),po.PathOp.DIFFERENCE)
def tri_head(x,y,angle=0,length=2.75,half=1.95):
    """Filled SF arrowhead (shuffle, repeat) with its apex at (x,y)."""
    a=math.radians(angle); c,s=math.cos(a),math.sin(a)
    def at(u,v): return (x+u*c-v*s, y+u*s+v*c)
    return poly([at(0,0),at(-length,-half),at(-length,half)])
def opened(name, body, rim, mark, tags='', solid=None):
    """A container whose outline opens where a mark passes through it.

    The surface keeps the tone inside the container; Solid fills the body and
    reverses the mark where it crosses the filled area (SF `.fill`)."""
    shape(name, body, mark, tags)
    b = DRAWINGS[name][0]
    ink = union(rim, mark)
    fill = union(b, stroke(b))
    if solid is None:
        solid = union(op(fill, mark, po.PathOp.DIFFERENCE), op(mark, fill, po.PathOp.DIFFERENCE))
    STYLE_OVERRIDES[name] = {'duotone':[(op(b, union(ink, stroke(b, 1.6, exact=True)), po.PathOp.DIFFERENCE),.24),(ink,1)],
                             'stroke':ink,'solid':solid}
def round_rect_path(x0,y0,x1,y1,r,start='right',gap=None):
    """Centerline of a rounded rectangle as an open path, broken by a gap
    (lo, hi) on one side, so the cut ends get the family's round caps."""
    k=r*.5523
    lo,hi=gap
    if start=='right':
        return (f'M{x1} {lo}V{y0+r}C{x1} {y0+r-k} {x1-r+k} {y0} {x1-r} {y0}H{x0+r}'
                f'C{x0+r-k} {y0} {x0} {y0+r-k} {x0} {y0+r}V{y1-r}C{x0} {y1-r+k} {x0+r-k} {y1} {x0+r} {y1}'
                f'H{x1-r}C{x1-r+k} {y1} {x1} {y1-r+k} {x1} {y1-r}V{hi}')
    if start=='left':
        return (f'M{x0} {lo}V{y0+r}C{x0} {y0+r-k} {x0+r-k} {y0} {x0+r} {y0}H{x1-r}'
                f'C{x1-r+k} {y0} {x1} {y0+r-k} {x1} {y0+r}V{y1-r}C{x1} {y1-r+k} {x1-r+k} {y1} {x1-r} {y1}'
                f'H{x0+r}C{x0+r-k} {y1} {x0} {y1-r+k} {x0} {y1-r}V{hi}')
    # top: gap (lo, hi) is an x interval on the top edge
    return (f'M{lo} {y0}H{x0+r}C{x0+r-k} {y0} {x0} {y0+r-k} {x0} {y0+r}V{y1-r}'
            f'C{x0} {y1-r+k} {x0+r-k} {y1} {x0+r} {y1}H{x1-r}C{x1-r+k} {y1} {x1} {y1-r+k} {x1} {y1-r}'
            f'V{y0+r}C{x1} {y0+r-k} {x1-r+k} {y0} {x1-r} {y0}H{hi}')

def stacked(name, back, front, detail=None, tags=''):
    """Two overlapping surfaces: the rear outline stops short of the front one
    behind an SF clearance gap in every style."""
    clearance = union(front, stroke(front, STROKE+2*.85, exact=True))
    rear_rim = op(stroke(back), clearance, po.PathOp.DIFFERENCE)
    front_rim = stroke(front)
    ink = union(rear_rim, front_rim, detail or po.Path())
    rear_surface = op(back, union(clearance, stroke(back, 1.6, exact=True)), po.PathOp.DIFFERENCE)
    front_surface = op(front, union(stroke(front, 1.6, exact=True), detail or po.Path()), po.PathOp.DIFFERENCE)
    shape(name, union(back, front), detail, tags)
    STYLE_OVERRIDES[name] = {'duotone':[(union(rear_surface, front_surface),.24),(ink,1)],
                             'stroke':ink, 'solid':stacked_solid(back, front, detail)}
def stacked_solid(back,front,detail=None):
    rear=union(back,stroke(back,1.25));fore=union(front,stroke(front,1.25))
    clearance=union(fore,stroke(fore,1.5))
    if detail:
        inset=op(fore,stroke(fore,1.8),po.PathOp.DIFFERENCE)
        fore=op(fore,op(detail,inset,po.PathOp.INTERSECTION),po.PathOp.DIFFERENCE)
    return union(op(rear,clearance,po.PathOp.DIFFERENCE),fore)
# Shared SF document: 10.8 x 13.7 with outline, a half-width folded corner
# drawn as an inner L, and softly rounded joins on the diagonal.
FILE=path('M4.37 1.67H7.95Q8.45 1.67 8.8 2.02L12.53 5.75Q12.88 6.1 12.88 6.6V13.08'
          'C12.88 13.77 12.32 14.33 11.63 14.33H4.37C3.68 14.33 3.12 13.77 3.12 13.08V2.92'
          'C3.12 2.23 3.68 1.67 4.37 1.67Z')
FOLD=stroke('M7.95 1.7V5.4Q7.95 6.6 9.15 6.6H12.85')

CATEGORY='Navigation'
ARROW_LENGTH, ARROW_HEAD = 10.9, 4.3
for name,angle in [('right',0),('down',90),('left',180),('up',270)]:
    h=ARROW_LENGTH/2
    glyph('arrow-'+name,transform(line((8-h,8),(8+h,8)),angle),
          transform(line((8+h-ARROW_HEAD,8-ARROW_HEAD),(8+h,8),(8+h-ARROW_HEAD,8+ARROW_HEAD)),angle))
# Diagonal arrows reach further (8.3 u square) with axis-aligned head arms.
for name,angle in [('up-right',0),('down-right',90),('down-left',180),('up-left',270)]:
    glyph('arrow-'+name,transform(line((3.85,12.15),(12.15,3.85)),angle),
          transform(line((6.15,3.85),(12.15,3.85),(12.15,9.85)),angle))
CHEVRON=[(5.42,2.985),(10.58,8),(5.42,13.015)]  # SF chevron.right, 6.2 x 11.1
for name,angle in [('right',0),('down',90),('left',180),('up',270)]:
    glyph('chevron-'+name,transform(line(*CHEVRON[:2]),angle),transform(line(*CHEVRON[1:]),angle))
    pair=[transform(path('M'+'L'.join(f'{x+dx} {y}' for x,y in CHEVRON)),angle) for dx in (-2.9,2.9)]
    glyph('chevrons-'+name,stroke(pair[0]),stroke(pair[1]))
# Diagonal chevrons are an axis-aligned corner, set back from the corner it
# points to so its mass stays on the optical center.
for name,angle in [('up-right',0),('down-right',90),('down-left',180),('up-left',270)]:
    glyph('chevron-'+name,transform(line((4.04,5.56),(10.44,5.56)),angle),transform(line((10.44,5.56),(10.44,11.96)),angle))
for name,angle in [('left',180),('right',0),('up',270),('down',90)]:
    shape('circle-arrow-'+name,circle(),arrow(angle,.55))
glyph('chevrons-up-down',line((4.26,6.1),(8,2.36),(11.74,6.1)),line((4.26,9.9),(8,13.64),(11.74,9.9)))
inward = line((3.35,4.75),(6.6,8),(3.35,11.25))
glyph('chevrons-in',inward,mirror(inward))
# SF house: eaves overhang the walls, a chimney on the right slope and a
# filled door; the walls carry the surface tone.
house_walls = path('M3.05 7.25L8 2.95L12.95 7.25V12.85C12.95 13.4 12.5 13.85 11.95 13.85H4.05C3.5 13.85 3.05 13.4 3.05 12.85Z')
house_roof = union(line((1.4,8.7),(8,2.95),(14.6,8.7)),line((11.6,5.4),(11.6,3.05)))
house_door = rr(6.6,9.5,2.8,4.35,.55,exact=True)
shape('home',house_walls,union(house_roof,house_door),'house dashboard start')
needle = op(poly([(11.45,4.55),(9.25,9.25),(4.55,11.45),(6.75,6.75)]),circle(8,8,.7),po.PathOp.DIFFERENCE)
shape('compass',circle(),needle)
# SF arrow.up.forward.app: an app-radius square with the arrow inside.
shape('external-link',rr(2.1,2.1,11.8,11.8,2.4,exact=True),
      union(line((5.45,10.55),(10.55,5.45)),line((6.6,5.45),(10.55,5.45),(10.55,9.4))))
# rectangle.portrait.and.arrow.right: a portrait door opens where the arrow passes.
door_out = rr(1.75,1.65,8.7,12.7,2.2,exact=True)
exit_arrow = union(line((6.15,8),(14.3,8)),line((11.5,5.2),(14.3,8),(11.5,10.8)))
opened('log-out',door_out,stroke(round_rect_path(1.75,1.65,10.45,14.35,2.2,'right',(5.2,10.8))),exit_arrow)
door_in = rr(5.55,1.65,8.7,12.7,2.2,exact=True)
entry_arrow = union(line((1.7,8),(9.85,8)),line((7.05,5.2),(9.85,8),(7.05,10.8)))
opened('log-in',door_in,stroke(round_rect_path(5.55,1.65,14.25,14.35,2.2,'left',(5.2,10.8))),entry_arrow)
for name,reflect in [('undo',False),('redo',True)]:
    f=mirror if reflect else lambda p:p
    glyph(name,f(stroke('M2.55 6.35H9.95A3.475 3.475 0 0 1 9.95 13.3H8.15')),f(line((6.35,2.55),(2.55,6.35),(6.35,10.15))))
# SF arrow.clockwise: three quarters of a circle, its open end at the top
# running into a chevron head that points along the turn.
for name,reflect in [('refresh',False),('reset',True),('rotate-left',True),('rotate-right',False)]:
    f=mirror if reflect else lambda p:p
    glyph(name,f(stroke('M13 8.75A5 5 0 1 1 8 4.05H9.75')),f(line((7,1.15),(9.9,4.05),(7,6.95))))
glyph('swap-horizontal',union(line((2.4,4.6),(13.6,4.6)),line((5.6,1.4),(2.4,4.6),(5.6,7.8))),
      union(line((13.6,11.4),(2.4,11.4)),line((10.4,8.2),(13.6,11.4),(10.4,14.6))))
glyph('swap-vertical',union(line((4.6,13.6),(4.6,2.4)),line((1.4,5.6),(4.6,2.4),(7.8,5.6))),
      union(line((11.4,2.4),(11.4,13.6)),line((8.2,10.4),(11.4,13.6),(14.6,10.4))))
# SF shuffle and repeat use filled arrowheads.
glyph('shuffle',stroke('M1.55 4.3H3.6Q4.75 4.3 5.5 5.25L10.25 10.75Q11 11.7 12.15 11.7H12.6'
                       'M1.55 11.7H3.6Q4.75 11.7 5.5 10.75L10.25 5.25Q11 4.3 12.15 4.3H12.6'),
      union(tri_head(14.55,4.3),tri_head(14.55,11.7)))
glyph('repeat',stroke('M2.7 9.75V7.2Q2.7 4.55 5.35 4.55H11.9M13.3 6.25V8.8Q13.3 11.45 10.65 11.45H4.1'),
      union(tri_head(14.4,4.55),tri_head(1.6,11.45,180)))

CATEGORY='Actions and status'
glyph('plus',line((8,3.22),(8,12.78)),line((3.22,8),(12.78,8)))
glyph('minus',line((3.22,8),(8,8)),line((8,8),(12.78,8)))
glyph('close',line((3.48,3.48),(12.52,12.52)),line((12.52,3.48),(3.48,12.52)))
glyph('check',line((3,8.4),(6.6,12.95)),line((6.6,12.95),(13,3.05)))
# Two SF checkmarks, the rear one shortened where the front one passes.
glyph('check-check',line((1.35,8.45),(3.9,11.5),(8.75,4.2)),line((6.2,10.3),(7.15,11.5),(12.6,4.2),(12.6,4.2)))
info_mark=union(circle(8,4.85,.78),stroke('M6.75 7.15H8.05V11.15M6.55 11.15H9.45'))
help_mark=union(stroke('M5.95 6.35Q6.05 4.35 8.05 4.35Q10.1 4.35 10.1 6.15Q10.1 7.25 8.95 7.85Q8 8.35 8 9.35'),circle(8,11.45,.72))
alert_mark=union(line((8,4.45),(8,8.95)),circle(8,11.3,.75))
for name,detail in [('check',check(8,8.05,.92)),('x',cross(8,8,.9)),('plus',plus(s=1.15)),('minus',line((5.7,8),(10.3,8))),('info',info_mark),('help',help_mark),('alert',alert_mark),('ellipsis',dots((5.15,8),(8,8),(10.85,8),r=.8))]:
    shape('circle-'+name,circle(),detail)
for old,new in [('info','circle-info'),('info-fill','circle-info'),('exclamation-circle-fill','circle-alert'),('ellipsis-circle','circle-ellipsis'),('minus-circle','circle-minus'),('circle-check-fill','circle-check'),('circle-x-fill','circle-x')]:
    b,d,o,c,t = DRAWINGS[new]; add(old,b,d,o,t)
# SF exclamationmark.triangle: wide, low, generously rounded corners.
warning = path('M6.85 2.85Q8 .95 9.15 2.85L14.35 11.6Q15.45 13.5 13.25 13.5H2.75Q.55 13.5 1.65 11.6Z')
warning_mark = union(line((8,5.9),(8,9.05)),circle(8,11.15,.72))
for name in ['triangle-alert','triangle-alert-fill']: shape(name,warning,warning_mark)
octagon = soften(path('M'+'L'.join(f'{8+6.45*math.cos(math.radians(22.5+45*i))} {8+6.45*math.sin(math.radians(22.5+45*i))}' for i in range(8))+'Z'),.75)
shape('octagon-alert',octagon,union(line((8,4.4),(8,8.85)),circle(8,11.2,.75)))
shape('ban',circle(),line((4.15,4.15),(11.85,11.85)))
SQUARE=rr(2.62,2.62,10.76,10.76,1.9,exact=True)  # SF square: 11.8 with outline
for name in ['checkbox','checkbox-fill']: shape(name,SQUARE,check(8,8.05,.95))
shape('square',SQUARE)
shape('circle',circle())
glyph('dot',circle(8,8,4.35),po.Path())
glyph('ellipsis',dots((3.27,8),(12.73,8),r=1.2),circle(8,8,1.2))
glyph('ellipsis-vertical',dots((8,3.27),(8,12.73),r=1.2),circle(8,8,1.2))
LENS=(6.75,6.75,4.65)
shape('search',circle(*LENS),line((10.35,10.35),(13.55,13.55)))
STYLE_OVERRIDES['search'] = {'solid': union(ring(LENS[0],LENS[1],LENS[2]+.52),line((10.35,10.35),(13.55,13.55)))}
for name,detail in [('zoom-in',plus(6.75,6.75,.85)),('zoom-out',line((5.05,6.75),(8.45,6.75)))]: shape(name,circle(*LENS),union(line((10.35,10.35),(13.55,13.55)),detail))
# SF line.3.horizontal.decrease: the system's filter glyph.
glyph('filter',lines('M2.02 4.72H13.98','M4.1 8H11.9'),line((6.15,11.28),(9.85,11.28)),'funnel refine')
for name,top,tip,back in [('sort-ascending',13.4,2.6,5.6),('sort-descending',2.6,13.4,10.4)]:
    glyph(name,lines('M1.8 4H7','M1.8 8H6','M1.8 12H5'),
          union(line((11.6,top),(11.6,tip)),line((8.6,back),(11.6,tip),(14.6,back))))
# SF slider.horizontal.3: three rails with capsule knobs interrupting them.
knobs=[(10.1,4),(5.9,8),(9.1,12)]
knob_shapes=[rr(x-1.75,y-.8,3.5,1.6,.8,exact=True) for x,y in knobs]
rails=union(*(op(line((2.05,y),(13.95,y)),k,po.PathOp.DIFFERENCE) for (x,y),k in zip(knobs,knob_shapes)))
glyph('sliders',rails,union(*(stroke(k) for k in knob_shapes)))
for name,x in [('toggle-on',10.95),('toggle-off',5.05)]:
    shape(name,rr(1.75,4.6,12.5,6.8,3.4),circle(x,8,2.25))
# SF square.and.arrow.down: an open-topped box the arrow drops into.
box = rr(2.82,5.0,10.36,9.3,2.2,exact=True)
box_rim = stroke(round_rect_path(2.82,5.0,13.18,14.3,2.2,'top',(5.4,10.6)))
opened('save',box,box_rim,union(line((8,1.2),(8,10.1)),line((5.45,7.55),(8,10.1),(10.55,7.55))))
# SF trash: lid with a handle over a tapered can and three ribs.
can = path('M3.6 3.95H12.4L11.75 12.95C11.7 13.75 11.1 14.35 10.3 14.35H5.7C4.9 14.35 4.3 13.75 4.25 12.95Z')
lid = union(line((2.3,3.95),(13.7,3.95)),stroke('M5.75 3.95V2.75Q5.75 1.5 7 1.5H9Q10.25 1.5 10.25 2.75V3.95'))
shape('trash',can,union(lid,lines('M6.05 6.3L6.25 11.85','M8 6.3V11.85','M9.95 6.3L9.75 11.85')),'delete remove bin')
archive_lid = rr(2.1,2.6,11.8,2.95,.9,exact=True)
shape('archive', union(rr(3.0,5.0,10.0,8.35),archive_lid),
      lines('M2.1 5.55H13.9', 'M6.35 8.35H9.65'))
# SF tray.and.arrow.down/up: a sloped tray whose top opens for the arrow.
tray = path('M4.3 5.0H11.7L14.35 9.5V12.6C14.35 13.6 13.6 14.35 12.6 14.35H3.4C2.4 14.35 1.65 13.6 1.65 12.6V9.5Z')
tray_rim = stroke('M5.75 5.0H5.1Q4.45 5.0 4.1 5.55L1.95 9.0Q1.65 9.45 1.65 10.0V12.6C1.65 13.6 2.4 14.35 3.4 14.35H12.6'
                  'C13.6 14.35 14.35 13.6 14.35 12.6V10.0Q14.35 9.45 14.05 9.0L11.9 5.55Q11.55 5.0 10.9 5.0H10.25')
tray_shelf = stroke('M1.9 9.5H5.25Q5.8 9.5 5.95 10.05Q6.4 11.55 8 11.55Q9.6 11.55 10.05 10.05Q10.2 9.5 10.75 9.5H14.1')
tray_lower = path('M1.65 9.5H5.25Q5.8 9.5 5.95 10.05Q6.4 11.55 8 11.55Q9.6 11.55 10.05 10.05Q10.2 9.5 10.75 9.5H14.35V12.6'
                  'C14.35 13.6 13.6 14.35 12.6 14.35H3.4C2.4 14.35 1.65 13.6 1.65 12.6Z')
for name,mark in [('download',union(line((8,1.2),(8,8.6)),line((5.6,6.2),(8,8.6),(10.4,6.2)))),
                  ('upload',union(line((8,8.8),(8,1.3)),line((5.6,3.7),(8,1.3),(10.4,3.7))))]:
    lower=union(tray_lower,stroke(tray_lower))
    opened(name,tray,union(tray_rim,tray_shelf),mark,
           solid=union(tray_rim,lower,op(mark,lower,po.PathOp.DIFFERENCE)))
shape('download-circle-fill',circle(),arrow(90,.55))
link_loop = stroke('M7.1 11.15L5.8 12.45A2.65 2.65 0 0 1 2.05 8.7L4.8 5.95Q6.55 4.2 8.05 5.6')
glyph('link', union(link_loop,transform(link_loop,180)),line((5.75,10.25),(10.25,5.75)))
link_end = stroke('M4 7.7L2.8 8.9A3.05 3.05 0 0 0 7.1 13.2L8.3 12')
glyph('unlink', union(link_end, transform(link_end, 180)),
      lines('M3.4 3.4L5.2 5.2', 'M10.8 10.8L12.6 12.6'))
# SF square.on.square: two app-radius squares, the rear one up and left.
copy_back, copy_front = rr(1.17,1.17,10.26,10.26,1.9,exact=True), rr(4.57,4.57,10.26,10.26,1.9,exact=True)
copy_fold = None
stacked('copy',copy_back,copy_front)
# SF clipboard: a tall board with a filled clip astride its top edge.
board = rr(3.1,2.45,9.8,12.15,1.9,exact=True)
clip = rr(5.75,1.15,4.5,2.6,1.0,exact=True)
shape('clipboard',board,clip)
shape('clipboard-check',board,union(clip,check(8,9.1,.82)))
for name in ['clipboard','clipboard-check']:
    b,d,*_=DRAWINGS[name]
    field=union(b,stroke(b))
    marks=op(d,clip,po.PathOp.DIFFERENCE)
    STYLE_OVERRIDES[name]={'solid':union(op(field,union(clip,stroke(clip,1.8,exact=True),marks),po.PathOp.DIFFERENCE),clip)}

CATEGORY='Files and folders'
# SF folder: 14.6 x 11.7 with outline, a short tab stepping down on a soft
# S-curve, generous corners, and a pocket line held clear of both walls.
FOLDER=path('M1.23 4.2C1.23 3.37 1.9 2.7 2.73 2.7H4.85C5.35 2.7 5.7 2.85 6.05 3.15L6.35 3.4'
            'C6.7 3.7 7.0 3.85 7.5 3.85H13.27C14.1 3.85 14.77 4.52 14.77 5.35V11.77'
            'C14.77 12.6 14.1 13.27 13.27 13.27H2.73C1.9 13.27 1.23 12.6 1.23 11.77Z')
FOLDER_POCKET=line((3.1,5.85),(12.9,5.85))
def zipper(x, top, bottom):
    # SF zipper: staggered teeth run down from the edge into a filled pull
    # with a small slot.
    teeth=[]
    y=top+.95; i=0
    while y < bottom-3.55:
        teeth.append(line((x-.95+.9*(i%2),y),(x-.05+.9*(i%2),y))); y+=1.55; i+=1
    pull=op(rr(x-1.15,bottom-3.0,2.3,3.0,.8,exact=True),rr(x-.32,bottom-1.55,.64,.95,.32,exact=True),po.PathOp.DIFFERENCE)
    return union(*teeth,pull)
def heart(cx, cy, w):
    s=w/4.6
    return path('M0 2.05C-.35 1.75-2.3 .35-2.3-1.0C-2.3-2.85.05-3.0 0-1.4'
                'C-.05-3.0 2.3-2.85 2.3-1.0C2.3 .35 .35 1.75 0 2.05Z').transform(s,0,0,s,cx,cy+.3*s)
def lock_mark(cx, top, w=3.6, h=2.55, r=1.0, leg=.55):
    body=rr(cx-w/2,top,w,h,.6,exact=True)
    return union(body,stroke(f'M{cx-r} {top}V{top-leg}A{r} {r} 0 0 1 {cx+r} {top-leg}V{top}'))
def magnifier(cx, cy, r, reach):
    # r is the lens centerline radius; the handle continues on the diagonal.
    e=r*.7071
    return union(stroke(circle(cx,cy,r)),line((cx+e+.3,cy+e+.3),(cx+reach,cy+reach)))
def doc(dx=0, dy=0): return FILE.transform(1,0,0,1,dx,dy), FOLD.transform(1,0,0,1,dx,dy)
DOC_TEXT=lines('M5.85 9.2H10.15','M5.85 11.45H10.15')
doc_image=union(circle(6.15,8.75,.85),path('M4.65 12.85L7.35 9.95L9.0 11.6L9.85 10.75L11.35 12.85Z'))
doc_audio=union(stroke('M9.35 12.25V8.05Q10.6 8.3 11.05 9.45'),
                circle(0,0,1).transform(1.3,-.45,.25,.95,8.1,12.3))
doc_table=union(stroke(rr(5.05,8.2,5.9,4.6,.7,exact=True)),lines('M5.05 10.5H10.95','M8 8.2V12.8'))
for name,detail in [('file',po.Path()),('file-text',DOC_TEXT),
                    ('file-code',stroke('M6.6 8.55L4.95 10.3L6.6 12.05M9.4 8.55L11.05 10.3L9.4 12.05')),
                    ('file-image',doc_image),('file-table',doc_table),
                    ('file-symlink',union(stroke('M5.55 12.75V11.45Q5.55 9.65 7.35 9.65H10.4'),line((8.95,8.2),(10.4,9.65),(8.95,11.1)))),
                    ('file-lock',lock_mark(8,10.35)),
                    ('file-audio',doc_audio),
                    ('file-video',poly([(6.65,8.25),(10.4,10.4),(6.65,12.55)])),
                    ('file-heart',heart(8,10.35,4.6)),
                    ('file-zip',zipper(6.1,1.67,12.6)),
                    ('file-download',arrow(90,.44,dx=-.3,dy=2.55)),
                    ('file-upload',arrow(270,.44,dx=-.3,dy=2.55))]:
    shape(name,FILE,union(FOLD,detail))
# SF doc badges sit at the lower left; the document steps right to make room.
badged_file, badged_fold = doc(1.3,-.45)
for name,kind in [('file-plus','plus'),('file-minus','minus'),('file-check','check'),('file-x','x')]:
    shape(name,badged_file,badged_fold); badge(name,kind,4.35,11.95)
# doc.text.magnifyingglass: the lens overlaps the lower right behind a gap.
search_file, search_fold = doc(-1.05,-.3)
shape('file-search',search_file,union(search_fold,DOC_TEXT.transform(1,0,0,1,-1.55,-.3)))
lens_mark=magnifier(10.85,10.9,2.3,3.3)
BADGES['file-search']=(lens_mark,union(lens_mark,stroke(lens_mark,2*BADGE_GAP,exact=True),circle(10.85,10.9,2.3)))
# SF folder badges sit at the top right; the folder steps down and left.
def folder_at(scale=1, dx=0, dy=0):
    body=transform(FOLDER,scale=scale,dx=dx,dy=dy)
    a,b=[(8+(x-8)*scale+dx,8+(y-8)*scale+dy) for x,y in ((3.1,5.85),(12.9,5.85))]
    return body,line(a,b)
badged_folder, badged_pocket = folder_at(.92,-.6,.5)
for name,kind in [('folder-plus','plus'),('folder-minus','minus'),('folder-check','check'),('folder-x','x')]:
    shape(name,badged_folder,badged_pocket); badge(name,kind,12.4,4.05,2.95)
for name,detail in [('folder',po.Path()),('folder-heart',heart(8,9.6,4.6)),
                    ('folder-lock',lock_mark(8,9.35)),
                    ('folder-search',magnifier(7.55,9.15,1.33,2.45)),
                    ('folder-code',stroke('M6.35 7.95L4.7 9.6L6.35 11.25M9.65 7.95L11.3 9.6L9.65 11.25')),
                    ('folder-zip',zipper(8,5.85,12.0)),
                    ('folder-download',arrow(90,.42,dy=1.6)),
                    ('folder-upload',arrow(270,.42,dy=1.6))]:
    shape(name,FOLDER,union(FOLDER_POCKET,detail))
# An open folder: the back panel and tab stay, the front flap tips forward.
folder_back = path('M1.23 4.2C1.23 3.37 1.9 2.7 2.73 2.7H4.85C5.35 2.7 5.7 2.85 6.05 3.15L6.35 3.4'
                   'C6.7 3.7 7.0 3.85 7.5 3.85H11.6C12.43 3.85 13.1 4.52 13.1 5.35V6.6H1.23Z')
folder_flap = soften(path('M3.55 6.6H14.75L12.95 13.27H1.23Z'),.6)
shape('folder-open', union(folder_back, folder_flap,path('M1.23 6.6H3.6L1.23 13.27Z')), stroke(folder_flap, 1.25))
FOLDERS_BACK, FOLDERS_FRONT = transform(FOLDER,0,.8,-1.2,-1.5), transform(FOLDER,0,.8,1.1,1.6)
shape('folders',union(FOLDERS_BACK,FOLDERS_FRONT),stroke(FOLDERS_FRONT,1.25))
# Document formats share the SF square container (11.8 u) with a centered mark.
FORMAT=rr(1.22,2.62,13.56,10.76,1.9,exact=True)
shape('pdf', FORMAT,
      stroke('M3.75 10.35V5.65H4.65C6.4 5.65 6.4 8.3 4.65 8.3H3.75'
             'M7.2 5.65V10.35H7.75C10.0 10.35 10.0 5.65 7.75 5.65Z'
             'M10.95 10.35V5.65H12.35M10.95 7.95H12.1'))
# tablecells: a header row and three columns inside the rectangle.
for name,detail in [('spreadsheet',stroke('M1.22 6.2H14.78M1.22 9.8H14.78M8 2.62V13.38')),
                    ('slides',union(lines('M4.4 6.1H11.6','M4.4 8.9H7.4'),rr(8.75,8.35,2.85,2.4,.5,exact=True))),
                    ('word',stroke('M4.35 5.65L5.85 10.35L8 6.6L10.15 10.35L11.65 5.65')),
                    ('zip',zipper(8,2.62,11.6))]: shape(name,FORMAT,detail)
reader = rr(2.12,2.12,11.76,11.76,1.9,exact=True)
book_spread = path('M4.35 4.55Q6.3 3.95 8 5.05Q9.7 3.95 11.65 4.55V9.1Q9.7 8.65 8 9.75Q6.3 8.65 4.35 9.1Z')
shape('epub',reader,union(stroke(book_spread),stroke('M8 5.05V9.75M2.12 11.45H13.88')))
CATEGORY='Communication'
# SF message: a wide oval with a small tail curling out at the lower left.
bubble_tail = path('M2.2 9.9C2.7 11.25 2.65 12.4 1.95 13.15C1.75 13.4 1.9 13.62 2.2 13.6'
                   'C3.0 13.5 3.85 13.0 4.6 12.16L4.0 10Z')
BUBBLE = fillet(union(ellipse(8,7.62,6.78,5.25),bubble_tail),.6)
# SF text.bubble: rounded rectangle with a short tail dropping at the left.
RECT_BUBBLE = path('M4.4 1.92H11.6C13.0 1.92 14.08 3.0 14.08 4.4V8.95C14.08 10.35 13.0 11.43 11.6 11.43H7.55'
                   'L5.45 13.6C5.1 13.95 4.6 13.75 4.6 13.25V11.43H4.4C3.0 11.43 1.92 10.35 1.92 8.95V4.4'
                   'C1.92 3.0 3.0 1.92 4.4 1.92Z')
for name,detail in [('message',po.Path()),('message-text',lines('M4.9 6.35H11.1','M4.9 8.95H9.1')),
                    ('message-plus',plus(8,7.62,1.15)),('message-check',check(8,7.7,.9)),
                    ('message-heart',heart(8,7.62,4.9)),('message-dots',dots((5.1,7.62),(8,7.62),(10.9,7.62),r=.8))]:
    shape(name,BUBBLE,detail)
for name,detail in [('comment-text',lines('M4.8 5.4H11.2','M4.8 8.0H9.2')),('conversation-add',plus(8,6.68,1.15))]:
    shape(name,RECT_BUBBLE,detail)
# bubble.left.and.bubble.right: the front bubble mirrors the rear one.
convo_back = RECT_BUBBLE.transform(.7,0,0,.7,-.09,.06)
convo_front = mirror(RECT_BUBBLE).transform(.7,0,0,.7,4.9,4.85)
stacked('conversation',convo_back,convo_front)
# SF envelope: full-width, low, with the flap and both lower folds.
ENVELOPE = rr(1.17,3.32,13.66,9.36,1.9,exact=True)
ENVELOPE_FOLDS = stroke('M1.95 4.25L6.95 8.45Q8 9.3 9.05 8.45L14.05 4.25M2.25 11.95L5.85 8.75M13.75 11.95L10.15 8.75')
for name in ['mail','envelope']: shape(name,ENVELOPE,ENVELOPE_FOLDS)
# envelope.badge.plus: the envelope steps up and left for a lower-right badge.
ENVELOPE_FOLD_PATH='M1.95 4.25L6.95 8.45Q8 9.3 9.05 8.45L14.05 4.25M2.25 11.95L5.85 8.75M13.75 11.95L10.15 8.75'
for name,kind in [('mail-plus','plus'),('mail-check','check')]:
    shape(name,transform(ENVELOPE,scale=.9,dx=-.7,dy=-.95),stroke(transform(path(ENVELOPE_FOLD_PATH),scale=.9,dx=-.7,dy=-.95)))
    badge(name,kind,12.15,11.85,3.15)
open_envelope = path('M1.17 6.85Q1.17 6.0 1.9 5.5L7.0 2.0Q8 1.35 9.0 2.0L14.1 5.5Q14.83 6.0 14.83 6.85V12.45'
                     'C14.83 13.5 14.0 14.33 12.95 14.33H3.05C2.0 14.33 1.17 13.5 1.17 12.45Z')
open_folds = stroke('M1.6 6.45L6.95 10.15Q8 10.9 9.05 10.15L14.4 6.45M2.0 13.65L6.2 9.75M14.0 13.65L9.8 9.75')
shape('mail-open',open_envelope,op(open_folds,open_envelope,po.PathOp.INTERSECTION))
# SF paperplane: the plane points up and right with a fold from its notch.
shape('send',path('M13.65 2.35L8.85 13.65L6.85 9.15L2.35 7.15Z'),line((6.85,9.15),(10.15,5.85)))
inbox_tray = transform(tray,dy=-1.68)
inbox_lower = transform(tray_lower,dy=-1.68)
opened('inbox',inbox_tray,union(stroke(inbox_tray),transform(tray_shelf,dy=-1.68)),po.Path(),
       solid=union(stroke(inbox_tray),inbox_lower,stroke(inbox_lower)))
# SF bell: a domed body on a small crown, sides that flare into a flat lip,
# and a half-round clapper below.
BELL = fillet(union(path('M8 2.95C10.6 2.95 11.95 4.85 11.95 7.4V8.6C11.95 9.6 12.45 10.15 13.2 10.85'
                         'C13.75 11.4 13.6 11.95 12.85 11.95H3.15C2.4 11.95 2.25 11.4 2.8 10.85'
                         'C3.55 10.15 4.05 9.6 4.05 8.6V7.4C4.05 4.85 5.4 2.95 8 2.95Z'),
                    circle(8,2.75,1.05)),.45)
BELL_CLAPPER = stroke('M6.1 11.95A1.9 1.9 0 0 0 9.9 11.95')
bell_clapper_solid = path('M5.9 13.0H10.1A2.1 1.45 0 0 1 5.9 13.0Z')
shape('bell',BELL,BELL_CLAPPER)
STYLE_OVERRIDES['bell']={'solid':union(BELL,stroke(BELL),bell_clapper_solid)}
shape('bell-unread',BELL,BELL_CLAPPER); badge('bell-unread','dot',12.05,3.75,2.35)
STYLE_OVERRIDES['bell-unread']=STYLE_OVERRIDES['bell']
shape('bell-off',BELL,union(BELL_CLAPPER,line((2,2),(14,14))))
shape('bell-plus',BELL,BELL_CLAPPER); badge('bell-plus','plus',11.95,4.1,3.15)
STYLE_OVERRIDES['bell-plus']=STYLE_OVERRIDES['bell']
# SF megaphone: mouthpiece, flaring cone, tall rim and a grip below.
megaphone_rim = rr(11.3,1.45,2.9,12.1,1.45,exact=True)
megaphone_body = union(rr(1.55,5.55,2.6,3.9,.7,exact=True),path('M4.0 5.55L11.3 2.6V12.4L4.0 9.45Z'),
                       megaphone_rim,path('M4.6 9.4L5.35 12.95Q5.5 13.6 6.15 13.5Q6.8 13.4 6.65 12.75L6.05 9.95Z'))
shape('megaphone',megaphone_body,union(stroke(megaphone_rim),line((4.15,5.6),(4.15,9.4))))
HANDSET = path('M4.35 1.75C4.85 1.55 5.4 1.75 5.65 2.25L6.9 4.85C7.15 5.35 7.0 5.9 6.6 6.25L5.6 7.1'
               'C6.3 8.75 7.4 9.85 8.95 10.55L9.85 9.5C10.2 9.1 10.75 8.95 11.25 9.2L13.8 10.45'
               'C14.3 10.7 14.5 11.25 14.3 11.75L13.85 12.9C13.45 13.9 12.4 14.45 11.35 14.2'
               'C6.45 13.05 2.95 9.55 1.8 4.65C1.55 3.6 2.1 2.55 3.1 2.15Z')
shape('phone-call',HANDSET,stroke('M9.55 1.85A4.7 4.7 0 0 1 14.15 6.45M9.4 4.35A2.25 2.25 0 0 1 11.65 6.6'))
# SF video: a rounded camera body with a separate, soft trapezoid lens.
CAMERA_BODY = rr(1.17,3.25,9.6,9.5,2.1,exact=True)
CAMERA_LENS = path('M11.75 6.55L13.65 5.1C14.15 4.75 14.83 5.1 14.83 5.7V10.3C14.83 10.9 14.15 11.25 13.65 10.9L11.75 9.45Z')
shape('video-call',CAMERA_BODY,CAMERA_LENS)
glyph('at-sign',stroke(path('M12.3 12.8C5.5 17.8-.2 11 2.2 5C4.5-.7 14.5 1 14.5 7.3C14.5 11 10 11.5 10 8.5V5').transform(.94,0,0,.94,.5,.45)),
      stroke(path('M10 6C7 3 4 6 5 8.8C6 11.5 10 10.5 10 7').transform(.94,0,0,.94,.5,.45)))
# SF dot.radiowaves.up.forward: a dot and three quarter-circle waves.
glyph('rss',stroke('M4.35 8.25A3.4 3.4 0 0 1 7.75 11.65M4.35 5.95A5.7 5.7 0 0 1 10.05 11.65M4.35 3.67A7.98 7.98 0 0 1 12.33 11.65'),circle(4.35,11.65,1.2))

CATEGORY='People and accessibility'
# SF person: a slightly oval head over a domed torso, 11.2 x 11.9 with outline.
head = ellipse(8,5.02,2.2,2.4)
shoulders = path('M2.92 12.4C2.92 10.6 5.2 9.31 8 9.31C10.8 9.31 13.08 10.6 13.08 12.4V12.53'
                 'C13.08 13.05 12.65 13.48 12.13 13.48H3.87C3.35 13.48 2.92 13.05 2.92 12.53Z')
person = union(head,shoulders)
shape('user',person)
avatar_frame = circle()
# person.crop.circle: a filled figure cropped by the dial.
avatar = union(circle(8,6.1,2.3),op(ellipse(8,15.35,5.75,5.0),circle(8,8,5.6),po.PathOp.INTERSECTION))
shape('circle-user',avatar_frame,avatar)
# person.2: the rear figure is smaller and stops short of the front one.
users_front = transform(person,scale=.86,dx=2.25,dy=.83)
users_back = transform(person,scale=.76,dx=-2.6,dy=1.48)
stacked('users',users_back,users_front)
CATEGORY='People and accessibility'
badge_person = union(transform(head,scale=.67,dx=-2.95,dy=-1.1),
                     transform(shoulders,scale=.67,dx=-2.95,dy=-.25))
for name, kind in [('user-plus','plus'),('user-check','check'),('user-x','x')]:
    shape(name,person); badge(name,kind)
def bound_cover(name, cover, holes, features):
    tabs = union(*(line((1.45,y),(x,y)) for x,y in holes))
    shape(name,cover,union(tabs,features))
    body = DRAWINGS[name][0]
    punches = union(*(circle(x,y,1.65) for x,y in holes))
    solid = op(union(body,stroke(body)),union(punches,features),po.PathOp.DIFFERENCE)
    STYLE_OVERRIDES[name] = {'solid':union(solid,tabs)}
# person.crop.rectangle: a filled figure standing on the card's lower edge.
CARD = rr(1.22,2.62,13.56,10.76,1.9,exact=True)
shape('contact',CARD,union(circle(8,6.45,2.05),op(ellipse(8,14.35,4.55,4.0),rr(1.74,3.14,12.52,9.72,1.4,exact=True),po.PathOp.INTERSECTION)))
# SF accessibility: the figure inside the system circle.
# Solid SF figures: round head, 1.75 u limbs, 2.3 u torso (figure.roll, accessibility).
LIMB, TORSO = 1.75, 2.3
shape('accessibility',circle(),union(circle(8,4.45,1.2),stroke('M4.45 6.85Q8 7.55 11.55 6.85',LIMB,exact=True),
      stroke('M8 7.4V9.0',TORSO,exact=True),stroke('M7.35 9.0L6.65 12.2M8.65 9.0L9.35 12.2',LIMB,exact=True)))
# Kept for modules that compose the previous chair parts.
wheel = stroke('M4.65 7.65A3.5 3.5 0 1 0 9.5 11.45')
front_caster = ring(12.25,13.4,1.5)
roll_wheel = stroke('M5.0 7.55A3.85 3.85 0 1 0 10.75 12.15')
glyph('wheelchair',union(roll_wheel,circle(13.25,13.55,.95)),
      union(circle(9.35,2.35,1.45),stroke('M8.55 5.35L7.85 8.85',TORSO,exact=True),
            stroke('M7.85 8.85H10.9L11.85 12.2M8.45 5.9L11.0 6.85',LIMB,exact=True)))
# SF face.smiling: upright oval eyes over a soft smile.
FACE_EYES = union(ellipse(5.85,6.45,.72,1.08),ellipse(10.15,6.45,.72,1.08))
for name,detail in [('smile',stroke('M5.15 9.65Q8 12.75 10.85 9.65')),('frown',stroke('M5.15 11.75Q8 8.65 10.85 11.75')),('meh',line((5.4,10.6),(10.6,10.6)))]:
    shape(name,circle(),union(FACE_EYES,detail))
# SF hand.raised: four fingers and a thumb tucked low against the palm.
hand_body = path('M4.6 9.0V4.05C4.6 3.45 5.08 2.97 5.68 2.97C6.27 2.97 6.75 3.45 6.75 4.05V2.95'
                 'C6.75 2.35 7.23 1.87 7.83 1.87C8.42 1.87 8.9 2.35 8.9 2.95V3.75'
                 'C8.9 3.15 9.38 2.67 9.98 2.67C10.57 2.67 11.05 3.15 11.05 3.75V5.5'
                 'C11.05 4.97 11.49 4.53 12.03 4.53C12.56 4.53 13.0 4.97 13.0 5.5V9.7'
                 'C13.0 12.4 11.1 14.35 8.55 14.35C6.8 14.35 5.55 13.6 4.6 12.2L2.55 9.15'
                 'C2.15 8.55 2.3 7.8 2.9 7.45C3.5 7.15 4.15 7.35 4.6 7.9Z')
shape('hand',hand_body,lines('M6.75 4.05V7.4','M8.9 3.75V7.4','M11.05 5.5V7.55'))
# SF hand.thumbsup: a raised thumb over a fist of wrapped, stacked fingers,
# with a slim cuff held clear on the wrist side.
fist = path('M5.0 7.3L6.95 3.0C7.35 2.1 8.2 1.65 9.05 1.9C9.95 2.2 10.35 3.1 10.1 4.0L9.55 6.55H12.45'
            'C13.2 6.55 13.75 7.1 13.75 7.8C13.75 8.5 13.2 9.0 12.6 9.05C13.2 9.1 13.6 9.6 13.6 10.25'
            'C13.6 10.9 13.1 11.4 12.45 11.45C13.0 11.55 13.35 12.0 13.35 12.55C13.35 13.2 12.85 13.7 12.2 13.7'
            'H7.0C5.9 13.7 5.0 12.8 5.0 11.7Z')
cuff = rr(.95,7.0,2.15,6.7,1.07,exact=True)
knuckles = lines('M10.35 9.05H12.6','M10.35 11.45H12.45')
shape('thumbs-up',union(fist,cuff),knuckles)
flip = lambda p: p.transform(1,0,0,-1,0,16)
shape('thumbs-down',union(flip(fist),flip(cuff)),flip(knuckles))
CATEGORY='Security'
# SF shield: a pointed crown, straight flanks and a tapered keel.
SHIELD=path('M8 2.12L12.2 3.6Q12.83 3.83 12.83 4.5V8.95Q12.83 10.4 11.6 11.25L8.6 13.45Q8 13.9 7.4 13.45'
            'L4.4 11.25Q3.17 10.4 3.17 8.95V4.5Q3.17 3.83 3.8 3.6Z')
keyhole = union(circle(8,6.75,1.3),poly([(7.4,7.3),(8.6,7.3),(8.95,10.35),(7.05,10.35)]))
for name,detail in [('shield',po.Path()),('shield-check',check(8,7.9,.85)),('shield-x',cross(8,7.75,.8)),
                    ('shield-alert',union(line((8,4.85),(8,8.25)),circle(8,10.4,.72))),
                    ('shield-keyhole',keyhole)]: shape(name,SHIELD,detail)
# SF lock: a compact body under a tall round shackle, no keyhole.
LOCK_BODY = rr(4.16,6.85,7.68,6.9,1.6,exact=True)
shape('lock',LOCK_BODY,stroke('M5.6 6.85V4.45A2.4 2.4 0 0 1 10.4 4.45V6.85'))
shape('lock-open',rr(2.9,6.85,7.68,6.9,1.6,exact=True),stroke('M9.0 6.85V4.45A2.4 2.4 0 0 1 13.8 4.45V5.75'))
# SF key: an upright bow with a small eye above a notched blade.
shape('key',union(circle(8,4.85,3.55),path('M6.85 8.0H9.15V9.15L9.85 9.85L9.15 10.55V10.95L9.85 11.65L9.15 12.35V13.0L8 14.15L6.85 13.0Z')),
      ring(8,3.9,1.15))
# SF touchid: concentric ridges opening downward, inner ridges running into the base.
glyph('fingerprint',stroke('M2.080 10.755A6.3 6.3 0 1 1 13.920 10.755M4.150 11.296A4.7 4.7 0 1 1 12.540 9.816L12.890 13.9'),stroke('M4.900 8.600A3.1 3.1 0 0 1 11.100 8.600V12.2M4.900 8.600V11.2Q4.9 12.9 4.3 13.9M6.500 8.600A1.5 1.5 0 0 1 9.500 8.600V13.95M6.5 8.6V10.9Q6.5 12.6 5.9 13.95'))
# SF eye: a full-width almond with an iris ring and a solid pupil.
shape('eye',path('M1.2 8C2.85 4.75 5.25 3.05 8 3.05C10.75 3.05 13.15 4.75 14.8 8C13.15 11.25 10.75 12.95 8 12.95C5.25 12.95 2.85 11.25 1.2 8Z'),
      union(ring(8,8,3.05),circle(8,8,1.05)))
DRAWINGS['eye-off'] = DRAWINGS['eye']
glyph('scan',lines('M2.22 5.35V3.92Q2.22 2.22 3.92 2.22H5.35','M10.65 2.22H12.08Q13.78 2.22 13.78 3.92V5.35',
                   'M13.78 10.65V12.08Q13.78 13.78 12.08 13.78H10.65','M5.35 13.78H3.92Q2.22 13.78 2.22 12.08V10.65'),None)
shape('qr-code',union(rr(2.1,2.1,4.6,4.6,1),rr(9.3,2.1,4.6,4.6,1),rr(2.1,9.3,4.6,4.6,1)),
      union(rr(3.65,3.65,1.5,1.5,.3,exact=True),rr(10.85,3.65,1.5,1.5,.3,exact=True),rr(3.65,10.85,1.5,1.5,.3,exact=True),
            rr(9.0,9.0,1.6,1.6,.3,exact=True),rr(12.3,9.0,1.6,1.6,.3,exact=True),rr(10.65,10.65,1.6,1.6,.3,exact=True),
            rr(9.0,12.3,1.6,1.6,.3,exact=True),rr(12.3,12.3,1.6,1.6,.3,exact=True)))
shape('badge-check',badge_body(),check(8,8.05,.9))

CATEGORY='Time and planning'
CLOCK_HANDS = line((8,4.05),(8,8),(5.35,8))  # SF clock: hands at nine o'clock
shape('clock',circle(),CLOCK_HANDS)
alarm_bells = union(path('M1.85 4.4C1.4 3.0 2.55 1.55 4.05 1.75C4.6 1.85 4.75 2.2 4.4 2.55L2.65 4.4C2.35 4.7 1.95 4.7 1.85 4.4Z'),
                    path('M14.15 4.4C14.6 3.0 13.45 1.55 11.95 1.75C11.4 1.85 11.25 2.2 11.6 2.55L13.35 4.4C13.65 4.7 14.05 4.7 14.15 4.4Z'))
shape('alarm-clock',circle(8,8.55,5.35),union(line((8,5.4),(8,8.55),(5.85,8.55)),alarm_bells,lines('M4.1 12.6L2.85 14.15','M11.9 12.6L13.15 14.15')))
# clock.arrow.circlepath: an open dial whose return carries a filled head.
history_arc = stroke('M3.4 9.3A5.55 5.55 0 1 0 4.95 4.0')
glyph('history',union(history_arc,tri_head(3.35,10.0,90,2.35,1.75)),line((8.95,4.95),(8.95,8.25),(10.95,10.25)))
# SF timer: an open dial with a hand sweeping from its pivot.
timer_dial = stroke('M8 1.98V3.85M8 1.98A6.02 6.02 0 1 1 3.75 3.75')
glyph('timer',timer_dial,union(circle(8,8,1.2),line((8,8),(5.45,5.45))))
hourglass_body = path('M5.2 2.65H10.8C11.1 2.65 11.3 2.9 11.25 3.2C11.0 5.4 10.0 6.9 8.75 8.0C10.0 9.1 11.0 10.6 11.25 12.8'
                      'C11.3 13.1 11.1 13.35 10.8 13.35H5.2C4.9 13.35 4.7 13.1 4.75 12.8C5.0 10.6 6.0 9.1 7.25 8.0'
                      'C6.0 6.9 5.0 5.4 4.75 3.2C4.7 2.9 4.9 2.65 5.2 2.65Z')
shape('hourglass',hourglass_body,path('M6.35 11.95Q6.8 10.35 8 9.85Q9.2 10.35 9.65 11.95Z'))
# SF calendar: a solid header band over a grid of small square dates.
CAL=rr(2.12,2.66,11.76,10.68,1.9,exact=True)
CALTOP=op(union(CAL,stroke(CAL,STROKE,exact=True)),rr(0,0,16,5.0,0),po.PathOp.INTERSECTION)
def date_grid(cells): return union(*(rr(x-.5,y-.5,1.0,1.0,.25,exact=True) for x,y in cells))
CAL_DATES = date_grid([(6.95,6.9),(9.05,6.9),(11.15,6.9),(4.85,8.95),(6.95,8.95),(9.05,8.95),(11.15,8.95),(4.85,11.0),(6.95,11.0),(9.05,11.0)])
CAL_BADGE = (11.95,11.95,3.15)
def calendar(name, detail=po.Path(), mark=None):
    shape(name,CAL,union(CALTOP,detail))
    b=DRAWINGS[name][0]
    field=union(b,stroke(b))
    interior=op(field,stroke(field,1.8),po.PathOp.DIFFERENCE)
    gap=line((1,5.45),(15,5.45),width=.9)
    STYLE_OVERRIDES[name]={'solid':op(field,union(gap,op(detail,interior,po.PathOp.INTERSECTION)),po.PathOp.DIFFERENCE)}
    if mark: badge(name,mark,*CAL_BADGE)
calendar('calendar',CAL_DATES)
calendar('calendar-days',union(CAL_DATES,date_grid([(11.15,11.0)])))
for name,kind in [('calendar-check','check'),('calendar-plus','plus'),('calendar-x','x'),('calendar-clock','clock')]:
    calendar(name,date_grid([(4.85,6.9),(6.95,6.9),(9.05,6.9),(4.85,8.95),(6.95,8.95),(4.85,11.0)]),kind)
calendar('calendar-range',union(line((5.5,9.1),(10.5,9.1)),dots((4.85,9.1),(11.15,9.1),r=1.0)))
calendar('calendar-heart',heart(8,9.25,4.2))
# SF checklist: checked and open rows beside their text lines.
glyph('list-todo',union(op(circle(3.6,4.85,2.05),check(3.6,4.9,.45),po.PathOp.DIFFERENCE),ring(3.6,11.15,2.05)),
      lines('M7.6 4.85H14.1','M7.6 11.15H14.1'))
# SF book.closed: cover, spine and the page block along the bottom.
shape('notebook',rr(3.12,1.67,9.76,12.66,1.6,exact=True),stroke('M5.3 1.67V11.2M3.12 12.55Q3.12 11.2 4.45 11.2H12.88'))
shape('sticky-note',path('M3.9 2.12H12.1C13.08 2.12 13.88 2.92 13.88 3.9V9.6L9.6 13.88H3.9C2.92 13.88 2.12 13.08 2.12 12.1V3.9C2.12 2.92 2.92 2.12 3.9 2.12Z'),
      stroke('M9.6 13.7V11.0Q9.6 9.6 11.0 9.6H13.7M4.95 5.55H11.05M4.95 8.15H8.95'))
shape('flag',path('M3.6 2.75Q6.0 1.55 8.2 2.75T12.75 2.75V9.15Q10.4 10.35 8.2 9.15T3.6 9.15Z'),line((3.6,2.25),(3.6,14.0)))
BOOKMARK = path('M5.0 1.65H11.0C11.72 1.65 12.3 2.23 12.3 2.95V13.35C12.3 13.95 11.65 14.25 11.2 13.9L8 11.45L4.8 13.9'
                'C4.35 14.25 3.7 13.95 3.7 13.35V2.95C3.7 2.23 4.28 1.65 5.0 1.65Z')
shape('bookmark',BOOKMARK)
shape('bookmark-plus',BOOKMARK,plus(8,6.6,.95))
shape('bookmark-check',BOOKMARK,check(8,6.65,.8))
CATEGORY='Security'
shape('shield-lock',SHIELD,lock_mark(8,7.65,3.9,2.9,1.1,.6))
CATEGORY='Time and planning'
# SF pin: a pushpin with a stepped cap, a domed collar and a fine needle.
shape('pin',path('M5.45 1.75H10.55Q11.2 1.75 11.05 2.35L10.4 5.15Q12.4 6.35 12.6 8.55Q12.65 9.15 12.05 9.15H3.95'
                 'Q3.35 9.15 3.4 8.55Q3.6 6.35 5.6 5.15L4.95 2.35Q4.8 1.75 5.45 1.75Z'),line((8,9.15),(8,14.25)))
shape('target',circle(),union(ring(8,8,3.5,1.25),circle(8,8,1.2)))
# SF trophy: cup, side handles, stem and a solid plinth.
shape('trophy',union(path('M4.35 2.15H11.65V6.25C11.65 8.5 10.1 10.25 8 10.25C5.9 10.25 4.35 8.5 4.35 6.25Z'),rr(5.35,12.05,5.3,2.1,.7,exact=True)),
      union(stroke('M4.35 3.25H2.85Q2.1 3.25 2.1 4.0V4.75Q2.1 7.2 4.6 7.6M11.65 3.25H13.15Q13.9 3.25 13.9 4.0V4.75Q13.9 7.2 11.4 7.6M8 10.25V12.05')))

CATEGORY='Media'
# Inner media marks are filled, as in SF play.circle / pause.circle / stop.circle.
for name,detail in [('play',poly([(6.5,5.05),(11.25,8),(6.5,10.95)])),
                    ('pause',union(rr(5.75,5.15,1.6,5.7,.55,exact=True),rr(8.65,5.15,1.6,5.7,.55,exact=True))),
                    ('stop',rr(5.75,5.75,4.5,4.5,.75,exact=True))]: shape(name,circle(),detail)
for name,source in [('pause-circle-fill','pause'),('play-circle','play'),('stop-circle','stop')]:
    b,d,o,c,t=DRAWINGS[source];add(name,b,d,o,t)
# SF forward.end / backward.end: an outlined triangle against an end bar.
skip_triangle = path('M3.6 3.65L10.0 8L3.6 12.35Z')
shape('skip-forward',skip_triangle,line((12.4,3.65),(12.4,12.35)))
shape('skip-back',mirror(skip_triangle),line((3.6,3.65),(3.6,12.35)))
# SF forward / backward: two outlined triangles, the second meeting the first's tip.
ff_rear, ff_front = path('M1.45 3.65L7.75 8L1.45 12.35Z'), path('M7.75 3.65L14.05 8L7.75 12.35Z')
for name,f in [('fast-forward',lambda p:p),('rewind',mirror)]:
    shape(name,union(f(ff_rear),f(ff_front)),stroke(f(ff_front)))
    STYLE_OVERRIDES[name]={'solid':union(f(ff_rear),f(ff_front),stroke(union(f(ff_rear),f(ff_front))))}
SPEAKER = path('M2.0 6.0Q2.0 5.4 2.6 5.4H4.6L8.05 2.35Q8.75 1.8 8.75 2.7V13.3Q8.75 14.2 8.05 13.65L4.6 10.6H2.6Q2.0 10.6 2.0 10.0Z')
shape('volume',SPEAKER,stroke('M10.95 5.9A3.0 3.0 0 0 1 10.95 10.1M12.4 3.95A5.5 5.5 0 0 1 12.4 12.05'))
shape('volume-off',transform(SPEAKER,dx=1.6),line((2,2),(14,14)))
# SF mic: capsule head over a cradle arc, stem and foot.
mic_body = rr(5.55,1.65,4.9,8.05,2.45)
mic_stand = lines('M3.95 7.0V7.75A4.05 4.05 0 0 0 12.05 7.75V7.0','M8 11.8V14.2','M5.85 14.2H10.15')
shape('microphone',mic_body,mic_stand)
DRAWINGS['microphone-off'] = DRAWINGS['microphone']
headband = stroke('M3.05 7.9V6.8A4.95 4.95 0 0 1 12.95 6.8V7.9')
earcups = union(rr(1.55,7.9,3.15,5.15),rr(11.3,7.9,3.15,5.15))
glyph('headphones',headband,earcups)
def notehead(x,y):
    return circle(0,0,1).transform(1.85,-.52,.2,1.3,x,y)
beam = stroke('M5.65 11.45V4.25L12.65 2.6V9.8M5.65 6.7L12.65 5.05')
heads = union(notehead(4.35,11.95),notehead(11.35,10.3))
glyph('music',beam,heads)
# SF photo: a filled sun and two filled peaks resting on the frame.
FRAME = rr(1.22,2.82,13.56,10.36,1.9,exact=True)
frame_inner = rr(1.74,3.34,12.52,9.32,1.4,exact=True)
PHOTO_SCENE = union(circle(5.05,6.3,1.35),op(path('M1.0 12.2L5.55 8.6Q6.1 8.15 6.65 8.6L8.65 10.25L10.6 7.75Q11.1 7.2 11.6 7.75L15.0 11.25V14H1Z'),frame_inner,po.PathOp.INTERSECTION))
shape('image',FRAME,PHOTO_SCENE)
# photo.badge.*: the photo steps up and left for a lower-right badge.
def photo_badge(name, kind, tags=''):
    shape(name,transform(FRAME,scale=.9,dx=-.75,dy=-.65),transform(PHOTO_SCENE,scale=.9,dx=-.75,dy=-.65),tags)
    badge(name,kind,12.2,11.95,3.15)
for name,kind,tags in [('image-plus','plus',''),('image-check','check','photo picture verified selected'),
                       ('image-search','search','photo picture search find visual lookup')]:
    photo_badge(name,kind,tags)
# SF camera: a body with a raised viewfinder hump, lens ring and flash dot.
shape('camera',path('M3.0 4.6H4.9L5.9 3.05Q6.25 2.55 6.85 2.55H9.15Q9.75 2.55 10.1 3.05L11.1 4.6H13.0'
                    'C14.0 4.6 14.78 5.4 14.78 6.4V11.65C14.78 12.65 14.0 13.45 13.0 13.45H3.0'
                    'C2.0 13.45 1.22 12.65 1.22 11.65V6.4C1.22 5.4 2.0 4.6 3.0 4.6Z'),
      union(ring(8,8.9,3.15),circle(12.15,6.75,.65)))
DRAWINGS['camera-off'] = DRAWINGS['camera']
# SF play.rectangle.
shape('video',FRAME,poly([(6.65,5.5),(10.65,8),(6.65,10.5)]))
# SF film: perforated side strips around two frames.
film_holes = union(*(rr(x-.5,y-.5,1.0,1.0,.3,exact=True) for x in (2.7,13.3) for y in (4.85,7.0,9.0,11.15)))
shape('film',FRAME,union(lines('M4.2 2.82V13.18','M11.8 2.82V13.18','M4.2 8H11.8'),film_holes))
STYLE_OVERRIDES['film']={'solid':op(union(FRAME,stroke(FRAME)),union(film_holes,rr(4.72,3.34,6.56,4.14,.8,exact=True),rr(4.72,8.52,6.56,4.14,.8,exact=True)),po.PathOp.DIFFERENCE)}
shape('radio',rr(1.22,5.0,13.56,8.9,1.9,exact=True),union(line((3.4,5.0),(11.6,2.0)),ring(5.6,9.45,2.25),lines('M10.1 8.05H12.35','M10.1 10.85H12.35')))
# SF tv: a wide screen on a short foot, no antenna.
shape('tv',rr(1.22,2.35,13.56,9.5,1.9,exact=True),line((5.2,13.85),(10.8,13.85)))
glyph('cast',stroke('M2.1 5.0V4.3Q2.1 2.6 3.8 2.6H12.2Q13.9 2.6 13.9 4.3V11.7Q13.9 13.4 12.2 13.4H10.6'),
      union(stroke('M2.1 7.6A5.8 5.8 0 0 1 7.9 13.4M2.1 10.45A2.95 2.95 0 0 1 5.05 13.4'),circle(2.35,13.15,.85)))
shape('airplay',rr(1.22,2.35,13.56,9.6,1.9,exact=True),poly([(8,8.4),(12.6,14.1),(3.4,14.1)]))
# SF waveform: seven rounded bars rising to the center.
wave=[(2.6,1.55),(4.4,3.25),(6.2,5.05),(9.8,4.15),(11.6,2.55),(13.4,1.3)]
glyph('waveform',lines(*(f'M{x} {8-h}V{8+h}' for x,h in wave)),line((8,1.85),(8,14.15)))
disc_glint = stroke('M4.65 6.85Q5.3 5.25 6.85 4.65')
shape('disc',circle(),union(ring(8,8,1.55,1.05),disc_glint,transform(disc_glint,180)))
glyph('podcast',stroke('M3.4 11A6 6 0 1 1 12.6 11M5.2 8.9A3.5 3.5 0 1 1 10.8 8.9',1.1),union(circle(8,6,1.25),rr(6.7,8.5,2.6,6,1.3)))

CATEGORY='Layout'
WINDOW=FRAME  # SF macwindow / rectangle: 14.6 x 11.4 with outline
for name,detail in [('app-window',dots((3.75,4.75),(5.55,4.75),(7.35,4.75),r=.6)),('browser',lines('M1.22 5.6H14.78','M3.5 4.2H3.5','M5.3 4.2H5.3')),
                    ('layout-sidebar',union(line((5.6,2.82),(5.6,13.18)),lines('M3.05 5.4H3.8','M3.05 7.4H3.8','M3.05 9.4H3.8'))),
                    ('table',stroke('M1.22 6.3H14.78M1.22 9.7H14.78M5.75 2.82V13.18M10.25 2.82V13.18'))]:
    shape(name,WINDOW,detail)
# rectangle.3.group and square.grid.2x2: separate tiles with SF gaps.
shape('layout-dashboard',union(rr(1.22,2.82,6.6,10.36,1.6,exact=True),rr(9.86,2.82,4.92,4.16,1.4,exact=True),rr(9.86,9.02,4.92,4.16,1.4,exact=True)))
shape('layout-grid',union(*(rr(x,y,4.36,4.36,1.3,exact=True) for x in (2.62,9.02) for y in (2.62,9.02))))
for name,detail in [('panel-left',line((5.6,2.82),(5.6,13.18))),('panel-right',line((10.4,2.82),(10.4,13.18))),
                    ('panel-top',line((1.22,6.05),(14.78,6.05))),('panel-bottom',line((1.22,9.95),(14.78,9.95))),
                    ('columns',line((8,2.82),(8,13.18))),('rows',line((1.22,8),(14.78,8)))]:
    shape(name,WINDOW,detail)
# arrow.up.left.and.arrow.down.right and its inward counterpart.
glyph('maximize',union(line((9.1,9.1),(13.4,13.4)),line((13.4,10.1),(13.4,13.4),(10.1,13.4))),
      union(line((6.9,6.9),(2.6,2.6)),line((2.6,5.9),(2.6,2.6),(5.9,2.6))))
glyph('minimize',union(line((13.6,13.6),(9.1,9.1)),line((9.1,12.4),(9.1,9.1),(12.4,9.1))),
      union(line((2.4,2.4),(6.9,6.9)),line((6.9,3.6),(6.9,6.9),(3.6,6.9))))
glyph('fullscreen',lines('M1.9 5.4V3.6Q1.9 1.9 3.6 1.9H5.4','M10.6 14.1H12.4Q14.1 14.1 14.1 12.4V10.6'),
      lines('M10.6 1.9H12.4Q14.1 1.9 14.1 3.6V5.4','M1.9 10.6V12.4Q1.9 14.1 3.6 14.1H5.4'))
shape('picture-in-picture',WINDOW,rr(7.9,7.85,4.85,3.3,.8,exact=True))
top_sheet = path('M1.55 5.5L8 1.95L14.45 5.5L8 9.05Z')
lower_sheet = path('M1.55 9.35L8 12.9L14.45 9.35V11.15L8 14.7L1.55 11.15Z')
glyph('layers',lower_sheet,top_sheet)
STYLE_OVERRIDES['layers'] = {'stroke':union(stroke(top_sheet),stroke('M1.55 10.3L8 13.85L14.45 10.3'))}
mux_back, mux_front = rr(1.17,1.17,10.26,10.26,1.9,exact=True), rr(4.57,4.57,10.26,10.26,1.9,exact=True)
stacked('multiplexer',mux_back,mux_front,lines('M9.7 4.57V14.83','M4.57 9.7H14.83'))

CATEGORY='Editing and design'
def sf_pencil(tx, ty, angle=-45, length=12.0, width=2.05, cap=1.45, gap=.8):
    """SF pencil (shared with lane D's pen-on-object icons): a slim solid bar
    with a sharpened tip at (tx, ty) and a separate end cap."""
    hw=width/2; cone=2.35; body_end=length-cap-gap
    p=path(f'M0 0L{cone} {-hw}H{body_end}V{hw}H{cone}Z'
           f'M{length-cap} {-hw}H{length}V{hw}H{length-cap}Z')
    p=soften(p,.3)
    a=math.radians(angle); c,s=math.cos(a),math.sin(a)
    return p.transform(c,s,-s,c,tx,ty)
glyph('pencil',sf_pencil(2.55,13.45,length=15.4),po.Path())
# SF eraser: a tilted rounded block with a band near its working end.
eraser_block = transform(rr(2.2,5.15,11.6,5.7,1.7,exact=True),-45)
shape('eraser',eraser_block,transform(line((6.35,5.15),(6.35,10.85)),-45))
brush = path('M1.7 14.3Q2.8 13.1 2.6 11.65Q2.35 9.05 5.2 8.65L10.75 2.25'
             'C12.95 .1 15.9 3.25 13.75 5.35L7.3 10.95Q7.05 14.4 1.7 14.3Z')
ferrule = line((5.15,8.65),(7.35,10.85))
shape('paintbrush',brush,ferrule)
shape('palette',path('M8 1.5C0 1.5-1 13 6 14.5Q10 15 9 12Q8 10 11 10C17 11 16 1.5 8 1.5Z'),dots((5,5),(9,4),(12,6),(3.5,8)))
SWATCH=rr(2.6,1.95,4,9.4)
SWATCH_DIAGONAL=SWATCH.transform(.707107,.707107,-.707107,.707107,8.84,.01)
swatch_front = rr(2,9.55,12,4.4)
swatch_pivot = circle(4.3,11.75,.62)
swatch_rear = op(stroke(SWATCH),SWATCH_DIAGONAL,po.PathOp.DIFFERENCE)
swatch_edges = op(union(swatch_rear,stroke(SWATCH_DIAGONAL)),swatch_front,po.PathOp.DIFFERENCE)
swatch_ink = union(swatch_edges,stroke(swatch_front),swatch_pivot)
shape('swatch',union(SWATCH,SWATCH_DIAGONAL,swatch_front),swatch_ink)
STYLE_OVERRIDES['swatch'] = {'stroke':swatch_ink}
glyph('crop',stroke('M4.3 1.6V10.55Q4.3 11.7 5.45 11.7H14.4'),stroke('M1.6 4.3H10.55Q11.7 4.3 11.7 5.45V14.4'))
# SF ruler: horizontal, with alternating ticks hanging from the top edge.
shape('ruler',rr(1.22,4.65,13.56,6.7,1.6,exact=True),lines('M3.4 4.65V7.6','M5.7 4.65V6.5','M8 4.65V7.6','M10.3 4.65V6.5','M12.6 4.65V7.6'))
glyph('scissors',union(ring(4,4,2.5,1.35),ring(4,12,2.5,1.35)),lines('M6 5.5L14 13','M6 10.5L14 3'))
nib = path('M2.1 13.95L4.2 5.3L9.15 2.05L13.95 6.85L10.75 11.9Z')
shape('pen-tool',nib,union(circle(7.85,8.15,1.15),line((2.1,13.95),(7.35,8.65))))
# Fit the bulb, collar and glass tube on one axis before tipping the tool.
bulb = transform(path('M5.85 6.55V3.15C5.85 .25 10.15 .25 10.15 3.15V6.55Z'),45)
tube = transform(path('M6.55 6.55H9.45V11.55Q9.45 12.55 8 13.25Q6.55 12.55 6.55 11.55Z'),45)
tip = transform(line((8,13.25),(8,14.85)),45)
collar = transform(line((4.65,6.55),(11.35,6.55)),45)
shape('pipette',union(bulb,tube),union(collar,tip))
STYLE_OVERRIDES['pipette'] = {'solid':union(bulb,stroke(bulb),stroke(tube),collar,tip)}
# Text formatting letters keep SF's cap height (about 9 u), not the full canvas.
bold_body = path('M3.1 1.65H8.65C13.15 1.65 14 6.1 11.2 7.65'
                 'C14.85 9.1 13.95 14.35 9.25 14.35H3.1Z')
bold_counters = path('M5.9 4.1V6.65H8.25C10.75 6.65 10.75 4.1 8.25 4.1Z'
                     'M5.9 9.05V11.9H8.8C11.45 11.9 11.45 9.05 8.8 9.05Z')
glyph('bold',transform(op(bold_body,bold_counters,po.PathOp.DIFFERENCE),scale=.74,dx=-.35),po.Path())
glyph('italic',lines('M7.0 3.4H11.6','M4.4 12.6H9.0'),line((9.3,3.4),(6.7,12.6)))
glyph('underline',stroke('M4.7 2.9V7.35A3.3 3.3 0 0 0 11.3 7.35V2.9'),line((4.2,13.1),(11.8,13.1)))
glyph('strikethrough',transform(stroke(path('M11.8 3.45C9.4 1.3 4.3 1.75 4.3 4.7C4.3 8.15 11.9 7.35 11.9 11.1C11.9 14.2 6.6 14.9 3.65 12.4').transform(.76,0,0,.76,1.95,1.9))),line((2.4,8),(13.6,8)))
glyph('font',line((3.2,12.6),(8,3.4),(12.8,12.6)),line((4.95,9.25),(11.05,9.25)))
# SF text.alignleft: four rows over 11.1 u, alternating full and short.
ROWS4=(3,6.333,9.667,13)
for name,align in [('align-left','left'),('align-center','center'),('align-right','right'),('align-justify','justify')]:
    ds=[]
    for i,w in enumerate([11.9,8.1,11.9,8.1]):
        if align=='justify':w=11.9
        x=2.05 if align in ['left','justify'] else 13.95-w if align=='right' else (16-w)/2
        ds.append(line((x,ROWS4[i]),(x+w,ROWS4[i])))
    glyph(name,union(ds[0],ds[2]),union(ds[1],ds[3]))
glyph('list',dots((2.75,4),(2.75,8),(2.75,12),r=1.05),lines('M6.05 4H13.95','M6.05 8H13.95','M6.05 12H13.95'))
glyph('list-ordered',stroke('M1.65 3.95L3 2.7V6.5M1.55 9.85C1.8 8.2 4.65 8.5 3.85 10.25Q3.4 11.25 1.6 13.2H4.05',1.15),
      lines('M6.75 4.65H14','M6.75 11.1H14'))
# SF increase.indent / decrease.indent: a filled pointer beside indented rows.
INDENT_ROWS=lines('M2.05 3H13.95','M7.0 6.333H13.95','M7.0 9.667H13.95','M2.05 13H13.95')
glyph('indent',INDENT_ROWS,tri_head(4.85,8,0,2.6,1.9))
glyph('outdent',INDENT_ROWS,tri_head(2.25,8,180,2.6,1.9))
glyph('wrap',lines('M2 3H14','M2 13H6'),stroke('M2 7H11A3 3 0 0 1 11 13H9M11 10L8 13 11 15'))
# SF quote.opening: two filled commas turned to open the quotation.
quote_bowl = circle(3.95,6.25,2.75)
quote_tail = stroke('M6.15 6.25C6.15 9.3 4.65 11.8 2.55 12.85')
comma = transform(union(quote_bowl,quote_tail),180,dx=-7.7)
comma_outline = transform(union(ring(3.95,6.25,2.75),quote_tail),180,dx=-7.7)
glyph('quote',comma,transform(comma,dx=7.7))
STYLE_OVERRIDES['quote'] = {'stroke':union(comma_outline,transform(comma_outline,dx=7.7))}
glyph('hash',lines('M6.3 2.4L4.75 13.6','M11.25 2.4L9.7 13.6'),lines('M2.6 5.9H13.6','M2.4 10.1H13.4'))
# SF character.cursor.ibeam: a letter beside the text cursor.
glyph('text-cursor',union(line((1.9,12.6),(5.1,3.4),(8.3,12.6)),line((3.05,9.25),(7.15,9.25))),
      lines('M10.4 2.6H13.6','M12.0 2.6V13.4','M10.4 13.4H13.6'))
shape('text-select',SQUARE,lines('M5.7 5.4H10.3','M8 5.4V10.6','M6.6 10.6H9.4'))

CATEGORY='Technology and development'
# Lane B shared bases. A wide SF console (apple.terminal, server.rack:
# 15.1 x 11.7 scaled to the 14.7 canvas) with window-chrome corners.
def close_joins(p, r=.55):
    """Round concave junctions (cloud puffs, merged parts) with radius r."""
    grown = union(p, stroke(p, 2*r, exact=True))
    return op(grown, stroke(grown, 2*r, exact=True), po.PathOp.DIFFERENCE)
def badged_copy(name, source, kind, cx=11.85, cy=11.85, r=3.25, tags=None):
    """Register an SF `.badge.*` variant on an existing base drawing."""
    b, d, o, c, t = DRAWINGS[source]
    DRAWINGS[name] = (b, d, o, CATEGORY, t if tags is None else tags)
    if source in STYLE_OVERRIDES: STYLE_OVERRIDES[name] = dict(STYLE_OVERRIDES[source])
    badge(name, kind, cx, cy, r)
CONSOLE = rr(1.17,2.82,13.66,10.36,1.9,exact=True)
PROMPT = lines('M3.75 5.55L5.6 7.1L3.75 8.65','M6.75 8.65H9.2')
shape('terminal',CONSOLE,PROMPT)
console_back = rr(1.17,1.6,11.6,8.6,1.9,exact=True)
console_front = rr(3.23,5.0,11.6,8.6,1.9,exact=True)
console_prompt = transform(PROMPT,dx=2.15,dy=2.65)
shape('terminal-stack',union(console_back,console_front),union(stroke(console_front),console_prompt))
shape('code-block',WINDOW,stroke('M5.65 6.3L4.05 8L5.65 9.7M10.35 6.3L11.95 8L10.35 9.7M8.85 5.4L7.15 10.6',1.2))
glyph('code',lines('M5 4L1 8 5 12','M11 4L15 8 11 12'),line((9,2),(7,14)))
glyph('braces',stroke('M6 2H5Q4 2 4 4V6Q4 8 2 8Q4 8 4 10V12Q4 14 6 14'),stroke('M10 2H11Q12 2 12 4V6Q12 8 14 8Q12 8 12 10V12Q12 14 10 14'))
glyph('command', stroke('M5.65 5.65H3.65A2 2 0 1 1 5.65 3.65V12.35'
                        'A2 2 0 1 1 3.65 10.35H12.35A2 2 0 1 1 10.35 12.35V3.65'
                        'A2 2 0 1 1 12.35 5.65Z',1.3), po.Path())
# SF cpu: compact package, short pins, an outlined die.
cpu_pins = union(*(transform(lines('M5.6 1.85V3.25','M8 1.85V3.25','M10.4 1.85V3.25'),a) for a in (0,90,180,270)))
shape('cpu',rr(3.75,3.75,8.5,8.5,1.5,exact=True),union(stroke(rr(6.05,6.05,3.9,3.9,.75,exact=True)),cpu_pins))
# SF cylinder.split.1x2: a narrow drum (11.1 x 13.5), the front rim of the
# lid and one split across the middle.
shape('database',path('M3 3.75A5 2 0 0 1 13 3.75V12.25A5 2 0 0 1 3 12.25Z'),stroke('M3 3.75A5 2 0 0 0 13 3.75M3 8A5 2 0 0 0 13 8'))
for name,kind in [('database-arrow-down','arrow-down'),('database-arrow-up','arrow-up')]:
    badged_copy(name,'database',kind,tags=name.replace('-',' '))
rack_units = lines('M1.17 6.27H14.83','M1.17 9.73H14.83')
shape('server-rack',CONSOLE,union(rack_units,dots((11.95,4.55),(11.95,8),(11.95,11.45),r=.68)))
for name,kind in [('server-plus','plus'),('server-crash','alert')]:
    badged_copy(name,'server-rack',kind,tags=name.replace('-',' '))
# SF cloud: flat base, small left puff, dominant crown, mid right puff.
CLOUD = close_joins(union(circle(4.05,9.52,2.88),circle(7.75,7.35,3.65),circle(11.55,9.12,3.28),
                          rr(4.05,8.5,7.5,3.9,0)), .7)
shape('cloud',CLOUD)
# SF display: a wide screen (15.3 x 12.9 scaled) on a short neck and foot.
shape('monitor',rr(1.17,2.3,13.66,9.0,1.5,exact=True),lines('M8 11.3V13.5','M5.35 13.5H10.65'))
# SF laptopcomputer: an open screen standing on a full-width flat base.
laptop_screen = rr(2.55,3.6,10.9,7.85,1.5,exact=True)
laptop_base = line((1.17,12.45),(14.83,12.45))
shape('laptop',laptop_screen,laptop_base)
# SF iphone: 8.2 x 13.5, a single island at the top.
shape('phone',rr(4.42,1.77,7.16,12.46,1.85,exact=True),line((7.1,3.75),(8.9,3.75)))
shape('phone-android',rr(4,1,8,14,1.5),union(circle(8,3,.5),dots((6,13),(8,13),(10,13),r=.4)))
shape('simulator',rr(4,1,8,14,2),union(poly([(6.5,5.5),(10,8),(6.5,10.5)]),line((7,13),(9,13))))
shape('tablet',rr(2.5,1,11,14,2),circle(8,12.5,.65))
# SF keyboard: wide and low (16 x 10.1 scaled), two rows of square keys
# above a space bar.
keys = union(*(rr(x-.5,y-.5,1.0,1.0,.25,exact=True) for x in (3.75,5.9,8.05,10.2,12.35) for y in (5.75,7.95)))
shape('keyboard',rr(1.17,3.4,13.66,9.2,1.5,exact=True),union(keys,line((5.35,10.2),(10.75,10.2))))
# SF computermouse: 9 x 14 capsule with the button split.
shape('mouse',rr(4.02,1.52,7.96,12.96,3.98,exact=True),stroke('M8 1.6V6.35M4.05 6.35H11.95'))
# SF applewatch: a tall squircle case, tapered straps, a crown at the side.
shape('watch',rr(3.9,3.4,8.2,9.2,2.4,exact=True),union(stroke('M5.6 3.4L6.0 1.6H10.0L10.4 3.4M5.6 12.6L6.0 14.4H10.0L10.4 12.6'),
      line((12.65,6.6),(12.65,7.9)),line((8,5.6),(8,8),(9.6,8.95))))
printer_chassis = rr(1.55,5.2,12.9,6.4)
output_sheet = rr(4.25,9.55,7.5,4.8)
printer = union(printer_chassis,output_sheet,rr(4.15,1.65,7.7,4.8))
printer_seams = union(line((3.4,5.2),(12.6,5.2)), stroke(output_sheet),stroke(circle(11.85,7.35,1.05)))
shape('printer',printer,printer_seams)
usb_body = rr(4.15,6.45,7.7,7.8)
usb_plug = rr(4.95,1.85,6.1,5.4)
contacts = lines('M6.7 3.9V4.55', 'M9.3 3.9V4.55')
shape('usb',union(usb_body,usb_plug),union(line((4.95,6.45),(11.05,6.45)),contacts))
# SF externaldrive: a wide, low case whose upper shell tapers inward.
DRIVE = path('M4.6 3.35H11.4Q12.35 3.35 12.8 4.15L14.83 7.75V10.25A2.4 2.4 0 0 1 12.43 12.65H3.57'
             'A2.4 2.4 0 0 1 1.17 10.25V7.75L3.2 4.15Q3.65 3.35 4.6 3.35Z')
shape('hard-drive',DRIVE,union(line((1.17,7.75),(14.83,7.75)),circle(11.75,10.2,.72)))
# SF places the externaldrive badge at the lower leading corner.
for name,kind,tags in [('hard-drive-plus','plus','storage disk drive add mount'),
                       ('hard-drive-check','check','storage disk drive verified healthy'),
                       ('hard-drive-x','x','storage disk drive error disconnect')]:
    badged_copy(name,'hard-drive',kind,cx=4.15,cy=11.85,tags=tags)
# SF battery: wide body (15.4 x 8.7 scaled), squircle corners, small nub;
# the charge is an inset pill that grows from the left.
BATTERY = rr(1.17,4.38,11.86,7.24,2.0,exact=True)
battery_nub = rr(13.85,6.55,.85,2.9,.42,exact=True)
def battery_level(width):
    return rr(2.55,5.76,width,4.48,1.05,exact=True) if width else po.Path()
shape('battery',BATTERY,union(battery_level(6.6),battery_nub))
shape('battery-charging',BATTERY,union(poly([(7.95,4.95),(4.55,8.55),(7.2,8.55),(6.55,11.05),(9.95,7.45),(7.3,7.45)]),battery_nub))
glyph('wifi',stroke('M1 5Q8-1 15 5M3.5 8Q8 4 12.5 8M6 11Q8 9 10 11'),circle(8,13,1))
glyph('bluetooth',stroke('M7.55 1.3V14.7L10.9 11.35L3.55 4'),
      stroke('M7.55 1.3L10.9 4.65L3.55 12'))
shape('network',union(rr(5.5,1,5,4,1),rr(1,11,5,4,1),rr(10,11,5,4,1)),stroke('M8 5V8H3.5V11M8 8H12.5V11'))
shape('git-branch',union(circle(4,3,1.5),circle(4,13,1.5),circle(12,3,1.5)),stroke('M4 4.5V11.5M12 4.5V5Q12 9 4 9',1.25))
shape('git-merge',union(circle(3.5,3,1.5),circle(3.5,13,1.5),circle(12.5,3,1.5)),stroke('M3.5 4.5V11.5M12.5 4.5V5Q12.5 8.5 6.5 8.5M8.5 6.5L6.5 8.5 8.5 10.5',1.2))
shape('git-pull-request',union(circle(4,3,1.5),circle(4,13,1.5),circle(12,13,1.5)),stroke('M4 4.5V11.5M12 11.5V6Q12 3 9 3M10 1L8 3 10 5',1.25))
shape('git-commit',circle(8,8,3),lines('M1 8H5','M11 8H15'))
# SF ladybug: a round shell under a domed head, a parting seam, two spots
# per wing and three short legs per side.
bug_leg = lines('M3.85 7.35L2.25 6.45','M3.5 9.75H1.65','M3.85 12.05L2.25 12.95')
shape('bug',union(circle(8,9.55,4.45),path('M5.35 5.6A2.65 2.65 0 0 1 10.65 5.6Z')),
      union(line((8,6.45),(8,12.4)),dots((5.95,8.35),(10.05,8.35),(6.05,11.35),(9.95,11.35),r=.62),
            bug_leg,mirror(bug_leg)))
shape('bot',rr(2,4,12,10,3),union(line((8,1),(8,4)),dots((5.5,8),(10.5,8),r=1),line((6,11),(10,11))))
agent_back = rr(1.45,2.6,8.6,7.5)
agent_front = rr(5.3,6.1,9.1,8)
agent_face = union(dots((7.8,9.1),(11.9,9.1),r=.6),line((8.4,11.65),(11.3,11.65)))
antenna = line((5.75,1.35),(5.75,2.6))
shape('agents',union(agent_back,agent_front),union(stroke(agent_front),agent_face,antenna))
shape('brain',path('M8 3C4-1 1 3 2 6C-1 8 1 12 4 12C4 16 8 15 8 13C8 15 12 16 12 12C15 12 17 8 14 6C15 3 12-1 8 3Z'),stroke('M8 3V13M4 5Q4 7 6 7M12 9Q10 9 10 11'))
# SF puzzlepiece.extension: a soft square with a knob out to the right
# and a matching socket in the left edge.
def puzzle_piece(body, knobs=(), sockets=()):
    # knobs: (circle, neck) pairs joined to the body; sockets: circles removed.
    for knob in knobs: body = union(body, *knob)
    for socket in sockets: body = op(body, socket, po.PathOp.DIFFERENCE)
    return close_joins(body,.5)
shape('extension',puzzle_piece(rr(1.55,2.85,10.5,10.3,1.6,exact=True),
      [(circle(13.2,8,1.55),rr(11.5,7.0,1.8,2.0,0))],[circle(1.55,8,1.55)]))
wrench = path('M12.3 1.8L9.55 4.65L11.5 6.6L14.35 3.8C15.7 7.05 13.3 10.2 10.1 9.5'
              'L5.25 14.05C3.1 15.95 .65 13.1 2.3 11.4L7.15 6.55C6.45 3.15 9.25 .85 12.3 1.8Z')
shape('wrench',wrench,circle(3.9,12.55,.75))
GEAR_TOOTH=path('M8 8L6.201388 3.657766Q6.75 3.45 6.75 2.95V1.7Q6.75 1.25 7.2 1.25H8.8Q9.25 1.25 9.25 1.7V2.95Q9.25 3.45 9.798612 3.657766Z')
GEAR=union(*(transform(GEAR_TOOTH,i*45) for i in range(8)))
shape('settings',op(GEAR,circle(8,8,2.4),po.PathOp.DIFFERENCE))
glyph('power',stroke('M4.1 3.8A5.8 5.8 0 1 0 11.9 3.8'),line((8,1.5),(8,7.5)))
glyph('spinner',stroke('M13 11A5.8 5.8 0 1 1 8 2.2',1.35),stroke('M8 2.2A5.8 5.8 0 0 1 13.8 8',1.35))
# SF gauge.with.dots.needle: the family circle, a 270 degree arc of
# dots and a tapered needle on a round hub.
gauge_dots = dots(*[(8+4.45*math.sin(math.radians(a)),8-4.45*math.cos(math.radians(a))) for a in range(-120,121,40)],r=.52)
gauge_needle = union(circle(8,8,.95),poly([(7.2,8.35),(7.75,4.35),(8.25,4.35),(8.8,8.35)]))
for name,n in [('gauge-low',-120),('gauge-medium',0),('gauge-high',60),('gauge-max',120)]:
    shape(name,circle(),union(gauge_dots,transform(gauge_needle,n)))
shape('logs',WINDOW,union(dots((4,5),(4,8),(4,11),r=.5),lines('M6 5H12','M6 8H10','M6 11H11')))
shape('diff',rr(1.5,2,13,12,2),union(plus(8,5,.7),line((6,11),(10,11))))
glyph('fold-vertical',lines('M2 8H14'),lines('M5 2l3 3 3-3','M5 14l3-3 3 3'))
# SF cursorarrow: narrow (7.3 x 12.9) with a vertical leading edge.
shape('cursor',path('M4.6 2.0L11.55 9.55L8.55 9.6L10.1 13.1L8.6 13.75L7.05 10.25L4.6 12.55Z'))
shape('themes',circle(),path('M8 2A6 6 0 0 1 8 14Z'))
# SF lightbulb: a narrow bulb (8.6 x 14.9) over two stacked base bands.
BULB = path('M5.85 10.45C5.85 8.75 4.2 7.85 4.2 5.4A3.8 3.8 0 0 1 11.8 5.4C11.8 7.85 10.15 8.75 10.15 10.45Z')
BULB_BASE = lines('M5.85 12.3H10.15','M6.75 14.1H9.25')
shape('lightbulb',BULB,BULB_BASE)
STAR=path('M8 1.5L10 5.7 14.5 6.3 11.2 9.5 12 14 8 11.8 4 14 4.8 9.5 1.5 6.3 6 5.7Z')
shape('star',STAR)
def sparkle(x,y,r):
    shoulder = .18*r
    return path(f'M{x} {y-r}Q{x+shoulder} {y-shoulder} {x+r} {y}'
                f'Q{x+shoulder} {y+shoulder} {x} {y+r}Q{x-shoulder} {y+shoulder} {x-r} {y}'
                f'Q{x-shoulder} {y-shoulder} {x} {y-r}Z')

# SF sparkles: one dominant star with two smaller companions above.
shape('sparkles',union(sparkle(9.55,9.85,4.85),sparkle(3.95,6.55,2.6),sparkle(7.0,2.2,1.6)))
# SF bolt: narrow and tall (9.0 x 14.3) with a softened zig-zag.
BOLT = path('M10.0 1.55L4.0 9.15H7.75L6.15 14.45L12.0 6.85H8.25Z')
shape('zap',BOLT)
for name,kind,tags in [('zap-check','check','lightning bolt power energy ready charged'),
                       ('zap-x','x','lightning bolt power energy error unavailable')]:
    badged_copy(name,'zap',kind,cx=11.6,cy=11.85,r=3.1,tags=tags)

CATEGORY='Charts and analytics'
# SF chart.bar.xaxis: solid columns standing on a baseline.
chart_columns = union(*(rr(x,y,2.7,11.85-y,.75,exact=True) for x,y in ((2.85,7.1),(6.65,2.6),(10.45,5.0))))
glyph('chart-bar',line((1.95,13.25),(14.05,13.25)),chart_columns)
for name,detail in [('chart-line',line((3,11),(6,7),(9,9),(13,4))),('chart-area',poly([(4.55,11.5),(4.55,9.3),(6.8,6.1),(9.1,7.8),(13.45,3.4),(13.45,11.5)])),('trending-up',lines('M2 12L6 8 9 10 14 3','M10 3H14V7')),('trending-down',lines('M2 4L6 8 9 6 13 11.5','M9 11.5H13V7.5'))]: glyph(name,lines('M2 2V14H14'),detail)
pie = path('M7 2A5.9 5.9 0 1 0 14 9H7Z')
quarter = path('M9.3 1.7A6 6 0 0 1 14.3 6.7H9.3Z')
shape('chart-pie', union(pie, quarter))
shape('chart-donut',ring(8,8,6,2.5),path('M8 2A6 6 0 0 1 14 8H10.5A2.5 2.5 0 0 0 8 5.5Z'))
glyph('activity',line((1.5,8.4),(4.7,8.4),(6.85,2.8),(9.15,13.2),(11.25,8.4),(14.5,8.4)),None)
shape('workflow',union(poly([(8,1),(11,4),(8,7),(5,4)]),rr(1,11,5,4,1),rr(10,11,5,4,1)),stroke('M8 7V9H3.5V11M8 9H12.5V11'))
compare_end = union(ring(3.45,12.25,2.05,1.1),
                    stroke('M3.45 10.25V5.6Q3.45 3.65 5.45 3.65H7.2M5.3 1.75L7.2 3.65L5.3 5.55',1.25))
glyph('git-compare',compare_end,transform(compare_end,180))

CATEGORY='Finance and commerce'
# SF creditcard: magnetic stripe band and a small chip, 14.7 x 10.6.
card = rr(1.17,3.22,13.66,9.56,1.5,exact=True)
card_stripe = op(rr(.5,5.6,15,1.5,0),union(card,stroke(card)),po.PathOp.INTERSECTION)
shape('credit-card',card,union(card_stripe,rr(3.25,9.2,3.0,1.6,.55,exact=True)))
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
# SF bag: a soft square body (11.4 x 12.9) under an arched handle; the
# badged variants carry SF's disc badge at the lower leading corner.
bag = rr(2.82,4.6,10.36,9.2,2.0,exact=True)
handle = stroke('M5.65 4.6V4.05A2.35 2.35 0 0 1 10.35 4.05V4.6')
shape('shopping-bag',bag,handle)
for name,kind,tags in [('shopping-bag-plus','plus','shopping bag retail purchase add item'),
                       ('shopping-bag-minus','minus','shopping bag retail remove item')]:
    badged_copy(name,'shopping-bag',kind,cx=4.15,cy=11.85,tags=tags)
shape('shopping-cart',path('M3 4H15L13 10H5Z'),union(stroke('M1 1.5H2.5L5 10'),circle(6,13.5,1.2),circle(12,13.5,1.2)))
shape('basket',path('M1.65 6.35H14.35L12.65 13.6H3.35Z'),
      lines('M4.05 6.35L7.4 2.7Q8 2 8.6 2.7L11.95 6.35', 'M6.1 8.85V11.15', 'M9.9 8.85V11.15'))
AWNING=path('M3 2H13L14.5 6Q14.5 8 12.3 8Q10.2 8 10.2 6Q10.2 8 8 8Q5.8 8 5.8 6Q5.8 8 3.7 8Q1.5 8 1.5 6Z')
shape('store',union(rr(2.5,6,11,8.5,1),AWNING),union(stroke(AWNING,1.1),stroke('M6.3 14V10H9.7V14',1.1),lines('M6.5 2L5.8 6','M9.5 2L10.2 6')))
# SF tag: the eyelet end at the upper right, the body running down-left.
shape('tag',mirror(path('M2.1 3.6Q2.1 2.1 3.6 2.1H7.55Q8.2 2.1 8.65 2.55L13.95 7.85Q14.95 8.85 13.95 9.85L9.85 13.95Q8.85 14.95 7.85 13.95L2.55 8.65Q2.1 8.2 2.1 7.55Z')),
      circle(10.9,5.1,1.0))
shape('gift',rr(2,6,12,8,1),union(stroke('M8 6V14M1 6H15V9H1ZM8 6C1 6 3 0 6 2L8 6C15 6 13 0 10 2Z',1.2)))
package_field = path('M1.65 4.75L8 1.65L14.35 4.75V11.45L8 14.4L1.65 11.45Z')
package_lid = path('M1.65 4.75L8 1.65L14.35 4.75L8 8.05Z')
tape = op(line((4.75,3.2),(11.2,6.4)),package_lid,po.PathOp.INTERSECTION)
shape('package',package_field,union(tape,stroke('M1.65 4.75L8 8.05L14.35 4.75M8 8.05V14.4')))
# SF barcode: bare bars of mixed widths on a common baseline.
barcode_bars = union(lines('M2.3 3.6V12.4','M4.6 3.6V12.4','M8.65 3.6V12.4','M13.7 3.6V12.4'),
                     rr(5.95,3.08,1.6,9.84,.5,exact=True),rr(10.0,3.08,2.4,9.84,.5,exact=True))
glyph('barcode',barcode_bars,None)
shape('percent',circle(),union(line((5.55,10.9),(10.45,5.1),width=1.25),circle(5.7,5.7,.9),circle(10.3,10.3,.9)))
shape('dollar', circle(), stroke('M10.3 5.55C8.3 4.2 5.6 4.95 5.6 6.45'
                                'C5.6 8.45 10.4 7.65 10.4 9.7C10.4 11.35 7.55 12 5.55 10.55M8 3.95V12.05'))
shape('euro', circle(), stroke('M10.55 5.05C7.8 3.45 6.1 5.35 6.1 8C6.1 10.8 7.9 12.5 10.55 10.95M4.85 6.85H9.05M4.85 9.15H8.7', 1.2))
shape('pound', circle(), stroke('M5.55 11.15H10.6M5.3 8.15H9.25M6.6 11.15V6.65Q6.6 3.65 9.95 4.95', 1.2))

CATEGORY='Work and education'
# SF briefcase: wide case, top handle, a waist seam broken by a small clasp.
briefcase_clasp = rr(6.75,7.75,2.5,2.2,.6,exact=True)
shape('briefcase',rr(1.17,4.5,13.66,9.15,1.9,exact=True),union(stroke('M5.6 4.5V3.35Q5.6 2.35 6.6 2.35H9.4Q10.4 2.35 10.4 3.35V4.5'),
      op(line((1.17,8.85),(14.83,8.85)),rr(6.2,7.2,3.6,3.3,0),po.PathOp.DIFFERENCE),stroke(briefcase_clasp)))
# SF building: a tall block with a regular grid of small square windows
# and a door at the base.
building = rr(3.2,1.75,9.6,12.5,1.2,exact=True)
windows = union(*(rr(x-.65,y-.65,1.3,1.3,.3,exact=True) for x in (5.65,8,10.35) for y in (3.85,6.35,8.85)))
shape('building',building,union(windows,stroke('M6.7 14.25V11.95Q6.7 11.45 7.2 11.45H8.8Q9.3 11.45 9.3 11.95V14.25')))
# SF building.columns: pediment, four columns, a plinth and its step.
shape('landmark',poly([(8,1.5),(14.45,5.3),(1.55,5.3)]),
      lines('M3.85 7.05V11.95','M6.6 7.05V11.95','M9.4 7.05V11.95','M12.15 7.05V11.95','M2.5 11.95H13.5','M1.55 14.0H14.45'))
shape('presentation',rr(1.5,2,13,9,1),lines('M8 11V15','M5 15L8 12 11 15','M4 8L7 5 9 7 12 4'))
shape('book',rr(3,1.7,10,12.6),
      lines('M5.6 1.8V11.4','M13 11.4H5.3Q3.1 11.4 3.1 13','M7.9 5.55H10.85'))
shape('book-open',path('M8 3Q4 1 1.5 2V13Q4 12 8 14Q12 12 14.5 13V2Q12 1 8 3Z'),line((8,3),(8,14)))
shape('graduation-cap',path('M1 6L8 2 15 6 8 10Z'),stroke('M4 8V11Q8 15 12 11V8M15 6V11'))
# SF rosette: a plain medallion over a notched ribbon.
award_disc = circle(8,6.1,4.6)
shape('award',union(award_disc,path('M5.15 9.3V14.35L8 12.75L10.85 14.35V9.3Z')),stroke(award_disc))
shape('medal',circle(8,10,4.5),union(path('M3 1H6L8 5 10 1H13L10 6H6Z'),circle(8,10,1.5)))
# SF lightbulb.max: a smaller bulb inside five short rays.
bulb_on = lambda p: transform(p,scale=.8,dy=1.55)
bulb_rays = union(*(line((8+4.6*math.sin(math.radians(a)),7.5-4.6*math.cos(math.radians(a))),
                         (8+6.15*math.sin(math.radians(a)),7.5-6.15*math.cos(math.radians(a)))) for a in (-90,-45,0,45,90)))
shape('lightbulb-on',bulb_on(BULB),union(bulb_on(BULB_BASE),bulb_rays))
shape('flask',path('M5 1H11V3H10V7L14 13Q15 15 12 15H4Q1 15 2 13L6 7V3H5Z'),union(line((5,10),(11,10)),dots((7,12),(10,13),r=.5)))
shape('test-tube',path('M4.5 1.5H11.5V10.5A3.5 3.5 0 0 1 4.5 10.5Z'),lines('M3.5 1.5H12.5','M4.5 8H11.5','M9 4.5H11'))
# SF atom: three equal orbits at 60 degrees around a solid nucleus.
orbit = stroke('M8 1.65A2.55 6.35 0 1 0 8 14.35A2.55 6.35 0 1 0 8 1.65Z')
glyph('atom',union(orbit,transform(orbit,60),transform(orbit,-60)),circle(8,8,1.0))
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
# SF cross: the outlined Greek cross itself, arms a third of its span.
shape('medical-cross',close_joins(union(rr(5.85,1.7,4.3,12.6,1.3,exact=True),rr(1.7,5.85,12.6,4.3,1.3,exact=True)),.45))
shape('first-aid',rr(1.5,4,13,10,2),union(plus(8,9,1),stroke('M5 4V1.5H11V4')))
capsule = path('M4.65 5A3.35 3.35 0 0 1 11.35 5V11A3.35 3.35 0 0 1 4.65 11Z')
capsule_seam = op(line((4.65,8),(11.35,8)),capsule,po.PathOp.INTERSECTION)
shape('pill',transform(capsule,42),transform(capsule_seam,42))
glyph('stethoscope',stroke('M2 2V6A4 4 0 0 0 10 6V2M2 2H3M9 2H10'),union(ring(13,8.5,1.6,1.1),stroke('M6 10V11.5Q6 14.5 9.5 14.5T13 11.5V10')))
# SF thermometer.medium: slim tube on a round bulb, scale ticks at the side.
shape('thermometer',path('M5.85 3.1A1.6 1.6 0 0 1 9.05 3.1V9.15A3.05 3.05 0 1 1 5.85 9.15Z'),
      union(line((7.45,6.4),(7.45,11.6)),circle(7.45,11.6,1.45),lines('M11.0 3.3H12.45','M11.0 5.35H12.45','M11.0 7.4H12.45')))
# SF bandage: a diagonal capsule with an outlined pad holding four dots.
shape('bandage',transform(rr(.6,4.6,14.8,6.8,3.4,exact=True),-45),
      transform(union(stroke(rr(5.4,4.6,5.2,6.8,0)),dots((7,7.2),(9,7.2),(7,8.8),(9,8.8),r=.55)),-45))
hospital_field = path('M1.55 7.4H4.2V1.7H11.8V7.4H14.45V14.2H1.55Z')
shape('hospital',hospital_field,union(plus(8,5.1,.72),stroke('M6.45 14.2V10.2H9.55V14.2')))
# SF dumbbell: horizontal, a tall inner plate and a short outer plate per side.
inner_plate = rr(3.55,4.1,2.4,7.8,1.2,exact=True)
outer_plate = rr(1.17,5.75,2.38,4.5,1.0,exact=True)
weight_plates = union(inner_plate,outer_plate)
shape('dumbbell',union(weight_plates,mirror(weight_plates)),
      union(line((5.95,8),(10.05,8)),stroke(inner_plate),mirror(stroke(inner_plate))))
# Solid: filled plates, the outer plate parted from the inner by a gap.
inner_fill = union(inner_plate,stroke(inner_plate),mirror(union(inner_plate,stroke(inner_plate))))
outer_fill = union(outer_plate,stroke(outer_plate),mirror(union(outer_plate,stroke(outer_plate))))
STYLE_OVERRIDES['dumbbell'] = {'solid':union(op(outer_fill,union(inner_fill,stroke(inner_fill,1.7,exact=True)),po.PathOp.DIFFERENCE),
                                            inner_fill,line((5.95,8),(10.05,8)))}
shape('weight',path('M5 6.5H11L14 13Q14.6 14.5 12.5 14.5H3.5Q1.4 14.5 2 13Z'),stroke('M5.5 6.5V4A2.5 2.5 0 0 1 10.5 4V6.5'))
forefoot = path('M5.65 10.1H2.25C1.65 8.85 1.4 7.15 1.7 5.6'
                'C2.15 3.4 4.6 2.7 6 4.2C7.4 5.65 6.9 7.2 6.2 8.55Z')
heel = path('M2.45 11.4H5.6L5.5 12.9C5.35 14.85 2.8 14.85 2.6 13.05Z')
footprint = transform(union(forefoot,heel),-12,dx=.55)
glyph('footprints',footprint,transform(mirror(footprint),dy=-2.65))
# SF bed.double: a headboard holding two pillows over a full-width
# mattress with its seam, standing on short legs.
headboard = rr(2.45,3.05,11.1,6.0,1.5,exact=True)
mattress = rr(1.17,7.75,13.66,4.1,1.1,exact=True)
pillows = union(rr(4.0,5.0,3.3,1.75,.75,exact=True), rr(8.7,5.0,3.3,1.75,.75,exact=True))
shape('bed', union(headboard,mattress), union(pillows, stroke(op(mattress,rr(0,0,16,7.6,0),po.PathOp.DIFFERENCE)),
      line((1.17,9.85),(14.83,9.85)), lines('M2.45 11.85V13.15','M13.55 11.85V13.15')))
# SF moon: a slimmer crescent, the inner arc nearly as large as the outer.
shape('moon',path('M7.9 1.95A6.15 6.15 0 1 0 14.05 9.45A5.0 5.0 0 0 1 7.9 1.95Z'))
shape('apple',path('M8 5C1 1 0 9 4 13C5.5 15 6.5 13.5 8 13.5S10.5 15 12 13C16 9 15 1 8 5Z'),stroke('M8 5Q8 1 11 1'))
# SF drop: narrow (8.8 x 12.9) with no interior highlight.
shape('droplet',path('M8 1.85C6.95 3.95 4.1 6.6 4.1 9.95A3.9 3.9 0 0 0 11.9 9.95C11.9 6.6 9.05 3.95 8 1.85Z'))
lung_l = path('M5.65 4.6C4.05 4.55 2.55 7.6 1.85 11.5Q1.15 14.7 3.55 14'
              'L5.65 13Q6.6 12.55 6.55 10.9L6.35 5.55Q6.3 4.65 5.65 4.6Z')
airway = stroke('M8 1.55V5.55M5.15 8.85L8 5.55L10.85 8.85')
shape('lungs',union(lung_l,mirror(lung_l)),airway)

CATEGORY='Maps and travel'
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
# SF bus: tall rounded front, one large windshield, two lamps, short wheels.
shape('bus', rr(2.85,1.65,10.3,11.25,2.2,exact=True), union(
    stroke(rr(4.55,3.5,6.9,4.75,.9,exact=True)), lines('M4.75 12.9V14.45','M11.25 12.9V14.45'),
    dots((5.35,10.45),(10.65,10.45),r=.75)))
shape('train',rr(3,1,10,12,3),union(stroke('M3 6H13M8 1V6M5 13L3 15M11 13L13 15'),dots((5.5,9.5),(10.5,9.5),r=.8)))
glyph('bicycle',union(ring(3.8,11.05,2.95),ring(12.2,11.05,2.95)),
      lines('M3.8 11.05L6.15 6.1L8.1 9.05L10.95 5.4',
            'M6.15 6.1L5.6 4.25H3.95','M12.2 11.05L10.45 2.8H12.85'))
plane_body = path('M6.55 3.55Q6.55 1.35 8 1.35Q9.45 1.35 9.45 3.55V6.35'
                  'L14.55 9.45V11.55L9.35 9.65V12.05L11.1 13.95V14.35L8 13.45'
                  'L4.9 14.35V13.95L6.65 12.05V9.65L1.45 11.55V9.45L6.55 6.35Z')
shape('plane',plane_body)
hull = path('M1.65 8.6L8 6.55L14.35 8.6L12.45 11.55H3.55Z')
cabin = path('M4.3 7.7V3.65H11.7V7.7L8 6.55Z')
wave = stroke('M1.7 14.1Q3.25 12.85 4.85 14.1T8 14.1Q9.55 12.85 11.15 14.1T14.3 14.1')
shape('ship',union(hull,cabin),union(stroke('M1.65 8.6L8 6.55L14.35 8.6M8 3.65V6.55'),stroke('M6.9 3.65V1.65H9.1V3.65'),wave))
bridge_windows = path('M4.85 4.2H7.45V6.15L4.85 7ZM8.55 4.2H11.15V7L8.55 6.15Z')
bow_seam = line((2.6,8.8),(8,7.1),(13.4,8.8))
ship_body = DRAWINGS['ship'][0]
ship_shell = union(ship_body,stroke(ship_body),stroke('M6.9 3.65V1.65H9.1V3.65'))
STYLE_OVERRIDES['ship'] = {'solid':union(op(ship_shell,union(bridge_windows,bow_seam),po.PathOp.DIFFERENCE),wave)}
# SF suitcase: wide case with a top handle and two full-height straps.
shape('suitcase',rr(1.17,4.6,13.66,8.9,1.9,exact=True),stroke(
    'M5.75 4.6V3.4Q5.75 2.45 6.7 2.45H9.3Q10.25 2.45 10.25 3.4V4.6M4.45 4.6V13.5M11.55 4.6V13.5'))
ticket = path('M1.55 3H14.45V5.95C11.1 6.15 11.1 9.85 14.45 10.05V13H1.55'
              'V10.05C4.9 9.85 4.9 6.15 1.55 5.95Z')
shape('ticket',ticket,lines('M9.7 5.2V6.25','M9.7 9.75V10.8'))
# SF tent: a single soft triangle with the door opening as a smaller one.
tent_shell = poly([(8,2.5),(14.35,13.25),(1.65,13.25)])
shape('tent', tent_shell, union(stroke('M5.45 13.25L8 8.4L10.55 13.25'),line((8,1.4),(8,2.5))))
shape('mountain',poly([(1.45,13.8),(6.05,2.65),(9.3,8.45),(11.1,5.25),(14.55,13.8)]),
      stroke('M4.2 7.05L5.65 8.25L6.8 6.85L7.95 7.05'))
# SF signpost.right: a right-pointing board on a post with a foot.
shape('signpost',poly([(2.0,2.7),(11.55,2.7),(14.2,5.4),(11.55,8.1),(2.0,8.1)]),lines('M7.1 1.35V2.7','M7.1 8.1V13.55','M4.6 13.55H9.6'))
shape('parking',rr(),stroke('M6 12V4H9A2 2 0 0 1 9 8H6',1.5))
shape('fuel',rr(2,2,8,12,1),union(rr(4,4,4,4,.5),stroke('M10 6H12V12Q15 15 15 11V6L12 3')))

CATEGORY='Weather and nature'
shape('sun',circle(8,8,3.5),lines('M8 1V2','M8 14V15','M1 8H2','M14 8H15','M3 3l1 1','M12 12l1 1','M3 13l1-1','M12 4l1-1'))
shape('sunrise',path('M3 12A5 5 0 0 1 13 12Z'),lines('M1 12H15','M3 14.5H13','M8 1.3V4.8','M5.7 3.6L8 1.3 10.3 3.6','M1 8H2','M14 8H15'))
shape('sunset',path('M3 12A5 5 0 0 1 13 12Z'),lines('M1 12H15','M3 14.5H13','M8 1.3V4.8','M5.7 2.5L8 4.8 10.3 2.5','M1 8H2','M14 8H15'))
# SF weather clouds keep the full cloud width and sit high; marks fill the band below.
WEATHER_CLOUD = transform(CLOUD,dy=-2.55).transform(1,0,0,.94,0,.04)
for name,detail in [('cloud-rain',lines('M4.95 11.25L4.15 13.95','M8.4 11.25L7.6 13.95','M11.85 11.25L11.05 13.95')),
                    ('cloud-snow',dots((4.6,11.55),(8,11.55),(11.4,11.55),(6.3,14.0),(9.7,14.0),r=.78)),
                    ('cloud-fog',lines('M3.3 11.55H12.7','M4.85 14.0H11.15')),
                    ('cloud-lightning',soften(transform(BOLT,scale=.38,dx=.1,dy=4.72),.12))]:
    shape(name,WEATHER_CLOUD,detail)
# SF snowflake: three full axes, one open fork near each tip, no hub.
snow_axis = line((8, 1.6), (8, 14.4))
snow_fork = line((6.15, 2.5), (8, 4.35), (9.85, 2.5))
glyph('snowflake', union(*(transform(snow_axis, i*60) for i in range(3))),
      union(*(transform(snow_fork, i*60) for i in range(6))))
glyph('wind',stroke('M1 5H10Q14 5 13 2Q12 0 10 2M1 8H13Q16 8 15 11Q14 13 12 11'),stroke('M2 11H7Q10 11 9 14Q8 16 6 14'))
canopy = path('M1.55 8.65A6.45 6.45 0 0 1 14.45 8.65Q12.25 6.9 10.15 8.65'
              'Q8 6.9 5.85 8.65Q3.75 6.9 1.55 8.65Z')
umbrella_handle = stroke('M8 7.9V12.4C8 14.85 11.75 14.85 11.75 12.4')
shape('umbrella',canopy,union(umbrella_handle,line((8,1.35),(8,2.2))))
STYLE_OVERRIDES['umbrella'] = {'solid':union(canopy,stroke(canopy),umbrella_handle,line((8,1.35),(8,2.2)))}
# SF rainbow: three wide concentric bands with short straight feet.
glyph('rainbow',stroke('M1.17 12.0V10.9A6.83 6.83 0 0 1 14.83 10.9V12.0'),
      stroke('M3.4 12.0V10.9A4.6 4.6 0 0 1 12.6 10.9V12.0M5.63 12.0V10.9A2.37 2.37 0 0 1 10.37 10.9V12.0'))
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
ember = path('M7.35 8.05C7.05 9.3 5.85 9.85 5.85 10.9C5.85 12.8 9.4 12.8 9.4 10.9Q9.4 9.75 7.35 8.05Z')
shape('flame', flame, stroke(ember))
RECYCLE_ARM=stroke('M5 4L7 1.7Q8 1 8.7 2.2L11 6M8 5.3L11 6 11.5 3',1.15)
glyph('recycle',union(RECYCLE_ARM,transform(RECYCLE_ARM,120)),transform(RECYCLE_ARM,240))
# SF pawprint: outlined oval toes fanned over a soft triangular pad.
def paw_toe(x,y,angle): return transform(circle(8,8,1).transform(1.3,0,0,1.75,8-8*1.3,8-8*1.75),angle,dx=x-8,dy=y-8)
paw_pad = path('M8 8.05C10.15 8.05 12.55 10.85 12.55 12.6C12.55 14.45 10.55 14.5 8 13.85C5.45 14.5 3.45 14.45 3.45 12.6C3.45 10.85 5.85 8.05 8 8.05Z')
shape('paw',union(paw_pad,paw_toe(2.75,6.85,-28),paw_toe(5.9,3.55,-9),paw_toe(10.1,3.55,9),paw_toe(13.25,6.85,28)))
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
# SF wineglass: a round bowl with a flat rim, slender stem and oval foot.
wine_bowl = path('M4.75 1.75H11.25Q12.1 4.6 12.1 6.3A4.1 4.1 0 0 1 3.9 6.3Q3.9 4.6 4.75 1.75Z')
shape('wine',wine_bowl,union(line((8,10.4),(8,13.6)),stroke('M5.35 13.85Q8 12.95 10.65 13.85'),line((4.3,5.05),(11.7,5.05))))
shape('bottle',path('M6 1H10V5L12 8V14H4V8L6 5Z'),lines('M6 3H10','M4 10H12'))
shape('chef-hat',path('M4 9C-1 9 0 3 4 3Q8-2 12 3C16 3 17 9 12 9V14H4Z'),stroke('M4 11H12M7 8V10M10 7V10'))
# SF sofa: wide and low (16 x 11.2 scaled): back cushions, two arms, seat.
sofa_arm = rr(1.17,6.05,2.95,5.55,1.35,exact=True)
sofa_back = rr(2.9,3.25,10.2,5.4,1.6,exact=True)
sofa_seat = rr(2.6,8.4,10.8,3.2,0)
sofa_body = union(sofa_back, sofa_arm, mirror(sofa_arm), sofa_seat)
sofa_seam = union(stroke(sofa_arm), mirror(stroke(sofa_arm)), line((4.12,8.65),(11.88,8.65)))
shape('sofa', sofa_body, union(sofa_seam, line((8,3.25),(8,8.65)), lines('M2.75 11.6V12.85','M13.25 11.6V12.85')))
# Solid: filled arms parted from back and seat by the family gap.
sofa_arms = union(sofa_arm,stroke(sofa_arm),mirror(union(sofa_arm,stroke(sofa_arm))))
sofa_rest = op(union(sofa_back,stroke(sofa_back),sofa_seat,stroke(sofa_seat)),
               union(sofa_arms,stroke(sofa_arms,1.8,exact=True)),po.PathOp.DIFFERENCE)
STYLE_OVERRIDES['sofa'] = {'solid':union(op(sofa_rest,union(line((3,8.65),(13,8.65)),line((8,3.25),(8,8.65))),po.PathOp.DIFFERENCE),sofa_arms,lines('M2.75 11.6V12.85','M13.25 11.6V12.85'))}
shape('lamp',path('M5 2H11L14 9H2Z'),lines('M8 9V14','M5 14H11'))
shape('door-open',path('M3 3L11 1V15L3 13Z'),union(stroke('M11 3H14V13H11'),circle(8.5,8,.65)))
key_head = circle(5.35,5.4,3.5)
key_bit = path('M6.7 8.15L8.15 6.7L14.3 12.85V14.2H11.15V11.95H8.95V10.2Z')
shape('key-round', union(key_head,key_bit), stroke(circle(5.15,5.2,1.5)))
shape('plug',rr(4,5,8,5,2),stroke('M5.5 1V5M10.5 1V5M8 10V15'))
fan_blade = path('M7.25 8.35C6.2 7.5 5.3 5.4 6.15 4.45C7.3 3.1 9.85 3.75 9.35 5.4Q9.05 6.55 8.35 8.4Z')
fan_blades = union(*(transform(fan_blade,i*120) for i in range(3)),circle(8,8,1.05))
shape('fan',circle(),fan_blades)
shape('gamepad',path('M4 4H12Q14 4 15 11Q16 15 12 13L10 11H6L4 13Q0 15 1 11Q2 4 4 4Z'),union(plus(5,8,.65),dots((10.5,7),(12.5,9),r=.7)))
# SF puzzlepiece: knobs out on the top and right edges.
shape('puzzle',puzzle_piece(rr(1.55,4.1,10.5,10.3,1.6,exact=True),
      [(circle(6.8,2.75,1.55),rr(5.8,3.0,2.0,1.6,0)),(circle(13.2,9.25,1.55),rr(11.5,8.25,1.8,2.0,0))]))
# SF music.note: one stem, one sloped flag and an oval head.
glyph('music-note',union(notehead(6.05,12.15),poly([(7.75,1.75),(11.75,2.95),(11.75,5.55),(7.75,4.35)])),line((7.75,2.3),(7.75,12.0)))
# SF bell.and.waves.left.and.right: the family bell, smaller, between two
# pairs of sound arcs.
bell_small = lambda p: transform(p,scale=.74,dy=.2)
bell_waves = stroke('M2.35 4.7Q.9 8.0 2.35 11.3')
shape('bell-ring',bell_small(BELL),union(bell_small(union(line((6,14),(10,14)),line((8,1),(8,2)))),bell_waves,mirror(bell_waves)))

CATEGORY='Editing and design'
clip_wire = path('M9.55 4.55V10.4A1.35 1.35 0 0 1 6.85 10.4V4.5A2.55 2.55 0 0 1 11.95 4.5V10.4'
                 'A3.75 3.75 0 0 1 4.45 10.4V4.4')
glyph('paperclip',stroke(transform(clip_wire,38)),po.Path())
CATEGORY='Technology and development'
# The console prompt followed by a remote (outgoing) arrow.
shape('ssh', CONSOLE, union(lines('M3.75 5.55L5.6 7.1L3.75 8.65'),
      union(line((7.6,10.2),(11.6,6.2)),line((8.75,6.2),(11.6,6.2),(11.6,9.05)))))
CATEGORY='Actions and status'
# arrow.clockwise.circle: the refresh arrow at about half the dial.
shape('refresh-circle-fill', circle(), union(stroke('M11.0 8.4A3.0 3.0 0 1 1 8 5.6H8.95'),line((7.35,4.05),(8.95,5.6),(7.35,7.15))))

CATEGORY='Actions and status'
# SF line.3.horizontal: 13 x 6.5 u.
glyph('menu',lines('M2.0 4.73H14.0','M2.0 11.27H14.0'),line((2.0,8),(14.0,8)))
CATEGORY='Technology and development'
for name,level in [('battery-full',9.1),('battery-low',2.3),('battery-empty',0)]:
    shape(name,BATTERY,union(battery_level(level),battery_nub))
glyph('wifi-off',DRAWINGS['wifi'][0],union(DRAWINGS['wifi'][1],line((2,2),(14,14))))
DRAWINGS['bluetooth-off'] = DRAWINGS['bluetooth']
shape('cloud-off',DRAWINGS['cloud'][0],line((2,2),(14,14)))
shape('git-fork',union(circle(3,3,1.7),circle(13,3,1.7),circle(8,13,1.7)),stroke('M3 5V6Q3 8 8 8Q13 8 13 6V5M8 8V11'))
CATEGORY='Communication'
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

def solid_body(body, rim, detail):
    field = union(body,rim)
    interior = op(field,stroke(field,1.8),po.PathOp.DIFFERENCE)
    structure, counters = [], []
    for part in components(detail):
        exterior = op(part,field,po.PathOp.DIFFERENCE)
        (structure if exterior.area > part.area*.12 else counters).append(part)
    cut = op(union(*counters),interior,po.PathOp.INTERSECTION)
    return union(op(field,cut,po.PathOp.DIFFERENCE),*structure)

def corner_mark(name, body, detail, mark, clearance, *, return_edge=False):
    # Compose the base first, so occlusion preserves counters in each style.
    shape(name,body,union(detail,mark))
    rim = stroke(body)
    host = union(rim,detail)
    ink = op(host,clearance,po.PathOp.DIFFERENCE)
    if return_edge:
        ink = union(ink,stroke(op(body,clearance,po.PathOp.DIFFERENCE)))
    ink = union(ink,mark)
    surface = op(body,union(ink,clearance),po.PathOp.DIFFERENCE)
    solid = solid_body(body,rim,detail)
    STYLE_OVERRIDES[name] = {'duotone':[(surface,.24),(ink,1)],'stroke':ink,
                             'solid':union(op(solid,clearance,po.PathOp.DIFFERENCE),mark)}

CATEGORY='Media'
CATEGORY='Security'
shape('scan-face',rr(3.8,3.8,8.4,8.4),union(
    lines('M1.5 4.8V1.5H4.8','M11.2 1.5H14.5V4.8','M1.5 11.2V14.5H4.8',
          'M11.2 14.5H14.5V11.2','M6.15 9.1Q8 10.55 9.85 9.1'),
    dots((6.25,6.5),(9.75,6.5),r=.55)))
CATEGORY='Editing and design'
# SF textformat.size: a small and a large letter on one baseline.
glyph('text-size',union(line((1.5,12.6),(4.0,7.0),(6.5,12.6)),line((2.4,10.75),(5.6,10.75))),
      union(line((6.9,12.6),(10.75,3.4),(14.6,12.6)),line((8.35,9.4),(13.15,9.4))))
for name,mark in [('heading-1',stroke('M12 6L14 4V13')),('heading-2',stroke('M11 6Q11 3 14 4Q16 5 13 8L11 12H15'))]:
    glyph(name,lines('M2 3V13','M8 3V13','M2 8H8'),mark)
CATEGORY='Time and planning'
CATEGORY='Technology and development'
# SF icloud.and.arrow.*: the cloud rises and the arrow runs through its base,
# with the outline cut back by a clearance gap in every style.
cloud_high = transform(CLOUD,dy=-1.75)
for name,flip in [('cloud-download',False),('cloud-upload',True)]:
    mark = union(line((8,6.1),(8,14.55)),line((5.45,12.0),(8,14.55),(10.55,12.0)))
    if flip: mark = union(line((8,6.1),(8,14.55)),line((5.45,8.65),(8,6.1),(10.55,8.65)))
    corner_mark(name,cloud_high,po.Path(),mark,stroke(mark,2.75,exact=True))
CATEGORY='Finance and commerce'
shape('yen', circle(), lines('M5.2 4.6L8 7.65L10.8 4.6','M8 7.65V12',
                             'M5.65 7.65H10.35','M5.65 9.85H10.35'))

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
        elif name == 'layers':
            mono=union(stroke(b,1.25),stroke(d,1.25))
        elif name == 'qr-code':
            mono=union(outer,d)

        if outline:
            solid=solid_body(b,outer,d)
        else: solid=union(b,d)
        if name == 'chart-area':
            mono=union(b,stroke(d,1.05))
        if name == 'fan':
            vanes = union(*(transform(stroke(fan_blade),i*120) for i in range(3)))
            mono=union(outer,vanes,circle(8,8,1.3))

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
        if name == 'headphones':
            mono=union(b,stroke(d,1.1))
        if name == 'lungs':
            field=union(b,outer)
            solid=union(op(field,d,po.PathOp.DIFFERENCE),op(d,field,po.PathOp.DIFFERENCE))
        if name == 'printer':
            cuts=union(line((4.5,5.2),(11.5,5.2)),rr(5.05,10.45,5.9,3.1),circle(12,7.3,.55))
            solid=op(union(b,outer),cuts,po.PathOp.DIFFERENCE)
        if name == 'gift':
            # The ribbon joins an exterior bow; it must still cut through the box.
            solid=op(solid,stroke('M8 6V13.6M2.2 9H13.8',1.15),po.PathOp.DIFFERENCE)
        if name == 'construction':
            # Both hazard stripes remain counters, independently of the legs.
            field=union(b,outer)
            interior=op(field,stroke(field,1.8),po.PathOp.DIFFERENCE)
            solid=op(union(field,lines('M4 10V14','M12 10V14')),
                     op(lines('M4 5L7 10','M9 5L12 10'),interior,po.PathOp.INTERSECTION),po.PathOp.DIFFERENCE)
        if name == 'sofa':
            pass  # Solid composed with the recipe (STYLE_OVERRIDES['sofa']).
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
        if name == 'archive':
            solid=op(union(b,outer),d,po.PathOp.DIFFERENCE)
        if name == 'agents':
            solid=union(stacked_solid(agent_back,agent_front,agent_face),antenna)
        if name == 'folders':
            solid=stacked_solid(FOLDERS_BACK,FOLDERS_FRONT)
        if name == 'terminal-stack':
            solid=stacked_solid(transform(WINDOW,0,.8,-1,-1.5),transform(WINDOW,0,.8,1,1.5),lines('M6 8l2 2-2 2','M10 12H12'))
        if name == 'swatch':
            rear=op(SWATCH,union(SWATCH_DIAGONAL,stroke(SWATCH_DIAGONAL,1.8)),po.PathOp.DIFFERENCE)
            fan=union(rear,SWATCH_DIAGONAL)
            solid=union(op(fan,union(swatch_front,stroke(swatch_front,2.1)),po.PathOp.DIFFERENCE),
                        op(swatch_front,swatch_pivot,po.PathOp.DIFFERENCE))
        if name == 'store':
            scallops=stroke('M1.5 6Q1.5 8 3.7 8Q5.8 8 5.8 6Q5.8 8 8 8Q10.2 8 10.2 6Q10.2 8 12.3 8Q14.5 8 14.5 6')
            reveal=op(scallops,rr(2.05,5.4,11.9,3.6,0),po.PathOp.INTERSECTION)
            solid=op(union(b,outer),union(reveal,rr(6.3,10,3.4,5.5)),po.PathOp.DIFFERENCE)
        if name in {'camera-off','microphone-off','bell-off','cloud-off','bluetooth-off','wifi-off','eye-off','ear-off','volume-off'}:
            slash=line((2,2),(14,14))
            clearance=line((2,2),(14,14),width=3.2 if name in {'bluetooth-off','camera-off','eye-off'} else 2.65)
            duo=[(op(p,clearance,po.PathOp.DIFFERENCE),a) for p,a in duo]+[(slash,1)]
            mono=union(op(mono,clearance,po.PathOp.DIFFERENCE),slash)
            if name == 'eye-off':
                solid=op(union(b,outer),circle(8,8,3),po.PathOp.DIFFERENCE)
            solid=union(op(solid,clearance,po.PathOp.DIFFERENCE),slash)
        overrides=STYLE_OVERRIDES.get(name,{})
        duo=overrides.get('duotone',duo)
        solid=overrides.get('solid',solid)
        mono=overrides.get('stroke',mono)
        if name in BADGES:
            disc,clearance=BADGES[name]
            duo=[(op(p,clearance,po.PathOp.DIFFERENCE),a) for p,a in duo if p]
            opaque=[i for i,(p,a) in enumerate(duo) if a==1]
            if opaque: duo[opaque[-1]]=(union(duo[opaque[-1]][0],disc),1)
            else: duo.append((disc,1))
            solid=union(op(solid,clearance,po.PathOp.DIFFERENCE),disc)
            mono=union(op(mono,clearance,po.PathOp.DIFFERENCE),disc)
        two_tones=any(p and 0<alpha<1 for p,alpha in duo)
        write(Path('icons')/(name+'.svg'),svg(duo))
        for style,layers in {
            'solid':[(solid,1)],
            'stroke':[(mono,1)],
        }.items():
            write(Path('icons/styles')/style/(name+'.svg'),svg(layers))
        tags=' '.join([*tags.split(),*(t for t in KEPT_TAGS.get(name,()) if t not in tags.split())])
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
    import sf_home, sf_media, sf_accessibility, sf_interface
    import sf_ext_windows, sf_ext_text, sf_ext_states, sf_ext_objects, sf_ext_world
    for module in (design, product, technology, world, sf_home, sf_media, sf_accessibility, sf_interface,
                   sf_ext_windows, sf_ext_text, sf_ext_states, sf_ext_objects, sf_ext_world):
        module.register(globals())

if __name__=='__main__':
    register_full_catalog()
    main()
