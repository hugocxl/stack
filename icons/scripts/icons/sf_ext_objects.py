"""Sports, home, health and everyday objects on the native 16-unit grid.

Each drawing follows the construction of its closest SF Symbol: natural
proportions, one stroke weight, few essential details, solid counters.
"""

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
    ring, soften = api['ring'], api['soften']
    drawings, overrides = api['DRAWINGS'], api['STYLE_OVERRIDES']

    def cut(body, detail):
        return api['op'](body, detail, api['po'].PathOp.DIFFERENCE)

    def inside(detail, body):
        return api['op'](detail, body, api['po'].PathOp.INTERSECTION)

    def ellipse(cx, cy, rx, ry):
        return circle(0, 0, 1).transform(rx, 0, 0, ry, cx, cy)

    def gap(p, width=1.8):
        # Clearance zone of about 0.9 u around a foreground part.
        return union(p, stroke(p, width, exact=True))

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
    ball_rim = stroke(ball)

    def ball_icon(name, seams, tags):
        # Meet the center of the rim. Its stroke masks every seam endpoint.
        shape(name, ball, inside(seams, ball), tags)

    # SF soccerball: a solid central pentagon and five solid edge patches
    # cut by the rim; no stitching. Solid punches the same panels out.
    center_patch = api['poly']([(8 + 2.55*math.sin(i*math.tau/5), 8.1 - 2.55*math.cos(i*math.tau/5))
                                for i in range(5)])
    edge_patch = path('M8 4.15L6.05 2.95L5.75 .9H10.25L9.95 2.95Z')
    patches = union(center_patch, *(turn(edge_patch, i*72, dy=.1) for i in range(5)))
    ball_icon('soccer-ball', patches, 'football soccer pentagon pitch team sport')
    overrides['soccer-ball'] = {'solid': cut(union(ball, ball_rim), inside(patches, cut(ball, ball_rim)))}
    # SF basketball: the seams are tilted, not a level cross.
    side_seam = stroke('M3.35 3.65Q8.35 8 3.35 12.35')
    ball_icon('basketball', turn(union(side_seam, mirror(side_seam),
                                       lines('M8 1.8V14.2', 'M1.8 8H14.2')), -28),
              'basketball hoop court dribble team sport')
    # Two facing seams, each with a row of short stitches on its outer side.
    seam = stroke('M4.95 2.75Q7.55 8 4.95 13.25')
    stitches = union(*(line((x, y), (x - 1.35, y + dy)) for x, y, dy in
                       ((5.85, 5.1, -.45), (6.35, 8, 0), (5.85, 10.9, .45))))
    half = union(seam, stitches)
    ball_icon('baseball', turn(union(half, turn(half, 180)), 30),
              'baseball stitching pitch bat diamond sport')
    felt = stroke('M1.95 8.8C6.7 8.8 8.8 5.65 8.8 1.95')
    ball_icon('tennis-ball', union(felt, turn(felt, 180)), 'tennis felt seam racket court sport')
    # SF american.football: pointed ball on a diagonal, a lace row with
    # stitches and a stripe near each tip.
    leather = path('M1.25 8C3.4 2.35 12.6 2.35 14.75 8C12.6 13.65 3.4 13.65 1.25 8Z')
    lacing = lines('M5.4 8H10.6', 'M6.3 6.85V9.15', 'M8 6.85V9.15', 'M9.7 6.85V9.15',
                   'M3.6 5.55Q4.6 8 3.6 10.45', 'M12.4 5.55Q11.4 8 12.4 10.45')
    shape('american-football', turn(leather, -40), inside(turn(lacing, -40), turn(leather, -40)),
          'american football gridiron laces touchdown pigskin sport')
    # SF cricket.ball: a straight double seam band across the diagonal.
    cricket_seam = union(lines('M1 6.25H15', 'M1 9.75H15'),
                         *(line((x, 8), (x + .75, 8)) for x in (1.6, 3.85, 6.1, 8.35, 10.6, 12.85)))
    ball_icon('cricket-ball', turn(cricket_seam, -45), 'cricket leather seam bowling bat sport')

    # SF tennis.racket: strung oval head on the upper right, a long throat
    # and a thick grip running down to the lower left.
    hoop = ellipse(8, 5.0, 3.55, 3.85)
    throat = stroke('M5.2 7.55L8 10.9L10.8 7.55M8 10.9V12.4')
    grip = rr(7.05, 12.0, 1.9, 4.0, .95)
    strings = inside(lines('M6.75 1.0V9.35', 'M9.25 1.0V9.35', 'M4.3 3.75H11.7', 'M4.3 6.25H11.7'), hoop)
    object_icon('tennis-racket', turn(hoop, 42, dx=1.0, dy=-1.0), turn(strings, 42, dx=1.0, dy=-1.0),
                'tennis racquet strings handle court sport', turn(union(throat, grip), 42, dx=1.0, dy=-1.0))
    # SF skateboard: the deck from above on a diagonal, with its trucks'
    # wheels showing at both ends and two bolt pairs on the deck.
    deck = rr(5.35, .6, 5.3, 14.8, 2.65)
    wheels = union(*(rr(x, y, 1.35, 2.3, .65, exact=True) for x in (3.55, 11.1) for y in (2.75, 10.95)))
    bolts = union(*(circle(x, y, .45) for x in (7.2, 8.8) for y in (3.35, 4.65, 11.35, 12.65)))
    shape('skateboard', turn(deck, 45), turn(union(wheels, bolts), 45),
          'skate deck wheels board skatepark sport')

    # SF skis: a parallel pair on the diagonal, each with one binding.
    ski = rr(4.1, .45, 2.9, 15.1, 1.45)
    ski_pair = union(ski, turn(ski, dx=4.9))
    bindings = lines('M5.55 7.25V8.75', 'M10.45 7.25V8.75')
    object_icon('skis', turn(ski_pair, 45), turn(bindings, 45),
                'ski pair alpine snow winter downhill bindings')
    board = path('M5.4 3.8C5.4 .2 10.6 .2 10.6 3.8Q10.1 8 10.6 12.2'
                 'C10.6 15.8 5.4 15.8 5.4 12.2Q5.9 8 5.4 3.8Z')
    straps = lines('M7.2 5.35H8.8', 'M7.2 10.65H8.8')
    object_icon('snowboard', turn(board, 45), turn(straps, 45),
                'snowboard snow bindings mountain winter sport')
    # SF surfboard: a long pointed board with its stringer, on the diagonal.
    surf = path('M8 .35C11.35 3.45 11.4 11.75 9.1 15.25Q8 15.75 6.9 15.25'
                'C4.6 11.75 4.65 3.45 8 .35Z')
    shape('surfboard', turn(surf, 45), turn(line((8, 3.35), (8, 12.85)), 45),
          'surf board ocean wave surfing beach water sport')
    blade = path('M6.2 2.2Q8 1.45 9.8 2.2L9.45 7.05Q9.35 7.9 8 9.05'
                 'Q6.65 7.9 6.55 7.05Z')
    shaft = lines('M8 8.9V14.15', 'M6.95 14.15H9.05')
    shape('oar', turn(blade, 42), turn(shaft, 42), 'oar paddle rowing boat canoe water sport')

    # SF sportscourt: a pitch with halfway line, centre circle and spot,
    # and a goal box on each end line.
    court = rr(1.17, 2.95, 13.66, 10.1)
    court_lines = union(lines('M8 2.95V13.05', 'M1.17 5.75H3.6V10.25H1.17',
                              'M14.83 5.75H12.4V10.25H14.83'),
                        ring(8, 8, 2.3), circle(8, 8, .6))
    shape('sports-court', court, court_lines, 'court tennis net field lines game sport')
    # SF helmet: a vented cycling shell with a short peak and a chin strap.
    shell = path('M1.9 10.15C1.55 5.55 4.75 2.55 8.75 2.55C12.35 2.55 14.6 5.0 14.45 8.4'
                 'Q14.35 10.15 12.75 10.15Z')
    vents = lines('M6.05 3.25L6.55 5.05', 'M8.75 2.75V4.7', 'M11.4 3.2L10.95 5.05')
    strap = stroke('M5.3 10.15L8.15 13.65L11.15 10.15')
    peak = line((1.35, 10.15), (4.1, 10.15))
    shape('helmet', shell, union(vents, strap, peak),
          'helmet cycling protective headgear safety bike sport')

    api['CATEGORY'] = 'Home and food'
    # SF fireplace: a mantel slab over a surround whose opening reaches the
    # hearth, with the flame standing inside the open firebox.
    slab = rr(.95, 1.95, 14.1, 1.85, .6, exact=True)
    surround = union(slab, rr(1.95, 3.0, 12.1, 10.85, .9, exact=True))
    opening = rr(4.65, 6.25, 6.7, 7.6, .9, exact=True)
    firebox = cut(surround, union(opening, rr(4.65, 10, 6.7, 6, 0)))
    flame = path('M8 7.75Q8.45 9.0 9.35 9.85C10.8 11.4 10.0 13.0 8.0 13.0'
                 'C6.0 13.0 5.3 11.4 6.55 10.05Q7.35 9.25 8 7.75Z')
    shape('fireplace', firebox, flame, 'hearth mantel fire heating living room chimney')

    # SF humidifier: a domed cone body, a seam line and a round control.
    humid = path('M6.25 1.85H9.75Q10.65 1.85 11.15 2.75L13.35 7.75Q13.85 8.95 13.85 10.25'
                 'Q13.85 13.75 10.35 13.75H5.65Q2.15 13.75 2.15 10.25Q2.15 8.95 2.65 7.75'
                 'L4.85 2.75Q5.35 1.85 6.25 1.85Z')
    knob = ring(8, 9.35, 1.55)
    seam_line = cut(line((2.15, 9.35), (13.85, 9.35)), circle(8, 9.35, 2.45))
    shape('humidifier', humid, union(knob, seam_line, circle(8, 9.35, .5)),
          'humidity mist steam vaporiser vaporizer climate air appliance')
    # SF dehumidifier: a tall unit with grille slots, standing on feet,
    # and a water drop set into its upper corner behind a clearance gap.
    unit = rr(1.85, 2.85, 8.9, 10.55)
    slots = lines('M4.1 7.85H5.6', 'M7.0 7.85H8.5', 'M4.1 9.85H5.6', 'M7.0 9.85H8.5',
                  'M4.1 11.85H5.6', 'M7.0 11.85H8.5')
    feet = lines('M3.6 13.4V14.55', 'M9.0 13.4V14.55')
    drop = path('M11.75 .95Q14.65 4.4 14.65 5.85A2.9 2.9 0 0 1 8.85 5.85Q8.85 4.4 11.75 .95Z')
    api['corner_mark']('dehumidifier', unit, union(slots, feet), drop, gap(drop), return_edge=True)
    drawings['dehumidifier'] = drawings['dehumidifier'][:4] + (
        'humidity dry moisture extraction climate air appliance',)

    # SF sensor: a soft square unit with three vertical vents that
    # broadcasts two arcs to its right.
    detector = rr(1.25, 3.0, 9.75, 10.0, 2.35, exact=True)
    vents = lines('M4.35 6.35V9.65', 'M6.12 6.35V9.65', 'M7.9 6.35V9.65')
    radio = lines('M12.55 5.65Q13.75 8 12.55 10.35', 'M14.4 4.1Q16.25 8 14.4 11.9')
    shape('home-sensor', detector, union(vents, radio),
          'home sensor motion detector occupancy automation wireless')

    # An elbow pipe ending in SF's flange blocks.
    elbow = path('M3.15 3.25H6.25V7.2Q6.25 9.45 8.5 9.45H12.7V12.6H8.5'
                 'C5.05 12.6 3.15 10.65 3.15 7.2Z')
    flanges = union(rr(1.95, 1.5, 5.5, 2.3, .65, exact=True),
                    rr(12.15, 8.25, 2.3, 5.55, .65, exact=True))
    shape('pipe', union(elbow, flanges), None, 'plumbing elbow water drain tube fitting')

    # SF roman.shade.closed: a headrail over three stacked folds, with the
    # beaded cord and its pull hanging at the side.
    headrail = line((3.95, 2.05), (14.55, 2.05))
    folds = union(*(rr(3.95, y, 10.6, 2.75, .7, exact=True) for y in (3.95, 7.4, 10.85)))
    cord = union(*(circle(2.05, y, .55) for y in (2.05, 3.85, 5.65)), rr(1.4, 7.25, 1.3, 3.6, .65))
    glyph('roman-shade', union(headrail, folds), cord,
          'roman shade blind window fabric pleat drawstring')
    cupboard = rr(3.35, 1.4, 9.3, 12.45)
    doors = line((8, 1.4), (8, 13.85))
    knobs = union(circle(6.75, 7.6, .55), circle(9.25, 7.6, .55))
    object_icon('cabinet', cupboard, union(doors, knobs), 'cabinet cupboard wardrobe doors furniture storage',
                lines('M4.6 13.85V14.65', 'M11.4 13.85V14.65'))
    # SF sink: a rim wider than the bowl, a gooseneck spout and two taps.
    basin = path('M2.35 8.55H13.65V10.35Q13.65 13.75 10.25 13.75H5.75'
                 'Q2.35 13.75 2.35 10.35Z')
    rim_line = line((1.3, 8.55), (14.7, 8.55))
    tap = union(stroke('M8 8.55V4.0Q8 2.4 9.6 2.4Q11.2 2.4 11.2 4.0V4.8'),
                lines('M4.75 8.55V6.15', 'M3.85 6.15H5.65'))
    shape('sink', basin, union(rim_line, tap), 'sink washbasin faucet tap kitchen bathroom plumbing')
    # SF stairs: one open stepped line rising to the upper right.
    glyph('stairs', stroke('M2.3 13.65V10.95H5.15V8.25H8.0V5.55H10.85V2.85H13.7'), None,
          'stairs steps staircase floor climb architecture')

    api['CATEGORY'] = 'Devices and connectivity'
    # SF hifireceiver: a wide low chassis with two knobs flanking a solid
    # display, on short feet.
    receiver = rr(1.17, 4.3, 13.66, 6.75)
    panel = union(circle(3.95, 7.65, 1.05), circle(12.05, 7.65, 1.05),
                  rr(5.95, 6.75, 4.1, 1.8, .45, exact=True))
    object_icon('hifi-receiver', receiver, panel, 'hifi stereo audio tuner receiver volume home theater',
                lines('M3.3 11.05V11.95', 'M12.7 11.05V11.95'))
    # SF av.remote: a slim handset with a keypad of dots and a rocker.
    remote = rr(4.8, .95, 6.4, 14.1, 2.0, exact=True)
    keypad = union(*(circle(x, y, .5) for x in (6.7, 8, 9.3) for y in (3.55, 5.15, 6.75, 8.35)))
    rockers = union(rr(6.15, 10.05, 1.3, 3.1, .65), rr(8.55, 10.05, 1.3, 3.1, .65))
    shape('av-remote', remote, union(keypad, rockers), 'remote control av television media buttons handset')
    # SF web.camera: a round camera head on a short neck and foot.
    head = circle(8, 5.95, 4.6)
    lens = union(ring(8, 5.95, 2.35), circle(8, 5.95, .7))
    stand = union(line((8, 11.1), (8, 13.65)), line((5.3, 13.85), (10.7, 13.85)))
    object_icon('web-camera', head, lens, 'webcam video conference camera streaming lens desktop', stand)

    api['CATEGORY'] = 'Health and fitness'
    # SF blood.pressure.cuff: a cylindrical cuff, its hose and the bulb.
    cuff = path('M5.1 3.45Q5.1 1.65 9.55 1.65Q14 1.65 14 3.45V10.05'
                'Q14 11.85 9.55 11.85Q5.1 11.85 5.1 10.05Z')
    band = stroke('M5.1 3.45Q5.1 5.25 9.55 5.25Q14 5.25 14 3.45')
    hose = stroke('M5.1 8.25Q2.4 8.25 2.4 10.35Q2.4 11.55 3.15 12.25')
    bulb = ellipse(0, 0, .95, 1.55).transform(.707, -.707, .707, .707, 4.05, 13.15)
    object_icon('blood-pressure-cuff', cuff, band,
                'blood pressure cuff sphygmomanometer monitor arm pump hypertension', union(hose, bulb))
    # SF inhaler: the canister sits in a boot leaning to the right.
    inhaler = path('M3.65 2.1H8.5L8.95 8.95H12.95V13.45H5.5Q4.25 13.45 4.15 12.15Z')
    object_icon('inhaler', turn(inhaler, 20), turn(lines('M3.85 5H8.65', 'M10.7 8.95V13.45'), 20),
                'inhaler asthma medication respiratory breathing mouthpiece')
    # SF cross.vial proportions: a separate cap over a shouldered bottle.
    cap = rr(5.25, .9, 5.5, 2.35, .65, exact=True)
    glass = path('M6.0 4.15H10.0V5.0Q12.0 5.6 12.0 7.6V13.05Q12.0 14.85 10.2 14.85H5.8'
                 'Q4.0 14.85 4.0 13.05V7.6Q4.0 5.6 6.0 5.0Z')
    object_icon('vial', glass, api['plus'](8, 9.85, .62),
                'vial sample medicine ampoule liquid laboratory glass', cap)
    shield = drawings['shield'][0]
    # Six equal arms radiate from the medical emblem's center.
    arm = line((8, 5.05), (8, 10.95))
    star = turn(union(arm, turn(arm, 60), turn(arm, -60)), dy=-.35)
    shape('star-of-life-shield', shield, star, 'star of life emergency medical services ems rescue shield')

    api['CATEGORY'] = 'Finance and commerce'
    # SF sunglasses: a wide, low browline frame with two soft lenses.
    lens = path('M.65 5.15H7.0L6.75 7.3C6.45 10.85 1.75 10.85 1.25 7.6Z')
    bridge = stroke('M7.0 5.75Q8 4.95 9.0 5.75')
    shape('sunglasses', union(lens, mirror(lens)), bridge, 'sunglasses shades eyewear lenses sun fashion')

    api['CATEGORY'] = 'Home and food'
    # SF comb: a spine and evenly spaced teeth, laid on the diagonal.
    spine = rr(.8, 3.9, 14.4, 3.0, .85, exact=True)
    teeth = union(*(line((x, 6.9), (x, 12.15)) for x in (1.75, 4.05, 6.35, 8.65, 10.95, 13.25)))
    shape('comb', turn(spine, -40), turn(teeth, -40), 'comb hair teeth grooming styling barber')

    # SF stroller: hood over the bassinet, push handle behind, two wheels.
    carriage = path('M14.25 7.55C14.1 4.45 11.95 2.15 8.95 2.05L8.35 7.55H3.25'
                    'Q3.95 11.1 7.45 11.1H9.65Q13.1 11.1 14.25 7.55Z')
    handle = stroke('M3.5 8.05L2.3 5.05H1.4M5.6 11.1L4.95 12.0M10.6 11.1L11.25 12.0')
    axle = union(ring(4.65, 13.45, 1.3), ring(11.6, 13.45, 1.3))
    object_icon('stroller', carriage, line((14.25, 7.55), (8.35, 7.55)),
                'stroller pram pushchair carriage baby wheels', union(handle, axle))

    # SF teddybear: ears, a head with eyes and muzzle, round body and feet.
    ear = circle(4.25, 2.85, 1.55)
    foot = circle(5.25, 12.6, 2.0)
    bear = union(ear, mirror(ear), circle(8, 5.3, 3.75),
                 circle(8, 10.6, 3.35), foot, mirror(foot))
    face = union(circle(6.55, 4.85, .55), circle(9.45, 4.85, .55),
                 ring(8, 6.65, 1.25), circle(8, 6.35, .45))
    shape('teddy-bear', bear, face, 'teddy bear plush stuffed animal toy nursery')
    # SF waterbottle: a separate cap over a narrow bottle with a label
    # band carrying a drop.
    bottle_cap = rr(5.85, .75, 4.3, 2.35, .65, exact=True)
    bottle = path('M6.0 3.95H10.0Q11.05 4.45 11.05 6.05V13.4Q11.05 15.2 9.25 15.2H6.75'
                  'Q4.95 15.2 4.95 13.4V6.05Q4.95 4.45 6.0 3.95Z')
    label = union(lines('M4.95 7.05H11.05', 'M4.95 12.3H11.05'),
                  path('M8 8.05Q9.2 9.5 9.2 10.15A1.2 1.2 0 0 1 6.8 10.15Q6.8 9.5 8 8.05Z'))
    object_icon('water-bottle', bottle, label, 'water bottle drink flask refill hydration canteen', bottle_cap)

    api['CATEGORY'] = 'Product tools'
    # SF level: a long low beam whose vial sits in a U notch on top.
    level_body = rr(1.17, 5.0, 13.66, 5.9)
    notch = stroke('M5.75 5.0V6.0Q5.75 8.25 8 8.25Q10.25 8.25 10.25 6.0V5.0')
    object_icon('level', level_body, union(notch, circle(8, 6.15, .6)),
                'spirit level bubble vial horizontal carpenter construction tool')
    plate, keeper = rr(1.6, 4.6, 7.8, 6.8), rr(12, 5.1, 2.4, 5.8)
    bolt = stroke('M4.45 6.65V8H14.15')
    shape('latch', union(plate, keeper), bolt, 'latch sliding bolt door gate lock hardware')
    # The keeper anchors the rod; the cut around the lever exposes its travel.
    lever_slot = union(bolt, stroke(bolt, 2.1))
    overrides['latch'] = {'solid': union(cut(union(plate, stroke(plate)), lever_slot),
                                         keeper, stroke(keeper), bolt)}

    api['CATEGORY'] = 'Media and communication'
    # SF pianokeys: the standard rectangle; black keys hang from the top
    # edge and white-key divisions run from them to the bottom.
    keyboard = rr(1.17, 2.8, 13.66, 10.4)
    whites = [1.17 + i*13.66/5 for i in range(1, 5)]
    black_keys = union(*(rr(x - .95, 2.4, 1.9, 6.15, .5, exact=True) for i, x in enumerate(whites) if i != 2))
    divisions = union(*(line((x, 8.0 if i != 2 else 2.8), (x, 13.2)) for i, x in enumerate(whites)))
    shape('piano-keys', keyboard, union(inside(black_keys, keyboard), divisions),
          'piano keys keyboard ivory music instrument octave')
    field = union(keyboard, stroke(keyboard))
    interior = cut(keyboard, stroke(keyboard))
    overrides['piano-keys'] = {'solid': cut(field, inside(union(divisions, stroke(black_keys)), interior))}

    # SF amplifier: a carry handle, a control strip of knobs, open grille.
    cabinet = rr(1.35, 3.6, 13.3, 10.55)
    amp_handle = stroke('M5.65 3.6V2.85Q5.65 1.85 6.65 1.85H9.35Q10.35 1.85 10.35 2.85V3.6')
    amp_knobs = union(*(circle(x, 5.85, .6) for x in (4.1, 6.55, 9.0, 11.45)),
                      line((1.35, 7.85), (14.65, 7.85)))
    object_icon('amplifier', cabinet, amp_knobs, 'amplifier guitar amp speaker cabinet grille audio gain', amp_handle)
    # SF tuningfork: tines to the upper right, a ball on the handle.
    fork = stroke('M5.6 .9V5.6A2.4 2.4 0 0 0 10.4 5.6V.9')
    stem = union(line((8, 8.0), (8, 13.6)), circle(8, 14.15, 1.05))
    glyph('tuning-fork', turn(fork, 45, dx=.35, dy=-.35), turn(stem, 45, dx=.35, dy=-.35),
          'tuning fork pitch reference resonance music instrument')

    api['CATEGORY'] = 'Work and education'
    # SF rosette: a medal disc above a solid swallow-tailed ribbon.
    medal = circle(8, 5.85, 4.55)
    ribbon = path('M5.1 9.0H10.9V14.15Q10.9 14.95 10.2 14.55L8 13.15L5.8 14.55'
                  'Q5.1 14.95 5.1 14.15Z')
    tails = cut(ribbon, circle(8, 5.85, 4.55 + .52 + .9))
    shape('rosette', medal, tails, 'rosette award prize ribbon cockade merit winner')

    # SF laurel: solid leaves alternating along a curved stem; two
    # branches face each other to form the wreath.
    stem = stroke('M6.6 14.35C3.6 12.6 2.25 8.85 3.6 3.45')
    leaf = ellipse(0, 0, .72, 1.6)

    def leaf_at(x, y, angle):
        a = math.radians(angle)
        return leaf.transform(math.cos(a), math.sin(a), -math.sin(a), math.cos(a), x, y)

    leaves = union(leaf_at(3.85, 2.0, 15), leaf_at(1.65, 5.4, -40), leaf_at(4.85, 6.35, 35),
                   leaf_at(1.7, 9.4, -60), leaf_at(5.35, 10.1, 50), leaf_at(3.45, 12.7, -75))
    branch = union(stem, leaves)
    glyph('laurel', union(branch, mirror(branch)), None,
          'laurel wreath leaves victory honor award champion')

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
    # SF magazine: an upright cover with a solid masthead block, and the
    # pages behind it showing along the right and bottom edges.
    cover = rr(2.25, 1.3, 9.05, 12.35)
    pages = stroke('M11.3 2.85H12.2Q13.55 2.85 13.55 4.2V13.35Q13.55 14.7 12.2 14.7H4.95'
                   'Q3.6 14.7 3.6 13.65')
    masthead = rr(4.0, 3.15, 5.55, 2.55, .5, exact=True)
    object_icon('magazine', cover, masthead, 'magazine periodical publication issue reading cover', pages)

    # SF greetingcard and menucard share one folded card: the front leaf
    # and the back leaf rising behind it on the right.
    leaf_front = rr(2.0, 2.65, 9.4, 12.0)
    leaf_back = stroke('M11.4 3.35L12.75 2.0Q13.85 1.2 13.85 2.6V11.65'
                       'Q13.85 12.45 13.15 12.95L11.4 14.2')
    heart = path('M6.7 11.55L4.85 9.75C3.55 8.45 5.45 6.85 6.7 8.35'
                 'C7.95 6.85 9.85 8.45 8.55 9.75Z')
    object_icon('greeting-card', leaf_front, heart, 'greeting card birthday invitation wishes folded heart', leaf_back)
    text_rows = lines('M4.4 6.15H9.0', 'M4.4 8.65H9.0', 'M4.4 11.15H7.4')
    object_icon('menu-card', leaf_front, text_rows, 'menu card restaurant food dining courses list', leaf_back)

    api['CATEGORY'] = 'Finance and commerce'
    # SF giftcard: the standard card with a ribbon cross and a bow.
    card = rr(1.17, 2.8, 13.66, 10.4)
    ribbon = lines('M7.2 2.8V13.2', 'M1.17 8.6H14.83')
    loop = stroke('M7.2 8.6Q3.85 8.6 3.85 6.6C3.85 4.65 6.35 4.85 7.2 8.6')
    bow = union(loop, turn(mirror(loop), dx=-1.6), stroke('M7.2 8.6L5.35 11.0M7.2 8.6L9.05 11.0'))
    object_icon('gift-card', card, union(ribbon, bow), 'gift card voucher prepaid present ribbon shopping')

    api['CATEGORY'] = 'Work and education'
    chair = rr(4.9, 1.65, 6.2, 4.05)
    desktop = rr(1.55, 7.9, 12.9, 2.55)
    legs = lines('M4.35 10.45L3.35 14.35', 'M11.65 10.45L12.65 14.35')
    shape('student-desk', union(chair, desktop), union(legs, line((8, 5.7), (8, 7.9))),
          'school classroom desk chair student furniture education')

    api['CATEGORY'] = 'Finance and commerce'
    # SF coat: long body with lapels, a front edge and two buttons.
    overcoat = path('M5.85 2.15H10.15L12.05 3.05L14.4 10.65L12.05 11.35L10.95 7.85'
                    'L11.45 14.15H4.55L5.05 7.85L3.95 11.35L1.6 10.65L3.95 3.05Z')
    lapels = union(lines('M5.85 2.15L6.2 4.4L8 6.95L9.8 4.4L10.15 2.15', 'M8 6.95V14.15'),
                   circle(9.35, 9.0, .55), circle(9.35, 11.5, .55))
    object_icon('coat', overcoat, lapels, 'overcoat long coat lapel formal winter outerwear clothing')
    # SF jacket: collar, centre zip and two slanted pockets.
    bomber = path('M5.45 2.75Q8 3.65 10.55 2.75L12.45 4L14.55 10.65L12.35 11.55'
                  'L10.85 8.25L11.3 13.25Q8 14.05 4.7 13.25L5.15 8.25'
                  'L3.65 11.55L1.45 10.65L3.55 4Z')
    zipper = lines('M8 4.6V13.65', 'M5.45 2.75L6.15 5.95L8 4.6L9.85 5.95L10.55 2.75',
                   'M5.35 9.75L6.55 10.65', 'M10.65 9.75L9.45 10.65')
    object_icon('jacket', bomber, zipper, 'jacket collar zip bomber sleeves outerwear clothing')

    api['CATEGORY'] = 'Maps and travel'
    # SF duffle.bag: a barrel bag with end panels, two straps and the
    # carry handle joining them over the top.
    barrel = rr(1.17, 5.0, 13.66, 8.85, 2.6, exact=True)
    panels = lines('M3.75 5.0V13.85', 'M12.25 5.0V13.85')
    duffle_handle = stroke('M6.4 5.0V3.6Q6.4 2.35 7.65 2.35H8.35Q9.6 2.35 9.6 3.6V5.0')
    object_icon('duffle-bag', barrel, union(panels, lines('M6.4 5.0V13.85', 'M9.6 5.0V13.85')),
                'duffel duffle travel luggage overnight holdall straps', duffle_handle)
    # The gym bag shares the barrel, with a zipped top and an end pocket.
    gym_handle = stroke('M5.6 5.0V4.05A2.4 2.4 0 0 1 10.4 4.05V5.0')
    pocket = union(line((3.95, 5.0), (3.95, 13.85)), line((3.95, 7.55), (14.83, 7.55)))
    object_icon('gym-bag', barrel, pocket, 'gym bag kit locker workout training sports pocket', gym_handle)

    api['CATEGORY'] = 'Devices and connectivity'
    # SF faxmachine: paper rising from the back, a keypad grid and the
    # output slot on the front.
    fax = rr(1.35, 5.2, 13.3, 9.2)
    paper = stroke('M4.35 5.2V1.85H11.65V5.2')
    fax_keys = union(*(circle(x, y, .55) for x in (4.1, 6.05, 8.0, 9.95, 11.9) for y in (7.6, 9.4)))
    tray = line((4.85, 11.95), (11.15, 11.95))
    object_icon('fax-machine', fax, union(fax_keys, tray), 'fax facsimile telephone office paper keypad', paper)
    base = path('M3.95 7.4H12.05L14.4 10.65V13.45H1.6V10.65Z')
    lid = stroke('M3.95 7.4L2.05 2.85H13.95L12.05 7.4')
    object_icon('scanner', base, union(line((1.6, 10.65), (14.4, 10.65)), line((10.95, 12.05), (12.35, 12.05))),
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
