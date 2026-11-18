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

    def overlapping(n,rear,front,rear_detail,front_detail):
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
        S(n,union(rear,front),union(rear_detail,front_detail))
        overrides[n]={'duotone':[(surface,.24),(ink,1)],'stroke':ink,
                      'solid':union(cut(filled(rear,rear_detail),clear),filled(front,front_detail))}
    api['CATEGORY']='Technology and development'
    screen=rr(1.8,2.3,12.4,8.5)
    stand=lines('M8 10.8V14M5.2 14H10.8')
    marks={
        'activity':stroke('M4.15 6.95H5.75L6.85 4.55L8.45 8.55L9.65 6.15H11.85'),
        'check':check(8,6.5,.65),'cloud':stroke('M5.85 8.25C4.2 8.25 4.15 5.95 5.95 5.95C6.55 3.55 9.65 3.8 10 6.15C12.2 5.95 12.2 8.25 10.3 8.25Z'),
        'dot':circle(8,6.5,1.2),'down':arr('down',8,6.4,.65),
        'pause':lines('M6.5 4.5V8.5','M9.5 4.5V8.5'),
        'play':play(8,6.5,.8),'stop':rr(6.2,4.7,3.6,3.6),
        'up':arr('up',8,6.4,.65),'x':cross(8,6.5,.7)}
    for state,m in marks.items(): S('monitor-'+state,screen,union(stand,m))
    S('tv-minimal',screen,lines('M5 10.8L4.2 13M11 10.8L11.8 13'))
    S('tv-minimal-play',screen,union(play(8,6.5,.8),lines('M5 10.8L4.2 13M11 10.8L11.8 13')))
    for n,top,base in [('monitor-pc',3.2,10.45),('computer',2.35,10.45),('monitor-speaker',3.2,10.45)]:
        display = rr(1.45,top,7.85,base-top)
        side = rr(11.55,2.8,3,10.65)
        stand_mark = stroke('M5.4 10.45V13M3.7 13H7.1')
        if n=='monitor-speaker':
            display = rr(1.45,top,6.85,base-top)
            side = rr(10.6,2.8,4,10.65)
            stand_mark = stroke('M4.9 10.45V13M3.3 13H6.5')
            face = union(circle(12.6,5.6,.65),ring(12.6,10.15,1.45))
        elif n=='computer':
            face = union(circle(13.05,5.45,.65),line((1.45,7.85),(9.3,7.85)))
        else:
            face = union(line((11.55,6.65),(14.55,6.65)),circle(13.05,11.1,.62))
        S(n,union(display,side),union(stand_mark,face))
    S('pc-case',rr(3.8,1.55,8.4,12.9),
      union(stroke('M4.1 6.8H11.9M6.05 4.15H9.95'),ring(8,10.55,1.8)))
    phone_face = rr(9.35,6.4,5.05,7.95)
    home_dot = circle(11.875,12.15,.61)
    overlapping('monitor-smartphone',rr(1.45,2.45,10.25,8.05),phone_face,
                stroke('M5.5 10.5V13.35M3.55 13.35H7.45'),home_dot)
    overlapping('tablet-smartphone',rr(1.75,1.6,9.45,12.5),phone_face,
                circle(5.75,11.85,.65),home_dot)

    laptop=rr(3,2.3,10,8.5)
    foot=stroke('M3 10.8L1.5 13H14.5L13 10.8')
    S('laptop-minimal',laptop,foot)
    S('laptop-minimal-check',laptop,union(foot,check(8,6.6,.7)))
    phone=rr(4.5,1.5,7,13)
    S('smartphone-charging',phone,union(poly([(8.5,4.3),(6.2,8.3),(8.3,8.3),(7.2,11.6),(10,7),(7.9,7)]),line((7,12.7),(9,12.7))))
    S('vibrate',rr(5,2.5,6,11),lines('M2.5 5L1.3 8L2.5 11M13.5 5L14.7 8L13.5 11'))
    off('vibrate-off',rr(5,2.5,6,11),lines('M2.5 5L1.3 8L2.5 11M13.5 5L14.7 8L13.5 11'))
    mouse = path('M3.95 5.55A4.05 4.05 0 0 1 12.05 5.55V10.45A4.05 4.05 0 0 1 3.95 10.45Z')
    button = line((6,4.2),(6,5.55))
    divider = stroke('M4 7.55H12M8 1.6V7.55')
    for n,mark in [('left',button),('right',api['mirror'](button))]:
        S('mouse-'+n,mouse,union(divider,mark))
    off('mouse-off',rr(4,1.5,8,13),line((8,3),(8,6)))
    S('card-sim',path('M5 1.5H11.7V14.5H3V3.5Z'),union(stroke(rr(5,7,5,5)),stroke('M7.5 7.2V11.8M5.2 9.5H9.8')))
    battery=rr(1.5,4,11.5,8)
    for n,m in [('medium',rr(3.4,6.2,4.5,3.6)),('plus',plus(7,8,.65)),('exclamation-point',warn(7,8,.8))]:
        S('battery-'+n,battery,union(m,line((14.7,6.8),(14.7,9.2))))
    drive = rr(1.8,8.1,12.4,6.05)
    face = union(line((1.8,10.9),(14.2,10.9)),circle(11.65,12.55,.55))
    down_arrow = stroke('M8 1.4V6M5.9 3.9L8 6L10.1 3.9')
    for name,arrow in [('download',down_arrow),('upload',down_arrow.transform(1,0,0,-1,0,7.4))]:
        S('hard-drive-'+name,drive,union(arrow,face))
    # The paper occludes the chassis through the full width of its front face.
    printer_body,printer_detail = api['DRAWINGS']['printer'][:2]
    page = rr(4,8.95,8,5.55)
    page_rim = stroke(page)
    tray = stroke('M4 5V1.45H12V5M4 3.25H12')
    chassis = stroke(printer_body)
    indicator = circle(12,7,.65)
    for n,mark in [('check',check(8,11.75,.58)),('x',cross(8,11.75,.62))]:
        name = 'printer-'+n
        S(name,printer_body,union(printer_detail,mark))
        clear = union(page,page_rim)
        ink = union(cut(chassis,clear),tray,indicator,page_rim,mark)
        surface = cut(union(printer_body,page),ink)
        solid = union(cut(union(printer_body,chassis),page),tray,page_rim,mark)
        overrides[name]={'duotone':[(surface,.24),(ink,1)],'stroke':ink,'solid':solid}
    gantry = rr(2,2,12,12)
    head = path('M6.4 2H9.6V4.35L8 6.1L6.4 4.35Z')
    print_part = path('M5 12V9.85H6.6V8.15H9.35V9.85H11V12Z')
    ink = union(stroke(gantry),stroke(head),stroke(print_part),line((2,12),(14,12)))
    G('printer-3d',ink)
    overrides['printer-3d']={'solid':union(ink,head,print_part)}
    S('projector',rr(1.8,5,12.4,7),union(ring(10.4,8.5,2.1),lines('M4 12L3.4 14M12 12L12.6 14M3.5 7.5H5.5M3.5 9.5H5.5')))
    vacuum = path('M2.05 8.2C2.05 4.65 4.7 2.35 8 2.35S13.95 4.65 13.95 8.2C13.95 10.15 13.2 12.25 11.65 13.2Q11.1 13.55 10.45 13.55H5.55Q4.9 13.55 4.35 13.2C2.8 12.25 2.05 10.15 2.05 8.2Z')
    S('robot-vacuum',vacuum,stroke('M2.65 10.6Q8 11.3 13.35 10.6M7.35 5.25H8.65'))
    foot = rr(1.8,11.75,7,2.6)
    pivots = union(circle(4.6,9,1.45),circle(8.8,4.7,1.4))
    links = stroke('M4.6 11.75V10.45M5.65 7.95L7.8 5.7M10.2 4.7L12.05 4M12.05 4L12 2.2L14 1.6M12.05 4L13.25 5.55L14.65 5')
    S('robot-arm',union(foot,pivots),links)
    # Opposed plug backs share one S-bend. The pins face away from the cord.
    plug_ends = union(rr(1.8,3,4.4,3.9), rr(9.8,9.1,4.4,3.9))
    S('cable', plug_ends, stroke('M2.65 3V1.5H5.35V3M10.65 13V14.5H13.35V13M4 6.9V9.7C4 13 8 13 8 9V7C8 3 12 3 12 6.3V9.1'))
    plug=path('M4 5H12V8Q12 11 8 11Q4 11 4 8Z')
    S('plug-2',plug,lines('M6 1.5V5M10 1.5V5M8 11V14.5'))
    bolt = poly([(13.2,9.15),(10.55,12.25),(12.25,12.25),(11.55,14.5),(14.5,11.1),(12.7,11.1)])
    badge('plug-zap',None,None,bolt,source='plug',x=12.8,y=12.3,radius=1.55,min_area=.85)
    plug_half = path('M2.75 5.7H5.7V10.3H2.75Q1.75 8 2.75 5.7Z')
    socket_half = path('M10.55 5.7H13.1Q14.25 8 13.1 10.3H10.55Z')
    terminals = stroke('M5.7 6.8H7.65M5.7 9.2H7.65M1.35 8H2.35M13.7 8H14.65')
    S('unplug',transform(union(plug_half,socket_half),-35),transform(terminals,-35))
    S('usb-c-port',rr(1.7,4.5,12.6,7),stroke(rr(4,6.9,8,2.2)))
    S('hdmi-port',path('M2 4H14V9L11.5 12H4.5L2 9Z'),union(line((5.45,6.6),(10.55,6.6)),dots((5.45,9.2),(8,9.2),(10.55,9.2),r=.64)))
    S('midi-port',circle(8,8,6),dots(*[(8+3.15*math.cos(i*math.pi/4),8-3.15*math.sin(i*math.pi/4)) for i in range(5)],r=.68))
    S('microchip',rr(4.2,4.2,7.6,7.6),union(stroke(rr(6.3,6.3,3.4,3.4)),lines('M5 1.5V4M8 1.5V4M11 1.5V4M5 12V14.5M8 12V14.5M11 12V14.5M1.5 5H4M1.5 8H4M1.5 11H4M12 5H14.5M12 8H14.5M12 11H14.5')))
    pins = stroke('M5 1.45V3.25M11 1.45V3.25M5 12.75V14.55M11 12.75V14.55M1.45 5H3M1.45 11H3M13 5H14.55M13 11H14.55')
    S('cpu-ai',rr(2.95,3.15,10.1,9.7),union(stroke('M4.95 10.3L6.95 5.65L8.95 10.3M5.6 9.05H8.3M10.95 5.85V10.15'),pins))
    fan_center = (6.35,7.25)
    blade = stroke('M6.35 7.25Q4.05 6.4 4.55 4.65')
    blade = transform(blade,dx=1.65,dy=.75)
    fan = union(*(transform(blade,i*120,dx=-1.65,dy=-.75) for i in range(3)),circle(*fan_center,.8),ring(*fan_center,3.7))
    S('gpu',rr(1.55,2.45,12.9,9.6),union(fan,stroke('M11.25 5.8H12.95V8.7H11.25ZM4.6 12.05V14.05M7.6 12.05V14.05M10.6 12.05V14.05')))
    traces = stroke('M3.85 4.05H7.25V6.1M3.85 11.25H6.35V9.45M9.9 7.25H12.15V4.05M9.05 9.9V12H12.15')
    S('circuit-board',rr(1.5,1.5,13,13),union(stroke(rr(6.1,6.1,3.8,3.8)),traces,
      dots((3.85,4.05),(3.85,11.25),(12.15,4.05),(12.15,12),r=.85)))
    freight = rr(1.5,4,13,8)
    corner = rr(1.65,4.15,1.6,1.6)
    corners = union(corner,api['mirror'](corner),transform(corner,180),transform(api['mirror'](corner),180))
    S('container', freight, union(corners,stroke('M5 6.1V9.9M8 6.1V9.9M11 6.1V9.9')))
    server,tiers = api['DRAWINGS']['server-rack'][:2]
    tiers = op(tiers,server,po.PathOp.INTERSECTION)
    badge('server-plus',server,tiers,plus(12,11.8,.8))
    badge('server-crash',server,tiers,warn(12,11.5,.85))
    S('server-nas',rr(1.8,3,12.4,10.5),union(stroke(rr(4,5,2.6,6.5)),stroke(rr(9.4,5,2.6,6.5)),dots((5.3,10),(10.7,10),r=.45)))


    for n,d in [('arrow-down',arr('down',12,11.6,.8)),('arrow-up',arr('up',12,11.6,.8)),('zap',poly([(12,8),(9.5,12),(12,12),(11,15),(14.5,10.5),(12,10.5)]))]: badge('database-'+n,None,None,d,source='database',radius=3.5)
    cloud=path('M4.2 13C.3 13 .5 7 4.3 7C4.5 1.5 12 1.5 12.5 7C16.3 7 16 13 12.5 13Z')
    badge('cloud-cog',None,None,cog(),source='cloud',x=12,y=11.8,radius=3.9,min_area=1.3)
    S('cloud-exclamation-point',cloud,warn(8,9,.85))
    for n,m in [('cog',cog()),('lock',lock()),('pen',stroke('M10 13.8L10.5 11.5L13.2 8.75L14.7 10.25L12 13Z')),('sync',stroke('M9.45 10.65Q11 7.65 14.1 10.05M14.1 8.4V10.35H12.15M14.35 12.65Q12.6 15.3 9.6 13.1M9.6 14.65V12.8H11.55'))]: badge('wifi-'+n,None,None,m,source='wifi',x=12,y=11.8,radius=3.55)
    G('antenna',union(stroke('M3.5 6A5.5 5.5 0 0 1 12.5 6M5.5 7.8A3 3 0 0 1 10.5 7.8'),circle(8,8.6,.75)),lines('M8 11.1V14M5 14H11'))
    signal_arc = stroke('M2.15 7.3Q1.75 4.55 3.65 2.1M4.55 6.35Q4.45 4.7 5.55 3.55')
    G('radio-tower',union(signal_arc,api['mirror'](signal_arc),circle(8,4.2,.85)),
      stroke('M4.9 14.3L8 6.75L11.1 14.3M6.45 10.3H9.55M5.4 12.8H10.6'))
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
    webcam= circle(8,6,4.5)
    off('webcam-off',webcam,union(ring(8,6,1.7),lines('M8 10.5V13.5M4.5 13.5H11.5')))
    lamp = path('M4 1.85H12V4.95Q12 5.25 11.8 5.55L10 7.7V13.95H6V7.7L4.2 5.55Q4 5.25 4 4.95Z')
    S('flashlight',lamp,stroke('M4.35 4.65H11.65M7.95 8.85V9.65M6 11.8H10'))
    off('flashlight-off',source='flashlight',center=(7.550,8.400),min_area=1.55)
    gong = circle(6.25,6,4.45)
    hammer = circle(13.1,8.55,1.25)
    S('bell-electric',union(gong,hammer),union(circle(6.25,6,.7),stroke('M6.25 10.45V13.85H13.1V9.8')))
    siren = path('M3.8 12.65V8.3C3.8 2.9 12.2 2.9 12.2 8.3V12.65Z')
    beacon = union(line((2,12.65),(14,12.65)),stroke('M8 1.45V2.6M1.6 4.35L2.8 5.45M14.4 4.35L13.2 5.45M6.45 7.3V9.25'))
    S('siren',siren,beacon)
    off('siren-off',source='siren',center=(7.725,8.275),min_area=1.7)
    housing = path('M2.15 4.65H7.75L10.55 3.55V10.55L7.75 9.45H2.15Z')
    S('spotlight',transform(housing,-24),union(transform(stroke('M8.25 4.5V9.6'),-24),
      stroke('M7.4 9.55V13.85M4.25 13.85H10.55M12 3.3L13.65 2.5M13.1 5.9L14.6 5.2')))

    # Developer diagrams use genuine node topology and arrow direction.
    book=rr(2.8,1.7,10.4,12.6)
    spine=stroke('M5 1.8V14.2M3 11.7H13')
    bookmarks={
        'down':arr('down',9,6.8,.7),'up':arr('up',9,6.8,.7),
        'up-2':stroke('M7.15 5.5L9 3.75L10.85 5.5M7.15 8.55L9 6.8L10.85 8.55M9 6.8V9.85'),
        'audio':stroke('M7 5V8M9 4V9M11 5V8'),
        'headphones':union(stroke('M7.35 7.4V6.55A1.85 1.85 0 0 1 11.05 6.55V7.4'),rr(6.8,6.85,1.45,2.35),rr(10.15,6.85,1.45,2.35)),
        'image':union(stroke('M5.15 10.45L8.45 6.85L13.1 10.45'),ring(10.55,4.85,1.52)),
        'key':union(ring(8,5.5,1.3),stroke('M9 6.5L11.5 9M10.5 8L11.5 7'))}
    for n,m in bookmarks.items(): S('book-'+n,book,union(spine,m))
    G('book-dashed',stroke('M5.5 2H4Q2.8 2 2.8 3.3V12.4Q2.8 13.7 4 13.7H5.5ZM8.1 2H9.3M11.8 2H13.25V4.65M13.25 7.3V9M13.25 11.6V13.7H11.65M8.95 13.7H8'))
    S('bot-message-square',path('M2 3H14V11H7L3 14V11H2Z'),union(dots((5.5,6.5),(10.5,6.5),r=.75),line((6,9),(10,9)),line((8,1),(8,3))))
    off('bot-off',source='bot',center=(7.1,9.05),min_area=1.55)
    brain=path('M8 3Q4 0 2.5 3Q1 4 2.5 6Q.5 8 2 10Q2.8 12 4.5 11.5Q4 15 8 13Q12 15 11.5 11.5Q14.5 12 14.5 8Q15 6 13.5 5Q14.5 1 11 1.8Q9.5 1 8 3Z')

    badge('brain-cog',None,None,cog(),source='brain',x=12.05,y=11.95,radius=3.8,min_area=1.3)
    S('brain-circuit',brain,stroke('M8 3V13M4.05 4.8V7.9H5.7M11.9 4.9V7.7H10.25V10.5'))
    off('brain-off',source='brain',min_area=1.7)
    off('bug-off',source='bug',min_area=1.8)
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
    G('git-compare-arrows',union(ring(4,3.25,2.05),ring(12,12.75,2.05)),
      stroke('M4 5.2V13M1.8 10.8L4 13L6.2 10.8M12 10.8V3M9.8 5.2L12 3L14.2 5.2'))
    requestbody = api['DRAWINGS']['git-pull-request'][0]
    for n,mark in [('closed',cross(12,3.25,.78)),('create',plus(12,3.25,.82))]:
        S('git-pull-request-'+n,requestbody,union(stroke('M4 4.5V11.5M12 11.5V6.75'),mark))
    for n in ['arrow','create-arrow']:
        nodes = union(circle(3.1,3.4,1.45),circle(3.1,12.5,1.45),circle(12.5,12.5,1.45))
        branch = stroke('M3.1 4.85V11.05M12.5 11.05V7.2Q12.5 3.8 9.1 3.8H7.2M9.35 1.65L7.2 3.8L9.35 5.95')
        mark = plus(7.65,10.35,.7) if n=='create-arrow' else empty
        S('git-pull-request-'+n,nodes,union(branch,mark))
    node_rings = union(*(ring(x,y,1.95) for x,y in [(3.8,3.05),(3.8,12.8),(12.1,12.8)]))
    G('git-pull-request-draft',node_rings,union(line((3.8,4.95),(3.8,10.9)),dots((12.1,3.2),(12.1,6.2),(12.1,9.2),r=.65)))
    off('webhook-off',source='webhook',center=(7.750,7.950),min_area=.8)
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
    G('play-triangle',play(8,8,2.35))
    G('pause-bars',rr(3.5,2,3,12),rr(9.5,2,3,12))
    S('video-camera',rr(1.5,4,8.5,8),poly([(10,6.5),(14.5,4),(14.5,12),(10,9.5)]))
    wave = stroke('M3.55 2.5Q.05 8 3.55 13.5M5.65 4.95Q3.85 8 5.65 11.05')
    G('radio-signal',union(wave,api['mirror'](wave)),circle(8,8,1.05))
    speaker=path('M2 6H5L9.5 2.5V13.5L5 10H2Z')
    S('volume-none',speaker)
    off('volume-slash',speaker,empty)
    wave=stroke('M2 6V10M5 3.5V12.5M8 1.8V14.2M11 4.5V11.5M14 6V10')
    G('audio-lines',wave)
    off('audio-lines-off',source='audio-lines',center=(7.775,8.225),min_area=1.6)
    badge('audio-lines-x',wave,empty,cross(12,11.8,.8),False)
    G('eject',poly([(8,2),(14,10),(2,10)]),line((2.5,13),(13.5,13)))
    G('step-back',play(7,8,1.7).transform(-1,0,0,1,16,0),line((3,3),(3,13)))
    G('step-forward',play(7,8,1.7),line((13,3),(13,13)))
    off('play-off',source='play-triangle',center=(7.000,9.000),min_area=1.55)
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
    S('videotape',rr(1.5,3.3,13,9.4),union(ring(4.5,7.2,1.6),ring(11.5,7.2,1.6),stroke(rr(5.25,9.75,5.5,2.05)),line((6.2,7.2),(9.8,7.2))))
    for n,arc,angle in [('2','M4.1 8A3.9 3.9 0 0 1 8 4.1',180),('3','M5.65 4.9A3.9 3.9 0 0 1 11.85 8.65',180)]:
        groove = stroke(arc)
        S('disc-'+n,circle(),union(ring(8,8,1.65),groove,transform(groove,angle)))
    S('disc-album',rr(1.5,1.5,13,13),union(stroke(circle(8,8,4.3)),ring(8,8,1.7)))
    platter = ring(6.15,8.05,3.55)
    arm = stroke('M12.15 5.25V7.75L8.15 10.3')
    S('turntable',rr(1.5,2.8,13,10.4),union(cut(platter,stroke(arm,1.95)),ring(6.15,8.05,1.43),arm,circle(12.15,5.25,.75)))
    G('circle-fading-play',union(stroke('M8 1.8A6.2 6.2 0 1 1 1.8 8'),dots((2.5,5),(4.6,2.7),r=.62)),play(8.5,8,.95))
    S('circle-power',circle(),power(8,8,.63))
    S('circle-star',circle(),star(8,8,.48))
    G('circle-slash',ring(),line((4.4,11.6),(11.6,4.4)))
    G('circle-slash-2',ring(),line((4.4,4.4),(11.6,11.6)))
    rear_mask = path('M1.55 2.75Q4.95 1.3 8.3 2.65L8.05 6.6Q8 9.45 5 10.45Q2.05 9.7 1.85 6.8Z')
    front_mask = path('M7.05 6.45Q10.8 7.55 14.45 5.4L14.15 9.65Q14.05 12.8 11.2 14.1Q7.8 13.45 7.35 10.35Z')
    overlapping('drama',rear_mask,front_mask,union(dots((3.65,4.55),(6.3,4.4),r=.57),stroke('M3.7 7.2Q4.85 8.6 6 7.05')),
                union(dots((9.3,8.9),(12.35,8.5),r=.6),stroke('M9.5 11.9Q10.65 9.9 12.25 11.45Q11.1 13.25 9.5 11.9Z')))
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
    off('megaphone-off',source='megaphone',center=(8.175,7.825),min_area=2)
    radio=rr(1.5,5,13,9)
    off('radio-off',radio,union(line((3,5),(12,1.5)),ring(5.5,9.5,2),lines('M10 8H12M10 11H12')))
    S('phone-forwarded',path('M2 2H5L6.2 5.5L4.5 7Q6.5 10.5 9.5 11.5L11 9.8L14 11V14Q5 16 1.5 5Z'),arr('right',11,4,.85))
    S('phone-log',path('M2 2H5L6.2 5.5L4.5 7Q6.5 10.5 9.5 11.5L11 9.8L14 11V14Q5 16 1.5 5Z'),lines('M9 2H14M10 4.5H14M11 7H14'))
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
    head = rr(7.05,.8,1.9,2.5)
    neck = rr(7.45,2.7,1.1,5.7)
    acoustic = path('M8 6.8C10.25 6.45 11.35 7.7 10.65 9.3Q10.25 10.15 11.1 10.95C13.4 13.85 10.6 15.1 8 15.1S2.6 13.85 4.9 10.95Q5.75 10.15 5.35 9.3C4.65 7.7 5.75 6.45 8 6.8Z')
    electric = path('M5.1 6.05Q6.1 8.5 7.6 7.6L8.5 7.35Q10.05 8.65 11.2 6.5C11.85 8.55 9.75 9.8 11.15 11.1C13.25 13.6 10.3 15.1 8 15.1C4.8 15.1 3.4 13.6 4.6 11.55Q5.6 10.1 5.1 9.05Q4.45 7.65 5.1 6.05Z')
    for n,wood,detail in [('guitar',acoustic,ring(8,9.45,1.65)),
                          ('guitar-electric',electric,line((7.05,9.85),(8.95,9.85)))]:
        offset_y = -.2 if n=='guitar' else 0
        body = transform(union(wood,neck,head),36,dy=offset_y)
        bridge = line((6.75,12.5),(9.25,12.5))
        S(n,body,transform(union(detail,bridge),36,dy=offset_y))
    for n,top,bottom in [('piano',2.25,13.75),('keyboard-music',4,12)]:
        body = rr(1.5,top,13,bottom-top)
        rail = top+2.35 if n=='piano' else top
        keys = union(*(line((x,rail),(x,bottom)) for x in (4.75,8,11.25)))
        black_keys = union(*(rr(x-.93,rail,1.86,(bottom-rail)*.52) for x in (4.75,8)))
        details = union(keys,black_keys,line((1.5,rail),(14.5,rail))) if n=='piano' else union(keys,black_keys)
        S(n,body,details)

    api['CATEGORY']='Charts and analytics'
    axes=stroke('M2 2.5V13.5H14')
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
        G('chart-no-axes-column'+suffix,union(*(rr(2.2+i*4.4,14-size,2.5,size) for i,size in enumerate(sizes))))
    G('chart-gantt',axes,stroke('M4.75 4H8M6 7.3H12M9 10.6H14'))
    G('chart-no-axes-gantt',stroke('M2 3.5H8M5 8H13M9 12.5H14'))
    G('chart-no-axes-combined',union(rr(2,9,2.5,5),rr(6.7,6.5,2.5,7.5),rr(11.5,8,2.5,6)),stroke('M2 6L7.5 2L13 4'))
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
    squaremarks={
        'activity':stroke('M4.25 8H5.8L7.15 4.65L8.95 11.35L10.3 8H11.75'),
        'bookmark':stroke('M5.5 4V12L8 10.2L10.5 12V4Z'),
        'chart-gantt':stroke('M4.5 5H8M6.3 8H11.5M8.45 11H11.5'),
        'dot':circle(8,8,1.2),'kanban':lines('M5 5V11M8 5V8M11 5V10'),
        'pause':lines('M6 4.85V11.15','M10 4.85V11.15'),
        'play':play(),'power':power(8,8,.6),'radical':stroke('M4.65 8.1L6.3 10.35L8.15 5.6H11.6'),
        'slash':line((4.7,11.3),(11.3,4.7)),
        'sparkles':union(path('M7 4.15Q7.55 7.95 10.1 8.7Q7.55 9.45 7 12Q6.45 9.45 3.9 8.7Q6.45 7.95 7 4.15Z'),path('M10.9 3.8Q11.2 5.05 12.4 5.4Q11.2 5.75 10.9 7Q10.6 5.75 9.4 5.4Q10.6 5.05 10.9 3.8Z')),
        'star':star(8,8,.5),'stop':rr(5,5,6,6),
        'terminal':stroke('M4.5 5L7.5 8L4.5 11M9 11H12')}
    for n,m in squaremarks.items(): S('square-'+n,rr(),m)
    badge('square-kanban-plus',None,None,plus(12,11.8,.8),source='square-kanban',radius=3.6,min_area=1.2)
    dash=stroke('M2 10V4Q2 2 4 2H12Q14 2 14 4V10M2 13V14H4M7 14H9M12 14H14V13')
    G('square-dashed-bottom',dash)
    G('square-dashed-bottom-code',dash,stroke('M6.25 5.55L4.4 8L6.25 10.45M9.75 5.55L11.6 8L9.75 10.45'))
    corner = stroke('M2 4.4V3.25A1.25 1.25 0 0 1 3.25 2H4.4')
    dash = union(*(transform(union(corner,line((7,2),(9,2))),90*i) for i in range(4)))
    G('square-dashed-kanban',dash,squaremarks['kanban'])
    for n,m in [('minus',line((5.8,8),(10.2,8))),('plus',plus(8,8,.9))]:S('diamond-'+n,poly([(8,1.5),(14.5,8),(8,14.5),(1.5,8)]),m)
    S('badge-question-mark',api['badge_body'](),union(stroke('M6.3 6.3C6.3 4.4 9.7 4.4 9.7 6.3C9.7 7.5 8 7.7 8 9'),circle(8,11,.6)))
    G('slash',line((4,14),(12,2)))
    for n,angle in [('bottom-vertical',0),('top-vertical',180),('left-horizontal',90),('right-horizontal',270)]:
        G('line-dot-'+n,transform(line((8,2),(8,10)),angle),transform(circle(8,13,1.4),angle))
    for n,flip in [('left',True),('right',False)]:
        p=path('M4 2L13 5.5L4 9Z') if not flip else path('M12 2L3 5.5L12 9Z')
        S('flag-triangle-'+n,p,line((4 if not flip else 12,2),(4 if not flip else 12,14)))
    for n,mark in [('minus',line((5.5,8),(10.5,8))),('plus',plus(8,8,.9))]:
        S('alarm-clock-'+n,circle(8,8.5,5),union(mark,lines('M2 3L4 1.5M12 1.5L14 3M4.5 12.5L3 14.5M11.5 12.5L13 14.5')))

    api['CATEGORY']='Photography and optics'


    for n,m in [('down',arr('down',12,11.8,.8)),('up',arr('up',12,11.8,.8)),('play',play(12,11.8,.9)),('upscale',stroke('M10 14L14.5 9.5M11 9.5H14.5V13'))]:badge('image-'+n,None,None,m,source='image')
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
    G('crosshair',union(ring(8,8,4.5),circle(8,8,.8)),lines('M8 1V4M8 12V15M1 8H4M12 8H15'))
    G('focus',stroke('M1.5 5V1.5H5M11 1.5H14.5V5M14.5 11V14.5H11M5 14.5H1.5V11'),ring(8,8,2.6))
    scan=stroke('M1.8 5V2H5M11 2H14.2V5M14.2 11V14H11M5 14H1.8V11')
    scanmarks={
        'eye':union(stroke('M4 8Q8 3 12 8Q8 13 4 8Z'),circle(8,8,1.05)),
        'heart':stroke('M8 11L4.5 7.5C2.5 4.7 6.4 3.6 8 6C9.6 3.6 13.5 4.7 11.5 7.5Z'),
        'line':line((3.5,8),(12.5,8)),
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
    for n,r in [('dim',2.3),('medium',3.3)]:
        rays=union(*(line((8+(r+2.2)*math.cos(i*math.pi/4),8+(r+2.2)*math.sin(i*math.pi/4)),(8+(5.65 if n=='dim' else 6.7)*math.cos(i*math.pi/4),8+(5.65 if n=='dim' else 6.7)*math.sin(i*math.pi/4))) for i in range(8)))
        S('sun-'+n,circle(8,8,r),rays)
    moon = cut(circle(7.7,8.25,5.95),circle(10.45,5.55,5.35))
    S('moon-star',moon,star(12,3.9,.31))
    S('sun-moon',union(circle(4.9,5.1,1.6),path('M9 5Q8 11 14 10Q12.5 15 8 13.5Q4 11 6 7Z')),stroke('M4.8 1.3V1.85M1.3 5.05H1.85M2.05 2.35L2.55 2.85'))
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
    off('flask-conical-off',source='flask',min_area=1.45)
    tube=path('M6 2H10V11Q10 14.5 8 14.5Q6 14.5 6 11Z')
    S('test-tube-diagonal',transform(tube,40),transform(stroke('M5 2H11M6 8H10'),40))
    S('test-tubes',union(path('M2 2H6V10Q6 13 4 13Q2 13 2 10Z'),path('M10 4H14V12Q14 15 12 15Q10 15 10 12Z')),stroke('M1 2H7M9 4H15M2 8H6M10 10H14'))
    barrel = path('M7.7 1.55L10.55 3.35L7.55 8.1L4.7 6.3Z')
    pivot = circle(10.75,6,1.3)
    S('microscope',union(barrel,pivot),stroke('M5.3 6.65L4.55 7.85M11.85 6.65C15 10.6 11.2 13.6 8.75 13.6M2.35 10.1H8.3M7.1 10.1L9.05 13.6M3.1 13.6H13.45M4.05 13.6L5.95 10.1'))
    barrel = path('M3.5 5.55L12 3.95V9.35L3.5 7.85Z')
    S('telescope',transform(barrel,-23),union(transform(stroke('M1.95 6.65H3.5M12 3.25V10.05'),-23),
      stroke('M7.9 8.65V10.45M4.65 14.3L7.9 10.45L11.15 14.3')))
    # The two crossings bound a lens; clip all three rungs to its inner edges.
    strand = path('M4.7 1.55C5.5 3.8 10.95 5.2 11.5 7.45C12.3 10.6 6.05 12 4.7 14.45')
    helix = union(stroke(strand),stroke(api['mirror'](strand)))
    middle = path('M8 3.95C10.1 5.1 11.8 6.35 11.55 8.05C11.2 9.8 9.65 10.9 8 11.8C6.35 10.9 4.8 9.8 4.45 8.05C4.2 6.35 5.9 5.1 8 3.95Z')
    rungs = op(stroke('M3.8 5.75H12.2M3.8 8H12.2M3.8 10.25H12.2'),middle,po.PathOp.INTERSECTION)
    G('dna',transform(union(helix,rungs),20))
    off('dna-off',source='dna',min_area=2.6)
    for n,is_germ in [('virus',False),('germ',True)]:
        body=path('M4.55 4.8Q6.75 2 9.65 4Q13 4 12.25 7.85Q13.85 10.8 10.85 12.25Q7.5 14.15 5.55 11.75Q2.45 10.9 3.75 8Q2.45 5.55 4.55 4.8Z') if is_germ else circle(8,8,4)
        spokes = union(*(transform(line((8,3.85),(8,1.55)),i*45) for i in range(8)))
        spokes = cut(spokes,body)
        pores = union(ring(6.55,9.35,1.3),circle(9.35,6.5,.7)) if not is_germ else dots((6.55,8.85),(9.45,6.45),r=.76)
        S(n,body,union(spokes,pores))
        off(n+'-off',source=n,min_area=1.35)
    sector = path('M6.2 6.96L4.46 5.95A4.1 4.1 0 0 1 8 3.9V5.92A2.08 2.08 0 0 0 6.2 6.96Z')
    S('radiation',circle(),union(circle(8,8,.95),*(transform(sector,i*120) for i in range(3))))
    # Each open claw sweeps around its own counter; the common band links all three.
    claw = stroke('M6.75 1.7C3.5 3.25 4.95 7.15 8 7.15S12.5 3.25 9.25 1.7')
    claws = union(*(transform(claw,120*i) for i in range(3)))
    G('biohazard',claws,ring(8,8,3.05))

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

    for n in ['guitar','guitar-electric']:
        b,d=api['DRAWINGS'][n][:2]
        filled=union(b,stroke(b));inset=cut(filled,stroke(filled,1.8))
        overrides[n]={'solid':union(cut(filled,op(d,inset,po.PathOp.INTERSECTION)),cut(d,filled))}
    for n in ['battery-medium','battery-plus','battery-exclamation-point']:
        b,d=api['DRAWINGS'][n][:2]
        overrides[n]={'solid':union(stroke(b),d)}

    added=set(api['DRAWINGS'])-before
    missing=set(NAMES)-added
    extra=added-set(NAMES)
    assert not missing, f'Missing technology recipes: {sorted(missing)}'
    assert not extra, f'Unexpected technology recipes: {sorted(extra)}'
