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

    # SF figure.* poses are solid silhouettes: a round head and thick
    # limbs with round ends, the same in every style.
    LIMB = 1.75

    def figure(head, *chains, torso=None):
        parts = [circle(*head)]
        for chain in chains:
            parts.append(stroke('M' + 'L'.join(f'{x} {y}' for x, y in chain), LIMB, exact=True))
        if torso:
            parts.append(stroke('M' + 'L'.join(f'{x} {y}' for x, y in torso), 2.3, exact=True))
        return union(*parts)

    walker = figure((9.05, 2.3, 1.6),
                    ((7.7, 9.0), (6.4, 11.6), (4.75, 14.1)),
                    ((7.7, 9.0), (9.55, 11.3), (10.15, 14.15)),
                    ((8.6, 5.6), (10.15, 7.55), (11.95, 7.95)),
                    torso=((8.55, 5.2), (7.7, 9.0)))
    g('person-walking', walker,
      tags='walk walking pedestrian movement activity steps fitness')

    runner = figure((10.6, 2.25, 1.6),
                    ((8.0, 8.65), (10.65, 10.25), (10.0, 13.9)),
                    ((8.0, 8.65), (6.6, 11.35), (3.35, 12.45)),
                    ((9.4, 5.4), (11.15, 7.35), (13.1, 6.6)),
                    ((9.4, 5.4), (6.9, 5.25), (5.4, 7.25)),
                    torso=((9.6, 5.1), (8.0, 8.65)))
    g('person-running', runner,
      tags='run running jogging sprint workout activity fitness')

    # A walking pole and a rear backpack distinguish hiking from walking.
    hiker = figure((8.75, 2.3, 1.6),
                   ((7.45, 9.0), (6.15, 11.6), (4.6, 14.1)),
                   ((7.45, 9.0), (9.25, 11.3), (9.85, 14.15)),
                   ((8.35, 5.6), (9.85, 7.55), (11.35, 7.75)),
                   torso=((8.3, 5.2), (7.45, 9.0)))
    pack = rr(3.35, 4.35, 2.95, 5.1, .95, exact=True)
    pole = stroke('M12.45 6.3V14.95')
    g('person-hiking', hiker, pack, pole,
      tags='hike hiking trekking trail walking outdoor activity backpack')

    # The chair is visibly separate from the sitter's back and upper legs.
    sitter = figure((9.7, 2.3, 1.6),
                    ((8.3, 9.25), (11.95, 9.4), (12.6, 13.85)),
                    ((9.1, 5.6), (10.6, 7.45), (12.5, 7.45)),
                    torso=((9.1, 5.2), (8.3, 9.25)))
    chair = stroke('M4.45 5.6V14.35M4.45 11.6H10.35')
    g('person-seated', sitter, chair,
      tags='sitting seated person chair rest accessibility posture')

    # SF figure.roll.runningpace: a leaning figure in the wheel, a small
    # caster and pace lines trailing behind.
    roller = figure((11.0, 2.3, 1.6),
                    ((8.15, 8.75), (11.85, 9.2), (12.55, 12.0)),
                    ((9.75, 5.5), (10.55, 7.9), (8.6, 9.85)),
                    torso=((10.0, 5.15), (8.15, 8.75)))
    rim = api['op'](api['ring'](8.15, 10.55, 4.15),
                    union(roller, stroke(roller, 1.8, exact=True)), api['po'].PathOp.DIFFERENCE)
    pace = stroke('M.95 6.85H3.35M.95 9.05H2.75M.95 11.25H2.95')
    g('wheelchair-active', roller, rim, api['ring'](13.85, 13.75, 1.05), pace,
      tags='active wheelchair mobility accessible adaptive sport propulsion')
