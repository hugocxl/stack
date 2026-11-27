"""Original home appliances and fixtures drawn to SF Symbols conventions.

Physical housings carry the quiet secondary surface; controls, windows and
open structures are opaque ink. No reference outlines are imported.
"""

NAMES = (
    'oven', 'stove', 'dishwasher', 'dryer', 'thermostat', 'ceiling-fan',
    'garage', 'window-open', 'window-closed', 'curtains', 'doorbell',
    'intercom', 'smart-lock', 'light-switch', 'power-outlet',
)


def register(api):
    shape, glyph = api['shape'], api['glyph']
    path, rr, circle = api['path'], api['rr'], api['circle']
    stroke, line, lines, union = api['stroke'], api['line'], api['lines'], api['union']
    ring, styles = api['ring'], api['STYLE_OVERRIDES']
    op, po = api['op'], api['po']
    api['CATEGORY'] = 'Home and food'

    def cut(a, b):
        return op(a, b, po.PathOp.DIFFERENCE)

    def inside(a, b):
        return op(a, b, po.PathOp.INTERSECTION)

    def ellipse(cx, cy, rx, ry):
        return circle(0, 0, 1).transform(rx, 0, 0, ry, cx, cy)

    def gap(p, width=1.8):
        return union(p, stroke(p, width, exact=True))

    def knobs(y, *xs, r=.55):
        return union(*(circle(x, y, r) for x in xs))

    # SF oven: a wide wall oven, a control row and a framed door window.
    oven = rr(1.85, 2.95, 12.3, 10.1)
    shape('oven', oven,
          union(knobs(4.75, 4.0, 5.65, 7.3), line((10.15, 4.75), (12.05, 4.75)),
                line((1.85, 6.6), (14.15, 6.6)), stroke(rr(4.05, 8.45, 7.9, 2.65, .55, exact=True))),
          'kitchen baking cooking appliance oven')

    # SF stove: a freestanding range with four knobs, oven door and feet.
    range_body = rr(2.25, 1.75, 11.5, 11.0)
    shape('stove', range_body,
          union(knobs(3.7, 4.6, 6.85, 9.15, 11.4), line((2.25, 5.65), (13.75, 5.65)),
                stroke(rr(4.4, 7.65, 7.2, 3.0, .55, exact=True)),
                lines('M3.85 12.75V14.15', 'M12.15 12.75V14.15')),
          'cooktop hob burners kitchen cooking appliance')

    # SF dishwasher and dryer share a narrow front-loading cabinet whose
    # lower corner holds the identifying mark behind a clearance gap.
    cabinet = rr(1.4, 1.45, 10.4, 12.3)
    panel = union(line((1.4, 4.85), (11.8, 4.85)), knobs(3.15, 3.55, 5.25))
    plate = union(ring(10.4, 11.3, 3.05), ring(10.4, 11.3, 1.6))
    rear_plate = cut(ring(12.25, 11.3, 3.05), gap(api['circle'](10.4, 11.3, 3.05)))
    api['corner_mark']('dishwasher', cabinet, panel, union(plate, rear_plate),
                       gap(union(circle(10.4, 11.3, 3.05), circle(12.25, 11.3, 3.05))), return_edge=True)
    heat = union(*(stroke(f'M{x} 9.25Q{x+.75} 10.05 {x} 10.85T{x} 12.45T{x} 14.05')
                   for x in (10.25, 12.25, 14.25)))
    drum = stroke(rr(3.0, 7.0, 4.4, 4.6, 1.2, exact=True))
    api['corner_mark']('dryer', cabinet, union(panel, drum), heat, gap(heat), return_edge=True)
    for name, tags in (('dishwasher', 'dishes cleaning plates kitchen appliance'),
                       ('dryer', 'laundry tumble dry clothes heat appliance')):
        api['DRAWINGS'][name] = api['DRAWINGS'][name][:4] + (tags,)

    shape('thermostat', circle(8, 8, 6),
          union(stroke('M5.7 5.4V9A1.65 1.65 0 1 0 7.8 9V5.4A1.05 1.05 0 0 0 5.7 5.4Z'),
                line((10, 5.8), (11, 5.8)), line((10, 8.25), (11.45, 8.25))),
          'temperature climate heating cooling room control')

    # SF fan.ceiling: canopy, downrod, a motor housing and four blades in
    # perspective, all clear of the housing.
    housing = ellipse(8, 8.9, 2.85, 1.6)

    def blade(x, y, width):
        return stroke(f'M{8 + (x - 8)*.3} {8.9 + (y - 8.9)*.3}L{x} {y}', width, exact=True)

    blades = cut(union(blade(1.95, 12.35, 2.2), blade(14.05, 12.35, 2.2),
                       blade(2.6, 6.35, 1.8), blade(13.4, 6.35, 1.8)), gap(housing))
    housing = ellipse(8, 8.9, 2.85, 1.6)
    blades = cut(blades, gap(housing))
    canopy = rr(5.7, 1.15, 4.6, 1.5, .75)
    shape('ceiling-fan', union(housing, blades, canopy), line((8, 2.65), (8, 7.3)),
          'overhead ventilation cooling fan home')

    # SF door.garage.closed: an open-bottomed frame around a sectional door
    # with a row of solid windows and a handle.
    frame = stroke('M1.55 14.45V3.35Q1.55 1.95 2.95 1.95H13.05Q14.45 1.95 14.45 3.35V14.45')
    door = rr(3.75, 4.15, 8.5, 10.3, .6, exact=True)
    windows = union(*(rr(x, 5.45, 1.8, 1.6, .35, exact=True) for x in (4.95, 7.1, 9.25)))
    door_detail = union(windows, lines('M3.75 8.35H12.25', 'M3.75 11.15H12.25'))
    shape('garage', door, union(frame, door_detail), 'garage door parking storage car home')

    # SF windows: a sash frame with a broad sill. Closed shows the cross
    # mullion; open swings both casements out of the frame.
    sash = rr(2.6, 1.6, 10.8, 11.3)
    sill = line((1.35, 13.95), (14.65, 13.95))
    shape('window-closed', sash, union(sill, lines('M8 1.6V12.9', 'M2.6 7.25H13.4')),
          'window panes glass closed architecture')
    leaves = stroke('M5.05 3.15L2.05 1.95V12.4L5.05 11.25ZM10.95 3.15L13.95 1.95V12.4L10.95 11.25Z')
    opening = stroke('M5.05 3.15H10.95M5.05 11.25H10.95')
    glyph('window-open', union(leaves, opening, sill), None,
          'window panes casement ventilation open architecture')

    # SF curtains.closed: a rod with finials and two hanging panels.
    rod = union(line((1.85, 2.15), (14.15, 2.15)), circle(1.35, 2.15, .95), circle(14.65, 2.15, .95))
    panels = union(rr(2.35, 3.65, 5.25, 10.75, .8, exact=True), rr(8.4, 3.65, 5.25, 10.75, .8, exact=True))
    shape('curtains', panels, rod, 'drapes curtain shade window home')

    # Entry hardware shares SF's narrow, softly cornered wall plate.
    plate = rr(3.95, 1.25, 8.1, 13.5, 2.4, exact=True)
    shape('doorbell', rr(4.25, 1.25, 7.5, 13.5, 3.0, exact=True),
          union(ring(8, 10.25, 2.05), circle(8, 4.75, .8)),
          'entry door bell visitor button camera')
    shape('intercom', plate,
          union(lines('M6.0 4.0H10.0', 'M6.0 6.1H10.0'), ring(8, 10.25, 1.85)),
          'entry speaker communication door buzzer')
    shape('smart-lock', plate,
          union(*(circle(x, y, .55) for x in (6.35, 8, 9.65) for y in (3.85, 5.65)),
                ring(8, 9.55, 1.3), line((8, 10.2), (8, 12.05))),
          'keypad access lock door code security')
    # SF lightswitch.on: a plate with the toggle up, drawn as a solid paddle.
    switch_plate = rr(3.85, 1.0, 8.3, 14.0, 2.2, exact=True)
    toggle = rr(5.45, 3.0, 5.1, 3.9, .7, exact=True)
    shape('light-switch', switch_plate, toggle,
          'wall switch rocker light power control')
    # SF poweroutlet.type.b: two solid blade slots over a round ground pin.
    outlet = rr(2.35, 2.45, 11.3, 11.1, 2.3, exact=True)
    shape('power-outlet', outlet,
          union(rr(5.35, 4.95, 1.15, 3.1, .45, exact=True), rr(9.5, 4.95, 1.15, 3.1, .45, exact=True),
                path('M7.05 11.45V10.45A.95 .95 0 0 1 8.95 10.45V11.45Z')),
          'socket electrical electricity wall outlet receptacle')
