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

    card = rr(2, 6.1, 12, 7.1)
    rim = stroke(card)
    backs = lines('M3.25 3.95H12.75', 'M4.65 1.8H11.35')
    shape('rectangle-stack', card, backs, 'cards layers deck stack collection')

    # Occlude the very same card and rear edges in all three styles.
    badge = circle(3.65, 12.3, 2.85)
    clearance = circle(3.65, 12.3, 3.95)
    edges = subtract(union(backs, rim), clearance)
    surface = subtract(subtract(card, rim), clearance)
    stack = subtract(union(card, rim, backs), clearance)
    minus = line((2.4, 12.3), (4.9, 12.3))
    plus = union(minus, line((3.65, 11.05), (3.65, 13.55)))
    for name, mark, tags in (
        ('rectangle-stack-plus', plus, 'add insert new'),
        ('rectangle-stack-minus', minus, 'remove delete subtract'),
    ):
        shape(name, card, union(backs, mark), 'cards layers deck stack collection ' + tags)
        disc = subtract(badge, mark)
        overrides[name] = {
            'duotone': [(union(surface, disc), .24), (union(edges, mark), 1)],
            'solid': union(stack, disc),
            'stroke': union(edges, disc),
        }

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
    frame = rr(1.35, 2.65, 13.3, 10.7)
    sidebar = lines('M6.85 2.65V13.35', 'M3.45 5.5H4.75',
                    'M3.45 8H4.75', 'M3.45 10.5H4.75')
    shape('sidebar-left', frame, sidebar, 'layout window panel sidebar leading left navigation')
    shape('sidebar-right', frame, api['mirror'](sidebar),
          'layout window panel sidebar trailing right inspector')
