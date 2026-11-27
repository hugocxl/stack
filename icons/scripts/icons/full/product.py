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
        ink = union(subtract(stroke(back), front), stroke(front), detail)
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
            return union(stroke(circle(x,y-1.68*scale,1.33*scale)),
                         stroke(position(path('M5.5 10.95Q5.9 9.5 8 9.5Q10.1 9.5 10.5 10.95'))))
        if kind == 'pen':
            return stroke(position(path('M4.95 11L5.25 8.65L9.05 4.85L10.95 6.75L7.05 10.65Z')))
        if kind == 'lock':
            return union(stroke(rr(x-2.45*scale,y,4.9*scale,3.1*scale)),
                         stroke(position(path('M6.35 8V6.1A1.65 1.65 0 0 1 9.65 6.1V8'))))
        if kind in ('info','exclamation-point','question-mark'):
            geom = {'info':'M8 7.2V10.7','exclamation-point':'M8 5.1V8.35',
                    'question-mark':'M6.2 6.1Q6.45 4.8 8 4.8C10.4 4.8 10.45 7 9 7.8Q8 8.4 8 8.8'}[kind]
            dot_y = {'info':4.75,'exclamation-point':10.95,'question-mark':11.35}[kind]
            return union(stroke(position(path(geom))),circle(x,y+(dot_y-8)*scale,.69))
        if kind == 'heart':
            scale *= .84
            return stroke(position(path('M8 11.2L5.35 8.7C2.9 6.25 5.85 3.95 8 6.2C10.15 3.95 13.1 6.25 10.65 8.7Z')))
        if kind == 'key':
            return union(stroke(position(circle(6.45,6.45,1.65))),
                         stroke(position(path('M7.7 7.7L10.7 10.7L11.15 10.25M9.3 9.3L10.55 8.05'))))
        paths = {
            'check':'M5.4 8L7.3 9.85L10.7 6.15', 'x':'M6.05 5.8L9.95 10.2M9.95 5.8L6.05 10.2',
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
        return stroke(position(path(paths[kind])))

    def recess(body, gap):
        # Turn the edge of the host around the foreground badge. The rounded
        # shoulder both reserves the badge's clearance and closes the host.
        return stroke(subtract(body, gap))

    def host_drawing(source):
        body, detail, outline, category, tags = api['DRAWINGS'][source]
        # These baseline contours occupy the full bleed before outlining.
        # Inset the unexpanded body by less than a tenth of a grid unit.
        if source in ('cloud','map-pin','lightbulb','wrench','database'):
            body = transform(body,scale=.985)
        return body, detail, outline, category, tags

    corner_badges = {}
    def corner_host(source):
        # Map the construction grid before expanding its lines. These small
        # hosts retain the same bells, lid, handle and rack bays as the bases.
        if source == 'alarm-clock':
            cx, cy, s = 6.45, 7.14, .84
            def centerline(d):
                return stroke(path(d).transform(s,0,0,s,cx-8*s,cy-8*s))
            return (circle(cx,cy,5.8*s),
                    centerline('M8 4V8H11M2 3L4 1M12 1L14 3M3 14L4 12M12 12L13 14'))
        if source == 'archive':
            body = rr(2.2,4.8,7.95,6.0)
            lid = rr(1.45,2.25,9.45,2.55)
            return body, union(lid,stroke('M4.95 7.3H8.05'))
        body, detail = host_drawing(source)[:2]
        # Leave space beside the original silhouette. Fit filled bodies and
        # detail centerlines first, then expand the contours at the family weight.
        if source in ('user','user-round'):
            head, shoulders = sorted(api['components'](body),key=lambda p:p.bounds[1])
            fitted = union(transform(head,scale=.67,dx=-2.95,dy=-1.1),
                           transform(shoulders,scale=.67,dx=-2.95,dy=-.25))
            return fitted, detail
        if source == 'tag':
            return transform(body,scale=.7,dx=-1.85,dy=-1.6),transform(detail,scale=.7,dx=-1.85,dy=-1.6)
        scale, dx, dy = .75, -1.65, -1.25
        def fit(p):
            return transform(p,scale=scale,dx=dx,dy=dy)
        lines_by_source = {
            'bell':'M6 14H10M8 1V2',
            'save':'M5 2V6H10V2M5 14V10H11V14',
            'package':'M1.65 4.75L8 8.05L14.35 4.75M8 8.05V14.4M4.85 3.25L11.1 6.4',
            'database':'M3 3.75A5 2 0 0 0 13 3.75M3 8A5 2 0 0 0 13 8',  # lane B base
            'image':'M2 12L6.5 8 9 10 11 7.5 14 11',
            'hourglass':'M6.5 5H9.5M6.45 11.4L8 9.9L9.55 11.4',
            'monitor':'M8 11V13.5M5.35 13.5H10.65',  # lane B base: no chin
        }
        if source == 'server-rack':
            return (rr(1.5,1.75,11.2,12.1),
                    union(stroke('M1.5 5.8H12.7M1.5 9.8H12.7M8 3.8H10.25M8 7.8H10.25M6.2 11.85H7.6'),
                          dots((4.1,3.8),(4.1,7.8),(4.1,11.85),r=.63)))
        if source in lines_by_source:
            detail = stroke(fit(path(lines_by_source[source])))
            if source == 'image':
                detail = union(detail,fit(circle(5,5.5,1.3)))
        elif source == 'map-pin':
            detail = stroke(fit(circle(8,6,1.55)))
        elif source == 'building-complex':
            detail = stroke(fit(building_windows))
        if source == 'heart':
            return transform(body,scale=.7,dx=-1.95,dy=-1.9),detail
        if source == 'star':
            return transform(body,scale=.69,dx=-2.05,dy=-2.1),detail
        if source == 'monitor':
            body = rr(1.48,2.25,9.75,6.75)
        elif source == 'image':
            body = rr(1.48,2.25,9.75,9)
        else:
            body = fit(body)
        return body, detail

    # A circular slot includes the diagonal reach of each family's widest
    # modifier and does not trace individual teeth or corners onto the host.
    slot_radii = {'heart':3.85,'star':4.3,'database':5.1,'package':4.75}

    def badged(name, source, suffix, tags=None):
        body, detail = corner_host(source)
        if name == 'image-minus':
            body = transform(body,dx=.35,dy=1.65)
            detail = transform(detail,dx=.35,dy=1.65)
            badge = line((10.45,11.35),(14.45,11.35))
        elif source in ('user','user-round'):
            if suffix == 'cog':
                badge = gear(12.35,10.45,2.75)
            elif suffix == 'star':
                badge = stroke(transform(api['STAR'],scale=.34,dx=4.4,dy=2.65))
            elif suffix == 'shield':
                badge = stroke('M10.5 9.55L12.45 8.7L14.4 9.55V11Q14.4 12.6 12.45 13.6Q10.5 12.6 10.5 11Z')
            else:
                badge = compact(suffix,12.75 if suffix in ('plus','minus') else 12.3,10.6,.76)
        elif source == 'server-rack':
            badge = gear(12.6,12.15,2.55)
        elif suffix == 'backup':
            badge = stroke('M10.2 11.2A2.3 2.3 0 1 1 10.55 13.6M10.05 9.35V11.35H12.05')
        elif suffix == 'cog':
            badge = gear(12,11.8,2.75)
        elif name == 'bell-dot':
            badge = circle(12.9,3.1,1.5)
        elif suffix in ('plus','minus') and source != 'archive':
            if source in slot_radii:
                badge = compact(suffix,12,11.6,.87)
            else:
                badge = compact(suffix,12.45,11.35,.87)
        elif source in ('alarm-clock','archive'):
            badge = compact(suffix,12.75,12.8,.74)
        else:
            badge = compact(suffix,11.65 if suffix in ('sync','pen','key','search') else 12.05,11.5 if suffix == 'question-mark' else 11.75,.92)
        if source in slot_radii and suffix not in ('plus','minus'):
            left,top,right,bottom = badge.bounds
            badge = transform(badge,dx=12-(left+right)/2,dy=11.6-(top+bottom)/2)
        shape(name,body,union(detail,badge),tags or name.replace('-',' '))
        # The badge clears the original drawing after its style has been composed.
        corner_badges[name] = (source,body,detail,badge)

    # ---- Interface controls and Product tools: SF Symbols conventions ----
    # These helpers are local to the two categories; the shared helpers above
    # (compact, stack, gear, badged, disabled_styles) keep their behaviour.
    drawings, badges = api['DRAWINGS'], api['BADGES']
    clearance_gap = api['BADGE_GAP']

    def rotate_about(p, angle, cx, cy):
        a = math.radians(angle)
        c, s = math.cos(a), math.sin(a)
        return p.transform(c, s, -s, c, cx-c*cx+s*cy, cy-s*cx-c*cy)

    def sf_mark(kind, cx, cy, r):
        """Knock-out marks for badge discs, beyond the shared badge kinds."""
        s = r/3.25
        if kind == 'question':
            return union(stroke(f'M{cx-1.2*s} {cy-.8*s}C{cx-1.2*s} {cy-2.5*s} {cx+1.25*s} {cy-2.5*s} '
                                f'{cx+1.25*s} {cy-1.0*s}C{cx+1.25*s} {cy-.1*s} {cx} {cy-.05*s} {cx} {cy+.7*s}'),
                         circle(cx, cy+1.8*s, .6))
        if kind in ('arrow-left', 'arrow-right'):
            return rotate_about(api['badge_mark']('arrow-up', cx, cy, r),
                                -90 if kind == 'arrow-left' else 90, cx, cy)
        if kind == 'restore':
            # A counterclockwise return arrow, the database backup convention.
            return union(stroke(f'M{cx-1.75*s} {cy+.2*s}A1.75 1.75 0 1 0 {cx-.55*s} {cy-1.65*s}'),
                         stroke(f'M{cx-2.75*s} {cy-.75*s}L{cx-1.75*s} {cy+.3*s}L{cx-.7*s} {cy-.7*s}'))
        if kind == 'dot':
            return po.Path()
        return api['badge_mark'](kind, cx, cy, r)

    def sf_badge(name, kind, cx=11.85, cy=11.85, r=3.25):
        """A filled disc with its mark knocked out, set behind a 0.9 u gap."""
        disc = subtract(circle(cx, cy, r), sf_mark(kind, cx, cy, r))
        badges[name] = (disc, circle(cx, cy, r+clearance_gap))

    def sf_ink_badge(name, ink, gap):
        # Symbol badges (gear, lens, pencil) keep their own silhouette.
        badges[name] = (ink, gap)

    def sf_gear(cx, cy, radius, teeth=8):
        # Rounded, evenly spaced teeth around a round bore; one solid mass.
        points = []
        pitch = 2*math.pi/teeth
        for tooth in range(teeth):
            for offset, reach in ((-.36, .76), (-.17, 1), (.17, 1), (.36, .76)):
                angle = tooth*pitch + offset*pitch
                points.append((cx+radius*reach*math.cos(angle), cy+radius*reach*math.sin(angle)))
        return subtract(api['poly'](points), circle(cx, cy, radius*.34))

    def sf_gear_badge(name, cx=11.75, cy=11.75, radius=3.25):
        sf_ink_badge(name, sf_gear(cx, cy, radius), circle(cx, cy, radius+clearance_gap))

    def sf_lens_badge(name, cx=11.0, cy=11.0, r=2.35):
        # Open magnifier: the lens interior hides the host, like doc.magnifyingglass.
        lens = api['ring'](cx, cy, r)
        hx, hy = cx+r*.7, cy+r*.7
        handle = line((hx, hy), (hx+1.75, hy+1.75))
        gap = union(circle(cx, cy, r+clearance_gap), line((hx, hy), (hx+1.75, hy+1.75), width=1.04+2*clearance_gap))
        sf_ink_badge(name, union(lens, handle), gap)

    def sf_pencil_badge(name, cx=11.55, cy=11.55, length=7.2, width=2.15):
        half, end = width/2, length/2
        body = path(f'M{-end} 0L{-end+1.85} {-half}H{end-.7}Q{end} {-half} {end} {-half+.7}'
                    f'V{half-.7}Q{end} {half} {end-.7} {half}H{-end+1.85}Z')
        a = math.radians(-45)
        c, s = math.cos(a), math.sin(a)
        pencil = api['soften'](body.transform(c, s, -s, c, cx, cy), .2)
        sf_ink_badge(name, pencil, union(pencil, stroke(pencil, 2*clearance_gap, exact=True)))

    def sf_host(name, source, tags, extra=None):
        """Register a full-size base symbol; the badge is applied by main()."""
        body, detail, outline, _, _ = drawings[source]
        if extra is not None:
            detail = union(detail, extra)
        (shape if outline else glyph)(name, body, detail, tags)
        if source in overrides:
            overrides[name] = dict(overrides[source])

    def sf_person(cx, cy, s=1):
        # Head and shoulders, as in SF person. At small sizes the head becomes
        # a small filled element and the shoulders an open arc, never thinner.
        if s < .8:
            return union(circle(cx, cy-1.85*s, 1.55*s),
                         path(f'M{cx-2.9*s} {cy+3.1*s}Q{cx-2.9*s} {cy+.55*s} {cx} {cy+.55*s}'
                              f'Q{cx+2.9*s} {cy+.55*s} {cx+2.9*s} {cy+3.1*s}Z'))
        head = stroke(circle(cx, cy-1.7*s, 1.45*s))
        shoulders = stroke(path(f'M{cx-2.55*s} {cy+2.85*s}Q{cx-2.55*s} {cy+.75*s} {cx} {cy+.75*s}'
                                f'Q{cx+2.55*s} {cy+.75*s} {cx+2.55*s} {cy+2.85*s}Z'))
        return union(head, shoulders)

    # SF square (11.8 u ink) and circle (13.1 u ink) containers.
    square = rr(2.6, 2.6, 10.8, 10.8)
    disc = circle(8, 8, 6)

    # Badge seal: the shared eight-point seal with a centered, full-weight mark.
    seal = api['badge_body']()
    shape('badge', seal, None, 'award seal')
    for suffix in ('exclamation-point','info','minus','plus','x'):
        shape('badge-'+suffix, seal, compact(suffix), 'award seal '+suffix)

    # Book: the shared closed book (spine and page curl); marks sit on the cover.
    book_body = drawings['book'][0]
    book_frame = stroke('M5.6 1.8V11.4M13 11.4H5.3Q3.1 11.4 3.1 13')
    for suffix in ('check','heart','lock','minus','plus','search','text','user','x'):
        mark = (sf_person(9.3, 6.5, .74) if suffix == 'user'
                else compact(suffix, 9.3, 6.45, .82))
        shape('book-'+suffix, book_body, union(book_frame, mark), 'book '+suffix)

    # Bookmark: the family ribbon (bookmark-off derives from it as well).
    bookmark = drawings['bookmark'][0]
    for suffix in ('minus','x'):
        shape('bookmark-'+suffix, bookmark, compact(suffix, 8, 6.55, .84), 'bookmark '+suffix)
    shape('bookmark-off', bookmark, line((2,2),(14,14)), 'bookmark disabled')

    # Calendar: the family body and header; marks are centered on the date field.
    cal, top = api['CAL'], api['CALTOP']
    for suffix in ('1','arrow-down','arrow-left','arrow-right','arrow-up','chevrons-left','chevrons-right','cog','minus'):
        mark = gear(8, 10, 2.55) if suffix == 'cog' else compact(suffix, 8, 10, .9)
        shape('calendar-'+suffix, cal, union(top, mark), 'calendar date '+suffix)
    lens = union(stroke(circle(7.55, 9.55, 1.75)), line((8.85, 10.85), (10.2, 12.2)))
    shape('calendar-search', cal, union(top, lens), 'calendar date search')
    shape('calendar-sync', cal, union(top, compact('sync', 8, 10, .92)), 'calendar date sync')
    # The numbered versions carry an SF status badge on the full calendar.
    for suffix, kind in (('check','check'),('minus','minus'),('plus','plus'),('x','x')):
        sf_host('calendar-'+suffix+'-2', 'calendar', 'calendar date '+suffix)
        sf_badge('calendar-'+suffix+'-2', kind)
    shape('calendar-off', cal, union(top, line((2,2),(14,14))), 'calendar disabled')
    turned = path('M3.2 3H12.8Q14 3 14 4.2V9.6L9.6 14H3.2Q2 14 2 12.8V4.2Q2 3 3.2 3Z')
    shape('calendar-fold', turned, union(top, stroke('M9.6 14V10.8Q9.6 9.6 10.8 9.6H14')), 'calendar folded date')
    stack('calendars', rr(1.7,1.9,9.6,9.7), rr(4.6,4.8,9.7,9.4),
          stroke('M4.6 8H14.3M7 3.7V6M11.9 3.7V6'), 'multiple dates calendars')

    # Clock faces: SF circle, a long minute hand at twelve and a short hour hand.
    for hour in range(1,13):
        angle = math.pi*hour/6
        hx, hy = 8+2.75*math.sin(angle), 8-2.75*math.cos(angle)
        shape('clock-'+str(hour), disc, stroke(f'M8 4.1V8L{hx:.3f} {hy:.3f}'), 'time hour '+str(hour))
    # Status clocks are full SF clocks (hands at twelve and nine) with a badge.
    clock_hands = stroke('M8 4.1V8H5.2')
    for suffix, kind in (('arrow-down','arrow-down'),('arrow-left','arrow-left'),('arrow-right','arrow-right'),
                         ('arrow-up','arrow-up'),('exclamation-point','alert'),('plus','plus')):
        shape('clock-'+suffix, disc, clock_hands, 'time '+suffix)
        sf_badge('clock-'+suffix, kind)
    # sf_ext_states derives clock-x from clock-check's registered drawing (its
    # small dial at (6.25, 6.7) and hands). Keep that registration unchanged and
    # compose the published styles from the same full clock as its siblings.
    shape('clock-check', circle(6.25,6.7,4.6),
          union(stroke('M6.25 3.9V6.7L8.05 7.7'), compact('check',12.5,12.4,.76)), 'time check')
    clock_rim = stroke(disc)
    clock_ink = union(clock_rim, clock_hands)
    overrides['clock-check'] = {'duotone': [(subtract(disc, clock_ink), .24), (clock_ink, 1)],
                                'solid': api['solid_body'](disc, clock_rim, clock_hands),
                                'stroke': clock_ink}
    sf_badge('clock-check', 'check')
    fading = 'M13.5 8A5.5 5.5 0 0 1 8 13.5M2.5 8A5.5 5.5 0 0 1 8 2.5A5.5 5.5 0 0 1 13.5 8'
    glyph('clock-fading', stroke(fading), union(clock_hands, dots((3.3,11),(5.3,13),r=.6)), 'time history fading')

    # Clipboard: the family board; the clip straddles the centre of its top edge.
    board = drawings['clipboard'][0]
    board_left, board_top, board_right, board_bottom = board.bounds
    board_x = (board_left+board_right)/2
    clip = rr(board_x-2.35, board_top-1.6, 4.7, 2.7, .9, exact=True)
    board_y = (board_top+1.6+board_bottom)/2
    def clipboard(name, content, tags):
        shape(name, board, union(clip, content), tags)
        filled = union(board, stroke(board))
        interior = subtract(filled, stroke(filled, 1.8))
        knocked = op(content, interior, po.PathOp.INTERSECTION)
        overrides[name] = {'solid': union(subtract(filled, union(knocked, stroke(clip, 1.8, exact=True))), clip)}
    for suffix in ('clock','minus','plus','x','pen'):
        clipboard('clipboard-'+suffix, transform(compact(suffix, 8, 9.35, .95), dx=board_x-8, dy=board_y-9.35), 'clipboard '+suffix)
    clipboard('clipboard-list', transform(union(dots((5.55,6.9),(5.55,9.35),(5.55,11.8),r=.65),
                                      stroke('M7.35 6.9H10.75M7.35 9.35H10.75M7.35 11.8H10.75')), dx=board_x-8, dy=board_y-9.35), 'clipboard checklist')
    clipboard('clipboard-copy', transform(stroke('M5.35 10.85V7.6Q5.35 6.85 6.1 6.85H8.85M7.4 9.15Q7.4 8.65 7.9 8.65H10.15Q10.65 8.65 10.65 9.15V11.85Q10.65 12.35 10.15 12.35H7.9Q7.4 12.35 7.4 11.85Z'), dx=board_x-8, dy=board_y-9.35), 'clipboard copy')
    clipboard('clipboard-paste', transform(stroke('M8 6.5V10.4M6.35 8.75L8 10.4L9.65 8.75M5.6 12.35H10.4'), dx=board_x-8, dy=board_y-9.35), 'clipboard paste')

    # Credit cards: the family card with an SF status badge.
    for suffix in ('check','minus','plus','x'):
        sf_host('credit-card-'+suffix, 'credit-card', 'payment credit card '+suffix)
        sf_badge('credit-card-'+suffix, suffix)
    # Copies: the family's two sheets; the mark is centered on the front sheet.
    for suffix in ('check','plus','x'):
        api['stacked']('copy-'+suffix, api['copy_back'], api['copy_front'],
                       api['badge_mark'](suffix, 9.7, 9.7, 3.4 if suffix == 'plus' else 4.1), 'duplicate copy '+suffix)

    # Geometric controls and mathematical notation are opaque glyphs.
    glyph('asterisk',lines('M8 2V14','M2.8 5L13.2 11','M2.8 11L13.2 5'),None,'star wildcard')
    glyph('brackets',lines('M6 2H3.5V14H6','M10 2H12.5V14H10'),None,'code square brackets')
    glyph('equal',lines('M4.05 5.92H11.95','M4.05 10.08H11.95'),None,'math equality')
    glyph('math-pi',lines('M3.25 4.35H12.75','M6.2 4.35V11.65','M9.8 4.35V10.45Q9.8 11.65 11 11.65H11.6'),None,'math pi')
    glyph('code-xml',lines('M5.5 4L2 8L5.5 12','M10.5 4L14 8L10.5 12','M9 2L7 14'),None,'code markup xml')
    glyph('arrow-down-to-line',lines('M8 1.9V10.5','M4.2 6.7L8 10.5L11.8 6.7','M3.7 13.6H12.3'),None,'download arrow line')
    glyph('arrow-up-to-line',lines('M8 14.1V5.5','M4.2 9.3L8 5.5L11.8 9.3','M3.7 2.4H12.3'),None,'upload arrow line')
    glyph('check-line',union(check(6.6,7.2,.8),line((9.6,11.6),(13.6,11.6))),None,'complete check line')
    glyph('x-line-top',union(cross(8,9.25,1.12),line((4.7,4.2),(11.3,4.2))),None,'close cross line')
    # Charts: rounded bars as surfaces (Duotone tint, Solid fill), axis as a line.
    # chart.bar.xaxis: filled, rounded data bars beside an axis line.
    bars = union(rr(4.9,2.75,5.6,2.3,.85,exact=True), rr(4.9,6.75,8.9,2.3,.85,exact=True),
                 rr(4.9,10.75,3.9,2.3,.85,exact=True))
    glyph('chart-bar-horizontal', stroke('M2.4 1.9V13.55Q2.4 14.1 2.95 14.1H14.1'), bars, 'chart horizontal bars')
    # chart.bar: outlined columns; the lower stacked segment is a filled mass
    # with a one-unit gap, so every style reads as two series per column.
    uppers, lowers = [], []
    for x, top_ink, lower in ((1.55, 5.2, 2.8), (6.2, 3.3, 3.8), (10.85, 1.4, 4.8)):
        uppers.append(rr(x+.52, top_ink+.52, 2.56, 14-lower-1.0-top_ink-1.04, .8, exact=True))
        lowers.append(rr(x, 14-lower, 3.6, lower, .95, exact=True))
    shape('chart-column-stacked', union(*uppers), union(*lowers), 'chart stacked columns')
    glyph('chart-scatter',union(lines('M2.5 2V13.5H14'),dots((5,10),(7,6),(9,9),(11,4),(13,7),r=.8)),None,'chart scatter points')

    api['CATEGORY'] = 'Files and folders'
    doc = api['FILE']
    fold = api['FOLD']
    BADGES, GAP = api['BADGES'], api['BADGE_GAP']

    # Document family, measured against SF doc.*: one shared page (draw.py
    # FILE and FOLD), every position derived from its bounds so the family
    # follows the shared page. Content sits centred in the lower page at
    # about half of its inner width; badges sit at the lower left, where SF
    # puts doc.badge.plus / .clock / .gearshape (2.6 u left of, 1.1 u below the page).
    px0, py0, px1, py1 = doc.bounds
    page_w, page_h = px1-px0, py1-py0
    unit = page_w/11
    page_ink = (px0-.52, py0-.52, px1+.52, py1+.52)
    content = ((px0+px1)/2, py0+.63*page_h)
    fb = fold.bounds
    fold_centerline = path(f'M{fb[0]+.52} {fb[1]+.52}V{fb[3]-.52}H{fb[2]-.52}')
    def on_page(d, scale=1, x=0, y=0):
        s = unit*scale
        return path(d).transform(s,0,0,s,content[0]+x*unit,content[1]+y*unit)
    def fit(*boxes, room=14.4):
        x0=min(b[0] for b in boxes); y0=min(b[1] for b in boxes)
        x1=max(b[2] for b in boxes); y1=max(b[3] for b in boxes)
        s=min(1,room/(x1-x0),room/(y1-y0))
        return lambda p: p.transform(s,0,0,s,8-s*(x0+x1)/2,8-s*(y0+y1)/2), s
    def page(T, s):
        # Re-stroke the fold when the page is scaled so it keeps full weight.
        return T(doc), (T(fold) if s > .97 else stroke(T(fold_centerline)))

    R = 3.25
    corner = (px0+.13, py1-1.59)
    def badged_doc(name, tags, kind=None, mark=None, at=corner, reach=(R,R,R,R)):
        box = (at[0]-reach[0], at[1]-reach[1], at[0]+reach[2], at[1]+reach[3])
        T, s = fit(page_ink, box)
        body, crease = page(T, s)
        shape(name, body, crease, tags)
        c = T(path(f'M{at[0]} {at[1]}h.001')).bounds
        cx, cy = c[0], c[1]
        if kind:
            api['badge'](name, kind, cx, cy, R*s)
        else:
            disc, clearance = mark(cx, cy, s)
            BADGES[name] = (disc, clearance)

    def hugging(ink):
        return ink, union(ink, stroke(ink, 2*GAP, exact=True))
    def centred(d, cx, cy, s):
        return path(d).transform(s,0,0,s,cx,cy)

    for suffix, kind in (('plus-corner','plus'),('minus-corner','minus'),('x-corner','x'),
                         ('check-corner','check'),('clock','clock')):
        badged_doc('file-'+suffix, 'document file '+suffix.replace('-',' '), kind=kind)
    # SF doc.badge.gearshape: a filled gear without a disc, set into the page.
    badged_doc('file-cog', 'document file settings cog',
               mark=lambda cx, cy, s: hugging(gear(cx, cy, 3.35*s)), reach=(3.4,3.4,3.4,3.4))
    for suffix, arrow in (('input','M-1.65 0H1.45M.05 -1.45L1.5 0L.05 1.45'),
                          ('output','M1.65 0H-1.45M-.05 -1.45L-1.5 0L-.05 1.45')):
        def arrow_disc(cx, cy, s, arrow=arrow):
            ink = stroke(centred(arrow, cx, cy, s))
            return subtract(circle(cx, cy, R*s), ink), circle(cx, cy, (R+GAP)*s)
        badged_doc('file-'+suffix, 'document file '+suffix, mark=arrow_disc)
    # Code, brace and type marks are knocked out of the same disc.
    for suffix, d in (
        ('code-corner','M-.8 -1.15L-2 0L-.8 1.15M.8 -1.15L2 0L.8 1.15'),
        ('type-corner','M-1.55 -1.6H1.55M0 -1.6V1.75'),
    ):
        def glyph_disc(cx, cy, s, d=d):
            ink = stroke(centred(d, cx, cy, s))
            return subtract(circle(cx, cy, R*s), ink), circle(cx, cy, (R+GAP)*s)
        badged_doc('file-'+suffix, 'document file '+suffix.replace('-',' '), mark=glyph_disc)
    # Braces need more room than a disc's counter: a linear corner mark
    # set behind a hugging gap, like SF person.badge.key.
    braces = ('M-.95 -2.2Q-1.75 -2.2 -1.75 -1.4V-.65Q-1.75 0 -2.4 0Q-1.75 0 -1.75 .65V1.4Q-1.75 2.2 -.95 2.2'
              'M.95 -2.2Q1.75 -2.2 1.75 -1.4V-.65Q1.75 0 2.4 0Q1.75 0 1.75 .65V1.4Q1.75 2.2 .95 2.2')
    badged_doc('file-braces-corner', 'document file braces corner',
               mark=lambda cx, cy, s: hugging(stroke(centred(braces, cx, cy, s))),
               at=(px0+.55, py1-1.35), reach=(2.95,2.75,2.95,2.75))
    # SF doc.text.magnifyingglass: an open lens over the lower-right corner.
    def lens(cx, cy, s):
        glass = union(api['ring'](cx, cy, 2.5*s), line((cx+1.75*s, cy+1.75*s), (cx+3.2*s, cy+3.2*s)))
        return glass, union(circle(cx, cy, (2.5+GAP)*s), stroke(glass, 2*GAP, exact=True))
    badged_doc('file-search-corner', 'document file search corner', mark=lens,
               at=(px1-1.2, py1-2.25), reach=(2.5,2.5,3.75,3.75))

    filled_person = union(circle(0,-1.35,1.2), path('M-2.25 2.45Q-2.25 .55 0 .55Q2.25 .55 2.25 2.45Z'))
    page_marks = {
        'axis-3d':'',
        'box':'M0 -2.35L2.15 -1.2V1.3L0 2.45L-2.15 1.3V-1.2ZM-2.15 -1.2L0 -.05L2.15 -1.2M0 -.05V2.45',
        'braces':'M-.9 -2.4Q-1.8 -2.4 -1.8 -1.5V-.7Q-1.8 0 -2.5 0Q-1.8 0 -1.8 .7V1.5Q-1.8 2.4 -.9 2.4'
                 'M.9 -2.4Q1.8 -2.4 1.8 -1.5V-.7Q1.8 0 2.5 0Q1.8 0 1.8 .7V1.5Q1.8 2.4 .9 2.4',
        'chart-column':'M-2 2.3V.4M0 2.3V-2.3M2 2.3V-.9',
        'chart-column-increasing':'M-2 2.3V1M0 2.3V-.6M2 2.3V-2.3',
        'chart-line':'M-2.35 -2.3V2.3H2.45M-.95 .75L.1 -.55L1.05 .2L2.35 -1.55',
        'chart-pie':'',
        'database':'M-2 -1.55A2 .85 0 0 1 2 -1.55A2 .85 0 0 1 -2 -1.55ZM-2 -1.55V1.6A2 .85 0 0 0 2 1.6V-1.55M-2 .05A2 .85 0 0 0 2 .05',
        'diff':'M-1.35 -.95H1.35M0 -2.3V.4M-1.35 2.15H1.35',
        'digit':'M-1.5 -2.3A.95 .95 0 0 1 -.55 -1.35V1.35A.95 .95 0 0 1 -2.45 1.35V-1.35A.95 .95 0 0 1 -1.5 -2.3Z'
                'M1 -1.45L2 -2.3V2.3',
        'headphone':'M-2.05 1V.05A2.05 2.05 0 0 1 2.05 .05V1',
        'key':'M-1.25 0m-1.15 0a1.15 1.15 0 1 0 2.3 0a1.15 1.15 0 1 0 -2.3 0M-.1 0H2.45M1.75 0V1.25',
        'pen':'',
        'pen-line':'M.35 2.4H2.45',
        'question-mark':'M-1.4 -1.35C-1.4 -2.2 -.8 -2.65 0 -2.65C.85 -2.65 1.45 -2.1 1.45 -1.4'
                        'C1.45 -.7 .95 -.4 .45 -.05C.1 .2 0 .45 0 .75',
        'exclamation-point':'M0 -2.5V.3',
        'signal':'M.03 -1.29A2 2 0 0 1 .03 1.29M1.33 -2.38A3.7 3.7 0 0 1 1.33 2.38',
        'sliders':'M-2.3 -1.2H2.3M-2.3 1.4H2.3M-.9 -2.3V-.1M1 .3V2.5',
        'terminal':'M-2.2 -1.7L-.5 0L-2.2 1.7M.7 1.9H2.4',
        'type':'M-2.1 -2.3H2.1M0 -2.3V2.4',
        'video-camera':'M-1.95 -1.45H.35Q.95 -1.45 .95 -.85V.85Q.95 1.45 .35 1.45H-1.95Q-2.55 1.45 -2.55 .85V-.85Q-2.55 -1.45 -1.95 -1.45Z'
                       'M.95 -.45L2.55 -1.35V1.35L.95 .45',
        'volume':'M1.4 -1.4Q2.45 0 1.4 1.4',
    }
    pencil = 'M-3.05 3L-2.75 .65L1.05 -3.15L2.95 -1.25L-.95 2.65Z'
    for suffix, d in page_marks.items():
        ink = stroke(on_page(d))
        if suffix in ('question-mark','exclamation-point'):
            ink = union(ink, on_page('M0 2.35m-.66 0a.66 .66 0 1 0 1.32 0a.66 .66 0 1 0 -1.32 0'))
        if suffix in ('question-mark','type'):
            ink = ink.transform(1,0,0,1,0,.25*unit)
        if suffix == 'headphone':
            cup = 'M-2.85 .75Q-2.85 .1 -2.2 .1H-1.9Q-1.25 .1 -1.25 .75V2.15Q-1.25 2.8 -1.9 2.8H-2.2Q-2.85 2.8 -2.85 2.15Z'
            ink = union(ink, on_page(cup), api['mirror'](on_page(cup)).transform(1,0,0,1,2*content[0]-16,0))
        if suffix == 'volume':
            ink = union(ink, api['poly']([(content[0]+x*unit, content[1]+y*unit) for x, y in
                        ((-2.45,-.85),(-1.45,-.85),(.15,-2.25),(.15,2.25),(-1.45,.85),(-2.45,.85))]))
        if suffix == 'axis-3d':
            # SF move.3d: three axes from one point, each with a filled head.
            def spoke(angle, pts):
                c, n = math.cos(angle), math.sin(angle)
                return [(content[0]+unit*(x*c-y*n), content[1]+unit*(x*n+y*c+.65)) for x, y in pts]
            ink = union(*(union(line(*spoke(a, ((0,0),(0,-1.6)))),
                                api["poly"](spoke(a, ((0,-3.05),(1.15,-1.45),(-1.15,-1.45)))))
                          for a in (0, 2*math.pi/3, -2*math.pi/3)))
        if suffix == 'chart-pie':
            # SF chart.pie: an open three-quarter sector and a detached filled slice.
            ink = union(stroke(on_page('M-.45 -1.55A2 2 0 1 0 1.55 .45H-.45Z')),
                        on_page('M.6 -.6V-3.12A2.52 2.52 0 0 1 3.12 -.6Z'))
        if suffix == 'pen':
            ink = stroke(on_page(pencil, .78))
        if suffix == 'pen-line':
            ink = union(ink, stroke(on_page(pencil, .66, -.35, -.55)))
        if suffix == 'signal':
            ink = union(ink, on_page('M-1.5 0m-.72 0a.72 .72 0 1 0 1.44 0a.72 .72 0 1 0 -1.44 0'))
        shape('file-'+suffix, doc, union(fold, ink), 'document file '+suffix.replace('-',' '))
    shape('file-user', doc, union(fold, filled_person.transform(unit,0,0,unit,*content)), 'document file user')
    # SF checkmark.seal.fill, set inside the page.
    seal = transform(api['badge_body'](), scale=.4*unit, dx=content[0]-8, dy=content[1]-8)
    shape('file-badge', doc, union(fold, subtract(seal, stroke(on_page('M-1.15 .05L-.3 .95L1.25 -.85')))),
          'document file badge')

    # SF doc.viewfinder: a small page inside viewfinder corners.
    T, s = fit((px0-2.7, py0-1.6, px1+2.7, py1+1.6), room=7.6)
    frame = stroke('M2.15 5.05V3.35Q2.15 2.15 3.35 2.15H5.05M10.95 2.15H12.65Q13.85 2.15 13.85 3.35V5.05'
                   'M13.85 10.95V12.65Q13.85 13.85 12.65 13.85H10.95M5.05 13.85H3.35Q2.15 13.85 2.15 12.65V10.95')
    small_page, small_fold = page(T, s)
    shape('file-scan', small_page, union(small_fold, frame), 'document file scan')

    # SF doc.on.doc: whole pages, each with its fold, separated by a clear gap.
    def sheets(name, layers, tags):
        inks, surfaces, solids = [], [], []
        cover = po.Path()
        for body, crease in reversed(layers):
            rim = stroke(body)
            filled = union(body, rim)
            inks.append(subtract(union(rim, crease), cover))
            surfaces.append(subtract(body, cover))
            solids.append(subtract(subtract(filled, crease), cover))
            cover = union(cover, filled, stroke(filled, 2*GAP, exact=True))
        ink = union(*inks)
        shape(name, union(*(b for b, _ in layers)), ink, tags)
        overrides[name] = {'duotone':[(subtract(union(*surfaces), ink), .24), (ink, 1)],
                           'stroke':ink, 'solid':union(*solids)}
    def offset_pages(count, step, fold_all):
        w, h = page_ink[2]-page_ink[0], page_ink[3]-page_ink[1]
        s = min(1, 14.4/(w+step*(count-1)), 14.4/(h+step*(count-1)))
        layers = []
        for i in range(count):
            shift = (i-(count-1)/2)*step*s
            T = lambda p, shift=shift: p.transform(s,0,0,s,8-s*(px0+px1)/2+shift,8-s*(py0+py1)/2+shift)
            body = T(doc) if fold_all or i == count-1 else T(rr(px0, py0, page_w, page_h))
            layers.append((body, stroke(T(fold_centerline)) if fold_all or i == count-1 else po.Path()))
        return layers
    sheets('files', offset_pages(2, .21*(page_ink[2]-page_ink[0]), True), 'multiple documents files')
    sheets('file-stack', offset_pages(3, .17*(page_ink[2]-page_ink[0]), False), 'documents stack')

    # Folder family, measured against SF folder.*: the shared folder body and
    # pocket line from draw.py; content centred below the pocket line at about
    # half of the pocket's height; badges at the top right, where SF puts
    # folder.badge.plus / .gearshape / .person.crop.
    folder, pocket = api['DRAWINGS']['folder'][:2]
    gx0, gy0, gx1, gy1 = folder.bounds
    pb = pocket.bounds
    pocket_y = (pb[1]+pb[3])/2
    pocket_centerline = path(f'M{pb[0]+.52} {pocket_y}H{pb[2]-.52}')
    funit = (gx1-gx0)/13.3
    pocket_space = (pocket_y+.52, gy1-.52)
    fcontent = ((gx0+gx1)/2, sum(pocket_space)/2+.1)
    folder_ink = (gx0-.52, gy0-.52, gx1+.52, gy1+.52)
    def in_folder(d, scale=1, x=0, y=0):
        s = funit*scale
        return path(d).transform(s,0,0,s,fcontent[0]+x*funit,fcontent[1]+y*funit)
    def folder_frame(T, s):
        return T(folder), (T(pocket) if s > .97 else stroke(T(pocket_centerline)))
    fcorner = (gx1+.52+1.4-R, gy0-.72+R)
    def badged_folder(name, tags, kind=None, mark=None, at=fcorner, reach=(R,R,R,R), r=R):
        box = (at[0]-reach[0], at[1]-reach[1], at[0]+reach[2], at[1]+reach[3])
        T, s = fit(folder_ink, box)
        body, seam = folder_frame(T, s)
        shape(name, body, seam, tags)
        c = T(path(f'M{at[0]} {at[1]}h.001')).bounds
        if kind:
            api['badge'](name, kind, c[0], c[1], r*s)
        else:
            BADGES[name] = mark(c[0], c[1], s)

    def gearshape(x, y, radius):
        # SF gearshape: eight short teeth and a round bore, softened corners.
        points = []
        for tooth in range(8):
            for angle, reach in ((-15.5, .78), (-9, 1), (9, 1), (15.5, .78)):
                theta = math.radians(45*tooth + angle + 22.5)
                points.append((x+radius*reach*math.cos(theta), y+radius*reach*math.sin(theta)))
        return subtract(api['poly'](points), circle(x, y, radius*.36))

    badged_folder('folder-clock', 'directory folder clock', kind='clock')
    badged_folder('folder-cog', 'directory folder cog',
                  mark=lambda cx, cy, s: hugging(gearshape(cx, cy, 3.45*s)), reach=(3.45,3.45,3.45,3.45))
    def person_disc(cx, cy, s):
        head = circle(cx, cy-.85*s, 1.0*s)
        body = op(path('M-2 2.6Q-2 .6 0 .6Q2 .6 2 2.6Z').transform(s,0,0,s,cx,cy),
                  circle(cx, cy, (R-.62)*s), po.PathOp.INTERSECTION)
        return subtract(circle(cx, cy, R*s), union(head, body)), circle(cx, cy, (R+GAP)*s)
    badged_folder('folder-user', 'directory folder user', mark=person_disc)
    for suffix, arrow in (('input','M1.65 0H-1.45M-.05 -1.45L-1.5 0L-.05 1.45'),
                          ('output','M-1.65 0H1.45M.05 -1.45L1.5 0L.05 1.45')):
        def folder_arrow(cx, cy, s, arrow=arrow):
            ink = stroke(centred(arrow, cx, cy, s))
            return subtract(circle(cx, cy, R*s), ink), circle(cx, cy, (R+GAP)*s)
        badged_folder('folder-'+suffix, 'directory folder '+suffix, mark=folder_arrow)
    # A notification dot rides the folder's upper right corner, as on SF envelope.badge.
    probe = op(folder, rr(gx1-1.6, 0, .2, 16, 0), po.PathOp.INTERSECTION).bounds[1]
    badged_folder('folder-dot', 'directory folder dot', kind='dot',
                  at=(gx1-.35, probe+.25), reach=(2.2,2.2,2.2,2.2), r=2.2)

    def circular_arrows(r):
        def at(theta, radius=r):
            t = math.radians(theta)
            return radius*math.cos(t), radius*math.sin(t)
        parts = []
        for start, end in ((190, 305), (10, 125)):
            arc = 'M'+'L'.join(f'{x:.3f} {y:.3f}' for x, y in (at(a) for a in range(start, end+1, 5)))
            parts.append(stroke(in_folder(arc)))
            t = math.radians(end)
            tx, ty = -math.sin(t), math.cos(t)
            ex, ey = at(end)
            parts.append(api['poly']([(fcontent[0]+funit*x, fcontent[1]+funit*y) for x, y in (
                (ex+tx*1.55, ey+ty*1.55), (ex+math.cos(t)*1.2, ey+math.sin(t)*1.2),
                (ex-math.cos(t)*1.2, ey-math.sin(t)*1.2))]))
        return union(*parts)

    pencil_small = 'M-3.05 3L-2.75 .65L1.05 -3.15L2.95 -1.25L-.95 2.65Z'
    folder_marks = {
        'bookmark': stroke(in_folder('M-1.3 -1.95H1.3V2.05L0 1.05L-1.3 2.05Z')),
        'git': union(stroke(in_folder('M-1.5 -1.6V1.6M1.55 -.95Q1.55 .75 -1.5 .75')),
                     dots(*((fcontent[0]+funit*x, fcontent[1]+funit*y) for x, y in ((-1.5,-1.6),(-1.5,1.6),(1.55,-.95))), r=.85)),
        'git-2': union(stroke(in_folder('M-1.6 -1.55V1.55M-1.6 -.45Q-1.6 1.55 1.6 1.55')),
                       dots(*((fcontent[0]+funit*x, fcontent[1]+funit*y) for x, y in ((-1.6,-1.55),(-1.6,1.55),(1.6,1.55))), r=.85)),
        'kanban': stroke(in_folder('M-2 -1.4V1.2M0 -1.4V.1M2 -1.4V2')),
        'key': stroke(in_folder(page_marks['key'])),
        'pen': stroke(in_folder(pencil_small, .7)),
        'root': union(stroke(in_folder('M0 -.75m-1.25 0a1.25 1.25 0 1 0 2.5 0a1.25 1.25 0 1 0 -2.5 0M0 .5V2.05'))),
        'search-2': stroke(in_folder('M-.45 -.45m-1.55 0a1.55 1.55 0 1 0 3.1 0a1.55 1.55 0 1 0 -3.1 0M.7 .7L2.05 2.05')),
        'symlink': stroke(in_folder('M-2 2V.8Q-2 -.6 -.6 -.6H2.1M.85 -1.85L2.1 -.6L.85 .65')),
        'sync': circular_arrows(1.95),
        'users': union(filled_person.transform(.78*funit,0,0,.78*funit,fcontent[0]-1.35*funit,fcontent[1]+.15*funit),
                       subtract(filled_person.transform(.78*funit,0,0,.78*funit,fcontent[0]+1.35*funit,fcontent[1]+.15*funit),
                                stroke(filled_person.transform(.78*funit,0,0,.78*funit,fcontent[0]-1.35*funit,fcontent[1]+.15*funit), 2*GAP, exact=True))),
    }
    for suffix, ink in folder_marks.items():
        shape('folder-'+suffix, folder, union(pocket, ink), 'directory folder '+suffix.replace('-',' '))
    shape('folder-closed', folder, pocket, 'directory closed')

    # Folder tree: one folder above two, linked by right-angled branches.
    def mini_folder(x, y, s):
        return folder.transform(s,0,0,s,x-s*(gx0+gx1)/2,y-s*(gy0+gy1)/2)
    root = mini_folder(8, 3.9, .41)
    children = union(mini_folder(3.95, 12.1, .37), mini_folder(12.05, 12.1, .37))
    branches = stroke('M8 6.1V8.2M3.95 10.1V8.2H12.05V10.1')
    shape('folder-tree', union(root, children), branches, 'directory folder tree')

    # Open folder with a dot: the shared open-folder planes, dot on the front flap.
    back, flap = api['folder_back'], api['folder_flap']
    fb2 = flap.bounds
    stack('folder-open-dot', back, flap, circle((fb2[0]+fb2[2])/2, (fb2[1]+fb2[3])/2+.1, .95),
          'directory open notification')

    api['CATEGORY'] = 'Communication'
    STROKE = api['STROKE']

    def dashed(outline, dash=1.95, gap=1.85, anchor=None):
        """Round-capped dashes along a closed centerline, evenly distributed."""
        from fontTools.pens.recordingPen import RecordingPen
        pen = RecordingPen(); outline.draw(pen)
        contours, pts, last = [], [], None
        for verb, args in pen.value:
            if verb == 'moveTo':
                pts = [args[0]]; last = args[0]
            elif verb == 'lineTo':
                pts.append(args[0]); last = args[0]
            elif verb in ('curveTo', 'qCurveTo'):
                ctrl = (last,)+args
                for i in range(1, 25):
                    t = i/24
                    if len(ctrl) == 4:
                        x = sum(c*p[0] for c, p in zip(((1-t)**3, 3*t*(1-t)**2, 3*t*t*(1-t), t**3), ctrl))
                        y = sum(c*p[1] for c, p in zip(((1-t)**3, 3*t*(1-t)**2, 3*t*t*(1-t), t**3), ctrl))
                    else:
                        x = sum(c*p[0] for c, p in zip(((1-t)**2, 2*t*(1-t), t*t), ctrl))
                        y = sum(c*p[1] for c, p in zip(((1-t)**2, 2*t*(1-t), t*t), ctrl))
                    pts.append((x, y))
                last = args[-1]
            elif verb in ('closePath', 'endPath'):
                if pts and pts[0] != pts[-1]: pts.append(pts[0])
                contours.append(pts); pts = []
        pieces = []
        for pts in contours:
            seg = [math.dist(a, b) for a, b in zip(pts, pts[1:])]
            total = sum(seg)
            n = max(1, round(total/(dash+gap)))
            period = total/n
            on = period*dash/(dash+gap)
            def point(s):
                s %= total
                for (a, b), d in zip(zip(pts, pts[1:]), seg):
                    if s <= d:
                        f = s/d if d else 0
                        return (a[0]+(b[0]-a[0])*f, a[1]+(b[1]-a[1])*f)
                    s -= d
                return pts[-1]
            # Centre one dash on the anchor (the tail tip) so no stub is left there.
            offset = 0
            if anchor:
                acc, best = 0, None
                for a, d in zip(pts, [0]+seg):
                    acc += d
                    gap_to = math.dist(a, anchor)
                    if best is None or gap_to < best[0]: best = (gap_to, acc)
                offset = best[1]-on/2
            for i in range(n):
                start = offset+i*period
                samples = [point(start+on*j/8) for j in range(9)]
                pieces.append(line(*samples))
        return union(*pieces)

    # Speech bubbles, measured against SF message (an oval, 14.9 x 12.4) and
    # bubble.left (a rounded rectangle, 14.2 x 13.2). Marks sit centred in the
    # body at about half of its inner height, at full weight.
    def oval(cx, cy, rx, ry):
        return path(f'M{cx-rx} {cy}a{rx} {ry} 0 1 0 {2*rx} 0a{rx} {ry} 0 1 0 {-2*rx} 0Z')
    bubble_round = union(oval(8, 7.25, 6.68, 4.93),
                         api['soften'](path('M3.05 9.6Q3.5 12.3 2.25 13.7Q5.2 13.8 7.05 11.95Z'), .3))
    round_mark = (8, 7.25)
    bubble_square = union(rr(1.42, 1.92, 13.16, 9.68, 3.0, exact=True),
                          api['soften'](path('M3.6 11V14Q3.6 14.45 4.05 14.1L7.45 11Z'), .3))
    square_mark = (8, 6.76)
    def mark_at(d, centre, scale=1):
        return path(d).transform(scale,0,0,scale,*centre)

    marks = {
        'check': 'M-2.15 .2L-.6 1.85L2.2 -1.95',
        'x': 'M-1.75 -1.75L1.75 1.75M1.75 -1.75L-1.75 1.75',
        'plus': 'M-2.2 0H2.2M0 -2.2V2.2',
        'exclamation-point': 'M0 -2.4V.5',
        'question-mark': 'M-1.4 -1.6C-1.4 -2.45 -.8 -2.9 0 -2.9C.85 -2.9 1.45 -2.35 1.45 -1.65'
                         'C1.45 -.95 .95 -.65 .45 -.3C.1 -.05 0 .2 0 .5',
        'text': 'M-2.75 -1.2H2.75M-2.75 1.2H1.05',
        'code': 'M-1.15 -1.8L-2.8 0L-1.15 1.8M1.15 -1.8L2.8 0L1.15 1.8',
        'reply': 'M-.55 -2.15L-2.65 -.1L-.55 1.95M-2.45 -.1H.35Q2.65 -.1 2.65 2.2',
        'diff': 'M-1.45 -1.05H1.45M0 -2.5V.4M-1.45 2.2H1.45',
        'share': 'M-1.55 1.55L1.95 -1.95M-.3 -1.95H1.95V.3',
    }
    def mark_ink(kind, centre):
        if kind == 'more':
            return dots(*((centre[0]+x, centre[1]) for x in (-2.55, 0, 2.55)), r=.85)
        if kind == 'heart':
            return mark_at('M0 2.25C-.55 1.85 -2.75 .4 -2.75 -.95C-2.75 -2.25 -1.05 -2.75 0 -1.45'
                           'C1.05 -2.75 2.75 -2.25 2.75 -.95C2.75 .4 .55 1.85 0 2.25Z', centre)
        if kind == 'lock':
            return union(rr(centre[0]-1.85, centre[1]-.45, 3.7, 2.75, .6, exact=True),
                         stroke(mark_at('M-1.1 -.45V-1.3A1.1 1.1 0 0 1 1.1 -1.3V-.45', centre)))
        if kind == 'quote':
            ink = []
            for qx in (-1.3, 1.3):
                ink += [circle(centre[0]+qx, centre[1]-.55, 1.05),
                        stroke(mark_at(f'M{qx+1.0} -.55C{qx+1.0} .8 {qx+.45} 1.65 {qx-.6} 2.1', centre))]
            return union(*ink)
        ink = stroke(mark_at(marks[kind], centre))
        if kind in ('exclamation-point', 'question-mark'):
            ink = union(ink, circle(centre[0], centre[1]+2.15, .68))
        return ink

    def slashed(name, body, detail, tags, outline=True):
        # SF .slash: one diagonal across the symbol behind a 0.85 u channel.
        detail = detail or po.Path()
        if outline:
            shape(name, body, detail, tags)
            b = api['DRAWINGS'][name][0]
            rim = stroke(b)
            ink = union(subtract(rim, detail), detail)
            layers = [(subtract(b, ink), .24), (ink, 1)]
            mono = union(rim, detail)
            solid = api['solid_body'](b, rim, detail)
        else:
            glyph(name, body, detail, tags)
            ink = union(body, detail)
            layers, mono, solid = [(ink, 1)], ink, ink
        channel = line((2, 2), (14, 14), width=STROKE+1.7)
        bar = line((2, 2), (14, 14))
        def cut(p):
            return union(*(c for c in api['components'](subtract(p, channel)) if c.area > .45))
        overrides[name] = {'duotone': [(cut(p), a) for p, a in layers[:-1]]+[(union(cut(layers[-1][0]), bar), 1)],
                           'stroke': union(cut(mono), bar), 'solid': union(cut(solid), bar)}

    shape('message-circle', bubble_round, None, 'conversation chat bubble')
    for suffix in ('check','exclamation-point','heart','plus','question-mark','x','code','more','text','reply'):
        shape('message-circle-'+suffix, bubble_round, mark_ink(suffix, round_mark), 'conversation chat '+suffix)
    slashed('message-circle-off', bubble_round, None, 'conversation disabled')
    round_dashes = dashed(api['soften'](bubble_round, .3), anchor=(2.25, 13.7))
    glyph('message-circle-dashed', round_dashes, None, 'conversation dashed')
    glyph('message-circle-dashed-check', round_dashes, mark_ink('check', round_mark), 'conversation dashed check')
    for suffix in ('code','diff','exclamation-point','lock','reply','share','x','quote'):
        shape('message-square-'+suffix, bubble_square, mark_ink(suffix, square_mark), 'message chat '+suffix)
    slashed('message-square-off', bubble_square, None, 'message disabled')
    glyph('message-square-dashed', dashed(api['soften'](bubble_square, .3), anchor=(3.75, 14.2)), None, 'conversation dashed')
    # SF message.badge: a notification dot over the upper right of the body.
    shape('message-square-dot', bubble_square, None, 'message chat dot')
    api['badge']('message-square-dot', 'dot', 13.0, 3.0, 2.05)

    # SF bubble.left.and.bubble.right: two bubbles with opposed tails, the
    # front one separated from the back one by a clear gap.
    def layered(name, layers, tags, extra=None):
        inks, surfaces, solids = [], [], []
        cover = po.Path()
        for body, detail in reversed(layers):
            rim = stroke(body)
            filled = union(body, rim)
            inks.append(subtract(union(rim, detail), cover))
            surfaces.append(subtract(body, cover))
            solids.append(subtract(subtract(filled, detail), cover))
            cover = union(cover, filled, stroke(filled, 2*GAP, exact=True))
        ink = union(*inks, extra)
        shape(name, union(*(b for b, _ in layers)), ink, tags)
        overrides[name] = {'duotone': [(subtract(union(*surfaces), ink), .24), (ink, 1)],
                           'stroke': ink, 'solid': union(*solids, extra)}
    for name, bubble in (('messages-circle', bubble_round), ('messages-square', bubble_square)):
        back = api['soften'](bubble, .3).transform(.7,0,0,.7,.55,.75)
        front = api['mirror'](api['soften'](bubble, .3)).transform(.7,0,0,.7,4.25,4.3)
        layered(name, [(back, po.Path()), (front, po.Path())], 'conversations messages')

    # People, measured against SF person (11.2 x 11.9): a round head and a
    # domed torso one unit below it. Badges follow the pilot user-plus.
    user_body = api['DRAWINGS']['user'][0]
    user_round = union(circle(8, 4.92, 2.35),
                       path('M2.92 12.85C2.92 10.65 5.15 9.3 8 9.3C10.85 9.3 13.08 10.65 13.08 12.85'
                            'Q13.08 13.43 12.5 13.43H3.5Q2.92 13.43 2.92 12.85Z'))
    shape('user-round', user_round, None, 'person profile')
    bmark = api['badge_mark']
    BX, BY = 11.85, 11.85
    def person_badge(name, base, kind, tags):
        if kind in ('plus','minus','check','x','alert'):
            # Keep the mark as the detail: users-minus reuses it.
            shape(name, base, bmark(kind, BX, BY, R), tags)
            api['badge'](name, kind, BX, BY, R)
            return
        if kind == 'arrow-left':
            ink = stroke('M{0} {1}H{2}M{3} {4}L{5} {1}L{3} {6}'.format(BX+1.65, BY, BX-1.45, BX-.05, BY-1.45, BX-1.5, BY+1.45))
            shape(name, base, ink, tags)
            BADGES[name] = (subtract(circle(BX, BY, R), ink), circle(BX, BY, R+GAP))
            return
        x, y = 12.1, 11.6
        if kind == 'cog':
            mark = gearshape(x, y, 3.3)
        elif kind == 'key':
            # SF person.badge.key: a filled key, bow up, bit to the right.
            mark = union(subtract(circle(x, y-1.6, 1.75), circle(x, y-2.05, .62)),
                         line((x, y-.4), (x, y+3.0)), line((x, y+1.35), (x+1.2, y+1.35)),
                         line((x, y+2.55), (x+.95, y+2.55)))
        elif kind == 'lock':
            mark = union(rr(x-2.2, y-.35, 4.4, 3.45, .75, exact=True),
                         stroke(f'M{x-1.25} {y-.35}V{y-1.35}A1.25 1.25 0 0 1 {x+1.25} {y-1.35}V{y-.35}'))
        elif kind == 'pen':
            mark = path(f'M{x-2.55} {y+2.55}L{x-2.15} {y+.85}L{x+1.0} {y-2.3}Q{x+1.6} {y-2.9} {x+2.2} {y-2.3}'
                        f'L{x+2.55} {y-1.95}Q{x+3.15} {y-1.35} {x+2.55} {y-.75}L{x-.6} {y+2.4}Z')
        elif kind == 'search':
            mark = union(api['ring'](x-.45, y-.45, 2.15), line((x+1.1, y+1.1), (x+2.7, y+2.7)))
        elif kind == 'shield':
            shield = api['soften'](path(f'M{x} {y-3.1}Q{x+1.6} {y-2.2} {x+2.85} {y-2.2}V{y}'
                                        f'Q{x+2.85} {y+2.35} {x} {y+3.3}Q{x-2.85} {y+2.35} {x-2.85} {y}V{y-2.2}'
                                        f'Q{x-1.6} {y-2.2} {x} {y-3.1}Z'), .35)
            mark = subtract(shield, stroke(f'M{x-1.35} {y+.1}L{x-.35} {y+1.15}L{x+1.4} {y-1.0}'))
        elif kind == 'star':
            mark = api['soften'](transform(api['STAR'], scale=.46, dx=x-8, dy=y-7.9), .25)
        clearance = union(mark, stroke(mark, 2*GAP, exact=True))
        if kind == 'search':
            clearance = union(clearance, circle(x-.45, y-.45, 2.15+GAP))
        if name == 'user-cog':
            # users-cog (sf_ext_states) reuses this drawing's detail at its
            # former place and size; keep that detail and compose every style here.
            shape(name, base, gear(12.35, 10.45, 2.75), tags)
            b = api['DRAWINGS'][name][0]
            rim = stroke(b)
            host = subtract(union(b, rim), clearance)
            ink = union(subtract(rim, clearance), mark)
            overrides[name] = {'duotone': [(subtract(host, union(rim, clearance)), .24), (ink, 1)],
                               'stroke': ink, 'solid': union(host, mark)}
            return
        shape(name, base, mark, tags)
        BADGES[name] = (mark, clearance)

    for prefix, base in (('user', user_body), ('user-round', user_round)):
        for suffix, kind in (('cog','cog'),('exclamation-point','alert'),('key','key'),('minus','minus'),
                             ('pen','pen'),('search','search'),('shield','shield'),('star','star')):
            person_badge(prefix+'-'+suffix, base, kind, 'person account '+suffix.replace('-',' '))
    for suffix, kind in (('arrow-left','arrow-left'),('check','check'),('plus','plus'),('x','x')):
        person_badge('user-round-'+suffix, user_round, kind, 'person account '+suffix.replace('-',' '))
    person_badge('user-lock', user_body, 'lock', 'person account lock')

    def placed(base, scale, right=None, left=None, bottom=13.1, centre=None):
        x0, y0, x1, y1 = base.bounds
        x0, y0, x1, y1 = x0-.52, y0-.52, x1+.52, y1+.52
        if centre is not None: dx = centre-scale*(x0+x1)/2
        elif right is not None: dx = right-scale*x1
        else: dx = left-scale*x0
        return base.transform(scale,0,0,scale,dx,bottom-scale*y1)
    empty = po.Path()
    # SF person.2: the rear person smaller and to the left of the front one,
    # both heads whole and apart.
    layered('users-round', [(placed(user_round, .72, left=.7), empty),
                            (placed(user_round, .86, right=15.3), empty)], 'people round group')
    # SF person.3: one person in front, two smaller ones behind on either side.
    for name, base in (('user-group', user_body), ('user-round-group', user_round)):
        layered(name, [(placed(base, .62, left=.7), empty),
                       (placed(base, .62, right=15.3), empty),
                       (placed(base, .78, centre=8, bottom=13.4), empty)], 'people group')
    # SF person.line.dotted.person: two people linked by a dotted line.
    for name, base in (('users-collaboration', user_body), ('users-round-collaboration', user_round)):
        pair = [(placed(base, .56, left=.7, bottom=12.5), empty),
                (placed(base, .56, right=15.3, bottom=12.5), empty)]
        layered(name, pair, 'people collaboration',
                extra=dots((6.75, 8.35), (8, 8.35), (9.25, 8.35), r=.5))

    # Envelopes, measured against SF envelope (15.5 x 11.0) and its badges.
    envelope, flap = api['DRAWINGS']['mail'][:2]
    ex0, ey0, ex1, ey1 = envelope.bounds
    env_ink = (ex0-.52, ey0-.52, ex1+.52, ey1+.52)
    fl = flap.bounds
    flap_centerline = path(f'M{fl[0]+.52} {fl[1]+.52}L{(fl[0]+fl[2])/2} {fl[3]-.52}L{fl[2]-.52} {fl[1]+.52}')
    def env_layout(box):
        return fit(env_ink, box)
    def env_flap(T, s):
        return T(flap) if s > .97 else stroke(T(flap_centerline))
    def badged_mail(name, tags, kind=None, mark=None, at=None, r=3.3):
        at = at or (env_ink[2]+.47-r, env_ink[3]+2.13-r)
        T, s = env_layout((at[0]-r, at[1]-r, at[0]+r, at[1]+r))
        shape(name, T(envelope), env_flap(T, s), tags)
        c = T(path(f'M{at[0]} {at[1]}h.001')).bounds
        if kind:
            api['badge'](name, kind, c[0], c[1], r*s)
        else:
            BADGES[name] = mark(c[0], c[1], s)
    # SF envelope.badge: a notification dot over the upper right corner.
    badged_mail('mail-badge', 'email notification', kind='dot', r=2.0,
                at=(env_ink[2]+.47-2.0, env_ink[1]-1.13+2.0))
    for suffix, kind in (('clock','clock'),('exclamation-point','alert'),('minus','minus'),('x','x')):
        badged_mail('mail-'+suffix, 'email message '+suffix.replace('-',' '), kind=kind)
    def knocked(d, scale=.72):
        def make(cx, cy, s):
            ink = stroke(path(d).transform(scale*s,0,0,scale*s,cx,cy))
            if d is marks['question-mark']:
                ink = union(ink, circle(cx, cy+2.15*scale*s, .62))
            return subtract(circle(cx, cy, 3.3*s), ink), circle(cx, cy, (3.3+GAP)*s)
        return make
    badged_mail('mail-question-mark', 'email message question mark', mark=knocked(marks['question-mark'], .78))
    def mail_pen(cx, cy, s):
        ink = stroke(path('M-1.55 1.55L-1.3 .5L.85 -1.65L1.85 -.65L-.3 1.5Z').transform(s,0,0,s,cx,cy))
        return subtract(circle(cx, cy, 3.3*s), ink), circle(cx, cy, (3.3+GAP)*s)
    badged_mail('mail-pen', 'email message pen', mark=mail_pen)
    def mail_lens(cx, cy, s):
        glass = union(api['ring'](cx-.5*s, cy-.5*s, 2.2*s), line((cx+1.05*s, cy+1.05*s), (cx+2.6*s, cy+2.6*s)))
        return glass, union(circle(cx-.5*s, cy-.5*s, (2.2+GAP)*s), stroke(glass, 2*GAP, exact=True))
    badged_mail('mail-search', 'email message search', mark=mail_lens)
    shape('mail-dot', envelope, union(flap, circle((ex0+ex1)/2, ey1-2.55, .9)), 'email message dot')
    # SF envelope.stack: the envelope with two receding edges above it.
    T, s = fit(env_ink, (env_ink[0], env_ink[1]-3.3, env_ink[2], env_ink[1]))
    top = T(path(f'M0 {ey0}h.001')).bounds[1]
    left, right = T(path(f'M{ex0} 0h.001')).bounds[0], T(path(f'M{ex1} 0h.001')).bounds[0]
    edges = union(line((left+1.45, top-1.6), (right-1.45, top-1.6)), line((left+2.9, top-3.2), (right-2.9, top-3.2)))
    shape('mails', T(envelope), union(env_flap(T, s), edges), 'multiple email messages')

    api['CATEGORY'] = 'Product tools'
    # Status variants keep the full-size family symbol and carry an SF badge
    # (filled disc with the mark knocked out, or a gear, lens or pencil) in the
    # lower trailing corner behind a 0.9 u gap. main() composes every style.
    for suffix in ('check', 'minus', 'plus', 'x'):
        sf_host('database-'+suffix, 'database', 'storage database '+suffix)
        sf_badge('database-'+suffix, suffix)
    sf_host('database-cog', 'database', 'storage database cog')
    sf_gear_badge('database-cog')
    sf_host('database-search', 'database', 'storage database search')
    sf_lens_badge('database-search')
    sf_host('database-backup', 'database', 'database backup restore')
    sf_badge('database-backup', 'clock')
    for suffix, kind in (('check','check'),('minus','minus'),('plus','plus'),('question-mark','question'),('x','x')):
        sf_host('package-'+suffix, 'package', 'parcel package '+suffix)
        sf_badge('package-'+suffix, kind)
    sf_host('package-search', 'package', 'parcel package search')
    sf_lens_badge('package-search')
    sf_host('package-pen', 'package', 'parcel package pen')
    sf_pencil_badge('package-pen')
    shape('package-2',path('M2 4L8 1.5L14 4V12L8 14.5L2 12Z'),stroke('M2 4L8 7L14 4M8 7V14M5 2.8L11 5.5'),'parcel box shipping')
    carton = path('M1.4 6.85L3.45 4.7L2.05 3.3L6.25 1.4L8 2.95L9.75 1.4L13.95 3.3L12.55 4.7L14.6 6.85L12.55 7.85V11.75L8 14.25L3.45 11.75V7.85Z')
    flap_seams = stroke('M3.45 4.7L8 2.95L12.55 4.7L8 6.95ZM1.4 6.85L6.05 9.15L8 6.95L9.95 9.15L14.6 6.85M8 6.95V14.25')
    shape('package-open',carton,flap_seams,'parcel open box')

    # Shields: as in checkmark.shield, the mark stays inside, centered, full weight.
    shield = api['SHIELD']
    for suffix, mark in (('minus', compact('minus', 8, 7.6, .95)), ('plus', compact('plus', 8, 7.6, .95)),
                         ('question-mark', compact('question-mark', 8, 7.55, .95)),
                         ('cog', gear(8, 7.6, 2.7)), ('user', sf_person(8, 7.55, .78))):
        shape('shield-'+suffix, shield, mark, 'security protection '+suffix)
    sf_host('shield-cog-corner', 'shield', 'security protection settings corner')
    sf_gear_badge('shield-cog-corner')
    shape('shield-ellipsis',shield,dots((5.3,7.4),(8,7.4),(10.7,7.4),r=.67),'security protection more')
    shape('shield-half',shield,stroke('M8 2V14'),'security protection half')
    shape('shield-ban',shield,op(stroke('M1.3 2.15L13.5 13.1'),shield,po.PathOp.INTERSECTION),'security forbidden')
    shape('shield-house',shield,stroke('M4.8 7.5L8 4.65L11.2 7.5M5.4 7V10.2H10.6V7M6.85 10.2V8.05H9.15V10.2'),'security home protection')
    shape('shield-off',shield,line((2,2),(14,14)),'security protection disabled')

    # Stars and hearts: full family symbol plus badge. The hidden corner marks
    # are what sf_ext_states reuses for shopping-bag-plus / -minus; main()
    # removes them with the badge clearance in every style.
    star = path('M8 1.4L9.9 5.5L14.4 6L11 9.2L11.8 13.8L8 11.5L4.2 13.8L5 9.2L1.6 6L6.1 5.5Z')
    for suffix in ('check', 'minus', 'plus', 'x'):
        sf_host('star-'+suffix, 'star', 'favorite star '+suffix, compact(suffix, 12, 11.6, .87))
        sf_badge('star-'+suffix, suffix)
    shape('star-half',star,stroke('M8 2V11.5'),'favorite star half')
    shape('star-off',star,line((2,2),(14,14)),'favorite star disabled')

    # Simple enclosed marks: SF square and circle containers.
    for suffix in ('exclamation-point','minus','plus','x'):
        shape('square-'+suffix, square, compact(suffix,8,8,1), 'status '+suffix)
    shape('square-check-big', square, check(8,8.1,.82), 'status checked')
    shape('circle-check-big', disc, check(8,8.1,.86), 'status checked')
    percent = union(stroke('M5.6 10.9L10.4 5.1'),stroke(circle(5.65,5.65,1.18)),stroke(circle(10.35,10.35,1.18)))
    shape('circle-percent', disc, percent, 'percentage ratio')
    shape('square-percent', square, transform(percent, scale=.93), 'percentage ratio')
    shape('diamond-percent',path('M8 1.28L14.72 8L8 14.72L1.28 8Z'),union(stroke('M6.05 10.1L9.95 5.9'),stroke(circle(6.3,6.4,1.08)),stroke(circle(9.7,9.6,1.08))),'percentage ratio')
    # person.crop.square / .circle: a head and shoulders that meet the frame.
    shape('square-user', square, union(stroke(circle(8,6.45,1.95)),
          stroke('M4.75 13.4V12.3Q4.75 10.55 6.5 10.55H9.5Q11.25 10.55 11.25 12.3V13.4')), 'account profile')
    shape('square-user-round', square, union(stroke(circle(8,6.45,1.95)),
          stroke('M4.25 13.4A3.75 3.75 0 0 1 11.75 13.4')), 'account round profile')
    shape('circle-user-round', disc, union(stroke(circle(8,6.3,2.15)),
          op(stroke('M2.4 13.9Q4.4 10.45 8 10.45Q11.6 10.45 13.6 13.9'), disc, po.PathOp.INTERSECTION)),
          'account round profile')
    shape('octagon-x',path('M5 1.8H11L14.2 5V11L11 14.2H5L1.8 11V5Z'),compact('x'),'stop close')
    glyph('circle-fading-check',stroke('M13.5 8A5.5 5.5 0 0 1 8 13.5M2.5 8A5.5 5.5 0 0 1 8 2.5A5.5 5.5 0 0 1 13.5 8M3.3 11L3.4 11.1M5.2 13L5.3 13.1'),compact('check'),'fading completed')
    glyph('circle-fading-plus',stroke('M13.5 8A5.5 5.5 0 0 1 8 13.5M2.5 8A5.5 5.5 0 0 1 8 2.5A5.5 5.5 0 0 1 13.5 8M3.3 11L3.4 11.1M5.2 13L5.3 13.1'),compact('plus'),'fading add')

    # Disabled versions reuse the actual subject, cut a channel through it,
    # and place the slash in that channel so the two marks remain legible.
    def disabled(name, source):
        b,d,outline,_,_ = host_drawing(source)
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
    glyph('grip', dots(*((x, y) for x in (4.6, 8, 11.4) for y in (4.6, 8, 11.4)), r=.78), None, 'grip')
    glyph('grip-horizontal', dots(*((x, y) for x in (4.6, 8, 11.4) for y in (6.3, 9.7)), r=.78), None, 'grip horizontal')
    glyph('grip-vertical', dots(*((x, y) for x in (6.3, 9.7) for y in (4.6, 8, 11.4)), r=.78), None, 'grip vertical')
    for name, geom in {
        'move':'M8 1.5V14.5M5.5 4L8 1.5L10.5 4M5.5 12L8 14.5L10.5 12M1.5 8H14.5M4 5.5L1.5 8L4 10.5M12 5.5L14.5 8L12 10.5',
        'separator-horizontal':'M2 8H14M8 1.5V5M6 3L8 5L10 3M8 14.5V11M6 13L8 11L10 13',
        'separator-vertical':'M8 2V14M1.5 8H5M3 6L5 8L3 10M14.5 8H11M13 6L11 8L13 10',
        'unfold-vertical':'M3 6.3H13M3 9.7H13M8 1.5V5M6 3.5L8 1.5L10 3.5M8 11V14.5M6 12.5L8 14.5L10 12.5',
        'locate':'M8 3A5 5 0 1 0 8 13A5 5 0 1 0 8 3M8 1.3V4M8 12V14.7M1.3 8H4M12 8H14.7',
        'locate-fixed':'M8 3A5 5 0 1 0 8 13A5 5 0 1 0 8 3M8 1.3V4M8 12V14.7M1.3 8H4M12 8H14.7M6.5 8A1.5 1.5 0 1 0 9.5 8A1.5 1.5 0 1 0 6.5 8',
        'list-checks':'M2 4L3 5L5 3M7 4H14M2 9L3 10L5 8M7 9H14M7 13H14',
        'list-filter':'M2.05 4.72H13.95M4.05 8H11.95M6.05 11.28H9.95',
        'list-tree':'M2.5 2V12.5H5.8M2.5 4.5H5.8M2.5 8.5H5.8M8.5 4.5H14M8.5 8.5H14M8.5 12.5H14',
        'spell-check':'M2 9L4 3L6 9M2.8 7H5.2M8 3H10Q12 3 12 4.5Q12 6 10 6H8ZM8 6H10.5Q12.5 6 12.5 7.5Q12.5 9 10.5 9H8ZM8.1 12.65L9.5 14.05L12.6 11.1',
        'regex':'M4.6 11.2V11.35M9.8 4.3V10.3M7.2 5.8L12.4 8.8M7.2 8.8L12.4 5.8',
        'nfc':'M5 3Q1 8 5 13M7.5 4.5Q5 8 7.5 11.5M10 6Q9 8 10 10M12.5 7V9',
        'waypoints':'M3 4L8 8L13 4M8 8L12 12M1.5 4A1.5 1.5 0 1 0 4.5 4A1.5 1.5 0 1 0 1.5 4M11.5 4A1.5 1.5 0 1 0 14.5 4A1.5 1.5 0 1 0 11.5 4M10.5 12A1.5 1.5 0 1 0 13.5 12A1.5 1.5 0 1 0 10.5 12M6.5 8A1.5 1.5 0 1 0 9.5 8A1.5 1.5 0 1 0 6.5 8',
        'voicemail':'M1.5 8A2.5 2.5 0 1 0 6.5 8A2.5 2.5 0 1 0 1.5 8M9.5 8A2.5 2.5 0 1 0 14.5 8A2.5 2.5 0 1 0 9.5 8M4 10.5H12',
    }.items():
        if name == 'waypoints':
            centers = ((3,4), (8,8), (13,4), (12,12))
            nodes = union(*(circle(x,y,1.5) for x,y in centers))
            links = api['op'](stroke('M3 4L8 8L13 4M8 8L12 12'),nodes,api['po'].PathOp.DIFFERENCE)
            glyph(name,union(links,*(stroke(circle(x,y,1.5)) for x,y in centers)),None,'connected waypoints nodes')
        else:
            glyph(name,stroke(geom),None,name.replace('-',' '))
    # arrowshape.turn.up.*: a closed arrow shape (tinted in Duotone, filled in Solid).
    turn = path('M1.75 6.75L6.45 2.65Q7.35 1.95 7.35 3.05V4.85C11.6 5 14.35 7.6 14.35 12.25'
                'Q14.35 13.2 13.7 12.5C12.35 10.6 10.4 9.6 7.35 9.55V11.35Q7.35 12.45 6.45 11.75'
                'L1.75 7.65Q1.25 7.2 1.75 6.75Z')
    shape('reply', turn, None, 'reply')
    shape('forward', api['mirror'](turn), None, 'forward')
    rear_head = stroke('M4.55 2.55L.9 5.75Q.25 6.3 .9 6.85L4.55 10.05')
    shape('reply-all', transform(turn, scale=.86, dx=1.7, dy=.3), transform(rear_head, dx=.2, dy=.95), 'reply all')
    # paperplane: closed dart with its fold line from the notch to the tip.
    plane = path('M2.25 2.35L14.05 7.4Q14.7 7.7 14.05 8L2.25 13.65Q1.45 14 1.7 13.15L3.45 7.7L1.7 2.85Q1.45 2 2.25 2.35Z')
    shape('send-horizontal', plane, stroke('M3.45 7.7H8.6'), 'send horizontal')
    # The three open terminals sweep around the outside of the triangle.
    hook = stroke('M6.05 2.7A2.2 2.2 0 1 1 7.5 5.64L12 10.25')
    glyph('webhook',union(hook,transform(hook,120),transform(hook,240)),None,'webhook')
    # text.badge.*: rows of text with an SF badge in the trailing lower corner.
    list_rows = stroke('M2 3.4H14M2 7.2H14M2 11H6.9')
    for suffix, kind in (('clock','clock'),('minus','minus'),('plus','plus'),('x','x')):
        glyph('list-'+suffix, list_rows, None, 'list '+suffix)
        sf_badge('list-'+suffix, kind, 12, 12, 3.1)

    # Hollow inactive bars preserve the full signal silhouette at zero and
    # low strengths; the filled bars indicate the actual active count.
    for suffix, count in (('zero',0),('low',1),('medium',2),('high',3),('',4)):
        bars = []
        for i, height in enumerate((3.7,6,8.3,10.6)):
            centerline = rr(1.3 + i*3.85,14.15-height,1.8,height-1.1)
            rim = stroke(centerline)
            bars.append(union(centerline,rim) if i < count else rim)
        glyph('signal'+('-'+suffix if suffix else ''),union(*bars),None,'mobile signal '+suffix)
    zero = circle(8,13,.75)
    low = union(zero,stroke('M6 10.5Q8 9 10 10.5'))
    high = union(low,stroke('M2 5Q8 .5 14 5M4 8Q8 5 12 8'))
    for level, ink in (('zero',zero),('low',low),('high',high)):
        glyph('wifi-'+level,ink,None,'wireless signal '+level)

    # Family symbols with SF badges.
    for source, suffixes in (('archive',('arrow-down','arrow-up','x')), ('heart',('minus','plus','x')),
                             ('map-pin',('plus','x')), ('save',('check','plus')), ('tag',('plus','x'))):
        for suffix in suffixes:
            legacy = compact('minus', 12, 11.6, .87) if (source, suffix) == ('heart', 'minus') else None
            sf_host(source+'-'+suffix, source, source.replace('-', ' ')+' '+suffix, legacy)
            sf_badge(source+'-'+suffix, suffix)
    sf_host('save-pen', 'save', 'save pen')
    sf_pencil_badge('save-pen')
    # Bells carry their badge at the top trailing corner (bell.badge).
    for suffix in ('check', 'minus'):
        sf_host('bell-'+suffix, 'bell', 'bell '+suffix)
        sf_badge('bell-'+suffix, suffix, 11.9, 4.1)
    sf_host('bell-dot', 'bell', 'bell dot')
    sf_badge('bell-dot', 'dot', 12.25, 3.75, 2.55)
    # checkmark.icloud: the mark sits inside the cloud's lower body.
    cloud_body = drawings['cloud'][0]
    left, top_edge, right, bottom = cloud_body.bounds
    cx, cy = (left+right)/2, bottom-3.05
    shape('cloud-check', cloud_body, check(cx, cy, .72), 'cloud check')
    shape('cloud-sync', cloud_body, compact('sync', cx, cy-.05, .86), 'cloud sync')
    for source, name in (('monitor','monitor-cog'), ('server-rack','server-cog'), ('hourglass','hourglass-cog')):
        sf_host(name, source, name.replace('-', ' '))
        sf_gear_badge(name)
    sf_host('alarm-clock-check', 'alarm-clock', 'alarm clock check')
    sf_badge('alarm-clock-check', 'check')
    disabled('alarm-clock-off','alarm-clock')
    sf_host('image-minus', 'image', 'image minus')
    sf_badge('image-minus', 'minus')

    api['CATEGORY'] = 'Devices and connectivity'
    # Closed captions: SF rectangle proportions with two open C counters.
    cc = stroke('M6.88 6.85A1.8 1.8 0 1 0 6.88 9.15M11.88 6.85A1.8 1.8 0 1 0 11.88 9.15')
    shape('captions', rr(1.45,2.65,13.1,10.7), cc, 'subtitles closed captions accessibility')
    slashed('captions-off', rr(1.45,2.65,13.1,10.7), cc, 'subtitles closed captions disabled')
    lens_mount = union(stroke('M10.86 5.3L14 4.6V8.15L10.4 7.7M6 8.3L7.6 12.2H12M12 10.4V14'),circle(3.5,5.5,.7))
    shape('cctv',path('M2 3L11 4.5L10.2 9L1.2 7.5Z'),lens_mount,'security surveillance camera')
    slashed('cctv-off',path('M2 3L11 4.5L10.2 9L1.2 7.5Z'),lens_mount,'security surveillance camera disabled')
    shape('ethernet-port',path('M2 2.5H14V11H11V13.5H5V11H2Z'),stroke('M4.7 4.45V6.8M6.9 4.45V6.8M9.1 4.45V6.8M11.3 4.45V6.8M2 9H14'),'wired network port')
    ram = rr(1.35,2.05,13.3,10.1)
    chips = union(stroke(rr(3.55,4.05,4.05,2.2)),stroke(rr(3.55,8.35,4.05,2.2)),
                  stroke(rr(9.75,4.05,2.8,6.5)))
    pins = stroke('M3.5 12.15V14.05M5.75 12.15V14.05M8 12.15V14.05M10.25 12.15V14.05M12.5 12.15V14.05')
    shape('memory-stick',ram,union(chips,pins),'computer ram memory')
    # SF wifi.router: a low, wide base under two concentric waves.
    waves = stroke('M5.45 6.15A3.6 3.6 0 0 1 10.55 6.15M3.55 4.25A6.3 6.3 0 0 1 12.45 4.25')
    shape('router', rr(1.25,8.7,13.5,4.55,1.6,exact=True),
          union(waves, stroke('M3.65 10.95H5.6'), dots((8.4,10.95),(10.35,10.95),(12.3,10.95),r=.62)),
          'wireless router network')
    # SF hifispeaker: a tall cabinet, small tweeter over a large woofer.
    shape('speaker', rr(3.55,1.9,8.9,12.2), union(api['ring'](8,9.85,2.75), circle(8,4.7,.95)), 'audio loudspeaker')
    shape('touchpad',rr(1.8,2.5,12.4,11),stroke('M2 10H14M8 10V13'),'trackpad computer input')
    slashed('touchpad-off',rr(1.8,2.5,12.4,11),stroke('M2 10H14M8 10V13'),'trackpad computer input disabled')
    shape('webcam',circle(8,6.5,4.8),union(stroke(circle(8,6.5,1.7)),stroke('M8 11.3V13.5M5.5 14H10.5')),'camera video computer')
    # SF headset: a single-weight band, filled ear cups and a short boom.
    cups = union(rr(1.6,7.35,2.75,4.75,1.3,exact=True), rr(11.65,7.35,2.75,4.75,1.3,exact=True))
    glyph('headset', cups, union(stroke('M2.95 8.2V7.3A5.05 5.05 0 0 1 13.05 7.3V8.2'),
                                 stroke('M13.05 12V12.4Q13.05 14.15 11.3 14.15H9.6')),
          'headphones microphone call')
    # SF iphone: 8.2 x 13.5 with a short island; the account sits on the screen.
    phone = rr(4.42,1.75,7.16,12.5,1.9,exact=True)
    shape('smartphone-user-round', phone,
          union(stroke('M7.2 3.65H8.8'), filled_person.transform(1.05,0,0,1.05,8,8.65)),
          'mobile phone account')
    display = rr(1.4,2.1,13.2,8.95)
    share_ink = stroke('M8 11.05V13.9M5.3 13.9H10.7M8 8.75V4.6M6.1 6.5L8 4.6L9.9 6.5')
    shape('screen-share', display, share_ink, 'display share presentation')
    # The arrow moves right of the slash so both remain whole.
    slashed('screen-share-off', display, stroke('M8 11.05V13.9M5.3 13.9H10.7M11.05 7.75V4.45M9.55 5.95L11.05 4.45L12.55 5.95'),
            'display share disabled')
    # SF cursorarrow: a slim arrow, upright left edge and a narrow tail.
    pointer = path('M4.9 2.1L4.9 11.55L7.05 9.75L8.6 13.6L10.05 13L8.5 9.3L11.1 9.25Z')
    shape('mouse-pointer', pointer, None, 'cursor pointer')
    small_pointer = pointer.transform(.84,0,0,.84,8-8*.84+1.75,8-8*.84+1.45)
    shape('mouse-pointer-click', small_pointer,
          stroke('M7.05 3.05V1.5M5.25 4.85H3.7M5.75 3.55L4.6 2.4M8.55 3.35L9.45 2.15'),
          'cursor click')
    rune = path('M3 5.76L12 10.8L7 14.3V1.7L12 5.2L3 10.24')
    glyph('bluetooth-connected',stroke(rune),dots((1.55,8),(14.45,8),r=.75),'wireless connected')
    glyph('bluetooth-searching',stroke(transform(rune,dx=-1)),stroke('M13.1 4.8Q15.5 8 13.1 11.2'),'wireless searching')
    shape('volume-1',path('M2 6H5L9 2.5V13.5L5 10H2Z'),stroke('M11.5 6Q13.5 8 11.5 10'),'audio sound low')

    api['CATEGORY'] = 'Interface controls'
    # viewfinder corners: rounded, as in SF *.viewfinder and the family scan.
    finder = 'M2 5.2V3.25Q2 2 3.25 2H5.2M10.8 2H12.75Q14 2 14 3.25V5.2M14 10.8V12.75Q14 14 12.75 14H10.8M5.2 14H3.25Q2 14 2 12.75V10.8'
    for name, geom in {
        'languages':'M2 4H10M6 2V4M3.5 5Q4.35 7.95 8 10M8.5 5Q7.5 9 2.5 11M10 14L12.25 7.9L14.5 14M10.7 12.25H13.8',
        'link-2':'M6 10L5 11A2.5 2.5 0 0 1 1.5 7.5L4 5A2.5 2.5 0 0 1 7.5 5M10 6L11 5A2.5 2.5 0 0 1 14.5 8.5L12 11A2.5 2.5 0 0 1 8.5 11M5.5 10.5L10.5 5.5',
        'loader':'M8 1.5V3.5M12.6 3.4L11.2 4.8M14.5 8H12.5M12.6 12.6L11.2 11.2M8 14.5V12.5M3.4 12.6L4.8 11.2M1.5 8H3.5M3.4 3.4L4.8 4.8',
        'scan-barcode':finder+'M4.9 5.3V10.7M6.95 5.3V10.7M9.05 5.3V10.7M11.1 5.3V10.7',
        'scan-qr-code':finder+'M4.9 4.9H7.1V7.1H4.9ZM8.9 4.9H11.1V7.1H8.9ZM4.9 8.9H7.1V11.1H4.9ZM9.15 9.15H11V11',
        'scan-text':finder+'M5 5.6H11M5 8H11M5 10.4H9',
        'ungroup':finder+'M4.6 4.6H7.4V7.4H4.6ZM8.6 8.6H11.4V11.4H8.6Z',
        'table-cells-merge':'M1.65 2H10.65V9.2H1.65ZM1.65 5.6H10.65M6.15 2V9.2M6.95 11.5L8.55 13L6.95 14.5M14.2 11.5L12.6 13L14.2 14.5',
        'table-cells-split':'M1.65 2H10.65V9.2H1.65ZM1.65 5.6H10.65M6.15 2V9.2M8.6 11.5L7 13L8.6 14.5M12.6 11.5L14.2 13L12.6 14.5',
    }.items(): glyph(name,stroke(geom),None,name.replace('-',' '))
    # slider.vertical.3: capsule knobs interrupt three tracks.
    tracks = []
    for x, knob in ((3.6, 7.9), (8, 3.7), (12.4, 9.3)):
        tracks += [stroke(rr(x-1.15, knob, 2.3, 3.2, 1.15, exact=True)),
                   line((x, 2.85), (x, knob)) if knob > 3.4 else po.Path(),
                   line((x, knob+3.2), (x, 13.15))]
    glyph('sliders-vertical', union(*tracks), None, 'sliders vertical')

    # sidebar.left: SF rectangle proportions, sidebar divider, chevron in the pane.
    panel = union(stroke(rr(1.2,2.6,13.6,10.8)),stroke('M5.65 2.6V13.4'))
    for action, chevron in (('close','M11.15 6.05L9.2 8L11.15 9.95'),('open','M9.3 6.05L11.25 8L9.3 9.95')):
        glyph('panel-left-'+action,panel,stroke(chevron),'panel left '+action)

    heading = api['DRAWINGS']['heading-1'][0]
    glyph('heading-3',heading,stroke('M10.75 5Q14.15 3.25 14.05 6.4Q14 7.8 11.95 8Q14.3 8.1 14.3 10.15Q14.3 12.6 10.75 11.7'),'heading 3')
    glyph('heading-4',heading,stroke('M13.6 12.35V4.35L10.15 9.45H14.7'),'heading 4')

    events = union(line((1.6,8),(14.4,8)),stroke('M4 8V4M8 8V12M12 8V4'),
                   dots((4,3.5),(8,12.5),(12,3.5),r=1.25))
    glyph('timeline', events, None, 'timeline')
    api['CATEGORY'] = 'Symbols'
    for suffix, geom in {
        'aquarius':'M1.9 6.05Q3.4 3.7 4.95 5.25T8 5.25T11.05 5.25T14.1 4.45M1.9 11.55Q3.4 9.2 4.95 10.75T8 10.75T11.05 10.75T14.1 9.95',
        'aries':'M8 14V7Q8 2 4.5 2Q2 2 2 5M8 7Q8 2 11.5 2Q14 2 14 5',
        'cancer':'M5 3.8A2.15 2.15 0 1 0 5 8.1A2.15 2.15 0 1 0 5 3.8M5 3.8C8.1 3.8 10.25 2.5 13.2 4.05M11 12.2A2.15 2.15 0 1 0 11 7.9A2.15 2.15 0 1 0 11 12.2M11 12.2C7.9 12.2 5.75 13.5 2.8 11.95',
        'capricorn':'M1.9 4.25L4.2 10.1L6.45 3.85C7.55 6.95 7.7 12.65 10.35 13.15C13.4 13.75 14.85 9.15 12.05 8.8C10.45 8.55 9.7 10.15 8.65 11.5',
        'gemini':'M3 2.5Q8 4 13 2.5M5 3.5V12.5M11 3.5V12.5M3 13.5Q8 12 13 13.5',
        'leo':'M5.5 8.6A2 2 0 1 0 1.5 8.6A2 2 0 1 0 5.5 8.6M5.5 8.6C5.5 6.5 4.8 5.4 5.1 3.8C5.8 .55 11.3 1.1 11.3 4.7C11.3 7 8.6 9.5 8.6 11.8C8.6 14.6 11.7 15 13.7 12.7',
        'libra':'M2 10H6Q4 8.5 4 6.5A4 4 0 0 1 12 6.5Q12 8.5 10 10H14M2 13H14',
        'ophiuchus':'M3.5 2.5V9Q3.5 13.5 8 13.5Q12.5 13.5 12.5 9V2.5M1.8 7Q3.4 5.3 5 7T8.2 7T11.4 7T14.6 7',
        'pisces':'M3 2Q8 8 3 14M13 2Q8 8 13 14M2 8H14',
        'sagittarius':'M3 13L13 3M8 3H13V8M5 7L9 11',
        'scorpio':'M1.75 4.3V11.5M1.75 6.25Q2.25 3.75 3.85 3.95Q5.25 4 5.25 6V11.5M5.25 6.25Q5.75 3.75 7.4 3.95Q8.75 4 8.75 6V10.15Q8.75 12 10.8 12H14.1M12.35 10.05L14.3 12L12.35 13.95',
        'taurus':'M4 8A4 4 0 1 0 12 8A4 4 0 1 0 4 8M5 4Q2 3 2 1.5M11 4Q14 3 14 1.5',
        'virgo':'M1.7 4V11.8M1.7 6Q2.2 3.8 3.75 4Q5.1 4.1 5.1 6V11.8M5.1 6Q5.65 3.8 7.25 4Q8.6 4.1 8.6 6V9.1C8.6 11.5 10.75 13 13.8 13.85M8.65 6.45C12.25 3.05 15.65 6.7 12.3 10.5Q10.25 12.65 7.7 13.6',
    }.items(): glyph('zodiac-'+suffix,stroke(geom),None,'astrology zodiac '+suffix)

    api['CATEGORY'] = 'Product tools'
    shape('briefcase-medical',rr(1.5,5,13,9),union(stroke('M5 5V2.5H11V5'),plus(8,9.5,.82)),'medical first aid case')
    buildings = path('M2 14V5.5H6.6V2H14V14Z')
    building_windows = path('M4.35 8.25V9.3M4.35 11.4V12M9 4.65V5.5M11.65 4.65V5.5M9 7.65V8.5M11.65 7.65V8.5M9 10.7V11.55')
    shape('building-complex',buildings,stroke(building_windows),'buildings office complex')
    sf_host('building-complex-plus','building-complex','buildings office complex plus')
    sf_badge('building-complex-plus','plus')
    wall = rr(1.7,3,10.5,10)
    mortar = stroke('M1.7 6.3H12.2M1.7 9.65H12.2M5.2 3V6.3M4.15 6.3V9.65M8.1 6.3V9.65M5.2 9.65V13')
    shield_badge = path('M12 8L14.5 9V11Q14.5 13 12 14Q9.5 13 9.5 11V9Z')
    fire_badge = path('M11.8 14.25C9.95 14.25 9 13.05 9.25 11.55Q9.4 10.2 10.45 9.05Q10.5 10.2 11.35 10.55Q12.65 8.85 12.05 6.9C15.55 9.7 15.2 14.1 11.8 14.25Z')
    for name, badge in (('brick-wall-fire',fire_badge),('brick-wall-shield',shield_badge)):
        shape(name,wall,union(mortar,stroke(badge)),'firewall network security '+name.split('-')[-1])
        # Use the same open corner for both badges. Outlining the clearance
        # would add another mortar joint at the edge of the shield or flame.
        gap = union(badge,stroke(badge,3.3))
        wall_ink = subtract(union(stroke(wall),mortar),gap)
        ink = union(wall_ink,stroke(badge))
        surface = union(subtract(wall,gap),badge)
        solid = union(subtract(subtract(union(wall,stroke(wall)),mortar),gap),badge)
        overrides[name] = {'stroke':ink,'duotone':[(subtract(surface,ink),.24),(ink,1)],'solid':solid}

    diploma = rr(1.65,1.95,11.6,9.05)
    seal = circle(10.5,8.35,2.45)
    left_tail = path('M8.9 9.4L6.6 14.25L9.5 13.65L11.1 10Z')
    right_tail = left_tail.transform(-1,0,0,1,21,0)
    tails = union(left_tail,right_tail)
    award = union(seal,tails)
    lettering = stroke('M3.85 4.2H6.65M3.85 6.55H4.9')
    shape('certificate',diploma,union(lettering,stroke(award)),'award certificate credential')
    # Run each ribbon behind the seal. The two open interiors are large
    # enough to distinguish the tails at the native size.
    award_ink = union(stroke(seal),subtract(union(stroke(left_tail),stroke(right_tail)),seal))
    clearance = union(award,stroke(award,4.35))
    paper = subtract(diploma,clearance)
    ink = union(stroke(paper),subtract(lettering,clearance),award_ink)
    surface = union(paper,award)
    solid_seal = union(seal,subtract(tails,union(seal,stroke(seal,2.1))))
    overrides['certificate'] = {'stroke':ink,'duotone':[(subtract(surface,ink),.24),(ink,1)],
                                'solid':union(subtract(paper,lettering),solid_seal)}
    contact_cover = rr(3.2,1.85,10.5,12.3)
    portrait = sf_person(8.95,8.15,.82)
    loops = union(*(stroke(rr(1.4,y,3.7,2.2)) for y in (4.2,9.6)))
    holes = union(*(rr(.65,y-.8,5.4,3.8) for y in (4.2,9.6)))
    shape('contact-round',contact_cover,union(portrait,loops),'address book contact person')
    cover_edge = stroke(contact_cover)
    contact_ink = union(subtract(cover_edge,holes),loops,portrait)
    contact_solid = union(subtract(union(contact_cover,cover_edge),union(holes,portrait)),loops)
    overrides['contact-round'] = {'duotone':[(subtract(contact_cover,union(contact_ink,holes)),.24),(contact_ink,1)],
                                  'stroke':contact_ink,'solid':contact_solid}
    shape('delete',path('M5 3H13Q14 3 14 4V12Q14 13 13 13H5L1.5 8Z'),cross(9,8,.7),'backspace delete key')
    gear_points = []
    for tooth in range(8):
        for offset, radius in ((-.32,5.1),(-.18,6.5),(.18,6.5),(.32,5.1)):
            angle = tooth*math.pi/4+offset
            gear_points.append((8+radius*math.cos(angle),8+radius*math.sin(angle)))
    shape('cog',api['poly'](gear_points),stroke(circle(8,8,2.2)),'gear settings')
    globe = circle(6.9,7.1,5.65)
    # Closed coastlines and an outlined lock retain their counters at small sizes.
    land = path('M1.45 5.2Q3 2.5 5.45 2L6.1 3.65L5.15 5.1L3.8 5.55L3.3 7.3L1.4 6.65Z M8.6 2L11.6 2.6L12.8 4.7L11.5 6.3L10.1 5.55L9.7 4.2L8.4 3.6Z M5.1 7.75Q5.55 7.05 6.65 7.55L8.25 8.45Q8.65 8.95 7.9 10L6.85 11.65L5.9 10.45L5.7 9.15Z')
    coast = op(stroke(land),globe,po.PathOp.INTERSECTION)
    meridians = stroke('M6.9 1.45V12.75M6.9 1.45C3.15 5.2 3.15 9 6.9 12.75C10.65 9 10.65 5.2 6.9 1.45Z')
    parallels = op(stroke('M1.25 5.05H12.55M1.25 9.05H12.55'),globe,po.PathOp.INTERSECTION)
    lock_body = rr(10.35,10.95,4.4,3.7)
    shackle = stroke('M11.15 10.95V9.65A1.4 1.4 0 0 1 13.95 9.65V10.95')
    lock = union(stroke(lock_body),shackle)
    earth_lock_space = union(lock_body,shackle,stroke(union(lock_body,shackle),2.2))
    globe_lock_outline = union(lock_body,lock,path('M11.15 11V9.65A1.4 1.4 0 0 1 13.95 9.65V11Z'))
    for name, detail in (('earth-lock',coast),('globe-lock',union(meridians,parallels))):
        shape(name, globe, union(detail,lock), 'world globe security lock')
        lock_space = (union(globe_lock_outline,stroke(globe_lock_outline,3.25))
                      if name == 'globe-lock' else earth_lock_space)
        edge = stroke(globe)
        host = union(recess(globe,lock_space),subtract(union(edge,detail),lock_space))
        ink = union(host,lock)
        solid = union(subtract(subtract(union(globe,edge),detail),lock_space),lock_body,lock)
        overrides[name] = {'duotone':[(subtract(union(subtract(globe,lock_space),lock_body),ink),.24),(ink,1)],
                           'stroke':ink,'solid':solid}

    marker = path('M3.45 9.7L10.4 2.75L13.3 5.65L6.35 12.6L5.25 12.15L3.85 13.55H1.85L3.85 10.7Z')
    shape('highlighter',marker,stroke('M8.95 4.2L11.85 7.1M7.4 14H12.4'),'marker pen highlighting')
    identity_card = rr(2.5,5.55,11,8.65)
    lanyard = stroke('M5.7 1.85L8 4.95L10.3 1.85M8 4.95V5.65')
    identity = union(sf_person(6.55, 9.95, .62), stroke('M9.9 8.9H11.3M9.9 11.1H11.3'))
    shape('id-card-lanyard',identity_card,union(lanyard,identity),'identity badge lanyard')
    overrides['id-card-lanyard'] = {'solid':union(subtract(union(identity_card,stroke(identity_card)),identity),lanyard)}
    shape('key-square',square,compact('key',8,8,1.12),'security key')
    # list.bullet.rectangle / rectangle.split: SF rectangle proportions.
    window = rr(1.2,2.6,13.6,10.8)
    shape('layout-list',window,union(stroke(rr(3.65,4.75,2.4,2.4,.7,exact=True)),stroke(rr(3.65,8.85,2.4,2.4,.7,exact=True)),
                                     stroke('M7.75 5.95H12.2M7.75 10.05H12.2')),'layout list')
    shape('layout-template',window,stroke('M1.2 6.3H14.8M6 6.3V13.4'),'layout template panels')
    # lock: SF's narrow body (8.7 x 12.5 overall) with a keyhole on the body.
    keyhole = union(circle(8,9.9,1.05),line((8,10.3),(8,11.85)))
    lock_body = rr(4.15,7.05,7.7,6.7)
    shape('lock-keyhole',lock_body,union(stroke('M5.35 7.05V4.9A2.65 2.65 0 0 1 10.65 4.9V7.05'),keyhole),'security locked keyhole')
    shape('lock-keyhole-open',transform(lock_body,dx=-1.6),
          union(stroke('M9.25 7.05V4.9A2.65 2.65 0 0 1 14.55 4.9V5.9'),transform(keyhole,dx=-1.6)),'security unlocked keyhole')
    notebook = rr(2,1.75,9.8,12.5)
    tabs = union(rr(11.15,3.55,2.85,2.65),rr(11.15,8.55,2.85,2.65))
    stack('notebook-tabs',tabs,notebook,stroke('M4.35 1.75V14.25M6.5 5.1H9.55M6.5 7.55H8.95'),'notebook index tabs')
    shape('newspaper',rr(2,2.5,12,11),stroke('M4 5H8V8H4ZM10 5H12M10 7H12M4.25 9.65H11.75M4.25 11.55H10.35'),'news paper article')
    shape('vault',rr(1.7,1.7,12.6,12.6),union(stroke(circle(8,8,3.5)),circle(8,8,.9),stroke('M8 4.5V6M8 10V11.5M4.5 8H6M10 8H11.5M12.5 3V4M12.5 12V13')),'safe vault security')
    shape('wallet-minimal',rr(2,4,12,8),union(stroke('M2.2 6.45H11.75Q14 6.45 14 8.7'),circle(11,9,.65)),'money wallet')
    pocket = rr(1.8,6.1,12.4,7.5)
    cards = path('M3.2 6.5V4.4L10.5 1.95L11.5 4.7L13 4.4V6.5Z')
    stack('wallet-cards',cards,pocket,stroke('M14.2 8.5H11.4A1.25 1.25 0 0 0 11.4 11H14.2'),'money wallet payment cards')

    fist = path('M2.6 6Q2.6 4 4.7 4Q5.15 2.5 7.1 3.2Q8.3 2 9.9 3.3Q12.7 2.8 12.9 5.2L13.4 8.5Q13.6 10.1 12.3 11.5L11.4 13.8H5L4.4 12Q2.6 10.6 2.6 8.3Z')
    shape('hand-fist',fist,stroke('M4.8 4V6.4M7.3 3.4V6M9.9 3.5V5.9M12.8 7.7L9 6.6Q7.3 6.3 7.1 7.6Q7 8.6 8.2 9.1L10 9.9'),'hand closed fist gesture')
    palm = path('M1.65 10.05L4.2 8.65Q5.45 7.95 6.85 8.8L8.6 9.85Q9.4 10.35 8.9 11.05L12.45 9.7Q13.85 9.25 14.1 10.2Q14.25 10.95 13.3 11.55L9.75 13.75Q8.65 14.35 7 13.95L1.65 12.55Z')
    shape('hand-heart',palm,union(stroke('M5.35 10.2L7.35 11.15Q8.15 11.5 8.9 11.05'),
                                 compact('heart',8.35,4.7,1.02)),'care giving love hand')
    clasp = path('M1.4 7.2L4 3.7L7.3 4.3L8.6 3.5Q9.5 3 10.6 3.7L14.6 6.2L12.9 9.1L10.5 11.9Q9.8 12.8 8.9 12.2L5.1 10.1L3.9 10.3Z')
    shape('handshake',clasp,stroke('M7.3 4.3L5.8 6.2Q5.1 7.2 6.2 7.7Q6.8 8 7.5 7.5L9.1 6.5L12.2 9.6M7.4 9.5L9.8 11.4'),'agreement partnership handshake')
    fedora = path('M3.7 7.4L5.1 2.5Q5.3 1.8 6.1 2.1L8 2.9L9.9 2.1Q10.7 1.8 10.9 2.5L12.3 7.4Z')
    lenses = union(stroke(circle(4.8,11.6,2.05)), stroke(circle(11.2,11.6,2.05)),
                   stroke('M6.75 12.1Q8 11.1 9.25 12.1M5.9 9.85Q8 8.65 10.1 9.85'))
    shape('hat-glasses',fedora,union(stroke('M1.75 7.4H14.25M4.4 5.15H11.6'),lenses),'incognito disguise hat glasses')
    shape('images',union(rr(1.5,1.5,9,9),rr(5,5,9.5,9.5)),union(stroke('M5 6Q5 5 6 5H13.5Q14.5 5 14.5 6V13.5Q14.5 14.5 13.5 14.5H6Q5 14.5 5 13.5ZM5 12L8 9L10 11L12 8.5L14 11'),circle(8,7,.6)),'photos multiple images')
    stand = path('M1.75 5.8L11.95 2.35L14.25 5.55L4 9Z')
    shape('lectern',stand,stroke('M8.2 7.65V13.65M4.85 13.8H11.55'),'podium speech presentation')
    books = union(rr(1.5,3.1,2.25,10.4),rr(5.95,2,2.25,11.5),
                  path('M10.15 3.45L12.45 2.95L14.55 12.95L12.25 13.45Z'))
    shape('library',books,stroke('M1.5 5.6H3.75M1.5 11H3.75M5.95 4.65H8.2M5.95 11H8.2M10.65 5.8L12.95 5.3'),'books collection library')
    box = path('M2.2 11.05V6.8A3.5 3.5 0 0 1 5.7 3.3H10.8A3.5 3.5 0 0 1 14.3 6.8V11.05Z')
    post = rr(6.85,10.4,2.7,4.1)
    door_seam = stroke('M5.7 3.3A3.5 3.5 0 0 1 9.2 6.8V11.05')
    slot = stroke('M4.4 7.75H6.95')
    flag = stroke('M11.35 6.1V1.65H13.65')
    shape('mailbox',union(box,post),union(door_seam,slot,flag,stroke('M2.2 11.05H14.3')),'postal mailbox')
    overrides['mailbox'] = {'solid':union(subtract(union(box,post,stroke(box)),union(door_seam,slot)),
                                          subtract(flag,box))}
    handset=path('M3 2L5.5 4.5L4.2 6.5Q5.7 9.5 8.8 11L10.8 9.7L13.5 12.5Q12 15 9.5 13.8Q4 11.3 2 6.3Q.8 3.8 3 2Z')
    for suffix, geom in {
        'incoming':'M10 2V6H14M14 2L10 6',
        'outgoing':'M10 6L14 2M10 2H14V6',
        'missed':'M10 2L14 6M14 2L10 6',
    }.items(): shape('phone-'+suffix,transform(handset,0,.8,-1,1),stroke(geom),'telephone call '+suffix)
    shape('phone-off',handset,line((2,2),(14,14)),'telephone call disabled')
    shape('ribbon',union(circle(8,5.3,3.3),path('M5.8 7.5L4.5 14L8 12.2L11.5 14L10.2 7.5Z')),stroke(circle(8,5.3,1.3)),'award medal ribbon')
    glyph('rotate-ccw-key',stroke('M12.7 12.3A6.15 6.15 0 1 0 2.05 6.15M2.05 3.1V6.15H4.9'),compact('key',9.05,8.9,.85),'rotate restore key')
    glyph('rotate-cw-fading-clock',stroke('M3 6A5.5 5.5 0 0 1 13.2 5M10.5 4.5L13.3 5L13.5 2.2M13.5 8Q13.5 10 12 11.7M9.5 13.4L9.4 13.4M6.5 13.4L6.4 13.4M3.5 11.8L3.4 11.7M8 5.2V8.2L10.3 9.5'),None,'clock rotate history')
    stack('save-all', rr(1.7,1.7,9.5,9.5), path('M4.8 4.6H11.8L14.3 7.1V14.3H4.8Z'),
          stroke('M7 4.6V7.7H10.4V4.6M7.4 14.3V10.6H11.8V14.3'), 'save multiple files')
    # plus.magnifyingglass: the family lens, the mark centered inside it.
    search_lens, search_handle = circle(6.7,6.7,4.7), line((10.3,10.3),(14,14))
    for suffix, mark in (('check', check(6.7,6.8,.62)), ('x', cross(6.7,6.7,.66)),
                         ('code', stroke('M5.6 5.25L4.15 6.7L5.6 8.15M7.8 5.25L9.25 6.7L7.8 8.15'))):
        shape('search-'+suffix, search_lens, union(search_handle, mark), 'find search '+suffix)
    # slider.horizontal.3: capsule knobs interrupt three tracks.
    settings_tracks = []
    for y, knob in ((3.6, 4.3), (8, 8.6), (12.4, 2.9)):
        settings_tracks += [stroke(rr(knob, y-1.15, 3.4, 2.3, 1.15, exact=True)),
                            line((1.85, y), (knob, y)) if knob > 2.5 else po.Path(),
                            line((knob+3.4, y), (14.15, y))]
    glyph('settings-2', union(*settings_tracks), None, 'settings adjustments sliders')
    # square.and.arrow.up: an open tray with rounded corners, arrow through the gap.
    glyph('share',stroke('M5.6 6.1H4.9Q3.7 6.1 3.7 7.3V13.25Q3.7 14.45 4.9 14.45H11.1Q12.3 14.45 12.3 13.25V7.3Q12.3 6.1 11.1 6.1H10.4'),
          stroke('M8 9.9V1.7M5.65 4.05L8 1.7L10.35 4.05'),'share upload')
    glyph('share-2',union(stroke('M5 7L11 4M5 9L11 12'),stroke(circle(3.5,8,1.6)),stroke(circle(12.5,3.5,1.6)),stroke(circle(12.5,12.5,1.6))),None,'share network nodes')
    shredder = rr(1.7,6.4,12.6,4.4)
    sheet = path('M4.4 6.4V2H10.4L11.6 3.3V6.4Z')
    stack('shredder',sheet,shredder,stroke('M4.2 10.8V14.2M7 10.8V13.1M9.8 10.8V14.4M12 10.8V12.5'),'paper shredder destroy')
    overrides['shredder']['solid'] = union(subtract(api['stacked_solid'](sheet,shredder),stroke('M4.2 8.6H11.8')),
                                            stroke('M4.2 10.8V14.2M7 10.8V13.1M9.8 10.8V14.4M12 10.8V12.5'))
    shape('sticker',path('M3 2H12Q14 2 14 4V9L9 14H3Q2 14 2 13V3Q2 2 3 2Z'),stroke('M9 14V9H14'),'peel sticker label')
    shape('switch-camera',rr(1.5,4,13,9),union(stroke('M5 4L6 2.5H10L11 4M5.1 7.5Q5.85 5.75 8 5.75Q10.05 5.75 10.95 7.5M11 5.95V7.7H9.3M10.9 9.4Q10.15 11.1 8 11.1Q5.95 11.1 5.05 9.4M5 10.95V9.2H6.7')),'camera switch rotate')
    tag_front = path('M1.7 3.6H6.5L12.1 9.2L7.7 13.6L1.7 7.6Z')
    tag_back = path('M5.2 1.7H9.2L14.5 7L10.1 11.4L5.2 6.5Z')
    stack('tags', tag_back, tag_front, circle(4.3,6.1,.82), 'multiple labels tags')
    glyph('timer-reset',stroke('M3.5 6.82A5 5 0 1 1 3.15 10.2M2.95 4.45V7.1H5.6M8 9L10 6.5M6 1.55H10M8 1.55V4M12 4L13 3'),None,'timer reset')
    mask = path('M1.6 4.7Q4.1 4.3 6.3 5.5Q8 6.7 9.7 5.5Q11.9 4.3 14.4 4.7L13.8 8.2Q13.2 11.9 10.6 11.7Q9.5 11.7 8 9.8Q6.5 11.7 5.4 11.7Q2.8 11.9 2.2 8.2Z')
    eye = path('M3.4 6.9Q5.5 6.5 6.8 8.45Q4.6 9.25 3.4 6.9Z')
    shape('venetian-mask',mask,union(eye,api['mirror'](eye)),'theater masquerade mask')
    shape('vote',path('M2 9H14V14H2ZM5 3L10 1.5L12 6L7 7.5Z'),stroke('M5.45 11.15H10.55M7 4.5L8 5.5L9.5 3.5'),'ballot election voting')

    # Solid styles for overlapping foreground objects need explicit gaps;
    # otherwise the generic silhouette merges the mark into the background.


    # Cut the final rendered style before adding the slash. Cutting the body
    # first would outline the cut edges and produce two distracting diagonals.
    def disabled_styles(name, source):
        b,d,outline,_,_=host_drawing(source)
        if name == 'screen-share-off':
            d = stroke('M8 11V14M5 14H11M10.65 7V4.2M9.2 5.65L10.65 4.2L12.1 5.65')
        elif name == 'message-square-off':
            d = po.Path()
        elif name == 'image-off':
            # The mountain remains visible on either side of the channel.
            d = union(*(piece for piece in api['components'](d) if piece.area > 3))
        elif name == 'server-off':
            d = union(stroke('M2 6H14M2 10H14M9 4H11'),dots((5,8),(5,12),r=.7))
        elif name == 'timer-off':
            d = stroke('M6 1.55H10M8 1.55V3.9M12 4L13 3')
        outer=stroke(b) if outline else po.Path()
        boundary=subtract(outer,d) if outer else po.Path()
        duo=[(subtract(b,union(boundary,d)),.24),(union(boundary,d),1)] if outline else [(union(b,d),1)]
        mono=union(outer,d) if outline else union(b,d)
        if name == 'video-off':
            mono = union(outer,stroke(d))
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
        reviewed = name in ('alarm-clock-off','calendar-off','cctv-off','image-off','lightbulb-off',
                            'message-square-off','screen-share-off','server-off','timer-off','trash-off')
        clearance=line((2,2),(14,14),width=3.15 if reviewed else 2.7)
        slash=line((2,2),(14,14))
        def visible(layer):
            clipped = subtract(layer,clearance)
            return union(*(piece for piece in api['components'](clipped) if piece.area > (1.25 if reviewed else .55)))
        if name == 'trash-off':
            # Even the short end of a clipped rib belongs to the opaque layer.
            duo_layers = [(subtract(layer,clearance),alpha) for layer,alpha in duo]+[(slash,1)]
        else:
            duo_layers = [(visible(layer),alpha) for layer,alpha in duo]+[(slash,1)]
        overrides[name]={
            'duotone':duo_layers,
            'solid':union(visible(solid),slash),
            'stroke':union(visible(mono),slash),
        }
    for name, source in (
        ('alarm-clock-off','alarm-clock'),('bookmark-off','bookmark'),('calendar-off','calendar'),
        ('flag-off','flag'),('heart-off','heart'),
        ('image-off','image'),('lightbulb-off','lightbulb'),('map-pin-off','map-pin'),
        ('monitor-off','monitor'),('pin-off','pin'),('power-off','power'),('save-off','save'),
        ('server-off','server-rack'),('shield-off','shield'),
        ('star-off','star'),('timer-off','timer'),('trash-off','trash'),
        ('video-off','video-call'),('wrench-off','wrench'),('zap-off','zap'),
    ):
        disabled_styles(name,source)

    # A diagonal running opposite to the handset keeps this disabled state
    # recognizable; a parallel slash would disappear into its silhouette.
    phone_base=union(handset,stroke(handset))
    phone_slash=line((2,14),(14,2))
    phone_gap=line((2,14),(14,2),width=2.7)
    overrides['phone-off']={'duotone':[(subtract(handset,union(phone_gap,stroke(handset))),.24),(union(subtract(stroke(handset),phone_gap),phone_slash),1)],'solid':union(subtract(phone_base,phone_gap),phone_slash),'stroke':union(subtract(stroke(handset),phone_gap),phone_slash)}

    # Half-state symbols need an actual half-filled silhouette, not a seam
    # dividing two identical halves. Keep the right counter open in every style.
    for name in ('star-half', 'shield-half'):
        body = api['DRAWINGS'][name][0]
        outline = stroke(body)
        half = op(body, rr(0, 0, 8, 16, 0), po.PathOp.INTERSECTION)
        ink = union(outline, half)
        overrides[name] = {'duotone': [(subtract(body, ink), .24), (ink, 1)],
                           'solid': ink, 'stroke': ink}

    # Foreground seams in Solid are open gaps between objects. Reusing an
    # interior contour as a counter leaves an unstable hairline double border.
    # copy-check / -plus / -x: composed by draw.stacked() with the shared pair.
    for name, back, front, detail in (



        ('images', rr(1.5,1.5,9,9), rr(5,5,9.5,9.5), union(stroke('M5 12L8 9L10 11L12 8.5L14 11'),circle(8,7,.6))),

    ):
        overrides[name] = {'solid': api['stacked_solid'](back, front, detail)}

    # Reserve a corner after composing the host so no detail bleeds into the badge.
    def detach_badge(name, badge):
        body, details, _, _, _ = api['DRAWINGS'][name]
        host_detail = subtract(details,badge)
        outer = stroke(body)
        filled = union(body,outer)
        interior = subtract(filled,stroke(filled,1.8))
        structural, counters = [], []
        for component in api['components'](host_detail):
            exterior = subtract(component,filled)
            (structural if exterior.area > component.area*.12 else counters).append(component)
        solid = union(subtract(filled,op(union(*counters),interior,po.PathOp.INTERSECTION)),*structural)
        left,top,right,bottom = badge.bounds
        gap = circle((left+right)/2,(top+bottom)/2,max(right-left,bottom-top)/2+1.5)
        if 'cog' in name:
            # Reserve the hub as well as the valleys between the teeth.
            left, top, right, bottom = badge.bounds
            gap = circle((left+right)/2, (top+bottom)/2, (right-left)/2 + .95)
        ink = union(recess(body,gap),subtract(union(outer,host_detail),gap),badge)
        overrides[name] = {'duotone':[(subtract(body,union(gap,ink)),.24),(ink,1)],
                           'stroke':ink,'solid':union(subtract(solid,gap),badge)}

    for name, (source, base, detail, badge) in corner_badges.items():
        # Keep each subject's original silhouette, strokes and counters.
        outline = stroke(base)
        host = union(outline,detail)
        left,top,right,bottom = badge.bounds
        gap = union(badge,stroke(badge,2.1))
        if 'cog' in name or name.endswith(('-search-2','-search','-star','-shield','-lock','-key','-sync','-pen')):
            gap = circle((left+right)/2,(top+bottom)/2,max(right-left,bottom-top)/2+1.05)
        if source in ('user','user-round','tag'):
            gap = union(badge,stroke(badge,2.05))
        if name == 'folder-search-2':
            gap = union(circle(11.65,10.85,3.7),badge,stroke(badge,2.2))
        elif name == 'mail-clock':
            gap = circle(11.55,11.5,4.85)
        elif source == 'mail':
            # One open corner for the entire mail family, below the V flap.
            gap = circle(12.75,12.25,4.05)
        elif name == 'image-minus':
            gap = circle(12.45,11.35,3.65)
        elif source == 'building-complex':
            gap = circle(12.15,11.6,3.7)
        elif source in slot_radii:
            gap = circle(12,11.6,slot_radii[source])
        if source in ('archive','alarm-clock','user','user-round','tag','star','heart'):
            ink = union(subtract(host,gap),badge)
        else:
            # Keep the host counter closed where the edge turns behind a badge.
            corner = union(gap,stroke(gap,1.1))
            ink = union(recess(base,corner),subtract(host,corner),badge)
            gap = corner
        host_solid = union(base,outline)
        counters, structure = [], []
        for component in api['components'](detail):
            external = subtract(component,host_solid)
            (structure if external.area > .12*component.area else counters).append(component)
        clipped = op(union(*counters),subtract(host_solid,stroke(host_solid,1.8)),po.PathOp.INTERSECTION)
        solid = subtract(union(subtract(host_solid,clipped),*structure),gap)
        overrides[name] = {'stroke':ink,'duotone':[(subtract(base,union(gap,ink)),.24),(ink,1)],
                           'solid':union(solid,badge)}
