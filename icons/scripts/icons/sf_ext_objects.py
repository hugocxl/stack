"""Sports, home, health and everyday objects on the native 16-unit grid."""

import math


NAMES = (
    'soccer-ball', 'basketball', 'baseball', 'tennis-ball', 'american-football',
    'cricket-ball', 'tennis-racket', 'skateboard', 'skis', 'snowboard',
    'surfboard', 'oar', 'sports-court', 'helmet',
    'fireplace', 'humidifier', 'dehumidifier', 'home-sensor', 'pipe',
    'roman-shade', 'cabinet', 'sink', 'stairs', 'hifi-receiver', 'av-remote',
    'web-camera', 'blood-pressure-cuff', 'inhaler', 'vial', 'star-of-life-shield',
    'sunglasses', 'comb', 'stroller', 'teddy-bear', 'water-bottle', 'level',
    'latch', 'piano-keys', 'amplifier', 'tuning-fork', 'rosette', 'laurel',
    'swatch-palette', 'magazine', 'greeting-card', 'menu-card', 'gift-card',
    'student-desk', 'coat', 'jacket', 'duffle-bag', 'gym-bag', 'fax-machine',
    'scanner', 'optical-disc',
)


def register(api):
    shape, glyph = api['shape'], api['glyph']
    path, rr, circle = api['path'], api['rr'], api['circle']
    stroke, line, lines = api['stroke'], api['line'], api['lines']
    union, mirror, turn = api['union'], api['mirror'], api['transform']
    drawings, overrides = api['DRAWINGS'], api['STYLE_OVERRIDES']

    def cut(body, detail):
        return api['op'](body, detail, api['po'].PathOp.DIFFERENCE)

    def inside(detail, body):
        return api['op'](detail, body, api['po'].PathOp.INTERSECTION)

    # Inset the Solid counters by one stroke. Feet, handles and stands
    # stay positive, even when they connect to a seam in the outline.
    def object_icon(name, body, seams, tags, fittings=None):
        shape(name, body, union(seams, fittings), tags)
        body = drawings[name][0]
        rim = stroke(body)
        counters = inside(seams, cut(body, rim))
        overrides[name] = {'solid': union(cut(union(body, rim), counters), fittings)}

    api['CATEGORY'] = 'Sports and outdoors'
    ball = drawings['volleyball'][0]

    def ball_icon(name, seams, tags):
        # Meet the center of the rim. Its stroke masks every seam endpoint.
        shape(name, ball, inside(seams, ball), tags)

    # Each leather patch presents a point to its opposite patch. Only the
    # short stretch of stitching between those two points remains visible.
    center_patch = api['poly']([(8 + 2.5*math.sin(i*math.tau/5), 8 - 2.5*math.cos(i*math.tau/5))
                                for i in range(5)])
    edge_patch = path('M8 4.3L6.35 3.25L5.95 1.45H10.05L9.65 3.25Z')
    patches = union(center_patch, *(turn(edge_patch, i*72) for i in range(5)))
    seam = line((8, 5.55), (8, 4.1))
    stitching = union(*(turn(seam, i*72) for i in range(5)))
    ball_icon('soccer-ball', union(patches, stitching), 'football soccer pentagon pitch team sport')
    # Leave the leather between the punched panels intact in Solid.
    ball_rim = stroke(ball)
    overrides['soccer-ball'] = {'solid': cut(union(ball, ball_rim), inside(patches, cut(ball, ball_rim)))}
    side_seam = stroke('M3.35 3.65Q8.35 8 3.35 12.35')
    ball_icon('basketball', union(side_seam, mirror(side_seam),
                                  lines('M8 1.8V14.2', 'M1.8 8H14.2')),
              'basketball hoop court dribble team sport')
    # Two pitched leather seams with an inset crossing stitch on each.
    stitched = lines('M2.15 5.95Q7.25 5.45 9.75 1.85', 'M4.6 4.35L5.65 6.45')
    ball_icon('baseball', union(stitched, turn(stitched, 180)),
              'baseball stitching pitch bat diamond sport')
    felt = stroke('M1.95 8.8C6.7 8.8 8.8 5.65 8.8 1.95')
    ball_icon('tennis-ball', union(felt, turn(felt, 180)), 'tennis felt seam racket court sport')
    leather = path('M1.45 8C3.4 2.5 12.6 2.5 14.55 8C12.6 13.5 3.4 13.5 1.45 8Z')
    lacing = lines('M5.5 8H10.5', 'M6.8 6.8V9.2', 'M9.2 6.8V9.2')
    shape('american-football', turn(leather, -38), turn(lacing, -38),
          'american football gridiron laces touchdown pigskin sport')
    cricket_seam = stroke('M1.55 6.05Q8 7.75 14.45 6.05')
    ball_icon('cricket-ball', turn(union(cricket_seam, turn(cricket_seam, dy=2.5)), -42),
              'cricket leather seam bowling bat sport')

    hoop = circle(0, 0, 1).transform(3.6, 0, 0, 3.85, 8, 5.4)
    throat = stroke('M5.05 7.6L8 12.1L10.95 7.6M8 12.1V14.65')
    strings = inside(lines('M6.8 1.45V9.35', 'M9.2 1.45V9.35', 'M4.3 5.4H11.7'), hoop)
    object_icon('tennis-racket', turn(hoop, 38), turn(strings, 38),
                'tennis racquet strings handle court sport', turn(throat, 38))
    deck = path('M1.6 5.15Q3 6.45 4.65 6.45H11.35Q13 6.45 14.4 5.15'
                'V7.1Q13.1 8.85 10.95 8.85H5.05Q2.9 8.85 1.6 7.1Z')
    wheels = union(circle(4.65, 11.7, 1.15), circle(11.35, 11.7, 1.15))
    shape('skateboard', deck, wheels, 'skate deck wheels board skatepark sport')

    ski = path('M4.4 14.3V3.8Q4.4 2.2 6.7 1.65V14.3Z')
    ski_pair = union(ski, mirror(ski))
    bindings = lines('M4.4 8H6.7', 'M9.3 8H11.6')
    object_icon('skis', turn(ski_pair, 18, dy=-.32), turn(bindings, 18, dy=-.32),
                'ski pair alpine snow winter downhill bindings')
    board = path('M5.55 4.35C5.2 .75 10.8 .75 10.45 4.35'
                 'Q9.9 8 10.45 11.65C10.8 15.25 5.2 15.25 5.55 11.65Q6.1 8 5.55 4.35Z')
    straps = lines('M5.8 5.65L10.25 6.5', 'M5.75 9.5L10.2 10.35')
    object_icon('snowboard', turn(board, 33), turn(straps, 33),
                'snowboard snow bindings mountain winter sport')
    board = path('M8 1.35C11.9 4.65 11.55 10.95 9.45 14.2'
                 'Q8 13.55 6.55 14.2C4.45 10.95 4.1 4.65 8 1.35Z')
    shape('surfboard', turn(board, 34), turn(line((8, 4.15), (8, 11.5)), 34),
          'surf board ocean wave surfing beach water sport')
    blade = path('M6.2 2.2Q8 1.45 9.8 2.2L9.45 7.05Q9.35 7.9 8 9.05'
                 'Q6.65 7.9 6.55 7.05Z')
    shaft = lines('M8 8.9V14.15', 'M6.95 14.15H9.05')
    shape('oar', turn(blade, 42), turn(shaft, 42), 'oar paddle rowing boat canoe water sport')

    court = rr(1.45, 3.65, 13.1, 8.7)
    court_lines = lines('M8 3.65V12.35', 'M4.1 3.65V12.35',
                        'M11.9 3.65V12.35', 'M4.1 8H11.9')
    shape('sports-court', court, court_lines, 'court tennis net field lines game sport')
    helmet = path('M2.1 9.55C1.55 5.75 3.95 2.95 7.8 2.85'
                  'C11.2 2.7 13.65 5.15 14.2 8L10.1 8.9L8.7 12.55'
                  'Q8.35 13.5 7.2 13.15L3.5 11.65Q2.3 11.2 2.1 9.55Z')
    shape('helmet', helmet, lines('M5.3 6.95L6.8 5.75', 'M8.5 6.2L9.75 5.25'),
          'helmet cycling protective headgear safety bike sport')

    api['CATEGORY'] = 'Home and food'
    mantel = path('M2.25 3.15H13.75V13.65H11.15V9.3A3.15 3.15 0 0 0 4.85 9.3V13.65H2.25Z')
    flame = path('M7.95 9.1Q8.25 10.1 9.05 10.95C10.95 13.7 6.3 14.55 6.45 12'
                 'Q6.55 10.9 7.95 9.1Z')
    shape('fireplace', mantel, flame, 'hearth mantel fire heating living room chimney')
    shelf = line((1.45, 3.15), (14.55, 3.15))
    surround = drawings['fireplace'][0]
    rim = union(stroke(surround), shelf, flame)
    overrides['fireplace'] = {'stroke': rim, 'duotone': [(cut(surround, rim), .24), (rim, 1)],
                              'solid': union(surround, rim)}

    tank = rr(3, 6.8, 10, 7.4)
    outlet = line((6.25, 9.45), (9.75, 9.45))
    mist = stroke('M6 4.6C4.7 3.5 7.1 2.95 6 1.65')
    shape('humidifier', tank, union(mist, turn(mist, dx=4), outlet),
          'humidity mist steam vaporiser vaporizer climate air appliance')
    intake = lines('M8 1.45V4.65', 'M6.35 3.15L8 4.8L9.65 3.15')
    shape('dehumidifier', tank, union(intake, outlet),
          'humidity dry moisture extraction climate air appliance')

    detector = rr(4.45, 9.4, 7.1, 4.4, 2.2)
    broadcast = lines('M2.1 4.85Q8 .05 13.9 4.85', 'M4.5 6.95Q8 4.1 11.5 6.95')
    shape('home-sensor', detector, union(broadcast, circle(8, 11.6, .6)),
          'home sensor motion detector occupancy automation wireless')

    elbow = path('M2.5 2.45H6.55V7.2Q6.55 9.45 8.8 9.45H13.7V13.45H8.8'
                 'C4.75 13.45 2.5 11.25 2.5 7.2Z')
    collars = lines('M1.55 2.45H7.5', 'M13.7 8.35V14.55')
    shape('pipe', elbow, collars, 'plumbing elbow water drain tube fitting')

    fabric = path('M2.4 2.6H12.05V10.95Q9.65 12.9 7.25 11.65'
                  'Q4.8 12.9 2.4 10.95Z')
    folds = lines('M2.4 5.55H12.05', 'M2.4 8.45H12.05')
    drawcord = stroke('M1.45 2.5H14.5V13.3')
    object_icon('roman-shade', fabric, folds, 'roman shade blind window fabric pleat drawstring', drawcord)
    cupboard = rr(2.15, 2.4, 11.7, 10.45)
    doors = lines('M8 2.4V12.85', 'M5.45 6.65V8.35', 'M10.55 6.65V8.35')
    object_icon('cabinet', cupboard, doors, 'cabinet cupboard wardrobe doors furniture storage',
                lines('M3.45 12.85V14.35', 'M12.55 12.85V14.35'))
    basin = path('M1.8 8.8H14.2L13.25 11.6Q12.5 13.6 10.5 13.6H5.5'
                 'Q3.5 13.6 2.75 11.6Z')
    tap = stroke('M6.15 8.8V4.15A1.9 1.9 0 0 1 9.95 4.15V5.15')
    shape('sink', basin, tap, 'sink washbasin faucet tap kitchen bathroom plumbing')
    stair = path('M1.65 11.75H4.75V8.65H7.85V5.55H10.95V2.45H14.35V5.5'
                 'L5.05 14.15H1.65Z')
    shape('stairs', stair, None, 'stairs steps staircase floor climb architecture')

    api['CATEGORY'] = 'Devices and connectivity'
    receiver = rr(1.5, 4.45, 13, 6.95)
    panel = union(stroke(circle(11.15, 7.9, 1.5)), line((3.8, 7.4), (6.9, 7.4)))
    object_icon('hifi-receiver', receiver, panel, 'hifi stereo audio tuner receiver volume home theater',
                lines('M3.2 11.4V12.55', 'M12.8 11.4V12.55'))
    remote = rr(4.55, 1.55, 6.9, 12.9)
    buttons = union(stroke(circle(8, 5.35, 1.55)), line((6.95, 9.65), (9.05, 9.65)),
                    circle(8, 12.15, .55))
    shape('av-remote', remote, buttons, 'remote control av television media buttons handset')
    webcam = rr(2.25, 2.9, 11.5, 7.9)
    stand = lines('M8 10.8V13.4', 'M4.85 13.4H11.15')
    object_icon('web-camera', webcam, stroke(circle(8, 6.85, 2.05)),
                'webcam video conference camera streaming lens desktop', stand)

    api['CATEGORY'] = 'Health and fitness'
    cuff = path('M2 3.3Q5.15 1.65 8.3 3.3V10.1Q5.15 8.45 2 10.1Z')
    hose = stroke('M5.15 9.25V10.75C5.15 14.65 12.1 14.65 12.1 10.75V8.5')
    bulb = rr(10.65, 4.05, 2.9, 4.75, 1.45)
    object_icon('blood-pressure-cuff', union(cuff, bulb), line((4.35, 5.6), (5.95, 5.6)),
                'blood pressure cuff sphygmomanometer monitor arm pump hypertension', hose)
    inhaler = path('M3.65 2.1H8.5L8.95 8.95H12.95V13.45H5.5Q4.25 13.45 4.15 12.15Z')
    object_icon('inhaler', inhaler, lines('M3.85 5H8.65', 'M10.7 8.95V13.45'),
                'inhaler asthma medication respiratory breathing mouthpiece')
    glass = path('M5.8 2.1H10.2V5.1L11.6 6.65V12.95Q11.6 14.2 10.35 14.2'
                 'H5.65Q4.4 14.2 4.4 12.95V6.65L5.8 5.1Z')
    object_icon('vial', glass, line((4.4, 9), (11.6, 9)),
                'vial sample medicine ampoule liquid laboratory glass',
                line((5.05, 2), (10.95, 2)))
    shield = drawings['shield'][0]
    # Six equal arms radiate from the medical emblem's center.
    arm = line((8, 5.05), (8, 10.95))
    star = turn(union(arm, turn(arm, 60), turn(arm, -60)), dy=-.35)
    shape('star-of-life-shield', shield, star, 'star of life emergency medical services ems rescue shield')

    api['CATEGORY'] = 'Finance and commerce'
    lens = path('M1.65 5.65Q4.25 4.9 6.9 5.8L6.5 8.65'
                'C6.05 11.85 2.5 11.6 2.05 9.2Z')
    bridge = stroke('M6.9 6.35Q8 5.45 9.1 6.35')
    shape('sunglasses', union(lens, mirror(lens)), bridge, 'sunglasses shades eyewear lenses sun fashion')

    api['CATEGORY'] = 'Home and food'
    spine = path('M2.1 4.05H13.9Q14.45 4.05 14.45 4.65V6.75H1.55V4.65Q1.55 4.05 2.1 4.05Z')
    teeth = union(*(line((x, 6.75), (x, 11.95)) for x in (1.55, 4.13, 6.71, 9.29, 11.87, 14.45)))
    shape('comb', spine, teeth, 'comb hair teeth grooming styling barber')

    carriage = path('M1.75 7.55C1.9 4.45 4.05 2.15 7.05 2.05L7.65 7.55H12.75'
                    'Q12.05 11.1 8.55 11.1H6.35Q2.9 11.1 1.75 7.55Z')
    handle = stroke('M12.5 8.05L13.7 5.05H14.6')
    axle = union(circle(5.1, 13.55, 1.05), circle(10.85, 13.55, 1.05))
    object_icon('stroller', carriage, line((1.75, 7.55), (7.65, 7.55)),
                'stroller pram pushchair carriage baby wheels', union(handle, axle))

    # The ears and paws form the outer silhouette; the muzzle reads at 16 px.
    ear = circle(4.1, 3.1, 1.5)
    paw = circle(4.35, 12.35, 1.95)
    bear = union(ear, mirror(ear), circle(8, 5.3, 3.7),
                 circle(8, 10.75, 3.1), paw, mirror(paw))
    face = union(circle(6.55, 4.95, .55), circle(9.45, 4.95, .55),
                 line((7.45, 7.1), (8.55, 7.1)), stroke('M6.15 10.15Q8 11.85 9.85 10.15'))
    shape('teddy-bear', bear, face, 'teddy bear plush stuffed animal toy nursery')
    flask = path('M6.1 1.8H9.9V4.05Q9.9 4.75 10.85 5.45'
                 'Q11.75 6.1 11.75 7.6V12.95Q11.75 14.2 10.5 14.2H5.5'
                 'Q4.25 14.2 4.25 12.95V7.6Q4.25 6.1 5.15 5.45Q6.1 4.75 6.1 4.05Z')
    object_icon('water-bottle', flask, lines('M6.1 4.05H9.9', 'M6.65 10.75H9.35'),
                'water bottle drink flask refill hydration canteen')

    api['CATEGORY'] = 'Product tools'
    # A flat straight beam with a capsule vial window holding one bubble,
    # and a short tick either side of centre.
    level_body = rr(1.2, 4.55, 13.6, 6.9)
    vial = rr(4.7, 6.35, 6.6, 3.3, 1.65)
    bubble = circle(8, 8, .6)
    ticks = lines('M3.15 6.9V9.1', 'M12.85 6.9V9.1')
    shape('level', level_body, union(stroke(vial), bubble, ticks),
          'spirit level bubble vial horizontal carpenter construction tool')
    overrides['level'] = {'solid': union(cut(union(level_body, stroke(level_body)),
                                             union(vial, ticks)), bubble)}
    plate, keeper = rr(1.6, 4.6, 7.8, 6.8), rr(12, 5.1, 2.4, 5.8)
    bolt = stroke('M4.45 6.65V8H14.15')
    shape('latch', union(plate, keeper), bolt, 'latch sliding bolt door gate lock hardware')
    # The keeper anchors the rod; the cut around the lever exposes its travel.
    lever_slot = union(bolt, stroke(bolt, 2.1))
    overrides['latch'] = {'solid': union(cut(union(plate, stroke(plate)), lever_slot),
                                         keeper, stroke(keeper), bolt)}

    api['CATEGORY'] = 'Media and communication'
    # A cropped D–A keyboard exposes the key tops. Only the key fronts
    # carry a continuous outline; there is no enclosing case or top rail.
    keyboard = path('M1.35 4.15H14.65V10.1Q14.65 11.35 13.4 11.35H2.6'
                    'Q1.35 11.35 1.35 10.1Z')
    fronts = stroke('M1.35 4.65V10.1Q1.35 11.35 2.6 11.35H13.4'
                    'Q14.65 11.35 14.65 10.1V4.65')
    black_keys = union(*(path(f'M{x-1.1} 4.15H{x+1.1}V7.55Q{x+1.1} 7.95 {x+.7} 7.95'
                              f'H{x-.7}Q{x-1.1} 7.95 {x-1.1} 7.55Z')
                         for x in (3.95, 9.1, 12.4)))
    divisions = union(line((6.45, 4.65), (6.45, 11.35)),
                      *(line((x, 7.55), (x, 11.35)) for x in (3.95, 9.1, 12.4)))
    key_ink = union(fronts, divisions, black_keys)
    shape('piano-keys', keyboard, union(divisions, black_keys),
          'piano keys keyboard ivory music instrument octave')
    # Extend the separations through the ends of the white keys.
    tips = union(*(line((x, 10.95), (x, 12.15)) for x in (3.95, 6.45, 9.1, 12.4)))
    overrides['piano-keys'] = {'stroke': key_ink,
                               'duotone': [(cut(keyboard, key_ink), .24), (key_ink, 1)],
                               'solid': cut(union(keyboard, fronts), union(divisions, tips, black_keys))}

    speaker_box = rr(2.8, 1.5, 10.4, 13)
    knobs = union(*(circle(x, 3.8, .6) for x in (5.15, 8, 10.85)))
    grille = stroke(circle(8, 9.55, 3.05))
    shape('amplifier', speaker_box, union(knobs, grille),
          'amplifier guitar amp speaker cabinet grille audio gain')
    fork = stroke('M5.45 1.8V7.45A2.55 2.55 0 0 0 10.55 7.45V1.8')
    glyph('tuning-fork', fork, line((8, 10), (8, 14.3)),
          'tuning fork pitch reference resonance music instrument')

    api['CATEGORY'] = 'Work and education'
    # Quadratic scallops give the cockade a soft folded fabric edge.
    def polar(angle, radius):
        return (8 + radius*math.sin(angle), 6.2 - radius*math.cos(angle))

    petals = []
    for i in range(8):
        angle = i*math.tau/8
        crest = polar(angle, 6.25)
        valley = polar(angle + math.pi/8, 4.05)
        petals.append(f'Q{crest[0]} {crest[1]} {valley[0]} {valley[1]}')
    x, y = polar(-math.pi/8, 4.05)
    seal = path(f'M{x} {y}' + ''.join(petals) + 'Z')
    tail = path('M5.15 9.2L4.25 14.2L6.15 13.45L7.4 14.45L7.9 10.45Z')
    tail = turn(tail, dx=-.35)
    ribbons = union(tail, mirror(tail))
    field = union(seal, ribbons)
    shape('rosette', field, union(inside(stroke(seal), ribbons), stroke(circle(8, 6.2, 2.05))),
          'rosette award prize ribbon cockade merit winner')
    overrides['rosette'] = {'solid': union(cut(union(seal, stroke(seal)), stroke(circle(8, 6.2, 2.05))),
                                          cut(union(ribbons, stroke(ribbons)), union(seal, stroke(seal, 3.2))))}

    twig = stroke('M6.8 13.95C4.05 12.4 2.35 9.25 3.35 5.7')
    top_leaf = path('M3.3 6.1C1.65 4.65 2.45 2.75 4.65 1.45C5.4 3.8 4.85 5.55 3.3 6.1Z')
    outer_leaf = path('M3.65 10.6C1.7 10.35 1.25 8.85 1.35 7.15C3.35 7.35 4.05 8.95 3.65 10.6Z')
    inner_leaf = path('M5.6 12.85C4.65 10.45 5.25 8.95 6.7 8.1C7.2 10.45 7.1 11.85 5.6 12.85Z')
    leaves = union(top_leaf, outer_leaf, inner_leaf)
    greenery = union(leaves, mirror(leaves))
    stems = union(cut(twig, leaves), mirror(cut(twig, leaves)))
    shape('laurel', greenery, stems, 'laurel wreath leaves victory honor award champion')

    api['CATEGORY'] = 'Editing and design'
    # Upright paint strips fan out around the common rivet.
    strip = rr(2.2, 1.85, 4.35, 12.45)
    pivot = (4.375, 12.1)

    def fan_strip(angle):
        a = math.radians(angle)
        c, s = math.cos(a), math.sin(a)
        x, y = pivot
        return strip.transform(c, s, -s, c, x - c*x + s*y, y - s*x - c*y)

    middle, rear = fan_strip(39), fan_strip(78)
    rivet = circle(*pivot, .6)
    color_chips = lines('M2.2 5.15H6.55', 'M2.2 8.4H6.55')
    edges = union(stroke(strip), cut(stroke(middle), strip), cut(stroke(rear), union(strip, middle)))
    fan = union(strip, middle, rear)
    shape('swatch-palette', fan, union(edges, color_chips, rivet), 'color palette swatches sample fan paint chips')
    overrides['swatch-palette'] = {
        'stroke': union(edges, color_chips, rivet),
        'solid': union(cut(union(rear, stroke(rear)), union(middle, stroke(middle, 3.2), strip, stroke(strip, 3.2))),
                       cut(union(middle, stroke(middle)), union(strip, stroke(strip, 3.2))),
                       cut(union(strip, stroke(strip)), union(inside(color_chips, cut(strip, stroke(strip))), rivet))),
    }

    api['CATEGORY'] = 'Documents and books'
    cover = path('M2.35 3.15Q6.9 3.2 11.35 1.65V10.85Q7 12.35 2.35 12.25Z')
    pages = stroke('M13.85 3.8V12.05Q13.85 12.95 12.8 13.25Q8.65 14.65 4.15 14.65')
    title = stroke('M5.3 5.75Q7.2 5.7 9.15 5')
    object_icon('magazine', cover, title, 'magazine periodical publication issue reading cover', pages)

    greeting = path('M2.6 3.6L12.75 5.5V14.25L2.6 12.35Z')
    fold = stroke('M2.65 3.6L11.1 1.65V5.15')
    heart = path('M7.75 11.05L5.65 8.9C4.35 7.4 6.45 6.3 7.75 8.05'
                 'C9.05 6.8 11.05 8.6 9.75 9.65Z')
    object_icon('greeting-card', greeting, heart, 'greeting card birthday invitation wishes folded heart', fold)
    menu = path('M3.15 3.5L12.85 2V13.45L3.15 14Z')
    text_rows = lines('M5.6 5.95L10.4 5.4', 'M5.6 8.45L10.4 7.9', 'M5.6 10.9L8.6 10.6')
    object_icon('menu-card', menu, text_rows, 'menu card restaurant food dining courses list')

    api['CATEGORY'] = 'Finance and commerce'
    card = rr(1.5, 3.4, 13, 9.2)
    ribbon = lines('M8 9.25V12.6', 'M1.5 9.25H14.5')
    loop = stroke('M8 9.25Q4.2 9.25 4.15 7.1C4.05 4.65 7.15 5.1 8 9.25')
    bow = union(loop, mirror(loop))
    object_icon('gift-card', card, union(ribbon, bow), 'gift card voucher prepaid present ribbon shopping')

    api['CATEGORY'] = 'Work and education'
    chair = rr(4.9, 1.65, 6.2, 4.05)
    desktop = rr(1.55, 7.9, 12.9, 2.55)
    legs = lines('M4.35 10.45L3.35 14.35', 'M11.65 10.45L12.65 14.35')
    shape('student-desk', union(chair, desktop), union(legs, line((8, 5.7), (8, 7.9))),
          'school classroom desk chair student furniture education')

    api['CATEGORY'] = 'Finance and commerce'
    overcoat = path('M5.85 2.15H10.15L12.05 3.05L14.4 10.65L12.05 11.35L10.95 7.85'
                    'L11.45 14.15H4.55L5.05 7.85L3.95 11.35L1.6 10.65L3.95 3.05Z')
    lapels = lines('M5.85 2.15L6.2 4.4L8 6.95L9.8 4.4L10.15 2.15', 'M8 6.95V14.15')
    object_icon('coat', overcoat, lapels, 'overcoat long coat lapel formal winter outerwear clothing')
    bomber = path('M5.45 2.75Q8 3.65 10.55 2.75L12.45 4L14.55 10.65L12.35 11.55'
                  'L10.85 8.25L11.3 13.25Q8 14.05 4.7 13.25L5.15 8.25'
                  'L3.65 11.55L1.45 10.65L3.55 4Z')
    zipper = lines('M8 4.6V13.65', 'M5.45 2.75L6.15 5.95L8 4.6L9.85 5.95L10.55 2.75')
    shape('jacket', bomber, zipper, 'jacket collar zip bomber sleeves outerwear clothing')

    api['CATEGORY'] = 'Maps and travel'
    duffle = path('M4.75 5.65H11.25Q13.75 5.65 14.2 9L14.45 11.85Q14.6 13.35 13.1 13.35'
                  'H2.9Q1.4 13.35 1.55 11.85L1.8 9Q2.25 5.65 4.75 5.65Z')
    handles = stroke('M5.35 5.65V4.4A2.65 2.65 0 0 1 10.65 4.4V5.65')
    straps = lines('M4.75 5.65V13.35', 'M11.25 5.65V13.35')
    object_icon('duffle-bag', duffle, straps, 'duffel duffle travel luggage overnight holdall straps', handles)
    gym = path('M5.45 5.25H10.55Q12.25 5.25 12.9 7L14.25 11.35Q14.75 13.3 12.75 13.3'
               'H3.25Q1.25 13.3 1.75 11.35L3.1 7Q3.75 5.25 5.45 5.25Z')
    loops = stroke('M5.7 5.25V4.1A2.3 2.3 0 0 1 10.3 4.1V5.25')
    pocket = stroke('M4.4 8.1H11.6L11.2 9.65Q11 10.65 9.95 10.65H6.05Q5 10.65 4.8 9.65Z')
    object_icon('gym-bag', gym, pocket, 'gym bag kit locker workout training sports pocket', loops)

    api['CATEGORY'] = 'Devices and connectivity'
    fax = rr(1.65, 5.65, 12.7, 7.65)
    paper = stroke('M6.45 5.65V2.25H12.15V5.65')
    handset = rr(3.65, 7.4, 2.25, 4.15, 1.125)
    keypad = union(*(circle(x, y, .6) for x in (8.65, 11.25) for y in (8.35, 10.85)))
    object_icon('fax-machine', fax, union(handset, keypad), 'fax facsimile telephone office paper keypad', paper)
    base = path('M3.95 7.4H12.05L14.4 10.65V13.45H1.6V10.65Z')
    lid = stroke('M3.95 7.4L2.05 2.85H13.95L12.05 7.4')
    object_icon('scanner', base, line((1.6, 10.65), (14.4, 10.65)),
                'flatbed scanner digitize document scan copier glass', lid)
    disc = drawings['disc'][0]
    hub = circle(8, 8, 2.55)
    inner_track = stroke(hub)
    beam = inside(lines('M9.3 5.85L11.25 2.8', 'M10.3 6.9L13.55 5.4'), disc)
    gleam = union(beam, turn(beam, 180))
    shape('optical-disc', disc, union(inner_track, gleam),
          'optical disc cd dvd blu-ray storage media laser')
    # Leave the spindle hole open through the reflective surface in every style.
    rim = stroke(disc)
    ink = union(rim, inner_track, gleam)
    surface = cut(disc, union(hub, ink))
    sectors = inside(gleam, cut(cut(disc, rim), circle(8, 8, 3.15)))
    overrides['optical-disc'] = {'duotone': [(surface, .24), (ink, 1)],
                                 'stroke': ink,
                                 'solid': cut(union(disc, rim), union(circle(8, 8, 1.65), sectors))}
