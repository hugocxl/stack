"""Original rounded home controls inspired by SF Symbols' semantic coverage.

Physical housings carry the quiet secondary surface; controls and open
structures stay legible in one tint. No reference outlines are imported.
"""

NAMES = (
    'oven', 'stove', 'dishwasher', 'dryer', 'thermostat', 'ceiling-fan',
    'garage', 'window-open', 'window-closed', 'curtains', 'doorbell',
    'intercom', 'smart-lock', 'light-switch', 'power-outlet',
)


def register(api):
    shape, glyph = api['shape'], api['glyph']
    path, rr, circle = api['path'], api['rr'], api['circle']
    stroke, line, union = api['stroke'], api['line'], api['union']
    api['CATEGORY'] = 'Home and food'
    empty = path('')

    def s(name, body, detail, tags):
        shape(name, body, detail, tags)

    def g(name, *pieces, tags):
        glyph(name, union(*pieces), empty, tags)

    def st(data, width=1.1):
        return stroke(data, width)

    appliance = rr(2.5, 1.7, 11, 12.6, 1.6)
    panel = line((2.8, 5.1), (13.2, 5.1), width=1.1)
    controls = union(circle(5, 3.4, .55), circle(8, 3.4, .55),
                     circle(11, 3.4, .55))

    s('oven', appliance,
      union(panel, controls, st(rr(4.6, 7.2, 6.8, 4.7, .8))),
      'kitchen baking cooking appliance oven')

    s('stove', rr(2, 2, 12, 12, 1.7),
      union(*(st(circle(x, y, 1.35), 1.1)
              for x, y in ((5.1, 5.1), (10.9, 5.1),
                           (5.1, 10.9), (10.9, 10.9)))),
      'cooktop hob burners kitchen cooking appliance')

    s('dishwasher', appliance,
      union(panel, circle(5.1, 3.4, .55), line((9.2, 3.4), (11.2, 3.4)),
            line((5.7, 7.8), (10.3, 7.8))),
      'dishes cleaning plates kitchen appliance')

    # The dial, drum and curved lower lip stay legible on a narrow housing.
    dryer_front = rr(2.65, 1.35, 10.7, 13.3)
    drum = circle(8,10.1,2.5)
    s('dryer', dryer_front,
      union(line((2.7,5.5),(13.3,5.5)),circle(5.1,3.45,.55),
            line((9.4,3.45),(11,3.45)),st(drum),
            st('M5.65 10.95Q8 9.65 10.35 10.95')),
      'laundry tumble dry clothes heat appliance')
    s('thermostat', circle(8, 8, 6),
      union(st('M5.7 5.4V9A1.65 1.65 0 1 0 7.8 9V5.4A1.05 1.05 0 0 0 5.7 5.4Z'),
            line((10, 5.8), (11, 5.8), width=1.1),
            line((10, 8.25), (11.45, 8.25), width=1.1)),
      'temperature climate heating cooling room control')

    # Two opposing pitched blades sit behind the suspended motor.
    motor = rr(6.15, 6.65, 3.7, 3.5)
    blade = path('M6.45 7.45L2.15 5.85Q1.4 5.55 1.4 6.4V7.6'
                 'Q1.4 8.1 2 8.35L6.45 9.65Z')
    s('ceiling-fan', union(motor, blade, api['mirror'](blade)),
      union(st(motor), st('M5.7 2.4H10.3M8 2.4V6.65M8 10.15V13.3')),
      'overhead ventilation cooling fan home')
    s('garage', path('M2 6L8 1.8L14 6V14H2Z'),
      st('M4.4 14V6.8H11.6V14M4.4 9.3H11.6M4.4 11.6H11.6'),
      'garage door parking storage car home')

    frame = rr(2.5, 2, 11, 12, .8)
    s('window-closed', frame, st('M8 2V14M2.5 8H13.5'),
      'window panes glass closed architecture')
    # Open leaves are outlined structures, with no faded arbitrary half.
    g('window-open', st('M5.5 3H10.5M5.5 13H10.5M2 1.8L5.5 3V13L2 14.2Z'
                       'M14 1.8L10.5 3V13L14 14.2ZM2 8H5.5M10.5 8H14', 1.25),
      tags='window panes casement ventilation open architecture')

    curtain = path('M1.9 3.1H6.8Q6.65 6.9 4.5 8.8L6 13.7H1.9Z')
    curtains = union(curtain, api['mirror'](curtain))
    rail = line((1.5, 3.1), (14.5, 3.1))
    ties = st('M1.9 8.8H4.5M11.5 8.8H14.1')
    s('curtains', curtains, union(rail, ties), 'drapes curtain shade window home')
    api['STYLE_OVERRIDES']['curtains'] = {'solid': api['op'](
        union(curtains, st(curtains), rail), st('M1 8.8H5.25M10.75 8.8H15'),
        api['po'].PathOp.DIFFERENCE)}
    api['STYLE_OVERRIDES']['window-closed'] = {'solid': union(
        st(frame, 1.75), st('M8 2V14M2.5 8H13.5', 1.65))}

    s('doorbell', rr(4.2, 1.7, 7.6, 12.6, 2.6),
      union(st(circle(8, 10.5, 1.65)), circle(8, 5, .75)),
      'entry door bell visitor button camera')

    s('intercom', rr(3, 1.7, 10, 12.6, 1.7),
      union(st('M5.4 4.1H10.6M5.4 6.4H10.6'),
            st(circle(8, 10.5, 1.6))),
      'entry speaker communication door buzzer')

    s('smart-lock', rr(4, 1.7, 8, 12.6, 2),
      union(*(circle(x, y, .55) for x, y in
              ((6.5, 4), (9.5, 4), (6.5, 6.7), (9.5, 6.7))),
            st('M6.6 9.7V10.9H10', 1.35)),
      'keypad access lock door code security')

    s('light-switch', rr(3, 1.7, 10, 12.6, 1.5),
      union(st(rr(5.5, 4, 5, 8, .7)),
            line((5.5, 7), (10.5, 7), width=1.1)),
      'wall switch rocker light power control')

    s('power-outlet', rr(2.5, 2, 11, 12, 2),
      union(st('M5.6 5.3V7.6M10.4 5.3V7.6'),
            st('M6.5 11V10.6A1.5 1.5 0 0 1 9.5 10.6V11')),
      'socket electrical electricity wall outlet receptacle')
