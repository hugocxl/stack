"""Original product-interface additions, drawn on the CXL 16-unit grid."""

import math


def register(api):
    shape, glyph = api['shape'], api['glyph']
    path, rr, circle = api['path'], api['rr'], api['circle']
    stroke, line, lines, union = api['stroke'], api['line'], api['lines'], api['union']
    transform, dots = api['transform'], api['dots']
    check, plus, cross = api['check'], api['plus'], api['cross']
    api['CATEGORY'] = 'Interface controls'

    def mark(kind, x=8, y=8, scale=1):
        # Compact symbols are deliberately drawn for their available interior.
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
            'cog': 'M8 5V6M8 10V11M5 8H6M10 8H11M5.9 5.9L6.6 6.6M9.4 9.4L10.1 10.1M10.1 5.9L9.4 6.6M6.6 9.4L5.9 10.1M6.7 8A1.3 1.3 0 1 0 9.3 8A1.3 1.3 0 1 0 6.7 8',
            'text': 'M5.7 6H10.3M5.7 8H10.3M5.7 10H9',
            '1': 'M7.2 6L8.5 5V11M7 11H10',
        }[kind]
        q = circle(8, 8, .8) if kind == 'dot' else stroke(p, 1.05)
        return q.transform(scale, 0, 0, scale, x-8*scale, y-8*scale)

    # Shared silhouettes: interior variants are kept within the surface rather
    # than allowing the status symbol to collide with the outline.
    badge = path('M8 1.4L10.1 2.5L12.5 2.7L13.4 5L14.6 7.2L13.7 9.6L13.2 12.1L10.7 12.9L8.5 14.5L6 13.4L3.6 13L2.8 10.6L1.5 8.3L2.5 6L3 3.6L5.5 3Z')
    shape('badge', badge, None, 'award seal')
    for suffix in ('exclamation-point','info','minus','plus','x'):
        shape('badge-'+suffix, badge, mark(suffix), 'award seal '+suffix)

    book = rr(3, 1.6, 10, 12.8, 1)
    for suffix in ('check','heart','lock','minus','plus','search','text','user','x'):
        shape('book-'+suffix, book, union(stroke('M5 2V11M3.2 11.2H12.8',1), mark(suffix,9,6.9,.75)), 'book '+suffix)
    bookmark = path('M4 2H12V14L8 11L4 14Z')
    for suffix in ('minus','x'):
        shape('bookmark-'+suffix, bookmark, mark(suffix,8,6.5,.8), 'bookmark '+suffix)
    shape('bookmark-off', bookmark, line((2,2),(14,14)), 'bookmark disabled')

    cal = rr(2.2,3,11.6,10.6,1.3)
    top = stroke('M2.5 6H13.5M5 1.7V4.1M11 1.7V4.1',1.1)
    for suffix in ('1','arrow-down','arrow-left','arrow-right','arrow-up','chevrons-left','chevrons-right','cog','minus','search','sync'):
        shape('calendar-'+suffix, cal, union(top, mark(suffix,8,9.6,.75)), 'calendar date '+suffix)
    # The numbered versions denote marks placed outside the date grid.
    for suffix in ('check','minus','plus','x'):
        small = rr(1.8,3,8,8.8,1.1)
        shape('calendar-'+suffix+'-2', small, union(stroke('M2 5.8H9.6M4 1.8V4M7.6 1.8V4',1.05), mark(suffix,12,11.5,.78)), 'calendar date '+suffix)
    shape('calendar-off', cal, union(top,line((2,2),(14,14))), 'calendar disabled')
    shape('calendar-fold', cal, union(top,stroke('M9.5 13.4V10.1H13',1.05)), 'calendar folded date')
    shape('calendars', union(rr(1.8,2.4,9.5,9.3,1.2), rr(4.5,5,9.5,9.3,1.2)), stroke('M4.5 7.6H14M7 3.8V6M11.5 3.8V6',1.05), 'multiple dates calendars')

    # Clock faces use independently calculated hands for each hour.
    for hour in range(1,13):
        angle = math.pi*hour/6
        hx, hy = 8+2.8*math.sin(angle), 8-2.8*math.cos(angle)
        shape('clock-'+str(hour), circle(8,8,6), stroke(f'M8 4.2V8L{hx:.3f} {hy:.3f}',1.15), 'time hour '+str(hour))
    for suffix in ('arrow-down','arrow-left','arrow-right','arrow-up','check','exclamation-point','plus'):
        shape('clock-'+suffix, circle(6.5,7,4.8), union(stroke('M6.5 4.2V7L8.3 8',1.05), mark(suffix,12,12,.6)), 'time '+suffix)
    glyph('clock-fading', stroke('M13.5 8A5.5 5.5 0 0 1 8 13.5M2.5 8A5.5 5.5 0 0 1 8 2.5A5.5 5.5 0 0 1 13.5 8M8 4.5V8L10.3 9.3'), dots((3.3,11),(5.3,13),r=.6), 'time history fading')

    clip = rr(3,3,10,11,1.4)
    cliptop = rr(5.5,1.6,5,2.8,.8)
    for suffix in ('clock','minus','plus','x','pen'):
        shape('clipboard-'+suffix, clip, union(cliptop,mark(suffix,8,9,.8)), 'clipboard '+suffix)
    shape('clipboard-list',clip,union(cliptop,stroke('M5.5 7H6M8 7H10.5M5.5 9.5H6M8 9.5H10.5M5.5 12H6M8 12H10.5',1)), 'clipboard checklist')
    shape('clipboard-copy',clip,union(cliptop,stroke('M5 7H9V11H5ZM7 5.5H11V9.5',1)), 'clipboard copy')
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
        'pen-line':'M5 13H11M5.5 11L6 9.5L9.5 6L10.7 7.2L7.2 10.7Z',
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
        detail_layer = stroke(detail,.95) if suffix in ('braces','type') else union(fold,stroke(detail,.95))
        if suffix == 'axis-3d':
            body = transform(doc,0,.66,-2.4,-1.7)
            detail_layer = union(transform(fold,0,.66,-2.4,-1.7),lines('M11.3 10.1V6.8','M10.4 7.7L11.3 6.8L12.2 7.7','M11.3 10.1L8.7 12.6','M8.7 11.5V12.6H9.8','M11.3 10.1L13.9 12.6','M12.8 12.6H13.9V11.5'))
        if suffix in ('input','output'):
            body = transform(doc,0,.72,-2,-1.3)
            detail_layer = union(transform(fold,0,.72,-2,-1.3),mark('arrow-left' if suffix == 'input' else 'arrow-right',12,11,.75))
        shape('file-'+suffix,body,detail_layer, 'document file '+suffix.replace('-',' '))
    shape('files', union(path('M2 1.7H8L11 4.7V12.5H2Z'),path('M5 4H11L14 7V14.3H5Z')),stroke('M5 4V14M5 4H11V7H14',1), 'multiple documents files')
    shape('file-stack', union(path('M2 2H10L12.5 4.5V12H2Z'),path('M4 4H11.5L14 6.5V14H4Z')),stroke('M4 4V14H14V6.5H11.5V4',1), 'documents stack')

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
        shape('folder-'+suffix,folder,stroke(detail,.95),'directory folder '+suffix.replace('-',' '))
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
        'quote':'M5 5H7V7H5V9M9 5H11V7H9V9',
        'reply':'M6.5 5L4.8 6.8L6.5 8.5M5 6.8H9Q11 6.8 11 9',
        'share':'M6.5 8.5L10.5 4.8M8 4.8H10.5V7.3M5 5H4.5V9H9V8.5',
        'x':'M6 5L10 9M10 5L6 9',
    }
    for suffix, detail in square_details.items():
        shape('message-square-'+suffix,bubble_square,stroke(detail,1),'message chat '+suffix)
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
    groupbody=union(circle(5,5,2),circle(11,5,2),path('M1.5 13Q1.5 9 5 9Q8 9 8 13ZM8 13Q8 9 11 9Q14.5 9 14.5 13Z'))
    shape('user-group',union(groupbody,circle(8,3,1.5)),line((8,10.3),(8,13),width=1),'people group')
    glyph('user-round-group',union(stroke('M1.5 13Q1.5 9.5 5 9.5Q8 9.5 8 13M8 13Q8 9.5 11 9.5Q14.5 9.5 14.5 13',1.1),stroke(circle(5,5,2),1.1),stroke(circle(11,5,2),1.1),stroke(circle(8,2.5,1),1.1)),None,'people round group')
    glyph('users-round',union(stroke('M1.5 13Q1.5 9.5 5 9.5Q8 9.5 8 13M8 13Q8 9.5 11 9.5Q14.5 9.5 14.5 13',1.1),stroke(circle(5,5,2),1.1),stroke(circle(11,5,2),1.1)),None,'people round group')
    shape('users-collaboration',groupbody,union(line((8,10.3),(8,13),width=1),stroke('M6 7.5L8 8.5L10 7.5',1)),'people collaboration')
    glyph('users-round-collaboration',union(stroke('M1.5 13Q1.5 9.5 5 9.5Q8 9.5 8 13M8 13Q8 9.5 11 9.5Q14.5 9.5 14.5 13',1.1),stroke(circle(5,5,2),1.1),stroke(circle(11,5,2),1.1),stroke('M6 7.5L8 8.5L10 7.5',1)),None,'people collaboration')

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
        shape('database-'+suffix,db,union(dbdetail,mark(suffix,12.5,12,.62)),'storage database '+suffix)
    shape('database-backup',db,union(dbdetail,stroke('M10.5 12Q11 10 13 10Q14.5 10 14.8 11.5M14.8 10V11.6H13M14 13Q12.5 14.3 11 13',1)), 'database backup restore')
    pack = path('M1.5 4L6.2 1.8L10.8 4V10L6.2 12.5L1.5 10Z')
    packdetail=stroke('M1.5 4L6.2 6.5L10.8 4M6.2 6.5V12.5',1)
    for suffix in ('check','minus','pen','plus','question-mark','search','x'):
        shape('package-'+suffix,pack,union(packdetail,mark(suffix,12,11.5,.7)),'parcel package '+suffix)
    shape('package-2',path('M2 4L8 1.5L14 4V12L8 14.5L2 12Z'),stroke('M2 4L8 7L14 4M8 7V14M5 2.8L11 5.5',1),'parcel box shipping')
    shape('package-open',path('M3 6L8 4L13 6V12L8 14.5L3 12Z'),stroke('M3 6L.9 4L5.8 1.8L8 4L10.2 1.8L15.1 4L13 6L15 8L10 10L8 7L6 10L1 8ZM8 7V14',1),'parcel open box')
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
            shape(kind+'-'+suffix,body,mark(suffix,8,8,1),'status '+suffix)
    shape('square-check-big',rr(2,2,12,12,1.7),check(8,8,.8),'status checked')
    shape('circle-check-big',circle(8,8,6),check(8,8,.8),'status checked')
    percent = stroke('M5.2 10.8L10.8 5.2M5 5A.8 .8 0 1 0 6.6 5A.8 .8 0 1 0 5 5M9.4 11A.8 .8 0 1 0 11 11A.8 .8 0 1 0 9.4 11',1)
    shape('circle-percent',circle(8,8,6),percent,'percentage ratio')
    shape('square-percent',rr(2,2,12,12,1.7),percent,'percentage ratio')
    shape('diamond-percent',path('M8 1.6L14.4 8L8 14.4L1.6 8Z'),percent,'percentage ratio')
    shape('square-user',rr(2,2,12,12,1.7),mark('user',8,8,1.3),'account profile')
    shape('square-user-round',rr(2,2,12,12,1.7),union(stroke(circle(8,6,1.7),1),stroke('M4.8 11.5Q4.8 8.5 8 8.5Q11.2 8.5 11.2 11.5',1)), 'account round profile')
    shape('circle-user-round',circle(8,8,6),mark('user',8,8,1.3),'account round profile')
    shape('octagon-x',path('M5 1.8H11L14.2 5V11L11 14.2H5L1.8 11V5Z'),mark('x'),'stop close')
    glyph('circle-fading-check',stroke('M13.5 8A5.5 5.5 0 0 1 8 13.5M2.5 8A5.5 5.5 0 0 1 8 2.5A5.5 5.5 0 0 1 13.5 8M3.3 11L3.4 11.1M5.2 13L5.3 13.1'),mark('check'),'fading completed')
    glyph('circle-fading-plus',stroke('M13.5 8A5.5 5.5 0 0 1 8 13.5M2.5 8A5.5 5.5 0 0 1 8 2.5A5.5 5.5 0 0 1 13.5 8M3.3 11L3.4 11.1M5.2 13L5.3 13.1'),mark('plus'),'fading add')

    # Disabled versions reuse the actual subject, cut a channel through it,
    # and place the slash in that channel so the two marks remain legible.
    op, po = api['op'], api['po']
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
        'reply-all':'M14 12Q13 7 8 7H6V4L2.5 8L6 12V9H8Q11.5 9 14 12ZM4 4L.8 8L4 12',
        'send-horizontal':'M1.5 2L14.5 8L1.5 14L3.5 8ZM3.5 8H14',
        'locate':'M8 3A5 5 0 1 0 8 13A5 5 0 1 0 8 3M8 1.3V4M8 12V14.7M1.3 8H4M12 8H14.7',
        'locate-fixed':'M8 3A5 5 0 1 0 8 13A5 5 0 1 0 8 3M8 1.3V4M8 12V14.7M1.3 8H4M12 8H14.7M6.5 8A1.5 1.5 0 1 0 9.5 8A1.5 1.5 0 1 0 6.5 8',
        'list-checks':'M2 4L3 5L5 3M7 4H14M2 9L3 10L5 8M7 9H14M7 13H14',
        'list-filter':'M2 3H14M4 7H12M6 11H10M7.5 14H8.5',
        'list-tree':'M3 2V13H6M3 5H6M8 4H14M8 9H14M8 13H14M6 8H7V10H6ZM6 12H7V14H6Z',
        'spell-check':'M2 9L4 3L6 9M2.8 7H5.2M8 3H10Q12 3 12 4.5Q12 6 10 6H8ZM8 6H10.5Q12.5 6 12.5 7.5Q12.5 9 10.5 9H8ZM8 12L9.5 13.5L13 10',
        'regex':'M2 10V10.1M7 5V11M4.5 6.5L9.5 9.5M4.5 9.5L9.5 6.5M12 10V10.1',
        'nfc':'M5 3Q1 8 5 13M7.5 4.5Q5 8 7.5 11.5M10 6Q9 8 10 10M12.5 7V9',
        'waypoints':'M3 4L8 8L13 4M8 8L12 12M1.5 4A1.5 1.5 0 1 0 4.5 4A1.5 1.5 0 1 0 1.5 4M11.5 4A1.5 1.5 0 1 0 14.5 4A1.5 1.5 0 1 0 11.5 4M10.5 12A1.5 1.5 0 1 0 13.5 12A1.5 1.5 0 1 0 10.5 12M6.5 8A1.5 1.5 0 1 0 9.5 8A1.5 1.5 0 1 0 6.5 8',
        'voicemail':'M1.8 8A3.2 3.2 0 1 0 8.2 8A3.2 3.2 0 1 0 1.8 8M7.8 8A3.2 3.2 0 1 0 14.2 8A3.2 3.2 0 1 0 7.8 8M5 11.2H11',
        'webhook':'M7 4A2 2 0 1 1 10.5 5.3M8 4L5 10M4 9A2 2 0 1 0 5.5 12.5M5 11H11M11 9A2 2 0 1 1 11 13M11.7 10L9 5.3',
    }.items():
        glyph(name,stroke(geom),None,name.replace('-',' '))
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
        glyph('wifi-'+suffix,union(circle(8,12,1),dots((3,5.5),(5.5,4),(8,3.5),(10.5,4),(13,5.5),r=.65)) if suffix == 'zero' else (union(stroke(geom),dots((3,5.5),(5.5,4),(8,3.5),(10.5,4),(13,5.5),r=.55)) if suffix == 'low' else stroke(geom)),None,'wireless signal '+suffix)

    def badged(name, source, suffix):
        b,d,_,_,_=api['DRAWINGS'][source]
        shape(name,transform(b,0,.72,-1.8,-1.5),union(transform(d,0,.72,-1.8,-1.5),mark(suffix,12,11.8,.68)),name.replace('-',' '))
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
        'timeline':'M2 8H14M4 5V11M8 5V11M12 5V11M3 3H5M7 13H9M11 3H13',
        'ungroup':'M2 6V2H6M10 2H14V6M2 10V14H6M10 14H14V10M5 5H9V9H5ZM8 8H12V12H8Z',
        'panel-left-close':'M2 3H14V13H2ZM6 3V13M12 6L9 8L12 10',
        'panel-left-open':'M2 3H14V13H2ZM6 3V13M9 6L12 8L9 10',
        'table-cells-merge':'M1.3 2.3H9V10H1.3ZM1.3 6.1H9M5.1 2.3V6.1M5.1 6.1V10M9.2 10L10.8 11.5L9.2 13M14.8 10L13.2 11.5L14.8 13',
        'table-cells-split':'M1.3 2.3H9V10H1.3ZM1.3 6.1H9M5.1 2.3V10M10.8 10L9.2 11.5L10.8 13M13.2 10L14.8 11.5L13.2 13',
    }.items(): glyph(name,stroke(geom,1.1),None,name.replace('-',' '))

    api['CATEGORY'] = 'Symbols'
    for suffix, geom in {
        'aquarius':'M2 6L4 4L6 6L8 4L10 6L12 4L14 6M2 12L4 10L6 12L8 10L10 12L12 10L14 12',
        'aries':'M8 14V7Q8 2 4.5 2Q2 2 2 5M8 7Q8 2 11.5 2Q14 2 14 5',
        'cancer':'M4.5 3.5A2 2 0 1 0 4.5 7.5A2 2 0 1 0 4.5 3.5M4.5 3.5H11.5M11.5 8.5A2 2 0 1 0 11.5 12.5A2 2 0 1 0 11.5 8.5M4.5 12.5H11.5',
        'capricorn':'M2 4L4 10L6 4L8.5 12Q9.5 14.5 12 13Q14 11.5 12 9.8Q10.5 8.8 9 10',
        'gemini':'M3 2.5Q8 4 13 2.5M5 3.5V12.5M11 3.5V12.5M3 13.5Q8 12 13 13.5',
        'leo':'M4 7A2.5 2.5 0 1 1 7 4.5Q7 6.5 5.5 8.5Q4 11 6 12.5Q8 14 10 11Q11 9.5 12.5 10.5Q14 11.5 13 13',
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
    shape('cog',path('M7 1.5H9L9.5 3.2L11 3.8L12.6 3L14 4.4L13.2 6L13.8 7.5L15 8L14.5 10L12.8 10.5L12.2 12L13 13.5L11.5 14.5L10 13.7L8.5 14L8 15L6 14.5L5.5 13L4 12.4L2.5 13L1.5 11.5L2.3 10L1.8 8.5L1 8L1.5 6L3 5.5L3.6 4L3 2.5L4.5 1.5L6 2.3Z'),stroke(circle(8,8,2.2),1.1),'gear settings')
    shape('earth-lock',circle(6.5,7,5),union(stroke('M3 4.2L5.2 4L5.8 5L4.8 6L5.3 7.3L4.6 8.2L3.3 7.1L2.2 7M7 2.2L7.8 3.5L9.3 3.8L9.8 5L8.5 5.4L8 6.7L9 7.5M5.7 9L6.8 8.7L7.8 9.6L7.5 11.6',.9),mark('lock',12,12,.7)),'earth world security')
    shape('globe-lock',circle(6.5,7,5),union(union(stroke('M2 5.5H11M2 8.5H10',1),stroke('M6.5 2V12',1),stroke('M6.5 2Q3.5 7 6.5 12',1),stroke('M6.5 2Q9 5 9 8',1)),mark('lock',12,12,.7)),'globe world security')
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
    shape('wallet-cards',rr(2,5,12,8,1.3),union(stroke('M3.5 5V2.5H11V5M2 8H14',1),circle(11,10,.65)),'money wallet payment cards')

    shape('hand-fist',path('M3 7V5.5Q3 4.5 4.2 4.5Q4.8 4.5 5 5Q5 3.8 6.2 3.8Q7 3.8 7.3 4.5Q7.5 3.5 8.7 3.5Q9.7 3.5 10 4.5Q10.5 4 11.4 4.4Q12 4.7 12 5.7V8L13.2 7.2Q14.5 6.6 14.2 8L12.5 11.8Q12 13 11 14H5L4.3 12Q3 11 3 9Z'),stroke('M5 5V7M7.4 4.5V7M10 4.7V7M4.5 9Q7 8 9.5 9',1),'hand closed fist gesture')
    shape('hand-heart',path('M1.5 10L4 8L6 8.5L8 10H11Q13 10 13 11L9 13.5H5L1.5 12Z'),union(stroke('M5 10.5H8.5',1),stroke('M8 7L5.5 5Q4.5 3.8 5.5 2.9Q6.7 2 8 3.5Q9.3 2 10.5 2.9Q11.5 3.8 10.5 5Z',1)),'care giving love hand')
    shape('handshake',path('M1.5 6L4 3L7 4L9 3L14.5 6L12.5 10L10.5 12L9 11.5L8 12.8L6.5 12L5.5 12L2.5 9Z'),stroke('M7 4L5.5 6Q5 7 6 7.5Q7 8 9 6.5L12.5 10M6 9L8.5 11.5M4.5 10L6.5 12',1),'agreement partnership handshake')
    shape('hat-glasses',union(path('M2 7H14L12.5 5H3.5Z'),rr(3.5,8,3.5,2.7,.8),rr(9,8,3.5,2.7,.8)),stroke('M4 5L5 1.8H11L12 5M7 9H9M2 8.5L3.5 9M12.5 9L14 8.5',1),'incognito disguise hat glasses')
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
    shape('save-all',union(rr(1.5,1.5,9.5,9.5,1),path('M5 4H11.5L14 6.5V14H5Z')),stroke('M5 4V14H14V6.5H11.5V4M7 4V7H11V4M7 14V10H12V14',1),'save multiple files')
    searchbody=stroke(circle(6,6,4),1.3)
    for suffix in ('check','x'):
        glyph('search-'+suffix,union(searchbody,line((9,9),(13,13))),mark(suffix,11.7,4,.65),'find search '+suffix)
    glyph('search-code',union(searchbody,line((9,9),(13,13))),stroke('M4.8 4.4L3.3 6L4.8 7.6M7.2 4.4L8.7 6L7.2 7.6',.9),'find search code')
    glyph('settings-2',stroke('M2 4H6M9 4H14M2 8H9M12 8H14M2 12H4M7 12H14M6 2.5H9V5.5H6ZM9 6.5H12V9.5H9ZM4 10.5H7V13.5H4Z',1.1),None,'settings adjustments sliders')
    glyph('share',stroke('M8 10V2M5 5L8 2L11 5M3 8V13H13V8'),None,'share upload')
    glyph('share-2',union(stroke('M5 7L11 4M5 9L11 12',1.1),stroke(circle(3.5,8,1.6),1.1),stroke(circle(12.5,3.5,1.6),1.1),stroke(circle(12.5,12.5,1.6),1.1)),None,'share network nodes')
    shape('shredder',rr(1.5,3,13,7,1.2),union(stroke('M4 6H12M4 12V14M6.5 12V14M9 12V14M11.5 12V14',1.1)),'paper shredder destroy')
    shape('sticker',path('M3 2H12Q14 2 14 4V9L9 14H3Q2 14 2 13V3Q2 2 3 2Z'),stroke('M9 14V9H14',1.1),'peel sticker label')
    shape('switch-camera',rr(1.5,4,13,9,1.5),union(stroke('M5 4L6 2.5H10L11 4M5 8Q5.5 6 8 6Q10 6 11 7.5M11 6.5V8H9.5M11 10Q10.5 12 8 12Q6 12 5 10.5M5 11.5V10H6.5',1)),'camera switch rotate')
    shape('tags',union(path('M1.5 3H7L12 8L8 12L3 7V4Z'),path('M5 3H9L14 8L10 12')),union(circle(4.5,5.5,.7),stroke('M10 12L12 14L15 11',1)),'multiple labels tags')
    glyph('timer-reset',stroke('M3 7A5.5 5.5 0 1 1 2.6 10M2 4V7H5M8 5V9L10 10M6 1H10'),None,'timer reset')
    shape('venetian-mask',path('M1.5 5Q4 4 6 5L8 7L10 5Q12 4 14.5 5L13 10Q12 12 10 11L8 9L6 11Q4 12 3 10Z'),union(stroke('M3.5 7Q5 6 6.5 8M9.5 8Q11 6 12.5 7',1),stroke('M8 2V4',1)),'theater masquerade mask')
    shape('vote',path('M2 9H14V14H2ZM5 3L10 1.5L12 6L7 7.5Z'),stroke('M4 9H12M5.5 11H10.5M7 4.5L8 5.5L9.5 3.5',1),'ballot election voting')

    # Solid styles for overlapping foreground objects need explicit gaps;
    # otherwise the generic silhouette merges the mark into the background.
    overrides = api.setdefault('STYLE_OVERRIDES', {})
    subtract = lambda a,b: op(a,b,po.PathOp.DIFFERENCE)
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
    pack_open=api['DRAWINGS']['package-open'][0]
    solid_pack=union(pack_open,stroke(pack_open,1.25))
    seam=stroke('M3 6L8 8L13 6M8 8V14',1.2)
    flaps=stroke('M3 6L1 4L5.8 1.8L8 4L10.2 1.8L15 4L13 6L15 8L10 10L8 7L6 10L1 8Z',1.15)
    overrides['package-open']={'solid':union(subtract(solid_pack,seam),flaps)}
    for name, bubble in (('messages-circle',bubble_round),('messages-square',bubble_square)):
        back=transform(bubble,0,.72,-2,-2)
        front=transform(bubble,0,.72,2,2)
        overrides[name]={'solid':api['stacked_solid'](back,front)}
