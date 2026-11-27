"""Original interface controls on the family's 16-unit grid."""

NAMES = (
    'circle-list-filter',
    'rectangle-stack', 'rectangle-stack-plus', 'rectangle-stack-minus',
    'checklist', 'checklist-checked', 'checklist-unchecked',
    'sidebar-left', 'sidebar-right',
)


def register(api):
    shape, glyph = api['shape'], api['glyph']
    circle, rr, ring = api['circle'], api['rr'], api['ring']
    stroke, line, lines = api['stroke'], api['line'], api['lines']
    union, overrides = api['union'], api['STYLE_OVERRIDES']

    def subtract(field, cut):
        return api['op'](field, cut, api['po'].PathOp.DIFFERENCE)

    api['CATEGORY'] = 'Interface controls'
    shape('circle-list-filter', circle(),
          lines('M4.65 5.75H11.35', 'M5.8 8H10.2', 'M7 10.25H9'),
          'filter list narrow refine results descending')

    # SF rectangle.stack: a tall card under two receding edges; the .badge
    # variants keep the same stack, fitted with a disc over its lower left corner.
    card = rr(1.85, 5.7, 12.3, 8.85)
    backs = lines('M3.25 3.75H12.75', 'M4.65 1.8H11.35')
    shape('rectangle-stack', card, backs, 'cards layers deck stack collection')
    radius, gap = 3.25, api['BADGE_GAP']
    cx, cy = 1.85+.95, 14.55-1.2
    x0, y0, x1, y1 = cx-radius, 1.28, 14.67, cy+radius
    scale = min(1, 14.4/(x1-x0), 14.4/(y1-y0))
    def fit(p):
        return p.transform(scale, 0, 0, scale, 8-scale*(x0+x1)/2, 8-scale*(y0+y1)/2)
    fitted_card = fit(card)
    fitted_backs = lines(*(api['svg_path'](fit(api['path'](d))) for d in ('M3.25 3.75H12.75', 'M4.65 1.8H11.35')))
    centre = fit(api['path'](f'M{cx} {cy}h.001')).bounds[:2]
    # Shared with the user and play badges in sf_ext_windows.
    api['RECTANGLE_STACK_BADGED'] = (fitted_card, fitted_backs, centre, radius*scale)
    for name, kind, tags in (
        ('rectangle-stack-plus', 'plus', 'add insert new'),
        ('rectangle-stack-minus', 'minus', 'remove delete subtract'),
    ):
        shape(name, fitted_card, fitted_backs, 'cards layers deck stack collection ' + tags)
        api['badge'](name, kind, *centre, radius*scale)

    api['CATEGORY'] = 'Product tools'
    row_centers = (4.55, 11.45)
    row_lines = union(*(line((8.35, y), (14.5, y)) for y in row_centers))
    for name, checked_rows, tags in (
        ('checklist', (True, False), 'mixed progress'),
        ('checklist-checked', (True, True), 'complete done'),
        ('checklist-unchecked', (False, False), 'pending incomplete'),
    ):
        discs, marks, open_rings = [], [], []
        for y, checked in zip(row_centers, checked_rows):
            if checked:
                discs.append(circle(3.85, y, 2.85))
                marks.append(line((2.65, y), (3.65, y + 1.18), (4.67, y - .9)))
            else:
                open_rings.append(ring(3.85, y, 2.85))
        rows = union(row_lines, *open_rings)
        tags = 'checklist list tasks todo completion ' + tags
        if discs:
            field, ticks = union(*discs), union(*marks)
            checked_discs = subtract(field, ticks)
            glyph(name, rows, checked_discs, tags)
            api['DUOTONE_GLYPHS'][name] = 'Filled task discs behind the checkmarks.'
            overrides[name] = {
                'duotone': [(checked_discs, .24), (union(rows, ticks), 1)],
            }
        else:
            glyph(name, rows, None, tags)

    api['CATEGORY'] = 'Layout'
    # SF sidebar.left: window chrome (2.4 u outer radius), divider at a third
    # of the width, three short rows at the top of the sidebar.
    frame = rr(1.245, 2.85, 13.51, 10.3, 1.9, exact=True)
    sidebar = lines('M6.3 2.85V13.15', 'M3.35 5.3H4.6',
                    'M3.35 7.05H4.6', 'M3.35 8.8H4.6')
    shape('sidebar-left', frame, sidebar, 'layout window panel sidebar leading left navigation')
    shape('sidebar-right', frame, api['mirror'](sidebar),
          'layout window panel sidebar trailing right inspector')
