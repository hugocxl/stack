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
    menu = line((1.35, 5.45), (14.65, 5.45))
    framed('menubar', window, menu, 'desktop window menu bar top system commands')
    framed('menubar-dock', window, union(menu, line((4.6, 10.8), (11.4, 10.8))),
           'desktop window menu bar dock launcher applications')

    for name, seam, tags in (
        ('window-split-horizontal', line((1.35, 8), (14.65, 8)), 'rows upper lower horizontal'),
        ('window-split-vertical', line((8, 2.65), (8, 13.35)), 'columns left right vertical'),
    ):
        framed(name, window, seam, 'window split panes divider layout ' + tags)

    rear = rr(1.45, 2.1, 10.1, 8.7)
    front = rr(4.45, 5.2, 10.1, 8.7)
    title = line((4.45, 8.15), (14.55, 8.15))
    rear_rim, front_rim = stroke(rear), stroke(front)
    field = union(front, front_rim)
    behind = cut(union(rear, rear_rim), union(field, stroke(field, 2.1)))
    edges = union(cut(rear_rim, field), front_rim, title)
    shape('window-stack', union(rear, front), edges, 'desktop overlapping windows switch multitask')
    overrides['window-stack'] = {
        'duotone': [(cut(union(rear, front), edges), .24), (edges, 1)],
        'stroke': edges, 'solid': union(behind, cut(field, line((5.5, 8.15), (13.5, 8.15)))),
    }

    for name, x, y, w, h, tags in (
        ('widget-small', 3.9, 3.9, 8.2, 8.2, 'compact square'),
        ('widget-medium', 1.4, 3.9, 13.2, 8.2, 'wide landscape'),
        ('widget-large', 1.95, 1.95, 12.1, 12.1, 'expanded square'),
    ):
        tile = rr(x, y, w, h)
        if name == 'widget-small':
            heading = line((x + 2.45, y + h - 4.85), (x + w - 3.5, y + h - 4.85))
        else:
            heading = circle(x + 2.8, y + 2.8, .8)
        caption = line((x + 2.45, y + h - 2.45), (x + w - 2.45, y + h - 2.45))
        if name == 'widget-large':
            caption = union(caption, line((x + 2.45, y + h - 4.6), (x + w - 4.6, y + h - 4.6)))
        framed(name, tile, union(heading, caption), 'home screen dashboard widget tile ' + tags)

    # Lift the active pane across the bottom-right bezel of the original display.
    display = drawings['picture-in-picture'][0]
    inset = rr(8.2, 9.9, 7.05, 5.25)
    clearance = union(inset, stroke(inset, 2.2))
    rim = cut(stroke(display), clearance)
    screen = cut(union(display, stroke(display)), clearance)
    enter = lines('M4.35 4.65L7.65 7.65', 'M5.25 7.65H7.65V5.25')
    leave = lines('M7.65 7.65L4.35 4.65', 'M4.35 7.05V4.65H6.75')
    swap = lines('M5.65 4.95C7.8 3.35 10.65 3.8 11.15 6.7',
                 'M9.3 5.55L11.15 6.7L12.3 4.85',
                 'M5.55 12.05C3.65 11.05 3.7 8.95 5.2 7.3',
                 'M3.65 7.75L5.2 7.3L5.65 9.15')
    for name, arrow, tags in (
        ('pip-enter', enter, 'enter shrink minimize'),
        ('pip-exit', leave, 'exit restore expand'),
        ('pip-swap', swap, 'swap exchange switch'),
    ):
        edges = union(rim, arrow, inset)
        shape(name, display, union(arrow, inset), 'picture in picture floating video player ' + tags)
        overrides[name] = {
            'duotone': [(cut(screen, edges), .24), (edges, 1)],
            'stroke': edges, 'solid': union(cut(screen, arrow), inset),
        }

    api['CATEGORY'] = 'Interface controls'
    card, backs = drawings['rectangle-stack'][:2]
    rim = stroke(card)
    badge = circle(3.65, 12.3, 2.85)
    clearance = circle(3.65, 12.3, 3.95)
    stack_edges = cut(union(backs, rim), clearance)
    stack_surface = cut(cut(card, rim), clearance)
    stack_solid = cut(union(card, rim, backs), clearance)
    head = circle(3.65, 11.06, .78)
    shoulders = api['path']('M2.19 13.99C2.2 12.5 5.1 12.5 5.11 13.99Q3.65 14.95 2.19 13.99Z')
    for name, mark, tags in (
        ('rectangle-stack-user', union(head, shoulders), 'person user profile shared collection'),
        ('rectangle-stack-play', poly([(2.85, 10.84), (5.15, 12.3), (2.85, 13.76)]),
         'play video media playlist'),
    ):
        disc = cut(badge, mark)
        shape(name, card, union(backs, mark), 'cards layers deck stack ' + tags)
        overrides[name] = {
            'duotone': [(union(stack_surface, disc), .24), (union(stack_edges, mark), 1)],
            'solid': union(stack_solid, disc), 'stroke': union(stack_edges, disc),
        }

    api['CATEGORY'] = 'Technology and development'
    pointer = drawings['mouse-pointer-click'][0]
    rays = lines('M3.85 1.3V2.65', 'M1.25 3L2.05 3.95',
                 'M6 3.4L7.05 2.25', 'M7.95 4.98L9.5 4.65')
    shape('cursor-rays', pointer, rays, 'cursor pointer click highlight select rays')
    trails = lines('M4.55 2.6H10.55', 'M7.95 4.8H12.6', 'M11.5 7H14.65')
    shape('cursor-motion', pointer, trails, 'cursor pointer motion speed movement tracking')

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
    glyph('fn', stroke('M6.6 2.7H5.7Q3.6 2.7 3.6 5.05V13.25M1.8 6.4H5.95'),
          stroke('M8.4 13.25V6.4M8.4 9.1C8.4 5.6 13.9 5.25 13.9 9V13.25'),
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
    # Both broadcast sectors share the transmitter's center and opening angle.
    waves = lines('M4.1 2.8A6.5 6.5 0 0 0 4.1 13.2',
                  'M5.81 5.08A3.65 3.65 0 0 0 5.81 10.92')
    glyph('personal-hotspot', circle(8, 8, 1.3), union(waves, api['mirror'](waves)),
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
