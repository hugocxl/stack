"""State variants composed from the catalog's original objects and badge families."""

NAMES = (
    'lock-check', 'lock-x', 'lock-clock',
    'microphone-plus', 'microphone-x', 'video-plus', 'video-check',
    'phone-plus', 'phone-check', 'phone-clock', 'users-plus', 'users-minus',
    'users-off', 'users-cog', 'user-off', 'user-clock', 'image-check', 'image-search',
    'link-plus', 'share-check', 'shopping-bag-plus', 'shopping-bag-minus', 'zap-check', 'zap-x',
    'tag-off', 'house-off', 'key-off', 'tv-off', 'laptop-check', 'laptop-off',
    'file-ellipsis', 'calendar-lock', 'clock-x', 'hard-drive-plus', 'hard-drive-check', 'hard-drive-x',
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

    # The badge occludes the keyhole. Keep the full shackle and avoid a clipped
    # fragment of the keyhole where it would meet the edge of the badge slot.
    shackle = next(p for p in components(drawings['lock'][1]) if p.bounds[1] < 7)
    lock_slot = circle(12, 12, 4.35)
    for name, mark, tags in (
        ('lock-check', check(12, 12, .74), 'padlock access secure verified approved'),
        ('lock-x', cross(12, 12, .78), 'padlock access denied rejected'),
        ('lock-clock', clock(12, 12), 'padlock access timed pending expiry'),
    ):
        state(name, 'lock', mark, tags, detail=shackle, gap=lock_slot)

    mic_slot = circle(12.8, 3.45, 3.2)
    for name, mark, tags in (
        ('microphone-plus', plus(12.8, 3.45, .82), 'audio recording microphone add input'),
        ('microphone-x', cross(12.8, 3.45, .74), 'audio recording microphone remove cancel'),
    ):
        state(name, 'microphone', mark, tags, gap=mic_slot)

    # Video call states share the camera and side lens of video-off.
    lens = drawings['video-call'][1]
    for name, mark, tags in (
        ('video-plus', plus(6, 8, .87), 'video camera call add recording'),
        ('video-check', check(6, 8, .73), 'video camera call enabled verified'),
    ):
        state(name, 'video-call', mark, tags, stroke_detail=stroke(lens))

    for name, mark, tags in (
        ('phone-plus', plus(12, 4), 'telephone handset add call contact'),
        ('phone-check', check(12, 4, .81), 'telephone handset call answered verified'),
        ('phone-clock', clock(12, 4), 'telephone handset call waiting scheduled history'),
    ):
        state(name, 'phone-incoming', mark, tags, detail=empty, gap=circle(12, 4, 4.35),
              category='Communication')

    # Use the single-person family's existing marks at the rear shoulder.
    group_slot = circle(12.55, 12.60, 3.85)
    for name, source, tags in (
        ('users-plus', 'user-plus', 'people group team members add invite'),
        ('users-minus', 'user-minus', 'people group team members remove'),
    ):
        badge = drawings[source][1]
        left, top, right, bottom = badge.bounds
        mark = api['transform'](badge, dx=12.55-(left+right)/2, dy=12.60-(top+bottom)/2)
        state(name, 'users', mark, tags, gap=group_slot)

    def off(name, source, tags, *, ascending=False, solid_base=None):
        # Reverse the slash when the subject itself runs from upper left to lower right.
        start, end = ((2, 14), (14, 2)) if ascending else ((2, 2), (14, 14))
        state(name, source, line(start, end), tags, gap=line(start, end, width=3.2),
              solid_base=solid_base, min_area=2.1)

    off('users-off', 'users', 'people group team unavailable disabled')
    cog = api['transform'](drawings['user-cog'][1], dx=.2, dy=2.15)
    state('users-cog', 'users', cog, 'people group team settings manage permissions', gap=group_slot)
    off('user-off', 'user', 'person account profile unavailable disabled')
    state('user-clock', 'user-plus', clock(12, 10.6), 'person account history pending waiting',
          detail=empty, gap=circle(12, 10.6, 4.35))

    # Both marks occupy image-plus's original corner slot.
    image_slot = circle(12, 11.8, 3.5)
    state('image-check', 'image', check(12, 11.8, .70), 'photo picture verified selected',
          gap=image_slot)
    search = union(stroke(circle(11.6, 11.25, 1.4)), line((12.6, 12.25), (13.85, 13.5)))
    state('image-search', 'image', search, 'photo picture search find visual lookup',
          gap=image_slot)

    state('link-plus', 'link', plus(3.15, 3.15, .83), 'hyperlink url attach add insert',
          gap=circle(3.15, 3.15, 3.25))
    state('share-check', 'share', check(12.25, 12.15, .76), 'share export sent completed',
          gap=circle(12.25, 12.15, 3.85), min_area=2)
    # Place the family's circular corner slot far enough down the full-size bag
    # to leave a unit of solid material below the right handle attachment.
    bag_slot = circle(12.79, 12.79, 3.85)
    for name, sibling, tags in (
        ('shopping-bag-plus', 'star-plus', 'shopping bag retail purchase add item'),
        ('shopping-bag-minus', 'heart-minus', 'shopping bag retail remove item'),
    ):
        mark = api['transform'](drawings[sibling][1], dx=.79, dy=1.19)
        state(name, 'shopping-bag', mark, tags, gap=bag_slot,
              solid_base=overrides['shopping-bag']['solid'])

    zap_slot = circle(12.60, 12.95, 3.45)
    for name, mark, tags in (
        ('zap-check', check(12.60, 12.95, .73), 'lightning bolt power energy ready charged'),
        ('zap-x', cross(12.60, 12.95, .76), 'lightning bolt power energy error unavailable'),
    ):
        state(name, 'zap', mark, tags, gap=zap_slot)

    off('tag-off', 'tag', 'label tag hidden disabled', ascending=True)
    off('house-off', 'home', 'house home unavailable disabled')
    off('key-off', 'key', 'security access key revoked disabled', ascending=True)
    off('tv-off', 'tv', 'television broadcast display disconnected')

    laptop_solid = overrides['laptop']['solid']
    state('laptop-check', 'laptop', check(8, 6.6, .7), 'computer laptop verified trusted',
          solid_base=laptop_solid)
    off('laptop-off', 'laptop', 'computer laptop offline disabled', solid_base=laptop_solid)

    dots = union(*(circle(x, 10, .67) for x in (5.4, 8, 10.6)))
    state('file-ellipsis', 'file', dots, 'document file more options actions overflow')

    # Preserve the binding and divider. Replace the dates in the calendar's
    # interior state slot with a small padlock whose shackle has an open counter.
    lock = union(api['rr'](5.7, 10.15, 4.6, 2.35),
                 stroke('M6.6 10.25V9.25A1.4 1.4 0 0 1 9.4 9.25V10.25'))
    state('calendar-lock', 'calendar', lock, 'schedule date locked private calendar',
          detail=api['CALTOP'])

    # Recover structural details from each sibling before replacing its mark.
    clock_hands = next(p for p in components(drawings['clock-check'][1]) if p.contains((6.25, 6.7)))
    state('clock-x', 'clock-check', cross(12.5, 12.4, .62), 'time clock expired cancelled',
          detail=clock_hands, gap=empty, category='Time and planning')

    drive_face = union(*(p for p in components(drawings['hard-drive-upload'][1])
                         if p.bounds[1] > 8))
    for name, mark, tags in (
        ('hard-drive-plus', plus(8, 3.7), 'storage disk drive add mount'),
        ('hard-drive-check', check(8, 3.7, .86), 'storage disk drive verified healthy'),
        ('hard-drive-x', cross(8, 3.7, .87), 'storage disk drive error disconnect'),
    ):
        state(name, 'hard-drive-upload', mark, tags, detail=drive_face, gap=circle(8, 3.7, 3.6))
