"""Original product-interface additions, drawn on the CXL 16-unit grid."""

import math


def register(api):
    shape, glyph = api['shape'], api['glyph']
    path, rr, circle = api['path'], api['rr'], api['circle']
    stroke, line, lines, union = api['stroke'], api['line'], api['lines'], api['union']
    transform, dots = api['transform'], api['dots']
    check, plus, cross = api['check'], api['plus'], api['cross']
    api['CATEGORY'] = 'Interface controls'

    op, po = api['op'], api['po']
    overrides = api['STYLE_OVERRIDES']

    def subtract(a, b):
        return op(a, b, po.PathOp.DIFFERENCE)

    def gear(x, y, radius):
        # Six broad, flat teeth leave room for a circular bore at badge size.
        points = []
        for tooth in range(6):
            for angle, reach in ((-30, .74), (-20, .74), (-13, 1), (13, 1), (20, .74)):
                theta = math.radians(60 * tooth + angle)
                points.append((x + radius * reach * math.cos(theta),
                               y + radius * reach * math.sin(theta)))
        return subtract(api['poly'](points), circle(x, y, radius * .34))

    def stack(name, back, front, detail, tags):
        front = api['soften'](front)
        back = api['soften'](back)
        ink = union(subtract(stroke(back, 1.25), front), stroke(front, 1.25), detail)
        surface = union(back, front)
        shape(name, surface, ink, tags)
        overrides[name] = {'duotone': [(subtract(surface, ink), .24), (ink, 1)],
                           'stroke': ink, 'solid': api['stacked_solid'](back, front, detail)}

    def compact(kind, x=8, y=8, scale=1):
        def position(p):
            return p.transform(scale,0,0,scale,x-8*scale,y-8*scale)

        if kind == 'dot':
            return circle(x,y,.9)
        if kind == 'user':
            return union(circle(x,y-1.65*scale,1.04*scale),
                         stroke(position(path('M5.7 10.5Q6 8.9 8 8.9Q10 8.9 10.3 10.5')),1.17))
        if kind == 'pen':
            return position(api['poly']([(5.25,10.8),(5.75,8.6),(9.8,4.55),(11.45,6.2),(7.4,10.25)]))
        if kind == 'lock':
            return union(position(rr(5.35,8,5.3,3.6,.65)),
                         stroke(position(path('M6.25 8V6.45A1.75 1.75 0 0 1 9.75 6.45V8')),1.13))
        if kind in ('info','exclamation-point','question-mark'):
            geom = {'info':'M8 7.2V10.7','exclamation-point':'M8 5.1V8.35',
                    'question-mark':'M6.2 6.1Q6.45 4.8 8 4.8C10.4 4.8 10.45 7 9 7.8Q8 8.4 8 8.8'}[kind]
            dot_y = {'info':4.75,'exclamation-point':10.95,'question-mark':11.35}[kind]
            return union(stroke(position(path(geom)),1.22),circle(x,y+(dot_y-8)*scale,.69))
        if kind == 'heart':
            return position(path('M8 11.2L5.35 8.7C2.9 6.25 5.85 3.95 8 6.2C10.15 3.95 13.1 6.25 10.65 8.7Z'))
        if kind == 'key':
            return union(stroke(position(circle(6.45,6.45,1.65)),1.15),
                         stroke(position(path('M7.7 7.7L11.5 11.5L12.6 10.4M9.9 9.9L11.1 8.7')),1.2))
        paths = {
            'check':'M5.4 8L7.3 9.85L10.7 6.15', 'x':'M6 6L10 10M10 6L6 10',
            'plus':'M5.7 8H10.3M8 5.7V10.3', 'minus':'M5.7 8H10.3',
            'text':'M5.75 6.65H10.25M5.75 9.35H9.45',
            'clock':'M5.15 8A2.85 2.85 0 1 0 10.85 8A2.85 2.85 0 1 0 5.15 8M8 6.45V8L9 8.55',
            'search':'M5 7.1A2.1 2.1 0 1 0 9.2 7.1A2.1 2.1 0 1 0 5 7.1M8.65 8.65L11 11',
            'arrow-left':'M5.4 8H10.6M7.6 5.8L5.4 8L7.6 10.2',
            'arrow-right':'M5.4 8H10.6M8.4 5.8L10.6 8L8.4 10.2',
            'arrow-up':'M8 5.4V10.6M5.8 7.6L8 5.4L10.2 7.6',
            'arrow-down':'M8 5.4V10.6M5.8 8.4L8 10.6L10.2 8.4',
            'chevrons-left':'M7.5 5.9L5.4 8L7.5 10.1M11.1 5.9L9 8L11.1 10.1',
            'chevrons-right':'M4.9 5.9L7 8L4.9 10.1M8.5 5.9L10.6 8L8.5 10.1',
            'sync':'M4.85 7.7A3.2 3.2 0 0 1 10.8 6.7M10.9 5V6.95H9M11.15 8.3A3.2 3.2 0 0 1 5.2 9.3M5.1 11V9.05H7',
            '1':'M6.7 6.25L8.2 5.15V10.8M6.7 10.8H9.7',
        }
        width = 1.18 if kind in ('clock','search','sync','text','chevrons-left','chevrons-right') else 1.25
        return stroke(position(path(paths[kind])),width)

    def mark(kind, x=8, y=8, scale=1):
        # Compact symbols are deliberately drawn for their available interior.
        if kind == 'cog':
            return gear(x, y, 2.75 if scale < .74 else 2.9)
        p = {
            'check': 'M5.8 8L7.3 9.5L10.3 6.5',
            'x': 'M6 6L10 10M10 6L6 10',
            'plus': 'M5.7 8H10.3M8 5.7V10.3',
            'minus': 'M5.7 8H10.3',
            'dot': None,
            'exclamation-point': 'M8 5.5V8.5M8 10.5V10.6',
            'question-mark': 'M6.3 6.4Q6.4 4.8 8 4.8Q10 4.8 10 6.4Q10 7.3 8 8.3V9M8 11V11.1',
            'info': 'M8 7.4V10.5M8 5.3V5.4',
            'search': 'M6.4 8A1.8 1.8 0 1 0 10 8A1.8 1.8 0 1 0 6.4 8M9.4 9.4L11 11',
            'clock': 'M5.5 8A2.5 2.5 0 1 0 10.5 8A2.5 2.5 0 1 0 5.5 8M8 6.5V8L9 8.8',
            'heart': 'M8 10.5L5.8 8.5Q4.6 7.1 5.8 6.2Q6.9 5.4 8 6.7Q9.1 5.4 10.2 6.2Q11.4 7.1 10.2 8.5Z',
            'user': 'M6.8 6.3A1.2 1.2 0 1 0 9.2 6.3A1.2 1.2 0 1 0 6.8 6.3M5.8 10.5Q6 8.5 8 8.5Q10 8.5 10.2 10.5',
            'lock': 'M6 8H10V11H6ZM6.8 8V6.7Q6.8 5.3 8 5.3Q9.2 5.3 9.2 6.7V8',
            'key': 'M5.5 7A1.5 1.5 0 1 0 8.5 7A1.5 1.5 0 1 0 5.5 7M8 8L10.7 10.7M9.6 9.6L10.5 8.7',
            'pen': 'M5.8 10.4L6.4 8.7L9.7 5.4L10.8 6.5L7.5 9.8Z',
            'arrow-left': 'M5.5 8H10.5M5.5 8L7.3 6.2M5.5 8L7.3 9.8',
            'arrow-right': 'M5.5 8H10.5M10.5 8L8.7 6.2M10.5 8L8.7 9.8',
            'arrow-up': 'M8 5.5V10.5M8 5.5L6.2 7.3M8 5.5L9.8 7.3',
            'arrow-down': 'M8 5.5V10.5M8 10.5L6.2 8.7M8 10.5L9.8 8.7',
            'chevrons-left': 'M7.6 6L5.6 8L7.6 10M10.4 6L8.4 8L10.4 10',
            'chevrons-right': 'M5.6 6L7.6 8L5.6 10M8.4 6L10.4 8L8.4 10',
            'sync': 'M5.7 7Q6.3 5.2 8 5.2Q9.6 5.2 10.4 6.6M10.4 5.4V6.8H9M10.3 9Q9.7 10.8 8 10.8Q6.4 10.8 5.6 9.4M5.6 10.6V9.2H7',

            'text': 'M5.7 6H10.3M5.7 8H10.3M5.7 10H9',
            '1': 'M7.2 6L8.5 5V11M7 11H10',
        }[kind]
        q = circle(8, 8, .8) if kind == 'dot' else stroke(p, 1.05)
        return q.transform(scale, 0, 0, scale, x-8*scale, y-8*scale)

    # Shared silhouettes: interior variants are kept within the surface rather
    # than allowing the status symbol to collide with the outline.
    badge = api['badge_body']()
    shape('badge', badge, None, 'award seal')
    for suffix in ('exclamation-point','info','minus','plus','x'):
        shape('badge-'+suffix, badge, compact(suffix), 'award seal '+suffix)

    book = rr(3, 1.6, 10, 12.8, 1)
    for suffix in ('check','heart','lock','minus','plus','search','text','user','x'):
        shape('book-'+suffix, book, union(stroke('M5 2V11M3.2 11.2H12.8',1), compact(suffix,9,6.7,.86)), 'book '+suffix)
    bookmark = path('M4 2H12V14L8 11L4 14Z')
    for suffix in ('minus','x'):
        shape('bookmark-'+suffix, bookmark, compact(suffix,8,6.5,.84), 'bookmark '+suffix)
    shape('bookmark-off', bookmark, line((2,2),(14,14)), 'bookmark disabled')

    cal = rr(2.2,3,11.6,10.6,1.3)
    top = stroke('M2.5 6H13.5M5 1.7V4.1M11 1.7V4.1',1.1)
    for suffix in ('1','arrow-down','arrow-left','arrow-right','arrow-up','chevrons-left','chevrons-right','cog','minus','search','sync'):
        shape('calendar-'+suffix, cal, union(top, gear(8,9.85,2.45) if suffix == 'cog' else compact(suffix,8,9.7,.84)), 'calendar date '+suffix)
    # The numbered versions denote marks placed outside the date grid.
    for suffix in ('check','minus','plus','x'):
        small = rr(1.8,3,8,8.8,1.1)
        if suffix == 'minus':
            shape('calendar-minus-2',cal,union(top,line((5.7,9.8),(10.3,9.8),width=1.25)),'calendar date minus')
        else:
            shape('calendar-'+suffix+'-2', small, union(stroke('M2 5.8H9.6M4 1.8V4M7.6 1.8V4',1.05),compact(suffix,12.35,12.35,.8)), 'calendar date '+suffix)
    shape('calendar-off', cal, union(top,line((2,2),(14,14))), 'calendar disabled')
    turned = path('M3.5 3H12.5Q13.8 3 13.8 4.3V9.2L9.4 13.6H3.5Q2.2 13.6 2.2 12.3V4.3Q2.2 3 3.5 3Z')
    shape('calendar-fold', turned, union(top, stroke('M9.4 13.6V10.3Q9.4 9.2 10.5 9.2H13.8',1.2)), 'calendar folded date')
    stack('calendars', rr(1.7,1.9,9.6,9.7,1.3), rr(4.6,4.8,9.7,9.4,1.3),
          stroke('M4.6 8H14.3M7 3.7V6M11.9 3.7V6',1.2), 'multiple dates calendars')

    # Clock faces use independently calculated hands for each hour.
    for hour in range(1,13):
        angle = math.pi*hour/6
        length = 3.65 if hour in (1,11) else 2.8
        hx, hy = 8+length*math.sin(angle), 8-length*math.cos(angle)
        shape('clock-'+str(hour), circle(8,8,6), union(stroke(f'M8 4.2V8L{hx:.3f} {hy:.3f}',1.08 if hour in (1,11) else 1.15),circle(8,8,.97) if hour == 6 else None), 'time hour '+str(hour))
    for suffix in ('arrow-down','arrow-left','arrow-right','arrow-up','check','exclamation-point','plus'):
        shape('clock-'+suffix, circle(6.5,7,4.8), union(stroke('M6.5 4.2V7L8.3 8',1.05), compact(suffix,12.2,12,.82)), 'time '+suffix)
    glyph('clock-fading', stroke('M13.5 8A5.5 5.5 0 0 1 8 13.5M2.5 8A5.5 5.5 0 0 1 8 2.5A5.5 5.5 0 0 1 13.5 8M8 4.5V8L10.3 9.3'), dots((3.3,11),(5.3,13),r=.6), 'time history fading')

    clip = rr(3,3,10,11,1.4)
    cliptop = rr(5.5,1.6,5,2.8,.8)
    for suffix in ('clock','minus','plus','x','pen'):
        shape('clipboard-'+suffix, clip, union(cliptop,compact(suffix,8,9,.96)), 'clipboard '+suffix)
    shape('clipboard-list',clip,union(cliptop,stroke('M5.3 6.6H5.5M7.8 6.6H10.7M5.3 8.95H5.5M7.8 8.95H10.7M5.3 11.3H5.5M7.8 11.3H10.7',1)), 'clipboard checklist')
    shape('clipboard-copy',clip,union(cliptop,stroke('M5.2 7.6V10.7M5.2 7.6H8.8M7.5 9.5H10.9V12.4H7.5Z',1)), 'clipboard copy')
    shape('clipboard-paste',clip,union(cliptop,stroke('M8 6V10M6.5 8.5L8 10L9.5 8.5M5.5 11.5H10.5',1)), 'clipboard paste')

    card = rr(1.7,3.5,12.6,9,1.4)
    for suffix in ('check','minus','plus','x'):
        shape('credit-card-'+suffix, card, union(stroke('M2 6H14',1),mark(suffix,10.3,9.2,.65)), 'payment credit card '+suffix)
    for suffix in ('check','plus','x'):
        shape('copy-'+suffix, union(rr(2,2,8,9,1),rr(5,5,9,9,1)), union(stroke('M5 6V13Q5 14 6 14H13Q14 14 14 13V6Q14 5 13 5H6Q5 5 5 6Z',1),mark(suffix,9.5,9.5,.65)), 'duplicate copy '+suffix)

    # Geometric controls and mathematical notation are opaque glyphs.
    glyph('asterisk',lines('M8 2V14','M2.8 5L13.2 11','M2.8 11L13.2 5'),None,'star wildcard')
    glyph('brackets',lines('M6 2H3.5V14H6','M10 2H12.5V14H10'),None,'code square brackets')
    glyph('equal',lines('M3 6H13','M3 10H13'),None,'math equality')
    glyph('math-pi',lines('M2.5 4H13.5','M5.5 4V12Q5.5 13.5 4.5 14','M10.5 4V12Q10.5 13.5 12 13.5'),None,'math pi')
    glyph('code-xml',lines('M5.5 4L2 8L5.5 12','M10.5 4L14 8L10.5 12','M9 2L7 14'),None,'code markup xml')
    glyph('arrow-down-to-line',lines('M8 2V10.5','M5 7.5L8 10.5L11 7.5','M3 13.5H13'),None,'download arrow line')
    glyph('arrow-up-to-line',lines('M8 13.5V5','M5 8L8 5L11 8','M3 2H13'),None,'upload arrow line')
    glyph('check-line',union(check(6,7,.8),line((9,12),(14,12))),None,'complete check line')
    glyph('x-line-top',union(cross(8,9,.9),line((3,2),(13,2))),None,'close cross line')
    glyph('chart-bar-horizontal',lines('M2.5 2V14H14','M5 4H10','M5 7H13','M5 10H8'),None,'chart horizontal bars')
    glyph('chart-column-stacked',lines('M2 14H14','M4 13V4H6.5V13','M9 13V2H11.5V13','M4 8H6.5','M9 7H11.5'),None,'chart stacked columns')
    glyph('chart-scatter',union(lines('M2.5 2V13.5H14'),dots((5,10),(7,6),(9,9),(11,4),(13,7),r=.75)),None,'chart scatter points')

    api['CATEGORY'] = 'Files and folders'
    doc = path('M3 1.8H9L13 5.8V14.2H3Z')
    fold = stroke('M9 1.8V5.8H13',1.05)
    # File interior symbols are authored on the grid below the folded corner.
    doc_details = {
        'axis-3d':'M7 11.5V7M7 11.5L4.8 10M7 11.5L10 10M7 7L6 8M7 7L8 8',
        'badge':'M8 7L9 7.6L10.2 7.6L10.6 8.8L11.2 9.8L10.5 10.8L10.2 12L9 12.2L8 13L7 12.2L5.8 12L5.5 10.8L4.8 9.8L5.4 8.8L5.8 7.6L7 7.6Z',
        'box':'M5 9L8 7.4L11 9V12L8 13.5L5 12ZM5 9L8 10.5L11 9M8 10.5V13.5',
        'braces':'M7 7H6V9L5.2 10L6 11V13H7M9 7H10V9L10.8 10L10 11V13H9',
        'braces-corner':'M7 7H6V9L5.2 10L6 11V13H7M9 7H10V9L10.8 10L10 11V13H9',
        'chart-column':'M5 12.5V10M8 12.5V7.5M11 12.5V9',
        'chart-column-increasing':'M5 12.5V11M8 12.5V9M11 12.5V7',
        'chart-line':'M5 12V8M5 12H11M6 10.5L8 9L9 10L11 7.5',
        'chart-pie':'M8 7A3 3 0 1 0 11 10H8ZM9 7V9H11',
        'check-corner':'M5.5 10L7.2 11.8L10.8 8',
        'clock':'M5.2 10A2.8 2.8 0 1 0 10.8 10A2.8 2.8 0 1 0 5.2 10M8 8.3V10L9 10.7',
        'code-corner':'M7 8L5 10L7 12M9 8L11 10L9 12',
        'cog':'M8 7V8M8 12V13M5 10H6M10 10H11M6.5 8.5L7 9M9 11L9.5 11.5M9.5 8.5L9 9M7 11L6.5 11.5M6.8 10A1.2 1.2 0 1 0 9.2 10A1.2 1.2 0 1 0 6.8 10',
        'database':'M5 8C5 6.5 11 6.5 11 8V12C11 13.5 5 13.5 5 12ZM5 8C5 9.5 11 9.5 11 8M5 10C5 11.5 11 11.5 11 10',
        'diff':'M5 8H8M6.5 6.5V9.5M8.5 12H11',
        'digit':'M5.5 8L7 7V12M5.5 12H8.5M9 8Q9 7 10 7Q11 7 11 8V11Q11 12 10 12Q9 12 9 11Z',
        'exclamation-point':'M8 7V10M8 12V12.1',
        'headphone':'M5 11V9.5A3 3 0 0 1 11 9.5V11M5 10H6V12H5ZM10 10H11V12H10Z',
        'input':'M5 9H10M7 7L5 9L7 11M5 11V12.5H11',
        'key':'M5 8.5A1.4 1.4 0 1 0 7.8 8.5A1.4 1.4 0 1 0 5 8.5M7.5 9.5L10.8 12.5M9.5 11.3L10.4 10.4',
        'minus-corner':'M5.5 10H10.5',
        'output':'M6 9H11M9 7L11 9L9 11M5 11V12.5H11',
        'pen':'M5.5 12.5L6 10.8L9.7 7.1L11 8.4L7.3 12.1Z',
        'pen-line':'M5 13H11M5.5 11.4L6 9.9L9.3 6.8L10.5 8L7.2 11Z',
        'plus-corner':'M5.5 10H10.5M8 7.5V12.5',
        'question-mark':'M6.5 8Q6.5 6.8 8 6.8Q9.7 6.8 9.7 8.2Q9.7 9 8 9.8V10.5M8 12.5V12.6',
        'scan':'M5 9V7.5H6.5M9.5 7.5H11V9M5 11V12.5H6.5M9.5 12.5H11V11',
        'search-corner':'M5 9.3A2.2 2.2 0 1 0 9.4 9.3A2.2 2.2 0 1 0 5 9.3M9 11L11 13',
        'signal':'M5 12V11M7 12V9.5M9 12V8M11 12V6.5',
        'sliders':'M5 7V13M8 7V13M11 7V13M4 9H6M7 11H9M10 8H12',
        'terminal':'M5 8L7 10L5 12M8.5 12H11',
        'type':'M5.7 7.4H10.3M8 7.4V11.8M6.8 11.8H9.2',
        'type-corner':'M5.7 7.4H10.3M8 7.4V11.8M6.8 11.8H9.2',
        'user':'M6.8 8.5A1.2 1.2 0 1 0 9.2 8.5A1.2 1.2 0 1 0 6.8 8.5M5.5 12.5Q5.8 10.5 8 10.5Q10.2 10.5 10.5 12.5',
        'video-camera':'M5 8H9V12H5ZM9 9L11 8V12L9 11',
        'volume':'M5 9H6.5L8.5 7.5V12.5L6.5 11H5ZM10 9Q11 10 10 11',
        'x-corner':'M6 8L10 12M10 8L6 12',
    }
    for suffix, detail in doc_details.items():
        body = rr(3,1.8,10,12.4,.8) if suffix in ('braces','type') else doc
        # The page fold and lower edge require a real optical margin. Keep
        # stroke weight while fitting centerlines rather than shrinking ink.
        detail_path = path(detail)
        if suffix in ('braces', 'type'):
            detail_path = detail_path.transform(1, 0, 0, 1, 0, -2)
        elif suffix not in ('axis-3d', 'input', 'output'):
            detail_path = detail_path.transform(.9, 0, 0, .82, .8, 1.8)
        detail_layer = stroke(detail_path,.95) if suffix in ('braces','type') else union(fold,stroke(detail_path,.95))
        if suffix == 'badge':
            detail_layer = union(fold, stroke(transform(api['badge_body'](), scale=.36, dy=2), .95))
        if suffix == 'chart-pie':
            detail_layer = union(fold, path('M7.6 7.2A2.7 2.7 0 1 0 10.3 9.9H7.6Z'),
                                 path('M8.6 6.7V8.9H10.8A2.2 2.2 0 0 0 8.6 6.7Z'))
        if suffix == 'cog':
            detail_layer = union(fold, gear(7.7,9.9,2.8))
        if suffix == 'axis-3d':
            axes = stroke('M7.65 10.25V5.45M6.65 6.55L7.65 5.45L8.65 6.55'
                          'M7.65 10.25L4.75 12.1M4.8 10.65L4.75 12.1H6.2'
                          'M7.65 10.25L10.95 11.95M9.5 12.1L10.95 11.95L10.75 10.55',1.08)
            body = path('M2.15 1.75H10.7L13.85 4.9V14.25H2.15Z')
            detail_layer = union(stroke('M10.7 1.75V4.9H13.85',1.15),axes)
        if suffix in ('input','output'):
            body = transform(doc,0,.72,-2,-1.3)
            detail_layer = union(transform(fold,0,.72,-2,-1.3),mark('arrow-left' if suffix == 'input' else 'arrow-right',12,11,.75))
        shape('file-'+suffix,body,detail_layer, 'document file '+suffix.replace('-',' '))
    shape('files', union(path('M2 1.7H8L11 4.7V12.5H2Z'),path('M5 4H11L14 7V14.3H5Z')),stroke('M5 4V14M5 4H11V7H14',1), 'multiple documents files')
    stack('file-stack', rr(1.8,1.6,9.1,10.3,1.1), path('M4.8 4.4H10.7L14.1 7.8V14.3H4.8Z'),
          stroke('M10.7 4.4V7.8H14.1',1.15), 'documents stack')

    folder = path('M1.8 3.8H6.2L7.6 5.4H14.2V12.8H1.8Z')
    folder_details = {
        'bookmark':'M6.5 7H9.5V11.5L8 10.5L6.5 11.5Z',
        'clock':'M5.5 9A2.5 2.5 0 1 0 10.5 9A2.5 2.5 0 1 0 5.5 9M8 7.5V9L9 9.7',
        'cog':'M8 6.4V7.4M8 10.6V11.6M5.4 9H6.4M9.6 9H10.6M6.9 7.9L7.3 8.3M8.7 9.7L9.1 10.1M9.1 7.9L8.7 8.3M7.3 9.7L6.9 10.1M7 9A1 1 0 1 0 9 9A1 1 0 1 0 7 9',
        'dot':'M8 8.8V9.2',
        'git':'M6 7V10.8M6 8.5Q10 8.5 10 6.8M5.3 6.5A.7 .7 0 1 0 6.7 6.5A.7 .7 0 1 0 5.3 6.5M5.3 11A.7 .7 0 1 0 6.7 11A.7 .7 0 1 0 5.3 11M9.3 6.5A.7 .7 0 1 0 10.7 6.5A.7 .7 0 1 0 9.3 6.5',
        'git-2':'M5.5 7L10.5 11M5.5 11L10.5 7M5 7A.6 .6 0 1 0 6.2 7A.6 .6 0 1 0 5 7M9.8 7A.6 .6 0 1 0 11 7A.6 .6 0 1 0 9.8 7M9.8 11A.6 .6 0 1 0 11 11A.6 .6 0 1 0 9.8 11',
        'input':'M5.5 9H11M7.5 7L5.5 9L7.5 11',
        'kanban':'M5 7V11M8 7V9.5M11 7V10.5',
        'key':'M5 8A1.5 1.5 0 1 0 8 8A1.5 1.5 0 1 0 5 8M7.5 9L10.5 11.5M9 10.2L10 9.2',
        'output':'M5.5 9H11M9 7L11 9L9 11',
        'pen':'M5.4 11L6 9.6L9.8 6.7L10.8 7.8L6.8 10.7Z',
        'root':'M8 6.5V8.5M5 11V10Q5 8.5 8 8.5Q11 8.5 11 10V11M4.2 11H5.8M10.2 11H11.8',
        'search-2':'M5 8.5A2 2 0 1 0 9 8.5A2 2 0 1 0 5 8.5M8.5 10L10.5 12',
        'symlink':'M5 11V9Q5 7 7 7H10.5M9 5.5L10.5 7L9 8.5',
        'sync':'M5.5 8Q6.1 6.6 7.8 6.6Q9.3 6.6 10.3 7.8M10.3 6.5V7.9H9M10.5 10Q9.9 11.4 8.2 11.4Q6.7 11.4 5.7 10.2M5.7 11.5V10.1H7',
        'tree':'M5.5 6.5V11H10.5M5.5 8H9M9 7.3H10.5V8.7H9ZM10.5 10.3H12V11.7H10.5Z',
        'user':'M7 7.8A1 1 0 1 0 9 7.8A1 1 0 1 0 7 7.8M5.8 11Q6 9.5 8 9.5Q10 9.5 10.2 11',
        'users':'M6 7.5A1 1 0 1 0 8 7.5A1 1 0 1 0 6 7.5M4.8 11Q5 9.3 7 9.3Q9 9.3 9.2 11M9.5 7A1 1 0 0 1 9.5 9M10 9.5Q11.3 9.6 11.5 11',
    }
    for suffix, detail in folder_details.items():
        detail_path = path(detail)
        if suffix in ('git', 'git-2', 'cog', 'key', 'search-2', 'root', 'symlink', 'sync', 'tree'):
            detail_path = detail_path.transform(.88, 0, 0, .78, .96, 2.65 if suffix == 'symlink' else 2.15)
        ink = gear(8,9.1,2.65) if suffix == 'cog' else stroke(detail_path,.95)
        if suffix == 'git-2':
            ink = union(stroke('M5.7 6.8V11.1M5.7 10.4Q10.1 10.4 10.1 7.7',1.1),
                        dots((5.7,6.8),(5.7,11.1),(10.1,7.7),r=.97))
        if suffix == 'root':
            ink = union(stroke('M8 7.4V9M5.2 10.8V9H10.8V10.8',1.08),
                        rr(6.95,6.7,2.1,1.65,.4), rr(4.15,10,2.1,1.75,.4), rr(9.75,10,2.1,1.75,.4))
        shape('folder-'+suffix,folder,ink,'directory folder '+suffix.replace('-',' '))
    shape('folder-closed',folder,stroke('M2 6.4H14',1),'directory closed')
    shape('folder-open-dot',path('M1.8 3.8H6.2L7.6 5.4H13.5L12.5 12.8H1.5Z'),union(stroke('M1.8 7H14L12.5 12.8',1),circle(8,9.5,.8)), 'directory open notification')

    api['CATEGORY'] = 'Communication'
    # Speech bubbles use separate round and square contours and keep the
    # identifying mark centered away from the tail.
    bubble_round = path('M2 7Q2 2 8 2Q14 2 14 7Q14 12 8 12H6L3 14L3.5 10.5Q2 9 2 7Z')
    bubble_square = path('M3 2.5H13Q14 2.5 14 3.5V10.5Q14 11.5 13 11.5H7L4 14V11.5H3Q2 11.5 2 10.5V3.5Q2 2.5 3 2.5Z')
    shape('message-circle', bubble_round, None, 'conversation chat bubble')
    for suffix in ('check','exclamation-point','heart','plus','question-mark','x'):
        shape('message-circle-'+suffix, bubble_round, mark(suffix,8,6.8,.8), 'conversation chat '+suffix)
    shape('message-circle-code', bubble_round, stroke('M6.5 5L4.8 6.8L6.5 8.6M9.5 5L11.2 6.8L9.5 8.6',1), 'conversation code')
    shape('message-circle-more', bubble_round, dots((5.5,7),(8,7),(10.5,7),r=.65), 'conversation more')
    shape('message-circle-text', bubble_round, stroke('M5 5.5H11M5 8H9.5',1), 'conversation text')
    shape('message-circle-reply', bubble_round, stroke('M6.5 5L4.8 6.8L6.5 8.5M5 6.8H9Q11 6.8 11 9',1), 'conversation reply')
    shape('message-circle-off', bubble_round, line((2,2),(14,14)), 'conversation disabled')
    glyph('message-circle-dashed',stroke('M3.4 3.5Q5.1 2 7 2M9 2Q11 2.1 12.5 3.5M13.7 5.5Q14.4 7.5 13.4 9.5M11.7 11Q10 12 8 12H6L3 14L3.5 10.5M2.3 8.8Q1.8 7 2.5 5.2'),None,'conversation dashed')
    glyph('message-circle-dashed-check',stroke('M3.4 3.5Q5.1 2 7 2M9 2Q11 2.1 12.5 3.5M13.7 5.5Q14.4 7.5 13.4 9.5M11.7 11Q10 12 8 12H6L3 14L3.5 10.5M2.3 8.8Q1.8 7 2.5 5.2'),mark('check',8,7,.7),'conversation dashed check')
    square_details = {
        'code':'M6.5 5L4.8 6.8L6.5 8.6M9.5 5L11.2 6.8L9.5 8.6',
        'diff':'M4.5 6H7.5M6 4.5V7.5M8.5 8.5H11.5',
        'dot':'M8 6.7V7.2',
        'exclamation-point':'M8 4.5V7.2M8 9V9.1',
        'lock':'M6 6.7H10V9.7H6ZM6.8 6.7V5.5Q6.8 4.2 8 4.2Q9.2 4.2 9.2 5.5V6.7',

        'reply':'M6.5 5L4.8 6.8L6.5 8.5M5 6.8H9Q11 6.8 11 9',
        'share':'M6.5 8.5L10.5 4.8M8 4.8H10.5V7.3M5 5H4.5V9H9V8.5',
        'x':'M6 5L10 9M10 5L6 9',
    }
    for suffix, detail in square_details.items():
        shape('message-square-'+suffix,bubble_square,stroke(detail,1),'message chat '+suffix)
    quote = path('M5.8 4.5C7 4.5 7.5 5.3 7.4 6.4C7.3 7.9 6.4 9 4.9 9.55L4.6 8.7Q5.9 8.05 6.05 7.3C3.85 7.55 3.7 4.55 5.8 4.5Z')
    shape('message-square-quote',bubble_square,union(quote,transform(quote,dx=4.1)),'message chat quote')
    shape('message-square-off',bubble_square,line((2,2),(14,14)),'message disabled')
    glyph('message-square-dashed',stroke('M3 2.5H5M7 2.5H9M11 2.5H13Q14 2.5 14 3.5V4.5M14 6.5V8.5M14 10Q14 11.5 12.5 11.5H11M9 11.5H7L4 14V11.5H3Q2 11.5 2 10.5V9M2 7V5M2 3.5Q2 2.5 3 2.5'),None,'conversation dashed')
    shape('messages-circle', union(transform(bubble_round,0,.72,-2,-2),transform(bubble_round,0,.72,2,2)), stroke('M5 9Q5 5 9.5 5Q14 5 14 9Q14 12.5 9.5 12.5H8L5.5 14L6 11.2Q5 10 5 9Z',1), 'conversations messages')
    shape('messages-square', union(transform(bubble_square,0,.72,-2,-2),transform(bubble_square,0,.72,2,2)), stroke('M6 5H13Q14 5 14 6V11Q14 12 13 12H9L6 14V12H6Q5 12 5 11V6Q5 5 6 5Z',1), 'conversations messages')

    # A reduced body gives standalone badges their own clear space.
    userbody = union(circle(5.5,4.5,2.3),path('M1.8 13.4V12Q1.8 8.5 5.5 8.5Q9.2 8.5 9.2 12V13.4Z'))
    roundbody = union(circle(5.5,4.5,2.3),path('M1.8 13.5Q1.8 9 5.5 9Q9.2 9 9.2 13.5Z'))
    for prefix, body in (('user',userbody),('user-round',roundbody)):
        for suffix in ('cog','exclamation-point','key','minus','pen','search','shield','star'):
            if prefix == 'user' and suffix in ('star',): pass
            if suffix in ('shield','star'):
                detail = stroke('M10 8L12 7L14 8V10Q14 12 12 13Q10 12 10 10Z',1) if suffix == 'shield' else stroke('M12 6.5L12.8 8.3L14.5 8.5L13.3 9.8L13.6 11.6L12 10.7L10.4 11.6L10.7 9.8L9.5 8.5L11.2 8.3Z',1)
            else:
                detail = mark(suffix,12,9.5,.68)
            shape(prefix+'-'+suffix,body,detail,'person account '+suffix)
    for suffix in ('arrow-left','check','plus','x'):
        shape('user-round-'+suffix,roundbody,mark(suffix,12,9.5,.68),'person account '+suffix)
    shape('user-lock',userbody,mark('lock',12,9.5,.68),'person account lock')
    shape('user-round',union(circle(8,4.5,2.7),path('M2.5 13.5Q2.5 9 8 9Q13.5 9 13.5 13.5Z')),None,'person profile')
    side_heads = union(circle(3.2,6.2,1.45),circle(12.8,6.2,1.45))
    side_shoulders = path('M1.6 13.2V11.7Q1.6 9.4 3.4 9.4Q5.6 9.4 5.6 11.7V13.2Z')
    side_people = union(side_heads,side_shoulders,api['mirror'](side_shoulders))
    middle = union(circle(8,3.8,1.85),path('M4.7 14V11.4Q4.7 8.3 8 8.3Q11.3 8.3 11.3 11.4V14Z'))
    stack('user-group',side_people,middle,None,'people group')
    glyph('user-round-group',union(*(stroke(circle(x,y,r),1.1) for x,y,r in ((3.3,6,1.55),(8,3.6,1.65),(12.7,6,1.55))),stroke('M1.1 13V11.7Q1.1 9.5 3.3 9.5Q5.5 9.5 5.5 11.7V13M10.5 13V11.7Q10.5 9.5 12.7 9.5Q14.9 9.5 14.9 11.7V13M6.6 11.3V9Q6.6 7.4 8 7.4Q9.4 7.4 9.4 9V11.3',1.1)),None,'people round group')
    glyph('users-round',union(stroke('M1.5 13Q1.5 9.5 5 9.5Q8 9.5 8 13M8 13Q8 9.5 11 9.5Q14.5 9.5 14.5 13',1.1),stroke(circle(5,5,2),1.1),stroke(circle(11,5,2),1.1)),None,'people round group')
    pair = union(circle(3.9,7.2,1.65), circle(12.1,7.2,1.65))
    shoulder = path('M1.5 14V12.9Q1.5 10.5 3.9 10.5Q6.3 10.5 6.3 12.9V14Z')
    exchange = stroke('M5 3H10.8M9.4 1.65L10.8 3L9.4 4.35',1.2)
    shape('users-collaboration',union(pair,shoulder,api['mirror'](shoulder)),exchange,'people collaboration')
    round_pair = union(stroke(pair,1.25),stroke('M1.5 14Q1.5 10.6 3.9 10.6Q6.3 10.6 6.3 14M9.7 14Q9.7 10.6 12.1 10.6Q14.5 10.6 14.5 14',1.25))
    glyph('users-round-collaboration',round_pair,exchange,'people collaboration')

    mail = rr(1.6,3.4,12.8,9.2,1.2)
    for suffix in ('clock','dot','exclamation-point','minus','pen','question-mark','search','x'):
        shape('mail-'+suffix,mail,union(stroke('M2 4L8 8L14 4',1.05),mark(suffix,10.5,10.1,.6)),'email message '+suffix)
    shape('mail-badge',mail,union(stroke('M2 4L8 8L14 4',1.05),circle(12,3,1.6)),'email notification')
    shape('mails',union(rr(1.5,2,10,8,1),rr(4.5,5,10,8,1)),stroke('M4.5 5L9.5 8L14.5 5M4.5 5V13H14.5V5Z',1),'multiple email messages')

    api['CATEGORY'] = 'Product tools'
    # Status marks sit outside reduced bodies, maintaining clear separation.
    db = path('M2 4Q2 1.5 6.5 1.5Q11 1.5 11 4V11Q11 13.5 6.5 13.5Q2 13.5 2 11Z')
    dbdetail = stroke('M2 4Q2 6.5 6.5 6.5Q11 6.5 11 4M2 7.5Q2 10 6.5 10Q8.5 10 10 9.4',1)
    for suffix in ('check','cog','minus','plus','search','x'):
        shape('database-'+suffix,db,union(dbdetail,mark(suffix,12.35 if suffix == 'cog' else 12.5,12,.62)),'storage database '+suffix)
    shape('database-backup',db,union(dbdetail,stroke('M10.5 12Q11 10 13 10Q14.5 10 14.8 11.5M14.8 10V11.6H13M14 13Q12.5 14.3 11 13',1)), 'database backup restore')
    pack = path('M1.5 4L6.2 1.8L10.8 4V10L6.2 12.5L1.5 10Z')
    packdetail=stroke('M1.5 4L6.2 6.5L10.8 4M6.2 6.5V12.5',1)
    for suffix in ('check','minus','pen','plus','question-mark','search','x'):
        shape('package-'+suffix,pack,union(packdetail,mark(suffix,12,11.5,.7)),'parcel package '+suffix)
    shape('package-2',path('M2 4L8 1.5L14 4V12L8 14.5L2 12Z'),stroke('M2 4L8 7L14 4M8 7V14M5 2.8L11 5.5',1),'parcel box shipping')
    carton = path('M1.55 6.8L3.5 4.5L8 2.45L12.5 4.5L14.45 6.8L12.5 7.8V11.7L8 14L3.5 11.7V7.8Z')
    flap_seams = stroke('M3.5 4.5L8 6.7L12.5 4.5M1.55 6.8L6.2 9.1L8 6.7L9.8 9.1L14.45 6.8M8 8.25V14',1.15)
    shape('package-open',carton,flap_seams,'parcel open box')
    shield = path('M6.4 1.8L11 3.5V7.2Q11 10.5 6.4 13Q1.8 10.5 1.8 7.2V3.5Z')
    for suffix in ('cog','minus','plus','question-mark','user'):
        shape('shield-'+suffix,shield,mark(suffix,12,10.8,.65),'security protection '+suffix)
    shape('shield-cog-corner',shield,mark('cog',10.8,12,.75),'security protection settings corner')
    shape('shield-ellipsis',shield,dots((4,7),(6.5,7),(9,7),r=.65),'security protection more')
    shape('shield-half',path('M8 1.5L13.5 3.5V7.5Q13.5 11.5 8 14.5Q2.5 11.5 2.5 7.5V3.5Z'),stroke('M8 2V14',1.1),'security protection half')
    shape('shield-ban',shield,stroke('M3.5 4L9 9.5',1.2),'security forbidden')
    shape('shield-house',shield,stroke('M3.5 7L6.4 4.5L9.3 7M4.3 6.5V10H8.5V6.5M5.8 10V8H7V10',1),'security home protection')
    shape('shield-off',shield,line((2,2),(14,14)),'security protection disabled')

    star = path('M8 1.4L9.9 5.5L14.4 6L11 9.2L11.8 13.8L8 11.5L4.2 13.8L5 9.2L1.6 6L6.1 5.5Z')
    for suffix in ('check','minus','plus','x'):
        shape('star-'+suffix,transform(star,0,.72,-1.6,-1.5),mark(suffix,12,12,.68),'favorite star '+suffix)
    shape('star-half',star,stroke('M8 2V11.5',1.1),'favorite star half')
    shape('star-off',star,line((2,2),(14,14)),'favorite star disabled')

    # Simple enclosed marks.
    for kind, body in (('square',rr(2,2,12,12,1.7)),('circle',circle(8,8,6))):
        suffixes = ('exclamation-point','minus','plus','x') if kind == 'square' else ()
        for suffix in suffixes:
            shape(kind+'-'+suffix,body,compact(suffix,8,8,1),'status '+suffix)
    shape('square-check-big',rr(2,2,12,12,1.7),check(8,8,.8),'status checked')
    shape('circle-check-big',circle(8,8,6),check(8,8,.8),'status checked')
    percent = union(stroke('M5.6 10.9L10.4 5.1',1.25),dots((5.45,5.45),(10.55,10.55),r=1))
    shape('circle-percent',circle(8,8,6),percent,'percentage ratio')
    shape('square-percent',rr(2,2,12,12,1.7),percent,'percentage ratio')
    shape('diamond-percent',path('M8 1.6L14.4 8L8 14.4L1.6 8Z'),union(stroke('M6.2 10.35L9.8 5.65',1.2),dots((6.05,6.05),(9.95,9.95),r=.8)),'percentage ratio')
    shape('square-user',rr(2,2,12,12,1.7),compact('user',8,8,1.22),'account profile')
    shape('square-user-round',rr(2,2,12,12,1.7),union(stroke(circle(8,5.45,1.5),1.17),stroke('M4.7 11.8Q4.7 9.2 8 9.2Q11.3 9.2 11.3 11.8',1.2)), 'account round profile')
    shape('circle-user-round',circle(8,8,6),compact('user',8,8,1.22),'account round profile')
    shape('octagon-x',path('M5 1.8H11L14.2 5V11L11 14.2H5L1.8 11V5Z'),mark('x'),'stop close')
    glyph('circle-fading-check',stroke('M13.5 8A5.5 5.5 0 0 1 8 13.5M2.5 8A5.5 5.5 0 0 1 8 2.5A5.5 5.5 0 0 1 13.5 8M3.3 11L3.4 11.1M5.2 13L5.3 13.1'),mark('check'),'fading completed')
    glyph('circle-fading-plus',stroke('M13.5 8A5.5 5.5 0 0 1 8 13.5M2.5 8A5.5 5.5 0 0 1 8 2.5A5.5 5.5 0 0 1 13.5 8M3.3 11L3.4 11.1M5.2 13L5.3 13.1'),mark('plus'),'fading add')

    # Disabled versions reuse the actual subject, cut a channel through it,
    # and place the slash in that channel so the two marks remain legible.
    def disabled(name, source):
        b,d,outline,_,_ = api['DRAWINGS'][source]
        clearance = line((2,2),(14,14),width=2.7)
        slash = line((2,2),(14,14))
        cut = lambda p: op(p,clearance,po.PathOp.DIFFERENCE)
        if outline:
            shape(name,cut(b),union(cut(d),slash),'disabled '+source)
        else:
            glyph(name,cut(b),union(cut(d),slash),'disabled '+source)
    for name, source in (
        ('flag-off','flag'),('heart-off','heart'),('image-off','image'),
        ('lightbulb-off','lightbulb'),('map-pin-off','map-pin'),('monitor-off','monitor'),
        ('pin-off','pin'),('power-off','power'),('save-off','save'),
        ('server-off','server-rack'),('timer-off','timer'),('trash-off','trash'),
        ('video-off','video-call'),('wrench-off','wrench'),('zap-off','zap'),
    ):
        disabled(name,source)

    # Actions and small marks.
    for name, geom in {
        'grip':'M5 4V4.1M8 4V4.1M11 4V4.1M5 8V8.1M8 8V8.1M11 8V8.1M5 12V12.1M8 12V12.1M11 12V12.1',
        'grip-horizontal':'M4 6V6.1M8 6V6.1M12 6V6.1M4 10V10.1M8 10V10.1M12 10V10.1',
        'grip-vertical':'M6 4V4.1M10 4V4.1M6 8V8.1M10 8V8.1M6 12V12.1M10 12V12.1',
        'move':'M8 1.5V14.5M5.5 4L8 1.5L10.5 4M5.5 12L8 14.5L10.5 12M1.5 8H14.5M4 5.5L1.5 8L4 10.5M12 5.5L14.5 8L12 10.5',
        'separator-horizontal':'M2 8H14M8 1.5V5M6 3L8 5L10 3M8 14.5V11M6 13L8 11L10 13',
        'separator-vertical':'M8 2V14M1.5 8H5M3 6L5 8L3 10M14.5 8H11M13 6L11 8L13 10',
        'unfold-vertical':'M3 6.3H13M3 9.7H13M8 1.5V5M6 3.5L8 1.5L10 3.5M8 11V14.5M6 12.5L8 14.5L10 12.5',
        'forward':'M2 11Q2 6.5 8 6.5H10V3L14.5 7.5L10 12V8.5H8Q4 8.5 2 11Z',
        'reply':'M14 12Q13 7 7 7H5V4L1.5 8L5 12V9H7Q11 9 14 12Z',
        'reply-all':'M14 12Q13 7 9 7H8V4L4.5 8L8 12V9H9Q11.5 9 14 12ZM3.5 4L.8 8L3.5 12',
        'send-horizontal':'M1.5 2L14.5 8L1.5 14L3.5 8ZM3.5 8H14',
        'locate':'M8 3A5 5 0 1 0 8 13A5 5 0 1 0 8 3M8 1.3V4M8 12V14.7M1.3 8H4M12 8H14.7',
        'locate-fixed':'M8 3A5 5 0 1 0 8 13A5 5 0 1 0 8 3M8 1.3V4M8 12V14.7M1.3 8H4M12 8H14.7M6.5 8A1.5 1.5 0 1 0 9.5 8A1.5 1.5 0 1 0 6.5 8',
        'list-checks':'M2 4L3 5L5 3M7 4H14M2 9L3 10L5 8M7 9H14M7 13H14',
        'list-filter':'M2 3H14M4 7H12M6 11H10M7.5 14H8.5',
        'list-tree':'M2.5 2V12.5H5.8M2.5 4.5H5.8M2.5 8.5H5.8M8.5 4.5H14M8.5 8.5H14M8.5 12.5H14',
        'spell-check':'M2 9L4 3L6 9M2.8 7H5.2M8 3H10Q12 3 12 4.5Q12 6 10 6H8ZM8 6H10.5Q12.5 6 12.5 7.5Q12.5 9 10.5 9H8ZM8 12L9.5 13.5L13 10',
        'regex':'M3 11V11.1M10 4V10M7.4 5.5L12.6 8.5M7.4 8.5L12.6 5.5',
        'nfc':'M5 3Q1 8 5 13M7.5 4.5Q5 8 7.5 11.5M10 6Q9 8 10 10M12.5 7V9',
        'waypoints':'M3 4L8 8L13 4M8 8L12 12M1.5 4A1.5 1.5 0 1 0 4.5 4A1.5 1.5 0 1 0 1.5 4M11.5 4A1.5 1.5 0 1 0 14.5 4A1.5 1.5 0 1 0 11.5 4M10.5 12A1.5 1.5 0 1 0 13.5 12A1.5 1.5 0 1 0 10.5 12M6.5 8A1.5 1.5 0 1 0 9.5 8A1.5 1.5 0 1 0 6.5 8',
        'voicemail':'M1.5 8A2.5 2.5 0 1 0 6.5 8A2.5 2.5 0 1 0 1.5 8M9.5 8A2.5 2.5 0 1 0 14.5 8A2.5 2.5 0 1 0 9.5 8M4 10.5H12',

    }.items():
        if name == 'waypoints':
            centers = ((3,4), (8,8), (13,4), (12,12))
            nodes = union(*(circle(x,y,1.5) for x,y in centers))
            links = api['op'](stroke('M3 4L8 8L13 4M8 8L12 12',1.2),nodes,api['po'].PathOp.DIFFERENCE)
            glyph(name,union(links,*(stroke(circle(x,y,1.5),1.2) for x,y in centers)),None,'connected waypoints nodes')
        else:
            glyph(name,stroke(geom),None,name.replace('-',' '))
    hook = stroke('M6.6 2.1A2.22 2.22 0 1 1 6.55 5.58L11.55 10.05',1.3)
    # The three terminals form an equilateral triangle about (8,8).
    glyph('webhook',union(hook,transform(hook,120),transform(hook,240)),None,'webhook')
    for suffix, geom in {
        'minus':'M2 4H9M2 8H9M2 12H9M11 9H14',
        'plus':'M2 4H9M2 8H9M2 12H9M10.5 10H14.5M12.5 8V12',
        'x':'M2 4H9M2 8H9M2 12H9M11 8L14 11M14 8L11 11',
        'clock':'M2 4H9M2 8H9M2 12H9M10 10A2.5 2.5 0 1 0 15 10A2.5 2.5 0 1 0 10 10M12.5 8.5V10L13.5 10.7',
    }.items(): glyph('list-'+suffix,stroke(geom,1.1),None,'list '+suffix)
    # Hollow inactive bars preserve the full signal silhouette at zero and
    # low strengths; the filled bars indicate the actual active count.
    for suffix, count in (('zero',0),('low',1),('medium',2),('high',3),('',4)):
        bars = []
        for i, h in enumerate((3.5, 5.8, 8.1, 10.4)):
            bar=rr(2+i*3.1, 13.5-h, 1.9, h, .7)
            bars.append(bar if i < count else stroke(bar,.7))
        glyph('signal'+('-'+suffix if suffix else ''),union(*bars),None,'mobile signal '+suffix)
    for suffix, geom in (('zero','M8 13V13.1'),('low','M5.8 10.5Q8 8.8 10.2 10.5M8 13V13.1'),('high','M2 5Q8 .5 14 5M4 8Q8 5 12 8M6 10.5Q8 9 10 10.5M8 13V13.1')):
        glyph('wifi-'+suffix,union(circle(8,12.35,.92),stroke('M2.2 6.1Q4.4 4.2 6.5 4.05M9.5 4.05Q11.6 4.2 13.8 6.1M4.6 8.75Q5.8 7.8 6.8 7.65M9.2 7.65Q10.2 7.8 11.4 8.75',1.25)) if suffix == 'zero' else (union(stroke(geom),dots((3,5.5),(5.5,4),(8,3.5),(10.5,4),(13,5.5),r=.55)) if suffix == 'low' else stroke(geom)),None,'wireless signal '+suffix)

    def badged(name, source, suffix):
        b,d,_,_,_=api['DRAWINGS'][source]
        host_detail = transform(d,0,.72,-1.8,-1.5) if suffix != 'cog' else {
            'monitor': stroke('M6.2 8.7V10.9M3.9 10.9H8.5',1.2),
            'hourglass': stroke('M4.9 4.4H7.5',1.15),
            'server-rack': union(stroke('M1.9 6.5H10.5',1.2),dots((4,4.2),(4,8.8),r=.68)),
        }[source]
        shape(name,transform(b,0,.72,-1.8,-1.5),union(host_detail,mark(suffix,12,11.8,.68)),name.replace('-',' '))
    for source, suffixes in {
        'archive':('arrow-down','arrow-up','x'),
        'bell':('check','dot','minus'),
        'cloud':('check','sync'),
        'heart':('minus','plus','x'),
        'map-pin':('plus','x'),
        'save':('check','pen','plus'),
        'tag':('plus','x'),
        'monitor':('cog',),
        'server-rack':('cog',),
    }.items():
        for suffix in suffixes:
            prefix = 'server' if source == 'server-rack' else source
            badged(prefix+'-'+suffix,source,suffix)
    badged('alarm-clock-check','alarm-clock','check')
    disabled('alarm-clock-off','alarm-clock')
    badged('image-minus','image','minus')
    badged('hourglass-cog','hourglass','cog')

    api['CATEGORY'] = 'Devices and connectivity'
    shape('captions',rr(1.6,3,12.8,10,1.6),stroke('M7 6Q5 4.5 4 6Q3 7.5 4 9Q5 10.5 7 9M12 6Q10 4.5 9 6Q8 7.5 9 9Q10 10.5 12 9',1.1),'subtitles closed captions accessibility')
    disabled('captions-off','captions')
    shape('cctv',path('M2 3L11 4.5L10.2 9L1.2 7.5Z'),union(stroke('M10.5 5L14 4V8L10 8M6 8.5L7.5 12H12M12 10V14',1.1),circle(3.5,5.5,.7)),'security surveillance camera')
    disabled('cctv-off','cctv')
    shape('ethernet-port',path('M2 2.5H14V11H11V13.5H5V11H2Z'),stroke('M5 4.5V7M7 4.5V7M9 4.5V7M11 4.5V7M5 10H11',1),'wired network port')
    shape('memory-stick',rr(1.5,4,13,7,1),union(stroke('M4 6H6V8.5H4ZM7 6H9V8.5H7ZM10 6H12V8.5H10ZM3 11V12.5M5 11V12.5M7 11V12.5M9 11V12.5M11 11V12.5M13 11V12.5',1)),'computer ram memory')
    shape('router',rr(1.7,8,12.6,5,1.2),union(stroke('M4 8V4M12 8V4M6 5Q8 3.2 10 5M7 6.5Q8 5.8 9 6.5',1.1),dots((4.5,10.5),(7,10.5),r=.5)),'wireless router network')
    shape('speaker',rr(3.2,1.6,9.6,12.8,1.4),union(stroke(circle(8,9.8,2.5),1.1),circle(8,4.5,1)),'audio loudspeaker')
    shape('touchpad',rr(1.8,2.5,12.4,11,1.4),stroke('M2 10H14M8 10V13',1.1),'trackpad computer input')
    disabled('touchpad-off','touchpad')
    shape('webcam',circle(8,6.5,4.8),union(stroke(circle(8,6.5,1.7),1.1),stroke('M8 11.3V13.5M5.5 14H10.5',1.1)),'camera video computer')
    shape('headset',path('M2 8V7A6 6 0 0 1 14 7V8H12V7A4 4 0 0 0 4 7V8Z'),union(rr(2,7.5,2.7,4,.8),rr(11.3,7.5,2.7,4,.8),stroke('M14 10V12Q14 14 11 14H9.5',1.1)),'headphones microphone call')
    shape('smartphone-user-round',rr(3,1.5,10,13,1.8),union(stroke('M6 3H10M7 13H9',1),mark('user',8,8,1.05)),'mobile phone account')
    shape('screen-share',rr(1.5,2,13,9,1.3),stroke('M8 11V14M5 14H11M8 8V4.2M6 6.2L8 4.2L10 6.2',1.1),'display share presentation')
    disabled('screen-share-off','screen-share')
    shape('mouse-pointer',path('M3 1.8L12 9L8 9.6L10 13.5L8 14.5L6 10.3L3 13Z'),None,'cursor pointer')
    shape('mouse-pointer-click',path('M4 5L12 10L8.5 10.5L10 13.5L8 14.5L6.5 11.3L4 13Z'),stroke('M3 1.5V3M1 4H2.5M6 2L5.3 3.3M1.5 7L2.7 6.2',1),'cursor click')
    glyph('bluetooth-connected',stroke('M7 1.5V14.5L12 10.5L3 3.5M7 1.5L12 5.5L3 12.5'),dots((1.5,8),(14.5,8),r=.7),'wireless connected')
    glyph('bluetooth-searching',stroke('M6 1.5V14.5L11 10.5L2 3.5M6 1.5L11 5.5L2 12.5M13 4Q15 8 13 12'),None,'wireless searching')
    shape('volume-1',path('M2 6H5L9 2.5V13.5L5 10H2Z'),stroke('M11.5 6Q13.5 8 11.5 10',1.2),'audio sound low')

    api['CATEGORY'] = 'Interface controls'
    for name, geom in {
        'heading-3':'M2 3V12M7 3V12M2 7.5H7M10 5Q12 3.5 13.5 5Q14.5 6.5 12 7.5Q14.5 8 14 10Q13.5 12 10 11',
        'heading-4':'M2 3V12M7 3V12M2 7.5H7M12 4L9.5 9H14M12.5 4V12',
        'languages':'M2 4H10M6 2V4M3.5 5Q4.5 9 9 11M8.5 5Q7.5 9 2.5 11M9 14L11.5 7L14 14M9.8 12H13.2',
        'link-2':'M6 10L5 11A2.5 2.5 0 0 1 1.5 7.5L4 5A2.5 2.5 0 0 1 7.5 5M10 6L11 5A2.5 2.5 0 0 1 14.5 8.5L12 11A2.5 2.5 0 0 1 8.5 11M5.5 10.5L10.5 5.5',
        'loader':'M8 1.5V3.5M12.6 3.4L11.2 4.8M14.5 8H12.5M12.6 12.6L11.2 11.2M8 14.5V12.5M3.4 12.6L4.8 11.2M1.5 8H3.5M3.4 3.4L4.8 4.8',
        'sliders-vertical':'M4 2V5M4 8V14M2.5 5H5.5V8H2.5ZM8 2V8M8 11V14M6.5 8H9.5V11H6.5ZM12 2V4M12 7V14M10.5 4H13.5V7H10.5Z',
        'scan-barcode':'M2 5V2H5M11 2H14V5M2 11V14H5M11 14H14V11M5 5V11M7 5V11M10 5V11M11.5 5V11',
        'scan-qr-code':'M2 5V2H5M11 2H14V5M2 11V14H5M11 14H14V11M5 5H7V7H5ZM9 5H11V7H9ZM5 9H7V11H5ZM9 9H10V10H9M11 11V11.1',
        'scan-text':'M2 5V2H5M11 2H14V5M2 11V14H5M11 14H14V11M5 6H11M5 8H11M5 10H9',

        'ungroup':'M2 6V2H6M10 2H14V6M2 10V14H6M10 14H14V10M5 5H9V9H5ZM8 8H12V12H8Z',
        'panel-left-close':'M2 3H14V13H2ZM6 3V13M12 6L9 8L12 10',
        'panel-left-open':'M2 3H14V13H2ZM6 3V13M9 6L12 8L9 10',
        'table-cells-merge':'M1.3 2.3H9V10H1.3ZM1.3 6.1H9M5.1 2.3V6.1M5.1 6.1V10M9.2 10L10.8 11.5L9.2 13M14.8 10L13.2 11.5L14.8 13',
        'table-cells-split':'M1.3 2.3H9V10H1.3ZM1.3 6.1H9M5.1 2.3V10M10.8 10L9.2 11.5L10.8 13M13.2 10L14.8 11.5L13.2 13',
    }.items(): glyph(name,stroke(geom,1.1),None,name.replace('-',' '))

    events = union(line((1.6,8),(14.4,8)),stroke('M4 8V4M8 8V12M12 8V4',1.2),
                   dots((4,3.5),(8,12.5),(12,3.5),r=1.25))
    glyph('timeline', events, None, 'timeline')
    api['CATEGORY'] = 'Symbols'
    for suffix, geom in {
        'aquarius':'M2 6L4 4L6 6L8 4L10 6L12 4L14 6M2 12L4 10L6 12L8 10L10 12L12 10L14 12',
        'aries':'M8 14V7Q8 2 4.5 2Q2 2 2 5M8 7Q8 2 11.5 2Q14 2 14 5',
        'cancer':'M4.5 3.5A2 2 0 1 0 4.5 7.5A2 2 0 1 0 4.5 3.5M4.5 3.5H11.5M11.5 8.5A2 2 0 1 0 11.5 12.5A2 2 0 1 0 11.5 8.5M4.5 12.5H11.5',
        'capricorn':'M2 4L4 10L6 4L8.5 12Q9.5 14.5 12 13Q14 11.5 12 9.8Q10.5 8.8 9 10',
        'gemini':'M3 2.5Q8 4 13 2.5M5 3.5V12.5M11 3.5V12.5M3 13.5Q8 12 13 13.5',
        'leo':'M5.5 8.6A2 2 0 1 0 1.5 8.6A2 2 0 1 0 5.5 8.6M5.5 8.6C5.5 6.5 4.8 5.4 5.1 3.8C5.8 .55 11.3 1.1 11.3 4.7C11.3 7 8.6 9.5 8.6 11.8C8.6 14.6 11.7 15 13.7 12.7',
        'libra':'M2 10H6Q4 8.5 4 6.5A4 4 0 0 1 12 6.5Q12 8.5 10 10H14M2 13H14',
        'ophiuchus':'M3.5 2.5V9Q3.5 13.5 8 13.5Q12.5 13.5 12.5 9V2.5M1.8 7Q3.4 5.3 5 7T8.2 7T11.4 7T14.6 7',
        'pisces':'M3 2Q8 8 3 14M13 2Q8 8 13 14M2 8H14',
        'sagittarius':'M3 13L13 3M8 3H13V8M5 7L9 11',
        'scorpio':'M2 4V11M2 6Q3 3 5 4Q6 4.5 6 6V11M6 6Q7 3 9 4Q10 4.5 10 6V12Q10 14 12 14H14M12 12L14 14L12 15',
        'taurus':'M4 8A4 4 0 1 0 12 8A4 4 0 1 0 4 8M5 4Q2 3 2 1.5M11 4Q14 3 14 1.5',
        'virgo':'M2 4V12M2 6Q3 3 5 4Q6 4.5 6 6V12M6 6Q7 3 9 4Q10 4.5 10 6V10Q10 14 13 14Q14 14 14 12Q14 10 11 9',
    }.items(): glyph('zodiac-'+suffix,stroke(geom,1.25),None,'astrology zodiac '+suffix)

    api['CATEGORY'] = 'Product tools'
    shape('briefcase-medical',rr(1.5,5,13,9,1.6),union(stroke('M5 5V2.5H11V5',1.1),plus(8,9.2,.65)),'medical first aid case')
    shape('building-complex',union(rr(2,5,5,9,.5),rr(7,2,7,12,.5)),union(stroke('M4 7V8M4 10V11M9 4V5M12 4V5M9 7V8M12 7V8M9 10V11M12 10V11M1 14H15',1)),'buildings office complex')
    badged('building-complex-plus','building-complex','plus')
    shape('brick-wall-fire',rr(1.7,3,10.5,10,.4),union(stroke('M2 6H12M2 9.5H12M5 3V6M9 6V9.5M5 9.5V13',1),stroke('M12 13Q9.5 11.5 11.5 9Q11.5 10.3 12.5 10Q14 9 13 7.5Q16 10 14 12.5Z',1)),'firewall network security')
    shape('brick-wall-shield',rr(1.7,3,10.5,10,.4),union(stroke('M2 6H12M2 9.5H12M5 3V6M9 6V9.5M5 9.5V13',1),stroke('M12 8L14.5 9V11Q14.5 13 12 14Q9.5 13 9.5 11V9Z',1)),'firewall network security shield')
    shape('certificate',path('M2.5 2H13.5V11H9.5L8 13L6.5 11H2.5Z'),union(stroke('M4.5 4.5H11.5M4.5 6.7H9',1),stroke(circle(8,10.3,1.7),1),stroke('M6.8 11.6L6.2 14.5L8 13.5L9.8 14.5L9.2 11.6',1)),'award certificate credential')
    shape('contact-round',rr(2.5,2,11,12,1.3),union(mark('user',8.3,8,1.1),stroke('M1.5 5H3.5M1.5 8H3.5M1.5 11H3.5',1)),'address book contact person')
    shape('delete',path('M5 3H13Q14 3 14 4V12Q14 13 13 13H5L1.5 8Z'),cross(9,8,.7),'backspace delete key')
    gear_points = []
    for tooth in range(8):
        for offset, radius in ((-.32,5.1),(-.18,6.5),(.18,6.5),(.32,5.1)):
            angle = tooth*math.pi/4+offset
            gear_points.append((8+radius*math.cos(angle),8+radius*math.sin(angle)))
    shape('cog',api['poly'](gear_points),stroke(circle(8,8,2.2),1.1),'gear settings')
    globe = circle(6.7,7,5.1)
    land = path('M1.2 3.8L4 2L6.2 2.3Q7 3.4 5.6 4.3L4.3 5.1L4.7 6.3L3.5 7.5L1 6.8Z M5.2 8Q6 7.3 7.3 7.8L8.9 8.8Q9.2 9.3 8.3 10.2L7.4 12.2L6.3 11.5L6.2 10.2Q4.5 9.6 5.2 8Z')
    land = op(land, globe, po.PathOp.INTERSECTION)
    lock = union(rr(9.45,10.8,5.25,3.9,.8),stroke('M10.35 10.8V9.2A1.72 1.72 0 0 1 13.79 9.2V10.8',1.15))
    lock_space = rr(8.5,6.05,7.6,10,2.4)
    for name, surface in (('earth-lock', land),
                          ('globe-lock', stroke('M1.6 7H11.8M6.7 1.9C3.5 4.6 3.5 9.4 6.7 12.1C9.9 9.4 9.9 4.6 6.7 1.9Z',1.16))):
        shape(name, globe, union(surface,lock), 'world globe security lock')
        edge = stroke(globe,1.25)
        host = subtract(union(edge,surface),lock_space)
        ink = union(host,lock)
        solid = union(subtract(subtract(union(globe,edge),surface),lock_space),lock)
        overrides[name] = {'duotone':[(subtract(globe,union(ink,lock_space)),.24),(ink,1)],
                           'stroke':ink,'solid':solid}

    shape('highlighter',path('M3 10L9.7 3.3L12.7 6.3L6 13H3Z'),stroke('M9 4L12 7M2 14H8',1.1),'marker pen highlighting')
    shape('id-card-lanyard',rr(2.5,5.5,11,8.5,1.3),union(stroke('M5 1.5L8 5.5L11 1.5M6.3 8.5A1.2 1.2 0 1 0 8.7 8.5A1.2 1.2 0 1 0 6.3 8.5M5.5 12Q5.8 10.4 7.5 10.4Q9.2 10.4 9.5 12M10.5 8.5H11.5',1)),'identity badge lanyard')
    shape('key-square',rr(2,2,12,12,1.5),mark('key',8,8,1.2),'security key')
    shape('layout-list',rr(1.5,2,13,12,1),stroke('M4 5H5.5V6.5H4ZM7.5 5.8H12M4 9H5.5V10.5H4ZM7.5 9.8H12',1),'layout list')
    shape('layout-template',rr(1.5,2,13,12,1),stroke('M2 6H14M6 6V14',1),'layout template panels')
    shape('lock-keyhole',rr(3,7,10,7,1.3),union(stroke('M5 7V5A3 3 0 0 1 11 5V7',1.2),circle(8,10,.7),line((8,10.5),(8,12),width=1)),'security locked keyhole')
    shape('lock-keyhole-open',rr(3,7,10,7,1.3),union(stroke('M5 7V5A3 3 0 0 1 11 5',1.2),circle(8,10,.7),line((8,10.5),(8,12),width=1)),'security unlocked keyhole')
    shape('notebook-tabs',rr(3,1.7,9.5,12.6,1),stroke('M5 2V14M12.5 4H14M12.5 7H14M12.5 10H14M7 5H10M7 7H10',1),'notebook index tabs')
    shape('newspaper',rr(2,2.5,12,11,1),stroke('M4 5H8V8H4ZM10 5H12M10 7H12M4 10H12M4 12H12',1),'news paper article')
    shape('vault',rr(1.7,1.7,12.6,12.6,1.3),union(stroke(circle(8,8,3.5),1.1),circle(8,8,.9),stroke('M8 4.5V6M8 10V11.5M4.5 8H6M10 8H11.5M12.5 3V4M12.5 12V13',1)),'safe vault security')
    shape('wallet-minimal',rr(2,4,12,8,1.3),union(stroke('M2 6H12Q14 6 14 8V11',1),circle(11,9,.65)),'money wallet')
    pocket = rr(1.8,6.1,12.4,7.5,1.45)
    cards = path('M3.2 6.5V4.4L10.5 1.95L11.5 4.7L13 4.4V6.5Z')
    stack('wallet-cards',cards,pocket,stroke('M14.2 8.5H11.4A1.25 1.25 0 0 0 11.4 11H14.2',1.15),'money wallet payment cards')

    fist = path('M2.6 6Q2.6 4 4.7 4Q5.15 2.5 7.1 3.2Q8.3 2 9.9 3.3Q12.7 2.8 12.9 5.2L13.4 8.5Q13.6 10.1 12.3 11.5L11.4 13.8H5L4.4 12Q2.6 10.6 2.6 8.3Z')
    shape('hand-fist',fist,stroke('M4.8 4V6.4M7.3 3.4V6M9.9 3.5V5.9M12.8 7.7L9 6.6Q7.3 6.3 7.1 7.6Q7 8.6 8.2 9.1L10 9.9',1.2),'hand closed fist gesture')
    shape('hand-heart',path('M1.5 10L4 8L6 8.5L8 10H11Q13 10 13 11L9 13.5H5L1.5 12Z'),union(stroke('M5 10.5H8.5',1),stroke('M8 7L5.5 5Q4.5 3.8 5.5 2.9Q6.7 2 8 3.5Q9.3 2 10.5 2.9Q11.5 3.8 10.5 5Z',1)),'care giving love hand')
    clasp = path('M1.4 7.2L4 3.7L7.3 4.3L8.6 3.5Q9.5 3 10.6 3.7L14.6 6.2L12.9 9.1L10.5 11.9Q9.8 12.8 8.9 12.2L5.1 10.1L3.9 10.3Z')
    shape('handshake',clasp,stroke('M7.3 4.3L5.8 6.2Q5.1 7.2 6.2 7.7Q6.8 8 7.5 7.5L9.1 6.5L12.2 9.6M7.4 9.5L9.8 11.4',1.16),'agreement partnership handshake')
    fedora = path('M3.7 7.4L5.1 2.5Q5.3 1.8 6.1 2.1L8 2.9L9.9 2.1Q10.7 1.8 10.9 2.5L12.3 7.4Z')
    lenses = union(stroke(circle(4.8,11.6,2.05),1.25), stroke(circle(11.2,11.6,2.05),1.25),
                   stroke('M6.85 11.35Q8 10.5 9.15 11.35',1.15))
    shape('hat-glasses',fedora,union(stroke('M1.8 7.5Q8 8.25 14.2 7.5',1.35),lenses),'incognito disguise hat glasses')
    shape('images',union(rr(1.5,1.5,9,9,1.2),rr(5,5,9.5,9.5,1.2)),union(stroke('M5 6Q5 5 6 5H13.5Q14.5 5 14.5 6V13.5Q14.5 14.5 13.5 14.5H6Q5 14.5 5 13.5ZM5 12L8 9L10 11L12 8.5L14 11',1),circle(8,7,.6)),'photos multiple images')
    shape('lectern',path('M2 4L12.5 2L14 4.5L3.5 6.5Z'),stroke('M8 6V13.5M4.5 14H11.5',1.2),'podium speech presentation')
    shape('library',union(rr(2,3,3,10,.5),rr(5.5,2,3,11,.5),path('M10 3L12 2.5L14 12.5L12 13Z')),stroke('M2 5H5M5.5 4H8.5M2 11H5M5.5 11H8.5M10.5 5L12.5 4.5',1),'books collection library')
    shape('mailbox',union(path('M3 6Q3 3 6 3H11Q14 3 14 6V11H3Z'),path('M6.5 11H10V14H6.5Z')),stroke('M3 6Q3 3 6 3Q9 3 9 6V11M9 7H13M11 3V1.5H13',1),'postal mailbox')
    handset=path('M3 2L5.5 4.5L4.2 6.5Q5.7 9.5 8.8 11L10.8 9.7L13.5 12.5Q12 15 9.5 13.8Q4 11.3 2 6.3Q.8 3.8 3 2Z')
    for suffix, geom in {
        'incoming':'M10 2V6H14M14 2L10 6',
        'outgoing':'M10 6L14 2M10 2H14V6',
        'missed':'M10 2L14 6M14 2L10 6',
    }.items(): shape('phone-'+suffix,transform(handset,0,.8,-1,1),stroke(geom,1.1),'telephone call '+suffix)
    shape('phone-off',handset,line((2,2),(14,14)),'telephone call disabled')
    shape('ribbon',union(circle(8,5.3,3.3),path('M5.8 7.5L4.5 14L8 12.2L11.5 14L10.2 7.5Z')),stroke(circle(8,5.3,1.3),1),'award medal ribbon')
    glyph('rotate-ccw-key',stroke('M5 3Q2 4.5 2 8A6 6 0 0 0 12 12M2 3V6H5'),mark('key',10.5,7,.7),'rotate restore key')
    glyph('rotate-cw-fading-clock',stroke('M3 6A5.5 5.5 0 0 1 13.2 5M10.5 4.5L13.3 5L13.5 2.2M13.5 8Q13.5 10 12 11.7M9.5 13.4L9.4 13.4M6.5 13.4L6.4 13.4M3.5 11.8L3.4 11.7M8 5.2V8.2L10.3 9.5'),None,'clock rotate history')
    stack('save-all', rr(1.7,1.7,9.5,9.5,1), path('M4.8 4.6H11.8L14.3 7.1V14.3H4.8Z'),
          stroke('M7 4.6V7.7H10.4V4.6M7.4 14.3V10.6H11.8V14.3',1.15), 'save multiple files')
    searchbody=stroke(circle(6,6,4),1.3)
    for suffix in ('check','x'):
        glyph('search-'+suffix,union(searchbody,line((9,9),(13,13))),mark(suffix,12.8,3.2,.7),'find search '+suffix)
    glyph('search-code',union(searchbody,line((9,9),(13,13))),stroke('M4.8 4.4L3.3 6L4.8 7.6M7.2 4.4L8.7 6L7.2 7.6',.9),'find search code')
    glyph('settings-2',stroke('M2 4H6M9 4H14M2 8H9M12 8H14M2 12H4M7 12H14M6 2.5H9V5.5H6ZM9 6.5H12V9.5H9ZM4 10.5H7V13.5H4Z',1.1),None,'settings adjustments sliders')
    glyph('share',stroke('M8 10V2M5 5L8 2L11 5M3 8V13H13V8'),None,'share upload')
    glyph('share-2',union(stroke('M5 7L11 4M5 9L11 12',1.1),stroke(circle(3.5,8,1.6),1.1),stroke(circle(12.5,3.5,1.6),1.1),stroke(circle(12.5,12.5,1.6),1.1)),None,'share network nodes')
    shredder = rr(1.7,6.4,12.6,4.4,1.1)
    sheet = path('M4.4 6.4V2H10.4L11.6 3.3V6.4Z')
    stack('shredder',sheet,shredder,stroke('M4.2 10.8V14.2M7 10.8V13.1M9.8 10.8V14.4M12 10.8V12.5',1.25),'paper shredder destroy')
    overrides['shredder']['solid'] = union(subtract(api['stacked_solid'](sheet,shredder),stroke('M4.2 8.6H11.8',1.15)),
                                            stroke('M4.2 10.8V14.2M7 10.8V13.1M9.8 10.8V14.4M12 10.8V12.5',1.25))
    shape('sticker',path('M3 2H12Q14 2 14 4V9L9 14H3Q2 14 2 13V3Q2 2 3 2Z'),stroke('M9 14V9H14',1.1),'peel sticker label')
    shape('switch-camera',rr(1.5,4,13,9,1.5),union(stroke('M5 4L6 2.5H10L11 4M5 8Q5.5 6 8 6Q10 6 11 7.5M11 6.5V8H9.5M11 10Q10.5 12 8 12Q6 12 5 10.5M5 11.5V10H6.5',1)),'camera switch rotate')
    tag_front = path('M1.7 3.6H6.5L12.1 9.2L7.7 13.6L1.7 7.6Z')
    tag_back = path('M5.2 1.7H9.2L14.5 7L10.1 11.4L5.2 6.5Z')
    stack('tags', tag_back, tag_front, circle(4.3,6.1,.82), 'multiple labels tags')
    glyph('timer-reset',stroke('M3 7A5.5 5.5 0 1 1 2.6 10M2 4V7H5M8 5V9L10 10M6 1H10'),None,'timer reset')
    mask = path('M1.6 4.7Q4.1 4.3 6.3 5.5Q8 6.7 9.7 5.5Q11.9 4.3 14.4 4.7L13.8 8.2Q13.2 11.9 10.6 11.7Q9.5 11.7 8 9.8Q6.5 11.7 5.4 11.7Q2.8 11.9 2.2 8.2Z')
    eye = path('M3.4 6.9Q5.5 6.5 6.8 8.45Q4.6 9.25 3.4 6.9Z')
    shape('venetian-mask',mask,union(eye,api['mirror'](eye)),'theater masquerade mask')
    shape('vote',path('M2 9H14V14H2ZM5 3L10 1.5L12 6L7 7.5Z'),stroke('M4 9H12M5.5 11H10.5M7 4.5L8 5.5L9.5 3.5',1),'ballot election voting')

    # Solid styles for overlapping foreground objects need explicit gaps;
    # otherwise the generic silhouette merges the mark into the background.


    mail_solid = subtract(union(mail,stroke(mail,1.25)),union(stroke('M2 4L8 8L14 4',1),circle(12,3,2.4)))
    overrides['mail-badge'] = {'solid':union(mail_solid,circle(12,3,1.55))}
    bricks = union(rr(2,3,4.5,2.2,.2),rr(7,3,4.5,2.2,.2),rr(2,5.8,2.2,2.2,.2),rr(4.8,5.8,4.5,2.2,.2),rr(9.8,5.8,1.7,2.2,.2),rr(2,8.6,4.5,2.2,.2),rr(7,8.6,3.5,2.2,.2),rr(2,11.4,2.2,1.7,.2),rr(4.8,11.4,4.5,1.7,.2))
    shield_badge = path('M12 8L14.5 9V11Q14.5 13 12 14Q9.5 13 9.5 11V9Z')
    fire_badge = path('M12 13Q9.5 11.5 11.5 9Q11.5 10.3 12.5 10Q14 9 13 7.5Q16 10 14 12.5Z')
    for name, badge in (('brick-wall-fire',fire_badge),('brick-wall-shield',shield_badge)):
        overrides[name] = {'solid':union(subtract(bricks,stroke(badge,1.5)),badge)}
    # Cut the final rendered style before adding the slash. Cutting the body
    # first would outline the cut edges and produce two distracting diagonals.
    def disabled_styles(name, source):
        b,d,outline,_,_=api['DRAWINGS'][source]
        outer=stroke(b,1.25) if outline else po.Path()
        boundary=subtract(outer,d) if outer else po.Path()
        duo=[(subtract(b,union(boundary,d)),.24),(union(boundary,d),1)] if outline else [(union(b,d),1)]
        mono=union(outer,d) if outline else union(b,d)
        if outline:
            filled=union(b,outer)
            interior=subtract(filled,stroke(filled,1.8))
            structural=[]; counters=[]
            for component in api['components'](d):
                exterior=subtract(component,filled)
                (structural if exterior.area > component.area*.12 else counters).append(component)
            cut=op(union(*counters),interior,po.PathOp.INTERSECTION)
            solid=union(subtract(filled,cut),*structural)
        else:
            solid=union(b,d)
        clearance=line((2,2),(14,14),width=2.7)
        slash=line((2,2),(14,14))
        overrides[name]={
            'duotone':[(subtract(layer,clearance),alpha) for layer,alpha in duo]+[(slash,1)],
            'solid':union(subtract(solid,clearance),slash),
            'stroke':union(subtract(mono,clearance),slash),
        }
    for name, source in (
        ('alarm-clock-off','alarm-clock'),('bookmark-off','bookmark'),('calendar-off','calendar'),
        ('captions-off','captions'),('cctv-off','cctv'),('flag-off','flag'),('heart-off','heart'),
        ('image-off','image'),('lightbulb-off','lightbulb'),('map-pin-off','map-pin'),
        ('message-circle-off','message-circle'),('message-square-off','message'),
        ('monitor-off','monitor'),('pin-off','pin'),('power-off','power'),('save-off','save'),
        ('screen-share-off','screen-share'),('server-off','server-rack'),('shield-off','shield'),
        ('star-off','star'),('timer-off','timer'),('touchpad-off','touchpad'),('trash-off','trash'),
        ('video-off','video-call'),('wrench-off','wrench'),('zap-off','zap'),
    ):
        disabled_styles(name,source)

    # A diagonal running opposite to the handset keeps this disabled state
    # recognizable; a parallel slash would disappear into its silhouette.
    phone_base=union(handset,stroke(handset,1.25))
    phone_slash=line((2,14),(14,2))
    phone_gap=line((2,14),(14,2),width=2.7)
    overrides['phone-off']={'duotone':[(subtract(handset,union(phone_gap,stroke(handset,1.25))),.24),(union(subtract(stroke(handset,1.25),phone_gap),phone_slash),1)],'solid':union(subtract(phone_base,phone_gap),phone_slash),'stroke':union(subtract(stroke(handset,1.25),phone_gap),phone_slash)}
    overrides['package-open'] = {'solid':subtract(union(carton,stroke(carton,1.25)),flap_seams)}
    for name, bubble in (('messages-circle',bubble_round),('messages-square',bubble_square)):
        back=transform(bubble,0,.72,-2,-2)
        front=transform(bubble,0,.72,2,2)
        overrides[name]={'solid':api['stacked_solid'](back,front)}

    # Half-state symbols need an actual half-filled silhouette, not a seam
    # dividing two identical halves. Keep the right counter open in every style.
    for name in ('star-half', 'shield-half'):
        body = api['DRAWINGS'][name][0]
        outline = stroke(body, 1.25)
        half = op(body, rr(0, 0, 8, 16, 0), po.PathOp.INTERSECTION)
        ink = union(outline, half)
        overrides[name] = {'duotone': [(subtract(body, ink), .24), (ink, 1)],
                           'solid': ink, 'stroke': ink}

    # Foreground seams in Solid are open gaps between objects. Reusing an
    # interior contour as a counter leaves an unstable hairline double border.
    for suffix in ('check', 'plus', 'x'):
        overrides['copy-'+suffix] = {'solid': api['stacked_solid'](
            rr(2,2,8,9,1), rr(5,5,9,9,1), mark(suffix,9.5,9.5,.65))}
    for name, back, front, detail in (
        ('mails', rr(1.5,2,10,8,1), rr(4.5,5,10,8,1), stroke('M4.5 5L9.5 8L14.5 5',1)),
        ('files', path('M2 1.7H8L11 4.7V12.5H2Z'), path('M5 4H11L14 7V14.3H5Z'), stroke('M11 4V7H14',1)),

        ('images', rr(1.5,1.5,9,9,1.2), rr(5,5,9.5,9.5,1.2), union(stroke('M5 12L8 9L10 11L12 8.5L14 11',1),circle(8,7,.6))),

    ):
        overrides[name] = {'solid': api['stacked_solid'](back, front, detail)}

    # Use exactly the same foreground outline as its surface; the earlier
    # independently drawn line left hooks at the tails of stacked bubbles.
    for name, bubble in (('messages-circle',bubble_round),('messages-square',bubble_square)):
        back = transform(bubble,scale=.72,dx=-2,dy=-2)
        front = transform(bubble,scale=.72,dx=2,dy=2)
        contour = union(subtract(stroke(back,1.25),front),stroke(front,1.25))
        overrides[name].update({'duotone':[(subtract(union(back,front),contour),.24),(contour,1)],
                                'stroke':contour})

    # Badge strokes must never merge into a host contour. Cut the final ink,
    # preserving a half-unit transparent channel without outlining that cut.
    def detach_badge(name, badge):
        body, details, _, _, _ = api['DRAWINGS'][name]
        host_detail = subtract(details,badge)
        outer = stroke(body,1.25)
        filled = union(body,outer)
        interior = subtract(filled,stroke(filled,1.8))
        structural, counters = [], []
        for component in api['components'](host_detail):
            exterior = subtract(component,filled)
            (structural if exterior.area > component.area*.12 else counters).append(component)
        solid = union(subtract(filled,op(union(*counters),interior,po.PathOp.INTERSECTION)),*structural)
        gap = union(badge,stroke(badge,1.3))
        if 'cog' in name:
            # Reserve the hub as well as the valleys between the teeth.
            left, top, right, bottom = badge.bounds
            gap = circle((left+right)/2, (top+bottom)/2, (right-left)/2 + .95)
        ink = union(subtract(union(outer,host_detail),gap),badge)
        overrides[name] = {'duotone':[(subtract(body,union(gap,ink)),.24),(ink,1)],
                           'stroke':ink,'solid':union(subtract(solid,gap),badge)}

    for name in ('hourglass-cog','monitor-cog','server-cog'):
        detach_badge(name,mark('cog',12,11.8,.68))
    for name in ('user-cog','user-round-cog'):
        detach_badge(name,mark('cog',12,9.5,.68))
    for suffix in ('check','plus','x'):
        detach_badge('calendar-'+suffix+'-2',compact(suffix,12.35,12.35,.8))
    detach_badge('database-backup',stroke('M10.5 12Q11 10 13 10Q14.5 10 14.8 11.5M14.8 10V11.6H13M14 13Q12.5 14.3 11 13',1))
    for suffix in ('check','cog','minus','plus','search','x'):
        detach_badge('database-'+suffix,mark(suffix,12.35 if suffix == 'cog' else 12.5,12,.62))
    for suffix in ('check','minus','pen','plus','question-mark','search','x'):
        detach_badge('package-'+suffix,mark(suffix,12,11.5,.7))
    for suffix in ('cog','minus','plus','question-mark','user'):
        detach_badge('shield-'+suffix,mark(suffix,12,10.8,.65))
    detach_badge('shield-cog-corner',mark('cog',10.8,12,.75))
    for prefix in ('user','user-round'):
        for suffix in ('shield','star'):
            detach_badge(prefix+'-'+suffix,api['DRAWINGS'][prefix+'-'+suffix][1])

    # Preserve the security badge as the foreground surface, with the brick
    # pattern ending behind it instead of showing through its counter.
    for name, badge in (('brick-wall-fire',fire_badge),('brick-wall-shield',shield_badge)):
        body, _, _, _, _ = api['DRAWINGS'][name]
        brick_lines = stroke('M2 6H12M2 9.5H12M5 3V6M9 6V9.5M5 9.5V13',1)
        border = stroke(badge,1.1)
        gap = union(badge,stroke(badge,2.2))
        ink = union(subtract(union(stroke(body,1.25),brick_lines),gap),border)
        overrides[name].update({'duotone':[(subtract(union(subtract(body,gap),badge),ink),.24),(ink,1)],'stroke':ink})
