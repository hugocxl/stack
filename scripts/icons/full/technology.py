"""Original 16-unit technology, science, media and sport artwork.

Every recipe is authored for IconsCXL. Shared constructions express actual
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
        a=lines('M8 11V5', 'M5.5 7.5L8 5L10.5 7.5')
        return transform(a, {'up':0,'right':90,'down':180,'left':270}[direction],s,x-8,y-8)
    def play(x=8,y=8,s=1):
        return poly([(x-1.7*s,y-2.4*s),(x+2.2*s,y),(x-1.7*s,y+2.4*s)])
    def star(x=8,y=8,s=1): return transform(api['STAR'],scale=s,dx=x-8,dy=y-8)
    def cog(x=8,y=8,s=1): return transform(api['DRAWINGS']['settings'][0],scale=s,dx=x-8,dy=y-8)
    def warn(x=8,y=8,s=1): return union(line((x,y-2*s),(x,y+.4*s),width=1.2),circle(x,y+2.3*s,.6))
    def power(x=8,y=8,s=1):
        return transform(union(stroke('M4.5 4.3A4.7 4.7 0 1 0 11.5 4.3',1.2),line((8,2),(8,7))),scale=s,dx=x-8,dy=y-8)
    def off(n,b,d=None,body=True):
        # A clear channel separates the slash from the disabled object.
        gap=line((1.8,1.8),(14.2,14.2),width=3)
        slash=line((1.8,1.8),(14.2,14.2))
        if body: S(n,cut(b,gap),union(cut(d or empty,gap),slash))
        else: G(n,cut(union(b,d),gap),slash)
    def badge(n,b,d,mark,body=True,x=12,y=11.8):
        clearance=circle(x,y,3.3)
        bb,dd=cut(b,clearance),cut(d or empty,clearance)
        (S if body else G)(n,bb,union(dd,mark))
        if body:
            bb,dd=api['DRAWINGS'][n][:2]
            filled=union(bb,stroke(bb,1.25))
            inset=cut(filled,stroke(filled,1.8))
            # A floating mark must not make a connected interior detail lose
            # its counter when Solid's structural-component rule runs.
            overrides[n]={'solid':union(cut(filled,op(cut(dd,mark),inset,po.PathOp.INTERSECTION)),cut(dd,filled),mark)}
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
    tower=rr(10.8,3.5,3.7,10.5,.8)
    S('monitor-pc',union(rr(1.2,3.5,8,6.8,1),tower),union(lines('M5.2 10.3V13M3.5 13H6.8M12 6H13.3'),circle(12.65,11.8,.5)))
    S('computer',union(rr(1.5,2,9.5,8.3,1),rr(12.3,2,2.5,12,.5)),union(lines('M6.2 10.3V13M3.5 13H9M1.5 7.8H11'),circle(13.55,4.3,.45)))
    S('pc-case',rr(4,1.5,8,13,1.2),union(lines('M4 5H12M6 3.3H10M6 7.5H10'),ring(8,11,1.6,.9)))
    S('monitor-smartphone',union(rr(1.3,2.8,10.2,7.7,1.2),rr(10.2,6.8,4.5,7.5,.8)),union(lines('M5.3 10.5V13M3.4 13H7.3'),stroke(rr(10.2,6.8,4.5,7.5,.8),1.1),line((11.8,12.8),(13.1,12.8),width=.9)))
    S('tablet-smartphone',union(rr(1.8,1.5,9.5,12.5,1.2),rr(9,6.5,5.3,8,1)),union(stroke('M9 6.5H13.3Q14.3 6.5 14.3 7.5V13.5Q14.3 14.5 13.3 14.5H10Q9 14.5 9 13.5Z',1.1),dots((6,12),(11.7,12.8),r=.45)))
    S('monitor-speaker',union(rr(1.2,3,9,7.5,1),rr(11.4,2.5,3.4,11,.8)),union(lines('M5.5 10.5V13M3.5 13H7.5'),ring(13.1,10.5,1,.65),circle(13.1,5.2,.5)))
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
    S('card-sim',path('M5 1.5H11.7V14.5H3V3.5Z'),union(stroke(rr(5,7,5,5,.5),1.1),lines('M7.5 7V12M5 9.5H10')))
    battery=rr(1.5,4,11.5,8,1.3)
    for n,m in [('medium',rr(3.4,6.2,4.5,3.6,.4)),('plus',plus(7,8,.65)),('exclamation-point',warn(7,8,.8))]:
        S('battery-'+n,battery,union(m,line((14.7,6.8),(14.7,9.2))))
    for n,direction in [('download','down'),('upload','up')]:
        S('hard-drive-'+n,rr(1.7,5.5,12.6,8,1.5),union(lines('M2 10H14'),dots((11.3,11.8),(13,11.8),r=.4),arr(direction,8,4.6,.85)))
    for n,m in [('check',check(8,10.9,.7)),('x',cross(8,10.9,.7))]:
        S('printer-'+n,rr(1.8,5,12.4,7,1.5),union(stroke('M4 5V1.8H12V5M4.2 9H11.8V14H4.2Z',1.1),m,circle(12,7,.5)))
    S('printer-3d',rr(2,2,12,12,1.2),union(lines('M2 5H14M8 5V7M6.5 7H9.5M8 7V8.5'),stroke('M5 11L8 9L11 11V13H5Z',1.05)))
    S('projector',rr(1.8,5,12.4,7,1.4),union(ring(10.4,8.5,2.1,1.05),lines('M4 12L3.4 14M12 12L12.6 14M3.5 7.5H5.5M3.5 9.5H5.5')))
    S('robot-vacuum',circle(8,9,5.7),union(stroke('M2.6 8H13.4',1.1),rr(6,4.5,4,2,.6),circle(8,10.8,.7)))
    S('robot-arm',union(rr(2,12.5,11.5,2,.5),circle(5,10,1.7),circle(8.3,5.8,1.6)),union(stroke('M5 10L8.3 5.8L11.4 3.2M11.4 3.2L13.4 3.3L14.5 5M11.4 3.2L11.6 1.3L13.4 1',1.6),line((5,11.7),(5,12.5))))
    S('cable',union(rr(1.5,2,4,4.5,.7),rr(10.5,9.5,4,4.5,.7)),stroke('M3.5 6.5V9Q3.5 12 7 12Q10 12 10 8V6Q10 3 13 3V9.5M2.5 2V.8M4.5 2V.8M11.5 14V15.2M13.5 14V15.2',1.2))
    plug=path('M4 5H12V8Q12 11 8 11Q4 11 4 8Z')
    S('plug-2',plug,lines('M6 1.5V5M10 1.5V5M8 11V14.5'))
    S('plug-zap',path('M2 5H9V8Q9 11 5.5 11Q2 11 2 8Z'),union(lines('M3.5 2V5M7.5 2V5M5.5 11V14'),poly([(12,2),(9.5,7.5),(12,7.5),(10.5,13),(14.5,6),(12,6)])))
    S('unplug',union(path('M2.5 7L6 3.5L8 5.5L4.5 9Z'),path('M8 10.5L11.5 7L13.5 9L10 12.5Z')),lines('M2.5 7L1 5.5M6 3.5L4.5 2M10 12.5L12 14.5M8 1V3M13 3L11.5 4.5M15 7H13'))
    S('usb-c-port',rr(1.7,4.5,12.6,7,3.5),stroke(rr(4,6.9,8,2.2,1.1),1.05))
    S('hdmi-port',path('M2 4H14V9L11.5 12H4.5L2 9Z'),union(line((5,7),(11,7),width=1.3),dots((5.5,9.4),(8,9.4),(10.5,9.4),r=.4)))
    S('midi-port',circle(8,8,6),dots((4.5,8),(5.5,5.2),(8,4.3),(10.5,5.2),(11.5,8),r=.65))
    S('microchip',rr(4.2,4.2,7.6,7.6,1),union(stroke(rr(6.3,6.3,3.4,3.4,.4),1),lines('M5 1.5V4M8 1.5V4M11 1.5V4M5 12V14.5M8 12V14.5M11 12V14.5M1.5 5H4M1.5 8H4M1.5 11H4M12 5H14.5M12 8H14.5M12 11H14.5')))
    S('cpu-ai',rr(3.5,3.5,9,9,1.2),union(stroke('M5.5 10L6.8 6L8.2 10M6 8.5H7.6M10 6V10',1),lines('M5 1V3M11 1V3M5 13V15M11 13V15M1 5H3M1 11H3M13 5H15M13 11H15')))
    S('gpu',rr(1.5,4,13,8.5,1),union(ring(6,8.3,2.6,1),lines('M6 6V10.5M3.8 8.3H8.2M10.5 6.5H12.5M10.5 9H12.5M4 12.5V14M6.5 12.5V14M9 12.5V14M1.5 3V13.5')))
    S('circuit-board',rr(1.5,1.5,13,13,1.3),union(stroke(rr(6,6,4,4,.6),1),stroke('M3.5 4H7V6M3.5 11H6V9M10 7H12V4M9 10V12H12',1),dots((3.5,4),(3.5,11),(12,4),(12,12),r=.6)))
    S('container',rr(1.5,3.5,13,9.5,.6),union(lines('M4 5.5V11M6.7 5.5V11M9.3 5.5V11M12 5.5V11M2 2H14M4 13V14.5M12 13V14.5')))
    server=rr(2.2,1.7,11.6,12.6,1.2)
    serverdetail=union(lines('M2.2 5.8H13.8M2.2 10H13.8'),dots((4.5,3.8),(4.5,7.8),(4.5,12),r=.55))
    badge('server-plus',server,serverdetail,plus(12,11.8,.8))
    badge('server-crash',server,serverdetail,warn(12,11.5,.85))
    S('server-nas',rr(1.8,3,12.4,10.5,1),union(stroke(rr(4,5,2.6,6.5,.6),1),stroke(rr(9.4,5,2.6,6.5,.6),1),dots((5.3,10),(10.7,10),r=.45)))
    db=path('M2.5 4C2.5 .7 13.5 .7 13.5 4V12C13.5 15.3 2.5 15.3 2.5 12Z')
    dbdetail=stroke('M2.5 4C2.5 7.3 13.5 7.3 13.5 4M2.5 8C2.5 11.3 13.5 11.3 13.5 8',1.1)
    for n,d in [('arrow-down',arr('down',12,11.6,.8)),('arrow-up',arr('up',12,11.6,.8)),('zap',poly([(12,8),(9.5,12),(12,12),(11,15),(14.5,10.5),(12,10.5)]))]: badge('database-'+n,db,dbdetail,d)
    cloud=path('M4.2 13C.3 13 .5 7 4.3 7C4.5 1.5 12 1.5 12.5 7C16.3 7 16 13 12.5 13Z')
    badge('cloud-cog',cloud,empty,cog(12,11.6,.4))
    S('cloud-exclamation-point',cloud,warn(8,9,.85))
    wifi=stroke('M1.5 4.8Q8-.4 14.5 4.8M4 7.6Q8 4.2 12 7.6M6.5 10.4Q8 9.2 9.5 10.4',1.25)
    wd=circle(8,13,.8)
    for n,m in [('cog',cog(12,11.8,.4)),('lock',lock()),('pen',stroke('M10 13.8L10.5 11.5L13.5 8.5L15 10L12 13Z',1.1)),('sync',stroke('M10 10Q13 8 14.5 10.5V9M14.5 13Q11.5 15 10 12.5V14',1.15))]: badge('wifi-'+n,wifi,wd,m,False)
    G('antenna',union(stroke('M3.5 6A5.5 5.5 0 0 1 12.5 6M5.5 7.8A3 3 0 0 1 10.5 7.8',1.2),circle(8,9,.7)),lines('M8 10V14M5 14H11'))
    G('radio-tower',stroke('M2 7A8 8 0 0 1 3.5 2M14 7A8 8 0 0 0 12.5 2M5 6A4 4 0 0 1 5.8 3M11 6A4 4 0 0 0 10.2 3',1.15),union(circle(8,4.5,.8),lines('M8 5.5L4.8 14.2M8 5.5L11.2 14.2M6.3 10H9.7M5.4 12.5H10.6')))
    S('satellite',union(transform(rr(1,4,4.5,6, .4),-35),transform(rr(10.5,6,4.5,6,.4),-35),transform(rr(5.3,4.3,5.4,7.4,.7),-35)),union(stroke('M4 2.5L10.5 13.5M1.8 6L5.5 3.5M10.5 12.5L14.2 10',1),line((9.5,3.5),(12,1.5)),circle(12,1.5,.6)))
    S('satellite-dish',path('M3 3Q13 2 13 12Q6 14 3 3Z'),union(lines('M8.5 7.5L12.5 3.5M7 11L5 14H12M9 11L11 14'),circle(12.5,3.5,.8)))
    webcam= circle(8,6,4.5)
    off('webcam-off',webcam,union(ring(8,6,1.7,1),lines('M8 10.5V13.5M4.5 13.5H11.5')))
    S('flashlight',path('M4 2H12V5L10 7V14H6V7L4 5Z'),lines('M4 5H12M6 9H10'))
    off('flashlight-off',path('M4 2H12V5L10 7V14H6V7L4 5Z'),lines('M4 5H12M6 9H10'))
    S('bell-electric',union(rr(2.5,2,3,12,.7),path('M6 5Q13 2 14 7Q15 11 7 12Z')),union(circle(6.5,4,.8),line((6.5,4),(9,6.5))))
    siren=path('M4 12V8C4 2.5 12 2.5 12 8V12Z')
    sd=lines('M2 13.5H14M8 1V2M1.5 5L3 6M13 6L14.5 5M8 6V9')
    S('siren',siren,sd);off('siren-off',siren,sd)
    S('spotlight',transform(rr(2.3,3.5,9,5.5,1),-30),lines('M8 9V14M4.5 14H11.5M12 2L14.5 1M13 5H15M12.5 8L14.5 9'))

    # Developer diagrams use genuine node topology and arrow direction.
    book=rr(2.8,1.7,10.4,12.6,1.1)
    spine=stroke('M5 1.8V14.2M3 11.7H13',1.05)
    bookmarks={
        'down':arr('down',9,6.8,.7),'up':arr('up',9,6.8,.7),
        'up-2':union(arr('up',9,7.7,.62),stroke('M7.4 3.5L9 2L10.6 3.5',1)),
        'audio':stroke('M7 5V8M9 4V9M11 5V8',1.1),
        'headphones':stroke('M6.8 8V6.5A2.4 2.4 0 0 1 11.6 6.5V8M6.8 6.5H7.7V8.7H6.8M10.7 6.5H11.6V8.7H10.7',.9),
        'image':union(stroke(rr(6.7,4,4.7,5.1,.4),.9),stroke('M7 8L8.5 6.5L10.8 8.5',.8),circle(10.3,5.3,.4)),
        'key':union(ring(8,5.5,1.3,.9),stroke('M9 6.5L11.5 9M10.5 8L11.5 7',1))}
    for n,m in bookmarks.items(): S('book-'+n,book,union(spine,m))
    G('book-dashed',stroke('M4.5 2H3V5M7 2H9M11.5 2H13V5M13 8V10M13 13.5H10M7.5 13.5H4Q3 13.5 3 12V8',1.25),stroke('M5.5 2V13.5',1.1))
    S('bot-message-square',path('M2 3H14V11H7L3 14V11H2Z'),union(dots((5.5,6.5),(10.5,6.5),r=.75),line((6,9),(10,9),width=1.1),line((8,1),(8,3))))
    off('bot-off',rr(2,4,12,10,2.5),union(dots((5.5,8),(10.5,8),r=.8),lines('M6 11H10M8 1V4')))
    brain=path('M8 3Q4 0 2.5 3Q1 4 2.5 6Q.5 8 2 10Q2.8 12 4.5 11.5Q4 15 8 13Q12 15 11.5 11.5Q14.5 12 14.5 8Q15 6 13.5 5Q14.5 1 11 1.8Q9.5 1 8 3Z')
    brainfold=stroke('M8 3V13M4 4.5Q4 7 6 7M12 7Q10 7 10 10',1.1)
    badge('brain-cog',brain,brainfold,cog(12,11.8,.4))
    S('brain-circuit',brain,union(stroke('M8 3V13M4 4.5V7H6M12 4.5V8H10V11',1),dots((4,4.5),(6,7),(12,4.5),(10,11),r=.6)))
    off('brain-off',brain,brainfold)
    bug=rr(4,4,8,10,4)
    bd=lines('M8 5V13M5 4L3 2M11 4L13 2M4 7H1M12 7H15M4 10H1M12 10H15M5 13L3 15M11 13L13 15')
    off('bug-off',bug,bd)
    badge('bug-play',bug,bd,play(12,11.8,.9))
    S('blocks',union(rr(1.5,8.8,5.5,5.5,.7),rr(8.8,8.8,5.5,5.5,.7),rr(5.2,1.5,5.5,5.5,.7)))
    S('boxes-linked',union(rr(1.5,2,4.5,4.5,.6),rr(10,2,4.5,4.5,.6),rr(5.8,10,4.5,4.5,.6)),lines('M6 4.2H10M3.8 6.5V8H8V10M12.2 6.5V8H8'))
    S('scratch-blocks',path('M2 2H5V3H8V2H14V7H10V8H7V7H2Z'),union(stroke('M2 9H5V10H8V9H13V14H9V15H6V14H2Z',1.2),line((4,5),(11,5),width=1)))
    G('chevrons-left-right-ellipsis',lines('M4 4L1 8L4 12M12 4L15 8L12 12'),dots((6.2,8),(8,8),(9.8,8),r=.45))
    G('parentheses',stroke('M5 2Q.5 8 5 14'),stroke('M11 2Q15.5 8 11 14'))
    G('option',lines('M2 3H5L11 13H14'),line((9,3),(14,3)))
    G('variable',stroke('M3 4Q6 2 7 6L9 11Q10 14 13 12M4 12L12 4',1.35),empty)
    G('radical',line((1.5,8),(4.2,11.5),(7,3),(14.5,3)),empty)
    G('form',union(stroke(rr(1.5,2,13,12,1),1.2),lines('M5 5H12M5 8H10M5 11H11')),dots((3.3,5),(3.3,8),(3.3,11),r=.4))
    for n,detail in [('minus',line((10,12),(14,12))),('plus',plus(12,12,.8))]:
        badge('git-branch-'+n,union(circle(4,3,1.5),circle(4,13,1.5),circle(12,3,1.5)),stroke('M4 4.5V11.5M12 4.5Q12 8 4 8',1.2),detail)
    S('git-commit-vertical',circle(8,8,2.8),lines('M8 1.5V5.2M8 10.8V14.5'))
    S('git-graph',union(circle(3.5,3,1.4),circle(3.5,12.7,1.4),circle(12.5,4.5,1.4),circle(12.5,12.7,1.4)),stroke('M3.5 4.4V11.3M12.5 5.9V11.3M3.5 7Q8 7 8 10Q8 12.7 11.1 12.7',1.2))
    S('git-merge-conflict',union(circle(3.5,3,1.4),circle(3.5,13,1.4),circle(12.5,3,1.4)),union(stroke('M3.5 4.4V11.6M12.5 4.4Q12.5 7 9 7',1.2),cross(11.5,11.7,.9)))
    G('git-compare-arrows',union(stroke('M4 3V12M2 10L4 12L6 10M12 13V4M10 6L12 4L14 6',1.25),ring(4,2,1.2,1)),ring(12,14,1.2,1))
    requestbody=union(circle(4,3,1.4),circle(4,13,1.4),circle(12,13,1.4))
    requestline=stroke('M4 4.4V11.6M12 11.6V6Q12 3 9 3',1.2)
    for n,m in [('arrow',arr('right',10.5,3,.75)),('closed',cross(11.5,3.3,.85)),('create',plus(11.5,3.3,.8)),('create-arrow',union(arr('right',11.5,3,.7),plus(8,7,.6)))]:
        S('git-pull-request-'+n,requestbody,union(cut(requestline,rr(8,0,8,6,0)),m))
    G('git-pull-request-draft',union(ring(4,3,1.4,1.1),ring(4,13,1.4,1.1),ring(12,13,1.4,1.1)),union(line((4,4.4),(4,11.6)),dots((12,4),(12,7),(12,10),r=.65)))
    G('webhook-off',cut(union(ring(4,11,2.2,1.2),ring(12,11,2.2,1.2),ring(8,3.5,2.2,1.2),lines('M5 9L7 5.5M9 5.5L11 9M6.2 11H9.8')),line((1.5,1.5),(14.5,14.5),width=3)),line((1.5,1.5),(14.5,14.5)))
    for n,d in [('merge',stroke('M2 2V5Q2 8 8 8M14 2V5Q14 8 8 8M8 8V14M5.5 11.5L8 14L10.5 11.5')),('split',stroke('M8 14V10Q8 5 3 3M8 10Q8 5 13 3M3 6V3H6M10 3H13V6'))]:G(n,d)
    S('combine',union(rr(1.5,1.5,5,5,.7),rr(9.5,1.5,5,5,.7),rr(5.5,10,5,4.5,.7)),lines('M4 6.5V8H12V6.5M8 8V10'))
    for n,coords,edges in [
        ('graph-hub',[(8,8),(2,3),(14,3),(2,13),(14,13)],[(0,1),(0,2),(0,3),(0,4)]),
        ('graph-ring',[(8,2),(13.7,6),(11.5,13),(4.5,13),(2.3,6)],[(0,1),(1,2),(2,3),(3,4),(4,0)]),
        ('graph-star',[(8,1.8),(14,6.5),(11.5,14),(4.5,14),(2,6.5)],[(0,2),(2,4),(4,1),(1,3),(3,0)])]:
        nodes=union(*(circle(x,y,1.15) for x,y in coords))
        conn=union(*(line(coords[a],coords[b],width=1.05) for a,b in edges))
        S(n,nodes,cut(conn,union(*(circle(x,y,1.45) for x,y in coords))))

    api['CATEGORY']='Media and communication'
    G('play-triangle',play(8,8,2.35))
    G('pause-bars',rr(3.5,2,3,12,1),rr(9.5,2,3,12,1))
    S('video-camera',rr(1.5,4,8.5,8,1.5),poly([(10,6.5),(14.5,4),(14.5,12),(10,9.5)]))
    G('radio-signal',stroke('M2 3Q-1 8 2 13M5 5Q3 8 5 11M14 3Q17 8 14 13M11 5Q13 8 11 11',1.25),circle(8,8,1.2))
    speaker=path('M2 6H5L9.5 2.5V13.5L5 10H2Z')
    S('volume-none',speaker)
    off('volume-slash',speaker,empty)
    wave=stroke('M2 6V10M5 3.5V12.5M8 1.8V14.2M11 4.5V11.5M14 6V10',1.25)
    G('audio-lines',wave)
    off('audio-lines-off',wave,empty,False)
    badge('audio-lines-x',wave,empty,cross(12,11.8,.8),False)
    G('eject',poly([(8,2),(14,10),(2,10)]),line((2.5,13),(13.5,13),width=1.8))
    G('step-back',play(9,8,1.7).transform(-1,0,0,1,16,0),line((3,3),(3,13),width=1.8))
    G('step-forward',play(7,8,1.7),line((13,3),(13,13),width=1.8))
    off('play-off',play(8,8,2),empty,False)
    G('repeat-1',stroke('M3 9V5Q3 3 5 3H13M13 7V11Q13 13 11 13H3M11 1L13 3L11 5M5 11L3 13L5 15',1.2),stroke('M7 6L8.5 5V10M7 10H10',1))
    S('closed-caption',rr(1.5,3,13,10,1.5),stroke('M6.5 5.5C3 4 2.5 11 6.5 10M12.7 5.5C9 4 8.5 11 12.7 10',1.15))
    S('hd',rr(1.5,3,13,10,1.5),stroke('M4 5.5V10.5M7 5.5V10.5M4 8H7M9.5 5.5H10.5Q13 5.5 13 8Q13 10.5 10.5 10.5H9.5Z',1.1))
    S('ad',rr(1.5,3,13,10,1.5),stroke('M3.2 10.5L5 5.5L6.8 10.5M4 8.5H6M9 5.5H10.5Q13 5.5 13 8Q13 10.5 10.5 10.5H9Z',1.1))
    S('clapperboard',rr(1.8,5,12.4,9,1),union(stroke('M1.8 5L1.1 2.8L13.5 1L14.1 4Z',1.2),lines('M5 2.3L7 4.3M10 1.6L12 3.6')))
    S('boom-box',rr(1.5,5,13,8.5,1.3),union(stroke('M4 5V2.5H12V5',1.1),ring(5,9.5,2.2,1),ring(11,9.5,2.2,1),lines('M7 6.5H9M3 3L11 1')))
    S('cassette-tape',rr(1.5,3.3,13,9.4,1.2),union(stroke(rr(3.5,5.2,9,3.8,1.9),1.1),dots((5.4,7.1),(10.6,7.1),r=.65),stroke('M5 10L4 12.7M11 10L12 12.7M5 10H11',1.05)))
    S('videotape',rr(1.5,3.3,13,9.4,1),union(ring(4.5,7.2,1.6,.9),ring(11.5,7.2,1.6,.9),stroke(rr(4.5,10,7,1.2,.3),.8),line((6.2,7.2),(9.8,7.2),width=.9)))
    for n,detail in [('2',union(ring(8,8,1.4,.8),stroke('M3 8A5 5 0 0 1 8 3M13 8A5 5 0 0 1 8 13',1.05))),('3',union(ring(8,8,1.2,.8),stroke('M5 3.8A5.2 5.2 0 0 1 12.2 11M11 12.2A5.2 5.2 0 0 1 3.8 5',1.05)))]:S('disc-'+n,circle(),detail)
    S('disc-album',rr(1.5,1.5,13,13,1),union(stroke(circle(8,8,4.4),1.05),ring(8,8,1.1,.7)))
    S('turntable',rr(1.5,3,13,10,1),union(ring(6.5,8,3.3,1.1),circle(6.5,8,.7),stroke('M11.5 5V8.5L10 10',1.2),circle(11.5,5,.65)))
    G('circle-fading-play',union(stroke('M8 1.8A6.2 6.2 0 1 1 1.8 8',1.25),dots((2.5,5),(4.6,2.7),r=.62)),play(8.5,8,.95))
    S('circle-power',circle(),power(8,8,.63))
    S('circle-star',circle(),star(8,8,.48))
    G('circle-slash',ring(),line((4,12),(12,4)))
    G('circle-slash-2',ring(),line((4,4),(12,12)))
    S('drama',union(path('M1.5 3Q5 1 8.5 3V8Q6 13 2 9Z'),path('M7.5 6Q11 4 14.5 6V11Q12 16 8 12Z')),union(stroke('M3 5H4M6 5H7M3 7Q5 9 7 7M9 8H10M12 8H13M9 11Q11 9 13 11',1)))
    G('list-music',lines('M2 3H10M2 6H8M2 9H7M2 12H6'),union(stroke('M11 11V3L14 2V10',1.2),circle(9.8,11.5,1.25),circle(12.8,10.5,1.25)))
    G('list-video',lines('M2 3H14M2 6H8M2 9H6M2 12H6'),play(11,10.5,1.2))
    mic=rr(5.5,1.5,5,8,2.5)
    md=stroke('M3.5 6.5V8Q3.5 12 8 12Q12.5 12 12.5 8V6.5M8 12V14.5M5.5 14.5H10.5',1.2)
    S('mic-audio-lines',rr(3.5,2,4,8,2),union(stroke('M1.5 7V8.5Q1.5 12 5.5 12Q9 12 9 9M5.5 12V14.5',1.1),stroke('M11 5V10M13.5 3V12',1.1)))
    S('mic-signal',mic,union(md,stroke('M12 2.5Q15 5 13.8 8M2.3 2.5Q0 5 1.3 8',1)))
    S('mic-vocal',transform(rr(2,3,7,5,2.5),-40),union(line((7.6,7.5),(13,13),width=2),stroke('M3 3.5L7 7.5M12 2V4M10.5 3H13.5',1.1)))
    headphones=stroke('M2.5 9V7A5.5 5.5 0 0 1 13.5 7V9',1.35)
    ears=union(rr(2,8,3,5,1.1),rr(11,8,3,5,1.1))
    off('headphone-off',ears,headphones)
    buds=union(path('M3.5 2Q1 2 1.5 5Q1.8 7 4 7V12Q4 14 6 14V5Q6 2 3.5 2Z'),path('M12.5 2Q15 2 14.5 5Q14.2 7 12 7V12Q12 14 10 14V5Q10 2 12.5 2Z'))
    bd=lines('M3.5 4.5V5.5M12.5 4.5V5.5')
    S('earbuds',buds,bd);off('earbuds-off',buds,bd)
    meg=path('M2 6H6L13 2.5V12.5L6 9H2Z')
    off('megaphone-off',meg,stroke('M5 9L6 14H9L8 10',1.2))
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
    G('clef-alto',lines('M3 2V14M5.5 2V14'),stroke('M6.5 8L10 3Q13 1 13 4Q13 7 9 8M6.5 8L10 13Q13 15 13 12Q13 9 9 8',1.2))
    S('drum',path('M2 4Q8 0 14 4V12Q8 16 2 12Z'),union(stroke('M2 4Q8 8 14 4M2 12L5 6L8 14L11 6L14 12',1.1),lines('M1.5 1L7 3M14.5 1L9 3')))
    S('metronome',poly([(6,1.7),(10,1.7),(14,14),(2,14)]),union(lines('M5 11H11M8 10L11 4'),circle(11,4,.7)))
    S('guitar',path('M5 7Q2 6 1.5 9Q.5 12 3.5 14Q7 16 9 13Q11 11 8 9L13 4L11 2Z'),union(ring(5.8,10.4,1.25,.9),stroke('M5.8 10.4L13.5 2.7M11 1.5L14.5 5M3 12L5 14',1.05)))
    S('guitar-electric',poly([(2,8),(6,8),(10.7,3.3),(12.7,5.3),(8,10),(8,14),(4,13),(1.5,10.5)]),union(lines('M5 11L13.5 2.5M11.5 1.5L14.5 4.5M3.8 9.5L6.5 12.2'),circle(5.5,10.8,.6)))
    for n,body in [('piano',rr(1.5,2.5,13,11,1.3)),('keyboard-music',rr(1.5,4,13,8,1))]:
        S(n,body,union(stroke('M4.1 7V13M6.7 7V13M9.3 7V13M11.9 7V13',1),rr(3.5,4.3,1.2,4.2,.3),rr(6.1,4.3,1.2,4.2,.3),rr(10.7,4.3,1.2,4.2,.3)))

    api['CATEGORY']='Charts and analytics'
    axes=stroke('M2 2.5V13.5H14',1.2)
    # Bars are solid data marks in every style, rather than faded fragments.
    chart_names=[]
    for orient,word in [('h','bar'),('v','column')]:
        for suffix,sizes in [('big',[9,9,9]),('decreasing',[9,6,3]),('increasing',[3,6,9])]:
            marks=[]
            for i,size in enumerate(sizes):
                marks.append(rr(4,3+i*3.2,size,1.8,.5) if orient=='h' else rr(4+i*3.2,12-size,1.8,size,.5))
            n='chart-'+word+'-'+suffix
            G(n,axes,union(*marks));chart_names.append(n)
    G('chart-bar-stacked',axes,union(rr(4,3,3,1.8,.4),rr(8.3,3,5,1.8,.4),rr(4,6.4,5,1.8,.4),rr(10.3,6.4,3,1.8,.4),rr(4,9.8,2,1.8,.4),rr(7.3,9.8,6,1.8,.4)))
    for suffix,sizes in [('',[5,10,7]),('-decreasing',[11,7,3]),('-increasing',[3,7,11])]:
        G('chart-no-axes-column'+suffix,union(*(rr(2.2+i*4.4,14-size,2.5,size,.65) for i,size in enumerate(sizes))))
    G('chart-gantt',axes,stroke('M4 4H8M6 7H12M9 10H14',1.7))
    G('chart-no-axes-gantt',stroke('M2 3H8M5 8H13M9 13H14',1.8))
    G('chart-no-axes-combined',union(rr(2,9,2.5,5,.5),rr(6.7,6.5,2.5,7.5,.5),rr(11.5,8,2.5,6,.5)),stroke('M2 6L7.5 2L13 4',1.3))
    G('chart-bell-curve',axes,stroke('M3 12C6 12 5 3 8.5 3C12 3 11 12 14 12',1.3))
    G('chart-spline',axes,stroke('M3 10C6 10 4 5 7 5S10 11 12 7L14 3',1.35))
    G('chart-candlestick',axes,union(stroke('M5.5 3V11M10.8 2V10',1.05),rr(4.5,5,2,4,.4),rr(9.8,4,2,3.5,.4)))
    G('chart-quadrant',lines('M8 1.5V14.5M1.5 8H14.5'),dots((4,4),(11,3),(11.8,11.7),(4.8,10.6),r=.8))
    G('chart-network',union(line((3,11),(5,3),(12,4),(13,12),(3,11),(12,4),width=1.05)),union(*(ring(x,y,1.35,1) for x,y in [(3,11),(5,3),(12,4),(13,12)])))
    radar_frame=stroke('M8 1.5L14 6L11.8 13.5H4.2L2 6Z',1)
    radar_spokes=union(*(line((8,8),p,width=.8) for p in [(8,1.5),(14,6),(11.8,13.5),(4.2,13.5),(2,6)]))
    radar_plot=path('M8 3.8L11.7 6.8L9 9.5L4.8 12L5.3 7.1Z')
    # A narrow knockout around the data boundary separates it from the grid
    # without using opacity to encode data.
    G('chart-radar',union(radar_frame,cut(radar_spokes,stroke(radar_plot,2.65))),stroke(radar_plot,1.35))
    G('trending-up-down',stroke('M1.5 11L6 6.5L9.5 9.5L14.5 3M11 3H14.5V6.5',1.3),stroke('M1.5 4L5.5 8M10 10L14.5 14M11 14H14.5V10.5',1.3))
    S('podium',union(rr(1.5,7.5,4.3,6.5,.6),rr(5.8,3,4.4,11,.6),rr(10.2,9.5,4.3,4.5,.6)),stroke('M8 5V8M2.8 10H4.5M11.5 12H13.2',1.1))
    S('kanban',union(rr(1.7,2.5,3.2,9,.7),rr(6.4,2.5,3.2,6,.7),rr(11.1,2.5,3.2,11,.7)))

    api['CATEGORY']='Actions and status'
    squaremarks={
        'activity':stroke('M3.5 8H5.5L7 4L9 12L10.5 8H12.5',1.2),
        'bookmark':stroke('M5.5 4V12L8 10.2L10.5 12V4Z',1.1),
        'chart-gantt':stroke('M4 5H8M6 8H12M9 11H12',1.4),
        'dot':circle(8,8,1.2),'kanban':lines('M5 5V11M8 5V8M11 5V10'),
        'pause':union(rr(5,4.7,1.8,6.6,.4),rr(9.2,4.7,1.8,6.6,.4)),
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
    S('badge-question-mark',poly([(8,1.2),(10,2.8),(12.5,2.7),(13.3,5.3),(15,7.2),(13.4,9.5),(13.2,12),(10.5,12.8),(8,14.8),(5.5,12.8),(2.8,12),(2.6,9.5),(1,7.2),(2.7,5.3),(3.5,2.7),(6,2.8)]),union(stroke('M6 5.3Q6 3.5 8 3.5Q10.8 3.5 10 6Q9.7 7 8 8V9',1.15),circle(8,11.3,.65)))
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
    G('aperture',ring(8,8,6,1.2),union(*(transform(stroke('M6.3 2.5L9.8 8',1.15),i*60) for i in range(6))))
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
    S('lens',circle(),union(ring(8,8,3.8,1),ring(8,8,1.4,.8)))
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
    G('galaxy',stroke('M8 8C12 3 15 8 12 11C8 16 1 12 2 7C3-1 14 0 14 6C14 11 8 14 5 10C2 6 8 2 10 5',1.2),circle(8,8,.8))

    api['CATEGORY']='Health, science and accessibility'
    G('person-standing',union(circle(8,2.5,1.4),lines('M8 5V9M3 6H13M8 9L4.5 14M8 9L11.5 14')),empty)
    mouth=path('M1.5 8Q5 3 8 5Q11 3 14.5 8Q10 14 8 11Q6 14 1.5 8Z')
    mouthdetail=stroke('M2 8Q8 10 14 8',1.05)
    S('mouth',mouth,mouthdetail);off('mouth-off',mouth,mouthdetail)
    S('pill-bottle',rr(4,4.5,8,10,1.2),union(stroke(rr(3.5,1.5,9,3,.5),1.1),plus(8,9.5,.85)))
    S('tablets',union(transform(rr(1.5,2.5,6,10,3),-25),circle(11.5,11.5,3.1)),union(stroke('M2.2 7L6.5 5M9.3 13.7L13.7 9.3',1.1)))
    S('iv-bag',rr(3.5,3,9,9,1.5),union(stroke('M6 3V1.5H10V3M8 12V14.5H12V13',1.1),plus(8,7.5,.75)))
    S('tube-lotion',path('M3.8 1.5H12.2L10.8 12H5.2Z'),union(stroke(rr(5,12,6,2.5,.5),1.1),stroke('M4.2 4H11.8',1.1),circle(8,8,.8)))
    G('bone-fracture',stroke('M6 5L4 3Q4 1 2.5 1.5Q.5 2 .8 4Q.5 6 3 6L5.5 8.5M10.5 7.5L13 10Q15.5 10 15 12Q15.5 14 13.5 14.5Q11.5 15 11.5 13L9 10.5',1.6),stroke('M7 4.5L9 7L6.5 9L8.5 11.5',1.1))
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
    S('microscope',union(transform(rr(4,1.5,5,7, .6),-30),rr(2,13,12,1.5,.5)),union(stroke('M10 6Q15 7 12.5 11.5Q11 14 7 13M8 11V13M3 10H9M4 8L3 10',1.3),circle(10,6,1)))
    S('telescope',transform(rr(3,3,9,4,.6),-25),union(stroke('M8 8V10M8 10L4 14.5M8 10L12 14.5M8 10V14.5',1.2),transform(lines('M2 3V7M12 2V8'),-25)))
    dna=stroke('M4 1.5C4 6.5 12 9.5 12 14.5M12 1.5C12 6.5 4 9.5 4 14.5',1.3)
    dnabars=stroke('M4.2 3H11.8M5.5 6H10.5M5.5 10H10.5M4.2 13H11.8',1.05)
    G('dna',dna,dnabars);off('dna-off',dna,dnabars,False)
    for n,is_germ in [('virus',False),('germ',True)]:
        body=path('M4 4Q7 1 10 4Q14 4 13 8Q15 11 11 13Q7 16 5 12Q1 11 3 8Q1 5 4 4Z') if is_germ else circle(8,8,4)
        spikes=stroke('M8 1V4M8 12V15M1 8H4M12 8H15M3 3L5 5M11 11L13 13M3 13L5 11M11 5L13 3',1.1)
        dd=union(spikes,dots((6.5,6.5),(10,8),(7,10.5),r=.65))
        S(n,body,dd);off(n+'-off',body,dd)
    S('radiation',circle(),union(circle(8,8,1),*(transform(path('M6.8 5.9L5.5 3.7Q3 5 3 7.4L6 7.65Q6.2 6.7 6.8 5.9Z'),i*120) for i in range(3))))
    G('biohazard',cut(union(*(transform(stroke('M5.3 2.5A3.4 3.4 0 1 0 10.7 2.5',1.15),i*120) for i in range(3)),ring(8,8,2.2,1)),circle(8,8,1.2)))

    api['CATEGORY']='Sports and outdoors'
    S('life-buoy',circle(),union(stroke(circle(8,8,2.6),1.15),stroke('M3.8 3.8L6.2 6.2M9.8 9.8L12.2 12.2M3.8 12.2L6.2 9.8M9.8 6.2L12.2 3.8',1.4)))
    S('rugby-ball',transform(rr(1.5,4.5,13,7,3.5),-35),transform(stroke('M6 6.5V9.5M8 6.5V9.5M10 6.5V9.5M5 8H11M3 5.5V10.5M13 5.5V10.5',1.05),-35))
    S('volleyball',circle(),stroke('M8 8L3 4M8 8L7 14M8 8L14 6M6 2Q9 3 10 6.7M13.5 10Q10 9.5 8 11M2 8Q5 7 6.2 6.5',1.1))
    S('ball-wave',circle(),stroke('M2.5 5Q6.5 3 8 7Q10 12 13.5 10M2 9Q5 7 7 11Q8 14 10 13.7',1.15))
    G('waves-ladder',stroke('M5 11V3Q5 1 7 1M10 11V3Q10 1 12 1M5 5H10M5 8H10',1.3),stroke('M1.5 12Q3 10.5 5 12T8.5 12T12 12T15 12M1.5 15Q3 13.5 5 15T8.5 15T12 15T15 15',1.1))
    S('sport-shoe',path('M2 8L4 4L7 7L9 6L10 9L14 10Q15 11 14 13H2Z'),stroke('M2 11H14.5M6 7L5.2 8.5M8 7L7.2 8.5M10 9L9 10',1.05))
    G('hockey-stick',stroke('M11 1.5L6 12Q5.5 13.5 4 13.5H1.5',2),stroke(rr(10.5,12,4,2.2,.7),1.1))
    G('hiking-stick',stroke('M6 3H10M8 3L5 14M9 1L11 2',1.7),stroke('M3.5 12.5L6.5 13.5',1.1))
    G('fishing-hook',stroke('M9 3V10Q9 14 5 14Q1 14 1.5 9L4 11',1.4),ring(9,2,1.3,1))
    G('fishing-rod',stroke('M3 14L7 5Q9 1 14 2M14 2V10Q14 13 11.5 13Q9 13 9.5 10L11 11',1.25),union(line((3,14),(5,10),width=2.2),ring(5.5,9.5,1.3,.9)))
    S('whistle',path('M1.5 6H10V4H14V9H10Q10 14 5.5 14Q1.5 14 1.5 10Z'),union(ring(5.5,10,1.6,.9),lines('M4 3V1.5M7 3L8 1.5')))


    # Preserve the printed paper as a separate white interior and keep its
    # status positive in Solid; its frame crosses the printer's silhouette.
    for state,mark in [('check',check(8,10.9,.6)),('x',cross(8,10.9,.6))]:
        n='printer-'+state
        b,d=api['DRAWINGS'][n][:2]
        filled=union(b,stroke(b,1.25))
        overrides[n]={'solid':union(cut(filled,rr(4.4,9.3,7.2,4.1,.2)),stroke('M4.2 9H11.8V14H4.2Z',1.1),mark,stroke('M4 5V1.8H12V5',1.1),circle(12,7,.5))}
    for n in ['guitar','satellite']:
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
