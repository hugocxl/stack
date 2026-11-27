"""Original formatting, math, playback and face icons on the family grid."""

NAMES = (
    'text-size-larger', 'text-size-smaller', 'textformat-abc', 'textformat-123',
    'indent-increase', 'indent-decrease', 'quote-level-increase', 'quote-level-decrease',
    'text-box', 'placeholder-text', 'text-shadow',
    'greater-than', 'less-than', 'greater-than-equal', 'less-than-equal',
    'multiply', 'square-root', 'sum',
    'play-pause', 'go-backward-10', 'go-backward-15', 'go-backward-30',
    'go-forward-10', 'go-forward-15', 'go-forward-30', 'record',
    'frame-backward', 'frame-forward', 'timelapse', 'slow-motion',
    'face-laugh',
)


def register(api):
    glyph, shape = api['glyph'], api['shape']
    stroke, lines, line = api['stroke'], api['lines'], api['line']
    rr, union, mirror = api['rr'], api['union'], api['mirror']
    drawings = api['DRAWINGS']

    def linear(name, mark, tags):
        glyph(name, mark, None, tags)

    api['CATEGORY'] = 'Typography and text'
    # Centerlines from full/design.py: place them before applying the family stroke.
    def character(centerline, x, y, scale):
        skeleton = api['path'](centerline)
        return stroke(api['transform'](skeleton, scale=scale, dx=x - 8, dy=y - 8))

    capital_a = 'M3 13L7.3 3Q8 1.4 8.7 3L13 13M5 9H11'
    size_letter = character(capital_a, 5.3, 8.25, .78)
    for name, edge, tip, tags in (
        ('text-size-larger', 8.95, 7.05, 'larger enlarge increase'),
        ('text-size-smaller', 7.05, 8.95, 'smaller shrink decrease'),
    ):
        glyph(name, size_letter, line((10.4, edge), (12.5, tip), (14.6, edge)),
              'font type size capital ' + tags)

    lower_b = 'M4 2V13M4 9.2C4 4.1 12.5 4.1 12.5 9.2S4 14.3 4 9.2Z'
    open_c = 'M12.5 4.5C10 1 3 2 3 8C3 14 10 15 12.5 11.5'
    linear('textformat-abc', union(character(capital_a, 3.03, 8.25, .36),
                                   character(lower_b, 8.42, 8.25, .36),
                                   character(open_c, 13.55, 8.73, .275)),
           'text format alphabet letters abc spelling mixed case')

    one = 'M5 5L8 2.5V13.5M5 13.5H11'
    two = 'M3.5 5Q3.5 2.5 8 2.5Q12.5 2.5 12.5 5Q12.5 7 8 9L3.5 13.5H12.5'
    three = 'M4 3H9Q14 3 11 7L8 8Q14 8 12 12Q10 15 4 13'
    linear('textformat-123', union(character(one, 2.44, 8, .392),
                                   character(two, 7.53, 8, .392),
                                   character(three, 12.99, 8, .392)),
           'text format digits numerals numbers 123')

    # SF increase.indent / decrease.indent: four ragged rows beside a small
    # filled triangle; SF increase.quotelevel: bars beside the same triangle.
    poly = api['poly']
    def pointer(x, y, direction):
        return poly([(x, y-1.95), (x+2.8*direction, y), (x, y+1.95)])
    rows = [3.75, 6.5, 9.25, 12.0]
    for name, x0, x1, tri, tags in (
        ('indent-increase', 6.0, 14.4, pointer(1.55, 7.85, 1), 'indent increase paragraph right nest'),
        ('indent-decrease', 1.6, 10.0, pointer(14.55, 7.85, -1), 'indent decrease paragraph left outdent'),
    ):
        text = union(*(line((x0, y), (x1 if i < 3 else x0+(x1-x0)*.55, y)) for i, y in enumerate(rows)))
        glyph(name, text, tri, tags)

    def quote_level(name, rails, tri, tags):
        linear(name, union(*(line((x, 2.4), (x, 13.6)) for x in rails), tri),
               'blockquote citation quotation nesting level ' + tags)

    quote_level('quote-level-increase', (2.3, 5.4, 8.5),
                pointer(11.25, 8, 1), 'increase deeper')
    quote_level('quote-level-decrease', (6.25,),
                pointer(11.85, 8, -1), 'decrease shallower')

    # SF character.textbox: a frame with a handle in each side and a letter.
    box = rr(1.95, 2.75, 12.1, 10.5)
    letter = lines('M5.45 11.0L8 4.95L10.55 11.0', 'M6.3 9.0H9.7')
    handles = union(api['circle'](1.95, 8, .85), api['circle'](14.05, 8, .85))
    sockets = union(api['circle'](1.95, 8, 1.85), api['circle'](14.05, 8, 1.85))
    shape('text-box', box, union(letter, handles), 'text box field frame type insert editable')
    cutout = lambda p: api['op'](p, sockets, api['po'].PathOp.DIFFERENCE)
    frame_ink = union(cutout(stroke(box)), letter, handles)
    api['STYLE_OVERRIDES']['text-box'] = {
        'duotone': [(cutout(api['op'](box, union(stroke(box), letter), api['po'].PathOp.DIFFERENCE)), .24), (frame_ink, 1)],
        'stroke': frame_ink,
        'solid': union(cutout(api['op'](union(box, stroke(box)), letter, api['po'].PathOp.DIFFERENCE)), handles)}
    # Greeked lines stand in for a heading and two lines of body copy.
    linear('placeholder-text', union(rr(1.9, 3.05, 8, 2.45, 1.25),
                                     lines('M2.45 8.65H13.55', 'M2.45 12H10.8')),
           'placeholder text sample skeleton content lorem ipsum')
    # Only the exposed edges of the offset letter are visible.
    linear('text-shadow', lines('M2.1 2.95H11.95M7.025 2.95V10.95',
                                'M13.9 5.45H9.65V13.05H7.4'),
           'text font shadow offset typography effect')

    api['CATEGORY'] = 'Math and symbols'
    for right, left, mark, tags in (
        # SF greaterthan (8.8 x 8.5) and greaterthanorequalto (7.8 x 10.7): text-sized.
        ('greater-than', 'less-than', stroke('M4.1 4.3L11.9 8L4.1 11.7'), ''),
        ('greater-than-equal', 'less-than-equal',
         lines('M4.6 2.85L11.4 6.05L4.6 9.25', 'M4.6 12.6H11.4'), ' or equal'),
    ):
        linear(right, mark, 'math comparison inequality greater than' + tags)
        linear(left, mirror(mark), 'math comparison inequality less than' + tags)
    linear('multiply', lines('M4.25 4.25L11.75 11.75', 'M11.75 4.25L4.25 11.75'),
           'math arithmetic multiply product times cross')
    linear('square-root', stroke('M1.65 8.25H3.6L5.95 12.95L8.75 3.05H14.35'),
           'math arithmetic square root radical algebra')
    linear('sum', stroke('M11.25 2.75H4.75L8.75 8L4.75 13.25H11.25'),
           'math sum summation sigma series total')

    api['CATEGORY'] = 'Media'
    circle, poly = api['circle'], api['poly']
    overrides = api['STYLE_OVERRIDES']

    def transport(name, triangle, bars, tags):
        glyph(name, stroke(triangle), bars, tags)
        overrides[name] = {'solid': union(triangle, stroke(triangle), bars)}

    transport('play-pause', poly([(1.85, 3.2), (8.45, 8), (1.85, 12.8)]),
              lines('M10.75 3.2V12.8', 'M14.15 3.2V12.8'),
              'media playback play pause resume toggle')
    # Reflect only the arrow. Numerals remain upright in both directions.
    # SF goforward.*: the arc ends in a filled triangular head.
    forward = union(stroke('M12.1 3.9C13.6 5.05 14.35 6.75 14.35 8.6'
                           'C14.35 12.1 11.5 14.65 8 14.65S1.65 12.1 1.65 8.6'
                           'C1.65 5.1 4.5 2.65 8 2.65H8.4'),
                    poly([(7.85, .9), (10.45, 2.65), (7.85, 4.4)]))
    one = stroke('M4.9 7.75L6.35 6.65V11.35')
    zero = stroke(rr(9, 6.65, 2.65, 4.7, 1.325))
    five = stroke('M11.3 6.65H8.95L8.7 8.7C10.45 8.1 11.8 8.75 11.55 10.2'
                  'C11.35 11.45 9.8 11.8 8.55 11.05')
    three = stroke('M4.75 6.95C6.85 5.75 7.4 8.55 5.35 8.95'
                   'C7.65 9.05 7.2 12.15 4.8 11.05')
    for direction, arrow, action in (('backward', mirror(forward), 'rewind replay'),
                                     ('forward', forward, 'advance skip')):
        for seconds, digits in ((10, union(one, zero)), (15, union(one, five)),
                                (30, union(three, zero))):
            glyph(f'go-{direction}-{seconds}', arrow, digits,
                  f'media playback seek {direction} {action} {seconds} seconds')

    linear('record', union(api['ring'](8, 8, 6.55), circle(8, 8, 2.85)),
           'media capture record recording start audio video')
    blade = poly([(5.7, 3.2), (13.65, 8), (5.7, 12.8)])
    bar = line((2.4, 3.2), (2.4, 12.8))
    transport('frame-forward', blade, bar, 'media advance step next single video frame forward')
    transport('frame-backward', mirror(blade), mirror(bar),
              'media reverse step previous single video frame backward')

    rotate = api['transform']
    for name, count, tags in (
        ('timelapse', 16, 'time lapse camera capture interval fast motion'),
        ('slow-motion', 10, 'slow motion camera playback speed high framerate'),
    ):
        ticks = []
        for i in range(count):
            inner = 3.95 if name == 'slow-motion' or i % 2 == 0 else 2.35
            ticks.append(rotate(line((8, 1.65), (8, inner)), angle=i * 360 / count))
        linear(name, union(*ticks), tags)

    api['CATEGORY'] = 'People and accessibility'
    face = drawings['smile'][0]
    eyes = stroke('M4.45 6.75Q5.65 4.55 6.85 6.75M9.15 6.75Q10.35 4.55 11.55 6.75')
    mouth = api['path']('M4.8 8.95H11.2C10.9 10.65 9.55 11.75 8 11.75'
                        'S5.1 10.65 4.8 8.95Z')
    shape('face-laugh', face, union(eyes, stroke(mouth)),
          'face laugh laughter laughing joy happy emoji expression')
