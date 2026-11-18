"""Original November 2026 coverage slice.

Register into draw.py's authoring API before export. All coordinates are authored
for this family's 16-unit canvas; no reference-library paths are imported.
"""


NAMES = (
    'calculator', 'piggy-bank', 'scale', 'id-card', 'ear', 'ear-off',
    'syringe', 'ambulance', 'baby', 'backpack', 'binoculars',
    'cat', 'dog', 'bird', 'rabbit', 'carrot', 'banana', 'cherry', 'sandwich',
    'cookie', 'ice-cream-cone', 'door-closed', 'bath', 'toilet',
    'washing-machine', 'refrigerator', 'hammer', 'construction', 'anchor',
)


def register(api):
    """Add the slice through the shared geometry and catalog helpers."""
    shape = api['shape']
    glyph = api['glyph']
    path = api['path']
    rr = api['rr']
    circle = api['circle']
    line = api['line']
    lines = api['lines']
    stroke = api['stroke']
    union = api['union']
    poly = api['poly']
    dots = api['dots']
    plus = api['plus']

    api['CATEGORY'] = 'Finance and commerce'
    shape('calculator', rr(3, 1.5, 10, 13, 1.5),
          union(stroke(rr(5, 3.5, 6, 3, .5), 1.1),
                dots((5.5, 9), (10.5, 9), (5.5, 12), (10.5, 12), r=.7)),
          'arithmetic accounting calculate keypad')
    shape('piggy-bank',
          path('M3 6Q4 4 7 4L9 2.5L10.5 4.5Q12 5 13 7H14.5V10H13L12 12V14H10V12.5H6V14H4V12Q1.5 11 1.5 8.5Q1.5 7 3 6Z'),
          union(line((5.5, 6), (8.5, 6), width=1.1), circle(11, 7.5, .55),
                stroke('M2 7Q.5 6 .8 4.5', 1.1)),
          'savings money reserve deposit')
    shape('scale',
          union(path('M1.45 8H5.55Q5.55 10.6 3.5 10.6Q1.45 10.6 1.45 8Z'),
                path('M10.45 8H14.55Q14.55 10.6 12.5 10.6Q10.45 10.6 10.45 8Z')),
          lines('M8 2V14M5 14H11M2.5 4H13.5',
                'M3.5 4L1.45 8M3.5 4L5.55 8M12.5 4L10.45 8M12.5 4L14.55 8'),
          'balance justice comparison legal weight')

    api['CATEGORY'] = 'People and accessibility'
    shape('id-card', rr(1.5, 3, 13, 10, 1.7),
          union(circle(5, 6.5, 1.2), stroke('M3 10.5Q3 8.5 5 8.5T7 10.5', 1.1),
                lines('M9.5 6.5H12M9.5 9.5H12')),
          'identity identification membership profile credentials')
    ear = path('M5 12Q5 15 8 14Q10 13.5 10 11Q10 9 12 7.5C15 2 7-1 3.5 3.5Q2 5.5 2.5 8')
    # An ear is an open anatomical contour, not a filled surface. Keep both
    # the outline and the inner fold opaque in every style.
    glyph('ear', stroke(ear), stroke('M6 5Q7 2.5 10 4Q12 6 9 7Q7.5 7.5 8 10', 1.2),
          'hearing audio listen sensory accessibility')
    glyph('ear-off', stroke(ear),
          union(stroke('M6 5Q7 2.5 10 4Q11.7 5.7 9.6 6.85', 1.2), line((2, 2), (14, 14))),
          'hearing deaf muted accessibility')
    shape('baby', circle(8, 8.5, 5.5),
          union(stroke('M8.7 3.05C8.2 4.4 6.1 5.5 5.85 4.3', 1.1),
                dots((6, 8), (10, 8), r=.6), stroke('M6 10.5Q8 12.5 10 10.5', 1.1)),
          'infant childcare newborn family')

    api['CATEGORY'] = 'Health and fitness'
    # Build on the vertical axis and rotate the completed barrel and fittings.
    barrel = rr(6.05, 4.8, 3.9, 6.75)
    fittings = lines('M4.85 4.8H11.15', 'M8 4.8V1.85', 'M6.15 1.85H9.85',
                     'M8 11.55V15', 'M6.05 7.8H7.5')
    shape('syringe', api['transform'](barrel, 45), api['transform'](fittings, 45),
          'injection vaccine medicine needle treatment')
    ambulance = path('M1.55 4H9.1V6H11.8L14.45 8.9V10.65H13.65'
                     'Q12 8.1 10.35 10.65H5.65Q4 8.1 2.35 10.65H1.55Z')
    shape('ambulance', ambulance,
          union(stroke('M9.1 6V8.9H14.45'), plus(5.05, 6.65, .61), line((3.95, 2.05),(6.15, 2.05)),
                circle(4,12.25,1.35),circle(12,12.25,1.35)),
          'emergency paramedic medical vehicle rescue')
    api['CATEGORY'] = 'Maps and travel'
    shape('backpack', rr(3, 4, 10, 10.5, 2.5),
          union(stroke('M5.5 4V2Q8 0 10.5 2V4', 1.1),
                stroke(rr(5, 8, 6, 4.5, 1), 1.1), line((6, 9.5), (10, 9.5), width=1)),
          'bag hiking school luggage travel')
    shape('binoculars',
          union(path('M1.5 12L3.5 4H6.2L7 12Q7 14 4.3 14Q1.5 14 1.5 12Z'),
                path('M9 12L9.8 4H12.5L14.5 12Q14.5 14 11.7 14Q9 14 9 12Z')),
          union(lines('M6.5 7H9.5M7 10H9'),
                stroke('M2 11.5Q4.2 10.3 6.5 11.5M9.5 11.5Q11.8 10.3 14 11.5', 1.1)),
          'watch observe explore search sightseeing')
    glyph('anchor', stroke('M8 4.7V14M4 7H12M1.5 10Q2.5 14 8 14Q13.5 14 14.5 10M1.5 10V12M1.5 10H3.5M14.5 10V12M14.5 10H12.5'),
          stroke(circle(8, 3, 1.6), 1.15),
          'nautical boat harbor mooring sea')

    api['CATEGORY'] = 'Weather and nature'
    cat_head = path('M2.35 6.95V2.3L6.1 4.1Q8 3.3 9.9 4.1L13.65 2.3V6.95'
                    'C14.65 11.9 11.75 14 8 14S1.35 11.9 2.35 6.95Z')
    cat_face = union(dots((5.45, 7.5), (10.55, 7.5), r=.65),
                     poly([(6.95, 9.55), (9.05, 9.55), (8, 10.8)]))
    shape('cat', cat_head, union(cat_face, lines('M1.25 9.45L4.2 10.3',
                                                'M14.75 9.45L11.8 10.3')),
          'animal feline pet kitten')
    cat_body = api['DRAWINGS']['cat'][0]
    api['STYLE_OVERRIDES']['cat'] = {'solid': api['op'](
        union(cat_body, stroke(cat_body)), cat_face, api['po'].PathOp.DIFFERENCE)}
    shape('dog',
          path('M4.8 3.6Q8 1.65 11.2 3.6Q13.5 3.3 14.3 7.3Q14.9 10.7 12.3 9.1Q12.3 13.6 8 13.8Q3.7 13.6 3.7 9.1Q1.1 10.7 1.7 7.3Q2.5 3.3 4.8 3.6Z'),
          union(stroke('M4.8 3.6Q5 6.3 3.7 9.1M11.2 3.6Q11 6.3 12.3 9.1', 1.05),
                dots((6.5, 7), (9.5, 7), r=.55),
                path('M6.5 9.3Q8 8.7 9.5 9.3Q9.6 10.5 8 11Q6.4 10.5 6.5 9.3Z')),
          'animal canine pet puppy')
    shape('bird',
          path('M1.6 7.9L4.9 8.5Q7.7 8 7.9 5Q8.1 2.1 10.7 2.1Q13 2.1 13 4.8L14.4 5.8L13 6.7Q12.8 12.6 8 12.6Q3.5 12.6 1.6 7.9Z'),
          union(circle(11.2, 4.5, .55), stroke('M5.7 9.6Q8 10.8 10.1 7.8M6.6 12.5V14.5M9.4 12.4V14.5', 1.05)),
          'animal avian wildlife songbird')
    shape('rabbit',
          path('M4 7Q2 1 4 1Q6 1 7 6H9Q10 1 12 1Q14 1 12 7Q15 9 13 12Q12 14 8 14Q4 14 3 12Q1 9 4 7Z'),
          union(dots((6, 9), (10, 9), r=.6),
                poly([(7, 11), (9, 11), (8, 12)])),
          'animal bunny pet wildlife')

    api['CATEGORY'] = 'Home and food'
    shape('carrot',
          path('M3 13Q5 5 8 4Q12 3 12 7Q11 10 3 13Z'),
          lines('M9 4L9 1M11 4L14 2M12 6L15 6M7 6L9 8M5 9L6.5 10.5'),
          'vegetable produce food nutrition')
    shape('banana',
          path('M3 3Q4 10 10 10Q12 10 13 8L14 8Q13 15 7 14Q1 13 2 5L3 3Z'),
          stroke('M3.5 7.3Q3.65 12.2 8.5 12.25Q10.75 12.25 12.55 10.05M3 3L4 1.5'),
          'fruit food tropical produce')
    shape('cherry', union(circle(4.2, 11.4, 2.65), circle(11.8, 10.1, 2.55)),
          stroke('M4.2 8.75Q4.65 5.1 7.55 3.55Q8.7 6.15 11.8 7.55M7.55 3.55Q9.2 .8 13.7 1.8Q12.1 5.8 7.55 3.55M7.55 3.55Q5.95 .9 2.25 1.9Q3.95 5.6 7.55 3.55'),
          'fruit food cherries produce')
    # Side elevation: rounded toast above a ruffled lettuce leaf, tomato
    # slices and a folded cheese corner resting on the lower slice.
    toast = path('M1.65 6.45Q1.25 5.8 1.8 5.15C3.5 2.4 5.9 3.15 8 3.35'
                 'C10.45 3.55 12.85 2.8 14.15 4.85Q14.9 5.85 14.35 6.45'
                 'V11.8Q14.35 13.05 13.1 13.05H2.9Q1.65 13.05 1.65 11.8Z')
    layers = lines('M1.65 6.45Q4.1 5.85 7.1 6.45T14.35 6.45',
                   'M1.65 8.35Q3 7.45 4.35 8.45T7 8.45Q8.4 7.3 9.85 8.45T12.35 8.5Q13.4 7.7 14.35 8.35',
                   'M1.65 10.6H6.25L8.35 11.65L10.2 10.6H14.35',
                   'M4.2 8.35Q4.4 9.7 5.65 10.6M11.25 8.95Q11.6 9.95 12.7 10.6')
    shape('sandwich',toast,layers,'food bread snack lunch')
    shape('cookie',
          path('M9.5 1.5Q9 4 11 4Q10.5 6.5 14 6Q16 12 11 14Q4 17 1.5 10Q0 4 5 2Q7 1 9.5 1.5Z'),
          dots((5, 5.5), (4, 9.5), (8, 8), (9.5, 12), (12, 9), r=.7),
          'food biscuit snack browser cookie')
    scoop = path('M2.85 7.55Q2 5.55 4.1 4.25C4.35 .45 11.65 .45 11.9 4.25Q14 5.55 13.15 7.55Z')
    cone = path('M3.5 7.55H12.5L8 14.45Z')
    shape('ice-cream-cone', union(scoop, cone),
          lines('M2.85 7.55H13.15', 'M4.65 9.3L9.25 12.55',
                'M7.85 7.55L11 9.8'), 'dessert icecream frozen cone sweet')
    shape('door-closed', rr(3, 1.5, 10, 13, .7),
          union(line((1.5, 14.5), (14.5, 14.5)), circle(10.5, 8, .65)),
          'door entrance room closed')
    shape('bath', path('M1.5 8H14.5L13 12Q12.5 13 11 13H5Q3.5 13 3 12Z'),
          lines('M3 8V3Q3 1 5 1Q7 1 7 3M5 13V15M11 13V15M1 8H15'),
          'bathtub bathroom wash bathing')
    toilet = path('M2 2H5.65V6.8H14.15Q14 10.1 10.25 11.5L10.75 13.95'
                  'H5.35L6 11.5Q2.85 10.05 2.85 7.1H2Z')
    shape('toilet', toilet, lines('M2.85 6.8H5.65', 'M3.6 9H13.45',
                                  'M6 11.5H10.25'), 'bathroom restroom lavatory sanitation')
    shape('washing-machine', rr(2.5, 1.5, 11, 13, 1.5),
          union(stroke(circle(8, 9.5, 3.2), 1.1),
                stroke('M5 9.5Q6.5 8 8 9.5T11 9.5M2.5 5H13.5', 1.05),
                dots((5, 3.3), (7.5, 3.3), r=.45)),
          'laundry washer appliance clothing cleaning')
    shape('refrigerator', rr(3, 1.5, 10, 13, 1.3),
          lines('M3 6.5H13M5 3.5V4.5M5 9V11'),
          'fridge freezer kitchen appliance cooling')

    api['CATEGORY'] = 'Work and education'
    shape('hammer',
          path('M3 4.8L5.3 2.5L7 4.2Q9.5 2.7 11.7 4.6Q13.5 6.2 14 8.1'
               'Q11.6 6.2 10.1 6.9L9.5 7.6L4 13.8Q3.3 14.6 2.4 13.8L1.9 13.3'
               'Q1.3 12.6 2 11.9L8 6.4L6.1 5.2L4.8 6.5Z'),
          line((7.25, 7.15), (9.05, 8.65)),
          'tool construction repair carpentry build')
    shape('construction', rr(1.5, 5, 13, 5, .8),
          lines('M4 5L7 10M9 5L12 10M4 10V14M12 10V14'),
          'barrier work roadworks construction maintenance')

    assert all(name in api['DRAWINGS'] for name in NAMES)
