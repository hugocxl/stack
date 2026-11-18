"""Original accessibility and movement concepts on the rounded CXL grid.

Poses use clear limb separation and the family's opaque line treatment.
Physical hearing-aid and caption-panel surfaces use selective secondary tone.
No reference-library outlines are imported.
"""

NAMES = (
    'hearing-aid', 'audio-description', 'assistive-listening',
    'person-walking', 'person-running', 'person-hiking', 'person-seated',
    'wheelchair-active',
)


def register(api):
    shape, glyph = api['shape'], api['glyph']
    path, rr, circle = api['path'], api['rr'], api['circle']
    stroke, line, union = api['stroke'], api['line'], api['union']
    api['CATEGORY'] = 'People and accessibility'
    empty = path('')

    def g(name, *pieces, tags):
        glyph(name, union(*pieces), empty, tags)

    def st(data, width=1.35):
        # Union separately expanded limbs to avoid coincident cap failures.
        return union(*(stroke('M' + contour, width)
                       for contour in data.split('M')[1:]))

    # A behind-the-ear housing, thin acoustic tube and separate ear tip.
    # The tube is a physical connector and stays positive in Solid.
    aid = path('M9.8 4.4C12.5 4.6 13.7 7.2 12.5 10.7L11.7 13'
               'Q11.1 14.7 9.7 14.2Q8.4 13.7 9 12.1L9.9 9.4'
               'Q10.7 7.2 9 6.8Z')
    shape('hearing-aid', aid,
          union(st('M9.8 4.4C10.4 .5 4.3 .4 4.3 4.2V7.8', 1.2),
                rr(3.1, 7.4, 2.4, 3.2, 1.1)),
          'hearing aid auditory assistive device accessibility')

    # Purpose-drawn AD letters retain open counters at the smallest size.
    shape('audio-description', rr(1.6, 3, 12.8, 10, 1.8),
          st('M3.8 10.7L5.1 5.6Q5.4 4.9 5.7 5.6L7 10.7'
             'M4.4 8.7H6.4M9.2 5.5V10.5H10.2'
             'C13 10.5 13 5.5 10.2 5.5Z', 1.05),
          'audio description described video narration accessibility ad')

    # Listening waves sit beside an ear rather than crossing its inner folds.
    ear = st('M2.3 6C2.3 .7 10.4 .7 10.4 6C10.4 8.6 8.2 9.2 7.5 11.8'
             'Q6.9 14.3 5.2 14.3Q3.2 14.3 3.2 12.1'
             'M4.8 6.4C4.8 3.3 8.1 3.5 8.1 5.9Q8.1 7.3 6.7 7.6V9', 1.2)
    g('assistive-listening', ear,
      st('M12.2 4.8Q13.4 6.8 12.2 8.8M14.1 3Q16.3 6.8 14.1 10.6', 1.1),
      tags='assistive listening hearing loop auditory accessibility sound')

    g('person-walking', circle(8.8, 2.1, 1.4),
      st('M8.4 5L7.4 9L5 14.1M7.4 9L10.3 11.2L11.3 14.1'
         'M8.4 5L5.5 6.5L4 9M8.4 5L10.4 7.3L12.2 7.9'),
      tags='walk walking pedestrian movement activity steps fitness')

    g('person-running', circle(10.3, 2.2, 1.4),
      st('M9 5L6.9 8.4L10 10.7L8.3 14M6.9 8.4L4.6 11.4H1.8'
         'M9 5L11.2 7.3L14 6.4M9 5L5.7 4.7L4 6.8'),
      tags='run running jogging sprint workout activity fitness')

    # A walking pole and a rear backpack distinguish hiking from walking.
    g('person-hiking', circle(8, 2.1, 1.4),
      st('M8.1 5L7 9.3L4.7 14.3M7 9.3L9.7 11.3L10.6 14.3'
         'M8.1 5L10.3 7.7H12.9M13 5.5V14.2'),
      path('M7.8 5L6.5 5.85L5.65 8.4Q5.4 9.2 4.5 9L3.3 8.7Q2.65 8.5 2.95 7.5L3.9 4.65Q4.2 3.7 5.15 4L6.6 4.6Z'),
      tags='hike hiking trekking trail walking outdoor activity backpack')

    # The chair is visibly separate from the sitter's back and upper legs.
    g('person-seated', circle(8.8, 2.3, 1.45),
      st('M8.2 5.3L7.9 8.8H11.1L12.2 13.7H14'
         'M3.5 5.9V10.3H10.6M3.5 10.3V14.1', 1.35),
      tags='sitting seated person chair rest accessibility posture')

    # Forward-leaning posture and an open wheel contour communicate propulsion.
    # Open upper-right arc leaves a clear channel around the active limbs.
    wheel = stroke('M4.95 7.8A3.55 3.55 0 1 0 9.85 11.95')
    g('wheelchair-active', circle(9.55, 2.25, 1.4), wheel,
      stroke('M8.65 4.9L6.95 8.65H10.55L12.5 12.9H14.25'
             'M8.65 4.9L5.65 4.45L3.8 6.6'),
      tags='active wheelchair mobility accessible adaptive sport propulsion')
