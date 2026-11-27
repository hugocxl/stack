"""Original window, pointer, keyboard and system symbols on the 16-unit grid."""

NAMES = (
    'menubar', 'menubar-dock', 'window-split-horizontal', 'window-split-vertical',
    'window-stack', 'widget-small', 'widget-medium', 'widget-large', 'pip-enter',
    'pip-exit', 'pip-swap', 'rectangle-stack-user', 'rectangle-stack-play',
    'cursor-rays', 'cursor-motion', 'keyboard-ellipsis', 'capslock', 'fn',
    'shift-key', 'escape', 'clear-key', 'power-sleep', 'zzz', 'power-toggle',
    'sos', 'cellular-bars', 'personal-hotspot', 'esim', 'airplay-video', 'cast-off',
)


def register(api):
    shape, glyph = api['shape'], api['glyph']
    rr, circle, poly = api['rr'], api['circle'], api['poly']
    line, lines, stroke = api['line'], api['lines'], api['stroke']
    union, drawings = api['union'], api['DRAWINGS']
    overrides = api['STYLE_OVERRIDES']

    def cut(field, detail):
        return api['op'](field, detail, api['po'].PathOp.DIFFERENCE)

    def framed(name, body, detail, tags):
        shape(name, body, detail, tags)
        rim = stroke(body)
        inside = api['op'](detail, cut(body, rim), api['po'].PathOp.INTERSECTION)
        overrides[name] = {'solid': cut(union(body, rim), inside)}

    api['CATEGORY'] = 'Layout'
    window = drawings['sidebar-left'][0]
    menu = line((1.245, 5.45), (14.755, 5.45))
    framed('menubar', window, menu, 'desktop window menu bar top system commands')
    # SF menubar.dock.rectangle: the dock is a filled capsule above the lower edge.
    framed('menubar-dock', window, union(menu, rr(4.55, 9.95, 6.9, 1.7, .85, exact=True)),
           'desktop window menu bar dock launcher applications')

    for name, seam, tags in (
        ('window-split-horizontal', line((1.245, 8), (14.755, 8)), 'rows upper lower horizontal'),
        ('window-split-vertical', line((8, 2.85), (8, 13.15)), 'columns left right vertical'),
    ):
        framed(name, window, seam, 'window split panes divider layout ' + tags)

    # SF macwindow.on.rectangle: a rear frame and a front window whose title
    # bar carries the three window controls; both use window-chrome corners.
    rear = rr(1.3, 2.05, 10.4, 8.2, 1.9, exact=True)
    front = rr(4.3, 5.2, 10.4, 8.6, 1.9, exact=True)
    controls = api['dots']((6.35, 7.25), (7.9, 7.25), (9.45, 7.25), r=.6)
    rear_rim, front_rim = stroke(rear), stroke(front)
    field = union(front, front_rim)
    clearance = union(field, stroke(field, 1.8, exact=True))
    behind = cut(union(rear, rear_rim), clearance)
    edges = union(cut(rear_rim, clearance), front_rim, controls)
    shape('window-stack', union(rear, front), edges, 'desktop overlapping windows switch multitask')
    overrides['window-stack'] = {
        'duotone': [(cut(union(cut(rear, clearance), front), edges), .24), (edges, 1)],
        'stroke': edges, 'solid': union(behind, cut(field, controls)),
    }

    # SF widget.small / .medium / .large: tiles with app-tile corners, a filled
    # rounded square at the top left and caption rows along the bottom.
    for name, x, y, w, h, rows, tags in (
        ('widget-small', 2.45, 2.45, 11.1, 11.1, 1, 'compact square'),
        ('widget-medium', 1.25, 3.0, 13.5, 10.0, 1, 'wide landscape'),
        ('widget-large', 1.25, 1.45, 13.5, 13.1, 3, 'expanded square'),
    ):
        tile = rr(x, y, w, h, 2.6, exact=True)
        icon = rr(x + 1.75, y + 1.75, 2.9, 2.9, .8, exact=True)
        caption = [line((x + 2.3, y + h - 2.35 - 1.75*i), (x + w - 2.3 - (2.2 if i == 2 else 0), y + h - 2.35 - 1.75*i))
                   for i in range(rows)]
        framed(name, tile, union(icon, *caption), 'home screen dashboard widget tile ' + tags)

    # SF pip.enter / .exit / .swap: a window with a filled inset that stands
    # out over its lower right corner behind a clear gap.
    display = rr(1.5, 2.75, 11.2, 8.9, 1.9, exact=True)
    inset = rr(8.15, 8.75, 6.85, 5.0, 1.3, exact=True)
    clearance = union(inset, stroke(inset, 1.8, exact=True))
    rim = cut(stroke(display), clearance)
    screen = cut(display, clearance)
    # Arrows end in filled heads, as in SF pip.enter.
    def headed(x0, y0, x1, y1, size=2.3):
        import math
        d = math.hypot(x1-x0, y1-y0); ux, uy = (x1-x0)/d, (y1-y0)/d
        bx, by = x1-ux*size, y1-uy*size
        return union(line((x0, y0), (bx+ux*.3, by+uy*.3)),
                     poly([(x1, y1), (bx-uy*size*.62, by+ux*size*.62), (bx+uy*size*.62, by-ux*size*.62)]))
    enter = headed(3.9, 5.1, 7.35, 8.4)
    leave = headed(7.35, 8.4, 3.9, 5.1)
    swap_mark = headed(13.15, 12.6, 10.05, 9.75, 2.0)
    for name, arrow, mark, tags in (
        ('pip-enter', enter, None, 'enter shrink minimize'),
        ('pip-exit', leave, None, 'exit restore expand'),
        ('pip-swap', enter, swap_mark, 'swap exchange switch'),
    ):
        tile = cut(inset, mark) if mark else inset
        edges = union(rim, arrow, tile)
        shape(name, display, union(arrow, tile), 'picture in picture floating video player ' + tags)
        overrides[name] = {
            'duotone': [(cut(screen, union(edges, rim)), .24), (edges, 1)],
            'stroke': edges, 'solid': union(cut(cut(union(display, stroke(display)), clearance), arrow), tile),
        }

    api['CATEGORY'] = 'Interface controls'
    card, backs, (bx, by), br = api['RECTANGLE_STACK_BADGED']
    k = br/3.25
    head = circle(bx, by-.85*k, 1.0*k)
    torso = api['op'](api['path']('M-2 2.6Q-2 .6 0 .6Q2 .6 2 2.6Z').transform(k, 0, 0, k, bx, by),
                      circle(bx, by, br-.62*k), api['po'].PathOp.INTERSECTION)
    for name, mark, tags in (
        ('rectangle-stack-user', union(head, torso), 'person user profile shared collection'),
        ('rectangle-stack-play', poly([(bx-.95*k, by-1.6*k), (bx+1.65*k, by), (bx-.95*k, by+1.6*k)]),
         'play video media playlist'),
    ):
        shape(name, card, backs, 'cards layers deck stack ' + tags)
        api['BADGES'][name] = (cut(circle(bx, by, br), mark), circle(bx, by, br+api['BADGE_GAP']))

    api['CATEGORY'] = 'Technology and development'
    pointer = drawings['mouse-pointer'][0]
    tip = (4.9, 2.1)
    # SF cursorarrow.rays: seven rays around the tip, the arrow in the eighth sector.
    centre = (6.6, 6.1)
    small = pointer.transform(.64, 0, 0, .64, centre[0]-.64*tip[0], centre[1]-.64*tip[1])
    import math
    rays = union(*(line((centre[0]+2.3*math.cos(math.radians(a)), centre[1]+2.3*math.sin(math.radians(a))),
                        (centre[0]+4.25*math.cos(math.radians(a)), centre[1]+4.25*math.sin(math.radians(a))))
                   for a in (0, 135, 180, 225, 270, 315)))
    shape('cursor-rays', small, rays, 'cursor pointer click highlight select rays')
    # SF cursorarrow.motionlines: the arrow trailing three motion lines.
    moving = pointer.transform(1, 0, 0, 1, -2.7, 0)
    trails = lines('M7.6 4.6H14.1', 'M9.15 6.4H13.6', 'M10.7 8.2H13.1')
    shape('cursor-motion', moving, trails, 'cursor pointer motion speed movement tracking')

    keyboard, keys = drawings['keyboard'][:2]
    badge = circle(12, 11.95, 3.3)
    badge_space = circle(12, 11.95, 4.4)
    dots = union(*(circle(x, 11.95, .49) for x in (10, 12, 14)))
    disc = cut(badge, dots)
    # Clip the legacy rim's fractional overhang at the family live area.
    rim = api['op'](stroke(keyboard), rr(.65, .65, 14.7, 14.7, 0), api['po'].PathOp.INTERSECTION)
    # Hide the whole key where the badge would leave a chip of its face.
    # Re-space the lower rows of the legacy drawing to keep one unit
    # between each row and the rim. The key contours retain their weight.
    exposed_keys = []
    for key in keys.contours:
        left, top, right, bottom = key.bounds
        if 8.8 < left < 10 and 7.8 < top < 9:
            continue
        shift = -.18 if top > 9 else -.35 if top > 7 else 0
        exposed_keys.append(api['transform'](key, dy=shift))
    exposed_keys = union(*exposed_keys)
    edges = cut(union(rim, exposed_keys), badge_space)
    surface = cut(cut(keyboard, union(rim, exposed_keys)), badge_space)
    glyph('keyboard-ellipsis', keyboard, keys, 'keyboard typing input more options shortcuts ellipsis')
    api['DUOTONE_GLYPHS']['keyboard-ellipsis'] = 'Keyboard housing and floating options badge.'
    overrides['keyboard-ellipsis'] = {
        'duotone': [(union(surface, disc), .24), (union(edges, dots), 1)],
        'solid': union(cut(cut(union(keyboard, rim), exposed_keys), badge_space), disc),
        'stroke': union(edges, disc),
    }

    def shift_arrow(top, base):
        return poly([(8, top), (14, top + 6), (10.6, top + 6), (10.6, base),
                     (5.4, base), (5.4, top + 6), (2, top + 6)])

    shape('shift-key', shift_arrow(2.25, 13.75), None, 'keyboard modifier uppercase shift arrow')
    latch = rr(5.4, 12.4, 5.2, 2.18)
    shape('capslock', union(shift_arrow(1.5, 10.25), latch), None,
          'keyboard modifier capital uppercase caps lock latch')
    # SF fn: text-sized, 10.4 x 9.5.
    fn_size = lambda d: stroke(api['transform'](api['path'](d), scale=.82, dy=.35))
    glyph('fn', fn_size('M6.6 2.7H5.7Q3.6 2.7 3.6 5.05V13.25M1.8 6.4H5.95'),
          fn_size('M8.4 13.25V6.4M8.4 9.1C8.4 5.6 13.9 5.25 13.9 9V13.25'),
          'function fn keyboard modifier shortcut')
    glyph('escape', stroke('M8.4 1.95A6.05 6.05 0 1 1 1.95 8.4'),
          lines('M8.05 8.05L2.45 2.45', 'M2.45 5.85V2.45H5.85'),
          'keyboard escape esc cancel dismiss shortcut')
    shape('clear-key', drawings['square'][0], lines('M5.7 5.7L10.3 10.3', 'M10.3 5.7L5.7 10.3'),
          'keyboard keypad clear erase reset')

    api['CATEGORY'] = 'Actions and status'
    crescent = api['path']('M6.9 1.8C3.45 2.5 1.65 5.58 2.1 8.85'
                           'C2.8 14.1 9.5 16.05 13.75 11.82'
                           'C10.45 12.53 7.47 11.15 6.1 8.45'
                           'C4.9 6.05 5.35 3.65 6.9 1.8Z')
    shape('power-sleep', crescent, None, 'power sleep standby suspend crescent moon')
    glyph('zzz', lines('M2 2.35H7.7L2 8.2H7.7', 'M9.85 6.4H14.25L9.85 11H14.25'),
          stroke('M4.7 10.7H7.7L4.7 14H7.7'), 'sleep sleeping snooze idle rest zzz')
    shape('power-toggle', circle(8, 8, 6.1), line((8, 4.55), (8, 11.45)),
          'power toggle on off switch system')
    letter_s = stroke('M4.65 5.35C3.55 3.8 1.45 4.55 1.45 6.15'
                      'C1.45 8.35 4.75 7.6 4.75 9.85C4.75 11.6 2.4 12.4 1.35 10.65')
    letter_o = stroke(rr(6.85, 4.5, 2.45, 7, 1.25))
    glyph('sos', union(letter_s, letter_o), api['transform'](letter_s, dx=10.03),
          'sos distress emergency rescue help signal')

    api['CATEGORY'] = 'Devices and connectivity'
    levels = [(2.75, 10.1), (6.25, 7.8), (9.75, 5.5), (13.25, 3.2)]
    bars = union(*(line((x, top), (x, 12.8)) for x, top in levels))
    glyph('cellular-bars', bars, None, 'mobile network reception cellular signal strength bars')
    overrides['cellular-bars'] = {
        'solid': union(*(rr(x - 1.2, top - .55, 2.4, 13.9 - top, 1.2) for x, top in levels)),
    }
    # SF personalhotspot: two interlinked loops, each passing over the other once.
    first = rr(1.35, 3.25, 8.3, 5.2, 2.6)
    second = rr(6.35, 6.95, 8.3, 5.2, 2.6)
    left, right = rr(0, 0, 8, 16, 0), rr(8, 0, 8, 16, 0)
    def part(p, half): return api['op'](p, half, api['po'].PathOp.INTERSECTION)
    band_a, band_b = stroke(first), stroke(second)
    over_a, over_b = stroke(first, 2.84, exact=True), stroke(second, 2.84, exact=True)
    links = union(cut(part(band_a, left), over_b), part(band_a, right),
                  part(band_b, left), cut(part(band_b, right), over_a))
    glyph('personal-hotspot', links, None,
          'tethering cellular internet share network broadcast personal hotspot')
    chip = rr(2.15, 1.65, 11.7, 12.7)
    contacts = union(*(line((x, y), (x, end)) for x in (5.4, 8, 10.6)
                       for y, end in ((1.65, 3.6), (14.35, 12.4))))
    sim = poly([(5.1, 5.75), (8.75, 5.75), (10.9, 7.9), (10.9, 10.25), (5.1, 10.25)])
    framed('esim', chip, union(contacts, sim), 'embedded sim digital cellular phone carrier chip')

    api['CATEGORY'] = 'Media'
    screen, receiver = drawings['airplay'][:2]
    bezel = stroke(screen)
    receiver_space = union(receiver, stroke(receiver, 2.1))
    play = poly([(6.85, 3.85), (9.65, 5.45), (6.85, 7.05)])
    edges = union(cut(bezel, receiver_space), play, receiver)
    shape('airplay-video', screen, union(receiver, play), 'airplay stream video wireless display television')
    overrides['airplay-video'] = {
        'duotone': [(cut(screen, union(edges, receiver_space)), .24), (edges, 1)],
        'solid': union(cut(union(screen, bezel), union(receiver_space, play)), receiver),
        'stroke': edges,
    }
    screen, waves = drawings['cast'][:2]
    slash = line((2, 2), (14, 14))
    slash_space = line((2, 2), (14, 14), width=3.2)
    # The slash covers the screen's short upper-left return at 16 px.
    cancelled = union(cut(union(screen, waves), union(slash_space, rr(0, 0, 2.65, 5, 0))), slash)
    glyph('cast-off', screen, waves, 'cast disconnect disabled wireless display screen mirroring off')
    overrides['cast-off'] = {
        'duotone': [(cancelled, 1)], 'solid': cancelled, 'stroke': cancelled,
    }
