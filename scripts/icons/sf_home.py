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
      union(panel, controls, line((5.5, 7.65), (10.5, 7.65), width=1.35)),
      'dishes cleaning plates kitchen appliance')

    # A shallow lower arc follows the curvature of the drum window.
    s('dryer', appliance,
      union(panel, controls, st(circle(8, 9.7, 3.1), 1.15),
            st('M6.65 10.2Q8 11.6 9.35 10.2', 1.05)),
      'laundry tumble dry clothes heat appliance')

    s('thermostat', circle(8, 8, 6),
      union(st('M5.7 5.4V9A1.65 1.65 0 1 0 7.8 9V5.4A1.05 1.05 0 0 0 5.7 5.4Z'),
            line((10, 5.8), (11, 5.8), width=1.1),
            line((10, 8.25), (11.45, 8.25), width=1.1)),
      'temperature climate heating cooling room control')

    # Side view of the suspended motor. Opposing pitched paddles attach
    # at the motor's waist beneath the ceiling plate and downrod.
    motor = rr(6.2, 6.55, 3.6, 3.6, 1.5)
    left_blade = path('M6.5 7.5L2.1 5.95Q1.4 5.75 1.4 6.55V7.45'
                      'Q1.4 8.05 2.05 8.2L6.5 8.9Z')
    blades = union(left_blade, api['mirror'](left_blade))
    s('ceiling-fan', union(motor, blades),
      union(st('M5.9 2.4H10.1M8 2.4V6.55', 1.25),
            st('M8 10.15V12.85', 1.05), circle(8, 13.2, .7)),
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

    curtains = path('M2.3 3H6Q6 7.5 3.5 9L5 14H2.3Z'
                    'M13.7 3H10Q10 7.5 12.5 9L11 14H13.7Z')
    s('curtains', curtains,
      union(line((1.5, 2.2), (14.5, 2.2)), st('M2.3 9H3.5M12.5 9H13.7')),
      'drapes curtain shade window home')

    curtain_field = union(curtains, st(curtains, 1.25), line((1.5, 2.2), (14.5, 2.2)))
    api['STYLE_OVERRIDES']['curtains'] = {'solid': api['op'](
        curtain_field, st('M1 9H5.1M10.9 9H15', 1.1), api['po'].PathOp.DIFFERENCE)}
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
