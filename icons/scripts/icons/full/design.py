"""Original rounded design, text, geometry and navigation coverage.

All recipes use the CXL 16-unit construction grid. Reference names are metadata;
no reference artwork or font outlines are used. Letterforms are purpose-drawn
monoline capitals with open counters, reused only for actual letter semantics.
"""
import json
import math
from pathlib import Path

from fontTools.misc.bezierTools import splitCubicAtT

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

    def cancel_surface(name, body, details, start=(2,2), end=(14,14)):
        badged(name, body, details, line(start,end), line(start,end,width=3.2))

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
        radius = api['RADIUS']
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
    # Lane D (SF polish): an SF Pro-like monoline alphabet. Glyphs are drawn on
    # a cap centerline of 10 em (0 = cap top, 10 = baseline) and placed by ink
    # cap height, so every text symbol shares one letter construction at the
    # family STROKE. The older `letters`/`digits` tables stay for other lanes.
    SW = api['STROKE']

    def earc(cx, cy, rx, ry, a0, a1, move=True):
        def at(a):
            return cx+rx*math.cos(math.radians(a)), cy+ry*math.sin(math.radians(a))
        (x0, y0), (x1, y1) = at(a0), at(a1)
        large = 1 if abs(a1-a0) > 180 else 0
        sweep = 1 if a1 > a0 else 0
        head = f'M{x0:.4f} {y0:.4f}' if move else f'L{x0:.4f} {y0:.4f}'
        return head+f'A{rx} {ry} 0 {large} {sweep} {x1:.4f} {y1:.4f}'

    def ellipse_d(cx, cy, rx, ry):
        return f'M{cx-rx} {cy}A{rx} {ry} 0 1 1 {cx+rx} {cy}A{rx} {ry} 0 1 1 {cx-rx} {cy}Z'

    XH = 2.75   # lowercase x-height top (SF Pro x-height ~ 0.73 cap)
    GLYPHS = {
        'A': (8.0, 'M0 10L3.62 0H4.38L8 10M1.2 6.65H6.8'),
        'B': (6.5, 'M0 0H3.5C5.35 0 6.1 1.1 6.1 2.4C6.1 3.75 5.1 4.75 3.5 4.75H0'
                   'M0 4.75H3.75C5.55 4.75 6.5 5.9 6.5 7.35C6.5 8.9 5.45 10 3.6 10H0V0'),
        'C': (8.1, earc(4.55, 5, 4.55, 5.15, -38, -322)),
        'D': (7.4, 'M0 0H2.85C5.95 0 7.4 2.2 7.4 5C7.4 7.8 5.95 10 2.85 10H0Z'),
        'E': (5.7, 'M5.7 0H0V10H5.7M0 4.95H5.15'),
        'F': (5.6, 'M5.6 0H0V10M0 5.1H5.05'),
        'G': (9.1, earc(4.6, 5, 4.6, 5.15, -38, -350)+'V5.25H5.2'),
        'H': (6.8, 'M0 0V10M6.8 0V10M0 5H6.8'),
        'I': (0, 'M0 0V10'),
        'J': (5.0, 'M5 0V6.9C5 9 3.9 10.1 2.45 10.1C1.1 10.1 .2 9.3 0 8'),
        'K': (6.7, 'M0 0V10M6.45 0L0 6.55M2.4 4.15L6.7 10'),
        'L': (5.5, 'M0 0V10H5.5'),
        'M': (8.8, 'M0 10V0L4.4 9.1L8.8 0V10'),
        'N': (7.0, 'M0 10V0L7 10V0'),
        'O': (9.4, ellipse_d(4.7, 5, 4.7, 5.15)),
        'P': (6.4, 'M0 10V0H3.6C5.4 0 6.4 1.25 6.4 2.75C6.4 4.3 5.4 5.5 3.6 5.5H0'),
        'Q': (9.4, ellipse_d(4.7, 5, 4.7, 5.15)+'M6 7.45L9.3 10.5'),
        'R': (6.6, 'M0 10V0H3.6C5.4 0 6.4 1.2 6.4 2.65C6.4 4.1 5.4 5.3 3.6 5.3H0M3.75 5.3L6.6 10'),
        'S': (6.8, 'M6.35 1.55C5.8 .5 4.7 -.1 3.3 -.1C1.5 -.1 .25 .9 .25 2.5'
                   'C.25 6.2 6.8 4.3 6.8 7.6C6.8 9.2 5.4 10.1 3.4 10.1C1.8 10.1 .6 9.4 0 8.3'),
        'T': (7.2, 'M0 0H7.2M3.6 0V10'),
        'U': (6.9, 'M0 0V6.4C0 8.7 1.4 10.1 3.45 10.1C5.5 10.1 6.9 8.7 6.9 6.4V0'),
        'V': (8.0, 'M0 0L3.62 10H4.38L8 0'),
        'W': (11.6, 'M0 0L2.75 10L5.8 .1L8.85 10L11.6 0'),
        'X': (7.4, 'M0 0L7.4 10M7.4 0L0 10'),
        'Y': (7.6, 'M0 0L3.8 5.45L7.6 0M3.8 5.45V10'),
        'Z': (6.8, 'M.35 0H6.6L0 10H6.8'),
        'a': (5.75, 'M.5 4C.95 3.1 1.85 2.65 3 2.65C4.7 2.65 5.75 3.5 5.75 5.1V10'
                    'M5.75 6.2H2.9C1 6.2 0 7 0 8.2C0 9.4 1 10.1 2.4 10.1C4.3 10.1 5.75 9 5.75 7.3'),
        'b': (6.4, 'M0 0V10'+ellipse_d(3.2, 6.38, 3.2, 3.72)),
        'c': (5.8, earc(3.05, 6.38, 3.05, 3.72, -40, -320)),
        'd': (6.4, 'M6.4 0V10'+ellipse_d(3.2, 6.38, 3.2, 3.72)),
        'e': (6.1, 'M.05 6.3H6.1C6.1 4.1 4.9 2.65 3.05 2.65C1.2 2.65 0 4.2 0 6.4'
                   'C0 8.6 1.25 10.1 3.15 10.1C4.5 10.1 5.5 9.4 5.9 8.4'),
        'f': (3.9, 'M3.9 .15Q3.5 0 3.1 0C1.9 0 1.3 .75 1.3 2V10M0 2.85H3.7'),
        'i': (0, 'M0 2.85V10'),
        'x': (5.9, 'M0 2.75L5.9 10M5.9 2.75L0 10'),
        '0': (6.6, ellipse_d(3.3, 5, 3.3, 5.15)),
        '1': (3.0, 'M0 2.05L3 0V10'),
        '2': (6.4, 'M.3 2.6C.6 .95 1.8 -.1 3.3 -.1C5 -.1 6.2 1 6.2 2.65C6.2 4 5.4 5 4.3 6L0 10H6.4'),
        '3': (6.3, 'M.2 1.9C.7 .6 1.8 -.1 3.2 -.1C4.9 -.1 6 .95 6 2.45C6 3.95 4.8 4.85 3.1 4.85H2.6'
                   'M3.1 4.85C5.1 4.85 6.3 5.9 6.3 7.45C6.3 9.05 5 10.1 3.2 10.1C1.6 10.1 .5 9.3 0 8.1'),
        '5': (6.3, 'M5.9 0H.8L.3 5C.9 4.2 1.9 3.75 3.1 3.75C5 3.75 6.3 5 6.3 6.9'
                   'C6.3 8.8 4.9 10.1 3.1 10.1C1.6 10.1 .5 9.35 0 8.2'),
        '6': (6.4, ellipse_d(3.2, 6.95, 3.2, 3.15)+'M0 6.95V5.4C0 2.1 1 -.1 3.2 -.1C4.2 -.1 5 .4 5.6 1.3'),
    }
    DOTTED = {'i': .55}

    def glyph_at(ch, left, top, s):
        width, d = GLYPHS[ch]
        p = st(path(d).transform(s, 0, 0, s, left, top))
        if ch in DOTTED:
            p = union(p, circle(left, top+DOTTED[ch]*s, .66))
        return p

    def word(text, cx=8, cy=8, cap=9.5, gap=.9, maxw=14.6, baseline=None):
        """Place glyphs by ink cap height; shrink uniformly to fit maxw."""
        s = (cap-SW)/10
        def width(s):
            return sum(GLYPHS[c][0]*s for c in text)+(len(text)-1)*(gap+SW)+SW
        if width(s) > maxw:
            fixed = (len(text)-1)*(gap+SW)+SW
            s = (maxw-fixed)/sum(GLYPHS[c][0] for c in text)
        x = cx-width(s)/2+SW/2
        top = (baseline-10*s) if baseline is not None else cy-5*s
        parts = []
        for c in text:
            parts.append(glyph_at(c, x, top, s))
            x += GLYPHS[c][0]*s+gap+SW
        return union(*parts)

    # SF square container (11.8 u ink, standard corner) and circle (13.1 u).
    SQ = rr(2.6, 2.6, 10.8, 10.8)
    SQ_BOX = (2.6, 2.6, 10.8, 10.8)

    def slashed(name, body, detail, gap=.85, ends=((2.3, 2.3), (13.7, 13.7)), outline_body=True):
        """SF .slash: one full-weight diagonal, upper-left to lower-right, behind a clearance gap."""
        bar = line(*ends)
        clearance = line(*ends, width=SW+2*gap)
        if outline_body:
            badged(name, body, detail, bar, clearance)
        else:
            kept = [part for part in api['components'](sub(union(body, detail), clearance)) if part.area >= .6]
            g(name, *kept, bar)

    def sfarrow(x0, y0, x1, y1, arm=None):
        """SF arrow: shaft meets the apex of a 45-degree chevron head."""
        length = math.hypot(x1-x0, y1-y0)
        arm = arm if arm is not None else .4*length
        ux, uy = (x1-x0)/length, (y1-y0)/length
        def wing(sign):
            a = math.atan2(-uy, -ux)+sign*math.pi/4
            return x1+arm*math.cos(a), y1+arm*math.sin(a)
        (lx, ly), (rx_, ry_) = wing(1), wing(-1)
        return st(f'M{x0} {y0}L{x1} {y1}M{lx:.4f} {ly:.4f}L{x1} {y1}L{rx_:.4f} {ry_:.4f}')

    def sfchevron(x, y, direction, half=1.7):
        """Open 90-degree chevron centred on its apex at (x, y)."""
        d = {'up': ((-1, 1), (1, 1)), 'down': ((-1, -1), (1, -1)),
             'left': ((1, -1), (1, 1)), 'right': ((-1, -1), (-1, 1))}[direction]
        (ax, ay), (bx, by) = d
        return st(f'M{x+ax*half} {y+ay*half}L{x} {y}L{x+bx*half} {y+by*half}')

    # SF text rows: four lines over 11.1 u (text.alignleft), list rows over 9.3 u.
    TX0, TX1 = 2.05, 13.95
    ROWS4 = (3, 6.333, 9.667, 13)
    ROWS3 = (4, 8, 12)

    def sfpencil(tx, ty, angle=-45, length=12.0, width=2.05, cap=1.45, gap=.8):
        """SF pencil: a slim solid bar with a sharpened tip and a separated end cap.
        Tip at (tx, ty); the body runs away from the tip along `angle`."""
        hw = width/2
        cone = 2.35
        body_end = length-cap-gap
        p = path(f'M0 0L{cone} {-hw}H{body_end}V{hw}H{cone}Z'
                 f'M{length-cap} {-hw}H{length}V{hw}H{length-cap}Z')
        p = api['soften'](p, .3)
        a = math.radians(angle)
        c, s_ = math.cos(a), math.sin(a)
        return p.transform(c, s_, -s_, c, tx, ty)

    def pencil_cut(p, extra=.9):
        return union(p, outline(p, 2*extra))

    # SF cursorarrow: a solid arrow cursor with a tail (tip at the origin).
    cursor = api['soften'](path('M0 0V10.4L2.55 8.05L4.2 11.75L5.85 11.0L4.25 7.4H7.75Z'), .3)
    def cursor_at(x, y, scale):
        return cursor.transform(scale, 0, 0, scale, x, y)

    # square.on.square pair: two SF squares (9.9 u ink) offset 3.7 u, 13.6 u overall.
    PAIR_BACK = rr(1.72, 1.72, 8.86, 8.86)
    PAIR_FRONT = rr(5.42, 5.42, 8.86, 8.86)

    def text_rows(spec):
        return st(''.join(f'M{a} {y}H{b}' for a, b, y in spec))

    for ch in 'abcdefghijklmnopqrstuvwxyz':
        C = ch.upper()
        if 'letter-'+ch in NAMES:
            g('letter-'+ch, word(C, cap=9.5), tags='alphabet character '+ch)
        if f'circle-letter-{ch}' in NAMES:
            s(f'circle-letter-{ch}', circle(), word(C, cap=6.2, maxw=7.6), tags='alphabet character '+ch)
        if f'square-letter-{ch}' in NAMES:
            s(f'square-letter-{ch}', SQ, word(C, cap=5.9, maxw=7.2), tags='alphabet character '+ch)
    slashed('circle-letter-p-off', circle(), word('P', cap=6.2))
    slashed('square-letter-p-off', SQ, word('P', cap=5.9))
    g('letters', word('Abc', cap=8.2, gap=.55))
    g('numbers', word('123', cap=8.6, gap=.8))
    g('binary', word('10', cy=4.75, cap=5.5, gap=1.3), word('01', cy=11.25, cap=5.5, gap=1.3))

    cat('Navigation')
    directions={'right':0,'down':90,'left':180,'up':270,'up-right':-45,'down-right':45,'down-left':135,'up-left':225}
    # ---- Lane C: one SF arrow system (measured from SF Symbols Regular) ----
    # arrow.right: 10.89 u centerline shaft, chevron head with 45 degree arms
    # whose projection is 4.31 u (0.4 of the length); diagonals 11.73 u with
    # 5.9 u axis-aligned arms. Containers use the same construction scaled.
    SW = api['STROKE']
    VEC = {'right':(1,0),'left':(-1,0),'down':(0,1),'up':(0,-1),
           'up-right':(1,-1),'down-right':(1,1),'down-left':(-1,1),'up-left':(-1,-1)}

    def gap_stroke(p, gap=.9):
        # Clearance cutter: the ink of p plus a uniform gap (exact width).
        return st(p, SW+2*gap, exact=True) if isinstance(p, str) else union(p, st(p, 2*gap, exact=True))

    def head(x1, y1, ux, uy, h):
        n = math.hypot(ux, uy); ux, uy = ux/n, uy/n
        return line((x1-h*ux+h*uy, y1-h*uy-h*ux), (x1, y1), (x1-h*ux-h*uy, y1-h*uy+h*ux))

    def seg(p0, p1, h=4.31, both=False):
        """SF arrow from p0 to p1: shaft meets the apex of a 45 degree chevron."""
        (x0, y0), (x1, y1) = p0, p1
        parts = [line(p0, p1), head(x1, y1, x1-x0, y1-y0, h)]
        if both: parts.append(head(x0, y0, x0-x1, y0-y1, h))
        return union(*parts)

    def A(direction='right', x=8, y=8, scale=1, L=None, h=None, both=False):
        vx, vy = VEC[direction]
        diag = vx and vy
        L = (11.73 if diag else 10.89) if L is None else L
        h = (4.17 if diag else 4.31) if h is None else h
        n = math.hypot(vx, vy); ux, uy = vx/n, vy/n
        half = L*scale/2
        return seg((x-ux*half, y-uy*half), (x+ux*half, y+uy*half), h*scale, both)

    def chevron(direction='right', x=8, y=8, w=5.16, hh=5.03):
        vx, vy = VEC[direction]
        if vx:
            pts = [(x-vx*w/2, y-hh), (x+vx*w/2, y), (x-vx*w/2, y+hh)]
        else:
            pts = [(x-hh, y-vy*w/2), (x, y+vy*w/2), (x+hh, y-vy*w/2)]
        return line(*pts)

    def sym(p, a, b, c, d):
        # Orthogonal symmetry of the 16 u square about its centre.
        return p.transform(a, b, c, d, 8-8*a-8*c, 8-8*b-8*d)
    SYMS = [(1,0,0,1),(0,1,-1,0),(-1,0,0,-1),(0,-1,1,0),(-1,0,0,1),(1,0,0,-1),(0,1,1,0),(0,-1,-1,0)]

    def oriented(p, base_first, base_final, first, final):
        # Pick the square symmetry that maps the drawn turn onto the named one.
        for a,b,c,d in SYMS:
            def m(v): return (a*v[0]+c*v[1], b*v[0]+d*v[1])
            if m(VEC[base_first]) == VEC[first] and m(VEC[base_final]) == VEC[final]:
                return sym(p, a, b, c, d)
        raise ValueError((first, final))

    def rpoly(points, r=1.0):
        """Closed polygon with true circular corner radii (SF rounded corners)."""
        n = len(points); rs = r if isinstance(r, (list, tuple)) else [r]*n
        segs = []
        for i, P in enumerate(points):
            A_, B_ = points[i-1], points[(i+1) % n]
            ux, uy = A_[0]-P[0], A_[1]-P[1]; la = math.hypot(ux, uy); ux /= la; uy /= la
            vx, vy = B_[0]-P[0], B_[1]-P[1]; lb = math.hypot(vx, vy); vx /= lb; vy /= lb
            th = math.acos(max(-1, min(1, ux*vx+uy*vy)))
            d = min(rs[i]/math.tan(th/2), la*.49, lb*.49)
            k = 4/3*math.tan((math.pi-th)/4)*d*math.tan(th/2)
            T1 = (P[0]+ux*d, P[1]+uy*d); T2 = (P[0]+vx*d, P[1]+vy*d)
            segs.append((T1, (T1[0]-ux*k, T1[1]-uy*k), (T2[0]-vx*k, T2[1]-vy*k), T2))
        out = 'M%.4f %.4f' % segs[0][0]
        for i, (T1, C1, C2, T2) in enumerate(segs):
            if i: out += 'L%.4f %.4f' % T1
            out += 'C%.4f %.4f %.4f %.4f %.4f %.4f' % (*C1, *C2, *T2)
        return path(out+'Z')

    def arc_pt(cx, cy, r, a):
        return (cx+r*math.cos(math.radians(a)), cy+r*math.sin(math.radians(a)))

    def arc_arrow(cx, cy, r, a0, a1, h=2.8, rx=None):
        """Circular arc from angle a0 to a1 (degrees, screen space) ending in an SF head."""
        rx = r if rx is None else rx
        x0, y0 = cx+rx*math.cos(math.radians(a0)), cy+r*math.sin(math.radians(a0))
        x1, y1 = cx+rx*math.cos(math.radians(a1)), cy+r*math.sin(math.radians(a1))
        sweep = 1 if a1 > a0 else 0
        large = 1 if abs(a1-a0) > 180 else 0
        arc = st(f'M{x0} {y0}A{rx} {r} 0 {large} {sweep} {x1} {y1}')
        s_ = 1 if a1 > a0 else -1
        t = math.radians(a1)
        return union(arc, head(x1, y1, -s_*rx*math.sin(t), s_*r*math.cos(t), h))

    SQ = rr(2.62, 2.62, 10.76, 10.76)   # SF square: 11.8 u ink, 1.7 u outer radius
    CIRC = circle()                     # SF circle: 13.1 u ink
    INNER = .56                         # arrow.right.circle / .square glyph scale

    def portal(name, body, frame, arrow, gap=.9):
        """Container crossed by an arrow (square.and.arrow.up, arrow.up.forward.app).

        Stroke: open frame plus arrow. Duotone: tinted body behind both.
        Solid: filled body with the inside part of the arrow knocked out and the
        outside part continuing in positive ink, as SF .fill does."""
        primary = union(frame, arrow)
        s(name, body, primary)
        filled = union(body, st(body))
        solid = union(sub(filled, arrow), sub(arrow, filled))
        secondary = sub(body, primary)
        api['STYLE_OVERRIDES'][name] = {'duotone': [(secondary, .24), (primary, 1)],
                                        'stroke': primary, 'solid': solid}

    # Long move arrows: the same chevron on a longer shaft, distinct from arrow-*.
    for direction in directions:
        diag = '-' in direction
        if 'move-'+direction in NAMES:
            g('move-'+direction, A(direction, L=16.4 if diag else 13.3, h=3.15 if diag else 3.35))
        name = 'square-arrow-'+direction
        if name in NAMES: s(name, SQ, A(direction, scale=INNER))

    # Enter / exit: SF square.and.arrow.up / .down and arrow.up.forward.app.
    # Drawn once for 'up' and 'up-right', then rotated; enter(d) uses the frame
    # of exit(opposite d) with the arrow reversed.
    straight_frame = 'M5.0 6.45H4.15A1.2 1.2 0 0 0 2.95 7.65V13.25A1.2 1.2 0 0 0 4.15 14.45H11.85A1.2 1.2 0 0 0 13.05 13.25V7.65A1.2 1.2 0 0 0 11.85 6.45H11.0'
    straight_body = rr(2.95, 6.45, 10.1, 8.0)
    diag_frame = 'M7.55 4.6H3.3A1.2 1.2 0 0 0 2.1 5.8V12.7A1.2 1.2 0 0 0 3.3 13.9H10.2A1.2 1.2 0 0 0 11.4 12.7V8.45'
    diag_body = rr(2.1, 4.6, 9.3, 9.3)
    opposite = {'up':'down','down':'up','left':'right','right':'left','up-right':'down-left',
                'down-left':'up-right','up-left':'down-right','down-right':'up-left'}
    for direction, angle in directions.items():
        for behavior in ('enter', 'exit'):
            name = f'square-arrow-{direction}-{behavior}'
            if name not in NAMES: continue
            frame_dir = direction if behavior == 'exit' else opposite[direction]
            diag = '-' in direction
            if diag:
                inner, outer = (6.75, 9.25), (13.75, 2.25)
                frame, body = st(diag_frame), diag_body
                base_angle = directions[frame_dir] - directions['up-right']
                h = 3.05
            else:
                inner, outer = (8, 11.1), (8, 1.5)
                frame, body = st(straight_frame), straight_body
                base_angle = directions[frame_dir] - directions['up']
                h = 2.9
            p0, p1 = (inner, outer) if behavior == 'exit' else (outer, inner)
            arrow = seg(p0, p1, h)
            portal(name, transform(body, base_angle), transform(frame, base_angle), transform(arrow, base_angle))

    # Circle exits: an open ring and an arrow leaving through the gap.
    for direction, angle in directions.items():
        name = f'circle-arrow-{direction}-exit'
        if name not in NAMES: continue
        cx, cy, r = 7.05, 8.95, 5.0
        ring_open = st(f'M{arc_pt(cx,cy,r,-12)[0]} {arc_pt(cx,cy,r,-12)[1]}A{r} {r} 0 1 1 {arc_pt(cx,cy,r,-78)[0]} {arc_pt(cx,cy,r,-78)[1]}')
        arrow = seg((cx, cy), (13.75, 2.25), 3.05)
        rot = directions[direction] - directions['up-right']
        portal(name, transform(circle(cx, cy, r), rot), transform(ring_open, rot), transform(arrow, rot))

    # arrowshape.*: rounded head and shaft, 13.8 x 11.7 u.
    bigshape = rpoly([(1.75, 5.65), (7.75, 5.65), (7.75, 2.75), (14.75, 8), (7.75, 13.25), (7.75, 10.35), (1.75, 10.35)],
                     [1.0, .55, .9, 1.0, .9, .55, 1.0])
    for direction, angle in list(directions.items())[:4]:
        s('arrow-big-'+direction, transform(bigshape, angle))
        dashed = fit(bigshape, 8.665, 8, .82)
        s('arrow-big-'+direction+'-dash', transform(dashed, angle), transform(line((1.6, 6.1), (1.6, 9.9)), angle))
        for container in ('circle', 'square'):
            for double in (False, True):
                name = container+'-'+('chevrons-' if double else 'chevron-')+direction
                if name not in NAMES: continue
                vx, vy = VEC[direction]
                if double:
                    mark = union(chevron(direction, 8-1.55*vx, 8-1.55*vy, 2.75, 2.85),
                                 chevron(direction, 8+1.55*vx, 8+1.55*vy, 2.75, 2.85))
                else:
                    mark = chevron(direction, 8+.15*vx, 8+.15*vy, 3.0, 3.05)
                s(name, CIRC if container == 'circle' else SQ, mark)
    # chevron.left.to.line: the chevron's apex rests on the bar.
    first = union(line((4.55, 2.97), (4.55, 13.03)), chevron('left', 8.0, 8, 5.4, 5.03))
    g('chevron-first', first)
    g('chevron-last', mirror(first))
    g('chevrons-down-up', chevron('down', 8, 3.95, 3.45, 3.75), chevron('up', 8, 12.05, 3.45, 3.75))
    g('chevrons-left-right', chevron('left', 3.85, 8, 4.95, 4.75), chevron('right', 12.15, 8, 4.95, 4.75))

    # Sorting arrows: one SF arrow plus the ordered numerals, letters or bars.
    for direction in ('down','up'):
        for order in ('0-1','1-0','a-z','z-a','narrow-wide','wide-narrow'):
            name = f'arrow-{direction}-{order}'
            arrowpart = A(direction, 4.25, 8, L=11.3, h=3.0)
            if order in ('0-1','1-0'):
                a, b = order.split('-')
                detail = union(number(a, 11.35, 4.55, .44), number(b, 11.35, 11.45, .44))
            elif order in ('a-z','z-a'):
                a, b = order.split('-')
                detail = union(letter(a, 11.35, 4.55, .44), letter(b, 11.35, 11.45, .44))
            else:
                widths = [2.3, 3.9, 5.5] if order == 'narrow-wide' else [5.5, 3.9, 2.3]
                detail = union(*(line((8.75, 3.2+i*4.8), (8.75+w, 3.2+i*4.8)) for i, w in enumerate(widths)))
            g(name, arrowpart, detail)
    # arrow.right.to.line: the apex meets the bar; from-line starts on the bar.
    for direction in ('left','right','up','down'):
        angle = directions[direction]
        for mode in ('from-line','to-line'):
            name = f'arrow-{direction}-{mode}'
            if name not in NAMES: continue
            bar_x = 13.45 if mode == 'to-line' else 2.55
            base = union(line((bar_x, 3.69), (bar_x, 12.31)), seg((2.55, 8), (13.45, 8)))
            g(name, transform(base, angle))
    g('arrow-down-to-dot', seg((8, 1.95), (8, 10.35), 3.6), circle(8, 13.35, 1.05))
    g('arrow-up-from-dot', seg((8, 10.35), (8, 1.95), 3.6), circle(8, 13.35, 1.05))
    g('arrows-up-from-line', seg((4.4, 11.3), (4.4, 2.0), 2.7), seg((11.6, 11.3), (11.6, 2.0), 2.7), line((1.9, 14.0), (14.1, 14.0)))
    g('arrow-down-up', seg((4.5, 2.3), (4.5, 13.7), 3.2), seg((11.5, 13.7), (11.5, 2.3), 3.2))
    g('arrow-right-left', seg((2.3, 4.5), (13.7, 4.5), 3.2), seg((13.7, 11.5), (2.3, 11.5), 3.2))
    # arrow.left.and.right: 11.6 u double-headed shaft, 3.4 u heads.
    g('move-horizontal', seg((2.19, 8), (13.81, 8), 3.41, both=True))
    g('move-vertical', seg((8, 2.19), (8, 13.81), 3.41, both=True))
    g('move-diagonal', seg((2.75, 13.25), (13.25, 2.75), 3.0, both=True))
    g('move-diagonal-2', seg((2.75, 2.75), (13.25, 13.25), 3.0, both=True))
    # arrow.up.right.and.arrow.down.left and its inward counterpart.
    g('maximize-2', seg((9.05, 6.95), (13.6, 2.4), 2.85), seg((6.95, 9.05), (2.4, 13.6), 2.85))
    g('minimize-2', seg((13.6, 2.4), (9.05, 6.95), 2.85), seg((2.4, 13.6), (6.95, 9.05), 2.85))
    for inward in (True, False):
        ends = ((2.3, 2.3), (6.6, 6.6))
        corners = [sym(seg(*(ends if inward else ends[::-1]), 2.45), *m) for m in SYMS[:4]]
        g('shrink' if inward else 'expand', *corners)
    # arrow.turn.*: a short tail that turns on a 3.6 u radius into a full arrow.
    turn = union(st('M13.5 3.5V4.6A3.6 3.6 0 0 1 9.9 8.2H2.5'), head(2.5, 8.2, -1, 0, 4.31))
    for initial in ('down','up','left','right'):
        for final in ('down','up','left','right'):
            name = f'corner-{initial}-{final}'
            if name in NAMES: g(name, oriented(turn, 'down', 'left', initial, final))

    # arrow.uturn.backward: head on top, a semicircular return below.
    uturn = union(st('M2.5 6.85H10.25A3.3 3.3 0 0 1 10.25 13.45H7.2'), head(2.5, 6.85, -1, 0, 4.31))
    for redo in (False, True):
        f = mirror if redo else (lambda p: p)
        prefix = 'redo' if redo else 'undo'
        g(prefix+'-2', f(uturn))
        g(prefix+'-dot', f(union(st('M2.5 6.85H10.25A3.3 3.3 0 0 1 10.25 13.45H8.1'), head(2.5, 6.85, -1, 0, 4.31),
                                circle(4.75, 13.45, 1.0))))
    # arrow.2.circlepath (chevron heads): two arcs whose heads sit just past
    # 3 and 9 o'clock, kept inside the 14.7 u limit.
    circlepath = union(arc_arrow(8, 8, 5.0, 197, 345, 2.4), arc_arrow(8, 8, 5.0, 17, 165, 2.4))
    for clockwise in (False, True):
        base = circlepath if clockwise else mirror(circlepath)
        suffix = 'cw' if clockwise else 'ccw'
        g('refresh-'+suffix, base)
        if clockwise: slash(base, 'refresh-cw-off')
        else: g('refresh-ccw-dot', base, circle(8, 8, 1.05))
        # Iteration: an open loop that straightens into a leftward arrow.
        loop = union(st('M3.65 7.15A4.95 4.95 0 1 1 8.6 12.1H2.45'), head(2.45, 12.1, -1, 0, 2.6))
        g('iteration-'+suffix, loop if clockwise else mirror(loop))
    # repeat: two rounded returns with SF heads.
    repeat = union(st('M2.35 8.7V7.35A2.6 2.6 0 0 1 4.95 4.75H13.15M13.65 7.3V8.65A2.6 2.6 0 0 1 11.05 11.25H2.85'),
                   head(13.15, 4.75, 1, 0, 2.55), head(2.85, 11.25, -1, 0, 2.55))
    g('repeat-2', repeat)
    slash(repeat, 'repeat-off')
    # arrow.right.and.line.vertical.and.arrow.left
    for inward in (True, False):
        left = seg((1.25, 8), (5.95, 8), 3.0) if inward else seg((5.95, 8), (1.25, 8), 3.0)
        g('fold-horizontal' if inward else 'unfold-horizontal', left, mirror(left), line((8, 2.3), (8, 13.7)))

    cat('Layout')
    # Lane D (SF polish). Window chrome follows macwindow / sidebar.left /
    # rectangle.split.*: SF's 15.1 x 11.7 frame scaled to the 14.7 u canvas,
    # 2.4 u outer corner. Square containers use the 11.8 u SF square (SQ).
    WX0, WY0, WW, WH = 1.17, 2.82, 13.66, 10.36
    WX1, WY1 = WX0+WW, WY0+WH
    WIN = rr(WX0, WY0, WW, WH, r=1.9, exact=True)

    def tile(x0, y0, x1, y1, r=.75):
        """Small SF tile from its ink box (outer radius ~1.3 u)."""
        return rr(x0+SW/2, y0+SW/2, x1-x0-SW, y1-y0-SW, r=r, exact=True)

    def vline(x, y0=WY0, y1=WY1):
        return line((x, y0), (x, y1))

    def hline(y, x0=WX0, x1=WX1):
        return line((x0, y), (x1, y))

    def dashes(points, horizontal):
        half = .8 if horizontal else .95
        return union(*(line((x-half, y), (x+half, y)) if horizontal else line((x, y-half), (x, y+half))
                       for x, y in points))

    # --- Alignment family: one canonical drawing (guide vertical, bars
    # horizontal), transposed for the other axis and mirrored for "end".
    def flip_x(p):
        return p.transform(-1, 0, 0, 1, 16, 0)

    GUIDE0, GUIDE1 = 1.25, 14.75
    BAR = 4.0      # SF bar thickness (ink)

    def hbar(x0, x1, yc, thick=BAR):
        return tile(x0, yc-thick/2, x1, yc+thick/2)

    def vbar(y0, y1, xc, thick=BAR):
        return tile(xc-thick/2, y0, xc+thick/2, y1)

    def guide_v(x):
        return line((x, GUIDE0), (x, GUIDE1))

    def align_canonical(position):
        if position == 'center':
            bars = union(hbar(4.55, 11.45, 5.15), hbar(2.2, 13.8, 10.85))
            return bars, sub(guide_v(8), bars)
        bars = union(hbar(2.85, 9.75, 5.15), hbar(2.85, 14.25, 10.85))
        body, rule = bars, guide_v(1.3)
        return (body, rule) if position == 'start' else (flip_x(body), flip_x(rule))

    def justify_canonical(position):
        if position == 'center':
            bars = union(vbar(2.6, 13.4, 4.55, 4.1), vbar(4.4, 11.6, 11.45, 4.1))
            return bars, guide_v(8)
        bars = union(vbar(2.6, 13.4, 4.9, 3.9), vbar(4.4, 11.6, 10.6, 3.9))
        body, rule = bars, guide_v(1.3)
        return (body, rule) if position == 'start' else (flip_x(body), flip_x(rule))

    def distribute_canonical(position):
        if position == 'center':
            bars = union(vbar(3.0, 13.0, 4.3, 4.3), vbar(4.6, 11.4, 11.7, 4.3))
            return bars, sub(union(guide_v(4.3), guide_v(11.7)), bars)
        bars = union(vbar(3.0, 13.0, 4.95, 3.8), vbar(4.6, 11.4, 12.25, 3.8))
        rules = union(guide_v(1.6), guide_v(8.9))
        return (bars, rules) if position == 'start' else (flip_x(bars), flip_x(rules))

    def space_canonical(behavior):
        if behavior == 'between':
            bars = union(vbar(2.6, 13.4, 4.85, 3.9), vbar(4.4, 11.6, 11.15, 3.9))
            return bars, union(guide_v(1.3), guide_v(14.7))
        bars = vbar(3.4, 12.6, 8, 5.0)
        bracket = st('M3.2 1.55H1.55V14.45H3.2')
        return bars, union(bracket, flip_x(bracket))

    for horizontal in (True, False):
        orient = 'horizontal' if horizontal else 'vertical'
        for position in ('start', 'center', 'end'):
            # Lucide align-*-vertical: vertical guide (SF align.horizontal.*).
            body, rule = align_canonical(position)
            if horizontal: body, rule = transpose(body), transpose(rule)
            s(f'align-{position}-{orient}', body, rule)
            for operation, build in (('distribute', distribute_canonical), ('justify', justify_canonical)):
                body, rule = build(position)
                if not horizontal: body, rule = transpose(body), transpose(rule)
                s(f'align-{orient}-{operation}-{position}', body, rule)
        for behavior in ('around', 'between'):
            body, rule = space_canonical(behavior)
            if not horizontal: body, rule = transpose(body), transpose(rule)
            s(f'align-{orient}-space-{behavior}', body, rule)

    # Two panes with an arrow entering the gap between them.
    for horizontal in (True, False):
        for end in (False, True):
            name = 'between-'+('horizontal' if horizontal else 'vertical')+'-'+('end' if end else 'start')
            body = union(vbar(2.1, 13.9, 3.85, 3.5), vbar(2.1, 13.9, 12.15, 3.5))
            detail = sfarrow(8, 2.2, 8, 8.6, 2.15)
            if end: detail = transform(detail, 180)
            if horizontal: body, detail = transpose(body), transpose(detail)
            s(name, body, detail)

    # --- Grids: square.split / rectangle.split construction.
    SQX0, SQY0, SQX1 = 2.6, 2.6, 13.4
    s('grid-2x2', SQ, union(line((8, SQY0), (8, SQX1)), line((SQX0, 8), (SQX1, 8))))
    for status, kind in (('check', 'check'), ('plus', 'plus'), ('x', 'x')):
        s('grid-2x2-'+status, SQ, union(line((8, SQY0), (8, SQX1)), line((SQX0, 8), (SQX1, 8))))
        api['badge']('grid-2x2-'+status, kind)
    thirds = (SQX0+10.8/3, SQX0+21.6/3)
    s('grid-3x3', SQ, union(*(line((x, SQY0), (x, SQX1)) for x in thirds), *(line((SQX0, y), (SQX1, y)) for y in thirds)))
    slashed('grid-3x3-off', SQ, union(*(line((x, SQY0), (x, SQX1)) for x in thirds), *(line((SQX0, y), (SQX1, y)) for y in thirds)))
    col3 = [WX0+WW*i/3 for i in (1, 2)]
    s('grid-3x2', WIN, union(*(vline(x) for x in col3), hline(8)))
    for count in (3, 4):
        s('columns-'+str(count), WIN, union(*(vline(WX0+WW*i/count) for i in range(1, count))))
        s('rows-'+str(count), WIN, union(*(hline(WY0+WH*i/count) for i in range(1, count))))
    gear_center = (12.35, 11.75)
    teeth = []
    for tooth in range(6):
        for phase, radius in ((-.5, 2.3), (-.28, 2.3), (-.22, 3.15), (.22, 3.15), (.28, 2.3)):
            angle = (tooth + phase) * math.pi / 3
            teeth.append((gear_center[0] + radius * math.cos(angle), gear_center[1] + radius * math.sin(angle)))
    cog = sub(poly(teeth), circle(*gear_center, 1.05))
    badged('columns-3-cog', WIN, union(*(vline(x) for x in col3)), cog, circle(*gear_center, 4.05))

    # --- Tiled layouts (square.grid.2x2 / rectangle.grid conventions).
    A0, A1, B0, B1 = 2.1, 7.05, 8.95, 13.9
    s('layout-panel-left', union(tile(A0, A0, A1, B1), tile(B0, A0, B1, A1), tile(B0, B0, B1, B1)))
    s('layout-panel-top', union(tile(A0, A0, B1, A1), tile(A0, B0, A1, B1), tile(B0, B0, B1, B1)))
    s('layout-freeform', union(tile(A0, A0, A1, 8.3), tile(B0, A0, B1, 5.8), tile(A0, 10.2, A1, B1), tile(B0, 7.7, B1, B1)))
    s('layout-grid-circles', union(*(circle(x, y, 2.475) for x in (4.575, 11.425) for y in (4.575, 11.425))))
    three = union(tile(A0, A0, A1, A1), tile(B0, A0, B1, A1), tile(A0, B0, A1, B1))
    s('layout-grid-plus', three, st('M11.425 9.35V13.5M9.35 11.425H13.5'))
    s('layout-arrow-down', three, sfarrow(11.425, 9.1, 11.425, 13.75, 1.75))
    s('layout-arrow-right', three, sfarrow(9.1, 11.425, 13.75, 11.425, 1.75))

    # --- Window chrome: macwindow, dock.rectangle, sidebar.*.
    s('app-window-mac', WIN, dots((3.3, 4.75), (5.1, 4.75), (6.9, 4.75), r=.6))
    s('dock', WIN, rr(3.7, 10.05, 8.6, 1.7, r=.85, exact=True))
    LEFT, RIGHT, TOP, BOTTOM = WX0+4.4, WX1-4.4, WY0+3.3, WY1-3.3
    for side, close, opened in (('right', 'right', 'left'), ('top', 'up', 'down'), ('bottom', 'down', 'up')):
        divider = {'right': vline(RIGHT), 'top': hline(TOP), 'bottom': hline(BOTTOM)}[side]
        center = {'right': ((WX0+RIGHT)/2, 8), 'top': (8, (TOP+WY1)/2), 'bottom': (8, (WY0+BOTTOM)/2)}[side]
        for action, direction in (('close', close), ('open', opened)):
            dx, dy = {'right': (.75, 0), 'left': (-.75, 0), 'up': (0, -.75), 'down': (0, .75)}[direction]
            s(f'panel-{side}-{action}', WIN, union(divider, sfchevron(center[0]+dx, center[1]+dy, direction, 1.6)))
    v_dash = lambda x: dashes(((x, 5.95), (x, 10.05)), False)
    h_dash = lambda y: dashes(((4.4, y), (8, y), (11.6, y)), True)
    for side, mark in (('left', v_dash(LEFT)), ('right', v_dash(RIGHT)), ('top', h_dash(TOP)), ('bottom', h_dash(BOTTOM))):
        s('panel-'+side+'-dashed', WIN, mark)
    s('panel-left-right-dashed', WIN, union(v_dash(LEFT), v_dash(RIGHT)))
    s('panel-top-bottom-dashed', WIN, union(h_dash(TOP), h_dash(BOTTOM)))
    s('panels-left-bottom', WIN, union(vline(LEFT), hline(BOTTOM, LEFT)))
    s('panels-right-bottom', WIN, union(vline(RIGHT), hline(BOTTOM, WX0, RIGHT)))
    s('panels-top-left', WIN, union(hline(TOP), vline(LEFT, TOP)))

    # --- Galleries: a current card with neighbours (rectangle.stack idiom).
    for vertical in (False, True):
        for end in (False, True):
            if end:
                body = tile(1.5, 2.1, 10.3, 13.9, r=1.2)
                extras = st('M12.15 3.45Q12.85 3.75 12.85 4.75V11.25Q12.85 12.25 12.15 12.55'
                            'M14.55 4.75Q14.95 5.05 14.95 5.85V10.15Q14.95 10.95 14.55 11.25')
            else:
                body = tile(3.9, 2.1, 12.1, 13.9, r=1.2)
                extras = union(line((1.4, 3.6), (1.4, 12.4)), line((14.6, 3.6), (14.6, 12.4)))
            if vertical: body, extras = transform(body, 90), transform(extras, 90)
            s('gallery-'+('vertical' if vertical else 'horizontal')+('-end' if end else ''), body, extras)
    s('gallery-thumbnails', union(tile(1.3, 2.1, 14.7, 9.7, r=1.2), tile(1.3, 11.0, 5.3, 13.9, r=.6),
                                  tile(6.0, 11.0, 10.0, 13.9, r=.6), tile(10.7, 11.0, 14.7, 13.9, r=.6)))

    # --- Spacing and sizing.
    for horizontal in (True, False):
        p = union(line((1.3, 2.3), (1.3, 13.7)), line((14.7, 2.3), (14.7, 13.7)),
                  sfarrow(3.3, 8, 6.9, 8, 1.75), sfarrow(12.7, 8, 9.1, 8, 1.75))
        g('gap-'+('horizontal' if horizontal else 'vertical'), p if horizontal else transform(p, 90))
        q = union(sfarrow(8, 8, 4.35, 8, 1.75), sfarrow(8, 8, 11.65, 8, 1.75))
        s('stretch-'+('horizontal' if horizontal else 'vertical'), SQ, q if horizontal else transform(q, 90))
    g('handle-bottom-right', line((5.6, 13.6), (13.6, 5.6)), line((10.1, 13.6), (13.6, 10.1)))
    s('ratio', WIN, st('M3.55 8.1V6.35Q3.55 5.3 4.6 5.3H6.6M12.45 7.9V9.65Q12.45 10.7 11.4 10.7H9.4'))
    s('proportions', WIN, st(rr(6.2, 6.0, 5.6, 4.0, r=.55, exact=True)))
    s('rectangle-horizontal', rr(WX0, WY0, WW, WH))
    s('rectangle-vertical', rr(3.18, 1.66, 9.64, 12.68))
    s('rectangle-ellipsis', rr(1.6, 3.85, 12.8, 8.3), dots((4.75, 8), (8, 8), (11.25, 8), r=.78))

    # --- Margin (space outside content) and padding (space inside a box).
    # Margins: an inset.filled content block, pushed in from the chosen sides.
    # Padding: dashed SF guides inside the container on the chosen sides.
    def sides(spec):
        return ('top', 'bottom', 'left', 'right') if not spec else ('left', 'right') if spec == 'horizontal' \
            else ('top', 'bottom') if spec == 'vertical' else (spec,)
    for name in ('margin', 'margin-top', 'margin-bottom', 'margin-left', 'margin-right', 'margin-horizontal', 'margin-vertical'):
        chosen = sides(name.removeprefix('margin').lstrip('-'))
        inset = {k: (3.15 if k in chosen else 1.55) for k in ('top', 'bottom', 'left', 'right')}
        block = rr(SQX0+inset['left'], SQY0+inset['top'], 10.8-inset['left']-inset['right'],
                   10.8-inset['top']-inset['bottom'], r=.6, exact=True)
        s(name, SQ, block)
    for name in ('square-padding', 'square-padding-top', 'square-padding-bottom', 'square-padding-left',
                 'square-padding-right', 'square-padding-horizontal', 'square-padding-vertical'):
        chosen = sides(name.removeprefix('square-padding').lstrip('-'))
        # Floating content guides, clear of the frame on every side.
        lo, hi = 5.3, 10.7
        guide = {'top': line((lo, lo), (hi, lo)), 'bottom': line((lo, hi), (hi, hi)),
                 'left': line((lo, lo), (lo, hi)), 'right': line((hi, lo), (hi, hi))}
        marks = [guide[side] for side in chosen]
        s(name, SQ, union(*marks))

    cat('Geometry')
    # ---- Lane C helpers: SF slashes and SF dash patterns ----
    SLASH_W = SW + 2*.85   # one full-weight slash behind a 0.85 u clearance

    def c_slash(name, p, start=(2, 2), end=(14, 14)):
        remaining = sub(p, line(start, end, width=SLASH_W))
        g(name, *(part for part in api['components'](remaining) if part.area >= .6), line(start, end))

    def c_cancel(name, body, details, start=(2, 2), end=(14, 14)):
        badged(name, body, details, line(start, end), line(start, end, width=SLASH_W))

    def bez(p0, c1, c2, p1, t):
        u = 1-t
        return (u*u*u*p0[0]+3*u*u*t*c1[0]+3*u*t*t*c2[0]+t*t*t*p1[0],
                u*u*u*p0[1]+3*u*u*t*c1[1]+3*u*t*t*c2[1]+t*t*t*p1[1])

    def flatten(p):
        """Polyline of a closed contour plus the arclength at each corner curve's middle."""
        pts, corners, cur = [], [], None
        for cmd, args in p.segments:
            if cmd == 'moveTo':
                cur = args[0]; pts = [cur]
            elif cmd == 'lineTo':
                q = args[0]; n = max(1, int(math.dist(cur, q)/.05))
                pts += [(cur[0]+(q[0]-cur[0])*i/n, cur[1]+(q[1]-cur[1])*i/n) for i in range(1, n+1)]; cur = q
            elif cmd == 'curveTo':
                c1, c2, q = args
                seg_pts = [bez(cur, c1, c2, q, i/48) for i in range(1, 49)]
                corners.append(len(pts)-1+24)
                pts += seg_pts; cur = q
            elif cmd == 'qCurveTo':
                c, q = args
                pts += [((1-t)**2*cur[0]+2*(1-t)*t*c[0]+t*t*q[0], (1-t)**2*cur[1]+2*(1-t)*t*c[1]+t*t*q[1])
                        for t in (i/24 for i in range(1, 25))]; cur = q
            elif cmd in ('closePath', 'endPath'):
                break
        if math.dist(pts[0], pts[-1]) > 1e-6: pts.append(pts[0])
        acc = [0.0]
        for a, b in zip(pts, pts[1:]): acc.append(acc[-1]+math.dist(a, b))
        return pts, acc, [acc[i] for i in corners]

    def dashed(p, dash=3.0, period=5.4, uniform=None):
        """SF dashed outline: a dash centred on every corner, evenly spaced between."""
        pts, acc, corners = flatten(p)
        total = acc[-1]
        if uniform:
            centers = [total*i/uniform for i in range(uniform)]
        else:
            centers = []
            for i, c in enumerate(corners):
                nxt = corners[(i+1) % len(corners)] + (total if i+1 == len(corners) else 0)
                m = max(1, round((nxt-c)/period))
                centers += [c+(nxt-c)*j/m for j in range(m)]

        def at(s):
            s %= total
            import bisect
            i = min(max(bisect.bisect_right(acc, s)-1, 0), len(pts)-2)
            t = (s-acc[i])/max(acc[i+1]-acc[i], 1e-9)
            return (pts[i][0]+(pts[i+1][0]-pts[i][0])*t, pts[i][1]+(pts[i+1][1]-pts[i][1])*t)
        ds = []
        for c in centers:
            samples = [at(c-dash/2+dash*k/24) for k in range(25)]
            ds.append('M'+'L'.join(f'{x:.4f} {y:.4f}' for x, y in samples))
        return st(''.join(ds))

    # Polygons: SF corner radii on true geometry, measured ink sizes.
    def regular(n, R, rotation, cx=8, cy=8):
        return [(cx+R*math.cos(math.radians(rotation)+2*math.pi*i/n), cy+R*math.sin(math.radians(rotation)+2*math.pi*i/n)) for i in range(n)]
    tri_pts = [(8, 1.05), (14.85, 13.55), (1.15, 13.55)]
    TRIANGLE = rpoly(tri_pts, [1.55, 1.35, 1.35])                 # triangle 13.3 x 12.1
    s('triangle', TRIANGLE)
    s('pentagon', rpoly(regular(5, 6.95, -90, 8, 8.62), 1.25))     # pentagon 13.9 x 13.5
    s('hexagon', rpoly(regular(6, 6.85, -90), 1.1))                 # hexagon 12.9 x 14.3
    OCTAGON = rpoly(regular(8, 6.5, -22.5), 1.0)                     # octagon 13.0
    s('octagon', OCTAGON)
    s('diamond', rpoly([(8, .75), (15.25, 8), (8, 15.25), (.75, 8)], 1.45))
    s('triangle-right', rpoly([(13.55, 2.05), (13.55, 13.55), (2.05, 13.55)], [1.0, 1.2, 1.0]))
    # pause.octagon: the xmark.octagon body with two full-weight bars.
    s('octagon-pause', OCTAGON, union(line((6.4, 5.5), (6.4, 10.5)), line((9.6, 5.5), (9.6, 10.5))))
    # oval scaled from 16 x 12.4 to the 14.7 u limit.
    s('ellipse', path('M1.2 8A6.8 5.18 0 1 1 14.8 8A6.8 5.18 0 1 1 1.2 8Z'))
    # app: the SF app-tile squircle (11.8 u, 3.1 u outer radius).
    SQUIRCLE = rr(2.62, 2.62, 10.76, 10.76, r=2.6, exact=True)
    s('squircle', SQUIRCLE)
    # Dashed primitives stay line-only in all styles (circle.dashed, square.dashed, app.dashed).
    ring_dashes = dashed(circle(8, 8, 5.98), uniform=14, dash=.8)
    g('circle-dashed', ring_dashes)
    s('circle-small', circle(8, 8, 3.9))
    g('circle-dot-dashed', ring_dashes, circle(8, 8, 2.0))
    g('circle-dashed-check', ring_dashes, check(7.75, 8.25, .95))
    g('square-dashed', dashed(rr(2.62, 2.62, 10.76, 10.76)))
    g('squircle-dashed', dashed(SQUIRCLE))
    g('triangle-dashed', dashed(TRIANGLE))
    # sparkle: four concave flanks meeting in softened points; astroid is the
    # thinner cusp curve with flanks pulled to the centre.
    s('astroid', path('M8 1.75Q8 8 14.25 8Q8 8 8 14.25Q8 8 1.75 8Q8 8 8 1.75Z'))
    s('sparkle', path('M8 1.7Q8.95 7.05 14.3 8Q8.95 8.95 8 14.3Q7.05 8.95 1.7 8Q7.05 7.05 8 1.7Z'))
    star_lines = 'M8 5.6V10.4M5.92 6.8L10.08 9.2M5.92 9.2L10.08 6.8'
    g('asterism', *(placed_stroke(star_lines, x, y) for x, y in ((8, 4.1), (4.1, 11.4), (11.9, 11.4))))
    # suit.club / suit.spade at SF size (about 12 u).
    club = union(poly([(8, 4.75), (4.95, 8.95), (11.05, 8.95)]), circle(8, 4.75, 2.65), circle(4.95, 8.95, 2.65), circle(11.05, 8.95, 2.65),
                 path('M7.25 8.6Q7.15 12.15 5.55 13.65H10.45Q8.85 12.15 8.75 8.6Z'))
    s('club', club)
    spade = union(path('M8 1.6L2.8 6.8C-1 11 5 14 8 10C11 14 17 11 13.2 6.8Z'), poly([(8, 9), (5.3, 14.3), (10.7, 14.3)]))
    s('spade', fit(spade, 8, 7.95, .87))
    s('cross', rpoly([(6.2, 1.65), (9.8, 1.65), (9.8, 6.2), (14.35, 6.2), (14.35, 9.8), (9.8, 9.8), (9.8, 14.35),
                      (6.2, 14.35), (6.2, 9.8), (1.65, 9.8), (1.65, 6.2), (6.2, 6.2)],
                     [1.0, 1.0, .45, 1.0, 1.0, .45, 1.0, 1.0, .45, 1.0, 1.0, .45]))
    # smallcircle.filled.circle
    s('circle-dot', CIRC, circle(8, 8, 2.05))
    c_slash('circle-off', st(CIRC))
    s('circle-pile', union(circle(8, 4.45, 2.75), circle(4.5, 10.85, 2.75), circle(11.5, 10.85, 2.75)))
    # angle: base, a 40 degree ray and the measured arc.
    g('angle', line((14.65, 12.85), (1.35, 12.85), (12.9, 3.15)), st('M7.05 12.85A5.7 5.7 0 0 0 5.716 9.186'))
    g('diameter', st(CIRC), line((3.85, 12.15), (12.15, 3.85)))
    g('radius', st(CIRC), line((8, 8), (11.95, 4.05)), circle(8, 8, 1.05))
    g('tangent', st(circle(8, 9.6, 4.3)), line((1.7, 4.78), (14.3, 4.78)))
    g('axis-3d', seg((3.9, 12.1), (3.9, 1.95), 2.4), seg((3.9, 12.1), (14.05, 12.1), 2.4), line((3.9, 12.1), (9.1, 6.9)))
    # cube: rounded hexagon with the Y seam meeting the outline.
    cube_pts = regular(6, 6.65, -90)
    CUBE = rpoly(cube_pts, 1.0)
    cube_seams = st('M%.3f %.3fL8 8L%.3f %.3fM8 8V%.3f' % (*cube_pts[5], *cube_pts[1], cube_pts[3][1]))
    s('box', CUBE, cube_seams)
    def small_box(x, y, scale):
        return union(st(fit(CUBE, x, y, scale)), placed_stroke('M%.3f %.3fL8 8L%.3f %.3fM8 8V%.3f' % (*cube_pts[5], *cube_pts[1], cube_pts[3][1]), x, y, scale))
    g('boxes', small_box(8, 4.6, .49), small_box(4.5, 11.05, .49), small_box(11.5, 11.05, .49))
    s('cuboid', rpoly([(6, 1.8), (14.2, 4.75), (14.2, 11.3), (10, 14.25), (1.8, 11.25), (1.8, 4.7)], .9),
      st('M1.8 4.7L10 7.75L14.2 4.75M10 7.75V14.25'))
    s('cone', path('M7.05 2.55Q8 1.0 8.95 2.55L14.05 11.4A6.05 2.75 0 0 1 1.95 11.4Z'))
    s('pyramid', rpoly([(8, .95), (14.45, 12.05), (8, 14.55), (1.55, 12.05)], [1.0, 1.0, .9, 1.0]), line((8, 2.2), (8, 14.4)))
    s('cylinder', path('M2.99 4.1A5.01 2.3 0 0 1 13.01 4.1V11.9A5.01 2.3 0 0 1 2.99 11.9Z'), st('M2.99 4.1A5.01 2.3 0 0 0 13.01 4.1'))
    # torus: outer oval with the hole drawn as the near and far rims.
    s('torus', path('M1.2 8A6.8 4.65 0 1 1 14.8 8A6.8 4.65 0 1 1 1.2 8Z'), st('M3.6 7.3Q8 10.4 12.4 7.3M5.4 8.31Q8 6.35 10.6 8.31'))
    s('shapes', union(circle(4.6, 4.7, 2.95), rr(7.75, 7.85, 6.3, 6.3), rpoly([(11.55, 1.55), (14.75, 6.95), (8.35, 6.95)], .55)))
    s('component', union(*(transform(rpoly([(8, 1.25), (10.55, 3.8), (8, 6.35), (5.45, 3.8)], .55), a) for a in (0, 90, 180, 270))))
    g('vector-square', st('M4.65 3.05H11.35M12.95 4.65V11.35M11.35 12.95H4.65M3.05 11.35V4.65'), *(outline(rect(x, y, 2.9, 2.9, .8, exact=True)) for x, y in [(1.6, 1.6), (11.5, 1.6), (1.6, 11.5), (11.5, 11.5)]))
    vertices = [(3, 11), (6, 3), (13, 6), (11, 13)]
    handles = union(*(rect(x-1.5, y-1.5, 3, 3) for x, y in vertices))
    g('vector-polygon', sub(line(*vertices, vertices[0]), handles), outline(handles))

    cat('Math and symbols')
    # SF operator metrics: divide 10.6 x 9.4, equal 8.9 x 5.2, notequal 8.9 x 9.1.
    divide = union(line((3.22, 8), (12.78, 8)), dots((8, 4.35), (8, 11.65), r=.95))
    equals = union(line((4.05, 5.92), (11.95, 5.92)), line((4.05, 10.08), (11.95, 10.08)))
    not_slash = line((5.45, 12.55), (10.55, 3.45))
    def tilde_at(y, x0=3.75, x1=12.25, a=1.0):
        k = (x1-x0)/8.5
        def X(v): return x0+(v-3.75)*k
        return st(f'M{X(3.75)} {y+.75*a}C{X(5.15)} {y-1.35*a} {X(6.6)} {y-.95*a} 8 {y}'
                  f'S{X(10.85)} {y+1.35*a} {X(12.25)} {y-.75*a}')
    approximately = union(tilde_at(5.95), tilde_at(10.05))
    sigma = st('M11.25 2.65H4.75L8.75 8L4.75 13.35H11.25')
    def paragraph(x=8, y=8, scale=1):
        bowl = path('M8 2.8V9.6H6.3C1.7 9.6 1.7 2.8 6.3 2.8Z')
        stems = 'M12.7 2.8H7.8V13.2M11.5 2.8V13.2'
        return union(fit(bowl,x,y,scale), placed_stroke(stems,x,y,scale))
    pilcrow = paragraph()
    for name, p in [('divide', divide), ('equal-not', union(equals, not_slash)),
                    ('equal-approximately', approximately),
                    ('equal-approximately-not', union(approximately, not_slash)),
                    ('sigma', sigma), ('pilcrow', pilcrow),
                    ('lambda', st('M3.6 2.35Q5.4 1.55 6.6 4.4L10.6 12.5Q11.6 14.4 13.2 13.1M7.6 6.9L3.4 13.7')),
                    ('omega', st('M3.2 13.35H6.1V11.05C1.2 8.7 2.6 2.1 8 2.1C13.4 2.1 14.8 8.7 9.9 11.05V13.35H12.8')),
                    ('phi', union(st(circle(8, 8, 4.35)), line((8, 1.9), (8, 14.1)))),
                    ('exclamation-mark', union(line((8, 2.45), (8, 9.65)), circle(8, 13.1, .95))),
                    ('question-mark', union(st('M4.75 5.35Q4.75 2.2 8 2.2Q11.25 2.2 11.25 5.1Q11.25 6.9 9.4 7.95Q8 8.75 8 10.2'), circle(8, 13.1, .95)))]:
        g(name, p)
    # scalemass with an approximate tilde: lucide weight-tilde.
    weight_body = rpoly([(3.75, 5.55), (12.25, 5.55), (14.35, 14.35), (1.65, 14.35)], [.9, .9, .9, .9])
    s('weight-tilde', weight_body, union(st(circle(8, 3.15, 1.6)), tilde_at(10.35, 5.2, 10.8, .8)))
    compact_math = {
        'divide': union(line((4.9, 8), (11.1, 8)), dots((8, 5.25), (8, 10.75), r=.8)),
        'equal': st('M5.0 6.5H11.0M5.0 9.5H11.0'),
        'pi': st('M4.65 5.15H11.35M6.6 5.15V9.6Q6.6 10.6 5.75 10.95M9.6 5.15V9.9Q9.6 10.95 10.75 10.95'),
        'sigma': st('M10.55 4.75H5.45L8.25 8L5.45 11.25H10.55'),
        'pilcrow': paragraph(scale=.62),
        'asterisk': placed_stroke(star_lines, scale=1.3),
        'function': st('M10.4 4.85Q8.55 3.95 8.2 6.1L7.65 9.95Q7.35 12.1 5.5 11.25M5.9 7.5H10.2'),
    }
    for symbol, mark in compact_math.items():
        s('square-' + symbol, SQ, mark)
        if symbol in ('divide', 'equal'):
            s('circle-' + symbol, CIRC, mark)
    for i in range(1, 6):
        ps = [line((3.5+j*3, 2.6), (3.5+j*3, 13.4)) for j in range(min(4, i))]
        if i == 5: ps.append(line((1.8, 11.4), (14.2, 4.6)))
        if i < 4: ps = [fit(p, 8+(4-i)*1.5, 8) for p in ps]
        g('tally-'+str(i), *ps)
    amp = 'M12.8 13L5.3 5.8Q2.8 2.2 6.7 1.8Q10.5 1.6 9 4.5L4 8C.5 10.5 4 15.2 8 13.4Q12 11.7 13 8'
    g('ampersand', st(amp))
    g('ampersands', placed_stroke(amp, 4.6, 8, .59), placed_stroke(amp, 11.65, 8, .59))
    section_half = st('M10.7 2.6C7.8 .6 3.4 2.75 5.55 5.05'
                      'C7.05 6.65 11.45 6.8 11.45 9Q11.45 10.3 10.45 10.95')
    g('section', section_half, transform(section_half, 180))
    s('copyleft', CIRC, mirror(letter('c', scale=.58)))
    s('creative-commons', CIRC, union(letter('c', 5.65, 8, .31), letter('c', 10.35, 8, .31)))

    cat('Typography and text')
    for direction in ('up', 'down'):
        y0, y1 = (12.1, 4.4) if direction == 'up' else (4.4, 12.1)
        g('a-arrow-'+direction, word('A', cx=4.7, cap=9.5), sfarrow(12.35, y0, 12.35, y1, 2.55))
    g('a-large-small', word('A', cx=4.55, cap=9.5), word('A', cx=12.0, cap=6.2, baseline=12.23))
    g('case-upper', word('AB', cap=9.5, gap=.8))
    g('case-lower', word('ab', cap=9.5, gap=.8))
    g('case-sensitive', word('Aa', cap=9.5, gap=.7))
    g('baseline', word('A', cy=7.05, cap=8.6), line((2.4, 13.35), (13.6, 13.35)))
    g('letter-spacing', word('A', cx=4.3, cy=5.6, cap=6.4), word('A', cx=11.7, cy=5.6, cap=6.4),
      sfarrow(8, 12.6, 2.1, 12.6, 2.1), sfarrow(8, 12.6, 13.9, 12.6, 2.1))
    g('line-height', sfarrow(3.4, 8, 3.4, 2.3, 2.1), sfarrow(3.4, 8, 3.4, 13.7, 2.1),
      text_rows(((7.6, TX1, 3), (7.6, TX1, 8), (7.6, TX1, 13))))
    g('ligature', st('M4.6 12.23V5.3C4.6 3.55 5.55 2.75 6.95 2.75C7.85 2.75 8.55 3.05 9.05 3.55'
                     'M2.6 6.05H11.1V12.23'), circle(11.1, 3.45, .66))
    for i in (5, 6):
        g('heading-'+str(i), word('H', cx=4.75, cap=9.5), word(str(i), cx=12.05, cap=6.4, baseline=12.23))
    # x at its x-height with a smaller figure below (sub) or above (super).
    g('subscript', word('x', cx=5.35, cy=6.65, cap=9.5), word('2', cx=12.05, cap=5.6, baseline=13.4))
    g('superscript', word('x', cx=5.35, cy=9.35, cap=9.5), word('2', cx=12.05, cap=5.6, baseline=6.6))
    for direction in ('left', 'right'):
        mark = paragraph(8, 6.55, .74)
        tip, tail = (2.6, 13.4) if direction == 'left' else (13.4, 2.6)
        g('pilcrow-'+direction, mark, sfarrow(tail, 13.15, tip, 13.15, 1.9))
    g('remove-formatting', word('T', cx=6.6, cy=6.35, cap=8.3), line((3.4, 13.3), (8.6, 13.3)),
      st('M11.15 10.25L14.05 13.15M14.05 10.25L11.15 13.15'))
    g('spell-check-2', word('Ab', cy=5.6, cap=7.2, gap=.75),
      st('M1.9 12.6Q3.05 10.6 4.2 12.6T6.5 12.6'), check(11.2, 12.15, .62))
    for direction in ('left', 'right'):
        tip, tail = (2.2, 12.9) if direction == 'left' else (13.8, 3.1)
        g('decimals-arrow-'+direction, circle(2.55, 7.45, .66), word('00', cx=9.35, cy=5.15, cap=6.1, gap=.75),
          sfarrow(tail, 12.25, tip, 12.25, 2.3))
    for end in ('center', 'end', 'start'):
        last = {'center': (5.0, 11.0), 'end': (7.5, TX1), 'start': (TX0, 8.5)}[end]
        g('text-align-justify-'+end, text_rows([(TX0, TX1, y) for y in ROWS4[:3]]+[(last[0], last[1], ROWS4[3])]))
    g('summary', text_rows([(TX0, 9.5, ROWS4[0])]+[(TX0, TX1, y) for y in ROWS4[1:3]]+[(TX0, 10.6, ROWS4[3])]))
    g('text-quote', text_rows([(6.4, TX1, ROWS3[0]), (6.4, TX1, ROWS3[1]), (6.4, 11.6, ROWS3[2])]), line((2.6, 2.95), (2.6, 13.05)))
    g('text-wrap', text_rows([(TX0, TX1, 3.2), (TX0, 4.3, 12.8)]),
      st('M2.05 8H11.2C12.85 8 13.95 9.1 13.95 10.4C13.95 11.7 12.85 12.8 11.2 12.8H7.4'),
      st('M9.25 10.95L7.4 12.8L9.25 14.65'))
    g('text-initial', word('A', cx=4.35, cy=5.85, cap=7.4),
      text_rows([(9.6, TX1, 3.1), (9.6, TX1, 7.2), (TX0, TX1, 12.9)]))
    g('whole-word', word('ab', cy=6.3, cap=8.2, gap=.75), st('M2.05 10.95V12.2Q2.05 13.4 3.25 13.4H12.75Q13.95 13.4 13.95 12.2V10.95'))
    g('space', st('M2.05 6.6V9.2Q2.05 10.4 3.25 10.4H12.75Q13.95 10.4 13.95 9.2V6.6'))
    g('type-outline', st('M6.75 2.15H9.25L14.35 13.85H11.55L10.4 11.05H5.6L4.45 13.85H1.65ZM8 5.15L6.45 8.85H9.55Z'))
    field = rr(1.65, 4.35, 12.7, 7.3)
    caret = st('M6.25 1.85H9.75M8 1.85V14.15M6.25 14.15H9.75')
    badged('text-cursor-input', field, empty, caret, rect(6.4, 0, 3.2, 16, 0))
    g('text-search', text_rows(((TX0, TX1, 3), (TX0, 7.6, 8), (TX0, 5.6, 13))),
      ring(11.35, 10.1, 2.55), line((13.2, 11.95), (14.4, 13.15)))
    pen=path('M2 11L11.5 1.5L14.5 4.5L5 14H1.5Z')
    def pencil_body(x, y):
        return fit(path('M4.7 9.7L10.7 3.7L13 6L7 12L3.7 13Z'), x, y, .62)

    def pencil_mark(x, y):
        return outline(pencil_body(x, y))

    def pencil_clearance(x, y):
        body = pencil_body(x, y)
        return union(body, outline(body, 3.2))

    g('text-pen', text_rows(((TX0, TX1, 3), (TX0, 8.6, 8), (TX0, 5.6, 13))), sfpencil(7.9, 13.55, -45, 8.9))
    g('table-of-contents', text_rows([(TX0, 9.6, y) for y in ROWS3]), dots(*((13.2, y) for y in ROWS3), r=.75))
    g('list-check', text_rows([(6.6, TX1, y) for y in ROWS3]), check(3.15, 8.1, .58))
    for behavior in ('down-up', 'up-down'):
        first, second = ('down', 'up') if behavior == 'down-up' else ('up', 'down')
        g('list-chevrons-'+behavior, text_rows([(7.2, TX1, y) for y in ROWS3]),
          sfchevron(3.4, 5.55 if first == 'down' else 3.85, first, 1.55),
          sfchevron(3.4, 10.45 if second == 'up' else 12.15, second, 1.55))
    g('list-collapse', text_rows([(7.2, TX1, y) for y in ROWS3]), sfchevron(4.75, 8, 'right', 2.0))
    g('list-start', text_rows(((7.6, TX1, ROWS3[0]), (TX0, TX1, ROWS3[1]), (TX0, TX1, ROWS3[2]))), sfarrow(2.05, 4, 5.6, 4, 1.8))
    g('list-end', text_rows(((TX0, TX1, ROWS3[0]), (TX0, TX1, ROWS3[1]), (7.6, TX1, ROWS3[2]))), sfarrow(2.05, 12, 5.6, 12, 1.8))
    g('list-restart', text_rows(((TX0, TX1, 3), (TX0, 8.4, 8), (TX0, 5.6, 13))),
      st('M13.75 13.2A2.85 2.85 0 1 1 13.95 9.55'), st('M11.95 9.65H14.05V7.55'))
    g('list-filter-plus', text_rows(((TX0, TX1, 3.4), (3.9, 12.1, 7.4), (5.8, 8.6, 11.4))),
      st('M12.15 9.6V13.9M10 11.75H14.3'))
    # Replace controls use actual text groups and directed exchange routes.
    g('replace', word('A', cx=4.35, cy=5.05, cap=6.6), word('B', cx=11.55, cy=10.95, cap=6.6),
      st('M8.9 2.85H10.4Q12.05 2.85 12.05 4.5V6.75'), sfchevron(12.05, 6.75, 'down', 1.5))
    g('replace-all', word('A', cx=3.7, cy=4.65, cap=5.4), word('A', cx=3.7, cy=11.35, cap=5.4),
      sfarrow(6.55, 8, 9.45, 8, 1.55), word('B', cx=12.75, cy=8, cap=5.4))
    # Horizontal link halves (Lucide link-2) in SF capsule proportions.
    half = st('M6.2 4.75H4.75A3.25 3.25 0 0 0 4.75 11.25H6.2')
    g('unlink-2', half, mirror(half))
    slashed('link-2-off', empty, union(half, mirror(half), line((5.7, 8), (10.3, 8))), outline_body=False)
    cat('Documents and books')
    # Lane D (SF polish): book.closed, book, clipboard and note conventions.
    BX0, BY0, BX1, BY1 = 3.12, 1.67, 12.88, 14.33   # book.closed ink 10.8 x 13.7
    PAGE_Y, SPINE_X = 11.55, 5.35
    book_body = path(f'M{BX0+1.35} {BY0}H{BX1-1.5}Q{BX1} {BY0} {BX1} {BY0+1.5}V{PAGE_Y+.35}'
                     f'Q{BX1} {PAGE_Y+1.05} {BX1-.55} {PAGE_Y+1.35}Q{BX1-.95} {BY1-.6} {BX1-.25} {BY1}'
                     f'H{BX0+1.6}Q{BX0} {BY1} {BX0} {BY1-1.6}V{BY0+1.35}Q{BX0} {BY0} {BX0+1.35} {BY0}Z')
    book_lines = st(f'M{SPINE_X} {BY0}V{PAGE_Y}M{BX1-.55} {PAGE_Y+.05}H{SPINE_X-.1}'
                    f'Q{BX0} {PAGE_Y} {BX0} {PAGE_Y+1.6}')
    cover = ((SPINE_X+BX1)/2, (BY0+PAGE_Y)/2)
    for name, detail in [('book-a', word('A', cx=cover[0], cy=cover[1], cap=4.7)),
                         ('book-type', word('T', cx=cover[0], cy=cover[1], cap=4.7)),
                         ('book-bookmark', st(f'M8.1 {BY0}V7.6L9.55 6.45L11.0 7.6V{BY0}')),
                         ('book-exclamation-point', union(line((cover[0], 4.15), (cover[0], 7.35)), circle(cover[0], 9.05, .68)))]:
        s(name, book_body, union(book_lines, detail))
    # A second copy recedes behind the front book (books.vertical spacing).
    front_book = fit(book_body, 9.0, 9.35, .84)
    s('book-copy', front_book, union(fit(book_lines, 9.0, 9.35, .84),
                                     st('M2.0 11.9V3.15Q2.0 1.6 3.55 1.6H10.6')))
    open_book = path('M8 4.05C6.65 2.85 4.75 2.4 2.95 2.6Q1.35 2.8 1.35 4.3V11.35Q1.35 12.6 2.65 12.45'
                     'C4.6 12.25 6.6 12.65 8 13.45C9.4 12.65 11.4 12.25 13.35 12.45Q14.65 12.6 14.65 11.35'
                     'V4.3Q14.65 2.8 13.05 2.6C11.25 2.4 9.35 2.85 8 4.05Z')
    spine = line((8, 4.1), (8, 13.2))
    s('book-open-text', open_book, union(spine, st('M3.65 6.05Q4.95 5.85 5.95 6.35M3.65 8.85Q4.95 8.65 5.95 9.15'
                                                   'M12.35 6.05Q11.05 5.85 10.05 6.35M12.35 8.85Q11.05 8.65 10.05 9.15')))
    s('book-open-check', open_book, union(spine, check(11.15, 7.9, .5)))
    # Discrete books on a shelf: two upright, one leaning (books.vertical).
    s('library-big', union(tile(1.3, 3.5, 5.0, 13.9, r=.6), tile(5.75, 2.1, 9.45, 13.9, r=.6),
                           transform(tile(10.35, 2.6, 14.05, 13.9, r=.6), -10, dx=-.75, dy=.35)),
      union(line((1.82, 5.9), (4.48, 5.9)), line((6.27, 4.5), (8.93, 4.5)), line((6.27, 11.5), (8.93, 11.5))))
    s('square-library', SQ, st('M5.4 5.4V10.6M8.0 5.4V10.6M10.05 5.6L11.25 10.45'))

    # Notebooks share the book.closed footprint with binding tabs on the spine.
    nb_body = rr(3.85, BY0, 9.03, BY1-BY0, r=1.35, exact=True)
    nb_tabs = union(*(line((2.25, y), (5.15, y)) for y in (4.6, 8, 11.4)))
    s('notebook-dot', nb_body, union(nb_tabs, circle(9.15, 8, 1.15)))
    s('notebook-text', nb_body, union(nb_tabs, text_rows(((7.0, 10.9, 5.3), (7.0, 10.9, 8), (7.0, 9.4, 10.7)))))
    nb_pen = sfpencil(8.6, 11.15, -45, 9.4, 2.05)
    nb_lines = union(nb_tabs, text_rows(((7.0, 10.9, 5.3), (7.0, 9.4, 8))))
    badged('notebook-pen', nb_body, nb_lines, nb_pen, pencil_cut(nb_pen))

    # Notepad: ring binding across the top edge (note.text proportions).
    pad = rr(2.6, 3.05, 10.8, 11.3)
    pad_rings = union(*(line((x, 1.55), (x, 4.6)) for x in (5.3, 8, 10.7)))
    pad_text = text_rows(((5.1, 10.9, 7.4), (5.1, 10.9, 9.9), (5.1, 8.9, 12.25)))
    s('notepad-text', pad, union(pad_rings, pad_text))
    g('notepad-text-dashed', pad_rings, pad_text,
      st('M2.6 5.9V4.25Q2.6 3.05 3.8 3.05M12.2 3.05Q13.4 3.05 13.4 4.25V5.9'
         'M2.6 8.15V9.75M13.4 8.15V9.75M2.6 12.0V13.15Q2.6 14.35 3.8 14.35H5.6'
         'M7.2 14.35H8.8M10.4 14.35H12.2Q13.4 14.35 13.4 13.15V12.0'))

    # Clipboard: board behind a solid clip, separated by SF clearance.
    board = rr(3.05, 2.75, 9.9, 11.6)
    clip = union(rr(5.45, 1.9, 5.1, 2.35, r=.85, exact=True), circle(8, 1.55, 1.0))
    clip_ring = op(clip, circle(8, 1.55, .42), po.PathOp.DIFFERENCE)
    clip_gap = union(clip, outline(clip, 1.7))
    badged('clipboard-type', board, word('T', cx=8, cy=9.0, cap=5.2), clip_ring, clip_gap)
    cb_pen = sfpencil(9.0, 12.1, -45, 8.6, 2.05)
    badged('clipboard-pen-line', board, union(text_rows(((5.35, 8.8, 7.0), (5.35, 7.2, 9.6))),),
           union(clip_ring, cb_pen), union(clip_gap, pencil_cut(cb_pen)))

    # Tables: tablecells chrome with header row / columns.
    third_y = (WY0+WH/3, WY0+2*WH/3)
    third_x = (WX0+WW/3, WX0+2*WW/3)
    s('sheet', WIN, union(*(hline(y) for y in third_y), *(vline(x, third_y[0]) for x in third_x)))
    s('table-2', WIN, union(hline(third_y[0]), vline(third_x[0])))
    s('table-properties', WIN, union(vline(third_x[0]), hline(8),
                                     text_rows(((7.25, 11.5, 5.4), (7.25, 10.2, 10.6)))))
    for horizontal in (True, False):
        if horizontal:
            body = union(tile(1.3, 2.1, 7.05, 13.9, r=1.2), tile(8.95, 2.1, 14.7, 13.9, r=1.2))
            detail = union(*(line((1.82, y), (6.53, y)) for y in (6.05, 9.95)), *(line((9.47, y), (14.18, y)) for y in (6.05, 9.95)))
        else:
            body = union(tile(1.3, 2.1, 14.7, 7.05, r=1.2), tile(1.3, 8.95, 14.7, 13.9, r=1.2))
            detail = union(*(line((x, 2.62), (x, 6.53)) for x in (5.85, 10.15)), *(line((x, 9.47), (x, 13.38)) for x in (5.85, 10.15)))
        s('table-'+('columns' if horizontal else 'rows')+'-split', body, detail)

    # Sticky note: SF square with a folded lower-right corner.
    note = path('M3.8 2.6H12.2Q13.4 2.6 13.4 3.8V9.85L9.85 13.4H3.8Q2.6 13.4 2.6 12.2V3.8Q2.6 2.6 3.8 2.6Z')
    note_fold = st('M9.85 13.3V11.05Q9.85 9.85 11.05 9.85H13.3')
    nc = (7.55, 7.55)
    for status, detail in [('plus', st(f'M{nc[0]} {nc[1]-2.1}V{nc[1]+2.1}M{nc[0]-2.1} {nc[1]}H{nc[0]+2.1}')),
                           ('minus', line((nc[0]-2.1, nc[1]), (nc[0]+2.1, nc[1]))),
                           ('x', st(f'M{nc[0]-1.55} {nc[1]-1.55}L{nc[0]+1.55} {nc[1]+1.55}M{nc[0]+1.55} {nc[1]-1.55}L{nc[0]-1.55} {nc[1]+1.55}')),
                           ('check', check(nc[0]-.1, nc[1]+.1, .6))]:
        s('sticky-note-'+status, note, union(note_fold, detail))
    slashed('sticky-note-off', note, union(note_fold, text_rows(((5.0, 10.2, 6.2), (5.0, 8.4, 8.9)))))
    front_note = fit(note, 9.2, 9.2, .86)
    s('sticky-notes', front_note, union(fit(note_fold, 9.2, 9.2, .86),
                                        st('M1.85 11.0V3.05Q1.85 1.85 3.05 1.85H11.0')))

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
    slashed('pen-off', *api['DRAWINGS']['pen'][:2])
    # SF pencil (pencil, pencil.line, pencil.slash, square.and.pencil): one
    # slim solid bar with a sharpened tip and a separated end cap.
    g('pencil-line', sfpencil(2.75, 11.35, -45, 12.6), line((5.4, 13.75), (13.75, 13.75)))
    def sparkle_at(x, y, radius):
        sparkle = path('M8 4Q8.7 7.3 12 8Q8.7 8.7 8 12Q7.3 8.7 4 8Q7.3 7.3 8 4Z')
        return fit(sparkle,x,y,radius/4)

    slashed('pencil-off', empty, sfpencil(3.0, 13.0, -45, 14.1), outline_body=False)
    g('pencil-sparkles', sfpencil(2.9, 13.1, -45, 13.4), sparkle_at(4.15, 4.15, 2.35), sparkle_at(12.15, 11.95, 1.85))
    # SF paintbrush.pointed: slim pill handle, short ferrule, a swept bristle
    # tip. Authored along +x from the tip, then laid on the 45-degree axis.
    def on_axis(p, tx=2.05, ty=13.95):
        a = math.radians(-45); c, s_ = math.cos(a), math.sin(a)
        return p.transform(c, s_, -s_, c, tx, ty)
    bristle = path('M0 .35C1.1 .05 2.1 -1.05 3.25 -1.55Q3.85 -1.8 4.5 -1.8H5.6V1.55H4.5C3.0 1.55 1.6 1.15 0 .35Z')
    handle = path('M5.6 -1.15H14.65A1.15 1.15 0 0 1 14.65 1.15H5.6Z')
    s('brush', on_axis(union(bristle, handle)), on_axis(st('M5.6 -1.55V1.55M7.25 -1.15V1.15')))
    # Flat brush (paintbrush) stood upright: pill handle, neck, bristle block.
    flat = union(rr(6.6, 1.45, 2.8, 5.3, r=1.4), rr(7.05, 6.3, 1.9, 1.8, r=0), rr(3.6, 8.0, 8.8, 6.4, r=1.0, exact=True))
    s('paintbrush-vertical', flat, union(line((3.6, 10.15), (12.4, 10.15)), line((6.55, 12.0), (6.55, 14.4)), line((9.45, 12.0), (9.45, 14.4))))
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
    g('wand-sparkles',wand, sparkle_at(4.1,3.7,1.9), sparkle_at(12.8,11.9,1.55))
    s('slice', path('M1.6 13.5L3.7 8.9L5.4 7.2L7.3 7.2L11.9 2.6Q13.2 1.3 14.2 2.7Q15 3.8 13.8 5L8.3 10.5L6.9 10.6Z'),
      st('M5.4 7.2L8.3 10.5M9.8 4.7L12.2 7.1'))
    g('signature',st('M1.5 11C6 14 8-1 5.5 2C3 5 4.5 14 7 11L9 8Q9 14 11 10Q12 7 13 9Q13.5 11 15 9'),line((3,14),(13,14)))
    g('line-squiggle',st('M1.5 11C5-2 2 17 8 8C14-1 9 17 14.5 5'))
    g('line-style',line((2,3),(14,3)),line((2,8),(7,8)),line((10,8),(14,8)),dots((2.5,13),(6.2,13),(9.9,13),(13.6,13),r=.6))
    # SF curvepath: two ring end points joined by one calm S curve.
    g('spline', st('M5.4 12.55C9.7 12.3 6.3 3.7 10.6 3.45'), ring(3.85, 12.6, 1.6), ring(12.15, 3.4, 1.6))
    pointer2=poly([(2.5,1.8),(13.8,8),(8.5,9),(6.8,14.3)])
    g('spline-pointer', st('M4.75 10.6C8.6 10.4 5.4 3.4 12.7 3.3'), ring(3.2, 10.65, 1.6), cursor_at(8.9, 8.35, .56))
    # SF lasso: an open oval loop whose tail drops through a small knot.
    loop = 'M4.35 10.5C1.55 9.4 1.2 6.5 2.75 4.65C4.4 2.65 7.55 1.95 10.35 2.45C13.55 3.0 15.1 5.35 14.15 7.6C13.15 9.95 9.95 11.05 6.75 10.75'
    g('lasso', st(loop+'C5.5 10.6 4.45 11.05 4.4 11.95C4.35 13.0 5.4 13.55 6.2 14.2'))
    lasso_cursor = cursor_at(9.6, 7.55, .56)
    lasso_line = st('M4.35 10.5C1.55 9.4 1.2 6.5 2.75 4.65C4.4 2.65 7.55 1.95 10.35 2.45C13.55 3.0 15.1 5.35 14.15 7.0'
                    'M7.3 10.85C6.0 10.65 4.6 11.0 4.45 12.0C4.35 13.0 5.4 13.55 6.2 14.2')
    g('lasso-select', sub(lasso_line, union(lasso_cursor, outline(lasso_cursor, 1.8))), lasso_cursor)
    g('frame', st('M4.6 2.2V13.8M11.4 2.2V13.8M2.2 4.6H13.8M2.2 11.4H13.8'))
    handles = union(*(transform(st('M2.6 4.7V3.4Q2.6 2.6 3.4 2.6H4.7'), a)
                      for a in (0, 90, 180, 270)))
    front = rr(7.6, 7.6, 3.9, 3.9, r=.75, exact=True)
    rear_group = rr(4.5, 4.5, 3.9, 3.9, r=.75, exact=True)
    g('group', handles, sub(outline(rear_group), union(front, outline(front, 2.7))), outline(front))
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
            body = path('M1.55 12.35L6.35 3.15A1.86 1.86 0 0 1 9.65 3.15'
                      'L14.45 12.35L11.65 13.8L8 6.8L4.35 13.8Z')
        elif join=='miter': body=path('M.8 12.3L8 .5L15.2 12.3L12.6 13.7L8 6L3.4 13.7Z')
        else: body=path('M1 12L6.5 2.5H9.5L15 12L12.5 13.5L8 5.8L3.5 13.5Z')
        # Optical size: the same 11.8 u footprint as the SF square.
        g('stroke-line-join-'+join, fit(body, 8, 8.75, .82))
    # Boolean operation symbols display the actual result inside the two
    # source outlines; this avoids arbitrary diagonal marks on identical boxes.
    a,b=PAIR_BACK,PAIR_FRONT
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
            contextual = st('M1.72 6.0V2.92Q1.72 1.72 2.92 1.72H6.0M14.28 10.0V13.08Q14.28 14.28 13.08 14.28H10.0')
        elif mode=='subtract': contextual=st('M14.28 9.2V13.08Q14.28 14.28 13.08 14.28H9.2')
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
            sheetpiece=outline(fit(plane,6.6,6.0,.8))
            if count==2: sheetpiece=union(sheetpiece,st('M1.4 8.85L6.6 11.65L9.0 10.35'))
            y0, y1 = (7.3, 14.0) if direction == 'down' else (14.0, 7.3)
            g(name, sheetpiece, sfarrow(12.85, y0, 12.85, y1, 2.05))
    lower_sheet_line = st('M1.5 9L8 12.5L14.5 9')
    g('layers-2', planestroke, lower_sheet_line)
    # SF badge slot: the mark sits in a clearance cut from the lower sheet.
    for action, mark in [('plus', st('M12.55 9.95V14.25M10.4 12.1H14.7')),
                         ('minus', line((10.4, 12.1), (14.7, 12.1)))]:
        clearance = union(mark, outline(mark, 2*.9), circle(12.55, 12.1, 2.15+.9))
        kept = [part for part in api['components'](sub(union(planestroke, lower_sheet_line), clearance)) if part.area >= 1.5]
        g('layers-'+action, *kept, mark)
    rear,front=PAIR_BACK,PAIR_FRONT
    for name,foreground,background in [('bring-to-front',front,rear),('send-to-back',rear,front)]:
        g(name,sub(outline(background),union(foreground,outline(foreground,2.7))),foreground,outline(foreground))
    s('square-square', SQ, st(rr(5.4, 5.4, 5.2, 5.2, r=.75, exact=True)))
    # SF square.stack: a front square with two receding sheets above it.
    g('square-stack', st(rr(3.0, 5.35, 10.0, 9.0)), st('M4.65 3.35H11.35M6.1 1.45H9.9'))
    # SF minus.square.on.square: the shared copy pair with the mark centred
    # in the front square at full weight (copy-slash uses the same pair).
    for status in ('minus','slash'):
        mark = (api['badge_mark']('minus',9.7,9.7,3.4) if status=='minus'
                else line((8.15,11.25),(11.25,8.15)))
        api['stacked']('copy-'+status,api['copy_back'],api['copy_front'],mark,'duplicate copy '+status)
        made.add('copy-'+status)
    # Two crossing rings (camera.filters construction); the shared lens is the blend.
    blend_l, blend_r = circle(5.55, 8, 4.25), circle(10.45, 8, 4.25)
    blend_rings = union(ring(5.55, 8, 4.75), ring(10.45, 8, 4.75))
    g('blend', blend_rings)
    api['DUOTONE_GLYPHS']['blend'] = 'The overlap of the two sources is the blended surface.'
    api['STYLE_OVERRIDES']['blend'] = {
        'duotone': [(sub(inter(blend_l, blend_r), blend_rings), .24), (blend_rings, 1)],
        'solid': union(sub(circle(5.55, 8, 4.75), circle(10.45, 8, 4.75+.9)), circle(10.45, 8, 4.75)),
        'stroke': blend_rings}
    s('opacity',circle(),inter(circle(),rect(8,2,6,12,0)))
    # Keep the halftone plane within the circular body in all styles.
    opacity_primary=union(inter(circle(),rect(8,2,6,12,0)),outline(circle()))
    api.setdefault('STYLE_OVERRIDES',{})['opacity']={
        'duotone':[(sub(inter(circle(),rect(2,2,6,12,0)),opacity_primary),.24),(opacity_primary,1)],
        'solid':union(outline(circle()),inter(circle(),rect(8,2,6,12,0))),
        # SF circle.lefthalf.filled is itself the Regular drawing: ring plus half.
        'stroke':opacity_primary}
    for horizontal in (True,False):
        name='square-centerline-dashed-'+('horizontal' if horizontal else 'vertical')
        divider=st('M8 1.6V4.3M8 6.8V9.2M8 11.7V14.4')
        square_divider = st('M8 2.6V4.4M8 7.1V8.9M8 11.6V13.4')
        s(name, SQ, transform(square_divider,90) if horizontal else square_divider)
        triangles=union(outline(poly([(2,3),(6,8),(2,13)])),outline(poly([(14,3),(10,8),(14,13)])),divider)
        g('triangles-centerline-dashed-'+('horizontal' if horizontal else 'vertical'),transform(triangles,90) if horizontal else triangles)
    for horizontal in (True,False):
        s('square-split-'+('horizontal' if horizontal else 'vertical'), SQ, line((2.6,8),(13.4,8)) if horizontal else line((8,2.6),(8,13.4)))
    s('square-round-corner', SQ, st('M5.4 10.6V8.6Q5.4 5.4 8.6 5.4H10.6'))
    s('square-dimensions', rr(2.0, 2.0, 8.9, 8.9), st('M2.0 13.55H10.9M2.0 12.5V14.6M10.9 12.5V14.6M13.55 2.0V10.9M12.5 2.0H14.6M12.5 10.9H14.6'))
    s('square-text', SQ, text_rows(((5.3, 10.7, 5.4), (5.3, 10.7, 8), (5.3, 8.7, 10.6))))
    s('square-menu', SQ, text_rows(((5.3, 10.7, 5.4), (5.3, 10.7, 8), (5.3, 10.7, 10.6))))
    s('square-code', SQ, union(sfchevron(5.1, 8, 'left', 1.85), sfchevron(10.9, 8, 'right', 1.85)))
    sq_pen = sfpencil(6.0, 10.0, -45, 11.4)
    badged('square-pen', SQ, empty, sq_pen, pencil_cut(sq_pen))
    # SF cursorarrow: a solid arrow cursor with a tail.
    s('square-mouse-pointer', SQ, cursor_at(6.0, 4.85, .56))
    slashed('square-off', SQ, empty)

    # SF square.dashed at the 11.8 u square: rounded corner arcs and one
    # centred dash per side, all at the family weight.
    def sq_dashed():
        x0, y0, x1, y1, r = 2.6, 2.6, 13.4, 13.4, api['RADIUS']
        ext = .9
        corner = st(f'M{x0} {y0+r+ext}V{y0+r}Q{x0} {y0} {x0+r} {y0}H{x0+r+ext}')
        corners = union(corner, flip_x(corner), corner.transform(1, 0, 0, -1, 0, 16), corner.transform(-1, 0, 0, -1, 16, 16))
        return union(corners, line((7.1, y0), (8.9, y0)), line((7.1, y1), (8.9, y1)),
                     line((x0, 7.1), (x0, 8.9)), line((x1, 7.1), (x1, 8.9)))
    sq_cursor = cursor_at(7.75, 7.0, .62)
    for name, p in [('square-dashed-plus', st('M8 5.6V10.4M5.6 8H10.4')),
                    ('square-dashed-x', st('M6.25 6.25L9.75 9.75M9.75 6.25L6.25 9.75')),
                    ('square-dashed-search', union(ring(10.0, 10.0, 2.65), line((11.95, 11.95), (14.15, 14.15)))),
                    ('square-dashed-mouse-pointer', sq_cursor)]:
        frame = sq_dashed()
        if name.endswith(('search', 'mouse-pointer')):
            frame = union(*(part for part in api['components'](sub(frame, union(p, outline(p, 2*.9)))) if part.area >= .5))
        g(name, frame, p)
    corner_x = st('M11.25 11.25L13.85 13.85M13.85 11.25L11.25 13.85')
    g('square-dashed-x-corner', sub(sq_dashed(), rect(9.6, 9.6, 6.4, 6.4, 0)), corner_x)
    g('square-dashed-top-solid', sub(sq_dashed(), rect(0, 0, 16, 5.5, 0)),
      st('M2.6 4.7V3.8Q2.6 2.6 3.8 2.6H12.2Q13.4 2.6 13.4 3.8V4.7'))
    def scissors_mark(x, y, scale):
        r = 2.15 * scale
        left = x - 4 * scale
        handles = union(outline(circle(left,y-4*scale,r)), outline(circle(left,y+4*scale,r)))
        blades = placed_stroke('M5.5 5.5L14 13M5.5 10.5L14 3', x, y, scale)
        return union(handles, blades)

    s('square-scissors', SQ, scissors_mark(8.1, 8, .56))
    g('scissors-line-dashed',scissors_mark(6.4,8,.77),st('M10.4 8H11.6M13.9 8H14.7'))
    g('square-bottom-dashed-scissors', st('M2.6 10.4V3.8Q2.6 2.6 3.8 2.6H12.2Q13.4 2.6 13.4 3.8V10.4'),
      st('M2.6 13.4H4.0M7.3 13.4H8.7M12.0 13.4H13.4'),
      scissors_mark(8.05, 6.55, .5))

    cat('Maps and travel')
    badge = api['badge']
    world, meridians = api['DRAWINGS']['globe'][:2]
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

    # SF badges: a filled disc with the mark knocked out, behind a 0.9 u gap.
    def disc_badge(name, mark, cx=11.85, cy=11.85, r=3.25):
        api['BADGES'][name] = (sub(circle(cx, cy, r), mark), circle(cx, cy, r+api['BADGE_GAP']))

    def ban_mark(cx=11.85, cy=11.85):
        return union(st(circle(cx, cy, 1.95)), line((cx-1.3, cy-1.3), (cx+1.3, cy+1.3)))

    def code_mark(cx=11.85, cy=11.85):
        return union(chevron('left', cx-1.45, cy, .95, 1.5), chevron('right', cx+1.45, cy, .95, 1.5))

    for state, kind in [('check', 'check'), ('plus', 'plus'), ('x', 'x')]:
        s('globe-'+state, world, meridians); badge('globe-'+state, kind)
    s('globe-ban', world, meridians); disc_badge('globe-ban', ban_mark())
    s('globe-code', world, meridians); disc_badge('globe-code', code_mark())
    c_cancel('globe-off', world, meridians)
    map_body, folds = api['DRAWINGS']['map'][:2]
    for state in ('plus', 'minus'):
        s('map-'+state, map_body, folds); badge('map-'+state, state)

    # map-pin family: the base teardrop; status badges sit bottom-right,
    # object marks (house, pen, magnifier) clear the pin like SF composites.
    base_pin, eye = api['DRAWINGS']['map-pin'][:2]
    x0, y0, x1, y1 = eye.bounds
    head_x, head_y = (x0+x1)/2, (y0+y1)/2
    for state, p in [('check', check(head_x+.1, head_y+.25, .82)), ('minus', line((head_x-2.15, head_y), (head_x+2.15, head_y))),
                     ('plus', plus(head_x, head_y, 1.05)), ('x', cross(head_x, head_y, .82))]:
        s('map-pin-'+state+'-inside', base_pin, p)
    for state in ('check', 'minus'):
        s('map-pin-'+state, base_pin, eye); badge('map-pin-'+state, state)
    for state, p in [('house', st('M10.05 11.75L12.25 9.75L14.45 11.75V14.35H10.05Z')),
                     ('pen', pencil_mark(11.5, 11.5)),
                     ('search', union(outline(circle(11.85, 11.55, 1.95)), line((13.3, 13.0), (14.6, 14.3))))]:
        badged('map-pin-'+state, base_pin, eye, p, union(circle(12.2, 12.0, 3.2), outline(p, 2.1)))
    pin_body = fit(base_pin, 8, 5.7, .64)
    pin_eye = circle(8, 4.7, 1.28)
    pin_ink = union(outline(pin_body), outline(pin_eye))
    pin_clearance = union(pin_body, outline(pin_body, 3.2))
    mappoly = path('M1.8 3.5L6 1.8L10 3.5L14.2 1.8V12.5L10 14.2L6 12.5L1.8 14.2Z')
    map_base = fit(mappoly, 8, 9.85, .77)
    map_folds = placed_stroke('M6 1.8V12.5M10 3.5V14.2', 8, 9.85, .77)
    map_edge = outline(map_base)
    primary = union(sub(union(map_edge, map_folds), pin_clearance), pin_ink)
    field = union(sub(map_base, pin_clearance), pin_body)
    map_fill = union(map_base, map_edge)
    map_solid = sub(map_fill, inter(map_folds, sub(map_fill, outline(map_fill, 1.8))))
    s('map-pinned', field)
    api['STYLE_OVERRIDES']['map-pinned'] = {
        'duotone': [(sub(field, primary), .24), (primary, 1)],
        'stroke': primary,
        'solid': union(sub(map_solid, pin_clearance),
                       sub(union(pin_body, outline(pin_body)), pin_eye))}
    s('land-plot', rpoly([(1.6, 9), (6.5, 2.5), (14.4, 6.6), (9.5, 13.1)], .9), st('M4.05 5.75L11.95 9.85M10.45 4.55L5.55 11.05'))
    # signpost.right board (rounded point) on a post; signpost-big is
    # signpost.right.and.left: two boards on one post.
    def board(x0, x1, y0, y1, point=2.6, right=True):
        pts = [(x0, y0), (x1-point, y0), (x1, (y0+y1)/2), (x1-point, y1), (x0, y1)]
        r = [1.0, .8, .7, .8, 1.0]
        if not right:
            pts = [(16-x, y) for x, y in pts]
        return rpoly(pts, r)
    s('milestone', board(1.9, 14.3, 3.3, 9.3), union(line((8, 1.4), (8, 3.3)), line((8, 9.3), (8, 14.6))))
    big_boards = union(board(5.6, 14.3, 2.1, 6.5), board(5.6, 14.3, 7.9, 12.3, right=False))
    s('signpost-big', big_boards, union(line((8, 6.5), (8, 7.9)), line((8, 12.3), (8, 14.6)), line((5.6, 14.6), (10.4, 14.6))))
    route_line, route_stops = api['DRAWINGS']['route'][:2]
    start_stop = min(api['components'](route_stops), key=lambda part: part.bounds[0])
    g('route-arrow-right', route_line, start_stop, seg((11.0, 13.05), (14.15, 13.05), 1.65))
    c_slash('route-off', union(route_line, route_stops))
    c_slash('locate-off', st('M8 3A5 5 0 1 0 8 13A5 5 0 1 0 8 3M8 1.3V4M8 12V14.7M1.3 8H4M12 8H14.7'))
    g('radar', outline(circle()), outline(circle(8, 8, 3)), line((8, 8), (12.24, 3.76)), circle(4.1, 10.3, .65))
    # location.north: a narrow arrowhead, 10 x 13.3 u.
    north = rpoly([(8, 1.25), (13.15, 14.0), (8, 11.45), (2.85, 14.0)], [.9, 1.0, .6, 1.0])
    s('navigation-2', north)
    c_cancel('navigation-2-off', north, empty)
    navigation, heading = api['DRAWINGS']['navigation'][:2]
    c_cancel('navigation-off', navigation, heading)
    # Cursor: the lucide pointer with SF corner radii.
    cursor = rpoly([(2.55, 1.85), (13.85, 7.95), (8.55, 9.0), (6.75, 14.3)], [.9, 1.0, .55, 1.0])
    s('mouse-pointer-2', cursor)
    c_cancel('mouse-pointer-2-off', cursor, empty)
    s('mouse-pointer-ban', cursor); disc_badge('mouse-pointer-ban', ban_mark())
    # Hands: original SF-like construction from finger capsules on a palm with a
    # rounded heel (hand.point.up / hand.raised proportions); finger gaps are
    # short full-weight lines that become counters in Solid.
    def capsule(p0, p1, w):
        return st(path(f'M{p0[0]} {p0[1]}L{p1[0]} {p1[1]}'), w, exact=True)
    def hand_body(fingers, thumb, palm):
        return union(*(capsule((x, top+w/2), (x, 10.5), w) for x, top, w in fingers), capsule(*thumb), palm)
    pointer_fingers = [(6.15, 1.3, 2.5), (8.55, 5.55, 2.3), (10.8, 6.25, 2.2), (12.75, 7.35, 1.7)]
    hand = hand_body(pointer_fingers, ((5.6, 11.3), (3.05, 8.35), 2.45),
                     rr(4.9, 8.2, 8.7, 6.35, 3.1, exact=True))
    s('pointer', hand, st('M7.4 7.35V9.55M9.7 8.0V9.65M11.9 8.95V9.85'))
    c_cancel('pointer-off', *api['DRAWINGS']['pointer'][:2])
    grab_fingers = [(4.85, 3.35, 2.4), (7.25, 2.45, 2.4), (9.65, 2.75, 2.4), (11.95, 3.9, 2.2)]
    grab = hand_body(grab_fingers, ((4.6, 11.5), (2.6, 8.75), 2.4),
                     rr(3.65, 6.6, 9.4, 7.95, 3.4, exact=True))
    s('hand-grab', grab, st('M6.05 4.65V7.15M8.45 3.9V7.15M10.85 4.25V7.15M4.3 8.4Q8.4 9.55 12.95 8.4'))
    wheel = outline(circle(8, 5.9, 4.4))
    cabins = union(*(outline(rect(x - 1.4, 7.4, 2.8, 2.8)) for x in (2.7, 13.3)))
    spokes = st('M8 1.5V5.9M3.6 5.9H12.4')
    hangers = st('M3.6 5.9H2.7V7.4M12.4 5.9H13.3V7.4')
    supports = st('M4.7 14.4L8 5.9L11.3 14.4M3.5 14.4H12.5')
    g('ferris-wheel', wheel, cabins, spokes, hangers, supports)
    track = 'M1.55 10.8C4.4 10.8 3.8 3.15 7.35 3.15C10.6 3.15 10.4 10.65 13 10.65Q13.95 10.65 14.65 9.55'
    g('roller-coaster', st(track), st('M3.35 9.45V13.9M7.35 3.15V13.9M12.25 10.35V13.9'))

    cat('Transform and flow')
    # Flow diagrams: three SF-radius nodes joined by rounded connectors.
    nodes = union(rr(1.6, 1.75, 4.3, 3.5), rr(10.1, 1.75, 4.3, 3.5), rr(5.85, 10.75, 4.3, 3.5))
    connector = st('M3.75 5.25V6.65A1.35 1.35 0 0 0 5.1 8H10.9A1.35 1.35 0 0 0 12.25 6.65V5.25M8 8V10.75')
    for vertical in (False, True):
        name = 'diagram-flow-'+('vertical' if vertical else 'horizontal')
        s(name, nodes if vertical else transform(nodes, 90), connector if vertical else transform(connector, 90))
    # move.3d (filled heads), scale.3d (filled end caps), rotate.3d (sphere).
    origin = (8, 8.6)
    ends = [(8, 2.3), (2.55, 11.75), (13.45, 11.75)]
    axes = union(*(line(origin, e) for e in ends))
    def tri_head(tip, frm, size=2.15):
        ux, uy = tip[0]-frm[0], tip[1]-frm[1]; n = math.hypot(ux, uy); ux, uy = ux/n, uy/n
        base = (tip[0]-ux*size*1.15, tip[1]-uy*size*1.15)
        return rpoly([(tip[0]+ux*.35, tip[1]+uy*.35), (base[0]+uy*size*.85, base[1]-ux*size*.85),
                      (base[0]-uy*size*.85, base[1]+ux*size*.85)], .35)
    g('move-3d', axes, *(tri_head(e, origin) for e in ends))
    g('scale-3d', axes, *(rr(e[0]-1.45, e[1]-1.45, 2.9, 2.9, .7, exact=True) for e in ends))
    sphere = circle()
    g('rotate-3d', st(sphere), st('M8 2.05A2.7 5.95 0 0 0 8 13.95'), st('M2.05 8.35A5.95 2.35 0 0 0 13.95 8.35'))
    for cw in (False, True):
        # rotate.right: a square with a hooked arrow above it.
        p = rr(6.35, 6.75, 7.8, 7.8)
        hook = union(st('M2.6 9.4V6.05A3 3 0 0 1 5.6 3.05H8.1'), head(8.1, 3.05, 1, 0, 1.85))
        name = 'rotate-'+('cw' if cw else 'ccw')+'-square'
        s(name, p if cw else mirror(p), hook if cw else mirror(hook))
    # clock.arrow.circlepath, turning clockwise.
    g('rotate-cw-clock', arc_arrow(7.4, 8.15, 5.0, 60, 360, 2.3), st('M7.4 5.15V8.15L9.25 9.3'))
    # A small square scaled out to the full frame (lucide scaling, SF metrics).
    s('scaling', rr(2.1, 7.9, 6.0, 6.0),
      union(st('M2.1 5.15V3.3A1.2 1.2 0 0 1 3.3 2.1H5.15M10.85 13.9H12.7A1.2 1.2 0 0 0 13.9 12.7V10.85'),
            seg((8.1, 7.9), (13.9, 2.1), 2.6)))
    brackets = st('M2.2 5.35V4.2A2 2 0 0 1 4.2 2.2H5.35M10.65 2.2H11.8A2 2 0 0 1 13.8 4.2V5.35'
                  'M13.8 10.65V11.8A2 2 0 0 1 11.8 13.8H10.65M5.35 13.8H4.2A2 2 0 0 1 2.2 11.8V10.65')
    g('scan-box', brackets, small_box(8, 8, .5))
    g('view', brackets, st('M4.0 8Q8 2.9 12 8Q8 13.1 4.0 8Z'), circle(8, 8, 1.35))
    funnel, funnel_seam = api['DRAWINGS']['filter'][:2]
    for state, kind in [('plus', 'plus'), ('x', 'x')]:
        s('funnel-'+state, funnel, funnel_seam); badge('funnel-'+state, kind, 12.0, 12.0, 3.1)
    s('search-exclamation-point', circle(6.7, 6.7, 4.7), union(line((10.3, 10.3), (14, 14)), line((6.7, 4.1), (6.7, 6.85)), circle(6.7, 9.0, .62)))
    s('search-slash', circle(6.7, 6.7, 4.7), union(line((10.3, 10.3), (14, 14)), line((5.0, 8.4), (8.4, 5.0))))
    # Pinwheel loader: a ring with three curved blades from the hub.
    blade = st('M8 6.65C8.2 4.85 9.55 3.75 11.35 3.6')
    s('loader-pinwheel', CIRC, union(st(circle(8, 8, 1.35)), *(transform(blade, a) for a in (0, 120, 240))))
    fading_ring = union(st('M8 2.02A5.98 5.98 0 1 1 2.02 8'), dots((2.55, 5.15), (4.95, 2.85), r=.62))
    g('circle-fading-arrow-up', fading_ring, A('up', scale=INNER))
    # arrow.clockwise.icloud with the backup (counterclockwise) turn.
    cloud = api['DRAWINGS']['cloud'][0]
    # The flatter SF cloud leaves no room for a readable circular arrow
    # inside, so the backup turn rides in an SF badge disc, knocked out.
    s('cloud-backup', cloud)
    turn = mirror(arc_arrow(8, 8.25, 1.45, -40, 265, 1.05)).transform(1, 0, 0, 1, 3.85, 3.6)
    api['BADGES']['cloud-backup'] = (sub(circle(11.85, 11.85, 3.25), turn), circle(11.85, 11.85, 4.15))
    keyboard_body, keys = api['DRAWINGS']['keyboard'][:2]
    c_cancel('keyboard-off', fit(keyboard_body, scale=.997), keys)
    # tray.and.arrow.down, scaled into the 14.7 u limit.
    tray = path('M4.85 4.55Q3.95 4.55 3.55 5.4L1.75 9.6V12.9Q1.75 14.2 3.05 14.2H12.95Q14.25 14.2 14.25 12.9V9.6L12.45 5.4Q12.05 4.55 11.15 4.55')
    tray_lip = st('M1.75 9.6H5.25Q5.75 11.55 8 11.55Q10.25 11.55 10.75 9.6H14.25')
    g('import', st(tray), tray_lip, seg((8, 1.55), (8, 9.4), 2.6))

    missing=set(NAMES)-made
    extra=made-set(NAMES)
    assert not missing, 'Unimplemented design names: '+', '.join(sorted(missing))
    assert not extra, 'Unassigned design names: '+', '.join(sorted(extra))
