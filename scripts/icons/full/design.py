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

    def st(d, w=1.35):
        return stroke(d, w)

    def sub(a, b):
        return op(a, b, po.PathOp.DIFFERENCE)

    def inter(a, b):
        return op(a, b, po.PathOp.INTERSECTION)

    def rect(x, y, w, h, r=.5):
        return rr(x, y, w, h, r)

    def outline(b, w=1.25):
        return stroke(b, w)

    def transpose(p):
        return p.transform(0,1,1,0,0,0)

    def fit(p, x=8, y=8, scale=1):
        return transform(p, scale=scale, dx=x-8, dy=y-8)

    def arr(direction='right', x=8, y=8, scale=1):
        angle = {'right': 0, 'down':90, 'left':180, 'up':270,
                 'up-right':-45, 'down-right':45, 'down-left':135, 'up-left':225}[direction]
        return transform(union(line((3.2,8),(12.8,8)),
                               line((9.4,4.6),(12.8,8),(9.4,11.4))),
                         angle, scale, x-8, y-8)

    def chev(direction='right', x=8, y=8, scale=1, double=False):
        angle={'right':0,'down':90,'left':180,'up':270}[direction]
        p = (union(line((3.5,4.5),(7,8),(3.5,11.5)),
                   line((8.5,4.5),(12,8),(8.5,11.5))) if double else
             line((5.7,4),(9.7,8),(5.7,12)))
        return transform(p, angle, scale, x-8,y-8)

    def slash(p, name):
        diagonal=line((2,2),(14,14))
        # Clear a hairline either side of the cancellation stroke, preserving
        # the contour behind it without a dense black intersection.
        g(name, sub(p, line((2,2),(14,14),width=2.7)), diagonal)

    def dashed(points, closed=False, dash=1.65, gap=1.4, width=1.2):
        ps=[]
        vertices=points+[points[0]] if closed else points
        for a,b in zip(vertices,vertices[1:]):
            dx,dy=b[0]-a[0],b[1]-a[1]
            length=math.hypot(dx,dy)
            n=max(1,round(length/(dash+gap)))
            for i in range(n):
                begin=i/n; end=min(1,begin+dash/length)
                ps.append(line((a[0]+dx*begin,a[1]+dy*begin),
                               (a[0]+dx*end,a[1]+dy*end),width=width))
        return union(*ps)

    def dash_circle(x=8,y=8,r=6):
        ps=[]
        for i in range(10):
            a=2*math.pi*i/10; b=a+.34
            mid=(a+b)/2
            ps.append(st(f'M{x+r*math.cos(a)} {y+r*math.sin(a)}Q{x+r*math.cos(mid)*1.015} {y+r*math.sin(mid)*1.015} {x+r*math.cos(b)} {y+r*math.sin(b)}',1.2))
        return union(*ps)

    def dash_square(x=2,y=2,w=12,h=12):
        return dashed([(x,y),(x+w,y),(x+w,y+h),(x,y+h)],True)

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
        'k':'M4 3V13M12 3L4 9M7.5 6.5L12.5 13',
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

    def letter(ch, x=8, y=8, scale=1, width=1.35):
        return fit(st(letters[ch],max(width,.85/scale)),x,y,scale)

    def number(ch,x=8,y=8,scale=1):
        return fit(st(digits[ch],max(1.35,.85/scale)),x,y,scale)

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
                s(name,circle() if container=='circle' else rr(),letter(ch,scale=.62),tags='alphabet character '+ch)
    for container in ('circle','square'):
        name=container+'-letter-p-off'
        boundary=outline(circle() if container=='circle' else rr())
        slash(union(boundary,letter('p',scale=.62)),name)
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
        if name in NAMES: s(name,rr(),arr(direction,scale=.63))
        for behavior in ('enter','exit'):
            name=f'square-arrow-{direction}-{behavior}'
            if name not in NAMES: continue
            # Open aperture at the relevant edge, with the arrow visibly
            # crossing it. Enter points into the frame; exit crosses outward.
            opening=transform(rect(10 if behavior=='exit' else -1,5,7,6),angle)
            frame=sub(outline(rr(2.5,2.5,11,11,1.5)),opening)
            a=arr('right',x=11 if behavior=='exit' else 5,y=8,scale=.65)
            g(name,frame,transform(a,angle))
        name=f'circle-arrow-{direction}-exit'
        if name in NAMES:
            frame=sub(ring(),transform(rect(9,4,8,8),angle))
            g(name,frame,transform(arr('right',11,8,.62),angle))
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
            arrowpart=arr(direction,3.2,8,.8)
            if order in ('0-1','1-0'):
                a,b=order.split('-')
                detail=union(number(a,11,4,.38),number(b,11,12,.38))
            elif order in ('a-z','z-a'):
                a,b=order.split('-')
                detail=union(letter(a,11,4,.38),letter(b,11,12,.38))
            else:
                widths=[2.5,4.5,6.5] if order=='narrow-wide' else [6.5,4.5,2.5]
                detail=union(*(line((8,3.5+i*4.5),(8+w,3.5+i*4.5),width=1.25) for i,w in enumerate(widths)))
            g(name,arrowpart,detail)
    for direction in ('left','right','up','down'):
        angle=directions[direction]
        for mode in ('from-line','to-line'):
            name=f'arrow-{direction}-{mode}'
            if name in NAMES:
                base=union(line((2,3),(2,13)),arr('right',9,8,.85))
                if mode=='to-line': base=union(line((14,3),(14,13)),arr('right',7,8,.85))
                g(name,transform(base,angle))
    g('arrow-down-to-dot',arr('down',8,6,.75),circle(8,13.8,.9))
    g('arrow-up-from-dot',arr('up',8,6,.75),circle(8,13.8,.9))
    g('arrows-up-from-line',arr('up',4.3,6.8,.57),arr('up',11.7,6.8,.57),line((2,14),(14,14)))
    g('arrow-down-up',arr('down',4.5,8,.8),arr('up',11.5,8,.8))
    g('arrow-right-left',arr('right',8,4.5,.8),arr('left',8,11.5,.8))
    for horizontal in (True,False):
        p=union(line((2,8),(14,8)),line((5,5),(2,8),(5,11)),line((11,5),(14,8),(11,11)))
        g('move-'+('horizontal' if horizontal else 'vertical'),p if horizontal else transform(p,90))
    for name,angle in [('move-diagonal',-45),('move-diagonal-2',45)]:
        g(name,transform(p,angle,.95))
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
        else: g('refresh-ccw-dot',base,circle(12.8,13.2,.85))
        # Iteration uses a return loop rather than a circular refresh arrow.
        loop=union(st('M3 4H11Q14 4 14 7V10Q14 13 11 13H4'),line((6,10),(3,13),(6,15)))
        g('iteration-'+suffix,loop if clockwise else mirror(loop))
    repeat=union(st('M2.5 9V5Q2.5 3 4.5 3H13M13.5 7V11Q13.5 13 11.5 13H3'),st('M10 1L13 3L10 5M6 11L3 13L6 15'))
    g('repeat-2',repeat)
    slash(repeat,'repeat-off')
    for inward in (True,False):
        ps=[dashed([(8,1.5),(8,14.5)],width=1),arr('right' if inward else 'left',3.7,8,.48),arr('left' if inward else 'right',12.3,8,.48)]
        g('fold-horizontal' if inward else 'unfold-horizontal',*ps)

    cat('Layout')
    # Alignment bars are objects; guide rules remain visually distinct.
    for horizontal in (True,False):
        orient='horizontal' if horizontal else 'vertical'
        for position in ('start','center','end'):
            name=f'align-{position}-{orient}'
            offset={'start':3,'center':8,'end':13}[position]
            spans=[(3,4),(9,7)]
            ps=[]
            for x,length in spans:
                y=offset if position=='start' else offset-length if position=='end' else offset-length/2
                ps.append(rect(x,y,3,length,.65))
            rule=line((1.5,offset),(14.5,offset),width=1.1)
            p=union(*ps)
            if not horizontal: p,rule=transpose(p),transpose(rule)
            s(name,p,rule)
        for operation in ('distribute','justify'):
            for position in ('start','center','end'):
                name=f'align-{orient}-{operation}-{position}'
                y={'start':3,'center':8,'end':13}[position]
                blocks=[]
                if operation=='distribute':
                    targets={'start':[2,7,12], 'center':[3,8,13], 'end':[4,9,14]}[position]
                    for target,width,height in zip(targets,[2.2,3.5,2.8],[7,10,8]):
                        left=target if position=='start' else target-width if position=='end' else target-width/2
                        blocks.append(rect(left,8-height/2,width,height,.45))
                    rules=union(*(line((target,1.5),(target,14.5),width=.85) for target in targets))
                else:
                    for x,length in [(3,3),(9,5)]:
                        top=y if position=='start' else y-length if position=='end' else y-length/2
                        blocks.append(rect(x,top,3,length,.5))
                    rules=line((1.5,y),(14.5,y),width=1.1)
                body=union(*blocks)
                if (operation=='distribute' and not horizontal) or (operation=='justify' and horizontal):
                    body,rules=transpose(body),transpose(rules)
                s(name,body,rules)
        for behavior in ('around','between'):
            name=f'align-{orient}-space-{behavior}'
            if behavior=='around':
                objects=union(rect(4,3,2.7,10,.5),rect(9.3,5,2.7,6,.5))
                rules=union(line((1.5,2),(1.5,14),width=1),line((8,2),(8,14),width=1),line((14.5,2),(14.5,14),width=1))
            else:
                objects=union(rect(1.5,3,3,10,.5),rect(11.5,5,3,6,.5))
                rules=union(line((6.5,2),(6.5,14),width=1),line((9.5,2),(9.5,14),width=1))
            if not horizontal: objects,rules=transpose(objects),transpose(rules)
            s(name,objects,rules)
    for horizontal in (True,False):
        for end in (False,True):
            name='between-'+('horizontal' if horizontal else 'vertical')+'-'+('end' if end else 'start')
            body=union(rect(1.8,2.5,4,11,.7),rect(10.2,2.5,4,11,.7))
            detail=union(line((8,2),(8,6.2)),line((6.2,4.4),(8,6.2),(9.8,4.4)))
            if end: detail=transform(detail,180)
            if horizontal: body,detail=transpose(body),transpose(detail)
            s(name,body,detail)

    def cells(cols,rows,x=2,y=2,w=12,h=12,gap=2):
        cw=(w-gap*(cols-1))/cols; ch=(h-gap*(rows-1))/rows
        return union(*(rect(x+i*(cw+gap),y+j*(ch+gap),cw,ch,.55) for j in range(rows) for i in range(cols)))

    for cols,rows in [(2,2),(3,2),(3,3)]:
        s(f'grid-{cols}x{rows}',cells(cols,rows))
    slash(outline(cells(3,3)),'grid-3x3-off')
    for status,detail in [('check',check(12.1,12.3,.5)),('plus',plus(12.1,12.3,.6)),('x',cross(12.1,12.3,.6))]:
        body=union(rect(2,2,4.8,4.8),rect(9.2,2,4.8,4.8),rect(2,9.2,4.8,4.8))
        s('grid-2x2-'+status,body,detail)
    for count in (3,4):
        s('columns-'+str(count),cells(count,1,gap=1.8))
        s('rows-'+str(count),cells(1,count,gap=1.8))
    cog=union(ring(11.7,12.2,2.1,.95),*(line((11.7+2.1*math.cos(a),12.2+2.1*math.sin(a)),(11.7+3*math.cos(a),12.2+3*math.sin(a)),width=1) for a in [i*math.pi/3 for i in range(6)]))
    s('columns-3-cog',sub(cells(3,1,gap=1.8),circle(11.7,12.2,3.7)),cog)
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
            divider=line((10,2),(10,14),width=1.1)
            arrowpart=arr('right' if action=='close' else 'left',6.1,8,.52)
            s(name+'-'+action,rr(),transform(union(divider,arrowpart),orientation))
    for side,angle in [('left',180),('right',0),('top',270),('bottom',90)]:
        outer=outline(rr())
        guide=dashed([(10,2.3),(10,13.7)],width=1.1)
        g('panel-'+side+'-dashed',outer,transform(guide,angle))
    for name,angle in [('panel-left-right-dashed',0),('panel-top-bottom-dashed',90)]:
        g(name,outline(rr()),transform(union(dashed([(5.5,2),(5.5,14)],width=1),dashed([(10.5,2),(10.5,14)],width=1)),angle))
    for name,angle in [('panels-left-bottom',0),('panels-right-bottom',180),('panels-top-left',90)]:
        divider=st('M6 2V14M6 10H14',1.2)
        s(name,rr(),mirror(divider) if name=='panels-right-bottom' else transform(divider,angle))
    s('app-window-mac',rr(1.5,2.5,13,11,1.7),union(line((1.5,6),(14.5,6),width=1.1),dots((4,4.3),(6.3,4.3),(8.6,4.3),r=.45)))
    s('dock',rr(1.5,2,13,12,1.6),union(outline(rect(3.5,9,9,3.2,1),1),dots((5.5,10.6),(8,10.6),(10.5,10.6),r=.45)))
    for vertical in (False,True):
        for end in (False,True):
            body=rect(4.5 if not end else 1.5,2,8,12,1.3)
            if end: extras=union(line((11.5,2),(11.5,14),width=1.1),line((14.5,2),(14.5,14),width=1.1))
            else: extras=union(line((1.5,2),(1.5,14),width=1.1),line((14.5,2),(14.5,14),width=1.1))
            if vertical: body,extras=transform(body,90),transform(extras,90)
            s('gallery-'+('vertical' if vertical else 'horizontal')+('-end' if end else ''),body,extras)
    s('gallery-thumbnails',union(rect(1.8,1.8,12.4,8,1),rect(1.8,12,3,2.5,.4),rect(6.5,12,3,2.5,.4),rect(11.2,12,3,2.5,.4)))
    for horizontal in (True,False):
        p=union(line((4,2),(4,14),width=1.2),line((12,2),(12,14),width=1.2),arr('right',6,8,.32),arr('left',10,8,.32))
        g('gap-'+('horizontal' if horizontal else 'vertical'),p if horizontal else transform(p,90))
        p=union(outline(rect(2,4,12,8,1)),arr('left',5.2,8,.38),arr('right',10.8,8,.38))
        g('stretch-'+('horizontal' if horizontal else 'vertical'),p if horizontal else transform(p,90))
    g('handle-bottom-right',line((8,14),(14,8)),line((12,14),(14,12)))
    s('ratio',rr(1.8,3,12.4,10,1.3),union(circle(5,6,.85),circle(11,10,.85),line((6,10),(10,6),width=1.15)))
    s('proportions',rr(1.8,3,12.4,10,1.3),outline(rect(5,5,9.2,8,1),1.1))
    for vertical in (False,True):
        s('rectangle-'+('vertical' if vertical else 'horizontal'),rect(4 if vertical else 1.8,1.8 if vertical else 4,8 if vertical else 12.4,12.4 if vertical else 8,1.5))
    s('rectangle-ellipsis',rr(1.8,4,12.4,8,1.5),dots((4.5,8),(8,8),(11.5,8),r=.65))
    for name in ('margin','margin-top','margin-bottom','margin-left','margin-right','margin-horizontal','margin-vertical',
                 'square-padding','square-padding-top','square-padding-bottom','square-padding-left','square-padding-right','square-padding-horizontal','square-padding-vertical'):
        padding=name.startswith('square-padding')
        side=name.removeprefix('square-padding').removeprefix('margin').lstrip('-')
        selected=('top','bottom','left','right') if not side else ('left','right') if side=='horizontal' else ('top','bottom') if side=='vertical' else (side,)
        body=rr(2,2,12,12,1.2)
        rules=[]
        for edge in selected:
            if edge=='top': rules.append(line((2.5,5),(13.5,5),width=1.05))
            elif edge=='bottom': rules.append(line((2.5,11),(13.5,11),width=1.05))
            elif edge=='left': rules.append(line((5,2.5),(5,13.5),width=1.05))
            else: rules.append(line((11,2.5),(11,13.5),width=1.05))
        if padding:
            # Dots identify padding inside the content boundary, distinguishing
            # these controls from margins around a page.
            points={'top':(8,3.5),'bottom':(8,12.5),'left':(3.5,8),'right':(12.5,8)}
            rules.extend(circle(*points[e],.5) for e in selected)
        else:
            rules.append(outline(rect(6.5,6.5,3,3,.3),.9))
        s(name,body,union(*rules))

    cat('Geometry')
    for name,n,rotation in [('triangle',3,-90),('pentagon',5,-90),('hexagon',6,-90),('octagon',8,-22.5),('diamond',4,-90)]:
        r=6.2
        points=[(8+r*math.cos(math.radians(rotation)+2*math.pi*i/n),8+r*math.sin(math.radians(rotation)+2*math.pi*i/n)) for i in range(n)]
        s(name,poly(points))
    s('triangle-right',poly([(3,2),(3,14),(14,14)]))
    s('octagon-pause',poly([(5,1.7),(11,1.7),(14.3,5),(14.3,11),(11,14.3),(5,14.3),(1.7,11),(1.7,5)]),union(line((6,5),(6,11),width=1.8),line((10,5),(10,11),width=1.8)))
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
    g('squircle-dashed',union(*(transform(st('M3 1.9Q1.9 1.9 1.9 3',1.2),a) for a in (0,90,180,270))),union(*(transform(line((6.2,1.7),(9.8,1.7),width=1.2),a) for a in (0,90,180,270))))
    g('triangle-dashed',dashed([(8,2),(14,14),(2,14)],True,dash=1.7,gap=1.5))
    astroid=path('M8 1.7Q8 8 14.3 8Q8 8 8 14.3Q8 8 1.7 8Q8 8 8 1.7Z')
    s('astroid',astroid)
    s('sparkle',poly([(8,1.6),(9.8,6.2),(14.4,8),(9.8,9.8),(8,14.4),(6.2,9.8),(1.6,8),(6.2,6.2)]))
    g('asterism',union(*(fit(union(line((8,5.5),(8,10.5),width=1.1),line((5.8,6.7),(10.2,9.3),width=1.1),line((5.8,9.3),(10.2,6.7),width=1.1)),x,y,.7) for x,y in [(8,4.2),(4.3,11.3),(11.7,11.3)])))
    s('club',union(circle(8,4.5,2.6),circle(4.7,8.5,2.8),circle(11.3,8.5,2.8),poly([(8,8),(5.2,14),(10.8,14)])))
    s('spade',union(path('M8 1.6L2.8 6.8C-1 11 5 14 8 10C11 14 17 11 13.2 6.8Z'),poly([(8,9),(5.3,14.3),(10.7,14.3)])))
    s('cross',poly([(6,2),(10,2),(10,6),(14,6),(14,10),(10,10),(10,14),(6,14),(6,10),(2,10),(2,6),(6,6)]))
    s('circle-dot',circle(),circle(8,8,1.5))
    slash(outline(circle()),'circle-off')
    s('circle-pile',union(circle(8,4.3,2.6),circle(4.5,10.8,2.6),circle(11.5,10.8,2.6)))
    g('angle',line((3,3),(3,13),(14,13)),st('M3 8Q8 8 8 13',1.1))
    g('diameter',outline(circle()),line((3.6,12.4),(12.4,3.6)),dots((3.6,12.4),(12.4,3.6),r=.85))
    g('radius',outline(circle()),line((8,8),(12.2,3.8)),circle(8,8,.9))
    g('tangent',outline(circle(8,9.5,4.2)),line((1.5,5.3),(14.5,5.3)),circle(8,5.3,.9))
    g('axis-3d',line((8,8),(8,1.7)),line((8,8),(14,12.8)),line((8,8),(2,12.8)),st('M6 3.7L8 1.7L10 3.7M11.4 12.6L14 12.8L13.5 10.2M2.5 10.2L2 12.8L4.6 12.6',1.1))
    box=path('M8 1.8L14 5V11L8 14.2L2 11V5Z')
    seams=st('M2 5L8 8.5L14 5M8 8.5V14.2',1.15)
    s('box',box,seams)
    # Three boxes rather than a badged single box.
    miniature=union(outline(box,1.2),seams)
    g('boxes',fit(miniature,8,4.5,.43),fit(miniature,4.2,10.8,.43),fit(miniature,11.8,10.8,.43))
    s('cuboid',path('M6 1.8L14 4.8V11.3L10 14.2L2 11.2V4.7Z'),st('M2 4.7L10 7.8L14 4.8M10 7.8V14.2M6 1.8V5.9',1.15))
    s('cone',path('M8 1.6L14 12Q14 14.5 8 14.5Q2 14.5 2 12Z'),st('M2 12Q8 9 14 12',1.1))
    s('pyramid',poly([(8,1.7),(14,12.5),(7,14.2),(2,11.5)]),st('M8 1.7L7 14.2M8 1.7L2 11.5',1.1))
    s('cylinder',path('M2.5 4Q2.5 1.5 8 1.5Q13.5 1.5 13.5 4V12Q13.5 14.5 8 14.5Q2.5 14.5 2.5 12Z'),st('M2.5 4Q2.5 6.5 8 6.5Q13.5 6.5 13.5 4',1.15))
    torus=path('M1.5 8C1.5 1 14.5 1 14.5 8C14.5 15 1.5 15 1.5 8ZM5.6 7.4C5.6 9.4 10.4 9.4 10.4 7.4C10.4 5.4 5.6 5.4 5.6 7.4Z')
    # Boolean hole has explicit winding-independent construction.
    torus=sub(ellipse,fit(ellipse,8,7.3,.38))
    s('torus',torus,st('M2.5 10Q8 14 13.5 10',1.05))
    g('shapes',outline(circle(4.6,4.8,2.6)),outline(rect(8.7,8.3,5.6,5.6,.7)),outline(poly([(11,1.6),(14.5,6.4),(7.5,6.4)]),1.1))
    g('component',*(outline(transform(rect(6,1.5,4,4,.5),a),1.1) for a in (0,90,180,270)))
    g('vector-square',st('M4.5 2.5H11.5M13.5 4.5V11.5M11.5 13.5H4.5M2.5 11.5V4.5',1.1),*(outline(rect(x,y,3,3,.35),1.1) for x,y in [(1,1),(12,1),(1,12),(12,12)]))
    g('vector-polygon',st('M3 11L6 3L13 6L11 13Z',1.15),*(rect(x-1,y-1,2,2,.35) for x,y in [(3,11),(6,3),(13,6),(11,13)]))

    cat('Math and symbols')
    divide=union(line((3,8),(13,8)),dots((8,3.5),(8,12.5),r=.9))
    equals=union(line((3,5.5),(13,5.5)),line((3,10.5),(13,10.5)))
    approximately=union(st('M2.5 5.5C5 1.5 11 9.5 13.5 5.5'),st('M2.5 10.5C5 6.5 11 14.5 13.5 10.5'))
    pi=st('M2 4H14M5 4V10Q5 13 3.5 13M11 4V11.5Q11 13 13 13')
    sigma=st('M12.5 2.5H3.5L8 8L3.5 13.5H12.5')
    pilcrow=union(st('M12.5 2.5H7Q2 2.5 2 6Q2 9.5 7 9.5H8M8 2.5V13.5M11.5 2.5V13.5'),rect(4.2,3.3,3.6,5.4,.8))
    asterisk=union(line((8,3),(8,13)),line((3.7,5.5),(12.3,10.5)),line((3.7,10.5),(12.3,5.5)))
    for name,p in [('divide',divide),('equal-not',union(equals,line((4,14),(12,2)))),
                   ('equal-approximately',union(st('M2.5 5C5 1 11 9 13.5 5'),line((3,11),(13,11)))),
                   ('equal-approximately-not',union(approximately,line((4,14),(12,2)))),
                   ('sigma',sigma),('pilcrow',pilcrow),('lambda',st('M3 2Q5 1 6.5 5L11 13Q12 15 14 13M7.5 7L3 14')),
                   ('omega',st('M3 13H6V10.5C-.5 7 3 1.5 8 1.5C13 1.5 16.5 7 10 10.5V13H13')),
                   ('phi',union(outline(circle(8,8,4.5)),line((8,1.7),(8,14.3)))),
                   ('exclamation-mark',union(line((8,2),(8,9.5),width=1.7),circle(8,13,.9))),
                   ('question-mark',union(st('M4.5 5Q4.5 1.5 8.5 1.5Q12.5 1.5 12.5 5Q12.5 7 9.5 8Q8 8.5 8 10'),circle(8,13.5,.8))),
                   ('weight-tilde',st('M2 8C5-1 11 17 14 8',1.6))]:
        g(name,p)
    for name,p in [('circle-divide',divide),('circle-equal',equals),('square-divide',divide),('square-equal',equals),
                   ('square-pi',pi),('square-sigma',sigma),('square-pilcrow',pilcrow),('square-asterisk',asterisk),
                   ('square-function',st('M11 3Q7 1 7 5V11Q7 15 3 13M4.5 7H11.5'))]:
        s(name,circle() if name.startswith('circle') else rr(),fit(p,scale=.6))
    for i in range(1,6):
        ps=[line((3.5+j*3,3),(3.5+j*3,13),width=1.25) for j in range(min(4,i))]
        if i==5: ps.append(line((2,11.5),(14,4.5),width=1.3))
        if i<4: ps=[fit(p,8+(4-i)*1.5,8) for p in ps]
        g('tally-'+str(i),*ps)
    amp=st('M12.8 13L5.3 5.8Q2.8 2.2 6.7 1.8Q10.5 1.6 9 4.5L4 8C.5 10.5 4 15.2 8 13.4Q12 11.7 13 8')
    g('ampersand',amp)
    g('ampersands',fit(amp,4.2,8,.51),fit(amp,11.8,8,.51))
    g('section',st('M11.5 3Q4-.5 4 5C4 8.5 12 6.5 12 10Q12 15.5 4.5 13M11.5 6Q5 2 4 7Q3 10 10 11',1.25))
    g('copyright' if 'copyright' in NAMES else 'copyleft',outline(circle()),mirror(letter('c',scale=.58)))
    s('creative-commons',circle(),union(letter('c',5.3,8,.3),letter('c',10.7,8,.3)))

    cat('Typography and text')
    lower_a=st('M11.5 6V13M11.5 8Q7 3 4 7Q1 12 6 13Q9 14 11.5 10',1.35)
    lower_b=st('M4 2V13M4 8Q8 3 11 7Q14 12 9 13Q6 14 4 10',1.35)
    for name,p in [('case-upper',union(letter('a',4.2,8,.52),letter('b',11.7,8,.52))),
                   ('case-lower',union(fit(lower_a,4.3,8,.54),fit(lower_b,11.5,8,.54))),
                   ('case-sensitive',union(letter('a',4.3,7.8,.54),fit(lower_a,11.7,9.2,.48))),
                   ('a-large-small',union(letter('a',4.5,7.5,.62),letter('a',12,10.2,.4)))]:
        g(name,p)
    for direction in ('up','down'):
        g('a-arrow-'+direction,letter('a',5.5,8,.7),arr(direction,12.5,8,.53))
    g('baseline',letter('a',8,6.3,.7),line((2,14),(14,14)))
    g('letter-spacing',letter('a',4.2,6,.48),letter('a',11.8,6,.48),line((2,13.5),(14,13.5)),st('M4 11.5L2 13.5L4 15.5M12 11.5L14 13.5L12 15.5',1.1))
    g('line-height',st('M8 3H14M8 8H12M8 13H14'),line((3,2),(3,14)),st('M1 4L3 2L5 4M1 12L3 14L5 12',1.1))
    g('ligature',st('M4 13V5Q4 2 7 2Q10 2 10 5V13M2 6H13M8 13H12'))
    for i in (5,6):
        g('heading-'+str(i),letter('h',5.2,8,.68),number(str(i),12.3,10.2,.36))
    g('type-outline',outline(poly([(8,2),(14,14),(11.3,14),(9.8,10.8),(6.2,10.8),(4.7,14),(2,14)]),1.1),outline(poly([(8,5.5),(6.8,8.7),(9.2,8.7)]),.8))
    for subscript in (True,False):
        g('subscript' if subscript else 'superscript',letter('x',5.4,8,.68),number('2',12.3,12 if subscript else 4,.32))
    for direction in ('left','right'):
        g('pilcrow-'+direction,fit(pilcrow,6 if direction=='right' else 10,8,.65),arr(direction,12.5 if direction=='right' else 3.5,9,.39))
    g('remove-formatting',letter('t',6.7,6.5,.8),line((2,14),(8,14)),cross(12.3,12.1,.65))
    g('spell-check-2',letter('a',4.3,4.8,.43),letter('b',11.4,4.8,.43),st('M2 13Q3.5 10 5 13T8 13'),check(12,12,.52))
    for direction in ('left','right'):
        g('decimals-arrow-'+direction,circle(2.2,7,.65),number('0',6.3,5,.34),number('0',12,5,.34),arr(direction,9,12.4,.63))
    textrows=union(line((2,3),(14,3)),line((2,7),(11,7)),line((2,11),(10,11)))
    for end in ('center','end','start'):
        last={'center':(4,12),'end':(6,14),'start':(2,10)}[end]
        g('text-align-justify-'+end,st('M2 2.5H14M2 6.2H14M2 9.9H14'),line((last[0],13.6),(last[1],13.6)))
    g('summary',line((2,2.5),(14,2.5),width=1.7),st('M2 6H14M2 9.5H14M2 13H9',1.2))
    g('text-quote',st('M7 3H14M7 7H14M7 11H12'),st('M2 3V13',2.1))
    g('text-wrap',st('M2 3H14M2 7H11Q14 7 14 10Q14 13 11 13H6'),line((8.5,10.5),(6,13),(8.5,15.5)),line((2,11),(3.5,11)))
    g('text-initial',letter('a',4.5,7.5,.57),st('M9 3H14M9 6.5H14M9 10H14M2 13.5H14',1.1))
    g('whole-word',label('ab',8,6.5,.46),st('M1.7 11.3V14H14.3V11.3'))
    g('space',st('M2 6V10H14V6'))
    s('text-cursor-input',rr(1.5,4,13,8,1.5),st('M6 1.5H10M8 1.5V14.5M6 14.5H10',1.15))
    cursor_frame=rr(1.5,4,13,8,1.5)
    api.setdefault('STYLE_OVERRIDES',{})['text-cursor-input']={
        'solid':union(sub(union(cursor_frame,outline(cursor_frame)),line((8,4.8),(8,11.2),width=1.15)),
                      st('M6 1.5H10M8 1.5V3M8 13V14.5M6 14.5H10',1.15))}
    text_small=st('M2 3H14M2 7H8M2 11H6',1.25)
    search=union(ring(11,10.5,2.6,1.1),line((13,12.5),(15,14.5),width=1.2))
    g('text-search',text_small,search)
    pen=path('M2 11L11.5 1.5L14.5 4.5L5 14H1.5Z')
    pen_detail=st('M10 3L13 6M2 11L5 14',1.05)
    pen_glyph=union(outline(pen),pen_detail)
    g('text-pen',st('M2 3H10M2 7H7M2 11H4',1.2),fit(pen_glyph,11,11,.6))
    g('table-of-contents',st('M2 3H11M2 8H8M2 13H11'),dots((14,3),(14,8),(14,13),r=.6))
    for suffix,p in [('check',check(3.5,8,.55)),('start',arr('left',3.4,8,.38)),('end',arr('right',3.4,8,.38))]:
        g('list-'+suffix,st('M7 3H14M7 8H14M7 13H14'),p)
    for behavior in ('down-up','up-down'):
        g('list-chevrons-'+behavior,st('M7 3H14M7 8H14M7 13H14'),chev('down' if behavior=='down-up' else 'up',3,4.5,.4),chev('up' if behavior=='down-up' else 'down',3,11.5,.4))
    g('list-collapse',st('M7 3H14M7 8H14M7 13H14'),chev('right',3,8,.6))
    g('list-restart',st('M2 3H14M2 7H9M2 11H6'),st('M14 14A3.1 3.1 0 1 1 14.7 9M12 9H15V6.5',1.1))
    g('list-filter-plus',st('M2 3H14M4 7H12M6 11H8'),plus(12.5,12.5,.7))
    # Replace controls use actual text groups and directed exchange routes.
    for all_ in (False,True):
        g('replace-all' if all_ else 'replace',letter('a',5.2,4.7,.5),letter('b',10.8,11.6,.5),
          st('M10 2H13Q14 2 14 3V7M12 5L14 7L15.5 5',1.1),
          st('M6 14H3Q2 14 2 13V9M.5 11L2 9L4 11',1.1) if all_ else empty)
    for name,d in [('link-2-off','M6 10L4.5 11.5Q1 13 1.8 9L4 6.5M10 6L11.5 4.5Q15 3 14.2 7L12 9.5'),
                   ('unlink-2','M6 10L4.5 11.5Q1 13 1.8 9L4 6.5M10 6L11.5 4.5Q15 3 14.2 7L12 9.5')]:
        p=st(d)
        if name=='link-2-off': slash(p,name)
        else: g(name,p,st('M5 2L6 4M2 5L4 6M10 12L11 14M12 10L14 11',1.1))

    cat('Documents and books')
    book=rr(3,1.7,10,12.6,1.2)
    book_spine=st('M5.5 2V14M3 11.5H13',1.05)
    open_book=path('M8 3.5Q4 1 1.5 3V12Q4 10.8 8 13.5Q12 10.8 14.5 12V3Q12 1 8 3.5Z')
    for name,detail in [('book-a',letter('a',9,7,.38)),('book-type',letter('t',9,7,.38)),
                        ('book-bookmark',st('M8 2V8L10 6.5L12 8V2',1.1)),
                        ('book-exclamation-point',union(line((9,4),(9,7.5),width=1.15),circle(9,9,.55)))]:
        s(name,book,union(book_spine,detail))
    # Distinct rear copy remains visible at the top and left.
    g('book-copy',st('M1 11V3Q1 1 3 1H10',1.2),outline(fit(book,9,9,.84)),fit(book_spine,9,9,.84))
    for name,detail in [('book-open-text',st('M3.5 5H5.7M3.5 8H5.7M10.3 5H12.5M10.3 8H12.5',.95)),('book-open-check',check(11,7.5,.46))]:
        s(name,open_book,union(line((8,3.5),(8,13.5),width=1.1),detail))
    # Parallel library spines are discrete books, not a comb of lines.
    library=union(rect(1.8,2,2.7,12,.5),rect(6,2,2.7,12,.5),poly([(10,2.6),(12.5,2),(15,13.3),(12.5,14)]))
    s('library-big',library,st('M2 5H4.3M6.2 5H8.5M11 5.2L13.1 4.7',.9))
    s('square-library',rr(),fit(union(outline(library),st('M2 5H4.3M6.2 5H8.5',.9)),scale=.63))
    notebook=rr(3,1.7,10.5,12.6,1.2)
    binding=union(*(line((1.8,y),(4,y),width=1.05) for y in (4,8,12)))
    for name,detail in [('notebook-dot',circle(9,8,1.1)),('notebook-text',st('M6 5H11M6 8H11M6 11H9',1.05)),
                        ('notebook-pen',fit(pen_glyph,11.8,11.5,.48))]:
        s(name,notebook,union(binding,detail))
    notepad=rr(2.5,3,11,11.5,1)
    rings=union(*(line((x,1.5),(x,4.5),width=1.1) for x in (5,8,11)))
    note_text=st('M5 7H11M5 10H11M5 12.5H9',1.05)
    s('notepad-text',notepad,union(rings,note_text))
    g('notepad-text-dashed',dash_square(2.5,3,11,11.5),rings,note_text)
    clip=rr(3,3,10,11,1.3)
    tab=outline(rect(5.4,1.5,5.2,3,1),1.05)
    s('clipboard-type',clip,union(tab,letter('t',8,9.3,.42)))
    s('clipboard-pen-line',clip,union(tab,line((5.5,11),(8.5,11),width=1.1),fit(pen_glyph,11.4,10.5,.45)))
    sheet=rr(2,2,12,12,1)
    grid=st('M2 5.5H14M2 9.5H14M6 2V14M10 5.5V14',1.1)
    s('sheet',sheet,grid)
    s('table-2',sheet,st('M2 6H14M2 10H14M6 6V14',1.1))
    s('table-properties',sheet,st('M2 5.5H14M2 9.5H14M6 2V14M9 7.5H12M9 12H12',1.05))
    for horizontal in (True,False):
        body=union(rect(1.5,2,5,12,.8),rect(9.5,2,5,12,.8))
        detail=st('M1.5 6H6.5M9.5 6H14.5M1.5 10H6.5M9.5 10H14.5',1.05)
        if not horizontal: body,detail=transform(body,90),transform(detail,90)
        s('table-'+('columns' if horizontal else 'rows')+'-split',body,detail)
    sticky=path('M3 2H13Q14 2 14 3V10L10 14H3Q2 14 2 13V3Q2 2 3 2Z')
    fold=st('M10 14V10H14',1.1)
    for status,detail in [('plus',plus(7.5,7,.7)),('minus',line((5,7),(10,7))),('x',cross(7.5,7,.65)),('check',check(7.5,7,.65))]:
        s('sticky-note-'+status,sticky,union(fold,detail))
    slash(union(outline(sticky),fold),'sticky-note-off')
    g('sticky-notes',st('M11 1H3Q1 1 1 3V11',1.2),fit(union(outline(sticky),fold),9,9,.8))

    cat('Design tools')
    # Pen and pencil surfaces differ: nib for pen, wood and graphite for pencil.
    nib=path('M3 10L7 1.8L14.2 9L6 13L2 14Z')
    nibdetail=union(line((3,13),(8.5,7.5),width=1.1),outline(circle(8.8,7.2,1.2),1.05),line((6.7,2.5),(13.5,9.3),width=1.05))
    s('pen',nib,nibdetail)
    s('pen-line',fit(nib,8.5,6.5,.8),union(fit(nibdetail,8.5,6.5,.8),line((2,14),(14,14))))
    slash(union(outline(nib),nibdetail),'pen-off')
    s('pencil-line',fit(pen,8.5,6.5,.8),union(fit(pen_detail,8.5,6.5,.8),line((2,14),(14,14))))
    slash(pen_glyph,'pencil-off')
    s('pencil-sparkles',fit(pen,7,9,.8),union(fit(pen_detail,7,9,.8),plus(12.5,3,.6),plus(3.5,2.5,.4)))
    brushbody=path('M2 14Q5 14 6.5 11Q8 11 9 8L13.5 3.5Q15 1.5 13.3 1.5Q12.5 1.5 11.5 3L7 7Q4 7 4 10Q4 12 2 14Z')
    s('brush',brushbody,st('M4.3 10Q6 9 7.5 11M7 7L9 9',1.05))
    brushvertical=path('M6 1.8H10V8L12 10V13Q8 16 4 13V10L6 8Z')
    s('paintbrush-vertical',brushvertical,st('M4 10H12M6.7 12V14M9.3 12V14M6 6H10',1.05))
    s('paint-roller',rect(1.7,2,10,4.5,1),union(st('M11.7 4.3H14V9H8V11',1.15),rect(6.8,11,2.4,3.5,.6)))
    bucket=path('M2 6L7 1L13 7L7 13Z')
    s('paint-bucket',bucket,union(line((2,6),(13,7),width=1.1),st('M5 2L2 1',1.1),path('M13.5 10Q16 13 13.5 14Q11 13 13.5 10Z')))
    spray=rect(3,6,7.5,8.5,1.1)
    s('spray-can',spray,union(outline(rect(4.5,3,4.5,3,.4),1.1),line((5.5,1.5),(8,1.5),width=1.2),dots((12.3,2.8),(14.7,1.8),(14.7,4.3),r=.55),line((5.5,9),(5.5,12),width=1.1)))
    stamp=path('M3 10H13L14 14H2Z')
    s('stamp',stamp,union(st('M5 10V8Q7 7 6 5Q4 1.5 8 1.5Q12 1.5 10 5Q9 7 11 8V10',1.2),line((2,14),(14,14),width=1.4)))
    compasslegs=union(st('M8 5L3 14M8 5L13 14M4.8 10H11.2'),outline(circle(8,3.8,2),1.15),line((8,1),(8,1.8),width=1.1))
    g('drafting-compass',compasslegs)
    g('magnet',st('M3 2V8.5C3 15.5 13 15.5 13 8.5V2H9.5V8.5C9.5 10.8 6.5 10.8 6.5 8.5V2ZM3 5H6.5M9.5 5H13'))
    wand=union(outline(poly([(2,12),(11.5,2.5),(13.5,4.5),(4,14)]),1.1),line((9.5,4.5),(11.5,6.5),width=1.05))
    g('wand',wand)
    g('wand-sparkles',fit(wand,7,9,.82),plus(12.5,2.8,.55),plus(3.3,3.1,.45),plus(13.2,10,.35))
    s('slice',poly([(1.8,14.2),(4,7.7),(9,2.7),(13.3,7),(8.3,12)]),st('M4 7.7L8.3 12M9 2.7L10.5 1.2L14.8 5.5L13.3 7',1.1))
    g('signature',st('M1.5 11C6 14 8-1 5.5 2C3 5 4.5 14 7 11L9 8Q9 14 11 10Q12 7 13 9Q13.5 11 15 9',1.2),line((3,14),(13,14),width=1.05))
    g('line-squiggle',st('M1.5 11C5-2 2 17 8 8C14-1 9 17 14.5 5'))
    g('line-style',line((2,3),(14,3),width=1.8),line((2,8),(7,8),width=1.3),line((10,8),(14,8),width=1.3),dots((2.5,13),(6.2,13),(9.9,13),(13.6,13),r=.6))
    spline=st('M2 13C10 13 6 3 14 3',1.25)
    g('spline',spline,outline(circle(2,13,1.3),1.05),outline(circle(14,3,1.3),1.05))
    pointer2=poly([(2.5,1.8),(13.8,8),(8.5,9),(6.8,14.3)])
    g('spline-pointer',fit(spline,7,6.5,.85),outline(circle(2,11,1.1),1),fit(outline(pointer2,1.2),11.5,12,.4))
    g('lasso',st('M4 11C-3 4 6-2 12 2C19 7 9 14 4 11Q1 12 2 14Q3 16 5 14',1.25))
    g('lasso-select',st('M4 11C-3 4 6-2 12 2C15 4 15 7 12 9M4 11Q1 12 2 14',1.2),fit(outline(pointer2,1.3),11.5,11.7,.48))
    g('frame',st('M4 1V15M12 1V15M1 4H15M1 12H15',1.25))
    g('group',dash_square(),outline(rect(4.5,4.5,5,5,.7),1.1),outline(rect(7,7,5,5,.7),1.1))
    for cap in ('butt','round','square'):
        # Literal cap demonstrations retain the corresponding end shape.
        body=rect(3,6,10,4,2 if cap=='round' else 0)
        if cap=='square': body=rect(2,6,12,4,0)
        g('stroke-line-cap-'+cap,body,line((3,2),(3,14),width=.8),line((13,2),(13,14),width=.8))
    for join in ('bevel','miter','round'):
        if join=='round': body=st('M2.5 13L8 3L13.5 13',3)
        elif join=='miter': body=path('M.8 12.3L8 .5L15.2 12.3L12.6 13.7L8 6L3.4 13.7Z')
        else: body=path('M1 12L6.5 2.5H9.5L15 12L12.5 13.5L8 5.8L3.5 13.5Z')
        g('stroke-line-join-'+join,body)
    # Boolean operation symbols display the actual result inside the two
    # source outlines; this avoids arbitrary diagonal marks on identical boxes.
    a,b=rect(1.7,1.7,8.2,8.2,1),rect(6.1,6.1,8.2,8.2,1)
    for mode in ('exclude','intersect','subtract','unite'):
        if mode=='exclude': result=op(a,b,po.PathOp.XOR)
        elif mode=='intersect': result=inter(a,b)
        elif mode=='subtract': result=sub(a,b)
        else: result=union(a,b)
        name='squares-'+mode
        # One faded source plane is meaningful construction context. The
        # actual boolean result is opaque with a contour in Stroke.
        g(name,outline(a,1.1),outline(b,1.1))
        if mode=='intersect':
            contextual=union(dash_square(1.7,1.7,8.2,8.2),dash_square(6.1,6.1,8.2,8.2))
        elif mode=='subtract': contextual=dash_square(6.1,6.1,8.2,8.2)
        else: contextual=empty
        primary=union(result,outline(result,1.1))
        secondary=sub(union(a,b),primary)
        tone_layers=([(secondary,.24)] if secondary.area>.001 else [])+[(primary,1)]
        if secondary.area>.001:
            api['DUOTONE_GLYPHS'][name]='Source construction planes recede behind the opaque Boolean result; layers are mutually clipped.'
        api.setdefault('STYLE_OVERRIDES',{})[name]={
            'duotone':tone_layers,
            'solid':union(result,outline(result,1.1)),
            'stroke':union(contextual,outline(result,1.25))}
    # Layer sheets remain independent planes, with explicit occlusion.
    plane=poly([(8,2),(14.5,5.5),(8,9),(1.5,5.5)])
    planestroke=outline(plane,1.15)
    for count in (1,2):
        for direction in ('up','down'):
            name=('layers-' if count==2 else 'layer-')+'arrow-'+direction
            sheetpiece=fit(planestroke,6.2,5.8,.76)
            if count==2: sheetpiece=union(sheetpiece,st('M1.2 8.5L6.2 11.2L10 9.2',1.15))
            g(name,sheetpiece,arr(direction,12.5,10.3,.52))
    g('layers-2',planestroke,st('M1.5 9L8 12.5L14.5 9'))
    for action,p in [('plus',plus(12.5,12,.63)),('minus',line((10.5,12),(14.5,12),width=1.3))]:
        g('layers-'+action,fit(planestroke,7,6.2,.86),st('M1 9L7 12.5L8.7 11.6',1.15),p)
    rear,front=rect(2,2,8.5,8.5,1.2),rect(5.5,5.5,8.5,8.5,1.2)
    for name,foreground,background in [('bring-to-front',front,rear),('send-to-back',rear,front)]:
        g(name,sub(outline(background),union(foreground,outline(foreground,2.7))),foreground,outline(foreground))
    s('square-square',rr(),outline(rect(5.2,5.2,5.6,5.6,.6),1.15))
    g('square-stack',st('M1.5 10V2.5Q1.5 1.5 2.5 1.5H10M4 12V5Q4 4 5 4H12',1.15),outline(rect(6.5,6.5,8,8,1.2),1.2))
    for status,p in [('minus',line((8.5,10),(12.5,10),width=1.15)),('slash',line((8,12),(13,7),width=1.15))]:
        g('copy-'+status,st('M2 11V3Q2 2 3 2H10',1.2),outline(rect(5,5,9,9,1.2),1.2),p)
    g('blend',sub(outline(circle(5.6,8,4.1)),circle(10.4,8,4.1)),outline(circle(10.4,8,4.1)),inter(circle(5.6,8,4.1),circle(10.4,8,4.1)))
    s('opacity',circle(),inter(circle(),rect(8,2,6,12,0)))
    # Keep the halftone plane within the circular body in all styles.
    opacity_primary=union(inter(circle(),rect(8,2,6,12,0)),outline(circle()))
    api.setdefault('STYLE_OVERRIDES',{})['opacity']={
        'duotone':[(sub(inter(circle(),rect(2,2,6,12,0)),opacity_primary),.24),(opacity_primary,1)],
        'solid':union(outline(circle()),inter(circle(),rect(8,2,6,12,0))),
        'stroke':union(outline(circle()),line((8,2),(8,14)))}
    for horizontal in (True,False):
        name='square-centerline-dashed-'+('horizontal' if horizontal else 'vertical')
        divider=dashed([(8,1),(8,15)],width=1.05)
        s(name,rr(),transform(divider,90) if horizontal else divider)
        triangles=union(outline(poly([(2,3),(6,8),(2,13)]),1.1),outline(poly([(14,3),(10,8),(14,13)]),1.1),divider)
        g('triangles-centerline-dashed-'+('horizontal' if horizontal else 'vertical'),transform(triangles,90) if horizontal else triangles)
    for horizontal in (True,False):
        s('square-split-'+('horizontal' if horizontal else 'vertical'),rr(),line((2,8),(14,8)) if horizontal else line((8,2),(8,14)))
    s('square-round-corner',rr(),st('M5 11V8Q5 5 8 5H11',1.7))
    s('square-dimensions',rr(2.5,2.5,10,10,1),st('M2.5 15H12.5M1 14V16M14 14V16M15 2.5V12.5M14 1H16M14 14H16',.9))
    s('square-text',rr(),st('M4.5 5H11.5M4.5 8H11.5M4.5 11H9',1.15))
    s('square-menu',rr(),st('M4.5 5H11.5M4.5 8H11.5M4.5 11H11.5',1.15))
    s('square-code',rr(),st('M6.5 5L3.5 8L6.5 11M9.5 5L12.5 8L9.5 11',1.15))
    s('square-pen',rr(),fit(pen_glyph,scale=.6))
    s('square-mouse-pointer',rr(),fit(outline(pointer2),scale=.62))
    slash(outline(rr()),'square-off')
    for name,p in [('square-dashed-plus',plus()),('square-dashed-x',cross()),('square-dashed-search',fit(search,8,8,.9)),('square-dashed-mouse-pointer',fit(outline(pointer2),10.6,11,.7))]:
        g(name,sub(dash_square(),circle(11,11,3.2)) if name.endswith(('search','mouse-pointer')) else dash_square(),p)
    g('square-dashed-x-corner',sub(dash_square(),rect(10,10,6,6)),cross(12,12,.7))
    g('square-dashed-top-solid',sub(dash_square(),rect(0,0,16,3)),line((2,2),(14,2)))
    scissors=union(outline(circle(4,4,2),1.1),outline(circle(4,12,2),1.1),line((5.5,5.5),(14,13),width=1.15),line((5.5,10.5),(14,3),width=1.15))
    s('square-scissors',rr(),fit(scissors,scale=.64))
    g('scissors-line-dashed',fit(scissors,6.5,8,.75),dashed([(10,8),(15,8)],width=1.1))
    g('square-bottom-dashed-scissors',st('M2 10V3Q2 2 3 2H13Q14 2 14 3V10',1.2),dashed([(2,13.5),(14,13.5)],width=1.1),fit(scissors,8,11,.45))

    cat('Maps and travel')
    globe=union(outline(circle()),st('M2 8H14M8 2C3.5 5 3.5 11 8 14C12.5 11 12.5 5 8 2',1.1))
    # Earth shows land masses rather than longitude lines.
    earthdetail=st('M4 2.7L5.5 5L3.5 7.3L5.7 9L6.3 13.8M10 2.5L9 5L12 6L10 8L12 10L13.7 9',1.1)
    s('earth',circle(),earthdetail)
    for state,p in [('check',check(12.3,12.4,.5)),('plus',plus(12.3,12.4,.6)),('x',cross(12.3,12.4,.57)),
                    ('ban',union(outline(circle(12.3,12.3,2.1),1.0),line((10.8,10.8),(13.8,13.8),width=.95))),
                    ('code',st('M10.5 10L8.5 12L10.5 14M13 10L15 12L13 14',1.05))]:
        cut=circle(12.3,12.3,3.2) if state!='code' else rect(7.5,9,8.5,7,.5)
        g('globe-'+state,sub(globe,cut),p)
    slash(globe,'globe-off')
    mappoly=path('M1.8 3.5L6 1.8L10 3.5L14.2 1.8V12.5L10 14.2L6 12.5L1.8 14.2Z')
    mapfold=st('M6 1.8V12.5M10 3.5V14.2',1.05)
    for state,p in [('plus',plus(12.5,12,.65)),('minus',line((10.5,12),(14.5,12),width=1.25))]:
        body=sub(mappoly,circle(12.5,12,3.1))
        s('map-'+state,body,union(sub(mapfold,circle(12.5,12,3.1)),p))
    pin=path('M8 14.5C6 12.5 2.5 8.5 2.5 5.8C2.5-.7 13.5-.7 13.5 5.8C13.5 8.5 10 12.5 8 14.5Z')
    hole=outline(circle(8,5.8,1.7),1.05)
    for state,p in [('check',check(8,6,.6)),('minus',line((5.7,5.8),(10.3,5.8),width=1.1)),
                    ('plus',plus(8,5.8,.55)),('x',cross(8,5.8,.57))]:
        name='map-pin-'+state+'-inside'
        s(name,pin,p)
    for state,p in [('check',check(12.2,12,.5)),('minus',line((10.5,12),(14.2,12),width=1.2)),
                    ('house',st('M10 12L12.5 9.5L15 12M10.7 11.5V14H14.3V11.5',1.05)),
                    ('pen',fit(pen_glyph,12.5,12,.42)),
                    ('search',union(outline(circle(12,11.7,1.9),1.05),line((13.5,13.2),(15,14.7),width=1.05)))]:
        region=circle(12.2,12,3.2)
        s('map-pin-'+state,sub(pin,region),union(sub(hole,region),p))
    g('map-pinned',fit(union(outline(mappoly),mapfold),8,10,.78),fit(union(outline(pin),hole),8,5,.55))
    s('land-plot',poly([(1.8,8),(7,3),(14.2,8),(9,13)]),st('M5 5L12 10M4 10L10.5 5.5M2 8V11M14 8V11',1.1))
    sign=poly([(2,4),(11,4),(14,7),(11,10),(2,10)])
    s('signpost-big',sign,union(line((8,1.5),(8,4)),line((8,10),(8,14.5)),line((5,7),(10,7),width=1.05)))
    s('milestone',poly([(2,4),(11,4),(14,7),(11,10),(2,10)]),union(line((6,10),(6,14.5)),arr('right',8,7,.42)))
    route=union(outline(circle(3,3,1.6),1.1),outline(circle(13,13,1.6),1.1),st('M5 3H11Q14 3 14 6Q14 8 11 8H5Q2 8 2 11Q2 13 5 13H11',1.1))
    slash(route,'route-off')
    g('route-arrow-right',outline(circle(3,3,1.6),1.1),st('M5 3H11Q14 3 14 6Q14 8 11 8H5Q2 8 2 11Q2 13 5 13H13',1.1),line((10,10),(13,13),(10,15.5),width=1.1))
    target=union(outline(circle(8,8,4.2)),line((8,1.5),(8,4)),line((8,12),(8,14.5)),line((1.5,8),(4,8)),line((12,8),(14.5,8)))
    slash(target,'locate-off')
    g('radar',outline(circle()),outline(circle(8,8,3),1.05),line((8,8),(12.7,3.3)),circle(4.7,8.9,.7))
    for name,p in [('navigation-2',poly([(8,1.7),(14,14),(8,11),(2,14)])),
                   ('mouse-pointer-2',pointer2)]:
        s(name,p)
        slash(outline(p),name+'-off')
    navigation=poly([(2,6),(14,2),(10,14),(7.5,8.5)])
    slash(outline(navigation),'navigation-off')
    hand=path('M4.5 13.5Q2 11.5 1.5 8.5Q1.5 7 3 7L5 9V3.5Q5 2 6.5 2Q8 2 8 3.5V7Q8 5.5 9.5 5.5Q11 5.5 11 7Q11 6 12.5 6.5Q14 6.8 14 8.5V11Q14 14 11 14H6Z')
    s('pointer',hand,st('M8 7V9M11 7V9',1.0))
    slash(union(outline(hand),st('M8 7V9M11 7V9',1)),'pointer-off')
    grab=path('M2 10V7Q2 5 4 6V5Q4 3 6 4Q6 2 8 3Q9 2 10.5 3.5Q12.5 3 13.5 5V10Q13.5 14 9.5 14H6Q3 14 2 10Z')
    s('hand-grab',grab,st('M4 6V8M6 4V8M8.5 3.5V8M11 4V8M2 10H6',1.05))
    ban=union(outline(circle(12.2,12.2,2.4),1.1),line((10.5,10.5),(13.9,13.9),width=1.05))
    s('mouse-pointer-ban',sub(pointer2,circle(12.2,12.2,3.2)),ban)
    wheel=union(outline(circle(8,7.2,5.5),1.15),*(line((8,7.2),(8+5.5*math.cos(a),7.2+5.5*math.sin(a)),width=.85) for a in [i*math.pi/3 for i in range(6)]),circle(8,7.2,.9),st('M8 7.2L4.8 14.5M8 7.2L11.2 14.5M3 14.5H13',1.15))
    g('ferris-wheel',wheel)
    g('roller-coaster',st('M1.5 10C4 10 3.5 3 6.5 3C9.5 3 9 11 12 11Q13.5 11 14.5 8M1.5 12C5 12 4.5 5 6.5 5C8.5 5 8 13 12 13Q14 13 15 10',1.05),st('M4 9V14.5M9.8 12V14.5M13.5 12.5V14.5',.85))

    cat('Transform and flow')
    for vertical in (False,True):
        pieces=union(outline(rect(1.2,1.8,4,3.5,.6),1.1),outline(rect(10.8,1.8,4,3.5,.6),1.1),outline(rect(6,10.8,4,3.5,.6),1.1),st('M3.2 5.3V7.5H12.8V5.3M8 7.5V10.8',1.1))
        g('diagram-flow-'+('vertical' if vertical else 'horizontal'),pieces if vertical else transform(pieces,90))
    for name in ('move-3d','scale-3d','rotate-3d'):
        axes=st('M7 8V2M7 8L1.5 12.5M7 8L14 12',1.15)
        if name=='move-3d': details=st('M5 4L7 2L9 4M1.5 9.5V12.5H4.5M11 12.5L14 12L13 9',1.1)
        elif name=='scale-3d': details=union(rect(5.7,1,2.6,2.6,.35),rect(1,11,2.6,2.6,.35),rect(12,10.7,2.6,2.6,.35))
        else: details=st('M2.5 5Q8-1 14 6M11 5L14 6L14 3M3 10Q8 16 13 11',1.1)
        g(name,axes,details)
    for cw in (False,True):
        p=union(outline(rect(3.5,4.5,7,7,1),1.15),st('M2 7Q2 1.5 7 1.5H13M10 0L13 1.5L10 4',1.1))
        g('rotate-'+('cw' if cw else 'ccw')+'-square',p if cw else mirror(p))
    s('rotate-cw-clock',circle(8,8.5,5),union(st('M8 5.5V8.5L10.5 10',1.1),st('M3 3Q8-1 13 3M10 3H13V.5',1.1)))
    g('scaling',outline(rect(2,8,6,6,.8),1.1),st('M2 5V2H5M8 2H14V8',1.1),line((8,8),(14,2)))
    g('scan-box',st('M1.5 5V1.5H5M11 1.5H14.5V5M1.5 11V14.5H5M11 14.5H14.5V11',1.1),fit(miniature,scale=.55))
    g('view',st('M1.5 5V1.5H5M11 1.5H14.5V5M1.5 11V14.5H5M11 14.5H14.5V11',1.1),st('M3.2 8Q8 1.8 12.8 8Q8 14.2 3.2 8Z',1.1),circle(8,8,1.25))
    funnel=path('M2 2H14L9.5 7.5V13L6.5 14V7.5Z')
    for state,p in [('plus',plus(12.5,12.5,.6)),('x',cross(12.5,12.5,.6))]:
        s('funnel-'+state,sub(funnel,circle(12.5,12.5,3)),p)
    s('search-exclamation-point',circle(6.7,6.7,4.6),union(line((10.3,10.3),(14,14)),line((6.7,3.8),(6.7,6.8),width=1.15),circle(6.7,8.8,.6)))
    s('search-slash',circle(6.7,6.7,4.6),union(line((10.3,10.3),(14,14)),line((4.7,8.7),(8.7,4.7),width=1.2)))
    g('loader-pinwheel',*(transform(st('M8 2Q13 2 13 7L8 8Z',1.05),a) for a in (0,90,180,270)))
    # Fading in the name denotes incomplete progress, expressed as a broken
    # circumference; no arbitrary opacity is applied to a continuous stroke.
    g('circle-fading-arrow-up',sub(dash_circle(),rect(5,0,6,5)),arr('up',8,7,.65))
    s('cloud-backup',path('M4 12Q1 12 1 9Q1 6 4 6Q4 1 8 1Q12 1 12 5Q15 5 15 8.5Q15 12 12 12Z'),union(outline(circle(8,9,2.5),1.05),st('M8 7.5V9L9.3 10',1)))
    keyboard=union(outline(rect(1.5,3.5,13,9,1.4)),dots(*[(x,y) for x in (4,6.7,9.4,12) for y in (6,8.7)],r=.45),line((5,11),(11,11),width=1.1))
    slash(keyboard,'keyboard-off')
    g('import',st('M9 2H13Q14 2 14 3V13Q14 14 13 14H9',1.2),arr('right',5.8,8,.8))

    missing=set(NAMES)-made
    extra=made-set(NAMES)
    assert not missing, 'Unimplemented design names: '+', '.join(sorted(missing))
    assert not extra, 'Unassigned design names: '+', '.join(sorted(extra))
