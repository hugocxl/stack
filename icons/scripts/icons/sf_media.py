"""Original capture and listening controls inspired by SF Symbols' semantic breadth.

Geometry is drawn on the CXL grid; no platform glyph outlines are imported.
Controls stay monochrome. Secondary tone is reserved for physical surfaces.
"""
import math

NAMES = (
    'motion-photo', 'camera-metering', 'camera-burst',
    'exposure-lock', 'focus-auto', 'focus-manual', 'audio-spatial',
    'audio-mono', 'audio-stereo', 'noise-cancellation',
    'audio-transcription', 'playback-speed',
)


def register(api):
    glyph, shape = api['glyph'], api['shape']
    path, rr, circle = api['path'], api['rr'], api['circle']
    line, stroke, union = api['line'], api['stroke'], api['union']
    op, po = api['op'], api['po']
    empty = path('')

    def g(name, *pieces, tags=''):
        glyph(name, union(*pieces), empty, tags)

    def st(d, w=1.35):
        return stroke(d, w)

    def sub(a, b):
        return op(a, b, po.PathOp.DIFFERENCE)

    def brackets():
        return st('M5 2H3Q2 2 2 3V5M11 2H13Q14 2 14 3V5'
                  'M14 11V13Q14 14 13 14H11M5 14H3Q2 14 2 13V11', 1.25)

    api['CATEGORY'] = 'Photography and optics'
    # SF livephoto: a ring of small dots around an open ring and a
    # heavier centre ring.
    halo = [circle(8 + 6.45*math.cos(i*math.tau/24), 8 + 6.45*math.sin(i*math.tau/24), .48)
            for i in range(24)]
    g('motion-photo', *halo, api['ring'](8, 8, 4.45),
      sub(circle(8, 8, 2.15), circle(8, 8, .95)),
      tags='live photo movement capture motion')
    # SF camera.metering.*: the standard rectangle opened at the middle of
    # each side, around a centre-weighted ring and spot.
    frame = sub(stroke(rr(1.69, 3.32, 12.62, 9.36)), rr(0, 6.35, 16, 3.3, 0))
    g('camera-metering', frame, api['ring'](8, 8, 3.0), circle(8, 8, 1.35),
      tags='camera exposure spot center weighted metering')
    # Three exposed top edges communicate a rapid sequence of captured frames.
    front = rr(2,6.4,12,7.5,1.4)
    back = st('M3.2 3.9H12.8M4.6 1.6H11.4',1.25)
    lens = stroke(circle(8,10.15,2),1.15)
    shape('camera-burst', front, union(back,lens), 'camera burst sequence continuous capture')
    # Exposure is a split disc; the adjacent lock makes the hold state explicit.
    disc = sub(circle(5.2,7.5,3.9), rr(5.2,2,8,11,0))
    exposure = union(disc, stroke(circle(5.2,7.5,3.9),1.25))
    lock_body = rr(9.1,8.4,5.3,5.2,.8)
    lock = union(stroke(lock_body,1.25), st('M10.2 8.4V6.8C10.2 4.4 13.3 4.4 13.3 6.8V8.4',1.25))
    g('exposure-lock', sub(exposure, union(lock_body, lock, stroke(lock, 2))), lock,
      tags='auto exposure lock camera brightness hold ae')
    g('focus-auto', brackets(), st('M5 10.8L7.45 5.4Q8 4.2 8.55 5.4L11 10.8M6.1 8.7H9.9',1.25),
      tags='autofocus automatic camera lens sharpness af')
    g('focus-manual', brackets(), st('M4.9 10.8V5.2L8 8.4L11.1 5.2V10.8',1.25),
      tags='manual focus camera lens sharpness mf')

    api['CATEGORY'] = 'Media'
    # A listening position with an orbit, distinct from an audio waveform.
    head = circle(8,5.1,2.1)
    shoulders = st('M4.3 12.8V11.7C4.3 8.8 11.7 8.8 11.7 11.7V12.8',1.25)
    orbit = st('M3.5 5.3C.8 6.6 .8 9.9 2.8 11.1M12.5 5.3C15.2 6.6 15.2 9.9 13.2 11.1',1.35)
    g('audio-spatial', head, shoulders, orbit,
      tags='spatial surround immersive audio listening')
    # A shared speaker source and explicit output channels distinguish these
    # settings from generic circle marks and sound-volume wavefronts.
    source = path('M2.1 6H4.1L7.4 3.4V12.6L4.1 10H2.1Z')
    for name, channels, tags in (
        ('audio-mono', (8,), 'mono monaural single channel sound'),
        ('audio-stereo', (5.45, 10.55), 'stereo left right dual channel sound'),
    ):
        dots = union(*(circle(11.6, y, 1.4) for y in channels))
        shape(name, source, dots, tags)
        api['STYLE_OVERRIDES'][name] = {'stroke': union(st(source), st(dots))}
    # Headphone cups remain visible; the quiet center distinguishes ANC from mute.
    cups = union(rr(1.6,7,2.7,5.1,1.1),rr(11.7,7,2.7,5.1,1.1))
    band = st('M2.95 7V6C2.95-.2 13.05-.2 13.05 6V7',1.25)
    quiet = st('M6.8 8.1H9.2',1.25)
    shape('noise-cancellation', cups, union(band,quiet),
          'active noise cancellation anc headphones quiet isolation')
    # Waveform to written lines communicates transcription without tiny letters.
    g('audio-transcription', st('M2 5.2V9.8M4.8 2.8V12.2M7.6 5.2V9.8',1.35),
      st('M10.5 5H14M10.5 8H14M10.5 11H13',1.25),
      tags='speech to text dictation audio transcription transcript')
    g('playback-speed', st('M2.3 11.9C-.4 7.8 2.3 2 8 2C13.7 2 16.4 7.8 13.7 11.9',1.25),
      st('M8 8L11.2 5',1.35), circle(8,8,.9),
      api['poly']([(6.25,10.5),(6.25,14),(9.5,12.25)]),
      tags='playback speed rate faster slower media')
