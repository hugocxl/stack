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
          union(path('M1.5 8H6.5Q6.5 11 4 11Q1.5 11 1.5 8Z'),
                path('M9.5 8H14.5Q14.5 11 12 11Q9.5 11 9.5 8Z')),
          lines('M8 2V14M5 14H11M2.5 4H13.5',
                'M4 4L1.5 8M4 4L6.5 8M12 4L9.5 8M12 4L14.5 8'),
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
          union(stroke('M6 5Q7 2.5 10 4Q12 6 9 7Q7.5 7.5 8 10', 1.2), line((2, 2), (14, 14))),
          'hearing deaf muted accessibility')
    shape('baby', circle(8, 8.5, 5.5),
          union(stroke('M6.5 3Q6 1 8 1.3Q10 1.6 8.5 3.5', 1.1),
                dots((6, 8), (10, 8), r=.6), stroke('M6 10.5Q8 12.5 10 10.5', 1.1)),
          'infant childcare newborn family')

    api['CATEGORY'] = 'Health and fitness'
    shape('syringe',
          path('M4 6L8 2L13 7L9 11Z'),
          union(lines('M3 5L10 12M7 1L14 8M10 4L13 1M11.5 .8L15.2 4.5M6.5 8.5L1 14'),
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
    glyph('anchor', stroke('M8 4.2V14M4 7H12M1.5 10Q2.5 14 8 14Q13.5 14 14.5 10M1.5 10V12M1.5 10H3.5M14.5 10V12M14.5 10H12.5'),
          stroke(circle(8, 3, 1.6), 1.15),
          'nautical boat harbor mooring sea')

    api['CATEGORY'] = 'Weather and nature'
    shape('cat',
          path('M2 7V2L6 4Q8 3 10 4L14 2V7Q15 13.5 8 14Q1 13.5 2 7Z'),
          union(dots((5.5, 7.5), (10.5, 7.5), r=.6),
                poly([(7, 9.5), (9, 9.5), (8, 10.5)]),
                stroke('M8 10.5V11.5M4 10L1 9M12 10L15 9', 1.05)),
          'animal feline pet kitten')
    shape('dog',
          path('M5 3Q8 1 11 3L13.5 3L14 9Q13 11 11.5 8V11Q11.5 14 8 14Q4.5 14 4.5 11V8Q3 11 2 9L2.5 3Z'),
          union(stroke('M5 3L4.5 8M11 3L11.5 8', 1.05),
                dots((6.5, 7), (9.5, 7), r=.55),
                poly([(7, 9), (9, 9), (8, 10.3)]), line((8, 10), (8, 11.5), width=1.05)),
          'animal canine pet puppy')
    shape('bird',
          path('M2 8L5 9Q8 8 8 5Q8 2 11 2Q13 2 13 5L15 6L13 7Q13 12 9 13Q4 15 2 8Z'),
          union(circle(11.2, 4.5, .55), stroke('M5.5 9Q7 13 10.5 8M7 13V15M10 13V15', 1.05)),
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
          stroke('M3 5Q4 12 10 12M3 3L4 1.5', 1.1),
          'fruit food tropical produce')
    shape('cherry', union(circle(4.5, 11, 3), circle(11.5, 11, 3)),
          stroke('M4.5 8Q5 5 8 3Q8 6 11.5 8M8 3Q11 1 13 2Q11 5 8 3', 1.1),
          'fruit food cherries produce')
    shape('sandwich', path('M2 10L8 3L14 10V13H2Z'),
          stroke('M2 10H14M4 10L5 12L7 10L9 12L11 10', 1.05),
          'food bread snack lunch')
    shape('cookie',
          path('M9.5 1.5Q9 4 11 4Q10.5 6.5 14 6Q16 12 11 14Q4 17 1.5 10Q0 4 5 2Q7 1 9.5 1.5Z'),
          dots((5, 5.5), (4, 9.5), (8, 8), (9.5, 12), (12, 9), r=.7),
          'food biscuit snack browser cookie')
    shape('ice-cream-cone',
          union(path('M4 8H12L8 15Z'),
                path('M3 8Q1.5 5.5 4 4Q4 1 8 1Q12 1 12 4Q14.5 5.5 13 8Z')),
          lines('M3 8H13M6 10L9 11M7 12L8.5 12.5'),
          'dessert icecream frozen cone sweet')
    shape('door-closed', rr(3, 1.5, 10, 13, .7),
          union(line((1.5, 14.5), (14.5, 14.5)), circle(10.5, 8, .65)),
          'door entrance room closed')
    shape('bath', path('M1.5 8H14.5L13 12Q12.5 13 11 13H5Q3.5 13 3 12Z'),
          lines('M3 8V3Q3 1 5 1Q7 1 7 3M5 13V15M11 13V15M1 8H15'),
          'bathtub bathroom wash bathing')
    shape('toilet',
          union(rr(2, 2, 4, 7, .6), path('M6 7H14V9Q14 11 10.5 11L11.5 14H5L6 10Z')),
          lines('M6 7V9H14M3.5 4H4.5'),
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
          path('M2 3L5 1.5L10 4L9 7L7.5 6.5L12.8 12.3Q14 13.5 12.5 14.5Q11.5 15.2 10.7 14L5.5 7L4 8L2 6L4 4.5Z'),
          line((7.5, 6.5), (5.5, 7), width=1.1),
          'tool construction repair carpentry build')
    shape('construction', rr(1.5, 5, 13, 5, .8),
          lines('M4 5L7 10M9 5L12 10M4 10V14M12 10V14'),
          'barrier work roadworks construction maintenance')

    assert all(name in api['DRAWINGS'] for name in NAMES)
