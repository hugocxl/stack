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
    # Compose the shaded hemisphere and limb as one foreground. The illuminated
    # surface stays open even in Solid, so the phase is independent of the tint.
    lunar_disc = circle(8, 8, 6.15)
    limb = stroke(lunar_disc)
    west = 'M8 1.85A6.15 6.15 0 0 0 8 14.15'
    crescent = path(west + 'A3.15 6.15 0 0 0 8 1.85Z')
    quarter = path(west + 'Z')
    gibbous = path(west + 'A3.15 6.15 0 0 1 8 1.85Z')
    for name, shade in (
        ('moon-new', lunar_disc),
        ('moon-waxing-crescent', crescent),
        ('moon-first-quarter', quarter),
        ('moon-waxing-gibbous', gibbous),
        ('moon-full', None),
        ('moon-waning-gibbous', mirror(gibbous)),
        ('moon-last-quarter', mirror(quarter)),
        ('moon-waning-crescent', mirror(crescent)),
    ):
        ink = union(limb, shade)
        shape(name, lunar_disc, shade, 'astronomy lunar phase night orbit ' + name.replace('-', ' '))
        styles[name] = {'duotone': [(subtract(lunar_disc, ink), .24), (ink, 1)],
                        'solid': ink, 'stroke': ink}

    storm_disc = circle(8, 8, 3.55)
    arm = stroke('M4.53 8.75C3.75 4.15 6.95 1.8 11.6 1.5')
    arms = union(arm, rotate(arm, 180))
    storm_ring = stroke(storm_disc)
    for name, eye, tags in (
        ('hurricane', circle(8, 8, 1.45), 'hurricane typhoon cyclone eye severe wind'),
        ('tropical-storm', circle(8, 8, .78), 'tropical storm cyclone forecast wind'),
    ):
        shape(name, storm_disc, union(arms, eye), tags)
        filled = union(storm_disc, storm_ring)
        if name == 'hurricane':
            vortex = union(subtract(filled, eye), arms)
            styles[name] = {'duotone': [(vortex, 1)], 'solid': vortex, 'stroke': vortex}
        else:
            styles[name] = {'solid': union(storm_ring, arms, eye)}

    gas_cloud = path('M4.1 13.35Q1.3 13.35 1.3 10.5V8.6Q1.3 5.85 3.85 5.35'
                     'C5.15 1.15 10.6 1.15 12.1 5.35Q14.7 5.8 14.7 8.6V10.55'
                     'Q14.7 13.35 11.9 13.35Z')
    for name, dx, tags in (
        ('co-cloud', 1.1, 'carbon monoxide gas air quality sensor'),
        ('co2-cloud', 0, 'carbon dioxide emissions atmosphere gas air quality'),
    ):
        letters = rotate(stroke('M5.15 7.8C2.95 5.95 2.95 12.25 5.15 10.4'
                                'M7.35 8.8C7.35 6.45 9.25 6.45 9.25 8.8V9.3'
                                'C9.25 11.65 7.35 11.65 7.35 9.3Z'), dx=dx)
        if name == 'co2-cloud':
            letters = union(letters, stroke('M11.4 8.5Q12.95 7.2 12.44 9L11.4 10.8H12.45'))
        shape(name, gas_cloud, letters, tags)

    degree = api['ring'](3.65, 4.15, 2.15)
    for name, letter, tags in (
        ('degree-celsius', 'M13.35 4.25C7.05 .15 5.5 13.15 10.95 13.25Q12.5 13.25 13.65 12',
         'temperature degrees celsius centigrade metric weather'),
        ('degree-fahrenheit', 'M7.95 13.3V3.35H13.8M7.95 7.95H12.65',
         'temperature degrees fahrenheit imperial weather'),
    ):
        glyph(name, union(degree, stroke(letter)), None, tags)

    # Splayed legs frame the curved spine. The long tapering tail carries the
    # silhouette, leaving room to identify the animal without miniature toes.
    gecko = path('M8.5 6.65C8.65 5.4 9.55 4.8 10.2 4.35'
                 'C10.65 2.35 13.85 1.45 14.2 3.1C14.5 4.8 12.75 5.7 11.55 5.85'
                 'C10.8 6.55 11.15 8.95 9.5 10.55C7.65 12.4 3.9 13.6 2.15 11.35'
                 'Q.95 9.9 1.85 8.1C1.9 10.55 3.15 11.45 5.05 10.7'
                 'Q7.55 9.85 8.5 6.65Z')
    limbs = stroke('M9.8 6.35L7.45 4.9L7.3 3.2M10.4 7.8L12.55 8.15L13.4 6.9'
                   'M7.65 9.55L5.55 8.25L5.3 6.9M8.2 10.9L9.25 12.7L11.05 12.9')
    shape('lizard', gecko, limbs, 'gecko reptile animal wildlife tail')

    dog = path('M2.45 6.75L3.8 7.35H8.75L10.15 4.3L10.35 2.7Q10.55 2.1 11.3 2.7'
               'L12.8 4.15L14.55 4.85L14.2 6.45Q13.95 7.2 12.5 7L11.45 6.8'
               'L10.6 9.15V13.5H8.7L8.45 10.8H5.5L4.4 13.5H2.45L3.65 9.65'
               'Q2.15 8.85 1.65 7.1Q1.3 5.6 2.45 6.75Z')
    harness = stroke('M5.65 7.35V9.55H8.1V7.35')
    shape('service-dog', dog, harness, 'assistance guide dog harness accessibility animal')

    api['CATEGORY'] = 'Maps and travel'
    # Keep the wheel open between the three spokes even in its solid style.
    hub = path('M5.4 7.15Q8 6.55 10.6 7.15L9.35 9.45Q8 10.45 6.65 9.45Z')
    wheel = stroke(circle(8, 8, 6.15))
    spokes = stroke('M2 6.75L5.65 7.55M10.35 7.55L14 6.75M8 9.55V14.05')
    shape('steering-wheel', hub, union(wheel, spokes), 'car steering wheel driver vehicle controls')

    pump = rr(2.4, 2.35, 7.65, 10.95)
    window = rr(4.6, 4.55, 3.25, 3.1)
    hose = stroke('M10 7.45Q11.7 7.45 11.7 9.45V10.85'
                  'C11.7 12.75 14.35 12.75 14.35 10.85V6.3L12.2 4.05')
    plinth = line((1.45, 13.65), (10.9, 13.65))
    shape('fuel-pump', pump, union(stroke(window), plinth, hose), 'fuel pump petrol gas station refuel')
    styles['fuel-pump'] = {'solid': union(subtract(union(pump, stroke(pump)), window), hose, plinth)}

    headrest = rr(9.55, 1.4, 3.6, 2.3)
    backrest = api['poly']([(9.35, 4.75), (13.05, 5.05), (12.25, 12.2), (8.55, 12.2)])
    cushion = rr(2.2, 9.6, 10.2, 2.6)
    rail = line((4.1, 14.25), (10.4, 14.25))
    shape('car-seat', union(headrest, backrest, cushion), rail,
          'vehicle car seat headrest driver passenger')

    # A quarter-turned tire reveals a strip of tread beyond the sidewall.
    tire = path('M7 1.95H9.15C15.85 1.95 15.85 14.05 9.15 14.05H7'
                'C.35 14.05 .35 1.95 7 1.95Z')
    bore = path('M6.9 5.3C4.2 5.3 4.2 10.7 6.9 10.7C9.6 10.7 9.6 5.3 6.9 5.3Z')
    side_edge = stroke('M7 1.95C13.65 1.95 13.65 14.05 7 14.05')
    shape('tire', tire, union(side_edge, stroke(bore)), 'tyre tire wheel sidewall rubber vehicle')
    tread_seam = stroke('M10.15 3.75C12.7 6.05 12.7 9.95 10.15 12.25')
    styles['tire'] = {'solid': subtract(union(tire, stroke(tire)), union(bore, tread_seam))}

    lamp = path('M8.35 3.65Q14.45 3.65 14.45 8Q14.45 12.35 8.35 12.35'
                'Q7.15 12.35 7.15 11.1V4.9Q7.15 3.65 8.35 3.65Z')
    beams = stroke('M1.55 4.9H4.85M1.55 8H4.85M1.55 11.1H4.85')
    shape('headlight', lamp, beams, 'car headlamp high beam light headlights')

    horn = path('M5.6 6.55L10.95 3.4Q11.65 3 11.65 3.85V12.15Q11.65 13 10.95 12.6L5.6 9.45Z')
    sound = union(line((1.55, 8), (5.6, 8)),
                  stroke('M13.55 5.75Q14.55 8 13.55 10.25'))
    shape('horn', horn, sound, 'vehicle horn honk trumpet sound alert')

    plate = rr(1.45, 3.8, 13.1, 8.4)
    bolts = union(circle(3.75, 6.1, .55), circle(12.25, 6.1, .55))
    serial = stroke('M4.3 9.3H7.8M10 9.3H11.7')
    shape('license-plate', plate, union(bolts, serial), 'car license plate registration number vehicle tag')

    cabin = path('M4.1 8.55L4.65 4.25H11.35L11.9 8.55Z')
    bow = path('M2.2 8.95L8 7.05L13.8 8.95L11.15 13.1Q9.4 12.9 8 13.85'
               'Q6.6 12.9 4.85 13.1Z')
    bridge = rr(6.05, 2.05, 3.9, 2.2)
    deck = union(bridge, cabin, bow)
    bow_line = stroke('M2.2 8.95L8 7.05L13.8 8.95M8 7.05V11.15')
    shape('ferry', deck, union(bow_line, line((4.65, 4.25), (11.35, 4.25))),
          'ferry boat passenger ship harbor crossing water transport')

    railcar = rr(3.6, 4.45, 8.8, 7.75)
    windscreen = rr(5.8, 6.65, 4.4, 2.35, 1.25)
    rail_details = stroke('M5.45 12.05L4.1 14.45M10.55 12.05L11.9 14.45'
                          'M5 1.55H11M5.65 1.55L7.35 4.45M10.35 1.55L8.65 4.45')
    shape('light-rail', railcar, union(rail_details, stroke(windscreen)),
          'tram light rail streetcar electric train public transit')
    styles['light-rail'] = {'solid': union(subtract(union(railcar, stroke(railcar)), windscreen), rail_details)}

    airline = path('M3.05 2.85Q4.2 2.35 4.7 3.45L7.5 9.45H12.6Q14 9.45 14 10.85'
                   'Q14 12.05 12.65 12.05H6.85Q5.7 12.05 5.2 10.9L2.4 4.65Q1.85 3.3 3.05 2.85Z')
    armrest = stroke('M6.4 7.4H10.3')
    support = stroke('M7.25 12L6.25 14.3M10.75 12L11.75 14.3')
    shape('airplane-seat', airline, union(armrest, support), 'airline cabin seat passenger airplane armrest')

    oil = path('M3.7 6.3H8.85L10.1 7.65L13.8 5.65L14.6 6.55L11.15 10.85'
               'Q10.55 11.8 9.55 11.8H4.8Q3.7 11.8 3.7 10.7Z')
    handle = stroke('M3.7 6.85H1.45V8.35Q1.45 10.15 3.7 10.15'
                    'M6.4 6.3V3.9M4.65 3.9H8.15')
    shape('oil-can', oil, handle, 'engine oil can lubrication service automotive')

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

    # Each key is its own cap. In the small key faces the open chevrons carry
    # direction and the negative perimeter separates adjacent buttons.
    caps, arrows = [], []
    for x, y, angle in ((8, 4.65, 0), (2.85, 10.7, -90), (8, 10.7, 180), (13.15, 10.7, 90)):
        caps.append(rr(x - 2, y - 2.35, 4, 4.7))
        arrows.append(rotate(stroke('M7.25 8.4L8 7.5L8.75 8.4'), angle, dx=x-8, dy=y-8))
    keycaps, arrows = union(*caps), union(*arrows)
    key_edges = []
    for x, y, angle in ((8, 3.1, 0), (2.85, 10, -90), (8, 10, 180), (13.15, 10, 90)):
        key_edges.extend((rotate(stroke('M6.7 8.7L8 7.3L9.3 8.7'), angle, dx=x-8, dy=y-8),
                          line((x-1.45, y+3.45), (x+1.45, y+3.45))))
    keys = subtract(keycaps, arrows)
    glyph('arrow-keys', keycaps, arrows, 'keyboard arrow keys cursor up down left right gaming')
    api['DUOTONE_GLYPHS']['arrow-keys'] = 'Four keycap surfaces behind their direction marks.'
    styles['arrow-keys'] = {'duotone': [(keys, .24), (arrows, 1)], 'solid': keys, 'stroke': keys}

    api['CATEGORY'] = 'Geometry'
    shape('capsule', rr(1.45, 4.05, 13.1, 7.9, 3.95), None, 'stadium obround pill capsule shape')
    oval = path('M1.45 8A6.55 4.65 0 1 0 14.55 8A6.55 4.65 0 1 0 1.45 8Z')
    shape('oval', oval, None, 'ellipse oval geometric shape horizontal')
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

    # A floor plane receding to the horizon: converging rails and one
    # cross rail, like a ground grid seen in perspective.
    plane = path('M4.75 3.3H11.25L14.45 12.7H1.55Z')
    grid = stroke('M6.95 3.3L5.95 12.7M9.05 3.3L10.05 12.7M3.2 7.85H12.8')
    shape('perspective', plane, grid, 'perspective projection plane vanishing grid transform')

    frame = rr(1.5, 3.15, 13, 9.7)
    inset = stroke('M1.5 6.25H10.85Q11.65 6.25 11.65 7.05V12.85')
    shape('aspect-ratio', frame, inset, 'aspect ratio resize proportions image frame crop')
    cut = stroke('M.7 6.25H10.85Q11.65 6.25 11.65 7.05V13.65')
    styles['aspect-ratio'] = {'solid': subtract(union(frame, stroke(frame)), cut)}

    tab = api['poly']([(9.45, 11.35), (11.35, 9.45), (14.3, 12.4), (12.4, 14.3)])
    loupe = union(circle(7.05, 7.05, 5.05), tab)
    shape('loupe', loupe, stroke(circle(7.05, 7.05, 2.75)),
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
    for name, (skeleton, tags) in currency.items():
        mark = stroke(skeleton)
        if name == 'danish-krone':
            mark = union(mark, circle(13.45, 12.75, .8))
        glyph(name, mark, None, f'currency money finance {tags}')

    # Both currencies use the same conventional double-barred Y.
    yen_body, yen_detail = api['DRAWINGS']['japanese-yen'][:2]
    glyph('yuan', yen_body, yen_detail, 'currency money finance china chinese yuan renminbi cny rmb')
