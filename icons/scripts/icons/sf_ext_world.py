"""Original weather, transport, gaming, geometry, editing and currency symbols."""

NAMES = (
    'moon-new', 'moon-waxing-crescent', 'moon-first-quarter', 'moon-waxing-gibbous',
    'moon-full', 'moon-waning-gibbous', 'moon-last-quarter', 'moon-waning-crescent',
    'hurricane', 'tropical-storm', 'co2-cloud', 'co-cloud', 'degree-celsius',
    'degree-fahrenheit', 'lizard', 'service-dog',
    'steering-wheel', 'fuel-pump', 'car-seat', 'tire', 'headlight', 'horn',
    'license-plate', 'ferry', 'light-rail', 'airplane-seat', 'oil-can', 'tow-hitch',
    'ev-motor', 'dpad', 'arrow-keys',
    'capsule', 'oval', 'rhombus', 'trapezoid', 'right-triangle', 'skew', 'perspective',
    'aspect-ratio', 'loupe', 'scribble', 'guide-point', 'swirl', 'light-spectrum',
    'baht', 'cedi', 'colon-sign', 'cruzeiro', 'danish-krone', 'norwegian-krone',
    'swedish-krona', 'dong', 'florin', 'guarani', 'hryvnia', 'kip', 'mill', 'naira',
    'peseta', 'zloty', 'shekel', 'singapore-dollar', 'australian-dollar', 'brazilian-real',
    'tugrik', 'won', 'yuan', 'austral',
)


