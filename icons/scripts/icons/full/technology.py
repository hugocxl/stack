"""Original 16-unit technology, science, media and sport artwork.

Every recipe is authored for Icons. Shared constructions express actual
families; state marks have clearance and never borrow reference-library paths.
"""
import math
from pathlib import Path
import json

NAMES = tuple(row['lucide_name'] for row in json.loads(
    Path(__file__).with_name('technology-scope.json').read_text())) + (
    'play-triangle', 'pause-bars', 'video-camera', 'radio-signal',
    'volume-none', 'volume-slash',
)


def register(api):
    shape, glyph = api['shape'], api['glyph']
    path, rr, circle = api['path'], api['rr'], api['circle']
    line, lines, stroke = api['line'], api['lines'], api['stroke']
    union, poly, dots = api['union'], api['poly'], api['dots']
    plus, cross, check = api['plus'], api['cross'], api['check']
    transform, ring, op, po = api['transform'], api['ring'], api['op'], api['po']
    overrides = api.setdefault('STYLE_OVERRIDES', {})
    empty = path('')
    before = set(api['DRAWINGS'])

    def cut(a, b): return op(a, b, po.PathOp.DIFFERENCE)
    def G(n, a, b=None): glyph(n, a, b or empty, n.replace('-', ' '))
    def S(n, a, b=None): shape(n, a, b, n.replace('-', ' '))

    def arr(direction='up', x=8, y=8, s=1):
        centerline=path('M8 11V5M5.5 7.5L8 5L10.5 7.5')
        angle={'up':0,'right':90,'down':180,'left':270}[direction]
        return stroke(transform(centerline,angle,s,x-8,y-8))
    def play(x=8,y=8,s=1):
        return poly([(x-1.7*s,y-2.4*s),(x+2.2*s,y),(x-1.7*s,y+2.4*s)])
    def star(x=8,y=8,s=1): return transform(api['STAR'],scale=s,dx=x-8,dy=y-8)
    def cog(x=12,y=11.8):
        # Rotate six radial tooth centerlines around a shared circular hub.
        tooth = line((8,6.35),(8,5.45))
        teeth = union(*(transform(tooth,60*i) for i in range(6)))
        return transform(union(ring(8,8,2.2),teeth),dx=x-8,dy=y-8)
    def warn(x=8,y=8,s=1): return union(line((x,y-2*s),(x,y+.4*s)),circle(x,y+2.3*s,.6))
    def power(x=8,y=8,s=1):
        arc = transform(path('M4.65 4.45A4.8 4.8 0 1 0 11.35 4.45'),scale=s,dx=x-8,dy=y-8)
        return union(stroke(arc),line((x,y-5.7*s),(x,y-.6*s)))
    def fit_outline(body):
        # An inherited contour fitted with a scaled outline needs room for a
        # full 1.1-unit outline. Fit the unexpanded body around its own center.
        x0,y0,x1,y1 = body.bounds
        # Leave 0.005 per edge for the rounded Bézier stroke expansion.
        span = 14.69-api['STROKE']
        sx,sy = min(1,span/(x1-x0)),min(1,span/(y1-y0))
        return body.transform(sx,0,0,sy,(x0+x1)*(1-sx)/2,(y0+y1)*(1-sy)/2)

    def layers(n,b,d,body,source=None):
        # A modifier inherits the exact fitted paths of its base.
        if source:
            b,d,body,category,_ = api['DRAWINGS'][source]
            if source in ('mouse','flask'):
                b = fit_outline(b)
            api['DRAWINGS'][n] = (b,d,body,category,n.replace('-',' '))
        else:
            (S if body else G)(n,b,d)
            b,d = api['DRAWINGS'][n][:2]
        if not body:
            ink = union(b,d)
            solid,mono = ink,ink
            if source == 'headphones':
                mono = union(b,stroke(d))
            duo = [(ink,1)]
        else:
            outer=stroke(b); ink=union(outer,d); filled=union(b,outer)
            inset=cut(filled,stroke(filled,1.8))
            counters=[]; structural=[]
            for part in api['components'](d):
                (structural if cut(part,filled).area>part.area*.12 else counters).append(part)
            solid=union(cut(filled,op(union(*counters),inset,po.PathOp.INTERSECTION)),*structural)
            duo,mono = [(cut(b,ink),.24),(ink,1)],ink
        base_styles = overrides.get(source,{})
        return base_styles.get('duotone',duo),base_styles.get('solid',solid),base_styles.get('stroke',mono)

    def clear_mark(ink,gap,min_area):
        visible = cut(ink,gap)
        if min_area:
            visible = union(*(part for part in api['components'](visible) if part.area >= min_area))
        return visible

    def off(n,b=None,d=None,body=True,*,source=None,center=(8,8),min_area=0):
        duo,solid,mono=layers(n,b,d or empty,body,source)
        x,y=center
        start,end=(x-5.7,y-5.7),(x+5.7,y+5.7)
        gap=line(start,end,width=3.1)
        slash=line(start,end)
        overrides[n]={'duotone':[(clear_mark(a,gap,min_area),v) for a,v in duo]+[(slash,1)],
                      'solid':union(clear_mark(solid,gap,min_area),slash),
                      'stroke':union(clear_mark(mono,gap,min_area),slash)}

    def badge(n,b,d,mark,body=True,x=12,y=11.8,*,source=None,radius=3.3,min_area=0):
        duo,solid,mono=layers(n,b,d or empty,body,source)
        clearance=union(circle(x,y,radius),mark,stroke(mark,1.8 if source else 1.5))
        overrides[n]={'duotone':[(clear_mark(a,clearance,min_area),v) for a,v in duo]+[(mark,1)],
                      'solid':union(clear_mark(solid,clearance,min_area),mark),
                      'stroke':union(clear_mark(mono,clearance,min_area),mark)}
    def lock(x=12,y=11.5):
        return union(stroke(rr(x-1.8,y,3.6,3)),stroke(f'M{x-1.1} {y}v-1.3a1.1 1.1 0 0 1 2.2 0v1.3'))

    def overlapping(n,rear,front,rear_detail,front_detail,*,structural_rear_detail=False):
        # Paint the front object once, with the same clearance in all three styles.
        front_ink = union(stroke(front),front_detail)
        clear = union(front,stroke(front,4.3))
        visible = cut(rear,clear)
        rear_ink = union(stroke(visible),cut(rear_detail,clear))
        ink = union(rear_ink,front_ink)
        surface = cut(union(visible,front),ink)
        def filled(body,detail):
            shell = union(body,stroke(body))
            return union(cut(shell,detail),cut(detail,shell))
        rear_solid = union(rear,stroke(rear),rear_detail) if structural_rear_detail else filled(rear,rear_detail)
        S(n,union(rear,front),union(rear_detail,front_detail))
        overrides[n]={'duotone':[(surface,.24),(ink,1)],'stroke':ink,
                      'solid':union(cut(rear_solid,clear),filled(front,front_detail))}
    api['CATEGORY']='Technology and development'
    soften, sfbadge = api['soften'], api['badge']
    # SF display: a wide 14.6 x 10 screen on a short, filled stand (neck + foot).
    screen = rr(1.2,2.4,13.6,8.96)
    stand = soften(union(rr(6.15,11.2,3.7,2.1,0),rr(5.5,13.05,5,1.07,.45,exact=True)),.18)
    cy = 6.88
    marks={
        'activity':stroke('M4.2 6.9H5.75L6.85 4.85L8.65 8.95L9.7 6.9H11.8'),
        'check':check(7.75,7.05,.82),
        'cloud':stroke('M5.95 8.85C4.35 8.85 4.3 6.6 5.9 6.5C6.25 4.4 9.35 4.35 9.95 6.35C11.8 6.3 11.95 8.85 10.1 8.85Z'),
        'dot':circle(8,cy,1.35),'down':arr('down',8,cy,.64),
        'pause':lines('M6.75 5.05V8.7','M9.25 5.05V8.7'),
        'play':play(8.3,cy,1.0),'stop':rr(6.25,cy-1.75,3.5,3.5,.6,exact=True),
        'up':arr('up',8,cy,.64),'x':cross(8,cy,.72)}
    for state,m in marks.items(): S('monitor-'+state,screen,union(stand,m))
    # SF tv: the same wide screen, a free-standing foot bar below.
    tv_screen = rr(1.2,2.75,13.6,8.5)
    tv_foot = line((5.25,13.35),(10.75,13.35))
    S('tv-minimal',tv_screen,tv_foot)
    S('tv-minimal-play',tv_screen,union(play(8.3,7.0,.9),tv_foot))
    small_stand = soften(union(rr(4.25,10.3,2.3,1.6,0),rr(3.7,11.85,3.4,1.0,.42,exact=True)),.15)
    for n in ('monitor-pc','computer'):
        display = rr(1.2,3.0,8.4,7.0)
        tower = rr(11.6,2.6,3.2,10.4,1.1,exact=True)
        if n=='computer':
            face = union(line((1.2,8.1),(9.6,8.1)),circle(13.2,4.9,.62),circle(13.2,10.9,.62))
        else:
            face = union(line((12.65,5.1),(13.75,5.1)),circle(13.2,10.9,.62))
        S(n,union(display,tower),union(small_stand,face))
    S('pc-case',rr(3.9,1.4,8.2,13.2,1.5,exact=True),
      union(lines('M6.1 4.2H9.9','M6.1 6.4H9.9'),ring(8,10.6,1.75)))
    phone_face = rr(9.45,6.2,4.9,8.15,1.25,exact=True)
    home_dot = rr(10.95,7.25,1.9,.7,.35,exact=True)
    monitor_stand = soften(union(rr(5.1,10.3,2.3,1.75,0),rr(4.5,12.0,3.5,1.0,.42,exact=True)),.15)
    overlapping('monitor-smartphone',rr(1.2,2.5,10.4,7.85),phone_face,
                monitor_stand,home_dot,structural_rear_detail=True)
    cabinet = rr(8.5,5.9,5.85,8.45,1.25,exact=True)
    speaker_face = union(circle(11.425,8.0,.62),ring(11.425,11.55,1.75))
    overlapping('monitor-speaker',rr(1.2,2.5,10.4,7.85),cabinet,
                monitor_stand,speaker_face,structural_rear_detail=True)
    overlapping('tablet-smartphone',rr(1.2,2.6,12.2,9.0,1.5,exact=True),phone_face,
                rr(4.85,10.05,2.3,.7,.35,exact=True),home_dot,structural_rear_detail=True)

    # SF laptopcomputer: screen resting on a full-width filled base.
    laptop = rr(2.15,3.7,11.7,8.1)
    laptop_base = rr(.7,11.25,14.6,1.4,.6,exact=True)
    S('laptop-minimal',laptop,laptop_base)
    S('laptop-minimal-check',laptop,laptop_base)
    sfbadge('laptop-minimal-check','check',12.25,10.75,3.15)
    # SF iphone: rounded slab with a small island; content sits in the middle.
    phone = rr(4.4,1.7,7.2,12.6,1.6,exact=True)
    island = rr(6.85,2.8,2.3,.8,.4,exact=True)
    bolt = poly([(8.95,5.25),(6.15,8.75),(7.95,8.75),(7.05,11.6),(9.85,8.05),(8.05,8.05)])
    S('smartphone-charging',phone,union(island,bolt))
    slim = rr(5.2,2.25,5.6,11.5,1.4,exact=True)
    waves = stroke('M3.45 5.95Q2.8 8 3.45 10.05M1.7 4.75Q.75 8 1.7 11.25')
    vib = union(waves,api['mirror'](waves),rr(7.05,3.25,1.9,.7,.35,exact=True))
    S('vibrate',slim,vib)
    inner_waves = stroke('M3.45 5.95Q2.8 8 3.45 10.05')
    off('vibrate-off',slim,union(inner_waves,api['mirror'](inner_waves),rr(7.05,3.25,1.9,.7,.35,exact=True)))
    # SF computermouse: a tall capsule split into two buttons; the active one is filled.
    mouse = rr(4.15,1.6,7.7,12.8,3.85)
    divider = stroke('M4.2 5.6H11.8M8 1.7V5.6')
    button = op(cut(mouse,stroke(mouse,1.0,exact=True)),rr(0,0,8,5.6,0),po.PathOp.INTERSECTION)
    for n,mark in [('left',button),('right',api['mirror'](button))]:
        S('mouse-'+n,mouse,union(divider,mark))
    off('mouse-off',source='mouse',center=(7.65,8.35))
    # SF simcard: card with its top-right corner clipped; a contact chip low in the card.
    card = path('M4.3 1.6H9.6L12.9 4.9V13.2Q12.9 14.4 11.7 14.4H4.3Q3.1 14.4 3.1 13.2V2.8Q3.1 1.6 4.3 1.6Z')
    chip = union(stroke(rr(5.5,7.35,5,5.3,1,exact=True)),stroke('M5.6 9.55H10.4M8 9.55V12.55'))
    S('card-sim',card,chip)
    # SF battery: wide low body, rounded nub, inset charge level.
    battery = rr(1.2,4.35,12.3,7.3,1.75,exact=True)
    nub = rr(14.35,6.15,1.0,3.7,.5,exact=True)
    for n,m in [('medium',rr(2.75,5.9,5.0,4.2,.95,exact=True)),('plus',plus(7.35,8,.72)),('exclamation-point',warn(7.35,8,.85))]:
        S('battery-'+n,battery,union(m,nub))
    # SF externaldrive, compacted below an SF arrow (as in tray.and.arrow.down).
    drive = path('M4.35 7.95H11.65Q12.25 7.95 12.55 8.45L14.65 11.2V12.75Q14.65 14.1 13.3 14.1H2.7Q1.35 14.1 1.35 12.75V11.2L3.45 8.45Q3.75 7.95 4.35 7.95Z')
    face = union(line((1.35,11.2),(14.65,11.2)),circle(12.1,12.65,.58))
    for name,arrow in [('download',stroke('M8 1.35V5.95M5.75 3.7L8 5.95L10.25 3.7')),
                       ('upload',stroke('M8 5.95V1.35M5.75 3.6L8 1.35L10.25 3.6'))]:
        S('hard-drive-'+name,drive,union(arrow,face))
    # Printer states use the shared printer with an SF badge.
    printer_body,printer_detail = api['DRAWINGS']['printer'][:2]
    for n,kind in [('check','check'),('x','x')]:
        S('printer-'+n,printer_body,printer_detail)
        sfbadge('printer-'+n,kind)
    gantry = rr(2.4,2.1,11.2,11.8)
    head = path('M6.5 2.1H9.5V4.3L8 5.9L6.5 4.3Z')
    print_part = path('M5.2 11.85V9.85H6.75V8.25H9.25V9.85H10.8V11.85Z')
    ink = union(stroke(gantry),stroke(head),stroke(print_part),line((2.4,11.85),(13.6,11.85)))
    G('printer-3d',ink)
    overrides['printer-3d']={'solid':union(ink,head,print_part)}
    # SF videoprojector: a long low body, a large lens ring, short vents.
    S('projector',rr(1.2,4.55,13.6,6.9,1.6,exact=True),
      union(ring(6.1,8,2.95),circle(6.1,8,.9),lines('M10.6 6.85H12.4','M10.6 9.15H12.4')))
    # SF robotic.vacuum: a low cylinder seen from above the front edge.
    def ellipse(cx,cy,rx,ry): return circle(0,0,1).transform(rx,0,0,ry,cx,cy)
    top = ellipse(8,6.55,6.8,2.75)
    vacuum = union(top,rr(1.2,6.55,13.6,2.9,0),ellipse(8,9.45,6.8,2.75))
    front = op(stroke(top),rr(0,6.55,16,6,0),po.PathOp.INTERSECTION)
    S('robot-vacuum',vacuum,union(front,ellipse(8,5.75,1.6,.72)))
    foot = rr(1.8,12.05,7,2.3)
    pivots = union(circle(4.6,8.65,1.25),circle(8.8,4.7,1.4))
    links = stroke('M4.6 12.05V9.9M5.5 7.78L7.8 5.7M10.2 4.7L12.05 4M12.05 4L12 2.2L14 1.6M12.05 4L13.25 5.55L14.65 5')
    S('robot-arm',union(foot,pivots),links)
    overrides['robot-arm']={'solid':union(foot,pivots,stroke(foot),stroke(pivots),links)}
    # Opposed plug backs share one S-bend. The pins face away from the cord.
    plug_ends = union(rr(1.8,3.1,4.4,3.8), rr(9.8,9.1,4.4,3.8))
    tips = union(rr(2.75,1.2,2.5,1.9,.45,exact=True),rr(10.75,12.9,2.5,1.9,.45,exact=True))
    S('cable', plug_ends, union(tips,stroke('M4 6.9V9.7C4 13 8 13 8 9V7C8 3 12 3 12 6.3V9.1')))
    plug=path('M4 5H12V8Q12 11 8 11Q4 11 4 8Z')
    S('plug-2',plug,lines('M6 1.5V5M10 1.5V5M8 11V14.5'))
    bolt = poly([(13.2,9.15),(10.55,12.25),(12.25,12.25),(11.55,14.5),(14.5,11.1),(12.7,11.1)])
    badge('plug-zap',None,None,bolt,source='plug',x=12.8,y=12.3,radius=1.55,min_area=.85)
    plug_half = path('M2.75 5.7H5.7V10.3H2.75Q1.75 8 2.75 5.7Z')
    socket_half = path('M10.55 5.7H13.1Q14.25 8 13.1 10.3H10.55Z')
    terminals = stroke('M5.7 6.8H7.65M5.7 9.2H7.65M1.35 8H2.35M13.7 8H14.65')
    S('unplug',transform(union(plug_half,socket_half),-35),transform(terminals,-35))
    S('usb-c-port',rr(1.2,4.3,13.6,7.4,2.2,exact=True),stroke(rr(4.1,6.85,7.8,2.3)))
    S('hdmi-port',path('M2 4.2H14V9L11.5 11.8H4.5L2 9Z'),union(line((5.45,6.6),(10.55,6.6)),dots((5.45,9.1),(8,9.1),(10.55,9.1),r=.62)))
    S('midi-port',circle(),dots(*[(8+3.2*math.cos(i*math.pi/4),8.3-3.2*math.sin(i*math.pi/4)) for i in range(5)],r=.68))
    # SF memorychip: a landscape package with short pins on its long edges.
    pins = lines(*(f'M{x} 2.4V3.7' for x in (4,6,8,10,12)),*(f'M{x} 12.3V13.6' for x in (4,6,8,10,12)))
    S('microchip',rr(1.85,4.2,12.3,7.6),pins)
    package,cpu_details = api['DRAWINGS']['cpu'][:2]
    pins = cut(cpu_details,package)
    lettering = stroke('M5.65 9.85L5.98 6.95Q6.12 5.85 7.05 5.85Q8 5.85 8.15 6.95L8.5 9.85M5.85 8.65H8.28M10.25 6.05V9.85')
    S('cpu-ai',package,union(pins,lettering))
    fan_center = (6.1,7.15)
    blade = stroke('M6.35 7.25Q4.05 6.4 4.55 4.65')
    blade = transform(blade,dx=1.65,dy=.75)
    fan = union(*(transform(blade,i*120,dx=-1.9,dy=-.85) for i in range(3)),circle(*fan_center,.8),ring(*fan_center,3.55))
    S('gpu',rr(1.2,2.6,13.6,9.1),union(fan,stroke('M11.35 5.6H12.85V8.7H11.35ZM4.6 11.7V13.9M7.6 11.7V13.9M10.6 11.7V13.9')))
    traces = stroke('M4.25 4.4H7.25V6.3M4.25 11.6H6.35V9.7M9.75 7.25H11.75V4.4M9.05 9.75V11.6H11.75')
    S('circuit-board',rr(2,2,12,12),union(stroke(rr(6.3,6.3,3.4,3.4,.6,exact=True)),traces,
      dots((4.25,4.4),(4.25,11.6),(11.75,4.4),(11.75,11.6),r=.8)))
    S('container', rr(1.2,3.6,13.6,8.8), lines(*(f'M{x} 6V10' for x in (4.4,6.8,9.2,11.6))))
    # server-plus / server-crash: SF disc badges, drawn in draw.py (lane B).
    S('server-nas',rr(1.8,3,12.4,10.5),union(stroke(rr(4,5,2.6,6.5)),stroke(rr(9.4,5,2.6,6.5)),dots((5.3,10),(10.7,10),r=.45)))


    # database-arrow-down / -up: SF disc badges, drawn in draw.py (lane B).
    badge('database-zap',None,None,poly([(12.45,8.6),(9.75,12.05),(11.75,12.05),(11.05,14.65),(13.95,11.05),(11.95,11.05)]),source='database',radius=3.5)
    cloud=path('M4.2 13C.3 13 .5 7 4.3 7C4.5 1.5 12 1.5 12.5 7C16.3 7 16 13 12.5 13Z')
    badge('cloud-cog',None,None,cog(),source='cloud',x=12,y=11.8,radius=3.9,min_area=1.3)
    cloud_body = api['DRAWINGS']['cloud'][0]
    x0,y0,x1,y1 = cloud_body.bounds
    S('cloud-exclamation-point',cloud_body,warn((x0+x1)/2,(y0+y1)/2+.75,.85))
    wifi_badges = {
        'cog':cog(12.55,11.7),
        'lock':lock(12.55,11.45),
        'pen':stroke('M10.4 13.9L10.9 11.55L13.35 8.95L14.75 10.35L12.25 13.1Z'),
        'sync':stroke('M10.25 10.7Q11.9 8.3 14.55 10.15M14.55 8.6V10.5H12.7'
                      'M14.7 12.7Q13 15.1 10.55 13.15M10.55 14.65V12.8H12.4')}
    for n,mark in wifi_badges.items():
        badge('wifi-'+n,None,None,mark,source='wifi',x=12.55,y=11.7,radius=3.5)
    # SF antenna.radiowaves.left.and.right: a dot on a mast between two pairs of arcs.
    def radiowaves(cx,cy,radii,spread):
        arcs=[]
        for r,a in zip(radii,spread):
            dx,dy=r*math.cos(math.radians(a)),r*math.sin(math.radians(a))
            arcs.append(f'M{cx-dx} {cy-dy}A{r} {r} 0 0 0 {cx-dx} {cy+dy}M{cx+dx} {cy-dy}A{r} {r} 0 0 1 {cx+dx} {cy+dy}')
        return stroke(''.join(arcs))
    G('antenna',union(radiowaves(8,6.3,(3.45,6.3),(50,47)),circle(8,6.3,1.1)),line((8,7.6),(8,14.2)))
    G('radio-tower',union(radiowaves(8,4.55,(2.75,5.05),(48,46)),circle(8,4.55,.95)),
      stroke('M4.9 14.3L8 6.3L11.1 14.3M6.35 10.55H9.65M5.4 12.95H10.6'))
    panel = rr(.95,4.75,3.25,6.5)
    panels = transform(union(panel,api['mirror'](panel)),45)
    bus = transform(rr(6.4,6.4,3.2,3.2),45)
    struts = transform(lines('M4.2 8H6.4','M9.6 8H11.8'),45)
    grid = transform(lines('M.95 8H4.2','M11.8 8H15.05'),45)
    S('satellite',union(panels,bus),union(struts,grid))
    # Keep both solar cells open in Solid so the panel division survives at 16 px.
    overrides['satellite']={'solid':union(bus,stroke(bus),stroke(panels),struts,grid)}
    bowl = path('M2.2 3.6Q5.75 7.85 12.55 10.2C7.55 13.55 1.35 10.2 2.2 3.6Z')
    S('satellite-dish',bowl,union(stroke('M7.15 8.15L9.8 4.25M7.25 11.3L5.95 14H10.8L8.9 11.4'),circle(10.15,3.65,1.05)))
    # SF web.camera: a round head with a lens, on a neck and a foot.
    webcam = circle(8,6.35,4.25)
    off('webcam-off',webcam,union(ring(8,6.35,2.35),lines('M8 10.6V13.35','M5.4 13.9H10.6')))
    # SF flashlight: narrow body under a wider head, a capped lens and a switch.
    lamp = path('M5.55 1.3H10.45Q11.05 1.3 11.05 1.9V4.1Q11.05 4.6 10.75 5.0L9.7 6.45V14.1Q9.7 14.7 9.1 14.7H6.9Q6.3 14.7 6.3 14.1V6.45L5.25 5.0Q4.95 4.6 4.95 4.1V1.9Q4.95 1.3 5.55 1.3Z')
    S('flashlight',lamp,union(line((4.95,3.15),(11.05,3.15)),rr(7.35,8.4,1.3,2.5,.65)))
    off('flashlight-off',source='flashlight',center=(7.550,8.400),min_area=1.55)
    gong = circle(6.25,6,4.45)
    hammer = circle(13.1,8.55,1.25)
    S('bell-electric',union(gong,hammer),union(circle(6.25,6,.7),stroke('M6.25 10.45V13.85H13.1V9.8')))
    # SF light.beacon.max: a dome with a filament on a wide base, five short rays.
    siren = path('M4.4 13.4V9.0A3.6 3.6 0 0 1 11.6 9.0V13.4Z')
    beacon = union(line((2.75,13.85),(13.25,13.85)),line((8,9.6),(8,13.4)),
                   lines('M8 1.25V3.05','M3.3 3.55L4.5 4.75','M12.7 3.55L11.5 4.75','M1.25 9H2.35','M14.75 9H13.65'))
    S('siren',siren,beacon)
    off('siren-off',source='siren',center=(7.725,8.275),min_area=1.7)
    housing = path('M2.15 4.65H7.75L10.55 3.55V10.55L7.75 9.45H2.15Z')
    S('spotlight',transform(housing,-24),union(transform(stroke('M8.25 4.5V9.6'),-24),
      stroke('M7.4 9.55V13.85M4.25 13.85H10.55M12 3.3L13.65 2.5M13.1 5.9L14.6 5.2')))

    # Developer diagrams use genuine node topology and arrow direction.
    # SF book.closed: a tall cover with a spine line and a page block below.
    book = path('M4.3 1.65H11.7Q12.9 1.65 12.9 2.85V11.3Q12.9 11.85 12.45 12.15V13.15Q12.45 14.35 11.25 14.35H4.3Q3.1 14.35 3.1 13.15V2.85Q3.1 1.65 4.3 1.65Z')
    spine = stroke('M4.6 1.7V11.3M3.15 11.3H12.85')
    bx,by = 8.75,6.45
    bookmarks={
        'down':arr('down',bx,by,.62),'up':arr('up',bx,by,.62),
        'up-2':stroke(f'M{bx-1.75} {by-.45}L{bx} {by-2.2}L{bx+1.75} {by-.45}M{bx-1.75} {by+2.05}L{bx} {by+.3}L{bx+1.75} {by+2.05}'),
        'audio':lines(f'M{bx-1.8} {by-.9}V{by+.9}',f'M{bx} {by-2}V{by+2}',f'M{bx+1.8} {by-.9}V{by+.9}'),
        'headphones':union(stroke(f'M{bx-1.85} {by+.9}V{by}A1.85 1.85 0 0 1 {bx+1.85} {by}V{by+.9}'),
                           rr(bx-2.4,by+.45,1.4,2.05,.5,exact=True),rr(bx+1.0,by+.45,1.4,2.05,.5,exact=True)),
        'image':union(stroke(f'M{bx-2.5} {by+2.1}L{bx-.6} {by}L{bx+.75} {by+1.2}L{bx+1.55} {by+.45}L{bx+2.5} {by+1.4}'),circle(bx+1.2,by-1.5,.8)),
        'key':union(ring(bx-.6,by-.75,1.65),stroke(f'M{bx+.4} {by+.3}L{bx+1.95} {by+2.05}M{bx+1.3} {by+1.35}L{bx+2.05} {by+.75}'))}
    for n,m in bookmarks.items(): S('book-'+n,book,union(spine,m))
    # Dashed cover: the spine stays solid; the free edges break into even dashes.
    gaps = union(*(rr(x-.55,y-.55,1.1,1.1,0) for x,y in
                   [(7.2,1.65),(10.45,1.65),(12.9,4.85),(12.9,8.35),(8.15,14.35),(10.75,14.35)]))
    G('book-dashed',union(cut(stroke(book),gaps),line((3.15,11.3),(12.85,11.3))))
    head,face = api['DRAWINGS']['bot'][:2]
    # Raise the face as a unit to make space for a speech tail.
    head = transform(head,dy=-1.65)
    face = cut(face,rr(7,.65,2,5,0))
    tail = poly([(3.55,11.8),(7.55,12.45),(3.5,14.8)])
    S('bot-message-square',union(head,tail),
      union(transform(face,dy=-1.65),line((8,1.25),(8,2.85))))
    off('bot-off',source='bot',center=(7.1,9.05),min_area=1.55)
    brain,folds = api['DRAWINGS']['brain'][:2]
    brain = fit_outline(brain)
    midline = max(api['components'](folds),key=lambda part:part.area)
    traces = stroke('M4.25 5.25V7.45H5.95M11.85 8.35H10.25V10.9')
    badge('brain-cog',None,None,cog(),source='brain',x=12.05,y=11.95,radius=3.8,min_area=1.3)
    S('brain-circuit',brain,union(midline,traces))
    off('brain-off',source='brain',min_area=1.7)
    off('bug-off',source='bug',center=(7.55,8.45),min_area=1.8)
    badge('bug-play',None,None,play(12,11.8,1),source='bug',radius=3.65,min_area=1.85)
    S('blocks',union(rr(1.5,8.8,5.5,5.5),rr(8.8,8.8,5.5,5.5),rr(5.2,1.5,5.5,5.5)))
    S('boxes-linked',union(rr(1.5,2,4.5,4.5),rr(10,2,4.5,4.5),rr(5.8,10,4.5,4.5)),stroke('M3.75 6.5V8.35H12.25V6.5M8 8.35V10'))
    tab = 'h2.55q.45 0 .65 .5l.25 .65h2.3l.3-.65q.2-.5 .65-.5'
    # The two edges use the same tab and a constant vertical offset.
    joint = path('M2 6.7'+tab+'H14V2.2H2Z')
    lower = path('M2 9.35'+tab+'H14V14H2Z')
    S('scratch-blocks',union(joint,lower))
    G('chevrons-left-right-ellipsis',lines('M3.65 4.2L1.5 8L3.65 11.8M12.35 4.2L14.5 8L12.35 11.8'),dots((5.65,8),(8,8),(10.35,8),r=.71))
    G('parentheses',stroke('M5 2Q.5 8 5 14'),stroke('M11 2Q15.5 8 11 14'))
    G('option',lines('M2 3H5L11 13H14'),line((9,3),(14,3)))
    G('variable',stroke('M3 4Q6 2 7 6L9 11Q10 14 13 12M4 12L12 4'),empty)
    G('radical',line((1.5,8),(4.2,11.5),(7,3),(14.5,3)),empty)
    G('form', line((2.2,1.8),(7,1.8)),
      union(stroke(rr(2,4.4,12,3.6)),stroke(rr(2,10.45,12,3.6))))
    for n,detail in [('minus',line((10,12),(14,12))),('plus',plus(12,12,.8))]:
        badge('git-branch-'+n,union(circle(4,3,1.5),circle(4,13,1.5),circle(12,3,1.5)),stroke('M4 4.5V11.5M12 4.5Q12 8 4 8'),detail)
    S('git-commit-vertical',circle(8,8,2.8),lines('M8 1.5V5.2M8 10.8V14.5'))
    S('git-graph',union(circle(3.5,3,1.4),circle(3.5,12.7,1.4),circle(12.5,4.5,1.4),circle(12.5,12.7,1.4)),stroke('M3.5 4.4V11.3M12.5 5.9V11.3M3.5 7Q8 7 8 10Q8 12.7 11.1 12.7'))
    S('git-merge-conflict',union(circle(3.4,3.15,1.45),circle(3.4,12.85,1.45),circle(12.5,3.15,1.45)),
      union(stroke('M3.4 4.6V11.4M12.5 4.6Q12.5 8.05 9 8.05'),cross(6.55,8.05,.55)))
    def git_nodes(name,centers,radius,links):
        G(name,union(*(ring(x,y,radius) for x,y in centers)),links)
        overrides[name]={'solid':union(links,*(circle(x,y,radius) for x,y in centers))}
    git_nodes('git-compare-arrows',[(4,3.25),(12,12.75)],2.05,
              stroke('M4 5.2V13M1.8 10.8L4 13L6.2 10.8M12 10.8V3M9.8 5.2L12 3L14.2 5.2'))
    requestbody = api['DRAWINGS']['git-pull-request'][0]
    for n,mark in [('closed',cross(12,3.25,.78)),('create',plus(12,3.25,.82))]:
        S('git-pull-request-'+n,requestbody,union(cut(stroke('M4 3.25V13.25M12 13.25V6.75'),requestbody),mark))
    for n in ['arrow','create-arrow']:
        nodes = union(circle(3.1,3.4,1.45),circle(3.1,12.5,1.45),circle(12.5,12.5,1.45))
        branch = stroke('M3.1 4.85V11.05M12.5 11.05V7.2Q12.5 3.8 9.1 3.8H7.2M9.35 1.65L7.2 3.8L9.35 5.95')
        mark = plus(7.65,10.35,.7) if n=='create-arrow' else empty
        S('git-pull-request-'+n,nodes,union(branch,mark))
    git_nodes('git-pull-request-draft',[(3.8,3.05),(3.8,12.8),(12.1,12.8)],1.95,
              union(line((3.8,4.95),(3.8,10.9)),dots((12.1,3.2),(12.1,6.2),(12.1,9.2),r=.65)))
    off('webhook-off',source='webhook',center=(7.2,8.8),min_area=1.5)
    G('merge',stroke('M2 2V5Q2 8 8 8M14 2V5Q14 8 8 8M8 8V14M5.5 11.5L8 14L10.5 11.5'))
    fork = stroke('M8 10.8C8 8.3 5.9 6.3 2.55 3M2.55 6.55V3H6.1')
    G('split',line((8,14.35),(8,10.8)),union(fork,api['mirror'](fork)))
    S('combine',union(rr(1.5,1.5,5,5),rr(9.5,1.5,5,5),rr(5.5,10,5,4.5)),lines('M4 6.5V8H12V6.5M8 8V10'))
    for n,coords,edges in [
        ('graph-hub',[(8,8),(2.8,3.05),(13.2,3.05),(2.8,12.95),(13.2,12.95)],[(0,1),(0,2),(0,3),(0,4)]),
        ('graph-ring',[(8+5.3*math.sin(i*math.tau/5),8-5.3*math.cos(i*math.tau/5)) for i in range(5)],[(0,1),(1,2),(2,3),(3,4),(4,0)])]:
        nodes=union(*(circle(x,y,1.48) for x,y in coords))
        conn=union(*(line(coords[a],coords[b]) for a,b in edges))
        S(n,nodes,cut(conn,union(*(circle(x,y,1.53) for x,y in coords))))

    # Each vertex is a node on the pentagram. Clip chords at the node faces.
    tips = [(8 + 5.8*math.sin(i*math.tau/5), 8.5 - 5.8*math.cos(i*math.tau/5)) for i in range(5)]
    nodes = union(*(circle(x,y,1.25) for x,y in tips))
    chords = union(*(line(tips[i],tips[(i+2)%5]) for i in range(5)))
    S('graph-star',nodes,cut(chords,nodes))

    api['CATEGORY']='Media and communication'
    def tri(points,r=.75): return soften(path('M'+'L'.join(f'{x} {y}' for x,y in points)+'Z'),r)
    # SF play: a rounded outline triangle; .fill fills it.
    S('play-triangle',tri([(4.6,3.15),(13.05,8),(4.6,12.85)]))
    # SF pause is two lines; pause.fill is two rounded bars.
    pause_lines = lines('M5.3 2.9V13.1','M10.7 2.9V13.1')
    G('pause-bars',pause_lines)
    overrides['pause-bars']={'solid':union(rr(3.85,2.4,2.9,11.2,1.1,exact=True),rr(9.25,2.4,2.9,11.2,1.1,exact=True))}
    # SF video: rounded body and a rounded trapezoid lens.
    S('video-camera',union(rr(1.2,3.5,8.9,9.0,2.1,exact=True),tri([(11.55,6.45),(14.8,4.55),(14.8,11.45),(11.55,9.55)],.45)))
    G('radio-signal',radiowaves(8,8,(2.85,4.75,6.6),(45,46,47)),circle(8,8,1.15))
    speaker=path('M4.95 5.95H7.15L10.95 2.95Q12.05 2.25 12.05 3.55V12.45Q12.05 13.75 10.95 13.05L7.15 10.05H4.95Q4.2 10.05 4.2 9.3V6.7Q4.2 5.95 4.95 5.95Z')
    S('volume-none',speaker)
    off('volume-slash',speaker,empty)
    # SF waveform: seven rounded bars, tallest at the centre.
    wave=lines(*(f'M{2.6+1.8*i} {8-h/2}V{8+h/2}' for i,h in enumerate([2.4,6.2,9.6,12.6,8.0,4.8,2.4])))
    G('audio-lines',wave)
    off('audio-lines-off',source='audio-lines',center=(7.775,8.225),min_area=1.6)
    G('audio-lines-x',transform(wave,scale=.92,dx=-1.1))
    sfbadge('audio-lines-x','x',12.1,11.9)
    # SF eject: a rounded triangle over a rounded bar, both outlined.
    S('eject',union(tri([(2.55,8.75),(8,2.75),(13.45,8.75)],.6),rr(2.55,11.05,10.9,2.25,.9,exact=True)))
    # SF forward.end / backward.end: outlined triangle against a full-height bar.
    end_tri = tri([(3.6,3.45),(10.35,8),(3.6,12.55)],.55)
    S('step-forward',end_tri,line((12.35,3.6),(12.35,12.4)))
    S('step-back',api['mirror'](end_tri),line((3.65,3.6),(3.65,12.4)))
    off('play-off',source='play-triangle',center=(8,8),min_area=1.55)
    G('repeat-1',stroke('M3 9V5Q3 3 5 3H13M13 7V11Q13 13 11 13H3M11 1L13 3L11 5M5 11L3 13L5 15'),stroke('M7 6L8.5 5V10M7 10H10'))
    S('closed-caption',rr(1.5,3,13,10),stroke('M6.5 5.5C3 4 2.5 11 6.5 10M12.7 5.5C9 4 8.5 11 12.7 10'))
    S('hd',rr(1.5,3,13,10),stroke('M4 5.5V10.5M7 5.5V10.5M4 8H7M9.5 5.5H10.5Q13 5.5 13 8Q13 10.5 10.5 10.5H9.5Z'))
    S('ad',rr(1.5,3,13,10),stroke('M3.5 10.65L5.5 5.35L7.5 10.65M4.15 9.25H6.85M9.45 5.5H10.5Q13 5.5 13 8Q13 10.5 10.5 10.5H9.45Z'))
    slate = rr(1.75,7.5,12.5,6.4)
    clap = path('M1.75 5.45L13.15 1.55L13.8 3.6L2.45 7.5Z')
    cuts = op(stroke('M5.2 4.05L7 5.95M9 2.85L10.8 4.75'),clap,po.PathOp.INTERSECTION)
    S('clapperboard',union(slate,clap),cuts)
    S('boom-box',rr(1.5,5.6,13,7.9),union(stroke('M5.35 5.6V3.1H10.65V5.6M2.05 5.7L3.35 1.6'),ring(5,9.55,2.15),ring(11,9.55,2.15)))
    S('cassette-tape',rr(1.5,3.3,13,9.4),union(stroke(rr(3.5,5.2,9,3.8)),dots((5.4,7.1),(10.6,7.1),r=.65),stroke('M5 10L4 12.7M11 10L12 12.7M5 10H11')))
    S('videotape',rr(1.5,2.4,13,11.2),union(ring(4.7,6.25,1.7),ring(11.3,6.25,1.7),
      stroke(rr(5.15,9.15,5.7,2.3)),line((6.2,6.25),(9.8,6.25))))
    for n,arc,angle in [('2','M4.1 8A3.9 3.9 0 0 1 8 4.1',180),('3','M5.65 4.9A3.9 3.9 0 0 1 11.85 8.65',180)]:
        groove = stroke(arc)
        S('disc-'+n,circle(),union(ring(8,8,1.65),groove,transform(groove,angle)))
    S('disc-album',rr(1.5,1.5,13,13),union(stroke(circle(8,8,4.3)),ring(8,8,1.7)))
    platter = ring(6.15,8.05,3.55)
    arm = stroke('M12.15 5.25V7.75L8.15 10.3')
    S('turntable',rr(1.5,2.8,13,10.4),union(cut(platter,stroke(arm,1.95)),ring(6.15,8.05,1.43),arm,circle(12.15,5.25,.75)))
    G('circle-fading-play',union(stroke('M8 2.0A6.0 6.0 0 1 1 2.0 8'),dots((2.55,5.25),(4.75,2.85),r=.62)),play(8.35,8,1.12))
    S('circle-power',circle(),power(8,8,.63))
    S('circle-star',circle(),star(8,8,.56))
    G('circle-slash',ring(),line((4.4,11.6),(11.6,4.4)))
    G('circle-slash-2',ring(),line((4.4,4.4),(11.6,11.6)))
    rear_mask = path('M1.55 2.75Q4.95 1.3 8.3 2.65L8.05 6.6Q8 9.45 5 10.45Q2.05 9.7 1.85 6.8Z')
    front_mask = path('M7.05 6.45Q10.8 7.55 14.45 5.4L14.15 9.65Q14.05 12.8 11.2 14.1Q7.8 13.45 7.35 10.35Z')
    overlapping('drama',rear_mask,front_mask,union(dots((3.65,4.55),(6.3,4.4),r=.57),stroke('M3.7 7.2Q4.85 8.6 6 7.05')),
                union(dots((9.3,8.9),(12.35,8.5),r=.6),stroke('M9.35 11.8Q10.7 9.85 12.45 11.35')))
    G('list-music',lines('M2 3H8.25M2 6H7.65M2 9H6.65M2 12H5.8'),union(stroke('M11 11V3L14 2V10'),circle(9.8,11.5,1.25),circle(12.8,10.5,1.25)))
    G('list-video',lines('M2 3H14M2 6H8M2 9H6M2 12H6'),play(11,10.5,1.2))
    mic=rr(5.5,1.5,5,8)
    md=stroke('M3.5 6.5V8Q3.5 12 8 12Q12.5 12 12.5 8V6.5M8 12V14.5M5.5 14.5H10.5')
    S('mic-audio-lines',rr(3.35,1.85,3.7,7.7),
      stroke('M1.6 7.5V8.4A3.6 3.6 0 0 0 8.8 8.4V7.5M5.2 12V14.25M11.35 5.65V9.65M14.1 3.8V11.5'))
    S('mic-signal',mic,union(md,stroke('M12.85 1.95Q14.65 3.15 14.35 5.6M3.15 1.95Q1.35 3.15 1.65 5.6')))
    grille = rr(5.15,1.45,5.7,6.4)
    handle = path('M6.25 6.95H9.75L9 13.7Q8.8 14.5 8 14.5T7 13.7Z')
    S('mic-vocal',transform(union(grille,handle),39),
      transform(stroke('M5.3 4.6H10.7M6.25 7.1Q8 8.25 9.75 7.1'),39))
    off('headphone-off',source='headphones',center=(7.725,8.425),min_area=1.65)
    # Inward-facing acoustic heads extend from the outside of the angled stems.
    bud = path('M2.25 5.3C1.6 3.25 3.1 2.3 4.85 2.75L6.45 3.25Q7.6 3.7 7.15 5.35Q6.8 6.85 5.05 6.65L4.6 6.55L5.7 11.95Q5.95 13.2 4.75 13.45Q3.65 13.6 3.45 12.4Z')
    buds = union(bud,api['mirror'](bud))
    vent = line((5.15,4.65),(5.9,4.85))
    S('earbuds',buds,union(vent,api['mirror'](vent)))
    off('earbuds-off',source='earbuds',min_area=1.2)
    off('megaphone-off',source='megaphone',center=(8,8),min_area=2.5)
    radio=rr(1.5,5,13,9)
    off('radio-off',radio,union(line((3,5),(12,1.5)),ring(5.5,9.5,2),lines('M10 8H12M10 11H12')))
    # SF phone: a handset with rounded ear and mouth pads joined by a curved grip.
    handset = path('M4.3 1.9C4.9 1.6 5.6 1.8 5.9 2.4L7.0 4.6C7.3 5.2 7.15 5.9 6.6 6.3L5.6 7.0C6.4 8.7 7.4 9.7 9.0 10.45'
                   'L9.75 9.4C10.15 8.85 10.85 8.7 11.45 9.0L13.6 10.1C14.2 10.4 14.4 11.1 14.1 11.7L13.4 13.1'
                   'C12.9 14.0 11.85 14.4 10.9 14.1C6.6 12.7 3.3 9.4 1.9 5.1C1.6 4.15 2.0 3.1 2.9 2.6Z')
    S('phone-forwarded',handset,stroke('M9.2 4.3H14.1M12.1 2.3L14.1 4.3L12.1 6.3'))
    S('phone-log',handset,lines('M9.4 2.3H14.1','M10.6 4.65H14.1','M11.8 7H14.1'))
    bubble = path('M1.6 2.25H10.35V9.05H6.3L3.45 11.85V9.05H1.6Z')
    S('speech',bubble,stroke('M4 5.6H7.95M13.35 7.05Q16.05 10.1 13.35 13.15M11.65 8.9Q12.75 10.1 11.65 11.3'))

    # Musical notation is monochrome; instrument bodies carry physical depth.
    def note_head(x,y,hollow=False):
        outline = path('M-2.35 .38C-2.4-.7-.95-1.65 .5-1.65C1.6-1.65 2.35-1.1 2.35-.3C2.35 .8 .95 1.65-.5 1.65C-1.55 1.65-2.35 1.3-2.35 .38Z')
        head = outline.transform(1,0,0,1,x,y)
        return stroke(head) if hollow else head
    G('eighth-note',note_head(6.05,12.2),stroke('M7.78 12V2.05C8.75 3.55 12.2 3.45 11.8 6.8'))
    G('half-note',note_head(6.25,12,True),line((8.6,11.7),(8.6,1.9)))
    G('sixteenth-notes',union(note_head(3.85,12.25),note_head(11.25,10.85)),
      stroke('M5.58 12V3.6L12.98 2.2V10.6M5.58 6.55L12.98 5.15'))
    G('clef-bass',union(stroke('M3.2 5.1C3.25 1.05 8.35 1.05 9.7 4.25C11.4 8.4 6.9 12.45 3.75 14'),circle(3.2,5.3,1.18)),dots((12.55,4.6),(12.55,7.8),r=.72))
    G('clef-treble',stroke('M6.15 13.45Q6.5 15 8.2 14.55Q9.8 14.15 9.2 11.95L7.5 4.15C6.7 1.3 9.2 .4 9.7 2.3C10.3 4.7 7.55 6.05 5.2 7.95C2.35 10.45 4.3 12.95 7.55 12.55C11.6 12.1 12.55 8.2 10.2 7.1C8.5 6.35 6.4 7.7 6.45 9.5'))
    clef_lobe = stroke('M7.45 3.7C8.35 .9 13 1.6 13.1 4.65C13.2 7.15 11.6 8 10 8Q9.05 8 8.6 7.2')
    G('clef-alto', union(line((2.5,2),(2.5,14)), line((5.1,2),(5.1,14))),
      union(clef_lobe,clef_lobe.transform(1,0,0,-1,0,16),stroke('M8.6 6.1L6.6 8L8.6 9.9')))
    drum = path('M2.1 6.5C2.1 3.95 13.9 3.95 13.9 6.5V11.85Q8 15.95 2.1 11.85Z')
    S('drum',drum,union(stroke('M2.1 6.5Q8 9.55 13.9 6.5M3 12.35L5.35 8.15L8 13.7L10.65 8.15L13 12.35'),stroke('M2 1.5L6.2 3.05M14 1.5L9.8 3.05')))
    S('metronome',poly([(6,1.7),(10,1.7),(14,14),(2,14)]),
      union(stroke('M5.3 11.65H10.7M7.1 11.65L9.2 5.65'),rr(8.15,6.45,1.75,1.7)))
    # Construct neck, headstock and bridge on one axis before rotating the instrument.
    headstock = rr(7.05,1,1.9,2.65)
    neck = line((8,3.2),(8,8))
    acoustic = path('M8 6.8C10.25 6.45 11.35 7.7 10.65 9.3Q10.25 10.15 11.1 10.95C13.4 13.85 10.6 15.1 8 15.1S2.6 13.85 4.9 10.95Q5.75 10.15 5.35 9.3C4.65 7.7 5.75 6.45 8 6.8Z')
    electric = path('M5.1 6.05Q6.1 8.5 7.6 7.6L8.5 7.35Q10.05 8.65 11.2 6.5C11.85 8.55 9.75 9.8 11.15 11.1C13.25 13.6 10.3 15.1 8 15.1C4.8 15.1 3.4 13.6 4.6 11.55Q5.6 10.1 5.1 9.05Q4.45 7.65 5.1 6.05Z')
    for n,wood,detail in [('guitar',acoustic,ring(8,9.45,1.65)),
                          ('guitar-electric',electric,line((7.05,9.85),(8.95,9.85)))]:
        offset_y = -.2 if n=='guitar' else 0
        body = transform(wood,36,dy=offset_y)
        fittings = transform(union(headstock,cut(neck,wood)),36,dy=offset_y)
        bridge = line((6.75,12.5),(9.25,12.5))
        face = transform(union(detail,bridge),36,dy=offset_y)
        S(n,body,union(face,fittings))
        shell = union(body,stroke(body))
        overrides[n]={'solid':union(cut(shell,face),fittings)}
    for n,top,bottom in [('piano',2.25,13.75),('keyboard-music',4,12)]:
        body = rr(1.5,top,13,bottom-top)
        rail = top+2.35 if n=='piano' else top
        keys = union(*(line((x,rail),(x,bottom)) for x in (4.75,8,11.25)))
        black_keys = union(*(rr(x-.93,rail,1.86,(bottom-rail)*.52) for x in (4.75,8)))
        details = union(keys,black_keys,line((1.5,rail),(14.5,rail))) if n=='piano' else union(keys,black_keys)
        S(n,body,details)

    api['CATEGORY']='Charts and analytics'
    axes=stroke('M2 2.5V13.5H14')
    # SF chart.bar.xaxis: data bars are filled, rounded marks in every style.
    def bar(x0,y0,x1,y1): return rr(x0,y0,x1-x0,y1-y0,.7,exact=True)
    for orient,word in [('h','bar'),('v','column')]:
        for suffix,sizes in [('big',[9.0,6.2]),('decreasing',[9.0,6.2,3.4]),('increasing',[3.4,6.2,9.0])]:
            marks=[]
            n=len(sizes)
            for i,size in enumerate(sizes):
                pos=(4.55+i*3.45) if n==3 else (5.2+i*4.2)
                if orient=='h':
                    marks.append(bar(3.65,pos-1.1,3.65+size,pos+1.1))
                else:
                    marks.append(bar(pos-1.1,12.35-size,pos+1.1,12.35))
            G('chart-'+word+'-'+suffix,axes,union(*marks))
    G('chart-bar-stacked',axes,union(bar(3.65,2.5,6.6,4.7),bar(7.6,2.5,13.6,4.7),
                                     bar(3.65,6.0,9.4,8.2),bar(10.4,6.0,13.6,8.2),
                                     bar(3.65,9.5,5.3,11.7),bar(6.3,9.5,13.6,11.7)))
    # SF chart.bar: outlined rounded bars on a common baseline; .fill fills them.
    for suffix,sizes in [('',[6.5,11,8.5]),('-decreasing',[11,8.25,5.5]),('-increasing',[5.5,8.25,11])]:
        S('chart-no-axes-column'+suffix,union(*(rr(1.31+i*5.14,13.5-size+.52,3.1,size-1.04,.9,exact=True) for i,size in enumerate(sizes))))
    G('chart-gantt',axes,union(bar(4.0,3.0,8.3,5.0),bar(6.0,6.5,12.0,8.5),bar(9.0,10.0,14.2,12.0)))
    G('chart-no-axes-gantt',stroke('M2 3.5H8M5 8H13M9 12.5H14'))
    S('chart-no-axes-combined',union(rr(1.6,9.6,2.9,3.9,.8,exact=True),rr(6.55,7.1,2.9,6.4,.8,exact=True),rr(11.5,8.6,2.9,4.9,.8,exact=True)),
      stroke('M1.8 5.6L7.6 2.4L14.2 4.6'))
    G('chart-bell-curve',axes,stroke('M4.35 11.05C6.5 11.05 5.8 3.55 8.95 3.55S11.4 11.05 13.55 11.05'))
    G('chart-spline',axes,stroke('M4.45 10C6.6 10 5.25 5.1 7.65 5.1S10.15 10.8 12.1 7.1L14 3.2'))
    G('chart-candlestick',axes,union(stroke('M5.5 3V11M10.8 2V10'),rr(4.12,5,2.76,4),rr(9.42,4,2.76,3.5)))
    G('chart-quadrant',lines('M8 1.5V14.5M1.5 8H14.5'),dots((4,4),(11,3),(11.8,11.7),(4.8,10.6),r=.8))
    G('chart-network',union(line((3,11),(5,3),(12,4),(13,12),(3,11),(12,4))),union(*(ring(x,y,1.35) for x,y in [(3,11),(5,3),(12,4),(13,12)])))
    vertices = [(8 + 6.65*math.sin(i*math.tau/5), 8 - 6.65*math.cos(i*math.tau/5)) for i in range(5)]
    frame = stroke(poly(vertices))
    spokes = union(*(line((8,8),p) for p in vertices))
    plot = poly([(7.45,4.75),(10.95,6.35),(9.85,11.05),(7.45,8.7),(4.6,8.3)])
    rim = stroke(plot)
    grid = union(frame,cut(spokes,plot))
    ink = union(grid,rim)
    S('chart-radar',plot,grid)
    overrides['chart-radar']={'duotone':[(cut(plot,ink),.24),(ink,1)],'solid':union(cut(grid,plot),plot,rim),'stroke':ink}
    G('trending-up-down',stroke('M1.6 10.8L5.7 6.7L8.25 8.35L14 2.8M10.55 2.8H14V6.25'),
      stroke('M8.25 8.35L14 13.45M10.55 13.45H14V10'))
    steps = path('M1.6 7.65H5.8V3.05H10.2V9.5H14.4V13.95H1.6Z')
    S('podium',steps,stroke('M5.8 7.65V13.95M10.2 9.5V13.95'))
    S('kanban',union(*(rr(x,2.5,2.45,h) for x,h in [(1.65,9),(6.775,6),(11.9,11)])))

    api['CATEGORY']='Actions and status'
    # SF square: 11.8 units of ink; inner glyphs at about half its interior.
    square = rr(2.62,2.62,10.76,10.76)
    squaremarks={
        'activity':stroke('M4.75 8H6.0L7.05 5.6L8.95 10.4L9.95 8H11.25'),
        'bookmark':path('M6.35 5.0H9.65Q10.15 5.0 10.15 5.5V11.0L8 9.6L5.85 11.0V5.5Q5.85 5.0 6.35 5.0Z'),
        'chart-gantt':lines('M5.4 6H8.3','M6.85 8H10.6','M8.6 10H10.6'),
        'dot':circle(8,8,1.4),'kanban':lines('M5.75 5.6V10.4','M8 5.6V8.2','M10.25 5.6V9.4'),
        'pause':lines('M6.75 5.5V10.5','M9.25 5.5V10.5'),
        'play':play(8.25,8,1.05),'power':power(8,8.1,.52),'radical':stroke('M4.95 8.2L6.4 10.3L8.05 5.65H11.2'),
        'slash':line((5.6,10.4),(10.4,5.6)),
        'sparkles':transform(union(path('M7 4.15Q7.55 7.95 10.1 8.7Q7.55 9.45 7 12Q6.45 9.45 3.9 8.7Q6.45 7.95 7 4.15Z'),path('M10.9 3.8Q11.2 5.05 12.4 5.4Q11.2 5.75 10.9 7Q10.6 5.75 9.4 5.4Q10.6 5.05 10.9 3.8Z')),scale=.78,dx=.25,dy=-.2),
        'star':star(8,8.1,.53),'stop':rr(6.05,6.05,3.9,3.9,.7,exact=True),
        'terminal':stroke('M5.35 5.75L7.6 8L5.35 10.25M8.85 10.25H10.75')}
    for n,m in squaremarks.items(): S('square-'+n,square,m)
    b,d,o,c,_=api['DRAWINGS']['square-kanban']
    api['DRAWINGS']['square-kanban-plus']=(b,d,o,c,'square kanban plus')
    if 'square-kanban' in overrides: overrides['square-kanban-plus']=dict(overrides['square-kanban'])
    api['badge']('square-kanban-plus','plus',12.1,12.0,3.15)
    dash=stroke('M2.62 10.2V4.62Q2.62 2.62 4.62 2.62H11.38Q13.38 2.62 13.38 4.62V10.2M2.62 12.6V13.38H3.9M7.2 13.38H8.8M12.1 13.38H13.38V12.6')
    G('square-dashed-bottom',dash)
    G('square-dashed-bottom-code',dash,stroke('M6.35 5.95L4.85 8L6.35 10.05M9.65 5.95L11.15 8L9.65 10.05'))
    corner = stroke('M2.62 4.55V4.12A1.5 1.5 0 0 1 4.12 2.62H4.55')
    dash = union(*(transform(union(corner,line((7.25,2.62),(8.75,2.62))),90*i) for i in range(4)))
    G('square-dashed-kanban',dash,squaremarks['kanban'])
    # SF plus.diamond: a softly rounded diamond with a centred mark.
    diamond = soften(path('M8 1.2L14.8 8L8 14.8L1.2 8Z'),.9)
    for n,m in [('minus',line((5.75,8),(10.25,8))),('plus',plus(8,8,1.1))]:S('diamond-'+n,diamond,m)
    S('badge-question-mark',api['badge_body'](),union(stroke('M6.3 6.3C6.3 4.4 9.7 4.4 9.7 6.3C9.7 7.5 8 7.7 8 9'),circle(8,11,.6)))
    G('slash',line((3.3,12.7),(12.7,3.3)))
    for n,angle in [('bottom-vertical',0),('top-vertical',180),('left-horizontal',90),('right-horizontal',270)]:
        G('line-dot-'+n,transform(line((8,2.2),(8,9.9)),angle),transform(circle(8,12.9,1.45),angle))
    for n,flip in [('left',True),('right',False)]:
        pennant = soften(path('M4 1.9L12.9 5.4L4 8.9Z'),.5)
        pole = line((4,2.2),(4,14.2))
        if flip: pennant,pole = api['mirror'](pennant),api['mirror'](pole)
        S('flag-triangle-'+n,pennant,pole)
    alarm_body,alarm_detail = api['DRAWINGS']['alarm-clock'][:2]
    alarm_parts = cut(alarm_detail,alarm_body)
    ax0,ay0,ax1,ay1 = alarm_body.bounds
    acx,acy = (ax0+ax1)/2,(ay0+ay1)/2
    for n,mark in [('minus',line((acx-2.3,acy),(acx+2.3,acy))),('plus',plus(acx,acy,1.15))]:
        S('alarm-clock-'+n,alarm_body,union(mark,alarm_parts))

    api['CATEGORY']='Photography and optics'


    # SF photo.badge.* variants share draw.py's photo and badge construction.
    for n,kind in [('down','arrow-down'),('up','arrow-up'),('play','play'),('upscale','expand')]:
        api['CATEGORY']='Media'
        api['photo_badge']('image-'+n,kind,'image '+n)
    api['CATEGORY']='Photography and optics'
    S('wallpaper',rr(1.5,2.5,13,11),union(stroke('M4.65 2.5V13.5M4.65 11.6L8.35 7.55L14.45 12.1'),ring(11.65,5.4,1.45)))
    S('picture-in-picture-2',rr(1.5,2,13,12),union(stroke(rr(8,8,5,4)),stroke('M3.5 4L6.5 7M3.5 7H6.5V4')))
    # Extend each edge of the hexagonal aperture outward to meet the rim.
    aperture_radius = 2.4
    vertex = (8+aperture_radius,8)
    next_vertex = (8+aperture_radius/2,8-aperture_radius*math.sqrt(3)/2)
    start = (vertex[0]+1.87*(vertex[0]-next_vertex[0]),vertex[1]+1.87*(vertex[1]-next_vertex[1]))
    blade = line(start,next_vertex)
    blades = union(*(transform(blade,i*60) for i in range(6)))
    G('aperture',ring(8,8,6.45),op(blades,circle(8,8,6),po.PathOp.INTERSECTION))
    G('crosshair',ring(8,8,5.05),lines('M8 1.2V4.6M8 11.4V14.8M1.2 8H4.6M11.4 8H14.8'))
    # SF viewfinder: four rounded corner brackets around a 12.6-unit field.
    scan_corner = 'M2.2 5.6V4.3Q2.2 2.2 4.3 2.2H5.6'
    scan=union(*(transform(stroke(scan_corner),90*i) for i in range(4)))
    G('focus',scan,ring(8,8,2.6))
    scanmarks={
        'eye':union(stroke('M4 8Q8 3 12 8Q8 13 4 8Z'),circle(8,8,1.05)),
        'heart':stroke('M8 11L4.5 7.5C2.5 4.7 6.4 3.6 8 6C9.6 3.6 13.5 4.7 11.5 7.5Z'),
        'line':line((4.6,8),(11.4,8)),
        'search':union(ring(7.4,7.4,2.75),line((9.1,9.1),(10.9,10.9))),
        'square':stroke(rr(5,5,6,6))}
    for n,m in scanmarks.items():G('scan-'+n,scan,m)
    lid = stroke('M2 5.85Q8 11.85 14 5.85')
    lash = stroke('M3.4 7.1L2.25 9M6.25 8.55L5.9 10.95')
    G('eye-closed',lid,union(lash,api['mirror'](lash)))
    G('eye-dashed',stroke('M1.5 8L3 6.3M5.5 4.8Q8 3.5 10.5 4.8M13 6.3L14.5 8M13 9.7L11.5 11M9 11.7H7M4.5 11L3 9.7'),ring(8,8,2))
    G('glasses',union(ring(4.5,9.5,2.8),ring(11.5,9.5,2.8)),stroke('M7.2 9Q8 8 8.8 9M1.7 9.5V6L3 3M14.3 9.5V6L13 3'))
    S('rectangle-goggles',path('M1.5 5H14.5V10Q14.5 12 12 12H10L8 9.5L6 12H4Q1.5 12 1.5 10Z'),stroke('M4 7H6M10 7H12'))
    S('lens',circle(),union(stroke(circle(8,8,3.8)),stroke(path('M6.25 7.55Q6.45 5.55 8.35 5.65Q8.4 7.6 6.25 7.55Z'))))
    axis = line((1.5,8),(14.5,8))
    for n,glass in [('concave',path('M4 2Q7 8 4 14H12Q9 8 12 2Z')),
                    ('convex',path('M8 1.5Q1 8 8 14.5Q15 8 8 1.5Z'))]:
        name = 'lens-'+n
        S(name,glass,axis)
        shell = union(glass,stroke(glass))
        overrides[name]={'solid':union(cut(shell,axis),cut(axis,shell))}
    S('mirror-rectangular',rr(3,1.5,10,10.5),union(lines('M8 12V14.5M5 14.5H11M5.5 6L7.45 4.05M6.8 8.55L10.25 5.1'),empty))
    S('mirror-round',circle(8,6.3,4.8),union(lines('M8 11.1V14.5M5 14.5H11M5.8 6.05L7.4 4.45M7.2 8.15L9.95 5.4')))
    overlapping('rectangle-circle',rr(1.55,2.2,10.5,9.15),circle(11.4,11.35,3.1),empty,empty)
    S('contrast',circle(),path('M8 2V14A6 6 0 0 0 8 2Z'))
    S('eclipse',path('M8 2A6 6 0 1 0 14 8Q8 9 8 2Z'),stroke('M11 1.5V3M13.5 2.5L12.5 4M14.5 5.5H13'))
    # SF sun.min uses dots for rays; sun.max uses short rays.
    S('sun-dim',circle(8,8,2.55),dots(*[(8+5.55*math.cos(i*math.pi/4),8+5.55*math.sin(i*math.pi/4)) for i in range(8)],r=.8))
    S('sun-medium',circle(8,8,2.85),union(*(line((8+4.95*math.cos(i*math.pi/4),8+4.95*math.sin(i*math.pi/4)),
                                                 (8+6.55*math.cos(i*math.pi/4),8+6.55*math.sin(i*math.pi/4))) for i in range(8))))
    moon = cut(circle(7.7,8.25,5.95),circle(10.45,5.55,5.35))
    S('moon-star',moon,star(12,3.9,.31))
    crescent = cut(circle(10.55,10.1,4.15),circle(12.45,7.95,3.7))
    S('sun-moon',union(circle(4.95,5.05,1.35),crescent),
      stroke('M4.95 1.25V1.6M1.25 5.05H1.5M2.05 2.15L2.5 2.6'))
    orbit = stroke('M2 10.95C-.55 5.3 10.15-.5 13.55 4.8C17 10.3 5.25 16.8 2 10.95Z')
    satellite = circle(4.3,4.65,1.4)
    G('orbit',union(cut(orbit,circle(4.3,4.65,2.45)),ring(8,8,1.85)),satellite)
    # A pair of open trailing arms around a detached galactic nucleus.
    arm = stroke('M2 10.15C.55 5.65 5.1 1.8 9.25 2.55C13.25 3.3 13.55 7.75 10.9 9.05Q10.1 9.45 9.65 9.25')
    G('galaxy',union(arm,transform(arm,180)),circle(8,8,.82))

    api['CATEGORY']='Health, science and accessibility'
    body = stroke('M8 5.55V8.75M3 6.35Q8 5.7 13 6.35M4.55 14.2L8 8.75L11.45 14.2')
    G('person-standing',circle(8,2.65,1.4),body)
    mouth=path('M1.65 7.75Q5.3 3.1 7.05 4.75Q8 5.55 8.95 4.75Q10.7 3.1 14.35 7.75Q8 15.25 1.65 7.75Z')
    mouthdetail=stroke('M2 8Q8 10 14 8')
    S('mouth',mouth,mouthdetail);off('mouth-off',source='mouth',min_area=1.5)
    S('pill-bottle',rr(4,4.5,8,10),union(stroke(rr(3.5,1.5,9,3)),plus(8,9.5,.85)))
    tablet = path('M2.9 4.6A2.45 2.45 0 0 1 7.8 4.6V7.25A2.45 2.45 0 0 1 2.9 7.25Z')
    score = line((2.9,5.925),(7.8,5.925))
    round_pill = circle(11.65,11.55,2.7)
    S('tablets',union(transform(tablet,-28),round_pill),
      union(transform(score,-28),line((9.74,13.46),(13.56,9.64))))
    bag = path('M6 3.9H10Q11.75 3.9 11.75 5.85V9.85Q11.75 11.75 9.7 11.75H6.3Q4.25 11.75 4.25 9.85V5.85Q4.25 3.9 6 3.9Z')
    S('iv-bag',bag,union(stroke('M6.45 3.9V2.85A1.55 1.55 0 0 1 9.55 2.85V3.9M8 11.75V13.05Q8 14.55 9.5 14.55H10.5M4.25 8.5Q6.1 7.6 8 8.5T11.75 8.5')))
    S('tube-lotion',path('M3.8 1.5H12.2L10.8 12H5.2Z'),union(stroke(rr(5,12,6,2.5)),stroke('M4.2 4H11.8'),circle(8,8,.8)))
    fragment = path('M1.6 5.1C.8 3.6 2 2.5 3.45 2.8C3.55 1.25 5.55 1.05 6.15 2.55Q6.6 3.6 5.95 4.55L8.1 6.7L6.4 6.55L6.45 8.2L4.2 5.95Q2.35 6.55 1.6 5.1Z')
    S('bone-fracture',union(fragment,transform(fragment,180)))
    for n,geometry in [
        ('venus',union(ring(8,5.5,3.5),lines('M8 9V14.5M5.5 12H10.5'))),
        ('mars',union(ring(6.5,9.5,4),lines('M9.3 6.7L14 2M10.5 2H14V5.5'))),
        ('non-binary',union(ring(8,10.5,3.5),lines('M8 7V1.5M5.5 2L10.5 5M10.5 2L5.5 5'))),
        ('mars-stroke',union(ring(5.65,10.35,3.65),lines('M8.1 7.9L14.1 1.9M10.65 1.9H14.1V5.35M9.05 4.65L11.35 6.95'))),
        ('transgender',union(ring(8,9.5,3.1),lines('M8 12V14.65M6.25 13.55H9.75M10 7L14 2.6M10.9 2.6H14V5.75M6 7L2 2.6M2 5.75V2.6H5.1M3.05 6.55L5.85 3.85'))),
        ('venus-and-mars',union(ring(5.55,6.65,3.5),ring(10,8.8,3.35),lines('M5.55 10.15V14.35M3.95 12.5H6.95M12.3 6.5L14.35 3.8M11.8 3.8H14.35V6.25'))),
    ]:G(n,geometry)
    # Glassware: bodies are filled surfaces; fluid lines and measuring ticks are details.
    S('beaker',path('M4 2H12V11Q12 14 8 14Q4 14 4 11Z'),stroke('M3 2H13M4 9H12M4 5H6M4 7H6'))
    S('flask-round',path('M6 1.5H10V6Q14 7 14 10.5Q14 14.5 8 14.5Q2 14.5 2 10.5Q2 7 6 6Z'),stroke('M5 1.5H11M2.5 10H13.5'))
    off('flask-conical-off',source='flask',center=(8.2,7.8),min_area=.6)
    tube=path('M6 2H10V11Q10 14.5 8 14.5Q6 14.5 6 11Z')
    S('test-tube-diagonal',transform(tube,40),transform(stroke('M5 2H11M6 8H10'),40))
    S('test-tubes',union(path('M2 2H6V10Q6 13 4 13Q2 13 2 10Z'),path('M10 4H14V12Q14 15 12 15Q10 15 10 12Z')),stroke('M1 2H7M9 4H15M2 8H6M10 10H14'))
    barrel = path('M7.7 1.55L10.55 3.35L7.55 8.1L4.7 6.3Z')
    pivot = circle(10.75,6,1.3)
    support = stroke('M5.3 6.65L4.55 7.85M11.85 6.65C15 10.6 11.2 13.6 8.75 13.6M2.35 10.1H8.3M7.1 10.1L9.05 13.6M3.1 13.6H13.45M4.05 13.6L5.95 10.1')
    S('microscope',union(barrel,pivot),support)
    overrides['microscope']={'solid':cut(union(barrel,stroke(barrel),pivot,stroke(pivot),support),
                                         circle(10.75,6,.85))}
    barrel = path('M3.5 5.55L12 3.95V9.35L3.5 7.85Z')
    S('telescope',transform(barrel,-23),union(transform(stroke('M1.95 6.65H3.5M12 3.25V10.05'),-23),
      stroke('M7.9 8.65V10.45M4.65 14.3L7.9 10.45L11.15 14.3')))
    # Use the same curves to define the strand and the clipping edge for its rungs.
    right_side = 'C10.6 4.4 11.45 5.65 11.45 8S10.6 11.6 8 13'
    strand = path('M5.35 1.8Q6.65 2.05 8 3'+right_side+'Q6.65 13.95 5.35 14.2')
    helix = union(stroke(strand),stroke(api['mirror'](strand)))
    middle = path('M8 3'+right_side+'C5.4 11.6 4.55 10.35 4.55 8S5.4 4.4 8 3Z')
    rungs = op(stroke('M4 5.85H12M4 8H12M4 10.15H12'),middle,po.PathOp.INTERSECTION)
    G('dna',transform(union(helix,rungs),20))
    off('dna-off',source='dna',min_area=1.4)
    for n,is_germ in [('virus',False),('germ',True)]:
        body=path('M4.55 4.8Q6.75 2 9.65 4Q13 4 12.25 7.85Q13.85 10.8 10.85 12.25Q7.5 14.15 5.55 11.75Q2.45 10.9 3.75 8Q2.45 5.55 4.55 4.8Z') if is_germ else circle(8,8,4.7)
        spokes = union(*(transform(line((8,3.85),(8,1.55)),i*45) for i in range(8)))
        spokes = cut(spokes,body)
        pores = union(ring(6.7,9.3,1.7),circle(9.65,6.35,.7)) if not is_germ else dots((6.15,9.55),(9.7,6.25),r=.76)
        S(n,body,union(spokes,pores))
        if is_germ:
            off('germ-off',source=n)
        else:
            off('virus-off',source=n,center=(9,7),min_area=1)
    sector = path('M6.2 6.96L4.46 5.95A4.1 4.1 0 0 1 8 3.9V5.92A2.08 2.08 0 0 0 6.2 6.96Z')
    S('radiation',circle(),union(circle(8,8,.95),*(transform(sector,i*120) for i in range(3))))
    claw = stroke('M6.65 1.5C3.65 3.25 5.1 5.7 8 5.7S12.35 3.25 9.35 1.5')
    lobe = union(claw,line((8,5.7),(8,6.7)))
    G('biohazard',union(*(transform(lobe,120*i) for i in range(3))),ring(8,8,1.8))

    api['CATEGORY']='Sports and outdoors'
    outer = circle(8,8,6.1)
    inner = circle(8,8,2.6)
    annulus = cut(outer,inner)
    bands = union(*(transform(line((8,1.9),(8,5.4)),45+90*i) for i in range(4)))
    bands = op(bands,annulus,po.PathOp.INTERSECTION)
    rims = union(stroke(outer),stroke(inner))
    ink = union(rims,bands)
    S('life-buoy',annulus,bands)
    overrides['life-buoy']={'duotone':[(cut(annulus,ink),.24),(ink,1)],'stroke':ink,
                            'solid':union(cut(annulus,bands),rims)}
    ball = path('M1.75 8C3.75 2.45 12.25 2.45 14.25 8C12.25 13.55 3.75 13.55 1.75 8Z')
    seam = stroke('M4.85 4.75Q7 8 4.85 11.25')
    S('rugby-ball',transform(ball,-36),transform(union(seam,api['mirror'](seam)),-36))
    seam = stroke('M8 8Q10.25 5.55 8.45 1.75M9.8 10.47Q13.25 8.1 11.85 3.1')
    seams = union(*(transform(seam,120*i) for i in range(3)))
    S('volleyball',circle(),op(seams,circle(),po.PathOp.INTERSECTION))
    wave_seams = stroke('M1.7 5.8Q5.75 2.9 8.3 7.35Q10.8 12.1 14.3 9.25M1.65 9.3Q5.25 7.35 7.25 11Q8.55 13.6 11 13.75')
    S('ball-wave',circle(),op(wave_seams,circle(),po.PathOp.INTERSECTION))
    water = stroke('M1.55 10.85Q3.15 9.35 4.75 10.85T7.95 10.85T11.15 10.85T14.35 10.85')
    rails = stroke('M4.75 10.85V3.15Q4.75 1.5 6.5 1.5M10.35 10.3V3.15Q10.35 1.5 12.1 1.5M4.75 4.65H10.35M4.75 7.5H10.35')
    G('waves-ladder',rails,union(water,transform(water,dy=3.15)))
    upper = path('M1.8 7.75L3.55 4.35Q4.05 3.7 4.55 4.55L6.25 6.55L8.4 5.9Q9.5 5.6 9.85 7L10.5 8.25C11.45 9.35 14.35 9 14.35 11.2V12.95H1.8Z')
    S('sport-shoe',upper,stroke('M1.95 10.95H14.15M10.5 8.25L9.65 10.95M6.55 6.55L5.85 8.1M8.85 6.6L8.15 8.15'))
    G('hockey-stick',stroke('M11 1.6L6.1 12.1Q5.5 13.5 4 13.5H1.8'),stroke(rr(9.6,11.55,4.3,2.7)))
    overrides['hockey-stick']={'solid':union(api['DRAWINGS']['hockey-stick'][0],rr(9.05,11,5.4,3.8))}
    grip = stroke('M6.4 3.9Q6.8 1.65 8.55 1.75Q10.15 1.95 9.6 3.65L6 14.4')
    G('hiking-stick',grip,line((5.05,12.05),(7.2,12.75)))
    G('fishing-hook',ring(9.65,3.1,2.05),stroke('M9.65 4.95V10.3C9.65 15.1 2.15 15.25 2.15 10.25V8.85L4.1 10.35'))
    rod = stroke('M2.65 14.15L6.75 5.5Q9.2 1.45 13.9 1.95')
    G('fishing-rod',rod,union(ring(6.2,10,1.7),stroke('M13.9 1.95V10.8Q13.9 13.25 12.05 13.25Q10.25 13.25 10.25 11.45')))
    whistle = path('M1.75 8.25Q1.75 6.2 3.85 6.2H6V7.55H8.25V6.2H14.25V8.95H10Q10 13.85 5.95 13.85Q1.75 13.85 1.75 9.8Z')
    S('whistle',whistle,union(ring(5.25,10.3,1.6),stroke('M5.85 3.9V2.15M8.55 4.15L9.55 2.6')))

    for n in ['battery-medium','battery-plus','battery-exclamation-point']:
        b,d=api['DRAWINGS'][n][:2]
        overrides[n]={'solid':union(stroke(b),d)}

    added=set(api['DRAWINGS'])-before
    # Some scoped names (SF badge variants) are composed earlier in draw.py.
    missing=set(NAMES)-set(api['DRAWINGS'])
    extra=added-set(NAMES)
    assert not missing, f'Missing technology recipes: {sorted(missing)}'
    assert not extra, f'Unexpected technology recipes: {sorted(extra)}'
