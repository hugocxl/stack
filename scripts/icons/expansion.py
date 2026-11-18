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
    shape('syringe',
          path('M4 6L8 2L13 7L9 11Z'),
          union(lines('M3 5L10 12M7.7 2L13.3 7.6M10.5 4.8L12.5 2.8M11.2 1.5L13.8 4.1M6.5 8.5L1.5 13.5'),
                stroke('M7 5L9 7', 1.1)),
          'injection vaccine medicine needle treatment')
    shape('ambulance',
          path('M1.5 4H9V6H12L14.5 9V12H1.5Z'),
          union(plus(5.2, 7.6, .7), stroke('M9 6V9H14.5', 1.1),
                circle(4, 12, 1.5), circle(12, 12, 1.5), line((4, 2), (6, 2), width=1.1)),
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
    shape('cat',
          path('M2 7V2L6 4Q8 3 10 4L14 2V7Q15 13.5 8 14Q1 13.5 2 7Z'),
          union(dots((5.5, 7.5), (10.5, 7.5), r=.6),
                poly([(7, 9.5), (9, 9.5), (8, 10.5)]),
                stroke('M8 10.5V11.5M4 10L1 9M12 10L15 9', 1.05)),
          'animal feline pet kitten')
    cat_body = api['DRAWINGS']['cat'][0]
    cat_face = union(dots((5.5, 7.5), (10.5, 7.5), r=.7),
                     path('M6.85 9.55Q8 9.1 9.15 9.55Q8.95 10.5 8 10.9Q7.05 10.5 6.85 9.55Z'))
    api['STYLE_OVERRIDES']['cat'] = {'solid': api['op'](
        union(cat_body, stroke(cat_body, 1.25)), cat_face, api['po'].PathOp.DIFFERENCE)}
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
          stroke('M4.1 9.2Q6.2 12.4 9 12.1M3 3L4 1.5', 1.1),
          'fruit food tropical produce')
    shape('cherry', union(circle(4.2, 11.4, 2.65), circle(11.8, 10.1, 2.55)),
          stroke('M4.2 8.75Q4.8 5.1 8 3Q8.8 5.9 11.8 7.55M8 3Q11 1 13 2Q11 5 8 3', 1.1),
          'fruit food cherries produce')
    # A right-triangular cut face, with a gently scalloped lettuce edge
    # visible between the bread and the lower crust.
    sandwich = path('M2.05 8.65L10.65 2.5Q11.35 2.05 11.85 2.9L14.3 7.65'
                    'Q14.55 8.1 14.35 8.7L14.2 11.6Q14.1 12.2 13.35 12.35'
                    'L2.75 13.55Q1.7 13.65 1.7 12.7V9.5Q1.7 8.95 2.05 8.65Z')
    filling = stroke('M1.85 9.1L14.3 7.95M1.75 11.25Q3.05 10.55 4.2 11.35'
                     'Q5.25 12.05 6.4 10.95Q7.4 10 8.65 10.65Q9.75 11.3 10.9 10.25'
                     'Q12 9.35 13.05 9.95L14.3 9.85', 1.05)
    shape('sandwich', sandwich, filling, 'food bread snack lunch')
    shape('cookie',
          path('M9.5 1.5Q9 4 11 4Q10.5 6.5 14 6Q16 12 11 14Q4 17 1.5 10Q0 4 5 2Q7 1 9.5 1.5Z'),
          dots((5, 5.5), (4, 9.5), (8, 8), (9.5, 12), (12, 9), r=.7),
          'food biscuit snack browser cookie')
    shape('ice-cream-cone',
          union(path('M3.7 7.4H12.3L8 14.5Z'),
                path('M3 8Q1.5 5.5 4 4Q4 1 8 1Q12 1 12 4Q14.5 5.5 13 8Z')),
          stroke('M3 8H13M6.35 9.9L9.1 11.2', 1.1),
          'dessert icecream frozen cone sweet')
    shape('door-closed', rr(3, 1.5, 10, 13, .7),
          union(line((1.5, 14.5), (14.5, 14.5)), circle(10.5, 8, .65)),
          'door entrance room closed')
    shape('bath', path('M1.5 8H14.5L13 12Q12.5 13 11 13H5Q3.5 13 3 12Z'),
          lines('M3 8V3Q3 1 5 1Q7 1 7 3M5 13V15M11 13V15M1 8H15'),
          'bathtub bathroom wash bathing')
    shape('toilet',
          path('M2.2 2.2H6V7H14Q13.9 10.5 10.1 11.4L10.7 13.8H5.2L6.1 11.4Q3 10.5 3 8.5H2.2Z'),
          stroke('M3 8.5V7H6M3.7 4.3H4.6', 1.15),
          'bathroom restroom lavatory sanitation')
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
          None,
          'tool construction repair carpentry build')
    shape('construction', rr(1.5, 5, 13, 5, .8),
          lines('M4 5L7 10M9 5L12 10M4 10V14M12 10V14'),
          'barrier work roadworks construction maintenance')

    assert all(name in api['DRAWINGS'] for name in NAMES)
