"""State variants composed from the catalog's original objects and badge families."""

NAMES = (
    'lock-check', 'lock-x', 'lock-clock',
    'microphone-plus', 'microphone-x', 'video-plus', 'video-check',
    'phone-plus', 'phone-check', 'phone-clock', 'users-plus', 'users-minus',
    'users-off', 'users-cog', 'user-off', 'user-clock', 'image-check', 'image-search',
    'link-plus', 'share-check',
    'tag-off', 'house-off', 'key-off', 'tv-off', 'laptop-check', 'laptop-off',
    'file-ellipsis', 'calendar-lock', 'clock-x',
)


def register(api):
    drawings, overrides = api['DRAWINGS'], api['STYLE_OVERRIDES']
    stroke, line, circle = api['stroke'], api['line'], api['circle']
    union, components = api['union'], api['components']
    plus, check, cross = api['plus'], api['check'], api['cross']
    empty = api['po'].Path()

    def cut(layer, gap):
        return api['op'](layer, gap, api['po'].PathOp.DIFFERENCE)

    def clock(x, y):
        # One hand meets the dial at twelve. Its short return stays clear of three.
        return union(stroke(circle(x, y, 2.75)),
                     line((x, y - 2.75), (x, y), (x + .85, y + .55)))

    def state(name, source, mark, tags, *, detail=None, gap=None, category=None,
              stroke_detail=None, solid_base=None, min_area=.85):
        body, original_detail, outlined, base_category, _ = drawings[source]
        detail = original_detail if detail is None else detail
        api['CATEGORY'] = category or base_category
        # The body has already been softened and fitted by its original recipe.
        # Register it verbatim so the state does not apply either operation twice.
        assert name not in drawings
        drawings[name] = (body, union(detail, mark), outlined, api['CATEGORY'], tags)
        rim = stroke(body) if outlined else empty
        if source == 'users':
            # Its inherited shoulder rim extends 0.015 beyond both grid edges.
            # Trim only that overshoot, preserving the positions of both people.
            grid = api['rr'](.65, .65, 14.7, 14.7, 0)
            rim = api['op'](rim, grid, api['po'].PathOp.INTERSECTION)
            solid_base = cut(api['solid_body'](body, rim, detail), stroke('M9 11.5V14.7'))
        ink = union(rim if outlined else body, detail)
        mono = ink if stroke_detail is None else union(rim, stroke_detail)
        if solid_base is None:
            solid_base = (api['solid_body'](body, rim, detail) if outlined else ink)
        surface = cut(body, ink) if outlined else empty
        if gap is None:
            # A mark on a surface reverses out of the solid silhouette.
            solid = cut(solid_base, mark)
            surface = cut(surface, mark)
        else:
            def visible(layer):
                # Discard isolated tips left by the badge or slash.
                return union(*(p for p in components(cut(layer, gap)) if p.area >= min_area))
            surface, ink, mono = visible(surface), visible(ink), visible(mono)
            solid = union(visible(solid_base), mark)
        ink = union(ink, mark)
        overrides[name] = {
            'duotone': ([(surface, .24)] if surface else []) + [(ink, 1)],
            'solid': solid,
            'stroke': union(mono, mark),
        }

    def badged(name, source, kind, cx, cy, r, tags, dx=0, dy=0, category=None, detail=None):
        # SF badge variant: the full base, shifted to make room, with a badge disc.
        body, base_detail, outlined, base_category, _ = drawings[source]
        detail = base_detail if detail is None else detail
        api['CATEGORY'] = category or base_category
        tr = api['transform']
        drawings[name] = (tr(body, dx=dx, dy=dy), tr(detail, dx=dx, dy=dy), outlined, api['CATEGORY'], tags)
        if source in overrides and detail is base_detail:
            overrides[name] = {k: ([(tr(p, dx=dx, dy=dy), a) for p, a in v] if isinstance(v, list) else tr(v, dx=dx, dy=dy))
                               for k, v in overrides[source].items()}
        api['badge'](name, kind, cx, cy, r)

    for name, kind, tags in (
        ('lock-check', 'check', 'padlock access secure verified approved'),
        ('lock-x', 'x', 'padlock access denied rejected'),
        ('lock-clock', 'clock', 'padlock access timed pending expiry'),
    ):
        badged(name, 'lock', kind, 11.6, 12.0, 3.15, tags, dx=-1.1)
    for name, kind, tags in (
        ('microphone-plus', 'plus', 'audio recording microphone add input'),
        ('microphone-x', 'x', 'audio recording microphone remove cancel'),
    ):
        badged(name, 'microphone', kind, 11.9, 4.1, 3.0, tags, dx=-1.3)

    # Video call states share the camera and side lens of video-off.
    lens = drawings['video-call'][1]
    for name, mark, tags in (
        ('video-plus', plus(5.97, 8, .87), 'video camera call add recording'),
        ('video-check', check(5.97, 8.05, .73), 'video camera call enabled verified'),
    ):
        state(name, 'video-call', mark, tags, stroke_detail=stroke(lens))

    for name, kind, tags in (
        ('phone-plus', 'plus', 'telephone handset add call contact'),
        ('phone-check', 'check', 'telephone handset call answered verified'),
        ('phone-clock', 'clock', 'telephone handset call waiting scheduled history'),
    ):
        badged(name, 'phone-incoming', kind, 11.9, 4.1, 3.2, tags, detail=empty, category='Communication')

    group_slot = circle(12.55, 12.60, 3.85)
    badged('users-plus', 'users', 'plus', 12.2, 12.0, 3.15, 'people group team members add invite', dx=-.6, dy=-.6)
    badged('users-minus', 'users', 'minus', 12.2, 12.0, 3.15, 'people group team members remove', dx=-.6, dy=-.6)

    def off(name, source, tags, *, ascending=False, solid_base=None):
        # Reverse the slash when the subject itself runs from upper left to lower right.
        start, end = ((2, 14), (14, 2)) if ascending else ((2, 2), (14, 14))
        state(name, source, line(start, end), tags, gap=line(start, end, width=3.2),
              solid_base=solid_base, min_area=2.1)

    off('users-off', 'users', 'people group team unavailable disabled')
    badged('users-cog', 'users', 'gear', 12.2, 12.0, 3.15, 'people group team settings manage permissions', dx=-.6, dy=-.6)
    off('user-off', 'user', 'person account profile unavailable disabled')
    badged('user-clock', 'user', 'clock', 11.85, 11.85, 3.25, 'person account history pending waiting')

    badged('link-plus', 'link', 'plus', 12.0, 12.0, 3.15, 'hyperlink url attach add insert')
    # SF square.and.arrow.up.badge.checkmark: the share base with a disc badge.
    api['CATEGORY'] = drawings['share'][3]
    api['badged_copy']('share-check', 'share', 'check', cy=11.3, tags='share export sent completed')
    # shopping-bag-plus / -minus: SF bag.badge.* disc badges, drawn in draw.py (lane B).
    # zap-check / zap-x: SF bolt.badge.* disc badges, drawn in draw.py (lane B).

    off('tag-off', 'tag', 'label tag hidden disabled')
    off('house-off', 'home', 'house home unavailable disabled')
    off('key-off', 'key', 'security access key revoked disabled', ascending=True)
    off('tv-off', 'tv', 'television broadcast display disconnected')

    # Content inside the screen stays inside, centered (SF convention).
    state('laptop-check', 'laptop', check(8, 7.55, .62), 'computer laptop verified trusted')
    off('laptop-off', 'laptop', 'computer laptop offline disabled')

    badged('file-ellipsis', 'file', 'ellipsis', 4.35, 11.95, 3.25, 'document file more options actions overflow', dx=1.3, dy=-.45)

    # SF calendar.badge.lock: the dates give way to a padlock.
    state('calendar-lock', 'calendar', api['lock_mark'](8, 9.0, 3.6, 2.6, 1.0, .55),
          'schedule date locked private calendar', detail=api['CALTOP'])

    badged('clock-x', 'clock', 'x', 11.85, 11.85, 3.25, 'time clock expired cancelled', category='Time and planning')

    # hard-drive-plus/-check/-x: SF lower-leading badges, drawn in draw.py (lane B).
