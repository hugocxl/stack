"""Original rounded design, text, geometry and navigation coverage.

All recipes use the CXL 16-unit construction grid. Reference names are metadata;
no reference artwork or font outlines are used. Letterforms are purpose-drawn
monoline capitals with open counters, reused only for actual letter semantics.
"""
import json
import math
from pathlib import Path

UPSTREAM_TO_LOCAL = {'pi': 'math-pi'}
NAMES = tuple(UPSTREAM_TO_LOCAL.get(r['lucide_name'], r['lucide_name'])
              for r in json.loads(Path(__file__).with_name('design-scope.json').read_text()))


def register(api):
    shape, glyph = api['shape'], api['glyph']
    path, rr, circle = api['path'], api['rr'], api['circle']
    line, stroke, union = api['line'], api['stroke'], api['union']
    poly, dots = api['poly'], api['dots']
    plus, cross, check = api['plus'], api['cross'], api['check']
    transform, mirror, ring = api['transform'], api['mirror'], api['ring']
    op, po = api['op'], api['po']
    empty = path('')
    made = set()

    def cat(category):
        api['CATEGORY'] = category

    def g(name, *pieces, tags=''):
        glyph(name, union(*pieces), empty, tags)
        made.add(name)

    def s(name, body, detail=None, tags=''):
        shape(name, body, detail, tags)
        made.add(name)

    st = stroke

    def sub(a, b):
        return op(a, b, po.PathOp.DIFFERENCE)

    def inter(a, b):
        return op(a, b, po.PathOp.INTERSECTION)

    rect = rr

    outline = stroke

    def badged(name, body, detail, badge, clearance):
        s(name, body, union(detail, badge))
        body=api['soften'](body)
        boundary=outline(body)
        primary=union(sub(union(boundary,detail),clearance),badge)
        secondary=sub(sub(body,clearance),primary)
        filled=union(body,boundary)
        interior=sub(filled,outline(filled,1.8))
        structural=[]
        counters=[]
        for piece in api['components'](detail):
            (structural if sub(piece,filled).area > piece.area*.12 else counters).append(piece)
        solid=union(sub(union(sub(filled,inter(union(*counters),interior)),*structural),clearance),badge)
        layers=[(secondary,.24),(primary,1)]
        api.setdefault('STYLE_OVERRIDES',{})[name]={
            'duotone':layers,'solid':solid,'stroke':primary}

    def transpose(p):
        return p.transform(0,1,1,0,0,0)

    def fit(p, x=8, y=8, scale=1):
        return transform(p, scale=scale, dx=x-8, dy=y-8)

    def arr(direction='right', x=8, y=8, scale=1):
        skeleton = path('M3.2 8H12.8M9.4 4.6L12.8 8L9.4 11.4')
        return st(transform(skeleton, directions[direction], scale, x-8, y-8))

    def chev(direction='right', x=8, y=8, scale=1, double=False):
        angle={'right':0,'down':90,'left':180,'up':270}[direction]
        skeleton = path('M3.6 4.4L7.2 8L3.6 11.6M8.8 4.4L12.4 8L8.8 11.6' if double
                        else 'M6 4L10 8L6 12')
        return st(transform(skeleton, angle, scale, x-8, y-8))

    def base_ink(name):
        body, details, outlined = api['DRAWINGS'][name][:3]
        return union(outline(body) if outlined else body, details)

    def slash(p, name):
        diagonal=line((2,2),(14,14))
        # Clear a hairline either side of the cancellation stroke, preserving
        # the contour behind it without a dense black intersection.
        remaining = sub(p, line((2,2),(14,14),width=3.2))
        g(name, *(part for part in api['components'](remaining) if part.area >= .6), diagonal)

    def cancelled(name, base, start, end):
        g(name, sub(base, line(start, end, width=3.2)), line(start, end))

    def dash_circle(x=8,y=8,r=6):
        ps=[]
        for i in range(10):
            a=2*math.pi*i/10; b=a+.34
            mid=(a+b)/2
            ps.append(st(f'M{x+r*math.cos(a)} {y+r*math.sin(a)}Q{x+r*math.cos(mid)*1.015} {y+r*math.sin(mid)*1.015} {x+r*math.cos(b)} {y+r*math.sin(b)}'))
        return union(*ps)

    def dash_square(x=2,y=2,w=12,h=12):
        # One rounded corner and one centered dash per side.
        edge = w/2
        drop = h/2
        radius = 1.25
        corner = st(f'M{x} {y+2.15}V{y+radius}a{radius} {radius} 0 0 1 {radius} {-radius}H{x+2.15}')
        return union(corner,corner.transform(-1,0,0,1,2*x+w,0),
                     corner.transform(1,0,0,-1,0,2*y+h),corner.transform(-1,0,0,-1,2*x+w,2*y+h),
                     line((x+edge-1,y),(x+edge+1,y)),line((x+edge-1,y+h),(x+edge+1,y+h)),
                     line((x,y+drop-1),(x,y+drop+1)),line((x+w,y+drop-1),(x+w,y+drop+1)))

    # Purpose-drawn alphabet. All letters share cap height, stroke and counters.
    letters = {
        'a':'M3 13L7.3 3Q8 1.4 8.7 3L13 13M5 9H11',
        'b':'M4 13V3H8.5C13 3 13 8 8.5 8H4M4 8H8.5C13.5 8 13.5 13 8.5 13H4',
        'c':'M12.5 4.5C10 1 3 2 3 8C3 14 10 15 12.5 11.5',
        'd':'M4 3H7.5C14 3 14 13 7.5 13H4Z',
        'e':'M12 3H4V13H12M4 8H10',
        'f':'M12 3H4V13M4 8H10',
        'g':'M12.5 4.5C10 1 3 2 3 8C3 14 10 15 12.5 11.5V8H8.5',
        'h':'M3.5 3V13M12.5 3V13M3.5 8H12.5',
        'i':'M5 3H11M8 3V13M5 13H11',
        'j':'M5 3H12V10Q12 14 8 14Q4 14 4 10',
        'k':'M4 3V13M12 3L4 8.6L12.5 13',
        'l':'M4 3V13H12',
        'm':'M2.5 13V3L8 9L13.5 3V13',
        'n':'M3.5 13V3L12.5 13V3',
        'o':'M8 2.5C1.5 2.5 1.5 13.5 8 13.5C14.5 13.5 14.5 2.5 8 2.5Z',
        'p':'M4 13V3H8.5C13.8 3 13.8 9 8.5 9H4',
        'q':'M8 2.5C1.5 2.5 1.5 13.5 8 13.5C14.5 13.5 14.5 2.5 8 2.5ZM9.5 10.5L13.5 14',
        'r':'M4 13V3H8.5C13.8 3 13.8 8.5 8.5 8.5H4M8.5 8.5L13 13',
        's':'M12 4Q10.5 2.5 8 2.5C1.5 2.5 1.5 7.5 8 8C14.5 8.5 14.5 13.5 8 13.5Q5 13.5 3.5 12',
        't':'M2.5 3H13.5M8 3V13',
        'u':'M3.5 3V9.5C3.5 15 12.5 15 12.5 9.5V3',
        'v':'M2.8 3L7.2 12.8Q8 14.5 8.8 12.8L13.2 3',
        'w':'M2 3L4.5 13L8 6L11.5 13L14 3',
        'x':'M3.5 3L12.5 13M12.5 3L3.5 13',
        'y':'M3 3L8 8.5L13 3M8 8.5V13',
        'z':'M3.5 3H12.5L3.5 13H12.5',
    }
    digits={
        '0':'M8 2.5C2.5 2.5 2.5 13.5 8 13.5C13.5 13.5 13.5 2.5 8 2.5Z',
        '1':'M5 5L8 2.5V13.5M5 13.5H11',
        '2':'M3.5 5Q3.5 2.5 8 2.5Q12.5 2.5 12.5 5Q12.5 7 8 9L3.5 13.5H12.5',
        '3':'M4 3H9Q14 3 11 7L8 8Q14 8 12 12Q10 15 4 13',
        '5':'M12 3H4V7.5Q12.5 5.5 12.5 10.5Q12.5 15 4 13',
        '6':'M11 3Q4 1 4 10Q4 14 8 14Q12 14 12 10Q12 6 4 8',
    }

    def letter(ch, x=8, y=8, scale=1):
        return placed_stroke(letters[ch], x, y, scale)

    def placed_stroke(d, x=8, y=8, scale=1):
        return st(fit(path(d), x, y, scale))

    def number(ch,x=8,y=8,scale=1):
        return placed_stroke(digits[ch], x, y, scale)

    def label(text,x=8,y=8,scale=.45):
        spacing=12*scale
        return union(*(letter(c,x+(i-(len(text)-1)/2)*spacing,y,scale)
                       for i,c in enumerate(text)))

    cat('Typography and text')
    for ch in letters:
        if 'letter-'+ch in NAMES: g('letter-'+ch,letter(ch),tags='alphabet character '+ch)
        for container in ('circle','square'):
            name=f'{container}-letter-{ch}'
            if name in NAMES:
                body, scale = (circle(), .55) if container == 'circle' else (rr(), .62)
                s(name, body, placed_stroke(letters[ch], scale=scale * (.91 if ch == 'q' else 1)), tags='alphabet character '+ch)
    for container, base in [('circle', 'circle-letter-p'), ('square', 'parking')]:
        body, mark = api['DRAWINGS'][base][:2]
        cancelled(container+'-letter-p-off', union(outline(body), mark), (1.75, 6.1), (10.35, 14.6))
    g('letters',letter('a',4.4,8,.52),letter('b',11.8,8,.52))
    g('numbers',number('1',4.3,8,.54),number('2',11.3,8,.54))
    g('binary',number('1',4.5,4.7,.38),number('0',11,4.7,.38),number('0',4.5,11.7,.38),number('1',11,11.7,.38))

    cat('Navigation')
    directions={'right':0,'down':90,'left':180,'up':270,'up-right':-45,'down-right':45,'down-left':135,'up-left':225}
    for direction,angle in directions.items():
        if 'move-'+direction in NAMES:
            # Distinct move control: arrowhead at each end of an axis.
            p=union(line((2,8),(14,8)),line((5,5),(2,8),(5,11)),line((11,5),(14,8),(11,11)))
            # A single directional move retains the destination direction,
            # including diagonals. The tail stop denotes its starting position.
            p=union(arr(direction),transform(line((2.5,5),(2.5,11)),angle))
            g('move-'+direction,p)
        name='square-arrow-'+direction
        if name in NAMES: s(name, rr(), arr(direction, scale=.72))
        for behavior in ('enter','exit'):
            name=f'square-arrow-{direction}-{behavior}'
            if name not in NAMES: continue
            # Open aperture at the relevant edge, with the arrow visibly
            # crossing it. Enter points into the frame; exit crosses outward.
            if '-' in direction:
                frame = st('M8 2H3.25A1.25 1.25 0 0 0 2 3.25V12.75A1.25 1.25 0 0 0 3.25 14H12.75A1.25 1.25 0 0 0 14 12.75V8')
                rotation = angle + 45
                center = (11.55, 4.45)
                heading = 'up-right'
                size = .84
            else:
                frame = st('M14 4.7V3.25A1.25 1.25 0 0 0 12.75 2H3.25A1.25 1.25 0 0 0 2 3.25V12.75A1.25 1.25 0 0 0 3.25 14H12.75A1.25 1.25 0 0 0 14 12.75V11.3')
                rotation = angle
                center = (11.2, 8)
                heading = 'right'
                size = .74
            if behavior == 'enter':
                frame = transform(frame,180)
                center = (16-center[0],16-center[1])
            arrow = arr(heading,*center,size)
            g(name, transform(frame, rotation), transform(arrow, rotation))
        name=f'circle-arrow-{direction}-exit'
        if name in NAMES:
            frame = st('M11.65 3.55A5.75 5.75 0 1 0 11.65 12.45')
            g(name, transform(frame, angle), transform(arr('right', 10.5, 8, .75), angle))
    for direction,angle in list(directions.items())[:4]:
        big=poly([(2.5,5.6),(8.2,5.6),(8.2,2.8),(14,8),(8.2,13.2),(8.2,10.4),(2.5,10.4)])
        s('arrow-big-'+direction,transform(big,angle))
        s('arrow-big-'+direction+'-dash',transform(transform(big,scale=.83,dx=1),angle),transform(line((1.2,6),(1.2,10)),angle))
        for container in ('circle','square'):
            for double in (False,True):
                name=container+'-'+('chevrons-' if double else 'chevron-')+direction
                if name in NAMES: s(name,circle() if container=='circle' else rr(),chev(direction,scale=.65,double=double))
    for name,reflect in [('chevron-first',False),('chevron-last',True)]:
        p=union(chev('left',9,8,.9),line((2.5,3),(2.5,13)))
        g(name,mirror(p) if reflect else p)
    g('chevrons-down-up',chev('up',8,11.4,.6),chev('down',8,4.6,.6))
    g('chevrons-left-right',chev('left',4,8,.7),chev('right',12,8,.7))

    # Sorting arrows encode actual ordered numerals, letters or bar widths.
    for direction in ('down','up'):
        for order in ('0-1','1-0','a-z','z-a','narrow-wide','wide-narrow'):
            name=f'arrow-{direction}-{order}'
            arrowpart=arr(direction,4,8,.78)
            if order in ('0-1','1-0'):
                a,b=order.split('-')
                detail=union(number(a,11.5,4.4,.49),number(b,11.5,11.6,.49))
            elif order in ('a-z','z-a'):
                a,b=order.split('-')
                detail=union(letter(a,11.5,4.4,.49),letter(b,11.5,11.6,.49))
            else:
                widths=[2.5,4.5,6.5] if order=='narrow-wide' else [6.5,4.5,2.5]
                detail=union(*(line((8,3.5+i*4.5),(8+w,3.5+i*4.5)) for i,w in enumerate(widths)))
            g(name,arrowpart,detail)
    for direction in ('left','right','up','down'):
        angle=directions[direction]
        for mode in ('from-line','to-line'):
            name=f'arrow-{direction}-{mode}'
            if name in NAMES:
                base=union(line((2,3),(2,13)),arr('right',9.4,8,.92))
                if mode=='to-line': base=union(line((14,3),(14,13)),arr('right',6.6,8,.92))
                g(name,transform(base,angle))
    g('arrow-down-to-dot',arr('down',8,6,.75),circle(8,13.8,.9))
    g('arrow-up-from-dot',arr('up',8,6,.75),circle(8,13.8,.9))
    g('arrows-up-from-line',arr('up',4.4,7.3,.8),arr('up',11.6,7.3,.8),line((2,14),(14,14)))
    g('arrow-down-up',arr('down',4.5,8,.8),arr('up',11.5,8,.8))
    g('arrow-right-left',arr('right',8,4.5,.8),arr('left',8,11.5,.8))
    for horizontal in (True,False):
        p=union(line((2,8),(14,8)),line((5,5),(2,8),(5,11)),line((11,5),(14,8),(11,11)))
        g('move-'+('horizontal' if horizontal else 'vertical'),p if horizontal else transform(p,90))
    for name,angle in [('move-diagonal',-45),('move-diagonal-2',45)]:
        g(name,st(transform(path('M2 8H14M5 5L2 8L5 11M11 5L14 8L11 11'),angle,.95)))
    for name,angle in [('maximize-2',-45),('minimize-2',135)]:
        # Separated corners make the two-dimensional resize affordance clear.
        p=union(st('M2 6V2H6M10 14H14V10'),line((2,2),(6,6)),line((14,14),(10,10)))
        if name=='minimize-2': p=union(st('M6 2V6H2M10 14V10H14'),line((2,2),(6,6)),line((14,14),(10,10)))
        g(name,p)
    for inward in (True,False):
        name='shrink' if inward else 'expand'
        ps=[]
        for angle in (0,90,180,270):
            a=union(line((1.8,1.8),(5.5,5.5)),st('M2 5.5H5.5V2') if inward else st('M1.8 5.8V1.8H5.8'))
            ps.append(transform(a,angle))
        g(name,*ps)
    # Eight elbow directions share radius and head size while preserving turn.
    for initial,final,d in [
        ('down','left','M5 2V9Q5 11 7 11H14'),('down','right','M11 2V9Q11 11 9 11H2'),
        ('up','left','M5 14V7Q5 5 7 5H14'),('up','right','M11 14V7Q11 5 9 5H2'),
        ('left','down','M14 5H7Q5 5 5 7V14'),('left','up','M14 11H7Q5 11 5 9V2'),
        ('right','down','M2 5H9Q11 5 11 7V14'),('right','up','M2 11H9Q11 11 11 9V2')]:
        # Initial direction refers to the entering stem; terminal arrow follows
        # the last path point, never a generic directional badge.
        heads={'down-left':[(11,8),(14,11),(11,14)],'down-right':[(5,8),(2,11),(5,14)],
               'up-left':[(11,2),(14,5),(11,8)],'up-right':[(5,2),(2,5),(5,8)],
               'left-down':[(2,11),(5,14),(8,11)],'left-up':[(2,5),(5,2),(8,5)],
               'right-down':[(8,11),(11,14),(14,11)],'right-up':[(8,5),(11,2),(14,5)]}
        # Lucide's naming describes the terminal compass turn: correct the
        # horizontal end so corner-down-left ends toward the left.
        p=union(st(d),line(*heads[initial+'-'+final]))
        if initial in ('down','up'): p=mirror(p)
        g('corner-'+initial+'-'+final,p)

    for redo in (False,True):
        for suffix in ('2','dot'):
            p=union(st('M3 7H9Q14 7 14 12'),line((6,4),(3,7),(6,10)))
            if suffix=='dot': p=union(p,circle(4,13,1))
            g(('redo' if redo else 'undo')+'-'+suffix,mirror(p) if redo else p)
    for clockwise in (False,True):
        base=union(st('M12.8 5A5.5 5.5 0 1 0 13 10.8'),st('M9 5H13V1.5'))
        if not clockwise: base=mirror(base)
        suffix='cw' if clockwise else 'ccw'
        g('refresh-'+suffix,base)
        if clockwise: slash(base,'refresh-cw-off')
        else: g('refresh-ccw-dot',base,circle(8,8,.85))
        # Iteration uses a return loop rather than a circular refresh arrow.
        loop=union(st('M3 4H11Q14 4 14 7V10Q14 13 11 13H4'),line((6,10),(3,13),(6,15)))
        g('iteration-'+suffix,loop if clockwise else mirror(loop))
    repeat=union(st('M2.5 9V5Q2.5 3 4.5 3H13M13.5 7V11Q13.5 13 11.5 13H3'),st('M10 1L13 3L10 5M6 11L3 13L6 15'))
    g('repeat-2',repeat)
    slash(repeat,'repeat-off')
    for inward in (True,False):
        ps=[st('M8 1.6V4.2M8 7V9M8 11.8V14.4'), arr('right' if inward else 'left',3.6,8,.43), arr('left' if inward else 'right',12.4,8,.43)]
        g('fold-horizontal' if inward else 'unfold-horizontal',*ps)

    cat('Layout')
    def aligned_pair(position, lengths):
        guide_y = {'start': 2, 'center': 8, 'end': 14}[position]
        bars = []
        for x, length in zip((3.3, 9.6), lengths):
            y = {'start': 4.35, 'center': 8 - length / 2, 'end': 11.65 - length}[position]
            bars.append(rect(x, y, 3.1, length))
        body = union(*bars)
        rule = line((1.6, guide_y), (14.4, guide_y))
        if position == 'center':
            rule = sub(rule, union(body, outline(body, 2.5)))
        return body, rule

    for horizontal in (True,False):
        orient='horizontal' if horizontal else 'vertical'
        for position in ('start','center','end'):
            name=f'align-{position}-{orient}'
            p, rule = aligned_pair(position, (5, 8))
            if not horizontal: p,rule=transpose(p),transpose(rule)
            s(name,p,rule)
        for operation in ('distribute','justify'):
            for position in ('start','center','end'):
                name=f'align-{orient}-{operation}-{position}'
                y={'start':3,'center':8,'end':13}[position]
                blocks=[]
                if operation=='distribute':
                    centers = (3, 8, 13)
                    widths = (2.9, 2.9, 2.9) if position == 'center' else (2.7, 3.3, 2.7)
                    shift = {'start': -.5, 'center': 0, 'end': .5}[position]
                    ticks = []
                    for center, width in zip(centers, widths):
                        tick = center + shift * 2.7
                        left = tick - (.5 + shift) * width
                        blocks.append(rect(left, 5.2, width, 7.8))
                        ticks.append(line((tick, 1.7), (tick, 3)))
                    rules = union(*ticks)
                else:
                    blocks, rules = aligned_pair(position, (4, 6.7))
                body = union(*blocks) if operation == 'distribute' else blocks
                if (operation=='distribute' and not horizontal) or (operation=='justify' and horizontal):
                    body,rules=transpose(body),transpose(rules)
                s(name,body,rules)
        for behavior in ('around','between'):
            name=f'align-{orient}-space-{behavior}'
            if behavior=='around':
                objects = union(rect(3, 5, 3, 7), rect(10, 5, 3, 7))
                rules = union(*(line((x, 2), (x, 3.8)) for x in (1.4, 8, 14.6)))
            else:
                objects = union(rect(1.8, 3.5, 3, 9), rect(11.2, 3.5, 3, 9))
                rules = line((6.8, 8), (9.2, 8))
            if not horizontal: objects,rules=transpose(objects),transpose(rules)
            s(name,objects,rules)
    for horizontal in (True,False):
        for end in (False,True):
            name='between-'+('horizontal' if horizontal else 'vertical')+'-'+('end' if end else 'start')
            body=union(rect(1.8,2.5,2.8,11),rect(11.4,2.5,2.8,11))
            detail=st('M8 2.3V7M6.25 5.25L8 7L9.75 5.25')
            if end: detail=transform(detail,180)
            if horizontal: body,detail=transpose(body),transpose(detail)
            s(name,body,detail)

    def cells(cols,rows,x=2,y=2,w=12,h=12,gap=2):
        cw=(w-gap*(cols-1))/cols; ch=(h-gap*(rows-1))/rows
        return union(*(rect(x+i*(cw+gap),y+j*(ch+gap),cw,ch) for j in range(rows) for i in range(cols)))

    for cols,rows in [(2,2),(3,2),(3,3)]:
        if cols == rows == 3:
            s('grid-3x3', rr(), st('M6 2V14M10 2V14M2 6H14M2 10H14'))
        elif cols == 3:
            s('grid-3x2',rr(),st('M6 2V14M10 2V14M2 8H14'))
        else:
            s(f'grid-{cols}x{rows}',cells(cols,rows))
    slash(base_ink('grid-3x3'),'grid-3x3-off')
    for status,detail in [('check',check(12.1,12.3,.5)),('plus',plus(12.1,12.3,.6)),('x',cross(12.1,12.3,.6))]:
        body=union(rect(2,2,4.8,4.8),rect(9.2,2,4.8,4.8),rect(2,9.2,4.8,4.8))
        s('grid-2x2-'+status,body,detail)
    for count in (3,4):
        verticals = union(*(line((2+i*12/count,2),(2+i*12/count,14)) for i in range(1,count)))
        s('columns-'+str(count),rr(),verticals)
        s('rows-'+str(count),rr(),transpose(verticals))
    gear_center = (11.8, 11.8)
    teeth = []
    for tooth in range(6):
        for phase, radius in ((-.5, 2.55), (-.28, 2.55), (-.22, 3.5), (.22, 3.5), (.28, 2.55)):
            angle = (tooth + phase) * math.pi / 3
            teeth.append((11.8 + radius * math.cos(angle), 11.8 + radius * math.sin(angle)))
    cog = sub(poly(teeth), circle(*gear_center, 1.15))
    columns, dividers = api['DRAWINGS']['columns-3'][:2]
    badged('columns-3-cog', columns, dividers,
           cog, circle(*gear_center, 4.45))
    s('layout-panel-left',union(rect(2,2,4,12),rect(8,2,6,5),rect(8,9,6,5)))
    s('layout-panel-top',union(rect(2,2,12,4),rect(2,8,5,6),rect(9,8,5,6)))
    s('layout-freeform',union(rect(2,2,6,7),rect(10,5,4,9),rect(2,11,6,3)))
    s('layout-grid-circles',union(*(circle(x,y,2.4) for x in (4.5,11.5) for y in (4.5,11.5))))
    s('layout-grid-plus',union(rect(2,2,5,5),rect(9,2,5,5),rect(2,9,5,5)),plus(11.5,11.5,.85))
    for direction in ('down','right'):
        s('layout-arrow-'+direction,union(rect(2,2,5,5),rect(9,2,5,5),rect(2,9,5,5)),arr(direction,11.7,11.7,.45))
    for name,orientation in [('panel-bottom',90),('panel-right',0),('panel-top',270)]:
        for action in ('close','open'):
            # A dedicated panel with a divider and arrow crossing the divider.
            divider=line((10,2),(10,14))
            arrowpart=arr('right' if action=='close' else 'left',6,8,.43)
            s(name+'-'+action,rr(),transform(union(divider,arrowpart),orientation))
    for side,angle in [('left',180),('right',0),('top',270),('bottom',90)]:
        outer=outline(rr())
        guide=st('M10 4.15V6.8M10 9.2V11.85')
        g('panel-'+side+'-dashed',outer,transform(guide,angle))
    for name,angle in [('panel-left-right-dashed',0),('panel-top-bottom-dashed',90)]:
        g(name,outline(rr()),transform(st('M5.5 4.15V6.8M5.5 9.2V11.85M10.5 4.15V6.8M10.5 9.2V11.85'),angle))
    for name,angle in [('panels-left-bottom',0),('panels-right-bottom',180),('panels-top-left',90)]:
        divider=st('M6 2V14M6 10H14')
        s(name,rr(),mirror(divider) if name=='panels-right-bottom' else transform(divider,angle))
    s('app-window-mac',rr(1.5,2.5,13,11),union(line((1.5,6),(14.5,6)),dots((4,4.3),(6.3,4.3),(8.6,4.3),r=.45)))
    s('dock',rr(1.5,2,13,12),union(outline(rect(3.5,9,9,3.2)),dots((5.5,10.6),(8,10.6),(10.5,10.6),r=.45)))
    for vertical in (False,True):
        for end in (False,True):
            body=rect(4.5 if not end else 1.5,2,8,12)
            if end: extras=st('M11 2.7Q12 2.8 12 4V12Q12 13.2 11 13.3M14 3.6Q14.7 3.9 14.7 4.9V11.1Q14.7 12.1 14 12.4')
            else: extras=union(line((1.5,2),(1.5,14)),line((14.5,2),(14.5,14)))
            if vertical: body,extras=transform(body,90),transform(extras,90)
            s('gallery-'+('vertical' if vertical else 'horizontal')+('-end' if end else ''),body,extras)
    s('gallery-thumbnails',union(rect(1.8,1.8,12.4,7.4),rect(1.8,11.5,2.9,2.9),rect(6.55,11.5,2.9,2.9),rect(11.3,11.5,2.9,2.9)))
    for horizontal in (True,False):
        p = st('M2 2V14M14 2V14M4.1 8H6.8M5.4 6.6L6.8 8L5.4 9.4M11.9 8H9.2M10.6 6.6L9.2 8L10.6 9.4')
        g('gap-'+('horizontal' if horizontal else 'vertical'),p if horizontal else transform(p,90))
        p = union(outline(rect(1.8, 3.6, 12.4, 8.8)), st('M7 8H4.1M5.7 6.4L4.1 8L5.7 9.6M9 8H11.9M10.3 6.4L11.9 8L10.3 9.6'))
        g('stretch-'+('horizontal' if horizontal else 'vertical'),p if horizontal else transform(p,90))
    g('handle-bottom-right',line((8,14),(14,8)),line((12,14),(14,12)))
    s('ratio', rr(1.8, 3.4, 12.4, 9.2), st('M4.4 8V6H7.3M11.6 8V10H8.7'))
    s('proportions',rr(1.8,3,12.4,10),outline(rect(6.2,6.4,5.6,4.1)))
    for vertical in (False,True):
        s('rectangle-'+('vertical' if vertical else 'horizontal'),rect(4 if vertical else 1.8,1.8 if vertical else 4,8 if vertical else 12.4,12.4 if vertical else 8))
    s('rectangle-ellipsis',rr(1.8,4,12.4,8),dots((4.5,8),(8,8),(11.5,8),r=.65))
    for name in ('margin','margin-top','margin-bottom','margin-left','margin-right','margin-horizontal','margin-vertical',
                 'square-padding','square-padding-top','square-padding-bottom','square-padding-left','square-padding-right','square-padding-horizontal','square-padding-vertical'):
        padding=name.startswith('square-padding')
        side=name.removeprefix('square-padding').removeprefix('margin').lstrip('-')
        selected=('top','bottom','left','right') if not side else ('left','right') if side=='horizontal' else ('top','bottom') if side=='vertical' else (side,)
        body=rr(2,2,12,12)
        if name == 'square-padding':
            marks = union(*(transform(line((7.4, 3.9), (8.6, 3.9)), a) for a in (0, 90, 180, 270)))
            s(name, body, union(outline(rect(5.85, 5.85, 4.3, 4.3)), marks))
            continue
        if name == 'margin':
            s(name, body, outline(rect(5, 5, 6, 6)))
            continue
        rules=[]
        for edge in selected:
            turn = {'top':0,'right':90,'bottom':180,'left':270}[edge]
            y = 6.2 if padding else 4.55
            rules.append(transform(line((2,y),(14,y)),turn))
            if padding:
                rules.append(transform(line((7.25,4.1),(8.75,4.1)),turn))
        if not padding:
            cx = 8 + (1.5 if side == 'left' else -1.5 if side == 'right' else 0)
            cy = 8 + (1.5 if side == 'top' else -1.5 if side == 'bottom' else 0)
            width,height = (2.65,5.1) if side=='horizontal' else (5.1,2.65) if side=='vertical' else (4,4)
            rules.append(outline(rect(cx-width/2,cy-height/2,width,height)))
        s(name,body,union(*rules))

    cat('Geometry')
    for name,n,rotation in [('triangle',3,-90),('pentagon',5,-90),('hexagon',6,-90),('octagon',8,-22.5),('diamond',4,-90)]:
        r=6.2
        points=[(8+r*math.cos(math.radians(rotation)+2*math.pi*i/n),8+r*math.sin(math.radians(rotation)+2*math.pi*i/n)) for i in range(n)]
        s(name,poly(points))
    s('triangle-right',poly([(3,2),(3,14),(14,14)]))
    s('octagon-pause',poly([(5,1.7),(11,1.7),(14.3,5),(14.3,11),(11,14.3),(5,14.3),(1.7,11),(1.7,5)]),union(line((6,5),(6,11)),line((10,5),(10,11))))
    ellipse=path('M1.5 8C1.5 1.8 14.5 1.8 14.5 8C14.5 14.2 1.5 14.2 1.5 8Z')
    s('ellipse',ellipse)
    squircle=path('M8 1.7C13.8 1.7 14.3 2.2 14.3 8C14.3 13.8 13.8 14.3 8 14.3C2.2 14.3 1.7 13.8 1.7 8C1.7 2.2 2.2 1.7 8 1.7Z')
    s('squircle',squircle)
    # Dashed primitive shapes intentionally stay line-only in all styles.
    g('circle-dashed',dash_circle())
    g('circle-small',outline(circle(8,8,3.3)))
    g('circle-dot-dashed',dash_circle(),circle(8,8,1.3))
    g('circle-dashed-check',dash_circle(),check(8,8,.75))
    g('square-dashed',dash_square())
    g('squircle-dashed',union(*(transform(st('M3 1.9Q1.9 1.9 1.9 3'),a) for a in (0,90,180,270))),union(*(transform(line((6.2,1.7),(9.8,1.7)),a) for a in (0,90,180,270))))
    g('triangle-dashed', st('M7 4L8 2L9 4M5.8 6.4L4.4 9.2M3.1 11.8L2 14H4.4M6.9 14H9.1M11.6 14H14L12.9 11.8M11.6 9.2L10.2 6.4'))
    astroid=path('M8 1.7Q8 8 14.3 8Q8 8 8 14.3Q8 8 1.7 8Q8 8 8 1.7Z')
    s('astroid',astroid)
    s('sparkle',poly([(8,1.6),(9.8,6.2),(14.4,8),(9.8,9.8),(8,14.4),(6.2,9.8),(1.6,8),(6.2,6.2)]))
    star_lines = 'M8 5.6V10.4M5.92 6.8L10.08 9.2M5.92 9.2L10.08 6.8'
    g('asterism', *(placed_stroke(star_lines, x, y) for x, y in ((8, 4.1), (4.1, 11.4), (11.9, 11.4))))
    # A single continuous trefoil boundary avoids internal lobe seams.
    s('club',path('M6.2 6.4C3 3.2 5.5 1.4 8 1.4C10.5 1.4 13 3.2 9.8 6.4C13.1 4.6 15.2 7 14 9.7C13 12 10 12 8.8 10Q9 12.5 10.6 14H5.4Q7 12.5 7.2 10C6 12 3 12 2 9.7C.8 7 2.9 4.6 6.2 6.4Z'))
    s('spade',union(path('M8 1.6L2.8 6.8C-1 11 5 14 8 10C11 14 17 11 13.2 6.8Z'),poly([(8,9),(5.3,14.3),(10.7,14.3)])))
    s('cross',poly([(6,2),(10,2),(10,6),(14,6),(14,10),(10,10),(10,14),(6,14),(6,10),(2,10),(2,6),(6,6)]))
    s('circle-dot',circle(),circle(8,8,1.5))
    slash(outline(circle()),'circle-off')
    s('circle-pile',union(circle(8,4.3,2.6),circle(4.5,10.8,2.6),circle(11.5,10.8,2.6)))
    g('angle',line((3,3),(3,13),(14,13)),st('M3 8Q8 8 8 13'))
    g('diameter',outline(circle()),line((3.76,12.24),(12.24,3.76)))
    g('radius',outline(circle()),line((8,8),(12.2,3.8)),circle(8,8,.9))
    g('tangent',outline(circle(8,9.5,4.2)),line((1.7,5.3),(14.3,5.3)))
    g('axis-3d',line((8,8),(8,1.7)),line((8,8),(14,12.8)),line((8,8),(2,12.8)),st('M6 3.7L8 1.7L10 3.7M11.4 12.6L14 12.8L13.5 10.2M2.5 10.2L2 12.8L4.6 12.6'))
    box=path('M8 1.8L14 5V11L8 14.2L2 11V5Z')
    seams=st('M2 5L8 8.5L14 5M8 8.5V14.2')
    s('box',box,seams)
    # Three boxes rather than a badged single box.
    def small_box(x, y, scale):
        edges = 'M8 1.8L14 5V11L8 14.2L2 11V5ZM2 5L8 8.5L14 5M8 8.5V14.2'
        return placed_stroke(edges, x, y, scale)
    g('boxes', small_box(8,4.45,.47), small_box(4.35,11.35,.47), small_box(11.65,11.35,.47))
    s('cuboid',path('M6 1.8L14 4.8V11.3L10 14.2L2 11.2V4.7Z'),st('M2 4.7L10 7.8L14 4.8M10 7.8V14.2'))
    s('cone',path('M8 1.6L14 12Q14 14.5 8 14.5Q2 14.5 2 12Z'),st('M2 12Q8 9 14 12'))
    s('pyramid',poly([(8,1.7),(14,12.5),(7,14.2),(2,11.5)]),st('M8 1.7L7 14.2'))
    s('cylinder',path('M2.5 4Q2.5 1.5 8 1.5Q13.5 1.5 13.5 4V12Q13.5 14.5 8 14.5Q2.5 14.5 2.5 12Z'),st('M2.5 4Q2.5 6.5 8 6.5Q13.5 6.5 13.5 4'))
    outside = path('M1.6 8C1.6 1.4 14.4 1.4 14.4 8C14.4 14.6 1.6 14.6 1.6 8Z')
    bore = path('M4.85 7.35C4.85 4.55 11.15 4.55 11.15 7.35C11.15 10.15 4.85 10.15 4.85 7.35Z')
    torus = sub(outside, bore)
    s('torus', torus)
    g('shapes',outline(circle(4,5.1,2.3)),outline(rect(6.6,9.4,5.2,5.2)),outline(poly([(11.2,1.65),(14.4,7),(8.05,7)])))
    g('component', *(outline(transform(rect(6.15, 1.55, 3.7, 3.7), a)) for a in (0,90,180,270)))
    g('vector-square',st('M4.5 2.5H11.5M13.5 4.5V11.5M11.5 13.5H4.5M2.5 11.5V4.5'),*(outline(rect(x,y,3,3)) for x,y in [(1,1),(12,1),(1,12),(12,12)]))
    g('vector-polygon',st('M3 11L6 3L13 6L11 13Z'),*(rect(x-1.35,y-1.35,2.7,2.7) for x,y in [(3,11),(6,3),(13,6),(11,13)]))

    cat('Math and symbols')
    divide=union(line((3,8),(13,8)),dots((8,3.5),(8,12.5),r=.9))
    equals=union(line((3,5.5),(13,5.5)),line((3,10.5),(13,10.5)))
    approximately=union(st('M2.5 5.5C5 1.5 11 9.5 13.5 5.5'),st('M2.5 10.5C5 6.5 11 14.5 13.5 10.5'))
    sigma=st('M12.5 2.5H3.5L8 8L3.5 13.5H12.5')
    def paragraph(x=8, y=8, scale=1):
        bowl = path('M8 2.8V9.6H6.3C1.7 9.6 1.7 2.8 6.3 2.8Z')
        stems = 'M12.7 2.8H7.8V13.2M11.5 2.8V13.2'
        return union(fit(bowl,x,y,scale), placed_stroke(stems,x,y,scale))
    pilcrow = paragraph()
    for name,p in [('divide',divide),('equal-not',union(equals,line((4,14),(12,2)))),
                   ('equal-approximately',approximately),
                   ('equal-approximately-not',union(approximately,line((4,14),(12,2)))),
                   ('sigma',sigma),('pilcrow',pilcrow),('lambda',st('M3 2Q5 1 6.5 5L11 13Q12 15 14 13M7.5 7L3 14')),
                   ('omega',st('M3 13H6V10.5C-.5 7 3 1.5 8 1.5C13 1.5 16.5 7 10 10.5V13H13')),
                   ('phi',union(outline(circle(8,8,4.5)),line((8,1.7),(8,14.3)))),
                   ('exclamation-mark',union(line((8,2),(8,9.5)),circle(8,13,.75))),
                   ('question-mark',union(st('M4.5 5Q4.5 1.5 8.5 1.5Q12.5 1.5 12.5 5Q12.5 7 9.5 8Q8 8.5 8 10'),circle(8,13.5,.8))),
                   ('weight-tilde',st('M2 9C5 1.5 10.6 14.5 14 7'))]:
        g(name,p)
    compact_math = {
        'divide': union(st('M4.9 8H11.1'), dots((8, 5.2), (8, 10.8), r=.7)),
        'equal': st('M4.8 6.4H11.2M4.8 9.6H11.2'),
        'pi': st('M4.4 5.1H11.7M6.5 5.1V9.5Q6.5 11 5.6 11.4M9.8 5.1V10Q9.8 11.2 11 11.2'),
        'sigma': st('M10.9 4.8H5.1L8 8L5.1 11.2H10.9'),
        'pilcrow': paragraph(scale=.65),
        'asterisk': placed_stroke(star_lines, scale=1.35),
        'function': st('M10.6 4.8Q8.4 3.8 8.1 6.2L7.6 9.9Q7.3 12.4 5.3 11.4M5.8 7.5H10.4'),
    }
    for symbol, mark in compact_math.items():
        s('square-' + symbol, rr(), mark)
        if symbol in ('divide', 'equal'):
            s('circle-' + symbol, circle(), mark)
    for i in range(1,6):
        ps=[line((3.5+j*3,3),(3.5+j*3,13)) for j in range(min(4,i))]
        if i==5: ps.append(line((2,11.5),(14,4.5)))
        if i<4: ps=[fit(p,8+(4-i)*1.5,8) for p in ps]
        g('tally-'+str(i),*ps)
    amp = 'M12.8 13L5.3 5.8Q2.8 2.2 6.7 1.8Q10.5 1.6 9 4.5L4 8C.5 10.5 4 15.2 8 13.4Q12 11.7 13 8'
    g('ampersand',st(amp))
    g('ampersands',placed_stroke(amp,4.6,8,.59),placed_stroke(amp,11.65,8,.59))
    g('section',st('M10.7 2.6C7.8 .6 3.5 2.3 5.4 4.8C6.9 6.6 11.9 6.8 11.2 9.5Q10.9 10.7 9.4 11.1M5.3 13.4C8.2 15.4 12.5 13.7 10.6 11.2C9.1 9.4 4.1 9.2 4.8 6.5Q5.1 5.3 6.6 4.9'))
    g('copyright' if 'copyright' in NAMES else 'copyleft',outline(circle()),mirror(letter('c',scale=.58)))
    s('creative-commons',circle(),union(letter('c',5.65,8,.31),letter('c',10.35,8,.31)))

    cat('Typography and text')
    lower_a = 'M12 5.4V13M12 9.2C12 4.1 3.5 4.1 3.5 9.2S12 14.3 12 9.2Z'
    lower_b = 'M4 2V13M4 9.2C4 4.1 12.5 4.1 12.5 9.2S4 14.3 4 9.2Z'
    for name,p in [('case-upper',union(letter('a',4.2,8,.52),letter('b',11.7,8,.52))),
                   ('case-lower',union(placed_stroke(lower_a,4.3,8,.54),placed_stroke(lower_b,11.5,8,.54))),
                   ('case-sensitive',union(letter('a',4.3,7.8,.54),placed_stroke(lower_a,11.7,8.27,.48))),
                   ('a-large-small',union(letter('a',4.5,7.5,.62),letter('a',12,8.6,.4)))]:
        g(name,p)
    for direction in ('up','down'):
        g('a-arrow-'+direction,letter('a',5.5,8,.7),arr(direction,12.5,8,.53))
    g('baseline',letter('a',8,7.2,.86),line((2.5,13.7),(13.5,13.7)))
    g('letter-spacing',letter('a',4.2,6,.48),letter('a',11.8,6,.48),st('M2 12.7H14M3.8 10.9L2 12.7L3.8 14.5M12.2 10.9L14 12.7L12.2 14.5'))
    g('line-height',st('M8 3H14M8 8H12M8 13H14'),st('M3.3 2.3V13.7M1.4 4.2L3.3 2.3L5.2 4.2M1.4 11.8L3.3 13.7L5.2 11.8'))
    g('ligature', st('M4.4 13.5V6C4.4 3.2 5.9 2 8.2 2H9M2.4 6.7H11.5V13.5'), circle(11.5, 3, .75))
    for i in (5,6):
        g('heading-'+str(i),letter('h',5.2,8,.68),number(str(i),12.1,9.7,.47))
    g('type-outline',st('M6.85 2.4H9.15L14.2 13.6H11L9.95 11H6.05L5 13.6H1.8ZM8 5.65L6.9 8.5H9.1Z'))
    for subscript in (True,False):
        g('subscript' if subscript else 'superscript',letter('x',5.4,8,.68),number('2',12,11.7 if subscript else 4.3,.46))
    for direction in ('left','right'):
        g('pilcrow-'+direction,paragraph(5.3 if direction=='right' else 10.7,8,.74),arr(direction,12.5 if direction=='right' else 3.5,9,.39))
    g('remove-formatting',letter('t',6.7,6.5,.8),line((2,14),(8,14)),cross(12.3,12.1,.65))
    g('spell-check-2',letter('a',4.3,4.8,.43),letter('b',11.4,4.8,.43),st('M2.3 11.6Q3.6 9.2 5 11.6T7.7 11.6'),check(11.9,11.4,.65))
    for direction in ('left','right'):
        g('decimals-arrow-'+direction,circle(2.25,7.1,.65),number('0',6,5.2,.46),number('0',12,5.2,.46),arr(direction,8,12.1,.72))
    for end in ('center','end','start'):
        last={'center':(4,12),'end':(6,14),'start':(2,10)}[end]
        g('text-align-justify-'+end,st('M2 2.5H14M2 6.2H14M2 9.9H14'),line((last[0],13.6),(last[1],13.6)))
    g('summary',line((2,2.5),(11,2.5)),st('M2 6H14M2 9.5H14M2 13H9'))
    g('text-quote',st('M6.3 3.7H13.8M6.3 7.8H13.8M6.3 11.9H11.8'),st('M2.7 2.6V13'))
    g('text-wrap',st('M2 3H14M2 7H11Q14 7 14 10Q14 13 11 13H6'),line((8.5,10.5),(6,13),(8.5,15.5)),line((2,11),(3.5,11)))
    g('text-initial',letter('a',4.5,7.5,.57),st('M9 3H14M9 6.5H14M9 10H14M2 13.5H14'))
    g('whole-word',label('ab',8,6.1,.52),st('M1.8 10.7V12.8H14.2V10.7'))
    g('space',st('M2 6V10H14V6'))
    field = rect(1.5,4,13,8)
    caret = st('M6.2 1.6H9.8M8 1.6V14.4M6.2 14.4H9.8')
    badged('text-cursor-input',field,empty,caret,rect(6.45,0,3.1,16,0))
    text_small=st('M2 3H14M2 7H8M2 11H6')
    search=union(ring(11,10.5,2.6),line((13,12.5),(15,14.5)))
    g('text-search',text_small,search)
    pen=path('M2 11L11.5 1.5L14.5 4.5L5 14H1.5Z')
    pen_detail=st('M10 3L13 6M2 11L5 14')
    pen_glyph=union(outline(pen),pen_detail)
    def pencil_body(x, y):
        return fit(path('M4.7 9.7L10.7 3.7L13 6L7 12L3.7 13Z'), x, y, .62)

    def pencil_mark(x, y):
        return outline(pencil_body(x, y))

    def pencil_clearance(x, y):
        body = pencil_body(x, y)
        return union(body, outline(body, 3.2))

    g('text-pen',st('M2 3H10M2 7H7M2 11H4'),pencil_mark(10.7,10.4))
    g('table-of-contents',st('M2 3H9.5M2 8H7.5M2 13H9.5M12.4 3H14.2M12.4 8H14.2M12.4 13H14.2'))
    list_rows = st('M8 3H14M8 8H14M8 13H14')
    g('list-check', st('M7 3H14M7 8H14M7 13H14'), check(3.5,8,.55))
    for suffix, y in [('start', 3.3), ('end', 12.7)]:
        g('list-' + suffix, list_rows, line((1.7, y), (5.6, y)),
          line((3.8, y - 1.8), (5.6, y), (3.8, y + 1.8)))
    for behavior in ('down-up','up-down'):
        g('list-chevrons-'+behavior,st('M7 3H14M7 8H14M7 13H14'),chev('down' if behavior=='down-up' else 'up',3,4.5,.4),chev('up' if behavior=='down-up' else 'down',3,11.5,.4))
    g('list-collapse',st('M7 3H14M7 8H14M7 13H14'),chev('right',3,8,.6))
    g('list-restart',st('M2 3H14M2 7H9M2 11H6'),st('M13.8 13.5A3 3 0 1 1 13.9 9.7M11.7 9.7H14.1V7.3'))
    g('list-filter-plus',st('M2 3H14M4 7H12M6 11H8'),plus(12.5,12.5,.7))
    # Replace controls use actual text groups and directed exchange routes.
    g('replace', letter('a',5.2,4.7,.5), letter('b',10.8,11.6,.5),
      st('M9.7 2H12.1Q13.3 2 13.3 3.2V7M11.8 5.5L13.3 7L14.8 5.5'))
    source_a = path('M1.6 6.2L3.7 1.7L5.8 6.2M2.45 4.7H4.95')
    g('replace-all', st(source_a), st(transform(source_a, dy=7.8)),
      st('M7.4 4.2V8H9.9M8.6 6.6L10 8L8.6 9.4'),
      st('M12 5.5V10.5H13.2C15.2 10.5 15.2 8 13.2 8H12M12 5.5H13.1C15 5.5 15 8 13.1 8'))
    # Product registers link-2 after this lane. Use its link centerline.
    slash(placed_stroke('M6 10L5 11A2.5 2.5 0 0 1 1.5 7.5L4 5A2.5 2.5 0 0 1 7.5 5M10 6L11 5A2.5 2.5 0 0 1 14.5 8.5L12 11A2.5 2.5 0 0 1 8.5 11M5.5 10.5L10.5 5.5',scale=.966), 'link-2-off')
    end = st('M6.1 7.4L4.4 9.1C1.7 11.8 4.2 14.3 6.9 11.6L8.6 9.9')
    g('unlink-2', end, transform(end, 180), st('M2.2 5H4.3M5 2.2V4.3M13.8 11H11.7M11 13.8V11.7'))

    cat('Documents and books')
    book=rr(3,1.7,10,12.6)
    book_seam = 'M5.6 1.8V11.4M13 11.4H5.3Q3.1 11.4 3.1 13'
    book_spine = st(book_seam)
    open_book=path('M8 3.5Q4 1 1.5 3V12Q4 10.8 8 13.5Q12 10.8 14.5 12V3Q12 1 8 3.5Z')
    for name,detail in [('book-a',letter('a',9,7,.38)),('book-type',letter('t',9,7,.38)),
                        ('book-bookmark',st('M8 2V8.4L9.7 7L11.4 8.4V2')),
                        ('book-exclamation-point',union(line((9.3,4),(9.3,6.65)),circle(9.3,9,.65)))]:
        s(name,book,union(book_spine,detail))
    # Distinct rear copy remains visible at the top and left.
    g('book-copy',st('M3 11.6H2.8Q1.6 11.6 1.6 10.4V2.8Q1.6 1.6 2.8 1.6H10.4'),
      outline(rect(4.4,4,9.5,10.4)),st('M7 4V11.7M13.9 11.7H6.5Q4.4 11.7 4.4 13'))
    for name,detail in [('book-open-text',st('M3.65 5.6Q4.5 5.35 5.8 5.9M3.65 8.6Q4.5 8.35 5.8 8.9M10.2 5.9Q11.5 5.35 12.35 5.6M10.2 8.9Q11.5 8.35 12.35 8.6')),('book-open-check',check(11,7.5,.46))]:
        s(name,open_book,union(line((8,3.5),(8,13.5)),detail))
    # Parallel library spines are discrete books, not a comb of lines.
    library=union(rect(1.5,2,2.45,12),rect(6.1,2,2.45,12),poly([(10.6,2.6),(12.8,2.2),(14.7,13.4),(12.5,13.8)]))
    s('library-big',library,st('M1.5 5.8H3.95M6.1 5.8H8.55M11.1 5.9L13.3 5.5'))
    s('square-library',rr(),st('M4.7 4.8V11.2M7.6 4.8V11.2M10 5L11.5 11.1'))
    notebook=rr(3,1.7,10.5,12.6)
    binding=union(*(line((1.8,y),(4,y)) for y in (4,8,12)))
    for name,detail in [('notebook-dot',circle(9,8,1.1)),('notebook-text',st('M6 5H11M6 8H11M6 11H9')),
                        ('notebook-pen',pencil_mark(11.5,11.5))]:
        if name=='notebook-pen':
            cover, lines = api['DRAWINGS']['notebook'][:2]
            badged(name, cover, lines, detail, union(pencil_clearance(11.5,11.5), rect(12.2,12.7,4,4,0)))
        else: s(name,notebook,union(binding,detail))
    notepad=rr(2.5,3,11,11.5)
    rings=union(*(line((x,1.5),(x,4.5)) for x in (5,8,11)))
    note_text=st('M5 7H11M5 10H11M5 12.5H9')
    s('notepad-text',notepad,union(rings,note_text))
    g('notepad-text-dashed',st('M2.5 6.4V4.25Q2.5 3 3.75 3H12.25Q13.5 3 13.5 4.25V6.4M2.5 9V11M13.5 9V11M2.7 13.35Q2.8 14.3 4 14.3H5.6M8.2 14.3H9.8M12.2 14.3Q13.4 14.3 13.5 13.1'),rings,st('M5.3 7H10.7M5.3 10H9.2'))
    clip = union(rect(3,3.2,10,11), rect(5.5,1.5,5,3.2))
    tab = st('M5.5 3.25V3.45Q5.5 4.7 6.75 4.7H9.25Q10.5 4.7 10.5 3.45V3.25')
    s('clipboard-type',clip,union(tab,letter('t',8,9.3,.42)))
    badged('clipboard-pen-line',clip,union(tab,line((5.5,11),(7.5,11))),
           pencil_mark(11.5,11), union(pencil_clearance(11.5,11), rect(11.8,12.4,4,4,0)))
    sheet=rr(2,2,12,12)
    grid=st('M2 5.5H14M2 9.5H14M6 2V14M10 5.5V14')
    s('sheet',sheet,grid)
    s('table-2',sheet,st('M2 6H14M2 10H14M6 6V14'))
    s('table-properties',sheet,st('M2 8H14M6 2V14M8.5 5H11.7M8.5 11H10.6'))
    for horizontal in (True,False):
        body=union(rect(1.5,2,5,12),rect(9.5,2,5,12))
        detail=st('M1.5 6H6.5M9.5 6H14.5M1.5 10H6.5M9.5 10H14.5')
        if not horizontal: body,detail=transform(body,90),transform(detail,90)
        s('table-'+('columns' if horizontal else 'rows')+'-split',body,detail)
    sticky=path('M3 2H13Q14 2 14 3V10L10 14H3Q2 14 2 13V3Q2 2 3 2Z')
    fold=st('M10 14V10H14')
    for status,detail in [('plus',plus(7.5,7,.7)),('minus',line((5,7),(10,7))),('x',cross(7.5,7,.65)),('check',check(7.5,7,.65))]:
        s('sticky-note-'+status,sticky,union(fold,detail))
    slash(base_ink('sticky-note'),'sticky-note-off')
    g('sticky-notes',st('M11 1.6H3Q1.6 1.6 1.6 3V11'),outline(fit(sticky,9.4,9.4,.8)),placed_stroke('M10 14V10H14',9.4,9.4,.8))

    cat('Design tools')
    # Pen and pencil surfaces differ: nib for pen, wood and graphite for pencil.
    def fountain_nib(x=8, y=8, scale=1):
        silhouette = path('M5.4 1.8H10.6V4.4Q10.6 5.3 12 7L8 14.2L4 7Q5.4 5.3 5.4 4.4Z')
        def place(p):
            return transform(p, 40, scale, x - 8, y - 8)
        body = place(silhouette)
        marks = union(outline(place(circle(8, 8.1, .95))),
                      st(place(path('M8 9.1V14.2M5.4 4.4H10.6'))))
        return body, marks

    nib, nibdetail = fountain_nib()
    s('pen', nib, nibdetail)
    small_nib, small_detail = fountain_nib(8.2, 6.6, .84)
    s('pen-line', small_nib, union(small_detail, line((2.2, 14), (13.8, 14))))
    cancelled('pen-off', union(outline(api['DRAWINGS']['pen'][0]), nibdetail), (2.2, 1.8), (14.2, 11.4))
    s('pencil-line',fit(pen,8.5,6.5,.8),union(placed_stroke('M10 3L13 6M2 11L5 14',8.5,6.5,.8),line((2,14),(14,14))))
    slash(pen_glyph,'pencil-off')
    def sparkle_at(x, y, radius):
        sparkle = path('M8 4Q8.7 7.3 12 8Q8.7 8.7 8 12Q7.3 8.7 4 8Q7.3 7.3 8 4Z')
        return fit(sparkle,x,y,radius/4)

    s('pencil-sparkles',fit(pen,7.4,9.5,.76),
      union(placed_stroke('M10 3L13 6',7.4,9.5,.76),sparkle_at(12.5,3,1.8),sparkle_at(4.3,3.5,1.45)))
    brushbody = path('M2.1 14Q4 12.5 4 10.8Q4 7.2 7 7.4L11.8 2.3Q12.9 1.1 14 2.2Q15 3.2 13.8 4.4L9.1 9.4Q9 12.8 6.3 13.5Q4.7 14.1 2.1 14Z')
    s('brush',brushbody,inter(brushbody,st('M6.6 7L9.6 10')))
    brushvertical=path('M7.8 1.55Q9.4 1.55 9.4 3.1L9.15 6.5Q9.15 7.4 10.3 7.9L12 8.7V14H4V8.7L5.7 7.9Q6.85 7.4 6.85 6.5L6.6 3.1Q6.6 1.55 7.8 1.55Z')
    s('paintbrush-vertical',brushvertical,st('M4 10H12M5.85 7.8H10.15M7 12.4V14M9.5 12.4V14'))
    s('paint-roller',rect(1.7,2,10,4.5),union(st('M11.7 4.3H14V9H8V11'),rect(6.8,11,2.4,3.5)))
    bucket = path('M2.1 8.2L7.6 2.7L13.8 8.9H11.8L7.6 13.1Q6.9 13.8 6.1 13Z')
    handle = st('M4.2 7.6C2.2 3.4 3.1 1.4 4.8 1.6Q6.5 1.8 7.6 4.9')
    drop = path('M13.5 10.3Q15 12.3 14.9 13Q14.8 14.5 13.5 14.5Q12.2 14.5 12.1 13Q12 12.3 13.5 10.3Z')
    s('paint-bucket', bucket, union(handle, st('M2.6 8.7H11.8'), drop))
    spray=rect(3,6,7.5,8.5)
    s('spray-can',spray,union(outline(rect(4.5,3,4.5,3)),st('M6.75 3V1.65H8.6'),dots((11.3,1.65),(14.35,1.25),(14.25,3.6),r=.55),line((5.5,9),(5.5,12))))
    stamp=path('M3 10H13L14 14H2Z')
    s('stamp',stamp,st('M5 10V8Q7 7 6 5Q4 1.5 8 1.5Q12 1.5 10 5Q9 7 11 8V10'))
    compasslegs=union(st('M7.2 5.7L3 14M8.8 5.7L13 14M5.07 9.9H10.93'),outline(circle(8,3.9,1.95)),line((8,1.25),(8,1.95)))
    g('drafting-compass',compasslegs)
    g('magnet',st('M3 2V8.5C3 15.5 13 15.5 13 8.5V2H9.5V8.5C9.5 10.8 6.5 10.8 6.5 8.5V2ZM3 5H6.5M9.5 5H13'))
    wand_body = poly([(2,12),(11.5,2.5),(13.5,4.5),(4,14)])
    wand_tip = poly([(8.5,5.5),(11.5,2.5),(13.5,4.5),(10.5,7.5)])
    wand = union(outline(wand_body),wand_tip)
    g('wand',wand)
    g('wand-sparkles',placed_stroke('M2 12L11.5 2.5L13.5 4.5L4 14ZM9 5L11 7',7,9.3,.83),sparkle_at(12.6,3,1.7),sparkle_at(4.2,3.7,1.45))
    s('slice', path('M1.6 13.5L3.7 8.9L5.4 7.2L7.3 7.2L11.9 2.6Q13.2 1.3 14.2 2.7Q15 3.8 13.8 5L8.3 10.5L6.9 10.6Z'),
      st('M5.4 7.2L8.3 10.5M9.8 4.7L12.2 7.1'))
    g('signature',st('M1.5 11C6 14 8-1 5.5 2C3 5 4.5 14 7 11L9 8Q9 14 11 10Q12 7 13 9Q13.5 11 15 9'),line((3,14),(13,14)))
    g('line-squiggle',st('M1.5 11C5-2 2 17 8 8C14-1 9 17 14.5 5'))
    g('line-style',line((2,3),(14,3)),line((2,8),(7,8)),line((10,8),(14,8)),dots((2.5,13),(6.2,13),(9.9,13),(13.6,13),r=.6))
    spline = 'M3.7 12.4C9.8 12.2 6.4 3.8 12.3 3.6'
    g('spline',sub(st(spline),union(circle(2.75,12.65,1.4),circle(13.25,3.35,1.4))),outline(circle(2.75,12.65,1.4)),outline(circle(13.25,3.35,1.4)))
    pointer2=poly([(2.5,1.8),(13.8,8),(8.5,9),(6.8,14.3)])
    g('spline-pointer',sub(st('M3.5 10.6C9.3 10.5 5.6 3.2 12.6 3.2'),circle(2.85,10.8,1.3)),
      outline(circle(2.85,10.8,1.3)),outline(fit(pointer2,11.3,11.1,.55)))
    g('lasso',st('M4 10C.6 7.4 2.3 2.1 8 2.1C14.4 2.1 16 8.5 11.5 10.9Q8.4 12.6 5.8 11.1Q4.3 10.3 3.1 12Q2.1 13.6 4.5 14.2'))
    g('lasso-select', st('M4.4 10.4C.4 7.7 2.6 2.2 7.7 2.2C11.6 2.2 14.5 4.5 13.4 7.3M7.1 10.8Q4.6 9.6 3 11.7Q2.1 13.1 3.6 14'), outline(fit(pointer2,11.6,11.6,.5)))
    g('frame',st('M4 1V15M12 1V15M1 4H15M1 12H15'))
    handles = union(*(transform(st('M1.6 4.2V2.2Q1.6 1.6 2.2 1.6H4.2'), a)
                      for a in (0, 90, 180, 270)))
    front = rect(7.2, 7.2, 4.9, 4.9)
    g('group', handles, sub(outline(rect(4.1, 4.1, 5, 5)), front), outline(front))
    for cap in ('butt','round','square'):
        # Literal cap demonstrations retain the corresponding end shape.
        guides = st('M3.75 3V5.7M3.75 10.3V13M12.25 3V5.7M12.25 10.3V13')
        if cap == 'round':
            body = line((3.75,8),(12.25,8))
        else:
            extension = api['STROKE']/2 if cap == 'square' else 0
            body = rect(3.75-extension,8-api['STROKE']/2,8.5+2*extension,api['STROKE'],0)
        g('stroke-line-cap-'+cap,body,guides)
    for join in ('bevel','miter','round'):
        if join=='round':
            sample = st('M2.5 13L8 3L13.5 13')
            # Two normal cuts expose the flat free ends of the join sample.
            body = inter(sample,path('M0 0H16V11.625L8 16.025L0 11.625Z'))
        elif join=='miter': body=path('M.8 12.3L8 .5L15.2 12.3L12.6 13.7L8 6L3.4 13.7Z')
        else: body=path('M1 12L6.5 2.5H9.5L15 12L12.5 13.5L8 5.8L3.5 13.5Z')
        g('stroke-line-join-'+join,body)
    # Boolean operation symbols display the actual result inside the two
    # source outlines; this avoids arbitrary diagonal marks on identical boxes.
    a,b=rect(1.7,1.7,8.2,8.2),rect(6.1,6.1,8.2,8.2)
    for mode in ('exclude','intersect','subtract','unite'):
        if mode=='exclude': result=op(a,b,po.PathOp.XOR)
        elif mode=='intersect': result=inter(a,b)
        elif mode=='subtract': result=sub(a,b)
        else: result=union(a,b)
        name='squares-'+mode
        # One faded source plane is meaningful construction context. The
        # actual boolean result is opaque with a contour in Stroke.
        g(name,outline(a),outline(b))
        if mode == 'exclude':
            # Remove a uniform gutter around the intersection from both lobes.
            overlap = inter(a, b)
            result = sub(union(a, b), union(overlap, outline(overlap, 2.5)))
        if mode=='intersect':
            contextual = st('M1.7 6.3V2.8Q1.7 1.7 2.8 1.7H6.3M14.3 9.7V13.2Q14.3 14.3 13.2 14.3H9.7')
        elif mode=='subtract': contextual=st('M14.3 8.8V13.05Q14.3 14.3 13.05 14.3H8.8')
        else: contextual=empty
        primary=union(result,outline(result))
        secondary=sub(union(a,b),primary)
        tone_layers=([(secondary,.24)] if secondary.area>.001 else [])+[(primary,1)]
        if secondary.area>.001:
            api['DUOTONE_GLYPHS'][name]='Source construction planes recede behind the opaque Boolean result; layers are mutually clipped.'
        api.setdefault('STYLE_OVERRIDES',{})[name]={
            'duotone':tone_layers,
            'solid':union(primary, contextual) if mode in ('intersect','subtract') else primary,
            'stroke':union(contextual,outline(result))}
    # Layer sheets remain independent planes, with explicit occlusion.
    plane=poly([(8,2),(14.5,5.5),(8,9),(1.5,5.5)])
    planestroke=outline(plane)
    for count in (1,2):
        for direction in ('up','down'):
            name=('layers-' if count==2 else 'layer-')+'arrow-'+direction
            sheetpiece=outline(fit(plane,6.7,6.1,.8))
            if count==2: sheetpiece=union(sheetpiece,st('M1.6 8.9L6.7 11.7L9.3 10.3'))
            g(name,sheetpiece,arr(direction,12.5,10.3,.52))
    g('layers-2',planestroke,st('M1.5 9L8 12.5L14.5 9'))
    layer_back, layer_front = api['DRAWINGS']['layers'][:2]
    for action,mark in [('plus',plus(13.05,13.1,.75)), ('minus',line((11.55,13.1),(14.55,13.1)))]:
        clearance = rect(10.65,8.35,5.35,7.65,0)
        name = 'layers-' + action
        back, front = sub(layer_back, clearance), sub(layer_front, clearance)
        g(name, back, front, mark)
        api['DUOTONE_GLYPHS'][name] = api['DUOTONE_GLYPHS']['layers']
        api['STYLE_OVERRIDES'][name] = {
            'duotone': [(sub(back, union(front,mark)), .4), (union(front,mark), 1)],
            'stroke': union(sub(union(outline(layer_back), outline(layer_front)), clearance), mark),
        }
    rear,front=rect(2,2,8.5,8.5),rect(5.5,5.5,8.5,8.5)
    for name,foreground,background in [('bring-to-front',front,rear),('send-to-back',rear,front)]:
        g(name,sub(outline(background),union(foreground,outline(foreground,2.7))),foreground,outline(foreground))
    s('square-square',rr(),outline(rect(5.2,5.2,5.6,5.6)))
    g('square-stack',st('M1.5 10V2.5Q1.5 1.5 2.5 1.5H10M4 12V5Q4 4 5 4H12'),outline(rect(6.5,6.5,8,8)))
    for status,p in [('minus',line((7.5,9.5),(11.5,9.5))),('slash',line((7.65,11.35),(11.35,7.65)))]:
        g('copy-'+status,st('M2 11V3Q2 2 3 2H10'),outline(rect(5,5,9,9)),p)
    g('blend',sub(outline(circle(5.6,8,4.1)),circle(10.4,8,4.1)),outline(circle(10.4,8,4.1)),inter(circle(5.6,8,4.1),circle(10.4,8,4.1)))
    s('opacity',circle(),inter(circle(),rect(8,2,6,12,0)))
    # Keep the halftone plane within the circular body in all styles.
    opacity_primary=union(inter(circle(),rect(8,2,6,12,0)),outline(circle()))
    api.setdefault('STYLE_OVERRIDES',{})['opacity']={
        'duotone':[(sub(inter(circle(),rect(2,2,6,12,0)),opacity_primary),.24),(opacity_primary,1)],
        'solid':union(outline(circle()),inter(circle(),rect(8,2,6,12,0))),
        'stroke':union(outline(circle()),st('M8 2V14'),inter(circle(),st('M8.2 9.3L13.5 4M8.2 13.5L14 7.7')))}
    for horizontal in (True,False):
        name='square-centerline-dashed-'+('horizontal' if horizontal else 'vertical')
        divider=st('M8 1.6V4.3M8 6.8V9.2M8 11.7V14.4')
        s(name,rr(),transform(divider,90) if horizontal else divider)
        triangles=union(outline(poly([(2,3),(6,8),(2,13)])),outline(poly([(14,3),(10,8),(14,13)])),divider)
        g('triangles-centerline-dashed-'+('horizontal' if horizontal else 'vertical'),transform(triangles,90) if horizontal else triangles)
    for horizontal in (True,False):
        s('square-split-'+('horizontal' if horizontal else 'vertical'),rr(),line((2.55,8),(13.45,8)) if horizontal else line((8,2.55),(8,13.45)))
    s('square-round-corner',rr(),st('M5 11V8.4Q5 5 8.4 5H11'))
    s('square-dimensions',rect(2.1,2.1,8.8,8.8),st('M2.1 13.7H10.9M2.1 12.65V14.75M10.9 12.65V14.75M13.7 2.1V10.9M12.65 2.1H14.75M12.65 10.9H14.75'))
    s('square-text',rr(),st('M4.5 5H11.5M4.5 8H11.5M4.5 11H9'))
    s('square-menu',rr(),st('M4.5 5H11.5M4.5 8H11.5M4.5 11H11.5'))
    s('square-code',rr(),st('M6.7 5.65L4.35 8L6.7 10.35M9.3 5.65L11.65 8L9.3 10.35'))
    s('square-pen',rr(),union(outline(fit(pen,scale=.62)),placed_stroke('M10 3L13 6',scale=.62)))
    s('square-mouse-pointer',rr(),outline(fit(pointer2,scale=.62)))
    slash(outline(rr()),'square-off')
    for name,p in [('square-dashed-plus',plus()),('square-dashed-x',cross()),('square-dashed-search',union(outline(circle(10.1,10.2,2.5)),st('M11.9 12L14.4 14.5'))),('square-dashed-mouse-pointer',outline(fit(pointer2,10.7,10.4,.59)))]:
        g(name,sub(dash_square(),rect(7,7,9,9,0)) if name.endswith(('search','mouse-pointer')) else dash_square(),p)
    g('square-dashed-x-corner',sub(dash_square(),rect(8.7,8.7,7.3,7.3,0)),cross(12.4,12.4,.78))
    g('square-dashed-top-solid',sub(dash_square(),rect(0,0,16,5,0)),st('M2 4.15V3.25A1.25 1.25 0 0 1 3.25 2H12.75A1.25 1.25 0 0 1 14 3.25V4.15'))
    def scissors_mark(x, y, scale):
        r = 2.15 * scale
        left = x - 4 * scale
        handles = union(outline(circle(left,y-4*scale,r)), outline(circle(left,y+4*scale,r)))
        blades = placed_stroke('M5.5 5.5L14 13M5.5 10.5L14 3', x, y, scale)
        return union(handles, blades)

    s('square-scissors',rr(),scissors_mark(8,8,.66))
    g('scissors-line-dashed',scissors_mark(6.4,8,.77),st('M10.4 8H11.6M13.9 8H14.7'))
    g('square-bottom-dashed-scissors', st('M2 10.3V3.2Q2 2 3.2 2H12.8Q14 2 14 3.2V10.3'),
      st('M2.1 13.6H4.1M7 13.6H9M11.9 13.6H13.9'),
      outline(circle(5.1, 6, 1.22)), outline(circle(5.1, 10.1, 1.22)),
      st('M6.15 6.55L11.7 10.65M6.15 9.6L11.7 5.5'))

    cat('Maps and travel')
    world, meridians = api['DRAWINGS']['globe'][:2]
    globe = union(outline(world),meridians)
    # Earth shows land masses rather than longitude lines.
    ocean = circle()
    americas = path('M1 1H8C8 3 7.4 4.4 5.7 5.1Q4.8 5.7 5.6 6.7L7.7 8.1Q8.8 8.9 7.7 10.7L6.5 13.4Q5.3 12.1 5.4 10.4Q5.5 9.3 4.1 8.5Q2 7.4 1 6Z')
    old_world = path('M14 1H16V13H12.2Q11.2 12.2 11.1 10.7Q11 9.5 9.8 8.8Q8.3 7.8 9.3 6.5Q10.1 5.5 11.6 5.8L12.4 5Q11 4.4 11.7 3Z')
    land = inter(ocean, union(americas, old_world))
    s('earth', ocean, land)
    coast = union(outline(ocean), land)
    api['STYLE_OVERRIDES']['earth'] = {
        'duotone': [(sub(ocean, coast), .24), (coast, 1)],
        'solid': coast, 'stroke': union(outline(ocean), inter(ocean, outline(land)))}
    for state,p in [('check',check(12.3,12.4,.5)),('plus',plus(12.3,12.4,.6)),('x',cross(12.3,12.4,.57)),
                    ('ban',union(outline(circle(12.45,12.45,2.2)),line((10.9,10.9),(14,14)))),
                    ('code',st('M10.3 10.4L8.6 12.1L10.3 13.8M13.1 10.4L14.75 12.1L13.1 13.8'))]:
        cut=circle(12.45,12.45,3.9) if state!='code' else rect(7.1,9,8.9,7)
        g('globe-'+state,sub(globe,cut),p)
    slash(globe,'globe-off')
    mappoly=path('M1.8 3.5L6 1.8L10 3.5L14.2 1.8V12.5L10 14.2L6 12.5L1.8 14.2Z')
    for state,p in [('plus',plus(12.5,12,.65)),('minus',line((10.5,12),(14.5,12)))]:
        map_body, folds = api['DRAWINGS']['map'][:2]
        badged('map-'+state,map_body,folds,p,rect(9.2,9.85,6.8,6.15))
    pin=path('M8 14.5C6 12.5 2.5 8.5 2.5 5.8C2.5-.7 13.5-.7 13.5 5.8C13.5 8.5 10 12.5 8 14.5Z')
    for state,p in [('check',check(8,6,.6)),('minus',line((5.7,5.8),(10.3,5.8))),
                    ('plus',plus(8,5.8,.55)),('x',cross(8,5.8,.57))]:
        name='map-pin-'+state+'-inside'
        s(name,pin,p)
    for state,p in [('check',check(12.2,12,.5)),('minus',line((10.5,12),(14.2,12))),
                    ('house',st('M10 11.45L12.2 9.2L14.4 11.45V14.15H10Z')),
                    ('pen',pencil_mark(11.5,11.5)),
                    ('search',union(outline(circle(12,11.7,1.9)),line((13.5,13.2),(14.7,14.5))))]:
        region=circle(12.2,12,3.2)
        base_pin, eye = api['DRAWINGS']['map-pin'][:2]
        # Keep the original pin profile. The base's expansion scales its eye,
        # so reconstruct that circle on its measured centerline before stroking.
        x0,y0,x1,y1 = eye.bounds
        eye = outline(circle((x0+x1)/2, (y0+y1)/2, (x1-x0)/2 - api['STROKE']/2))
        # Fit the centerline of the supplied pin before adding its fixed-width outline.
        base_pin = fit(base_pin, scale=.993)
        badged('map-pin-'+state, base_pin, eye, p, union(region, outline(p,2.1)))
    pin_body = fit(pin, 8, 5.6, .58)
    pin_foreground = union(outline(pin_body), outline(circle(8,4.5,1.05)))
    pin_clearance = union(pin_body, outline(pin_body, 3.1))
    map_base = fit(mappoly,8,9.85,.77)
    map_edges = union(outline(map_base), placed_stroke('M6 1.8V12.5M10 3.5V14.2',8,9.85,.77))
    g('map-pinned', sub(map_edges,pin_clearance), pin_foreground)
    s('land-plot', poly([(1.6, 9), (6.5, 2.5), (14.4, 6.6), (9.5, 13.1)]), st('M4.05 5.75L11.95 9.85M10.45 4.55L5.55 11.05'))
    sign=poly([(2,4),(11,4),(14,7),(11,10),(2,10)])
    s('signpost-big',sign,union(line((8,1.5),(8,4)),line((8,10),(8,14.5)),line((5,7),(10,7))))
    s('milestone',poly([(2,4),(11,4),(14,7),(11,10),(2,10)]),union(line((6,10),(6,14.5)),arr('right',7.7,7,.46)))
    route_line, route_stops = api['DRAWINGS']['route'][:2]
    cancelled('route-off',union(route_line,route_stops),(1.6,5.65),(10.65,14.7))
    g('route-arrow-right',outline(circle(3,3,1.6)),st('M5 3H11Q14 3 14 6Q14 8 11 8H5Q2 8 2 11Q2 13 5 13H13'),line((10,10),(13,13),(10,15.5)))
    slash(st('M8 3A5 5 0 1 0 8 13A5 5 0 1 0 8 3M8 1.3V4M8 12V14.7M1.3 8H4M12 8H14.7'),'locate-off')
    g('radar', outline(circle()), outline(circle(8, 8, 3)), line((8, 8), (12.24, 3.76)), circle(4.1, 10.3, .65))
    for name,p in [('navigation-2',poly([(8,1.7),(14,14),(8,11),(2,14)])),
                   ('mouse-pointer-2',pointer2)]:
        s(name,p)
        if name == 'mouse-pointer-2':
            cancelled(name + '-off', outline(api['DRAWINGS'][name][0]), (2.4, 12.4), (13.6, 3.2))
        else:
            slash(base_ink(name), name + '-off')
    navigation, heading = api['DRAWINGS']['navigation'][:2]
    cancelled('navigation-off', union(outline(navigation), heading), (2, 3), (13.5, 14.5))
    hand = path('M5.1 13.8L2.1 9.6C.8 7.7 2.7 6.5 3.9 7.8L5.1 9.1V3.15C5.1 1.35 7.8 1.35 7.8 3.15L8 6.6C8.1 4.8 10.6 4.9 10.8 6.7C11.6 5.5 13.4 6.1 13.65 7.45L14 9.9Q14.4 14.2 10.8 14.2H6.4Q5.55 14.2 5.1 13.8Z')
    s('pointer',hand,st('M8 6.6V8.7M10.8 6.7V8.6'))
    slash(base_ink('pointer'),'pointer-off')
    grab = path('M2.1 8Q1.8 6.2 3.5 6.2L3.4 5Q3.4 3.3 5.2 3.5Q5.7 1.6 7.5 2.3Q8.4 2.6 8.6 3.5Q9.2 2.4 10.5 2.9Q11.6 3.2 11.8 4.6Q13.9 4 14 6.2V9.8Q14 13.8 10 14H7Q4.6 14 3.4 11.7Z')
    s('hand-grab', grab, st('M3.5 6.2L6.2 6.8Q8.8 7.4 7.6 9Q6.9 10 5.7 9.4M5.2 3.5L5.7 5M8.6 3.5L9 5.6M11.8 4.6L12 6.2'))
    ban=union(outline(circle(12.2,12.2,2.4)),line((10.5,10.5),(13.9,13.9)))
    s('mouse-pointer-ban',sub(pointer2,circle(12.2,12.2,3.2)),ban)
    wheel = outline(circle(8, 5.9, 4.4))
    cabins = union(*(outline(rect(x - 1.4, 7.4, 2.8, 2.8)) for x in (2.7, 13.3)))
    spokes = st('M8 1.5V5.9M3.6 5.9H12.4')
    hangers = st('M3.6 5.9H2.7V7.4M12.4 5.9H13.3V7.4')
    supports = st('M4.7 14.4L8 5.9L11.3 14.4M3.5 14.4H12.5')
    g('ferris-wheel', wheel, cabins, spokes, hangers, supports)
    g('roller-coaster',st('M1.6 9.7C3.7 9.7 3.8 2.2 7.1 2.2C10.5 2.2 9.8 10.8 12.5 10.8Q13.8 10.8 14.65 9'),st('M1.6 12C5.3 12 5.6 4.6 7.1 4.6C8.6 4.6 8.1 13.1 12.5 13.1Q13.7 13.1 14.65 12.3M3.9 10.9V14.3M7.1 4.6V14.3M12.5 13.1V14.3'))

    cat('Transform and flow')
    for vertical in (False,True):
        pieces=union(outline(rect(1.2,1.8,4,3.5)),outline(rect(10.8,1.8,4,3.5)),outline(rect(6,10.8,4,3.5)),st('M3.2 5.3V7.5H12.8V5.3M8 7.5V10.8'))
        g('diagram-flow-'+('vertical' if vertical else 'horizontal'),pieces if vertical else transform(pieces,90))
    for name in ('move-3d','scale-3d','rotate-3d'):
        axes=st('M8 8V2M8 8L2.2 11.7M8 8L13.8 11.7')
        if name=='move-3d': details=st('M6.1 3.9L8 2L9.9 3.9M2.7 9.1L2.2 11.7L4.85 12.3M13.3 9.1L13.8 11.7L11.15 12.3')
        elif name=='scale-3d': details=union(rect(6.7,1.05,2.6,2.6),rect(.9,10.4,2.6,2.6),rect(12.5,10.4,2.6,2.6))
        else:
            axes = union(outline(circle(7.6,8,1.35)), st('M7.6 4.65V6.65M6.43 8.68L4.7 9.7M8.77 8.68L10.5 9.7'))
            details = st('M12.9 4.4C9.4 1.4 2 2.8 1.8 7.8C1.6 13.7 11 15.1 14 9.3M11.8 9.7L14 9.3L14.5 11.6')
        g(name,axes,details)
    for cw in (False,True):
        p=union(outline(rect(4.2,6.5,7.2,7.2)),st('M2 8V6Q2 2.3 5.8 2.3H13M10.5 .7L13 2.3L10.5 4'))
        g('rotate-'+('cw' if cw else 'ccw')+'-square',p if cw else mirror(p))
    s('rotate-cw-clock',circle(7.8,9.9,4.45),union(st('M7.8 7.45V9.9L9.65 11'),st('M2.7 4.35Q7.5 -.35 13.25 4.35M10.7 4.35H13.25V1.8')))
    g('scaling',outline(rect(2,8,6,6)),st('M2 5V2H5M8.5 2H14V7.5M8 8L14 2'))
    g('scan-box',st('M1.5 5V1.5H5M11 1.5H14.5V5M1.5 11V14.5H5M11 14.5H14.5V11'),small_box(8,8,.59))
    g('view',st('M1.5 5V1.5H5M11 1.5H14.5V5M1.5 11V14.5H5M11 14.5H14.5V11'),st('M3.2 8Q8 1.8 12.8 8Q8 14.2 3.2 8Z'),circle(8,8,1.25))
    funnel, funnel_seam = api['DRAWINGS']['filter'][:2]
    for state,p in [('plus',plus(12.9,12.4,.83)),('x',cross(12.9,12.4,.75))]:
        badged('funnel-'+state, funnel, funnel_seam, p, union(p,outline(p,2.1)))
    s('search-exclamation-point',circle(6.7,6.7,4.6),union(line((10.3,10.3),(14,14)),line((6.7,3.8),(6.7,6.8)),circle(6.7,8.8,.6)))
    s('search-slash',circle(6.7,6.7,4.6),union(line((10.3,10.3),(14,14)),line((4.7,8.7),(8.7,4.7))))
    g('loader-pinwheel',*(transform(st('M9.2 2.1Q13.9 3.5 13.4 7.4L9 6.5Z'),a) for a in (0,90,180,270)))
    # Fading in the name denotes incomplete progress, expressed as a broken
    # circumference; no arbitrary opacity is applied to a continuous stroke.
    arc = st('M4.5 3.2A5.9 5.9 0 0 0 2.15 7M2.55 10.25A5.9 5.9 0 0 0 5.8 13.45')
    g('circle-fading-arrow-up', arc, mirror(arc), arr('up',8,7.1,.76))
    s('cloud-backup',path('M4.6 12.9C.6 12.9 .5 6.6 4.2 6.4C4.5 .5 12.1 .5 12.4 6Q14.6 6.5 14.6 9.3Q14.6 12.9 11.6 12.9Z'),
      union(outline(circle(8,8.5,2.7)),st('M8 7.2V8.5L9 9.1')))
    keyboard_body, keys = api['DRAWINGS']['keyboard'][:2]
    slash(union(outline(fit(keyboard_body,scale=.997)),keys),'keyboard-off')
    g('import',st('M9 2H13Q14 2 14 3V13Q14 14 13 14H9'),arr('right',5.8,8,.8))

    missing=set(NAMES)-made
    extra=made-set(NAMES)
    assert not missing, 'Unimplemented design names: '+', '.join(sorted(missing))
    assert not extra, 'Unassigned design names: '+', '.join(sorted(extra))