def register(api):
    shape, glyph = api['shape'], api['glyph']
    path, circle, rr = api['path'], api['circle'], api['rr']
    stroke, line, union = api['stroke'], api['line'], api['union']
    mirror, rotate = api['mirror'], api['transform']
    styles = api['STYLE_OVERRIDES']

    def subtract(body, cut):
        return api['op'](body, cut, api['po'].PathOp.DIFFERENCE)

    api['CATEGORY'] = 'Weather and nature'

    def ellipse(cx, cy, rx, ry):
        return circle(0, 0, 1).transform(rx, 0, 0, ry, cx, cy)

    # SF moon phases ink the illuminated part and leave the dark limb open:
    # new moon is an empty ring, full moon a solid disc. The terminator is a
    # half ellipse meeting the limb at both poles. Waning phases are mirrored.
    lunar_disc = circle(8, 8, 6)
    limb = stroke(lunar_disc)
    lit_disc = circle(8, 8, 6.2)
    east = subtract(lit_disc, rr(0, 0, 8, 16, 0))
    terminator = ellipse(8, 8, 3.1, 6.2)
    crescent = subtract(east, terminator)
    gibbous = union(east, terminator)
    for name, lit in (
        ('moon-new', None),
        ('moon-waxing-crescent', crescent),
        ('moon-first-quarter', east),
        ('moon-waxing-gibbous', gibbous),
        ('moon-full', lit_disc),
        ('moon-waning-gibbous', mirror(gibbous)),
        ('moon-last-quarter', mirror(east)),
        ('moon-waning-crescent', mirror(crescent)),
    ):
        ink = union(limb, lit)
        shape(name, lunar_disc, lit, 'astronomy lunar phase night orbit ' + name.replace('-', ' '))
        dark = subtract(lunar_disc, ink)
        styles[name] = {'duotone': [(dark, .24), (ink, 1)] if dark.area > .01 else [(ink, 1)],
                        'solid': ink, 'stroke': ink}

    # SF storms are narrow: two tapered comma arms leave a central disc and
    # curl to opposite sides. The hurricane is a solid vortex with an open
    # eye; the tropical storm keeps an open ring around a small dot.
    storm_disc = circle(8, 8, 2.95)
    arm = path('M5.05 8.4C4.6 4.1 7.5 1.45 11.95 1.5A.62 .62 0 0 1 11.95 2.74'
               'C8.75 2.8 6.6 4.75 6.45 7.25Z')
    arms = union(arm, rotate(arm, 180))
    vortex = subtract(union(storm_disc, arms), circle(8, 8, 1.2))
    glyph('hurricane', vortex, None, 'hurricane typhoon cyclone eye severe wind')
    storm_ring = api['ring'](8, 8, 2.95)
    storm_ink = union(storm_ring, subtract(arms, circle(8, 8, 2.5)), circle(8, 8, .85))
    shape('tropical-storm', circle(8, 8, 2.43), union(subtract(arms, circle(8, 8, 2.5)), circle(8, 8, .85)),
          'tropical storm cyclone forecast wind')
    styles['tropical-storm'] = {'solid': storm_ink, 'stroke': storm_ink}

    # The family cloud steps down-left to make room for two rising bubbles;
    # the formula sits low in the cloud with a small subscript, as in SF.
    gas_cloud = rotate(api['DRAWINGS']['cloud'][0], scale=.93, dx=-.6, dy=1.25)
    bubbles = union(circle(14.05, 3.55, 1.05), circle(12.15, 1.85, .75))
    letter_c = ('M6.3 8.6C6.0 8.1 5.65 7.9 5.2 7.9C4.4 7.9 3.95 8.65 3.95 9.75'
                'C3.95 10.85 4.4 11.6 5.2 11.6C5.65 11.6 6.0 11.4 6.3 10.9')
    letter_o = ellipse(8.4, 9.75, 1.2, 1.85)
    two = stroke('M10.45 10.55Q10.6 10.0 11.1 10.0Q11.75 10.0 11.7 10.6Q11.65 11.0 10.45 12.1H11.85')
    for name, dx, tags in (
        ('co-cloud', .6, 'carbon monoxide gas air quality sensor'),
        ('co2-cloud', 0, 'carbon dioxide emissions atmosphere gas air quality'),
    ):
        letters = rotate(union(stroke(letter_c), stroke(letter_o)), dx=dx)
        if name == 'co2-cloud':
            letters = union(letters, two)
        shape(name, gas_cloud, union(letters, bubbles), tags)

    degree = api['ring'](3.65, 4.15, 2.15)
    for name, letter, tags in (
        ('degree-celsius', 'M13.35 4.25C7.05 .15 5.5 13.15 10.95 13.25Q12.5 13.25 13.65 12',
         'temperature degrees celsius centigrade metric weather'),
        ('degree-fahrenheit', 'M7.95 13.3V3.35H13.8M7.95 7.95H12.65',
         'temperature degrees fahrenheit imperial weather'),
    ):
        glyph(name, union(degree, stroke(letter)), None, tags)

    # Seen from above, the body, curled tail and head form one continuous
    # C, like SF's lizard. Four bent legs splay out with short toes.
    gecko = path('M12.95 1.55C14.25 1.75 14.45 3.35 13.45 4.25'
                 'C12.75 4.85 11.95 4.95 11.25 5.35'
                 'C9.15 6.6 7.55 7.85 7.15 9.7C6.8 11.35 7.85 12.55 9.65 12.65'
                 'C11.35 12.75 12.85 12.15 14.45 11.15'
                 'C13.35 12.85 11.45 14.25 9.25 14.3C5.75 14.4 4.35 11.65 5.05 9.0'
                 'C5.65 6.65 7.55 5.05 9.75 3.6C10.35 2.75 11.25 1.3 12.95 1.55Z')
    limbs = stroke('M10.45 4.2L9.0 3.0L9.15 1.55M9.0 3.0L7.65 2.55'
                   'M12.1 5.15L12.65 6.85L14.15 7.25M12.65 6.85L12.3 8.3'
                   'M5.55 8.25L3.4 7.85L2.45 6.45M3.4 7.85L1.85 8.55'
                   'M6.0 11.85L4.6 13.15L2.95 12.95M4.6 13.15L4.55 14.55')
    shape('lizard', gecko, limbs, 'gecko reptile animal wildlife tail')

    # A standing dog in profile with a guide harness handle over its back.
    dog = path('M3.4 6.0H9.75L10.05 3.65Q10.3 2.35 11.6 2.35H12.55Q13.35 2.35 13.7 3.05'
               'L14.7 4.35Q15.15 5.45 14.0 5.65L12.95 5.8Q12.4 6.05 12.4 7.0'
               'L12.4 12.95Q12.4 13.7 11.65 13.7Q10.85 13.7 10.85 12.95'
               'L10.65 9.6H6.1L5.75 12.95Q5.7 13.7 4.95 13.7Q4.15 13.7 4.15 12.95'
               'L4.0 9.4Q2.6 8.6 2.7 7.3Q2.8 6.0 3.4 6.0Z')
    harness = stroke('M6.8 9.6V6.0M8.1 6.0L7.2 3.7H5.3M3.1 6.6Q1.6 5.6 1.55 3.85'
                     'M11.25 2.9Q10.85 4.35 11.55 5.05')
    shape('service-dog', dog, harness, 'assistance guide dog harness accessibility animal')

    api['CATEGORY'] = 'Maps and travel'
    # Standard rim with a soft hub and three spokes, as in SF steeringwheel.
    hub = rr(5.25, 6.55, 5.5, 3.5, 1.75)
    rim = api['ring'](8, 8, 6.52)
    spokes = stroke('M1.75 7.35L5.25 8.0M10.75 8.0L14.25 7.35M8 10.05V14.25')
    shape('steering-wheel', hub, union(rim, spokes), 'car steering wheel driver vehicle controls')

    # A tall pump with a solid display, a wide plinth and a looping hose.
    pump = rr(2.35, 1.65, 7.4, 11.6)
    display = rr(3.95, 3.3, 4.2, 3.2, .55, exact=True)
    hose = stroke('M9.75 7.0H10.45Q11.55 7.0 11.55 8.1V10.9'
                  'C11.55 12.85 14.2 12.85 14.2 10.9V5.15L12.15 3.0')
    plinth = line((1.35, 13.75), (10.75, 13.75))
    shape('fuel-pump', pump, union(display, plinth, hose), 'fuel pump petrol gas station refuel')

    # One continuous seat profile: bucket backrest and cushion, no rail.
    seat = path('M4.55 1.6Q5.95 1.45 6.25 2.85L7.05 7.75Q7.25 8.75 8.25 8.85'
                'L12.45 9.2Q13.95 9.35 13.95 11.0Q13.95 12.95 11.95 12.95H5.45'
                'Q3.6 12.95 3.4 11.05L2.55 3.75Q2.35 1.8 4.55 1.6Z')
    shape('car-seat', seat, None, 'vehicle car seat headrest driver passenger')

    # A quarter-turned tire reveals a strip of tread beyond the sidewall.
    tire = path('M7 1.95H9.15C15.85 1.95 15.85 14.05 9.15 14.05H7'
                'C.35 14.05 .35 1.95 7 1.95Z')
    bore = path('M6.9 5.3C4.2 5.3 4.2 10.7 6.9 10.7C9.6 10.7 9.6 5.3 6.9 5.3Z')
    side_edge = stroke('M7 1.95C13.65 1.95 13.65 14.05 7 14.05')
    shape('tire', tire, union(side_edge, stroke(bore)), 'tyre tire wheel sidewall rubber vehicle')
    tread_seam = stroke('M10.15 3.75C12.7 6.05 12.7 9.95 10.15 12.25')
    styles['tire'] = {'solid': subtract(union(tire, stroke(tire)), union(bore, tread_seam))}

    # SF high beam: a rounded lamp lens and four level beams.
    lamp = path('M8.25 3.1C12.95 3.1 14.55 5.3 14.55 8C14.55 10.7 12.95 12.9 8.25 12.9'
                'Q7.05 12.9 7.05 11.7V4.3Q7.05 3.1 8.25 3.1Z')
    beams = stroke('M1.45 4.55H4.75M1.45 6.85H4.75M1.45 9.15H4.75M1.45 11.45H4.75')
    shape('headlight', lamp, beams, 'car headlamp high beam light headlights')

    # A trumpet horn: flared bell, narrow throat and the return tube below.
    horn = path('M1.55 4.85H5.85Q10.15 4.65 12.45 2.1Q14.45 .75 14.45 3.35V8.75'
                'Q14.45 11.35 12.45 10.0Q10.15 7.45 5.85 7.25H1.55Z')
    tube = stroke('M2.45 7.25V9.25Q2.45 10.65 3.85 10.65H7.75Q8.85 10.65 8.85 9.55V7.75')
    shape('horn', horn, tube, 'vehicle horn honk trumpet sound alert')

    # A wide plate with registration characters, sized like SF licenseplate.
    plate = rr(1.17, 3.65, 13.66, 8.7)
    serial = stroke('M3.75 6.75L4.95 5.75V10.25'
                    'M6.85 6.75Q7.2 5.75 8.2 5.75Q9.35 5.75 9.35 6.95'
                    'Q9.35 7.75 8.55 8.45L6.85 10.25H9.45'
                    'M10.75 5.75H12.85L11.65 7.6Q13.1 7.6 13.1 8.95'
                    'Q13.1 10.35 11.8 10.35Q11.0 10.35 10.6 9.75')
    shape('license-plate', plate, serial, 'car license plate registration number vehicle tag')

    # SF ferry: bridge with windows above a broad hull, riding one wave.
    superstructure = union(rr(5.85, 1.45, 4.3, 2.6), rr(3.95, 3.65, 8.1, 4.55))
    hull = path('M1.75 8.2H14.25Q13.0 11.0 11.2 12.05Q9.4 11.95 8 12.95'
                'Q6.6 11.95 4.8 12.05Q3.0 11.0 1.75 8.2Z')
    windows = union(rr(5.25, 5.25, 2.1, 1.5, .45, exact=True),
                    rr(8.65, 5.25, 2.1, 1.5, .45, exact=True))
    wave = stroke('M1.6 14.35Q3.2 13.25 4.8 14.35T8 14.35T11.2 14.35T14.4 14.35')
    shape('ferry', union(superstructure, hull), union(windows, wave),
          'ferry boat passenger ship harbor crossing water transport')

    # SF lightrail: pantograph, tall car with a solid windscreen and lamps.
    railcar = rr(3.45, 4.35, 9.1, 9.05, 2.2, exact=True)
    windscreen = rr(4.95, 5.85, 6.1, 3.35, .6, exact=True)
    lamps = union(circle(5.85, 11.15, .65), circle(10.15, 11.15, .65))
    rail_details = stroke('M5.6 13.35L4.35 14.75M10.4 13.35L11.65 14.75'
                          'M5.05 1.35H10.95M6.35 1.35L8 4.35L9.65 1.35')
    shape('light-rail', railcar, union(windscreen, lamps, rail_details),
          'tram light rail streetcar electric train public transit')

    airline = path('M3.05 2.85Q4.2 2.35 4.7 3.45L7.5 9.45H12.6Q14 9.45 14 10.85'
                   'Q14 12.05 12.65 12.05H6.85Q5.7 12.05 5.2 10.9L2.4 4.65Q1.85 3.3 3.05 2.85Z')
    armrest = stroke('M6.4 7.4H10.3')
    support = stroke('M7.25 12L6.25 14.3M10.75 12L11.75 14.3')
    shape('airplane-seat', airline, union(armrest, support), 'airline cabin seat passenger airplane armrest')

    # SF oilcan: handle, filler cap, a long raised spout and a falling drop.
    oil = path('M3.6 6.35H8.75L10.05 7.65L14.15 5.35L14.85 6.1L11.05 10.85'
               'Q10.45 11.75 9.45 11.75H4.7Q3.6 11.75 3.6 10.65Z')
    handle = stroke('M3.6 6.9H1.45V8.35Q1.45 10.1 3.6 10.1'
                    'M6.2 6.35V4.0M4.5 4.0H7.9')
    drop = path('M14.2 8.65Q15.25 10.05 15.25 10.75A1.05 1.05 0 0 1 13.15 10.75'
                'Q13.15 10.05 14.2 8.65Z')
    shape('oil-can', oil, union(handle, drop), 'engine oil can lubrication service automotive')

    socket = path('M1.65 5.6H4.5L7.6 9.4H12.9Q14.15 9.4 14.15 10.6'
                  'Q14.15 11.8 12.9 11.8H7.2Q6.25 11.8 5.6 11L3.1 7.9H1.65Z')
    ball = circle(11.45, 5.15, 2.25)
    neck = line((11.45, 7.4), (11.45, 9.4))
    shape('tow-hitch', union(socket, ball), neck, 'tow hitch trailer ball coupling towing vehicle')

    motor = rr(3.6, 4.15, 9.35, 7.7)
    shaft = stroke('M1.45 6.8H3.6M1.45 9.2H3.6M12.95 6.8H14.55M12.95 9.2H14.55')
    winding = stroke('M5.85 8.25Q6.95 5.05 8.3 7.95T10.7 7.65')
    shape('ev-motor', motor, union(shaft, winding), 'electric vehicle motor rotor drive power alternating current')

    api['CATEGORY'] = 'Media'
    paddle = path('M6.25 2.45Q6.25 1.65 7.05 1.65H8.95Q9.75 1.65 9.75 2.45'
                  'V4.45L8 6.15L6.25 4.45Z')
    shape('dpad', union(*(rotate(paddle, a) for a in (0, 90, 180, 270))), None,
          'controller d-pad directional pad game navigation buttons')

    # SF arrowkeys: an inverted T of four equal keycaps with solid arrows.
    keys, arrows = [], []
    tri = path('M8 7.2L9.05 8.85H6.95Z')
    for cx, cy, angle in ((8, 5.35, 0), (2.95, 10.65, -90), (8, 10.65, 180), (13.05, 10.65, 90)):
        keys.append(rr(cx - 1.95, cy - 1.95, 3.9, 3.9, .95, exact=True))
        arrows.append(rotate(api['soften'](tri, .2), angle, dx=cx-8, dy=cy-8.1 if angle == 0 else cy-8))
    shape('arrow-keys', union(*keys), union(*arrows),
          'keyboard arrow keys cursor up down left right gaming')

    api['CATEGORY'] = 'Geometry'
    shape('capsule', rr(1.17, 2.85, 13.66, 10.3, 5.15), None, 'stadium obround pill capsule shape')
    shape('oval', ellipse(8, 8, 6.83, 5.2), None, 'ellipse oval geometric shape horizontal')
    shape('rhombus', path('M8 1.55L12.7 8L8 14.45L3.3 8Z'), None,
          'lozenge diamond rhombus quadrilateral geometry')
    shape('trapezoid', path('M4.55 3.4H11.45L14.5 12.6H1.5Z'), None,
          'trapezium trapezoid polygon parallel quadrilateral')
    shape('right-triangle', path('M13.55 2.45V13.55H2.45Z'), None,
          'triangle right angle diagonal geometry polygon')

    api['CATEGORY'] = 'Design tools'
    corners = ((5.4, 2.65), (12.95, 4.85), (13.4, 13.35), (2.35, 10.45))
    skewed = path('M5.4 2.65L12.95 4.85L13.4 13.35L2.35 10.45Z')
    nodes = union(*(circle(x, y, 1.15) for x, y in corners))
    shape('skew', skewed, nodes, 'transform shear distort skew handles vector corners')
    styles['skew'] = {'solid': union(skewed, stroke(skewed), nodes)}

    # SF perspective: a quad foreshortened to the left, crossed by its two
    # axes, which run past the outline on every side.
    plane = path('M3.55 4.35L12.45 2.45V13.55L3.55 11.65Z')
    axes = stroke('M1.05 8H14.95M8 1.05V14.95')
    shape('perspective', plane, axes, 'perspective projection plane vanishing grid transform')
    field = union(plane, stroke(plane))
    styles['perspective'] = {'solid': union(subtract(field, axes), subtract(axes, field))}

    # Standard SF rectangle with the nested 4:3 frame of aspectratio.
    frame = rr(1.17, 2.8, 13.66, 10.4)
    inset = stroke('M1.17 6.35H10.2Q11.05 6.35 11.05 7.2V13.2')
    shape('aspect-ratio', frame, inset, 'aspect ratio resize proportions image frame crop')
    cut = stroke('M.4 6.35H10.2Q11.05 6.35 11.05 7.2V14.0')
    styles['aspect-ratio'] = {'solid': subtract(union(frame, stroke(frame)), cut)}

    # SF loupe: a jeweler's eyepiece. A short barrel with a dark lens on top
    # flares into a wide skirt with a rounded rim.
    barrel = rr(4.65, 1.65, 6.7, 5.0, 1.1, exact=True)
    skirt = path('M4.65 6.0H11.35L12.95 11.4Q13.45 13.9 10.95 13.9H5.05'
                 'Q2.55 13.9 3.05 11.4Z')
    lens = ellipse(8, 3.2, 2.45, .72)
    collar = stroke('M4.65 6.25Q8 7.65 11.35 6.25')
    shape('loupe', union(barrel, skirt), union(lens, collar),
          'magnifier loupe optical lens inspect jeweler photography')

    scribble = stroke('M1.55 9.3L7.55 3.55C9.8 1.5 11.05 3.1 9.1 5.55'
                      'L5.6 10.15C3.8 12.75 5.4 13.35 7.2 11.55L10.25 8.65'
                      'C12.45 6.65 13.05 8.15 11.85 9.9L10.95 11.45'
                      'C9.6 13.7 11.45 14.05 14.4 11.3')
    glyph('scribble', scribble, None, 'freehand pen pencil drawing sketch scribble')
    handles = union(circle(2.95, 8, 1.55), circle(13.05, 8, 1.55))
    glyph('guide-point', line((2.95, 8), (13.05, 8)), handles,
          'vector guide point anchor control handles tangent')

    swirl_disc = circle(8, 8, 6.15)
    swirl = path('M8 1.85A6.15 6.15 0 0 1 8 14.15'
                 'C11.9 11.75 10.7 9.45 7.95 7.95C5.25 6.5 4.7 3.95 8 1.85Z')
    swirl_ink = union(swirl, stroke(swirl_disc))
    shape('swirl', swirl_disc, swirl, 'swirl twist tonal balance filter contrast effect')
    styles['swirl'] = {'solid': swirl_ink, 'stroke': swirl_ink}

    api['CATEGORY'] = 'Photography and optics'
    bands = ((2.45, 2.45), (4.65, 4.95), (6.85, 5.95),
             (9.15, 5.95), (11.35, 4.95), (13.55, 2.45))
    glyph('light-spectrum', union(*(line((x, 8-h), (x, 8+h)) for x, h in bands)), None,
          'light spectrum vibrance optical color wavelength exposure')

    api['CATEGORY'] = 'Finance and commerce'
    # Standalone currency signs are open monoline lettering like dollar-sign,
    # japanese-yen and swiss-franc. Shared letters use the same native masters.
    open_c = 'M12.2 4.65C10.5 1.35 4 2 3.8 7.95C3.6 13.95 10.15 14.8 12.3 11.55'
    kr = ('M3.45 2.3V13.35M7.85 6.05L3.45 9.6L8 13.35'
          'M10.45 13.35V6.05M10.45 9Q11.1 5.8 13.55 6.05')
    dollar = ('M14.15 4.8C12.7 2.35 8.8 3.05 8.8 5.6C8.8 8.4 14.35 7.45 14.35 10.5'
              'C14.35 13.25 10.4 14.1 8.45 11.6M11.5 1.45V14.55')
    currency = {
        'baht': ('M4.75 3.35H8.8C12.9 3.35 12.85 7.8 8.8 7.8H4.75'
                 'M8.8 7.8C13.5 7.8 13.45 12.65 8.8 12.65H4.75V3.35M7.65 1.45V14.55',
                 'thailand thai thb'),
        'cedi': (open_c + 'M8.45 1.4V14.6', 'ghana ghanaian ghs'),
        'colon-sign': (open_c + 'M8.4 1.5L5.5 14.5M11.3 1.5L8.4 14.5',
                       'colón costa rica costarricense crc'),
        'cruzeiro': ('M12.15 5.65C11.15 1.35 4.05 1.55 3.9 7.75'
                     'C3.65 14.9 11.05 15.15 12.55 10.8'
                     'M8.05 13.35V9.15Q8.05 7.35 10.05 7.35H11.3', 'brazil historical cr'),
        'danish-krone': ('M1.95 2.3V13.35M6.35 6.05L1.95 9.6L6.5 13.35'
                         'M8.95 13.35V6.05M8.95 9Q9.6 5.8 12.05 6.05', 'denmark danish dkk krone kr'),
        'norwegian-krone': (kr, 'norway norwegian nok kroner kr'),
        'swedish-krona': (kr, 'sweden swedish sek kronor kr'),
        'dong': ('M10.65 1.55V11.4M7.7 3.65H12.75'
                 'M10.65 8.15C10.65 3.8 3.75 4.05 3.75 8.15'
                 'C3.75 12.55 10.65 12.5 10.65 8.15ZM3.75 14H10.65', 'vietnam vietnamese đồng vnd'),
        'florin': ('M12.15 3.15C10.05 2.15 8.7 3.05 8.2 5.3L6.75 11.25'
                   'Q6.15 14.3 3.5 13.25M4.35 8.1H11.55', 'aruba guilder florin awg'),
        'guarani': ('M12.25 5.25C10.55 1.4 3.75 1.95 3.75 7.95'
                    'C3.75 14.65 12.3 14.65 12.3 9.5V8.55H8.3M8.25 1.45V14.55',
                    'paraguay paraguayan guaraní pyg'),
        'hryvnia': ('M4.4 4.6C5.65 1.85 11.85 1.8 11.85 4.8Q11.85 6.25 10.05 6.7'
                    'M3.2 6.7H12.8M3.2 9.3H12.8M5.95 9.3Q4.15 9.75 4.15 11.2'
                    'C4.15 14.2 10.35 14.15 11.6 11.4', 'ukraine ukrainian hryvnia uah'),
        'kip': ('M5.05 2.45V13.55M11.75 2.45L5.6 8L11.85 13.55M3 8H12.85', 'laos lao lak'),
        'mill': ('M2.85 12.15V5.45M2.85 8.15C2.85 4.45 7.85 4.3 7.85 7.85V12.15'
                 'M7.85 8.15C7.85 4.45 12.95 4.3 12.95 7.85V12.15M10.2 1.5L5.75 14.5',
                 'mill mille thousandth cent accounting'),
        'naira': ('M4.05 13.65V2.35L11.95 13.65V2.35M2.1 6.7H13.9M2.1 9.3H13.9', 'nigeria nigerian ngn'),
        'peseta': ('M4.65 13.65V2.65H8.55C14 2.65 14 9.05 8.55 9.05H4.65M2.55 5.8H13.55',
                   'spain spanish peseta esp historical'),
        'zloty': ('M2.45 6.05H8.45L2.45 13.05H8.45M11.85 2.75V13.05M9.95 9.05L13.75 6.55',
                  'poland polish złoty pln zł'),
        'shekel': ('M2.25 13.25V2.75H6.9Q9.55 2.75 9.55 5.65V9.95'
                   'M5.65 6.05V13.25H10.85Q13.75 13.25 13.75 10.3V2.75', 'israel israeli new sheqel ils'),
        'singapore-dollar': ('M6.1 4.8C4.95 2.65 1.65 3.05 1.65 5.55'
                             'C1.65 8.1 6.25 7.8 6.25 10.65C6.25 13.25 2.8 13.7 1.45 11.65' + dollar,
                             'singapore singaporean sgd'),
        'australian-dollar': ('M1.35 12.75L3.95 3.25L6.55 12.75M2.25 9.4H5.65' + dollar,
                              'australia australian aud aussie'),
        'brazilian-real': ('M1.5 12.85V3.3H3.65C7.3 3.3 7.3 8.15 3.65 8.15H1.5'
                           'M3.65 8.15L6.45 12.85' + dollar, 'brazil brazilian real brl reais'),
        'tugrik': ('M3.25 2.65H12.75M8 2.65V13.55M4.85 8.7L11.15 5.75M4.85 11.7L11.15 8.75',
                   'mongolia mongolian tögrög tugrik mnt'),
        'won': ('M1.7 2.8L4.6 13.2L8 3L11.4 13.2L14.3 2.8M1.3 8.25H14.7',
                'korea korean south north krw kpw'),
        'austral': ('M2.85 13.55L8 2.45L13.15 13.55M2.95 8.05H13.05M2.1 10.7H13.9',
                    'argentina argentine historical ara'),
    }
    # Narrow the signs that SF sets on a condensed width; squeezing the
    # skeleton before stroking keeps the single family weight.
    squeeze = {'naira': .76, 'peseta': .8, 'shekel': .82, 'kip': .8, 'austral': .72,
               'hryvnia': .83, 'mill': .82, 'zloty': .85, 'dong': .87, 'tugrik': .84}
    for name, (skeleton, tags) in currency.items():
        sx = squeeze.get(name, 1)
        mark = stroke(path(skeleton).transform(sx, 0, 0, 1, 8 - 8*sx, 0))
        if name == 'danish-krone':
            mark = union(mark, circle(13.45, 12.75, .8))
        glyph(name, mark, None, f'currency money finance {tags}')

    # Both currencies use the same conventional double-barred Y.
    yen_body, yen_detail = api['DRAWINGS']['japanese-yen'][:2]
    glyph('yuan', yen_body, yen_detail, 'currency money finance china chinese yuan renminbi cny rmb')
