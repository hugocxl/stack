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
    def small(p, x=11.8, y=11.7, s=.52):
        return transform(p, scale=s, dx=x-8, dy=y-8)
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
    def warn(x=8,y=8,s=1): return union(line((x,y-2*s),(x,y+.4*s),width=1.2),circle(x,y+2.3*s,.6))
    def power(x=8,y=8,s=1):
        arc = transform(path('M4.65 4.45A4.8 4.8 0 1 0 11.35 4.45'),scale=s,dx=x-8,dy=y-8)
        return union(stroke(arc,1.2),line((x,y-5.7*s),(x,y-.6*s),width=1.25))
    def layers(n,b,d,body,source=None):
        # A modifier inherits the exact fitted paths of its base.
        if source:
            b,d,body,category,_ = api['DRAWINGS'][source]
            api['DRAWINGS'][n] = (b,d,body,category,n.replace('-',' '))
        else:
            (S if body else G)(n,b,d)
            b,d = api['DRAWINGS'][n][:2]
        if not body:
            ink = union(b,d)
            solid,mono = ink,ink
            if source == 'headphones':
                mono = union(b,stroke(d,1.1))
            duo = [(ink,1)]
        else:
            outer=stroke(b,1.25); ink=union(outer,d); filled=union(b,outer)
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

    def off(n,b=None,d=None,body=True,*,source=None,start=(1.8,1.8),end=(14.2,14.2),width=3,min_area=0):
        duo,solid,mono=layers(n,b,d or empty,body,source)
        gap=line(start,end,width=width)
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
        return union(stroke(rr(x-1.8,y,3.6,3,.5),1.15),stroke(f'M{x-1.1} {y}v-1.3a1.1 1.1 0 0 1 2.2 0v1.3',1.1))

    api['CATEGORY']='Technology and development'
    screen=rr(1.8,2.3,12.4,8.5,1.5)
    stand=lines('M8 10.8V14M5.2 14H10.8')
    marks={
        'activity':stroke('M3.5 7H5.5L6.7 4.5L8.3 8.5L9.5 6H12.5',1.05),
        'check':check(8,6.5,.65),'cloud':stroke('M5.2 8.3C3.4 8.3 3.5 5.7 5.4 5.7C5.8 3.1 9.7 3.2 10 5.7C12.7 5.4 12.8 8.3 10.6 8.3Z',1),
        'dot':circle(8,6.5,1.2),'down':arr('down',8,6.4,.65),
        'pause':lines('M6.5 4.5V8.5','M9.5 4.5V8.5'),
        'play':play(8,6.5,.8),'stop':rr(6.2,4.7,3.6,3.6,.3),
        'up':arr('up',8,6.4,.65),'x':cross(8,6.5,.7)}
    for state,m in marks.items(): S('monitor-'+state,screen,union(stand,m))
    S('tv-minimal',screen,lines('M5 10.8L4.2 13M11 10.8L11.8 13'))
    S('tv-minimal-play',screen,union(play(8,6.5,.8),lines('M5 10.8L4.2 13M11 10.8L11.8 13')))
    for n,top,base in [('monitor-pc',3.2,10.45),('computer',2.35,10.45),('monitor-speaker',3.2,10.45)]:
        display = rr(1.45,top,7.85,base-top,1)
        side = rr(11.55,2.8,3,10.65,.75)
        stand_mark = stroke('M5.4 10.45V13M3.7 13H7.1',1.25)
        if n=='monitor-speaker':
            display = rr(1.45,top,6.85,base-top,1)
            side = rr(10.6,2.8,4,10.65,.85)
            stand_mark = stroke('M4.9 10.45V13M3.3 13H6.5',1.25)
            face = union(circle(12.6,5.6,.65),circle(12.6,10.15,1.05))
        elif n=='computer':
            face = union(circle(13.05,5.45,.65),line((1.45,7.85),(9.3,7.85),width=1.1))
        else:
            face = union(line((11.55,6.65),(14.55,6.65)),circle(13.05,11.1,.62))
        S(n,union(display,side),union(stand_mark,face))
    S('pc-case',rr(4,1.5,8,13,1.2),union(lines('M4 5H12M6 3.3H10M6 7.5H10'),ring(8,11,1.6,.9)))
    S('monitor-smartphone',union(rr(1.3,2.8,10.2,7.7,1.2),rr(10.2,6.8,4.5,7.5,.8)),union(lines('M5.3 10.5V13M3.4 13H7.3'),stroke(rr(10.2,6.8,4.5,7.5,.8),1.1),line((11.8,12.8),(13.1,12.8),width=.9)))
    S('tablet-smartphone',union(rr(1.8,1.5,9.5,12.5,1.2),rr(9,6.5,5.3,8,1)),union(stroke('M9 6.5H13.3Q14.3 6.5 14.3 7.5V13.5Q14.3 14.5 13.3 14.5H10Q9 14.5 9 13.5Z',1.1),dots((6,12),(11.7,12.8),r=.45)))

    laptop=rr(3,2.3,10,8.5,1)
    foot=stroke('M3 10.8L1.5 13H14.5L13 10.8',1.2)
    S('laptop-minimal',laptop,foot)
    S('laptop-minimal-check',laptop,union(foot,check(8,6.6,.7)))
    phone=rr(4.5,1.5,7,13,1.6)
    S('smartphone-charging',phone,union(poly([(8.5,4.3),(6.2,8.3),(8.3,8.3),(7.2,11.6),(10,7),(7.9,7)]),line((7,12.7),(9,12.7),width=.9)))
    S('vibrate',rr(5,2.5,6,11,1.1),lines('M2.5 5L1.3 8L2.5 11M13.5 5L14.7 8L13.5 11'))
    off('vibrate-off',rr(5,2.5,6,11,1.1),lines('M2.5 5L1.3 8L2.5 11M13.5 5L14.7 8L13.5 11'))
    S('mouse-left',rr(4,1.5,8,13,4),union(stroke('M4.2 7H11.8M8 1.8V7',1.1),rr(5.1,3.1,1.7,2.5,.6)))
    S('mouse-right',rr(4,1.5,8,13,4),union(stroke('M4.2 7H11.8M8 1.8V7',1.1),rr(9.2,3.1,1.7,2.5,.6)))
    off('mouse-off',rr(4,1.5,8,13,4),line((8,3),(8,6)))
    S('card-sim',path('M5 1.5H11.7V14.5H3V3.5Z'),union(stroke(rr(5,7,5,5,.5),1.1),stroke('M7.5 7.2V11.8M5.2 9.5H9.8',1.05)))
    battery=rr(1.5,4,11.5,8,1.3)
    for n,m in [('medium',rr(3.4,6.2,4.5,3.6,.4)),('plus',plus(7,8,.65)),('exclamation-point',warn(7,8,.8))]:
        S('battery-'+n,battery,union(m,line((14.7,6.8),(14.7,9.2))))
    for n,direction in [('upload','up')]:
        S('hard-drive-'+n,rr(1.7,5.5,12.6,8,1.5),union(lines('M2 10H14'),dots((11.3,11.8),(13,11.8),r=.4),arr(direction,8,4.6,.85)))
    drive = rr(1.8,8.1,12.4,6.05)
    S('hard-drive-download',drive,union(stroke('M8 1.4V6M5.9 3.9L8 6L10.1 3.9M1.8 10.9H14.2'),circle(11.65,12.55,.55)))
    for n,m in [('check',check(8,11.5,.5)),('x',cross(8,11.5,.5))]:
        S('printer-'+n,rr(1.8,5,12.4,7,1.5),union(stroke('M4 5V1.8H12V5M4.2 9H11.8V14H4.2Z',1.1),m,circle(12,7,.5)))
    gantry = rr(2,2,12,12)
    head = path('M6.4 2H9.6V4.35L8 6.1L6.4 4.35Z')
    print_part = path('M5 12V9.85H6.6V8.15H9.35V9.85H11V12Z')
    ink = union(stroke(gantry),stroke(head),stroke(print_part),line((2,12),(14,12)))
    G('printer-3d',ink)
    overrides['printer-3d']={'solid':union(ink,head,print_part)}
    S('projector',rr(1.8,5,12.4,7,1.4),union(ring(10.4,8.5,2.1,1.05),lines('M4 12L3.4 14M12 12L12.6 14M3.5 7.5H5.5M3.5 9.5H5.5')))
    S('robot-vacuum',circle(8,9,5.7),union(stroke('M2.6 8H13.4',1.1),rr(6,4.5,4,2,.6),circle(8,10.8,.7)))
    foot = rr(1.8,11.75,7,2.6)
    pivots = union(circle(4.6,9,1.45),circle(8.8,4.7,1.4))
    links = stroke('M4.6 11.75V10.45M5.65 7.95L7.8 5.7M10.2 4.7L12.05 4M12.05 4L12 2.2L14 1.6M12.05 4L13.25 5.55L14.65 5')
    S('robot-arm',union(foot,pivots),links)
    # Opposed plug backs share one S-bend. The pins face away from the cord.
    plug_ends = union(rr(1.8,3,4.4,3.9,.8), rr(9.8,9.1,4.4,3.9,.8))
    S('cable', plug_ends, stroke('M2.65 3V1.5H5.35V3M10.65 13V14.5H13.35V13M4 6.9V9.7C4 13 8 13 8 9V7C8 3 12 3 12 6.3V9.1',1.25))
    plug=path('M4 5H12V8Q12 11 8 11Q4 11 4 8Z')
    S('plug-2',plug,lines('M6 1.5V5M10 1.5V5M8 11V14.5'))
    S('plug-zap',path('M2 5H9V8Q9 11 5.5 11Q2 11 2 8Z'),union(lines('M3.5 2V5M7.5 2V5M5.5 11V14'),poly([(12,2),(9.5,7.5),(12,7.5),(10.5,13),(14.5,6),(12,6)])))
    plug_half = path('M2.75 5.7H5.7V10.3H2.75Q1.75 8 2.75 5.7Z')
    socket_half = path('M10.55 5.7H13.1Q14.25 8 13.1 10.3H10.55Z')
    terminals = stroke('M5.7 6.8H7.65M5.7 9.2H7.65M1.35 8H2.35M13.7 8H14.65',1.2)
    S('unplug',transform(union(plug_half,socket_half),-35),transform(terminals,-35))
    S('usb-c-port',rr(1.7,4.5,12.6,7,3.5),stroke(rr(4,6.9,8,2.2,1.1),1.05))
    S('hdmi-port',path('M2 4H14V9L11.5 12H4.5L2 9Z'),union(line((5,7),(11,7),width=1.3),dots((5.5,9.4),(8,9.4),(10.5,9.4),r=.4)))
    S('midi-port',circle(8,8,6),dots((4.5,8),(5.5,5.2),(8,4.3),(10.5,5.2),(11.5,8),r=.65))
    S('microchip',rr(4.2,4.2,7.6,7.6,1),union(stroke(rr(6.3,6.3,3.4,3.4,.4),1),lines('M5 1.5V4M8 1.5V4M11 1.5V4M5 12V14.5M8 12V14.5M11 12V14.5M1.5 5H4M1.5 8H4M1.5 11H4M12 5H14.5M12 8H14.5M12 11H14.5')))
    S('cpu-ai',rr(3.5,3.5,9,9,1.2),union(stroke('M5.5 10L6.8 6L8.2 10M6 8.5H7.6M10 6V10',1),lines('M5 1V3M11 1V3M5 13V15M11 13V15M1 5H3M1 11H3M13 5H15M13 11H15')))
    fan_center = (6.35,7.25)
    blade = stroke('M6.35 7.25Q4.05 6.4 4.55 4.65')
    def fan_blade(angle):
        return transform(transform(blade,dx=1.65,dy=.75),angle,dx=-1.65,dy=-.75)
    fan = union(*(fan_blade(i*120) for i in range(3)),circle(*fan_center,.8),ring(*fan_center,3.7))
    S('gpu',rr(1.55,2.45,12.9,9.6),union(fan,stroke('M11.25 5.8H12.95V8.7H11.25ZM4.6 12.05V14.05M7.6 12.05V14.05M10.6 12.05V14.05')))
    S('circuit-board',rr(1.5,1.5,13,13,1.3),union(stroke(rr(6,6,4,4,.6),1),stroke('M3.5 4H7V6M3.5 11H6V9M10 7H12V4M9 10V12H12',1),dots((3.5,4),(3.5,11),(12,4),(12,12),r=.6)))
    freight = rr(1.5,4,13,8,.65)
    corner = rr(1.65,4.15,1.6,1.6,.3)
    corners = union(corner,api['mirror'](corner),transform(corner,180),transform(api['mirror'](corner),180))
    S('container', freight, union(corners,stroke('M5 6.1V9.9M8 6.1V9.9M11 6.1V9.9',1.2)))
    server=rr(2.2,1.7,11.6,12.6,1.2)
    serverdetail=union(lines('M2.2 5.8H13.8M2.2 10H13.8'),dots((4.5,3.8),(4.5,7.8),(4.5,12),r=.55))
    badge('server-plus',server,serverdetail,plus(12,11.8,.8))
    badge('server-crash',server,serverdetail,warn(12,11.5,.85))
    S('server-nas',rr(1.8,3,12.4,10.5,1),union(stroke(rr(4,5,2.6,6.5,.6),1),stroke(rr(9.4,5,2.6,6.5,.6),1),dots((5.3,10),(10.7,10),r=.45)))


    for n,d in [('arrow-down',arr('down',12,11.6,.8)),('arrow-up',arr('up',12,11.6,.8)),('zap',poly([(12,8),(9.5,12),(12,12),(11,15),(14.5,10.5),(12,10.5)]))]: badge('database-'+n,None,None,d,source='database',radius=3.5)
    cloud=path('M4.2 13C.3 13 .5 7 4.3 7C4.5 1.5 12 1.5 12.5 7C16.3 7 16 13 12.5 13Z')
    badge('cloud-cog',cloud,empty,cog())
    S('cloud-exclamation-point',cloud,warn(8,9,.85))
    wifi=stroke('M1.5 4.8Q8-.4 14.5 4.8M4 7.6Q8 4.2 12 7.6M6.5 10.4Q8 9.2 9.5 10.4',1.25)
    wd=circle(8,13,.8)
    for n,m in [('cog',cog()),('lock',lock()),('pen',stroke('M10 13.8L10.5 11.5L13.5 8.5L15 10L12 13Z',1.1)),('sync',stroke('M10 10Q13 8 14.5 10.5V9M14.5 13Q11.5 15 10 12.5V14',1.15))]: badge('wifi-'+n,None,None,m,source='wifi',x=12,y=11.8,radius=3.55)
    G('antenna',union(stroke('M3.5 6A5.5 5.5 0 0 1 12.5 6M5.5 7.8A3 3 0 0 1 10.5 7.8',1.2),circle(8,8.6,.75)),lines('M8 11.1V14M5 14H11'))
    G('radio-tower',stroke('M2 7A8 8 0 0 1 3.5 2M14 7A8 8 0 0 0 12.5 2M5 6A4 4 0 0 1 5.8 3M11 6A4 4 0 0 0 10.2 3',1.15),union(circle(8,4.5,.8),lines('M8 5.5L4.8 14.2M8 5.5L11.2 14.2M6.3 10H9.7M5.4 12.5H10.6')))
    panels = union(rr(1.35,5.55,3.25,4.9,.35),rr(11.4,5.55,3.25,4.9,.35))
    bus = rr(6.35,4.85,3.3,6.3,.75)
    links = stroke('M4.6 8H6.35M9.65 8H11.4M8 4.85V2.65M1.35 8H4.6M11.4 8H14.65',1.2)
    S('satellite',transform(union(panels,bus),-32),transform(union(links,line((7.05,2.65),(8.95,2.65),width=1.2)),-32))
    bowl = path('M2.2 3.6Q5.75 7.85 12.55 10.2C7.55 13.55 1.35 10.2 2.2 3.6Z')
    S('satellite-dish',bowl,union(stroke('M7.15 8.15L9.8 4.25M7.25 11.3L5.95 14H10.8L8.9 11.4',1.3),circle(10.15,3.65,1.05)))
    webcam= circle(8,6,4.5)
    off('webcam-off',webcam,union(ring(8,6,1.7,1),lines('M8 10.5V13.5M4.5 13.5H11.5')))
    S('flashlight',path('M4 2H12V5L10 7V14H6V7L4 5Z'),lines('M4 5H12M6 9H10'))
    off('flashlight-off',path('M4 2H12V5L10 7V14H6V7L4 5Z'),lines('M4 5H12M6 9H10'))
    gong = circle(6.25,6,4.45)
    hammer = circle(13.1,8.55,1.25)
    S('bell-electric',union(gong,hammer),union(circle(6.25,6,.7),stroke('M6.25 10.45V13.85H13.1V9.8')))
    siren=path('M4 12V8C4 2.5 12 2.5 12 8V12Z')
    sd=lines('M2 13.5H14M8 1V2M1.5 5L3 6M13 6L14.5 5M8 6V9')
    S('siren',siren,sd);off('siren-off',siren,sd)
    S('spotlight',transform(rr(2.3,3.5,9,5.5,1),-30),lines('M8 9V14M4.5 14H11.5M12 2L14.5 1M13 5H15M12.5 8L14.5 9'))

    # Developer diagrams use genuine node topology and arrow direction.
    book=rr(2.8,1.7,10.4,12.6,1.1)
    spine=stroke('M5 1.8V14.2M3 11.7H13',1.05)
    bookmarks={
        'down':arr('down',9,6.8,.7),'up':arr('up',9,6.8,.7),
        'up-2':stroke('M7.15 5.5L9 3.75L10.85 5.5M7.15 8.55L9 6.8L10.85 8.55M9 6.8V9.85',1.1),
        'audio':stroke('M7 5V8M9 4V9M11 5V8',1.1),
        'headphones':union(stroke('M7.35 7.4V6.55A1.85 1.85 0 0 1 11.05 6.55V7.4',1.12),rr(6.8,6.85,1.45,2.35,.55),rr(10.15,6.85,1.45,2.35,.55)),
        'image':union(stroke('M5.15 10.45L8.45 6.85L13.1 10.45'),ring(10.55,4.85,1.52)),
        'key':union(ring(8,5.5,1.3,.9),stroke('M9 6.5L11.5 9M10.5 8L11.5 7',1))}
    for n,m in bookmarks.items(): S('book-'+n,book,union(spine,m))
    G('book-dashed',stroke('M5.5 2H4Q2.8 2 2.8 3.3V12.4Q2.8 13.7 4 13.7H5.5ZM8.1 2H9.3M11.8 2H13.25V4.65M13.25 7.3V9M13.25 11.6V13.7H11.65M8.95 13.7H8',1.25))
    S('bot-message-square',path('M2 3H14V11H7L3 14V11H2Z'),union(dots((5.5,6.5),(10.5,6.5),r=.75),line((6,9),(10,9),width=1.1),line((8,1),(8,3))))
    off('bot-off',source='bot',start=(1.5,3.65),end=(12.7,14.85),width=3.25,min_area=1.55)
    brain=path('M8 3Q4 0 2.5 3Q1 4 2.5 6Q.5 8 2 10Q2.8 12 4.5 11.5Q4 15 8 13Q12 15 11.5 11.5Q14.5 12 14.5 8Q15 6 13.5 5Q14.5 1 11 1.8Q9.5 1 8 3Z')

    badge('brain-cog',None,None,cog(),source='brain',x=12.05,y=11.95,radius=3.8,min_area=1.3)
    S('brain-circuit',brain,stroke('M8 3V13M4.05 4.8V7.9H5.7M11.9 4.9V7.7H10.25V10.5',1.15))
    off('brain-off',source='brain',width=3.3,min_area=1.7)
    off('bug-off',source='bug',width=3.45,min_area=1.8)
    badge('bug-play',None,None,play(12,11.8,1),source='bug',radius=3.65,min_area=1.85)
    S('blocks',union(rr(1.5,8.8,5.5,5.5,.7),rr(8.8,8.8,5.5,5.5,.7),rr(5.2,1.5,5.5,5.5,.7)))
    S('boxes-linked',union(rr(1.5,2,4.5,4.5,.6),rr(10,2,4.5,4.5,.6),rr(5.8,10,4.5,4.5,.6)),stroke('M3.75 6.5V8.35H12.25V6.5M8 8.35V10',1.25))
    tab = 'h2.55q.45 0 .65 .5l.25 .65h2.3l.3-.65q.2-.5 .65-.5'
    # The two edges use the same tab and a constant vertical offset.
    joint = path('M2 6.7'+tab+'H14V2.2H2Z')
    lower = path('M2 9.35'+tab+'H14V14H2Z')
    S('scratch-blocks',union(joint,lower))
    G('chevrons-left-right-ellipsis',lines('M3.65 4.2L1.5 8L3.65 11.8M12.35 4.2L14.5 8L12.35 11.8'),dots((5.65,8),(8,8),(10.35,8),r=.69))
    G('parentheses',stroke('M5 2Q.5 8 5 14'),stroke('M11 2Q15.5 8 11 14'))
    G('option',lines('M2 3H5L11 13H14'),line((9,3),(14,3)))
    G('variable',stroke('M3 4Q6 2 7 6L9 11Q10 14 13 12M4 12L12 4',1.35),empty)
    G('radical',line((1.5,8),(4.2,11.5),(7,3),(14.5,3)),empty)
    G('form', line((2.2,1.8),(7,1.8),width=1.2),
      union(stroke(rr(2,4.4,12,3.6,.8),1.25),stroke(rr(2,10.45,12,3.6,.8),1.25)))
    for n,detail in [('minus',line((10,12),(14,12))),('plus',plus(12,12,.8))]:
        badge('git-branch-'+n,union(circle(4,3,1.5),circle(4,13,1.5),circle(12,3,1.5)),stroke('M4 4.5V11.5M12 4.5Q12 8 4 8',1.2),detail)
    S('git-commit-vertical',circle(8,8,2.8),lines('M8 1.5V5.2M8 10.8V14.5'))
    S('git-graph',union(circle(3.5,3,1.4),circle(3.5,12.7,1.4),circle(12.5,4.5,1.4),circle(12.5,12.7,1.4)),stroke('M3.5 4.4V11.3M12.5 5.9V11.3M3.5 7Q8 7 8 10Q8 12.7 11.1 12.7',1.2))
    S('git-merge-conflict',union(circle(3.5,3,1.4),circle(3.5,13,1.4),circle(12.5,3,1.4)),union(stroke('M3.5 4.4V11.6M12.5 4.4Q12.5 7 9 7',1.2),cross(11.5,11.7,.9)))
    G('git-compare-arrows',union(stroke('M4 3V12M2 10L4 12L6 10M12 13V4M10 6L12 4L14 6',1.25),ring(4,2,1.2,1)),ring(12,14,1.2,1))
    requestbody=union(circle(4,3,1.4),circle(4,13,1.4),circle(12,13,1.4))
    requestline=stroke('M4 4.4V11.6M12 11.6V6Q12 3 9 3',1.2)
    for n,m in [('closed',cross(11.5,3.3,.85)),('create',plus(11.5,3.3,.8))]:
        S('git-pull-request-'+n,requestbody,union(cut(requestline,rr(8,0,8,6,0)),m))
    for n in ['arrow','create-arrow']:
        nodes = union(circle(3.1,3.4,1.45),circle(3.1,12.5,1.45),circle(12.5,12.5,1.45))
        branch = stroke('M3.1 4.85V11.05M12.5 11.05V7.2Q12.5 3.8 9.1 3.8H7.2M9.35 1.65L7.2 3.8L9.35 5.95',1.25)
        mark = plus(7.65,10.35,.7) if n=='create-arrow' else empty
        S('git-pull-request-'+n,nodes,union(branch,mark))
    G('git-pull-request-draft',union(ring(4,3,1.4,1.1),ring(4,13,1.4,1.1),ring(12,13,1.4,1.1)),union(line((4,4.4),(4,11.6)),dots((12,4),(12,7),(12,10),r=.65)))
    off('webhook-off',source='webhook',start=(1.55,1.75),end=(13.95,14.15),width=3.1,min_area=.8)
    G('merge',stroke('M2 2V5Q2 8 8 8M14 2V5Q14 8 8 8M8 8V14M5.5 11.5L8 14L10.5 11.5'))
    fork = stroke('M8 10.8C8 8.3 5.9 6.3 2.55 3M2.55 6.55V3H6.1')
    G('split',line((8,14.35),(8,10.8)),union(fork,api['mirror'](fork)))
    S('combine',union(rr(1.5,1.5,5,5,.7),rr(9.5,1.5,5,5,.7),rr(5.5,10,5,4.5,.7)),lines('M4 6.5V8H12V6.5M8 8V10'))
    for n,coords,edges in [
        ('graph-hub',[(8,8),(2,3),(14,3),(2,13),(14,13)],[(0,1),(0,2),(0,3),(0,4)]),
        ('graph-ring',[(8,2),(13.7,6),(11.5,13),(4.5,13),(2.3,6)],[(0,1),(1,2),(2,3),(3,4),(4,0)])]:
        nodes=union(*(circle(x,y,1.15) for x,y in coords))
        conn=union(*(line(coords[a],coords[b],width=1.05) for a,b in edges))
        S(n,nodes,cut(conn,union(*(circle(x,y,1.45) for x,y in coords))))

    # Each vertex is a node on the pentagram. Clip chords at the node faces.
    tips = [(8 + 5.95*math.sin(i*math.tau/5), 8.5 - 5.95*math.cos(i*math.tau/5)) for i in range(5)]
    nodes = union(*(circle(x,y,1.25) for x,y in tips))
    chords = union(*(line(tips[i],tips[(i+2)%5]) for i in range(5)))
    S('graph-star',nodes,cut(chords,nodes))

    api['CATEGORY']='Media and communication'
    G('play-triangle',play(8,8,2.35))
    G('pause-bars',rr(3.5,2,3,12,1),rr(9.5,2,3,12,1))
    S('video-camera',rr(1.5,4,8.5,8,1.5),poly([(10,6.5),(14.5,4),(14.5,12),(10,9.5)]))
    wave = stroke('M3.55 2.5Q.05 8 3.55 13.5M5.65 4.95Q3.85 8 5.65 11.05',1.35)
    G('radio-signal',union(wave,api['mirror'](wave)),circle(8,8,1.05))
    speaker=path('M2 6H5L9.5 2.5V13.5L5 10H2Z')
    S('volume-none',speaker)
    off('volume-slash',speaker,empty)
    wave=stroke('M2 6V10M5 3.5V12.5M8 1.8V14.2M11 4.5V11.5M14 6V10',1.25)
    G('audio-lines',wave)
    off('audio-lines-off',source='audio-lines',start=(1.6,2.05),end=(13.95,14.4),width=3.25,min_area=1.6)
    badge('audio-lines-x',wave,empty,cross(12,11.8,.8),False)
    G('eject',poly([(8,2),(14,10),(2,10)]),line((2.5,13),(13.5,13)))
    G('step-back',play(7,8,1.7).transform(-1,0,0,1,16,0),line((3,3),(3,13)))
    G('step-forward',play(7,8,1.7),line((13,3),(13,13)))
    off('play-off',source='play-triangle',start=(1.3,3.3),end=(12.7,14.7),width=3.1,min_area=1.55)
    G('repeat-1',stroke('M3 9V5Q3 3 5 3H13M13 7V11Q13 13 11 13H3M11 1L13 3L11 5M5 11L3 13L5 15',1.2),stroke('M7 6L8.5 5V10M7 10H10',1))
    S('closed-caption',rr(1.5,3,13,10,1.5),stroke('M6.5 5.5C3 4 2.5 11 6.5 10M12.7 5.5C9 4 8.5 11 12.7 10',1.15))
    S('hd',rr(1.5,3,13,10,1.5),stroke('M4 5.5V10.5M7 5.5V10.5M4 8H7M9.5 5.5H10.5Q13 5.5 13 8Q13 10.5 10.5 10.5H9.5Z',1.1))
    S('ad',rr(1.5,3,13,10,1.5),stroke('M3.25 10.7L5.35 5.4L7.45 10.7M4.1 9.1H6.6M9.45 5.5H10.5Q13 5.5 13 8Q13 10.5 10.5 10.5H9.45Z',1.1))
    slate = rr(1.75,7.5,12.5,6.4,1)
    clap = path('M1.75 5.45L13.15 1.55L13.8 3.6L2.45 7.5Z')
    cuts = op(stroke('M5.2 4.05L7 5.95M9 2.85L10.8 4.75',1.15),clap,po.PathOp.INTERSECTION)
    S('clapperboard',union(slate,clap),cuts)
    S('boom-box',rr(1.5,5.6,13,7.9,1.3),union(stroke('M5.35 5.6V3.1H10.65V5.6M2.05 5.7L3.35 1.6',1.2),ring(5,9.55,2.15,1.1),ring(11,9.55,2.15,1.1)))
    S('cassette-tape',rr(1.5,3.3,13,9.4,1.2),union(stroke(rr(3.5,5.2,9,3.8,1.9),1.1),dots((5.4,7.1),(10.6,7.1),r=.65),stroke('M5 10L4 12.7M11 10L12 12.7M5 10H11',1.05)))
    S('videotape',rr(1.5,3.3,13,9.4,1),union(ring(4.5,7.2,1.6,.9),ring(11.5,7.2,1.6,.9),stroke(rr(4.5,10,7,1.2,.3),.8),line((6.2,7.2),(9.8,7.2),width=.9)))
    for n,arc,angle in [('2','M4.1 8A3.9 3.9 0 0 1 8 4.1',180),('3','M5.65 4.9A3.9 3.9 0 0 1 11.85 8.65',180)]:
        groove = stroke(arc,1.12)
        S('disc-'+n,circle(),union(ring(8,8,1.65),groove,transform(groove,angle)))
    S('disc-album',rr(1.5,1.5,13,13,1),union(stroke(circle(8,8,4.3)),ring(8,8,1.7)))
    S('turntable',rr(1.5,3,13,10,1),union(ring(6.5,8,3.3,1.1),circle(6.5,8,.7),stroke('M11.5 5V8.5L10 10',1.2),circle(11.5,5,.65)))
    G('circle-fading-play',union(stroke('M8 1.8A6.2 6.2 0 1 1 1.8 8',1.25),dots((2.5,5),(4.6,2.7),r=.62)),play(8.5,8,.95))
    S('circle-power',circle(),power(8,8,.63))
    S('circle-star',circle(),star(8,8,.48))
    G('circle-slash',ring(),line((4.4,11.6),(11.6,4.4)))
    G('circle-slash-2',ring(),line((4.4,4.4),(11.6,11.6)))
    def overlapping(n,rear,front,rear_detail,front_detail):
        # Paint the front object once, with the same clearance in all three styles.
        rear_ink = union(stroke(rear,1.25),rear_detail)
        front_ink = union(stroke(front,1.25),front_detail)
        clear = union(front,stroke(front,3.15))
        ink = union(cut(rear_ink,clear),front_ink)
        surface = cut(union(cut(rear,clear),front),ink)
        def filled(body,detail):
            shell = union(body,stroke(body,1.25))
            return union(cut(shell,detail),cut(detail,shell))
        S(n,union(rear,front),union(rear_detail,front_detail))
        overrides[n]={'duotone':[(surface,.24),(ink,1)],'stroke':ink,
                      'solid':union(cut(filled(rear,rear_detail),clear),filled(front,front_detail))}
    rear_mask = path('M1.55 2.75Q4.95 1.3 8.3 2.65L8.05 6.6Q8 9.45 5 10.45Q2.05 9.7 1.85 6.8Z')
    front_mask = path('M7.05 6.45Q10.8 7.55 14.45 5.4L14.15 9.65Q14.05 12.8 11.2 14.1Q7.8 13.45 7.35 10.35Z')
    overlapping('drama',rear_mask,front_mask,union(dots((3.65,4.55),(6.3,4.4),r=.57),stroke('M3.7 7.2Q4.85 8.6 6 7.05',1.05)),
                union(dots((9.3,8.9),(12.35,8.5),r=.6),stroke('M9.5 11.9Q10.65 9.9 12.25 11.45Q11.1 13.25 9.5 11.9Z')))
    G('list-music',lines('M2 3H10M2 6H8M2 9H7M2 12H6'),union(stroke('M11 11V3L14 2V10',1.2),circle(9.8,11.5,1.25),circle(12.8,10.5,1.25)))
    G('list-video',lines('M2 3H14M2 6H8M2 9H6M2 12H6'),play(11,10.5,1.2))
    mic=rr(5.5,1.5,5,8,2.5)
    md=stroke('M3.5 6.5V8Q3.5 12 8 12Q12.5 12 12.5 8V6.5M8 12V14.5M5.5 14.5H10.5',1.2)
    S('mic-audio-lines',rr(3.5,2,4,8,2),union(stroke('M1.5 7V8.5Q1.5 12 5.5 12Q9 12 9 9M5.5 12V14.5',1.1),stroke('M11 5V10M13.5 3V12',1.1)))
    S('mic-signal',mic,union(md,stroke('M12 2.5Q15 5 13.8 8M2.3 2.5Q0 5 1.3 8',1)))
    grille = rr(5.15,1.45,5.7,6.4,2.8)
    handle = path('M6.25 6.95H9.75L9 13.7Q8.8 14.5 8 14.5T7 13.7Z')
    S('mic-vocal',transform(union(grille,handle),39),
      transform(stroke('M5.3 4.6H10.7M6.25 7.1Q8 8.25 9.75 7.1',1.15),39))
    headphones=stroke('M2.5 9V7A5.5 5.5 0 0 1 13.5 7V9',1.35)
    ears=union(rr(2,8,3,5,1.1),rr(11,8,3,5,1.1))
    off('headphone-off',ears,headphones)
    buds=union(path('M3.5 2Q1 2 1.5 5Q1.8 7 4 7V12Q4 14 6 14V5Q6 2 3.5 2Z'),path('M12.5 2Q15 2 14.5 5Q14.2 7 12 7V12Q12 14 10 14V5Q10 2 12.5 2Z'))
    bd=lines('M3.5 4.5V5.5M12.5 4.5V5.5')
    S('earbuds',buds,bd);off('earbuds-off',buds,bd)
    off('megaphone-off',source='megaphone',start=(1.8,1.45),end=(14.55,14.2),width=3.3,min_area=2)
    radio=rr(1.5,5,13,9,1.5)
    off('radio-off',radio,union(line((3,5),(12,1.5)),ring(5.5,9.5,2,1),lines('M10 8H12M10 11H12')))
    S('phone-forwarded',path('M2 2H5L6.2 5.5L4.5 7Q6.5 10.5 9.5 11.5L11 9.8L14 11V14Q5 16 1.5 5Z'),arr('right',11,4,.85))
    S('phone-log',path('M2 2H5L6.2 5.5L4.5 7Q6.5 10.5 9.5 11.5L11 9.8L14 11V14Q5 16 1.5 5Z'),lines('M9 2H14M10 4.5H14M11 7H14'))
    S('speech',path('M1.5 2H11.5V9H6L3 12V9H1.5Z'),stroke('M4 5.5H8.5M13 7Q16 10 13 13M11.5 9Q13 10 11.5 11',1.1))

    # Musical notation is monochrome; instrument bodies carry physical depth.
    G('eighth-note',union(stroke('M9.5 11V2Q13 3 12 6',1.35),circle(7.7,11.8,2)),empty)
    G('half-note',ring(6.4,12,2,1.2),line((8.4,12),(8.4,2),width=1.35))
    G('sixteenth-notes',union(circle(3.5,12,1.7),circle(11.5,10,1.7)),stroke('M5 12V3L13 1V10M5 5.8L13 3.8',1.35))
    G('clef-bass',union(stroke('M3 5Q3 1 7 2Q13 5 3 13',1.5),circle(3.2,5,.95)),dots((12,4),(12,7),r=.8))
    G('clef-treble',stroke('M6.5 13.3Q5.3 15 7.5 15Q9.8 15 9.5 13L7.5 3.5Q7 1 8.8 1Q11 1.5 9 4.8L5.2 8Q2.5 10.5 5.7 12Q9.5 14 11.4 10.3Q12.5 7 9.2 6.6Q6.4 6.2 6 9Q5.7 10.5 7.7 10.8',1.2),empty)
    clef_lobe = stroke('M7.45 3.7C8.35 .9 13 1.6 13.1 4.65C13.2 7.15 11.6 8 10 8Q9.05 8 8.6 7.2',1.3)
    G('clef-alto', union(line((2.5,2),(2.5,14)), line((5.1,2),(5.1,14),width=1.1)),
      union(clef_lobe,clef_lobe.transform(1,0,0,-1,0,16),stroke('M8.6 6.1L6.6 8L8.6 9.9')))
    S('drum',path('M2 4Q8 0 14 4V12Q8 16 2 12Z'),union(stroke('M2 4Q8 8 14 4M2 12L5 6L8 14L11 6L14 12',1.1),lines('M1.5 1L7 3M14.5 1L9 3')))
    S('metronome',poly([(6,1.7),(10,1.7),(14,14),(2,14)]),union(lines('M5 11H11M8 10L11 4'),circle(11,4,.7)))
    # Construct neck, headstock and bridge on one axis before rotating the instrument.
    head = rr(7.05,.8,1.9,2.5,.5)
    neck = rr(7.45,2.7,1.1,5.7,.25)
    acoustic = path('M8 6.8C10.25 6.45 11.35 7.7 10.65 9.3Q10.25 10.15 11.1 10.95C13.4 13.85 10.6 15.1 8 15.1S2.6 13.85 4.9 10.95Q5.75 10.15 5.35 9.3C4.65 7.7 5.75 6.45 8 6.8Z')
    electric = path('M5.1 6.05Q6.1 8.5 7.6 7.6L8.5 7.35Q10.05 8.65 11.2 6.5C11.85 8.55 9.75 9.8 11.15 11.1C13.25 13.6 10.3 15.1 8 15.1C4.8 15.1 3.4 13.6 4.6 11.55Q5.6 10.1 5.1 9.05Q4.45 7.65 5.1 6.05Z')
    for n,wood,detail in [('guitar',acoustic,ring(8,9.45,1.65)),
                          ('guitar-electric',electric,line((7.05,9.85),(8.95,9.85),width=1.15))]:
        body = transform(union(wood,neck,head),36)
        bridge = line((6.75,12.5),(9.25,12.5),width=1.12)
        S(n,body,transform(union(detail,bridge),36))
    for n,top,bottom in [('piano',2.25,13.75),('keyboard-music',4,12)]:
        body = rr(1.5,top,13,bottom-top,1.05)
        rail = top+2.35 if n=='piano' else top
        keys = union(*(line((x,rail),(x,bottom),width=1.05) for x in (4.75,8,11.25)))
        black_keys = union(*(rr(x-.93,rail,1.86,(bottom-rail)*.52,.32) for x in (4.75,8)))
        details = union(keys,black_keys,line((1.5,rail),(14.5,rail),width=1.1)) if n=='piano' else union(keys,black_keys)
        S(n,body,details)

    api['CATEGORY']='Charts and analytics'
    axes=stroke('M2 2.5V13.5H14',1.2)
    # Bars are solid data marks in every style, rather than faded fragments.
    for orient,word in [('h','bar'),('v','column')]:
        for suffix,sizes in [('big',[8.8,8.8]),('decreasing',[8.8,5.8,2.8]),('increasing',[2.8,5.8,8.8])]:
            marks=[]
            for i,size in enumerate(sizes):
                pos=4.55+i*(5 if suffix=='big' else 3.45)
                if orient=='h':
                    marks.append(line((4.55,pos),(4.55+size,pos)))
                else:
                    marks.append(line((pos,11.05-size),(pos,11.05)))
            G('chart-'+word+'-'+suffix,axes,union(*marks))
    G('chart-bar-stacked',axes,stroke('M4.65 3.6H7.05M9.25 3.6H13.65M4.65 7.25H9.25M11.45 7.25H13.65M4.65 10.9H6M8.2 10.9H13.65'))
    for suffix,sizes in [('',[5,10,7]),('-decreasing',[11,7,3]),('-increasing',[3,7,11])]:
        G('chart-no-axes-column'+suffix,union(*(rr(2.2+i*4.4,14-size,2.5,size,.65) for i,size in enumerate(sizes))))
    G('chart-gantt',axes,stroke('M4.75 4H8M6 7.3H12M9 10.6H14'))
    G('chart-no-axes-gantt',stroke('M2 3.5H8M5 8H13M9 12.5H14'))
    G('chart-no-axes-combined',union(rr(2,9,2.5,5,.5),rr(6.7,6.5,2.5,7.5,.5),rr(11.5,8,2.5,6,.5)),stroke('M2 6L7.5 2L13 4',1.3))
    G('chart-bell-curve',axes,stroke('M4.35 11.05C6.5 11.05 5.8 3.55 8.95 3.55S11.4 11.05 13.55 11.05',1.3))
    G('chart-spline',axes,stroke('M4.45 10C6.6 10 5.25 5.1 7.65 5.1S10.15 10.8 12.1 7.1L14 3.2',1.35))
    G('chart-candlestick',axes,union(stroke('M5.5 3V11M10.8 2V10',1.05),rr(4.12,5,2.76,4,.4),rr(9.42,4,2.76,3.5,.4)))
    G('chart-quadrant',lines('M8 1.5V14.5M1.5 8H14.5'),dots((4,4),(11,3),(11.8,11.7),(4.8,10.6),r=.8))
    G('chart-network',union(line((3,11),(5,3),(12,4),(13,12),(3,11),(12,4),width=1.05)),union(*(ring(x,y,1.35,1) for x,y in [(3,11),(5,3),(12,4),(13,12)])))
    vertices = [(8 + 6.65*math.sin(i*math.tau/5), 8 - 6.65*math.cos(i*math.tau/5)) for i in range(5)]
    frame = stroke(poly(vertices),1.2)
    spokes = union(*(line((8,8),p,width=1.05) for p in vertices))
    plot = poly([(7.45,4.75),(10.95,6.35),(9.85,11.05),(7.45,8.7),(4.6,8.3)])
    rim = stroke(plot,1.2)
    grid = union(frame,cut(spokes,plot))
    ink = union(grid,rim)
    S('chart-radar',plot,grid)
    overrides['chart-radar']={'duotone':[(cut(plot,ink),.24),(ink,1)],'solid':union(cut(grid,plot),plot,rim),'stroke':ink}
    G('trending-up-down',stroke('M1.6 10.8L5.7 6.7L8.25 8.35L14 2.8M10.55 2.8H14V6.25'),
      stroke('M8.25 8.35L14 13.45M10.55 13.45H14V10'))
    S('podium',union(rr(1.5,7.5,4.3,6.5,.6),rr(5.8,3,4.4,11,.6),rr(10.2,9.5,4.3,4.5,.6)),stroke('M8 5V8M2.8 10H4.5M11.5 12H13.2',1.1))
    S('kanban',union(rr(1.7,2.5,3.2,9,.7),rr(6.4,2.5,3.2,6,.7),rr(11.1,2.5,3.2,11,.7)))

    api['CATEGORY']='Actions and status'
    squaremarks={
        'activity':stroke('M3.5 8H5.5L7 4L9 12L10.5 8H12.5',1.2),
        'bookmark':stroke('M5.5 4V12L8 10.2L10.5 12V4Z',1.1),
        'chart-gantt':stroke('M4 5H8M6 8H12M9 11H12',1.4),
        'dot':circle(8,8,1.2),'kanban':lines('M5 5V11M8 5V8M11 5V10'),
        'pause':lines('M6 4.85V11.15','M10 4.85V11.15'),
        'play':play(),'power':power(8,8,.6),'radical':stroke('M4 8L6 10.5L8 5H12',1.25),
        'slash':line((4.7,11.3),(11.3,4.7)),
        'sparkles':union(star(7,7,.34),star(11.5,4.5,.14),star(11.5,11.5,.17)),
        'star':star(8,8,.5),'stop':rr(5,5,6,6,.6),
        'terminal':stroke('M4.5 5L7.5 8L4.5 11M9 11H12',1.15)}
    for n,m in squaremarks.items(): S('square-'+n,rr(),m)
    badge('square-kanban-plus',rr(),squaremarks['kanban'],plus(12,11.8,.8))
    dash=stroke('M2 10V4Q2 2 4 2H12Q14 2 14 4V10M2 13V14H4M7 14H9M12 14H14V13',1.25)
    G('square-dashed-bottom',dash)
    G('square-dashed-bottom-code',dash,stroke('M6 5L3.5 8L6 11M10 5L12.5 8L10 11',1.1))
    G('square-dashed-kanban',stroke('M2 5V3Q2 2 3 2H5M8 2H10M13 2Q14 2 14 3V5M14 8V10M14 13Q14 14 13 14H11M8 14H6M3 14Q2 14 2 13V10M2 8V7',1.2),squaremarks['kanban'])
    for n,m in [('minus',line((5.8,8),(10.2,8))),('plus',plus(8,8,.9))]:S('diamond-'+n,poly([(8,1.5),(14.5,8),(8,14.5),(1.5,8)]),m)
    S('badge-question-mark',api['badge_body'](),union(stroke('M6.3 6.3C6.3 4.4 9.7 4.4 9.7 6.3C9.7 7.5 8 7.7 8 9',1.1),circle(8,11,.6)))
    G('slash',line((4,14),(12,2)))
    for n,angle in [('bottom-vertical',0),('top-vertical',180),('left-horizontal',90),('right-horizontal',270)]:
        G('line-dot-'+n,transform(line((8,2),(8,10)),angle),transform(circle(8,13,1.4),angle))
    for n,flip in [('left',True),('right',False)]:
        p=path('M4 2L13 5.5L4 9Z') if not flip else path('M12 2L3 5.5L12 9Z')
        S('flag-triangle-'+n,p,line((4 if not flip else 12,2),(4 if not flip else 12,14)))
    for n,mark in [('minus',line((5.5,8),(10.5,8))),('plus',plus(8,8,.9))]:
        S('alarm-clock-'+n,circle(8,8.5,5),union(mark,lines('M2 3L4 1.5M12 1.5L14 3M4.5 12.5L3 14.5M11.5 12.5L13 14.5')))

    api['CATEGORY']='Photography and optics'
    image=rr(1.8,2.5,12.4,11,1.4)
    landscape=union(stroke('M2 11L6 7L10 11L12 9L14 11',1.1),circle(10.5,5.5,.8))
    for n,m in [('down',arr('down',12,11.8,.8)),('up',arr('up',12,11.8,.8)),('play',play(12,11.8,.9)),('upscale',stroke('M10 14L14.5 9.5M11 9.5H14.5V13',1.25))]:badge('image-'+n,image,landscape,m)
    S('wallpaper',rr(1.5,2.5,13,11,1.2),union(landscape,stroke('M5 2.5V13.5',1.15)))
    S('picture-in-picture-2',rr(1.5,2,13,12,1.4),union(stroke(rr(8,8,5,4, .5),1.1),stroke('M3.5 4L6.5 7M3.5 7H6.5V4',1.1)))
    # Extend each edge of the hexagonal aperture outward to meet the rim.
    aperture_radius = 2.4
    vertex = (8+aperture_radius,8)
    next_vertex = (8+aperture_radius/2,8-aperture_radius*math.sqrt(3)/2)
    start = (vertex[0]+1.87*(vertex[0]-next_vertex[0]),vertex[1]+1.87*(vertex[1]-next_vertex[1]))
    blade = line(start,next_vertex,width=1.15)
    blades = union(*(transform(blade,i*60) for i in range(6)))
    G('aperture',ring(8,8,6.45,1.25),op(blades,circle(8,8,6),po.PathOp.INTERSECTION))
    G('crosshair',union(ring(8,8,4.5,1.2),circle(8,8,.8)),lines('M8 1V4M8 12V15M1 8H4M12 8H15'))
    G('focus',stroke('M1.5 5V1.5H5M11 1.5H14.5V5M14.5 11V14.5H11M5 14.5H1.5V11',1.3),ring(8,8,2.6,1.2))
    scan=stroke('M1.8 5V2H5M11 2H14.2V5M14.2 11V14H11M5 14H1.8V11',1.2)
    scanmarks={
        'eye':union(stroke('M4 8Q8 3 12 8Q8 13 4 8Z',1),circle(8,8,1.05)),
        'heart':stroke('M8 11L4.5 7.5C2.5 4.7 6.4 3.6 8 6C9.6 3.6 13.5 4.7 11.5 7.5Z',1.1),
        'line':line((3.5,8),(12.5,8)),
        'search':union(ring(7,7,2.5,1.1),line((8.9,8.9),(11.8,11.8),width=1.2)),
        'square':stroke(rr(5,5,6,6,.7),1.1)}
    for n,m in scanmarks.items():G('scan-'+n,scan,m)
    G('eye-closed',stroke('M2 6Q8 12 14 6M3 7L1.7 9M6 8.5L5.5 11M10 8.5L10.5 11M13 7L14.3 9',1.25))
    G('eye-dashed',stroke('M1.5 8L3 6.3M5.5 4.8Q8 3.5 10.5 4.8M13 6.3L14.5 8M13 9.7L11.5 11M9 11.7H7M4.5 11L3 9.7',1.25),ring(8,8,2,1.1))
    G('glasses',union(ring(4.5,9.5,2.8,1.2),ring(11.5,9.5,2.8,1.2)),stroke('M7.2 9Q8 8 8.8 9M1.7 9.5V6L3 3M14.3 9.5V6L13 3',1.15))
    S('rectangle-goggles',path('M1.5 5H14.5V10Q14.5 12 12 12H10L8 9.5L6 12H4Q1.5 12 1.5 10Z'),stroke('M4 7H6M10 7H12',1.1))
    S('lens',circle(),union(stroke(circle(8,8,3.8),1.12),stroke(path('M6.25 7.55Q6.45 5.55 8.35 5.65Q8.4 7.6 6.25 7.55Z'))))
    S('lens-concave',path('M4 2Q7 8 4 14H12Q9 8 12 2Z'),line((1.5,8),(14.5,8),width=1.05))
    S('lens-convex',path('M8 1.5Q1 8 8 14.5Q15 8 8 1.5Z'),line((1.5,8),(14.5,8),width=1.05))
    S('mirror-rectangular',rr(3,1.5,10,10.5,1.3),union(lines('M8 12V14.5M5 14.5H11M5.5 5L8 2.5M6.5 8L10.5 4'),empty))
    S('mirror-round',circle(8,6.3,4.8),union(lines('M8 11.1V14.5M5 14.5H11M5.5 5L8 2.5M6.5 8L10.5 4')))
    S('rectangle-circle',union(rr(1.5,3,8.5,10,1),circle(10.5,9,4)),stroke(circle(10.5,9,4),1.15))
    S('contrast',circle(),path('M8 2V14A6 6 0 0 0 8 2Z'))
    S('eclipse',path('M8 2A6 6 0 1 0 14 8Q8 9 8 2Z'),stroke('M11 1.5V3M13.5 2.5L12.5 4M14.5 5.5H13',1.1))
    for n,r in [('dim',2.3),('medium',3.3)]:
        rays=union(*(line((8+(r+1.4)*math.cos(i*math.pi/4),8+(r+1.4)*math.sin(i*math.pi/4)),(8+6.2*math.cos(i*math.pi/4),8+6.2*math.sin(i*math.pi/4)),width=1.1) for i in range(8)))
        S('sun-'+n,circle(8,8,r),rays)
    S('moon-star',path('M7 2Q1 2 1.8 8.5Q2 14.8 9 14Q12.5 13.7 14 10.5Q7 12 7 2Z'),star(11.8,4.3,.29))
    S('sun-moon',union(circle(4.2,4.2,1.8),path('M9 5Q8 11 14 10Q12.5 15 8 13.5Q4 11 6 7Z')),stroke('M4.2 1V1.5M1 4.2H1.5M1.8 1.8L2.3 2.3M6.1 1.8L6.6 1.3',1.05))
    G('orbit',union(stroke('M2 11C-1 5 10-1 14 5C17 11 6 17 2 11Z',1.1),circle(8,8,2)),circle(3.7,3.7,1.1))
    orbit = path('M1.5 8A6.5 5 0 1 1 14.5 8A6.5 5 0 1 1 1.5 8Z')
    arm = stroke('M1.5 8C1.5 4.3 7.45 4.5 9.15 6.25')
    G('galaxy',transform(union(stroke(orbit),arm,transform(arm,180),ring(8,8,1.45)),-28))

    api['CATEGORY']='Health, science and accessibility'
    body = stroke('M8 5.55V8.75M3 6.35Q8 5.7 13 6.35M4.55 14.2L8 8.75L11.45 14.2',1.4)
    G('person-standing',circle(8,2.65,1.4),body)
    mouth=path('M1.5 8Q5 3 8 5Q11 3 14.5 8Q10 14 8 11Q6 14 1.5 8Z')
    mouthdetail=stroke('M2 8Q8 10 14 8',1.05)
    S('mouth',mouth,mouthdetail);off('mouth-off',mouth,mouthdetail)
    S('pill-bottle',rr(4,4.5,8,10,1.2),union(stroke(rr(3.5,1.5,9,3,.5),1.1),plus(8,9.5,.85)))
    tablet = path('M2.9 4.6A2.45 2.45 0 0 1 7.8 4.6V7.25A2.45 2.45 0 0 1 2.9 7.25Z')
    score = line((2.9,5.925),(7.8,5.925))
    round_pill = circle(11.65,11.55,2.7)
    S('tablets',union(transform(tablet,-28),round_pill),
      union(transform(score,-28),line((9.74,13.46),(13.56,9.64))))
    bag = path('M6 3.9H10Q11.75 3.9 11.75 5.85V9.85Q11.75 11.75 9.7 11.75H6.3Q4.25 11.75 4.25 9.85V5.85Q4.25 3.9 6 3.9Z')
    S('iv-bag',bag,union(stroke('M6.45 3.9V2.85A1.55 1.55 0 0 1 9.55 2.85V3.9M8 11.75V13.05Q8 14.55 9.5 14.55H10.5M4.25 8.5Q6.1 7.6 8 8.5T11.75 8.5')))
    S('tube-lotion',path('M3.8 1.5H12.2L10.8 12H5.2Z'),union(stroke(rr(5,12,6,2.5,.5),1.1),stroke('M4.2 4H11.8',1.1),circle(8,8,.8)))
    fragment = path('M1.6 5.1C.8 3.6 2 2.5 3.45 2.8C3.55 1.25 5.55 1.05 6.15 2.55Q6.6 3.6 5.95 4.55L8.1 6.7L6.4 6.55L6.45 8.2L4.2 5.95Q2.35 6.55 1.6 5.1Z')
    S('bone-fracture',union(fragment,transform(fragment,180)))
    for n,geometry in [
        ('venus',union(ring(8,5.5,3.5,1.3),lines('M8 9V14.5M5.5 12H10.5'))),
        ('mars',union(ring(6.5,9.5,4,1.3),lines('M9.3 6.7L14 2M10.5 2H14V5.5'))),
        ('non-binary',union(ring(8,10.5,3.5,1.3),lines('M8 7V1.5M5.5 2L10.5 5M10.5 2L5.5 5'))),
        ('mars-stroke',union(ring(6.5,9.5,4,1.3),lines('M9.3 6.7L14 2M10.5 2H14V5.5M9.8 3.7L12.3 6.2'))),
        ('transgender',union(ring(8,9.5,3.1,1.2),lines('M8 12.6V15M6.5 14H9.5M10.2 7.3L14 3.5M11 3.5H14V6.5M5.8 7.3L2 3.5M2 6.5V3.5H5M2.5 7L5.5 4'))),
        ('venus-and-mars',union(ring(5.5,6,3,1.2),ring(10,10,3,1.2),lines('M5.5 9V14M3.5 12H7.5M12 8L14.5 5.5M12 5.5H14.5V8'))),
    ]:G(n,geometry)
    # Glassware: bodies are filled surfaces; fluid lines and measuring ticks are details.
    S('beaker',path('M4 2H12V11Q12 14 8 14Q4 14 4 11Z'),stroke('M3 2H13M4 9H12M4 5H6M4 7H6',1.1))
    S('flask-round',path('M6 1.5H10V6Q14 7 14 10.5Q14 14.5 8 14.5Q2 14.5 2 10.5Q2 7 6 6Z'),stroke('M5 1.5H11M2.5 10H13.5',1.1))
    off('flask-conical-off',path('M6 1.5H10V6L14 12Q15 14.5 12 14.5H4Q1 14.5 2 12L6 6Z'),stroke('M5 1.5H11M4.5 10H11.5',1.1))
    tube=path('M6 2H10V11Q10 14.5 8 14.5Q6 14.5 6 11Z')
    S('test-tube-diagonal',transform(tube,40),transform(stroke('M5 2H11M6 8H10',1.1),40))
    S('test-tubes',union(path('M2 2H6V10Q6 13 4 13Q2 13 2 10Z'),path('M10 4H14V12Q14 15 12 15Q10 15 10 12Z')),stroke('M1 2H7M9 4H15M2 8H6M10 10H14',1.1))
    barrel = path('M7.7 1.55L10.55 3.35L7.55 8.1L4.7 6.3Z')
    pivot = circle(10.75,6,1.3)
    S('microscope',union(barrel,pivot),stroke('M5.3 6.65L4.55 7.85M11.85 6.65C15 10.6 11.2 13.6 8.75 13.6M2.35 10.1H8.3M7.1 10.1L9.05 13.6M3.1 13.6H13.45M4.05 13.6L5.95 10.1'))
    S('telescope',transform(rr(3,3,9,4,.6),-25),union(stroke('M8 8V10M8 10L4 14.5M8 10L12 14.5M8 10V14.5',1.2),transform(lines('M2 3V7M12 2V8'),-25)))
    dna=stroke('M4 1.5C4 6.5 12 9.5 12 14.5M12 1.5C12 6.5 4 9.5 4 14.5',1.3)
    dnabars=stroke('M4.2 3H11.8M5.5 6H10.5M5.5 10H10.5M4.2 13H11.8',1.05)
    G('dna',dna,dnabars);off('dna-off',dna,dnabars,False)
    for n,is_germ in [('virus',False),('germ',True)]:
        body=path('M4.55 4.8Q6.75 2 9.65 4Q13 4 12.25 7.85Q13.85 10.8 10.85 12.25Q7.5 14.15 5.55 11.75Q2.45 10.9 3.75 8Q2.45 5.55 4.55 4.8Z') if is_germ else circle(8,8,4)
        spokes = union(*(transform(line((8,3.85),(8,1.55),width=1.15),i*45) for i in range(8)))
        spokes = cut(spokes,body)
        pores = union(ring(6.55,9.35,1.3),circle(9.35,6.5,.7)) if not is_germ else dots((6.55,8.85),(9.45,6.45),r=.76)
        S(n,body,union(spokes,pores))
        off(n+'-off',source=n,width=3.2,min_area=1.35)
    S('radiation',circle(),union(circle(8,8,1),*(transform(path('M6.8 5.9L5.5 3.7Q3 5 3 7.4L6 7.65Q6.2 6.7 6.8 5.9Z'),i*120) for i in range(3))))
    # Each open claw sweeps around its own counter; the common band links all three.
    claw = stroke('M6.75 1.7C3.5 3.25 4.95 7.15 8 7.15S12.5 3.25 9.25 1.7')
    claws = union(*(transform(claw,120*i) for i in range(3)))
    G('biohazard',claws,ring(8,8,3.05))

    api['CATEGORY']='Sports and outdoors'
    S('life-buoy',circle(),union(stroke(circle(8,8,2.6),1.15),stroke('M3.8 3.8L6.2 6.2M9.8 9.8L12.2 12.2M3.8 12.2L6.2 9.8M9.8 6.2L12.2 3.8',1.4)))
    buoy_body,buoy_detail=api['DRAWINGS']['life-buoy'][:2]
    buoy_ink=union(stroke(buoy_body,1.25),buoy_detail)
    buoy_hole=circle(8,8,2.025)
    buoy_solid=cut(union(buoy_body,stroke(buoy_body,1.25)),buoy_detail)
    overrides['life-buoy']={'duotone':[(cut(cut(buoy_body,buoy_ink),buoy_hole),.24),(buoy_ink,1)],
                            'solid':cut(buoy_solid,buoy_hole)}
    ball = path('M1.75 8C3.75 2.45 12.25 2.45 14.25 8C12.25 13.55 3.75 13.55 1.75 8Z')
    seam = stroke('M4.85 4.75Q7 8 4.85 11.25',1.15)
    S('rugby-ball',transform(ball,-36),transform(union(seam,api['mirror'](seam)),-36))
    S('volleyball',circle(),stroke('M8 8L3 4M8 8L7 14M8 8L14 6M6 2Q9 3 10 6.7M13.5 10Q10 9.5 8 11M2 8Q5 7 6.2 6.5',1.1))
    wave_seams = stroke('M1.7 5.8Q5.75 2.9 8.3 7.35Q10.8 12.1 14.3 9.25M1.65 9.3Q5.25 7.35 7.25 11Q8.55 13.6 11 13.75',1.2)
    S('ball-wave',circle(),op(wave_seams,circle(),po.PathOp.INTERSECTION))
    water = stroke('M1.55 10.85Q3.15 9.35 4.75 10.85T7.95 10.85T11.15 10.85T14.35 10.85')
    rails = stroke('M4.75 10.85V3.15Q4.75 1.5 6.5 1.5M10.35 10.3V3.15Q10.35 1.5 12.1 1.5M4.75 4.65H10.35M4.75 7.5H10.35')
    G('waves-ladder',rails,union(water,transform(water,dy=3.15)))
    S('sport-shoe',path('M2 8L4 4L7 7L9 6L10 9L14 10Q15 11 14 13H2Z'),stroke('M2 11H14.5M6 7L5.2 8.5M8 7L7.2 8.5M10 9L9 10',1.05))
    G('hockey-stick',stroke('M11 1.6L6.1 12.1Q5.5 13.5 4 13.5H1.8'),stroke(rr(9.6,11.55,4.3,2.7)))
    overrides['hockey-stick']={'solid':union(api['DRAWINGS']['hockey-stick'][0],rr(9.05,11,5.4,3.8))}
    grip = line((8.3,2),(8.3,6.2))
    strap = stroke('M8.3 2.5C13.6 .9 13.15 7 8.3 5.5',1.15)
    G('hiking-stick',union(grip,strap),stroke('M7.95 6L5.05 14.4M4.55 12.6L6.35 13.1',1.35))
    G('fishing-hook',stroke('M9 3V10Q9 14 5 14Q1 14 1.5 9L4 11',1.4),ring(9,2,1.3,1))
    rod = stroke('M2.65 14.15L6.75 5.5Q9.2 1.45 13.9 1.95')
    G('fishing-rod',rod,union(ring(6.2,10,1.7),stroke('M13.9 1.95V10.8Q13.9 13.25 12.05 13.25Q10.25 13.25 10.25 11.45')))
    S('whistle',path('M1.5 6H10V4H14V9H10Q10 14 5.5 14Q1.5 14 1.5 10Z'),union(ring(5.5,10,1.6,.9),lines('M4 3V1.5M7 3L8 1.5')))


    # Preserve the printed paper as a separate white interior and keep its
    # status positive in Solid; its frame crosses the printer's silhouette.
    for state,mark in [('check',check(8,11.5,.5)),('x',cross(8,11.5,.5))]:
        n='printer-'+state
        b,d=api['DRAWINGS'][n][:2]
        filled=union(b,stroke(b,1.25))
        overrides[n]={'solid':union(cut(filled,rr(4.4,9.3,7.2,4.1,.2)),stroke('M4.2 9H11.8V14H4.2Z',1.1),mark,stroke('M4 5V1.8H12V5',1.1),circle(12,7,.5))}
    for n in ['guitar','guitar-electric']:
        b,d=api['DRAWINGS'][n][:2]
        filled=union(b,stroke(b,1.25));inset=cut(filled,stroke(filled,1.8))
        overrides[n]={'solid':union(cut(filled,op(d,inset,po.PathOp.INTERSECTION)),cut(d,filled))}
    for n in ['battery-medium','battery-plus','battery-exclamation-point']:
        b,d=api['DRAWINGS'][n][:2]
        overrides[n]={'solid':union(stroke(b,1.25),d)}

    added=set(api['DRAWINGS'])-before
    missing=set(NAMES)-added
    extra=added-set(NAMES)
    assert not missing, f'Missing technology recipes: {sorted(missing)}'
    assert not extra, f'Unexpected technology recipes: {sorted(extra)}'
