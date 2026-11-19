"""Original rounded world, commerce, and recreation families for full coverage."""
import json
from pathlib import Path

NAMES = [x['lucide_name'] for x in json.loads(Path(__file__).with_name('world-scope.json').read_text())]

def register(api):
    p=api['path']; st=api['stroke']; rr=api['rr']; ci=api['circle']; un=api['union']; ln=api['line']; tr=api['transform']; op=api['op']; po=api['po']; ring=api['ring']; dots=api['dots']; poly=api['poly']
    shape=api['shape']; glyph=api['glyph']; drawings=api['DRAWINGS']; overrides=api['STYLE_OVERRIDES']
    categories={'home':'Home and food','food-beverage':'Home and food','tools':'Work and education','finance':'Finance and commerce','shopping':'Finance and commerce','transportation':'Maps and travel','emoji':'People and accessibility','nature':'Weather and nature','gaming':'Media','animals':'Weather and nature','buildings':'Home and food','travel':'Maps and travel','weather':'Weather and nature'}
    scope={x['lucide_name']:x for x in json.loads(Path(__file__).with_name('world-scope.json').read_text())}
    def cat(n): api['CATEGORY']=categories[scope[n]['primary_category']]
    def g(n,d,detail=None):
        cat(n);glyph(n,st(d) if isinstance(d,str) else d,detail or po.Path())
    def s(n,b,d=None):
        cat(n);shape(n,p(b) if isinstance(b,str) else b,st(d) if isinstance(d,str) else d)
    def stack(n, planes, detail=None, exterior=None, front_mask=None):
        # Mask each rear plane with the complete face in front of it.
        outline=po.Path()
        solid=po.Path()
        for face in planes:
            rim=st(face)
            mask=front_mask if face is planes[-1] and front_mask is not None else face
            outline=un(op(outline,mask,po.PathOp.DIFFERENCE),rim)
            clearance=mask if mask is front_mask else un(face,st(face,3.25))
            solid=un(op(solid,clearance,po.PathOp.DIFFERENCE),face,rim)
        detail=detail or po.Path()
        exterior=exterior or po.Path()
        ink=un(outline,detail,exterior)
        surface=un(op(un(*planes[:-1]),front_mask,po.PathOp.DIFFERENCE),planes[-1]) if front_mask is not None else un(*planes)
        s(n,surface,ink)
        overrides[n]={'duotone':[(op(surface,ink,po.PathOp.DIFFERENCE),.24),(ink,1)],
                      'stroke':ink,'solid':un(op(solid,detail,po.PathOp.DIFFERENCE),exterior)}

    def base_layers(n):
        b,d,outlined,*_=drawings[n];outer=st(b) if outlined else po.Path();ink=un(outer,d) if outlined else un(b,d)
        if outlined:
            filled=un(b,outer);interior=op(filled,st(filled,1.8),po.PathOp.DIFFERENCE)
            counters=[];structural=[]
            for part in api['components'](d):
                (structural if op(part,filled,po.PathOp.DIFFERENCE).area>part.area*.12 else counters).append(part)
            solid=un(op(filled,op(un(*counters),interior,po.PathOp.INTERSECTION),po.PathOp.DIFFERENCE),*structural)
            duo=[(op(b,ink,po.PathOp.DIFFERENCE),.24),(ink,1)]
        else:solid=ink;duo=[(ink,1)]
        ov=overrides.get(n,{})
        duo=ov.get('duotone',duo)
        solid=ov.get('solid',solid)
        ink=ov.get('stroke',ink)
        if n in {'banknote','ticket','shopping-cart','fish','umbrella'}:
            live=rr(.651,.651,14.698,14.698,0)
            def trim(layer):
                return op(layer,live,po.PathOp.INTERSECTION)
            duo=[(trim(layer),alpha) for layer,alpha in duo]
            solid,ink=trim(solid),trim(ink)
        return duo,solid,ink

    def face_mark(n,base,symbol):
        duo,solid,mono=base_layers(base)
        ink=un(mono,symbol)
        g(n,ink)
        overrides[n]={'duotone':[(op(a,symbol,po.PathOp.DIFFERENCE),v) for a,v in duo]+[(symbol,1)],
                      'solid':op(solid,symbol,po.PathOp.DIFFERENCE),'stroke':ink}

    def off(n,base,min_fragment_area=0):
        duo,solid,mono=base_layers(base)
        slash=ln((2,2),(14,14))
        clear=st('M2 2L14 14',2.65)
        def cut(layer):
            visible=op(layer,clear,po.PathOp.DIFFERENCE)
            if min_fragment_area:
                # Drop only the isolated end of a detail severed by the slash.
                visible=un(*(c for c in api['components'](visible) if c.area>=min_fragment_area))
            return visible
        ink=un(cut(mono),slash)
        g(n,ink)
        overrides[n]={'duotone':[(cut(a),v) for a,v in duo]+[(slash,1)],
                      'solid':un(cut(solid),slash),'stroke':ink}
    def badge(n,base,mark,footprint=None,offset=(0,0),slot=None):
        duo,solid,mono=base_layers(base)
        # Reserve the entire badge footprint so its counters show through.
        footprint=mark if footprint is None else footprint
        clear=slot if slot is not None else un(footprint,st(footprint,2.15))
        def cut(layer):
            return op(tr(layer,dx=offset[0],dy=offset[1]),clear,po.PathOp.DIFFERENCE)
        ink=un(cut(mono),mark)
        g(n,ink)
        overrides[n]={'duotone':[(cut(a),v) for a,v in duo]+[(mark,1)],
                      'solid':un(cut(solid),mark),'stroke':ink}
    def mark(kind):
        return {'plus':api['plus'](12,12,.9),'minus':ln((10,12),(14,12)), 'x':api['cross'](12,12,.85),'check':api['check'](12,12,.7),'heart':tr(p('M8 13L2.5 7.5C-1 2 5-1 8 4C11-1 17 2 13.5 7.5Z'),scale=.29,dx=4,dy=4),'percent':un(ci(10.5,10.5,.55),ci(13.5,13.5,.55),ln((10.2,13.8),(13.8,10.2)))}[kind]
    # Foods use distinct silhouettes, with only identifying interior detail.
    food={
      'amphora':('M6 1.7H10C9.4 3.8 9.9 4.9 10.9 6.4C13.2 9.8 10.8 12.7 8 14.3C5.2 12.7 2.8 9.8 5.1 6.4C6.1 4.9 6.6 3.8 6 1.7Z', un(st('M5.85 4.5C5.3 5.9 2 3.6 2 6.3C2 8 3.2 9.6 4.9 10.5'),api['mirror'](st('M5.85 4.5C5.3 5.9 2 3.6 2 6.3C2 8 3.2 9.6 4.9 10.5')))),
      'avocado':('M8 1C11 1 10 5 13 8C16 13 11 15 8 15C3 15 1 12 3 8C6 5 5 1 8 1Z',None),
      'bacon':('M5.6 1.6Q7.5 3.1 9.55 1.75L12.1 3.75Q10 6.25 11.45 9.25L9.3 14.3Q7.3 12.85 5.2 14.25L2.9 12.3Q4.7 9.8 3.3 6.9Z', 'M5.6 1.6Q7.6 4.4 5.9 7.1Q7.35 10.3 5.2 14.25M9.55 1.75Q10.8 4.2 8.65 7.05Q10.15 10.05 8.35 13.75'),
      'barrel':('M4.1 2.1Q1.7 8 4.1 13.9H11.9Q14.3 8 11.9 2.1Z', 'M3.3 4.9H12.7M3.3 11.1H12.7M6.8 2.1Q5.3 8 6.8 13.9M9.2 2.1Q10.7 8 9.2 13.9'),
      'bean':('M11 2C16 2 15 9 11 12C7 16 1 15 1.5 10C2 6 6 9 7 6C7 3 8 2 11 2Z','M5 11Q10 11 11 6'),
      'beef':('M2.1 7Q1.8 4 4.8 3.4L10.4 2.3C14.5 1.6 16.1 6.7 12.6 8.7L10.1 10.2Q9 14.3 5.8 13.8C2.7 13.5 2 10.4 2.1 7Z',un(st(ci(10.8,5.5,1.5)),st('M4.3 7.6Q4.3 10.6 6.4 11'))),
      'beer':('M3.2 5.1H10.9V13.8H3.2Z', 'M10.9 6.2H12.5C15.3 6.2 15.3 11.3 10.9 11.3M6.3 7.3V11.4M3.2 5.1C2.6 3.1 4.1 1.8 5.8 2.8Q9 1.2 10.9 5.1'),
      'blender':('M3 2H12L11 10H5Z','M5 10L3 14H13L11 10M12 3H14V7H12M6 5H8M7 12H9'),
      'bottle-wine':('M6.5 1.6H9.5V5.6C9.5 7.2 11.4 7.5 11.4 9.1V14.3H4.6V9.1C4.6 7.5 6.5 7.2 6.5 5.6Z', 'M6.5 3.6H9.5M4.6 9.8H11.4'),
      'broccoli':('M6.1 9.1C2.4 10.5 .7 7 3.2 5.4C2.2 2.3 5.7 1 8 3.1C10.3 1 13.8 2.3 12.8 5.4C15.3 7 13.6 10.5 9.9 9.1L10.7 14H5.3Z', 'M5.9 6.4L8 8.8L10.3 6.3M8 8.8V11.3'),
      'cake-slice':('M1.8 6.8L10.8 2.8Q13.6 3.8 14.2 6.2V12.6L1.8 13.4Z', 'M1.8 6.8L14.2 6.2M1.8 9.9Q3.3 8.4 4.8 9.7T8 9.5T11.2 9.3T14.2 9.1M5.8 9.95V13.1M10.3 8.95V12.9'),
      'can':(rr(4,2,8,12),'M4 5H12M4 12H12M7 3.5H9'),
      'can-soda':('M4.85 1.8H11.15L10.85 3.1Q12.45 4.75 12.45 6.1V11Q12.45 12.5 11.05 13.3V14.15H4.95V13.3Q3.55 12.5 3.55 11V6.1Q3.55 4.75 5.15 3.1Z', 'M4.3 4.55Q8 5.45 11.7 4.55M7.2 3.15H8.8M4.15 9.55Q7.4 7.1 11.9 7.05'),
      'candy':(ci(8,8,3.35), un(st('M4.8 6.9L1.85 5.55L2.35 8L1.85 10.45L4.8 9.1M11.2 6.9L14.15 5.55L13.65 8L14.15 10.45L11.2 9.1'),st('M6.15 10.8L9.9 5.3'))),
      'carton':('M5 1.8H10.8L13.6 5.3V14H2.4V5.3Z', 'M2.4 5.3H13.6M10.8 1.8L8.7 5.3V14M10.7 8.4H11.6'),
      'cheese':('M2 7L12 2Q15 4 14 7V10Q11 10 12 13L14 14H2Z','M2 7H14M5 10H5.1M8 12H8.1'),
      'citrus':('M2 4.9L14 7.2C13.1 11.4 10.5 13.4 6.7 12.7C3 12 1.4 8.8 2 4.9Z', 'M2.3 5.1C2.4 11.3 10.8 13.5 13.8 7.3M8 6.1L5.3 9.6M8 6.1L9.4 10.6'),
      'cooking-pot':(rr(3,5.4,10,8.4), 'M2.2 5.4H13.8M1.5 8H3M13 8H14.5M6.1 3H9.9M8 3V5.4'),
      'croissant':('M2 12.7C1.3 10.3 1.9 7.4 3.7 6.5Q4 4.1 6 4.1C6.9 2.4 9 2.3 10.1 3.8Q12.5 3.8 12.8 6.2C14.8 7.5 14.9 10.3 13.7 12.8Q12.8 10.8 11.4 10.1Q10.5 10.5 9.6 9.4Q8.2 9.8 6.7 9.1Q5.9 10.4 4.9 10.1Q3.1 11.1 2 12.7Z', 'M3.7 6.5Q5.1 7.5 4.9 10.1M6 4.1Q7.4 6.1 6.7 9.1M10.1 3.8Q11.2 6.3 9.6 9.4M12.8 6.2Q13.1 8.4 11.4 10.1'),
      'cup-soda':('M3 5H13L11.5 14H4.5Z','M2 5H14M9 5L10 1H13'),
      'cupcake':('M3 8H13L11 14H5Z','M3 8C0 5 3 3 5 4C4 0 9 0 10 3C15 2 16 7 13 8M6 10L7 12M10 10L9 12'),
      'dessert':('M2.8 6.2C3 4.3 4.5 3.3 6.1 4.1C7 1.7 10 2 10.7 4Q13.2 3.8 13.2 6.2V12.9H2.8Z', 'M2.8 6.7Q5 7.8 7.1 6.8T11.1 6.8Q12.2 7.2 13.2 6.7M2.8 10.2H13.2M1.6 12.9H14.4'),
      'donut':(ci(8,8,6), 'M5.4 4.8L6.1 4.4M10.4 4.8L11.1 5.4M4.5 9.8L5.1 10.5M10.6 11.3L11.1 10.7'),
      'drumstick':('M5.7 8.4C4.4 6.1 5.9 3 8.1 2.1C11.6 .6 14.7 3 14.3 6.3C14 9.4 11.3 11.2 8.2 10.2L5.9 12.2C6.6 14.8 3.3 15.2 3 13C.8 13 .9 9.8 3.6 10.4Z', 'M5.7 8.4Q6.5 9.7 8.2 10.2'),
      'egg':('M8 1.7C10.3 1.7 13.3 7.4 13.3 10.3C13.3 15.5 2.7 15.5 2.7 10.3C2.7 7.4 5.7 1.7 8 1.7Z', None),
      'egg-fried':('M2.3 6.4C2 3.5 4.9 2.2 7.3 3C10.3 1.3 13.6 3.3 13.2 6Q15.7 9.4 12.8 11.7C11.7 14.1 9.3 14.1 7.5 13.1C4.8 14.5 2.3 12.7 2.7 10.6C1.3 9.1 1.4 7.6 2.3 6.4Z', None),
      'glass-water':('M3 2H13L11.5 14H4.5Z','M4 8Q6 6 8 8T12 8'),
      'ham':('M2.5 5.4C3.4 2.5 7.5 1.6 11.2 3.6C14.7 5.4 15.5 8.3 13.4 11.7C11.7 14.6 7.6 14.8 4.3 12.4C1.7 10.5 1.3 8.3 2.5 5.4Z', 'M2.5 5.4C5.6 .7 16.3 7.2 11.3 12.4Q9.8 13.9 7.6 13.7M5.8 7.1C6.4 5.8 8.6 6.4 8.2 7.9C7.7 9.6 5.2 8.6 5.8 7.1Z'),
      'hamburger':('M1.9 6.5C2.9 .7 13.1 .7 14.1 6.5ZM2.4 11.7H13.6Q13.2 14.1 10.8 14.1H5.2Q2.8 14.1 2.4 11.7Z', st('M2.7 8.65H6.6L8.6 9.9L10.1 8.65H13.3Q14.8 8.65 14 10.25L13.4 11.7H2.6L2 10.25Q1.2 8.65 2.7 8.65Z')),
      'ice-cream-bowl':('M2 8H14Q13 12.6 8 12.6Q3 12.6 2 8Z', 'M8 12.6V14.4M5.2 14.4H10.8M3.05 8C1.85 4.35 5.05 2.55 7.25 5.05M6.6 8C6.6 1.95 13.2 1.95 13.2 8'),
      'leafy-green':('M3.2 11.6C1 9 2.5 4.4 5.1 4.5C5.8 1.3 9.1 1.4 10.2 3.1C13 2.2 15 4.5 13.4 7C15.3 9.7 12.2 13.4 8.4 12.6Q5.9 13.4 3.2 11.6Z', 'M1.8 14.2L10.7 5.1M6.5 9.4L6.4 6.9M6.5 9.4L9.4 9'),
      'lollipop':(ci(8,6.1,4.65), 'M8 10.75V14.5M5 6.1C4.8 3.2 9.05 2.5 10.35 4.85C11.95 7.95 7.75 9.9 6.5 7.5Q5.9 5.95 7.45 5.6Q8.9 5.35 9.15 6.55'),
      'mango':('M7.4 3.8C10.9 1.9 14.1 4.1 14 7.6C13.9 11.9 8.6 14.7 3.3 13.8Q2.5 13.6 1.6 12.8C4.2 11.6 3.6 6.1 7.4 3.8Z', 'M9.4 3.4Q8.7 1.6 7.3 1.6'),
      'martini':('M2 2.3H14L8 9.3Z', 'M8 9.3V13.9M4.8 13.9H11.2M4.4 5.1H11.6'),
      'microwave':(rr(1.6,3.1,12.8,9.8), un(st(rr(3.45,5.25,5.5,5.5)),st('M10.8 3.15V12.85'),dots((12.6,6.4),(12.6,9.55),r=.55))),
      'milk':('M5.4 1.9H10.5L12.8 5.4V14.1H3.2V5.4Z', 'M3.2 5.4H12.8M10.5 1.9L8.9 5.4V14.1M5.1 9.7H6.9'),
      'nut':('M3 6.6C2.2 6.5 2.1 5.9 2.5 5C3.5 2.6 5.8 2.2 8 2.2C10.2 2.2 12.5 2.6 13.5 5C13.9 5.9 13.8 6.5 13 6.6L12.4 6.8C12.4 10 10.6 12.6 8 14.3C5.4 12.6 3.6 10 3.6 6.8Z', 'M3.1 6.6Q8 7.3 12.9 6.6M8 2.4Q8.2 1.6 9 1.4'),
      'paper-bag':('M2.9 4.6L4.45 2.1H11.55L13.1 4.6V14.15H2.9Z', 'M2.9 4.6H13.1M5.45 4.6V6.45C5.45 9.8 10.55 9.8 10.55 6.45V4.6'),
      'popcorn':('M2.7 6.8Q1.8 4.5 4 4Q4.4 1.6 6.5 2.8Q8.2 1 9.8 3Q12.3 1.9 12.8 4Q14.9 4.8 13.3 6.8L12.2 14H3.8Z', 'M2.7 6.8H13.3M5.9 7L6.6 14M10.1 7L9.4 14'),
      'popsicle':('M4.1 5.4C4.1 3.2 5.8 1.5 8 1.5Q8.9 1.5 9.65 1.9C8.95 3.75 10.25 5.2 11.9 4.75V10.05Q11.9 11.3 10.65 11.3H5.35Q4.1 11.3 4.1 10.05Z', 'M8 11.3V14.5'),
      'salad':('M2 8.2H14Q12.9 14 8 14Q3.1 14 2 8.2Z', 'M3.4 8.2Q2 6.3 2.75 4.85Q4.55 4.45 5.95 5.85M6.45 8.2C5.2 5.25 6.05 3.25 8 2.15C9.95 3.25 10.8 5.25 9.55 8.2M10.05 5.85Q11.45 4.45 13.25 4.85Q14 6.3 12.6 8.2'),
      'soup':('M2 8H14Q13 14 8 14Q3 14 2 8Z','M5 2Q3 4 5 6M9 1Q7 3 9 5M13 2L10 8'),
    }
    for n,(b,d) in food.items():s(n,b,d)
    # Counters that belong to recognizable ring-like food silhouettes.
    for n,center in [('avocado',ci(8,10,2.5)),('donut',ci(8,8,2.1)),('egg-fried',ci(8,8,2.5))]:
        b,d,outlined,category,tags=drawings[n];drawings[n]=(b,un(d,st(center)),outlined,category,tags)
        if n=='donut':
            duo,solid,mono=base_layers(n);hole=ci(8,8,1.5);overrides[n]={'duotone':[(op(a,hole,po.PathOp.DIFFERENCE),v) for a,v in duo],'solid':op(solid,un(center,st(center)),po.PathOp.DIFFERENCE),'stroke':mono}
    g('candy-cane',st('M4.55 14.25V5.5C4.55 .2 12.75 .2 12.75 5.5V6.9H10V5.4C10 3.65 7.35 3.65 7.35 5.4V14.25ZM4.55 9L7.35 7.1M4.55 12.45L7.35 10.55M8.4 1.55L8.85 4.05'))
    g('faucet',st('M1.75 7V13.45M1.75 8.9H5.35V6.3Q5.35 5.15 6.55 5.15H10.75Q13.9 5.15 13.9 8.35V10.65H11.25V8.9H8.1V10.45Q8.1 11.5 7.05 11.5H1.75M7.8 5.15V2.35M5.65 2.35H9.95'))
    s('fish-symbol','M4.9 8Q8.4 1 14.2 8Q8.4 15 4.9 8Z',un(st('M4.9 8L1.8 5.2V10.8Z'),ci(10.8,7.5,.62)))
    centres=[(3.25,4.9),(8,4.9),(12.75,4.9),(5.625,8.95),(10.375,8.95),(8,13)]
    berries=[ci(x,y,1.35) for x,y in centres]
    grape_stem=st('M8 3.55Q8.4 1.6 10.35 1.45')
    s('grape',un(*berries),grape_stem)
    s('groceries','M2 7.7H14L12 14H4Z','M3.5 7.7V4.3L4.3 3.8V2.1H6.2V3.8L7 4.3V7.7M8.3 7.7L10.9 2.9C12.2 1.1 14.4 2.8 13.3 4.4L11.6 7.7M6.3 10.1V12M9.7 10.1V12')
    s('hand-platter','M2.7 8C3.1 2.2 12.9 2.2 13.3 8Z','M1.6 8H14.4M8 1.8V3.7M1.8 11.9L4.2 10.35H8.6M2.4 14.25H8.4Q9.35 14.25 10 13.8L14.1 10.65')
    s('hop', 'M8 1.7C11.8 2.5 14.1 5.6 13.2 9C12.5 11.5 10.1 13.5 8 14.55C5.9 13.5 3.5 11.5 2.8 9C1.9 5.6 4.2 2.5 8 1.7Z', 'M3 5.65Q6.3 5.9 8 8.25Q9.7 5.9 13 5.65M3.05 8.95Q6.4 9.15 8 11.65Q9.6 9.15 12.95 8.95M8 1.7V4.55')
    g('utensils-crossed',un(
        st('M2 3.1L5.65 6.75Q6.75 7.85 7.8 6.8Q8.85 5.75 7.75 4.65L4.3 1.3'),
        st('M3.15 2.2L6.6 5.65M7.7 6.8L14.1 13.65'),
        st('M1.75 13.9L6.5 9.15M9.45 6.35Q9.35 3.3 14.15 1.65L10.6 6.8Z')))
    fork_and_knife=drawings['utensils-crossed'][0]
    overrides['utensils-crossed']={'solid':un(fork_and_knife,p('M9.45 6.35Q9.35 3.3 14.15 1.65L10.6 6.8Z'))}
    g('vegan',st('M1.85 5.5L6.65 13.8L10.9 6.85M8.8 10.2C6.75 5.85 9.4 2.45 14.05 1.9C14.45 6.55 12.35 10.15 8.8 10.2Z'))
    # Two pairs of broad kernels on a single diagonal stem.
    wheat_stem=st('M2 14.1L11.05 5.05')
    kernels=st('M5.25 10.85Q1.95 10.75 2.05 6.65Q5.7 7.15 5.25 10.85Z'
               'M5.25 10.85Q7.95 9.85 10.95 12.25Q8.1 14.7 5.25 10.85Z'
               'M8.85 7.25Q5.4 7.05 5.55 2.9Q9.05 3.45 8.85 7.25Z'
               'M8.85 7.25Q11.6 6.1 14.5 8.6Q11.9 11.1 8.85 7.25Z'
               'M10.85 5.25Q10.4 1.75 14 1.65Q14.25 5.1 10.85 5.25Z')
    g('wheat',un(wheat_stem,kernels))
    for n,base in [('bean-off','bean'),('beef-off','beef'),('beer-off','beer'),('candy-off','candy'),('carton-off','carton'),('egg-off','egg'),('fish-off','fish'),('hop-off','hop'),('milk-off','milk'),('nut-off','nut'),('wine-off','wine')]:off(n,base)
    off('wheat-off','wheat',min_fragment_area=2)
    homes={
      'air-vent':(rr(2,2,12,12),'M4 5H12M4 8H12M4 11H12'),
      'alarm-smoke':('M2 2.4H14V4.9Q14 6.7 11.8 6.7H4.2Q2 6.7 2 4.9Z', 'M4.7 4.55H6.2M9.8 4.55H11.3M5.8 9.1C3.4 11.4 7.2 11.9 5.3 14.2M10.8 9.1C8.4 11.4 12.2 11.9 10.3 14.2'),
      'bed-double':('M1.85 5.25H14.15V12.65H1.85Z', 'M1.9 9.1H14.1M8 5.25V9.1M2.55 5.25V3.65Q2.55 2.5 3.7 2.5H12.3Q13.45 2.5 13.45 3.65V5.25M1.85 12.65V14.55M14.15 12.65V14.55'),
      'bed-single':('M1.85 8.4H14.1V11.15H1.85Z','M1.85 4.05V13.8M14.1 8.4V13.8M2 8.4V5.75H4.45Q6.25 5.75 6.25 7.55V8.4M6.25 8.4V5.75H12.4Q14.1 5.75 14.1 7.45V8.4'),
      'blinds':(rr(2,2,10.1,9.3),'M2 5.1H12.1M2 8.2H12.1M11.6 2H14.1V13.85M13.25 13.85H14.8'),
      'fence':('M2 3L4 1L6 3V14H2ZM10 3L12 1L14 3V14H10Z','M1 6H15M1 11H15'),
      'fire-extinguisher':('M6 7Q6 5.7 7.5 5.3V4.5H10V5.3Q11.6 5.7 11.6 7V13Q11.6 14.3 10.3 14.3H7.3Q6 14.3 6 13Z', 'M7 4L12.8 2.2M8.5 4.3L12.6 4.8M7.5 4.6Q3 4.2 3 8.3V11M6.2 9H11.4'),
      'heater':(rr(2,4,12,9),'M5 6V11M8 6V11M11 6V11M4 13V15M12 13V15M4 1V2M8 1V2M12 1V2'),
      'lamp-ceiling':('M4.35 6.8H11.65L14.4 10.85H1.6Z', 'M8 1.65V6.8M5.95 10.85C6.05 14.1 9.95 14.1 10.05 10.85'),
      'lamp-desk':('M6.3 3.2L9.3 1.8L12.9 4.9L7.9 8.2Z', 'M6.5 4.6L3.1 7.5L7.1 13.6M3.7 13.8H11.8'),
      'lamp-floor':('M5 2H11L13 7H3Z','M8 7V14M4 14H12'),
      'lamp-wall-down':('M7 7H13L15 12H5Z','M2 2V9M2 5H10V7'),
      'lamp-wall-up':('M7 7H13L15 2H5Z','M2 6V13M2 10H10V7'),
      'plant-pot':('M4 9H12L11 14H5Z','M8 9V5M8 6Q1 6 3 2Q8 1 8 6ZM8 5Q8 0 13 2Q14 6 8 5Z'),
      'shelving-unit':(rr(2,2,12,12), 'M2 7.6H14M2 11.5H14M4.65 4.25V7.6M7 4.85V7.6M9.35 4.55L10.55 7.6M4.45 11.5V9.2H7V11.5M10.65 9.75V11.5'),
      'soap-dispenser-droplet':(rr(1.9,6.15,6.95,7.9), 'M5.4 6.15V3.2M3.3 3.2H12.65V5.15M12.65 7.55Q8.9 12.35 12.65 13.2Q16.4 12.35 12.65 7.55Z'),
      'solar-panel':('M3 2H13L15 11H1Z','M2 6.5H14M6 2L5 11M10 2L11 11M8 11V14M5 14H11'),

      'brush-cleaning':(rr(1.8,7.1,12.4,2.8), 'M4.1 7.1V5.7Q4.1 3.6 6.2 3.6H9.8Q11.9 3.6 11.9 5.7V7.1M2.5 9.9V13M5.25 9.9V13M8 9.9V13M10.75 9.9V13M13.5 9.9V13'),
      'mop':('M4.7 8.7L7.5 9.4Q8 11.3 10.3 13Q9.4 14.7 7.8 13.6Q6.4 15.1 4.8 13.6Q3 14.7 1.7 13.1Q4.1 11.3 4.7 8.7Z', 'M6.1 9L10.1 1.8M4.8 13.6L5.75 11.35'),
      'toothbrush':(rr(5.3,1.7,3.15,6.5), 'M6.9 8.2V14.35M2.8 2.8H5.4M2.8 5H5.4M2.8 7.2H5.4'),
    }
    for n,(b,d) in homes.items():s(n,b,d)
    towel=rr(5.35,3.55,6.75,10.55)
    rail=st('M1.65 5.1H5.35M12.1 5.1H14.55M1.65 3.55V6.65M14.55 3.55V6.65')
    towel_detail=st('M7.8 3.55V8.35M5.35 11.1H12.1')
    s('towel-rack',towel,un(rail,towel_detail))
    towel_cuts=st('M7.8 3.55V8.35M6.7 11.1H10.75')
    overrides['towel-rack']={'solid':un(op(un(towel,st(towel)),towel_cuts,po.PathOp.DIFFERENCE),rail)}
    back=p('M3.6 8V4.45Q3.6 2.5 5.55 2.5H10.45Q12.4 2.5 12.4 4.45V8L11.25 10.25H4.75Z')
    upholstery=p('M1.75 8.15C1.75 6.15 4.95 6.15 4.95 8.15V9.65H11.05V8.15C11.05 6.15 14.25 6.15 14.25 8.15V12.75H1.75Z')
    legs=st('M3.2 12.75V14.45M12.8 12.75V14.45')
    stack('armchair',[back,upholstery],exterior=legs)
    overrides['armchair']['solid']=op(overrides['armchair']['solid'],st('M4 11.5H12'),po.PathOp.DIFFERENCE)
    bed_body=p('M1.85 5.75H12.4Q14.1 5.75 14.1 7.45V11.15H1.85Z')
    bed_posts=st('M1.85 4.05V13.8M14.1 11.15V13.8')
    bedding=st('M3.45 8.4H12.5M6.25 5.55V8.4')
    overrides['bed-single']={'solid':un(op(un(bed_body,st(bed_body)),bedding,po.PathOp.DIFFERENCE),bed_posts)}
    g('bubbles',un(st(ci(5,10,4)),st(ci(11,4,2.5)),ci(13,12,1)))
    g('rocking-chair','M4 1V9H12M5 9L3 14M10 9L12 14M1 13Q8 17 15 13M4 6H12V9')
    g('shower-head',un(st('M1.7 3.2Q3.15 1.5 4.9 3.05L6.3 4.32M4.75 7.9Q4.7 4.5 7.55 3.75Q9.25 3.3 10.7 4.2Z'),st('M6.4 9.35L7.3 10.8M9.1 7.7L10 9.15M11.8 6.1L12.7 7.55M8.5 12.6L9.4 14.05M11.2 10.95L12.1 12.4M13.9 9.35L14.65 10.55')))
    shine=p('M12.6 6.5Q13 8.7 15 9.1Q13 9.5 12.6 11.7Q12.2 9.5 10.2 9.1Q12.2 8.7 12.6 6.5Z')
    mop_body,mop_detail,*_=drawings['mop']
    s('mop-sparkles',mop_body,un(mop_detail,shine))
    sparkle_face=p('M12.45 2.7Q12.95 4.85 14.65 5.4Q12.95 5.95 12.45 8.1Q11.95 5.95 10.25 5.4Q11.95 4.85 12.45 2.7Z')
    badge('toothbrush-sparkles','toothbrush',st(sparkle_face),sparkle_face)
    door_slot=rr(7.65,7.1,9,9)
    lock_case=rr(10.3,11.4,4.3,3)
    lock_bow=st('M11.05 11.4V10.2A1.4 1.4 0 0 1 13.85 10.2V11.4')
    badge('door-closed-locked','door-closed',un(st(lock_case),lock_bow),slot=door_slot)
    parcel=p('M9.25 10.25L12 8.65L14.75 10.25V13.35L12 14.7L9.25 13.35Z')
    badge('door-closed-package','door-closed',un(st(parcel),st('M9.25 10.25L12 11.85L14.75 10.25M12 11.85V14.65')),slot=door_slot)
    cog_face=ci(12.25,12.25,1.55)
    tooth=st('M12.25 10.25V10.85')
    tooth=tr(tooth,dx=-4.25,dy=-4.25)
    cog=un(st(cog_face),*(tr(tooth,angle,dx=4.25,dy=4.25) for angle in range(0,360,60)))
    badge('door-closed-cog','door-closed',cog,slot=door_slot)
    # The full doorway fits to the left of the shared lower-right badge slot.
    house_slot=rr(9.85,8.35,6.8,8)
    def house_badge(name,symbol):
        badge(name,'home',symbol,offset=(-.7,-.7),slot=house_slot)
    house_badge('house-heart',tr(mark('heart'),dx=.8,dy=.8))
    wifi=un(st('M10.95 10.9Q12.85 9.1 14.75 10.9M11.85 12.55Q12.85 11.65 13.85 12.55'),ci(12.85,14.35,.55))
    house_badge('house-wifi',wifi)
    # Hand tools retain characteristic heads and working edges.
    tools={
      'anvil':('M1.4 5.3H7V4H14.5V7.6H11.7Q9.7 9.9 11.8 11.4L13.2 12.4V13H5.3V12.4L6.8 11.4Q8 10 7.5 8.8C4.9 8.8 2.6 7.4 1.4 5.3Z', None),
      'axe':('M5.9 3.7L8.2 2.4L9.7 4Q11.2 5.3 14.3 4.6Q14.6 8.4 11.6 10.3Q10.3 7.8 7.8 6.7L6.7 6.2Z', 'M6.65 6.1L2.2 13.9'),
      'bolt':(poly([(4.9,2.5),(11.1,2.5),(14.3,8),(11.1,13.5),(4.9,13.5),(1.7,8)]),st(ci(8,8,2.85))),
      'broom':('M6.45 6.7L12 10.15L8.8 14.35L1.75 10.9Z', 'M9.3 8.35L13.55 1.6M5.85 7.3L3.95 11.95M8.7 8.15L6.55 13.2'),
      'drill':('M2 3.2H10V8.15H7.65L6.6 13.95H3.3L4.3 8.15H2Z', 'M10 4.45H12V6.9H10M12 5.7H14.5M4.45 5.5H6.8M3.85 10.9H7.05'),
      'gavel':('M7.1 1.7L13.15 7.75L10.1 10.8L4.05 4.75Z', 'M7.05 7.75L2.1 12.7M8.1 14.1H14'),
      'hard-hat':('M2.65 9.7Q3 3.65 8 3.65Q13 3.65 13.35 9.7Q14.5 9.8 14.5 10.95V12.65H1.5V10.95Q1.5 9.8 2.65 9.7Z', 'M2.05 9.9H13.95M6.2 4V7.55M9.8 4V7.55'),
      'inspection-panel':(rr(2,2,12,12),'M4 4H12V12H4ZM10 7V9'),
      'laser':(rr(1.6,6.1,5.5,3.8), 'M3.6 6.15V9.85M7.1 8H12.45M12.45 5.1V3.85M12.45 10.9V12.15M14.05 6.15L14.75 5.45M14.05 9.85L14.75 10.55'),

      'pickaxe':('M1.55 7.7C3.6 3.1 9.4 1.45 14.5 4.4L13.15 6.25C9.65 3.95 5.9 4.45 1.55 7.7Z', 'M8.5 4.6L4.95 14.2'),
      'pocket-knife':('M2 10Q2 8.6 3.5 8.6H12.1C15.2 8.6 15.2 13.1 12.1 13.1H3.5Q2 13.1 2 11.7Z', un(st('M3.65 8.6L13.8 2.15Q13.4 6.6 8.5 8.6M7.3 8.65V13.05M10.4 8.65V13.05'),st(ci(4.6,10.85,.95)))),
      'screw':('M3.7 2.1H12.3V4.8H10.1V10.8L8 14.3L5.9 10.8V4.8H3.7Z', 'M5.9 4.8H10.1M5.9 8.25L10.1 6.55M5.95 10.9L10.1 9.2'),
      'spool':(un(rr(2.75,2,10.5,2.55),rr(2.75,11.45,10.5,2.55),rr(4.8,3.35,6.4,9.3)), 'M4.8 4.55H11.2M4.8 7.9L11.2 5.8M4.8 10.6L11.2 8.5M4.8 11.45H11.2'),
      'tool-case':(rr(2,5,12,9),'M5 5V2H11V5M2 9H14M5 8V10M11 8V10'),
      'toolbox':('M2 5H14V14H2Z','M5 5V2H11V5M2 9H14M6 8H10V10H6Z'),
    }
    for n,(b,d) in tools.items():s(n,b,d)
    mound=p('M1.6 14.1Q3.75 9.8 7.05 10.3Q8.45 10.75 9.7 14.1Z')
    shovel=p('M8.35 7.25L12.75 8.8Q12.9 11.4 10.15 12.45Q7.95 10.75 8.35 7.25Z')
    stack('mound-shovel',[mound,shovel],exterior=st('M10.55 8L12.7 2.05M11.6 1.75L13.8 2.5'))
    screw_face=drawings['screw'][0]
    screw_cuts=st('M6.75 4.8H9.25M6.95 7.85L9.05 6.95M6.95 10.4L9.05 9.55')
    overrides['screw']={'solid':op(un(screw_face,st(screw_face)),screw_cuts,po.PathOp.DIFFERENCE)}
    bolt_hole=ci(8,8,2.3)
    bolt_duo,bolt_solid,bolt_stroke=base_layers('bolt')
    overrides['bolt']={'solid':op(bolt_solid,ci(8,8,3.2),po.PathOp.DIFFERENCE),
                       'duotone':[(op(part,bolt_hole,po.PathOp.DIFFERENCE),alpha) for part,alpha in bolt_duo]}
    broom_face=drawings['broom'][0]
    broom_handle=st('M9.3 8.35L13.55 1.6')
    bristles=st('M5.2 9.05L3.65 12.75M7.85 10.15L6.1 14.05')
    overrides['broom']={'solid':un(op(un(broom_face,st(broom_face)),bristles,po.PathOp.DIFFERENCE),broom_handle)}
    badge('broom-sparkles','broom',st('M4.35 1.7Q4.85 3.7 6.8 4.2Q4.85 4.7 4.35 6.7Q3.85 4.7 1.9 4.2Q3.85 3.7 4.35 1.7Z'),ci(4.35,4.2,2.1))
    ruler=rr(1.9,1.8,4.6,12.4)
    pencil=p('M10.95 2.05L14.15 2.95L11.65 11.8L9.1 14.4L8.45 10.9Z')
    divisions=st('M1.9 5H4.4M1.9 8H3.85M1.9 11H4.4M8.45 10.9L11.65 11.8M10.3 4.35L13.5 5.25')
    s('pencil-ruler',un(ruler,pencil),divisions)
    g('ruler-dimension-line','M2 5H14V10H2ZM5 5V7M8 5V8M11 5V7M2 14H14M2 12V15M14 12V15')
    # Nature and animals: silhouettes remain distinguishable without labels.
    shell_seams=st('M5.15 6.95L7 5.8L8.85 6.95V9.05L7 10.2L5.15 9.05Z'
                  'M7 3.55V5.8M7 10.2V12.45M2.6 8H5.15M8.85 8H11.4')
    nature={
      'birdhouse':('M3 5.5L8 1.5L13 5.5V13H3Z','M1.7 6.5L3 5.5M13 5.5L14.3 6.5M8 13V15M6 11H10'),
      'feather':('M3.8 11.8C2.9 7.4 6.7 2.2 13.7 1.7Q14.1 5.2 12.2 7.5L10.3 8.2L11.2 8.7C9.4 11.7 6.5 12.8 3.8 11.8Z', 'M1.9 14.2Q7.5 7.2 13.35 2.25'),
      'flame-kindling':('M7.55 1.65Q7.7 5.25 10.35 5.45L11.8 3.75Q14.65 7.6 11 9.45C7.45 11.35 3.65 9.85 3.45 7.3Q3.25 4.55 7.55 1.65Z', 'M2.05 11.6L13.95 14.4M2.05 14.4L13.95 11.6'),
      'flower-2':('M8 5C3.9-.05 .25 4.55 4.95 8C.25 11.45 3.9 16.05 8 11C12.1 16.05 15.75 11.45 11.05 8C15.75 4.55 12.1-.05 8 5Z', st(ci(8,8,1.35))),
      'mountain-snow':('M1.6 13.95L7.25 2.3L14.4 13.95Z', 'M5.15 6.65L6.85 8.05L8.05 6.45L10.15 7M9.6 13.95L11.8 9.8'),
      'rose':('M3 5.4Q2.6 3 5.5 3.2Q7.2 .8 9.4 2.6Q12.4 2.1 12.9 4.9C13.1 7.3 10.5 9.5 8.1 9.5Q4.8 9.6 3 5.4Z', 'M3 5Q5 4.8 7.2 7Q9.8 4.7 12.8 4.9M5.5 3.2Q8.2 2.85 8.8 5.55M8.1 9.5V14.3M8.1 13Q10.8 12.9 12.3 10.7'),
      'shovel':('M5.05 8.85H10.95V10.65Q10.95 13.05 8 14.6Q5.05 13.05 5.05 10.65Z', 'M8 8.85V4.6M5.95 1.55H10.05V2.55Q10.05 4.6 8 4.6Q5.95 4.6 5.95 2.55Z'),
      'shrub':('M2 11.95C.65 9.7 1.9 7.3 4.1 7.1C4 4.85 6.25 3.85 8 5.1C10.25 3.65 12.7 5.15 12.5 7.4C15.3 7.95 15.2 10.85 13.45 12Q11.75 12.9 9.25 12.3V13.6H6.8V12.3Q4.25 12.85 2 11.95Z', 'M4.35 13.8H11.6M8.05 12.65V9.25M8.05 11.2L5.95 9.85'),
      'stone':('M1.7 10L3.1 6.6L7.05 3.75L11.9 4.85L14.35 8.95L12.9 12L8.6 13.15L3 12.15Z', 'M3.1 6.6L6.9 8.15L11.9 4.85M6.9 8.15L5.65 12.65'),
      'tree-deciduous':('M6.6 11.1Q3.2 12.25 2 9.6C.7 7.1 2.5 4.8 4.85 4.95C5.15 1.05 10.7 .85 11.35 4.7C14.7 4.75 15.55 8.2 13.55 10.05Q11.9 11.65 9.25 10.85L9.4 13.05L10.2 14.25H5.65L6.6 12.85Z', 'M7.9 11.05V8.8M7.9 10.55L6.15 9.35'),
      'tree-palm':('M5.9 14.15Q7.8 9.5 7.95 6.2Q8.45 5.55 9.05 6.2Q9.45 9.3 8.5 14.15Z','M8.45 6.2C5.25 3.85 2.6 5.7 1.65 8.85M8.45 6.2C7.6 3.1 5.2 1.8 3.1 2.25M8.45 6.2C9.45 3.15 11.25 1.8 13.45 2.2M8.45 6.2C11.3 4.45 13.8 6.15 14.45 9.45'),
      'bone':(tr(p('M4.5 6.55H11.5C12.35 6.55 11.55 4.45 13.45 4.45C15.65 4.45 16.05 7.1 14.2 8C16.05 8.9 15.65 11.55 13.45 11.55C11.55 11.55 12.35 9.45 11.5 9.45H4.5C3.65 9.45 4.45 11.55 2.55 11.55C.35 11.55 -.05 8.9 1.8 8C-.05 7.1 .35 4.45 2.55 4.45C4.45 4.45 3.65 6.55 4.5 6.55Z'),45,scale=.965),None),
      'origami':('M1.8 6.15L14.1 1.8L10.1 14.15L6.1 10.35Z', 'M1.8 6.15L8.8 6.45L14.1 1.8M8.8 6.45L6.1 10.35M8.8 6.45L10.1 14.15'),
      'panda':(un(ci(3.9,4.1,2),ci(12.1,4.1,2),p('M8 3.2C11.7 3.2 14 6 14 9.2C14 15.8 2 15.8 2 9.2C2 6 4.3 3.2 8 3.2Z')), un(tr(rr(4.1,6.55,2.15,3.25),25),api['mirror'](tr(rr(4.1,6.55,2.15,3.25),25)),st('M7.45 10.5H8.55'))),
      'rat':('M4.8 9.8C4.6 6.3 7.1 4.5 9.8 5.5C9.3 2.9 12.6 2.9 12.4 5.6L14.4 8.5Q14.9 9.2 14 9.5L12 10.1C10.8 12.3 6.5 12.5 4.8 9.8Z', 'M5.1 10.45C2.5 13.8 .6 10.2 2.15 8Q3.6 6 1.6 4.5M11.9 7.6H12'),
      'shell':('M6.5 12.7C3.8 11.65 .9 7.35 2.05 4.85Q2.6 3.45 4.1 3.85Q4.8 1.35 7.05 2.65Q8 1.3 9.55 2.5Q11.45 1.95 12.15 4.05Q14.15 3.9 14.35 5.7Q14.65 9 9.4 12.7Q9.35 14.1 8 14.1Q6.65 14.1 6.5 12.7Z', 'M4.15 3.9Q4.65 7.25 5.75 9M7.9 2.35L8 10.45M11.95 4.1Q11.35 7.25 10.25 9'),
      'shrimp':('M12.1 5.3C10.8 3.2 8 2.65 5.6 3.5C1.7 4.7 .9 8.9 3.3 11.5C5.4 14 9.4 14.2 11.8 11.9Q13.4 13.1 14.5 12.25L13.3 10.8L14.35 9.05Q12.8 8.6 11.5 10.25C8.2 12.1 4.9 10.2 5.7 8.1Q6.6 6 10.5 7.5Z', 'M10.3 3.6Q11.1 1.7 13.4 1.6M6.6 3.2L7.65 6.95M3.4 5L5.9 7.65M2.15 8.8L5.6 8.8M4.25 12.4L6.45 10.45M8.2 13.35L8.25 11.1M11.6 10.35L11.8 11.9M8.75 3.1L9.95 7.25'),
      'snail':(un(ci(6.2,7.8,3.85),p('M1.75 12.65Q3.5 12.45 4.3 10.8L9.05 10.6Q10.25 10.5 10.55 8.5Q10.95 6.45 12.5 6.75Q14.15 6.9 14.1 8.7V10.15Q14 13.2 10.4 13.2H4.35Z')), 'M4.25 7.7C4.15 5.1 8.45 5.1 8.45 8.15C8.45 10.65 5.75 10.7 5.45 8.75M11.5 6.85L11 4.8M13.25 7L14.5 5.15'),
      'squirrel':('M5.8 11.8C1.75 11.2 .6 7.3 2.15 4.4C3.05 2.65 5.2 1.85 6.45 2.8C8.55 4.4 6.45 6.4 5.35 5.25C4.5 6.4 5.35 8.1 6.8 8.15Q7.7 6.95 9.15 7.2L9.8 4.75L10.4 2.85L11.95 4.7Q13.55 4.9 13.65 6.55L14.55 7.35L13.25 8.55L11.8 8.65L11.3 10.4L12.95 10.15Q13.9 10.25 13.6 11.25L11.25 11.95L10.6 12.85L12.55 13.15Q13.4 13.6 12.7 14.15H7.15Q4.95 14.05 5.8 11.8Z', un(st('M5.85 11.85C5.5 9.8 6.65 8.7 8.1 8.65'),ci(12,6.65,.5))),
      'turtle':('M2.6 8C2.6 5.4 4.5 3.55 7 3.55C9.8 3.55 11.4 5.3 11.4 8C11.4 10.7 9.8 12.45 7 12.45C4.5 12.45 2.6 10.6 2.6 8Z', un(st('M3.9 4.8Q1.7 4.85 1.65 2.65Q3.65 2.1 5.1 4M3.9 11.2Q1.7 11.15 1.65 13.35Q3.65 13.9 5.1 12M8.4 3.8Q9.6 1.8 11.2 2.1Q11.45 4.4 10.35 5.05M8.4 12.2Q9.6 14.2 11.2 13.9Q11.45 11.6 10.35 10.95'),st(ci(13.05,8,1.55)),st('M2.7 6.7L1.3 8L2.7 9.3'),shell_seams)),
      'worm':('M1.6 9.5C3.6 10.1 4.2 8.9 4.7 6.3C5.4 2.5 9.5 2.3 10.3 5.7C10.9 7.8 9.6 9.2 10.6 9.9Q11.5 10.4 12 9.2C13.1 7.3 15.5 9.4 14.2 11.4C12.4 14.4 8.1 13.5 7.5 10.8C6.9 8.7 8.5 6.2 7.4 6.1C6.3 6 7.1 10.4 4.4 11.4Q2.2 12 1.6 9.5Z', 'M4.55 7.55L6.75 8.25M7.65 11.2L10.25 10.2'),
    }
    for n,(b,d) in nature.items():s(n,b,d)
    b,d,o,c,t=drawings['birdhouse'];drawings['birdhouse']=(b,un(d,st(ci(8,7.8,1.6))),o,c,t)
    # The valleys partition one palmate blade, leaving one rim at each join.
    leaf_half=p('M8 12.4Q5.4 14.55 2.25 13.35Q3.15 11.55 5.5 10.9Q2.15 10.2 1.4 6.9Q4.15 7.2 5.65 8.8Q3.2 5.8 3.15 3.15Q5.8 4.2 7.05 7.15Q6.45 4.35 8 1.35Z')
    leaf=un(leaf_half,api['mirror'](leaf_half))
    veins=st('M5.5 10.9L7 12.8M5.65 8.8L7.45 12.65M7.05 7.15L8 12.4')
    g('cannabis',un(st(leaf),veins,api['mirror'](veins),st('M8 12.4V14.65')))
    off('cannabis-off','cannabis')
    shrimp_body,shrimp_detail,outlined,category,tags=drawings['shrimp']
    drawings['shrimp']=(tr(api['mirror'](shrimp_body),-9),tr(api['mirror'](shrimp_detail),-9),outlined,category,tags)
    off('shrimp-off','shrimp')
    # A park/tree grouping intentionally shows separate trunks and canopies.
    g('park',st('M1.55 14.1H14.55M3.9 14.1V8.2M1.55 8.2L3.9 2.15L6.25 8.2ZM7.5 10.8H14.35M8.2 10.8V14.1M13.6 10.8V14.1M8.15 8.35H13.7V10.8'))
    pine=p('M4.7 2.1L8.1 8.9H6.2L7.6 11.1H5.3V14H4.1V11.1H1.6L3.1 8.9H1.5Z')
    broadleaf=p('M10.7 4.1C12.1 3 14 4.1 13.8 5.9C15.65 7.4 14.35 10.7 12.1 10.7L12.3 14.1H9.95L10.2 10.7C7.7 11 6.4 8.2 8 6.4Q7.8 4.2 10.7 4.1Z')
    stack('trees',[pine,broadleaf])
    # Board games and leisure symbols.
    g('bow-arrow','M2.2 2.7Q12.5 3.5 13.3 13.8L4.3 11.7ZM2.3 13.7L13.9 2.1M10.7 2.1H13.9V5.3')
    s('bomb',ci(7.3,9.1,5.15),st('M10.6 5.1L11.7 3.6Q12.55 2.2 14.25 2.45'))
    leaf=p('M8 8C7.9 6.6 5.4 5.1 5.5 3.4C5.6 1.3 7.2 1.1 8 2.2C8.8 1.1 10.4 1.3 10.5 3.4C10.6 5.1 8.1 6.6 8 8Z')
    clover=un(*(tr(leaf,angle) for angle in (0,90,180,270)))
    s('clover',clover,st('M8 8Q10 12.8 13.6 14.1'))
    s('crown','M2 4L5 7L8 2L11 7L14 4L12 13H4Z','M4 10H12')
    for n in range(1,7):
        positions={1:[(8,8)],2:[(5,5),(11,11)],3:[(5,5),(8,8),(11,11)],4:[(5,5),(11,5),(5,11),(11,11)],5:[(5,5),(11,5),(8,8),(5,11),(11,11)],6:[(5,5),(11,5),(5,8),(11,8),(5,11),(11,11)]}[n]
        s(f'dice-{n}',rr(2,2,12,12),dots(*positions,r=.7))
    s('dices',un(rr(1.7,1.7,8.4,8.4),rr(6,6,8.3,8.3)),un(st(rr(6,6,8.3,8.3)),dots((4,4),(8.6,8.6),(11.7,11.7),r=.72)))
    front_die=rr(6,6,8.3,8.3)
    rear_die=rr(1.7,1.7,8.4,8.4)
    clearance=un(front_die,st(front_die,3.25))
    rear_solid=op(un(rear_die,st(rear_die)),un(clearance,ci(4,4,.76)),po.PathOp.DIFFERENCE)
    overrides['dices']={'solid':un(rear_solid,op(un(front_die,st(front_die)),dots((8.6,8.6),(11.7,11.7),r=.76),po.PathOp.DIFFERENCE))}
    s('gamepad-2','M5.15 4.1H10.85Q13.35 4.1 14.25 11.6Q14.6 14.55 12 12.9L10.15 11.15H5.85L4 12.9Q1.4 14.55 1.75 11.6Q2.65 4.1 5.15 4.1Z',un(st('M3.85 7.65H6.8M5.325 6.2V9.1'),dots((10.8,6.15),(12.35,7.75),(10.8,9.35),(9.25,7.75),r=.58)))
    s('gamepad-directional','M6 1.8H10V5.9H14.2V10.1H10V14.2H6V10.1H1.8V5.9H6Z','M8 4V5M4 8H5M11 8H12M8 11V12')
    s('gem','M4.45 2.3H11.55L14.45 6.25L8 14.35L1.55 6.25Z','M1.55 6.25H14.45M4.45 2.3L5.95 6.25L8 14.35M11.55 2.3L10.05 6.25L8 14.35M5.95 6.25L8 2.3L10.05 6.25')
    s('ghost','M2 14V7C2-1 14-1 14 7V14L11 12L8 14L5 12Z',dots((5.5,7),(10.5,7),r=.8))
    goal_frame=st('M1.85 12.8V4.25Q1.85 3 3.1 3H12.9Q14.15 3 14.15 4.25V8.85')
    net=un(ln((5.95,3),(5.95,9.85)),ln((10.05,3),(10.05,9.85)),ln((1.85,7.25),(14.15,7.25)))
    ball=ci(12.9,12.6,1.85)
    g('goal',un(goal_frame,net,st(ball)))
    s('joystick',rr(2,10,12,4),un(ln((8,10),(8,5)),ci(8,3,2),ci(4,12,.5)))
    s('playing-card',rr(3,1,10,14),poly([(8,5),(11,8),(8,11),(5,8)]))
    stack('playing-cards',[rr(1.75,1.55,8.1,11.25),rr(5.85,3.15,8.4,11.25)],st('M10.05 6.3L12.1 8.75L10.05 11.2L8 8.75Z'))
    fan_card=rr(5,2.6,6.6,10.9)
    fan=[tr(fan_card,-23,dx=-2.2,dy=.2),tr(fan_card,-8,dx=-.7),tr(fan_card,12,dx=1.5,dy=.2)]
    stack('playing-cards-fan',fan,tr(un(st('M8.3 5.8L9.95 8L8.3 10.2L6.65 8Z'),st('M6.55 4.5H7.6M9 11.5H10.05')),12,dx=1.5,dy=.2))
    for n,text in [('scroll',False),('scroll-text',True)]:
        paper=p('M4.1 3.6Q4.1 1.75 5.95 1.75H12.1Q14.3 1.75 14.3 4V5.15H11.6V11.65Q11.6 14.2 9.05 14.2H3.8Q1.65 14.2 1.65 11.7H4.1Z')
        folds=st('M11.6 5.15V3.45Q11.6 2.5 12.1 1.9M4.1 11.7H8.15Q8.1 13.4 9.05 14.2')
        s(n,paper,un(folds,st('M6.2 5.75H9.2M6.2 8.45H9.2')) if text else folds)
        paper=drawings[n][0]
        cuts=st('M11.6 3.35V5.85M3.25 11.7H8.1')
        if text:
            cuts=un(cuts,st('M6.4 5.6H9M6.4 8.25H9'))
        overrides[n]={'solid':op(un(paper,st(paper)),cuts,po.PathOp.DIFFERENCE)}
    s('skull','M4.75 13.75V11.05C-.7 8.8 .8 1.65 8 1.65C15.2 1.65 16.7 8.8 11.25 11.05V13.75Z',un(ci(5.15,7.05,1.2),ci(10.85,7.05,1.2),p('M8 8.65L9 10.3H7Z'),st('M6.85 12V13.7M9.15 12V13.7')))
    blade=st('M5.25 9.05L11.85 2.45L14.3 1.7L13.55 4.15L6.95 10.75Z')
    grip=st('M3.5 7.3L8.7 12.5M5.2 9.2L2.4 12M3.9 13L6.55 10.45')
    pommel=st(ci(2.8,13.2,1.35))
    sword=un(blade,grip,pommel)
    g('sword',sword)
    # A pair on this grid needs one grip and one guard per blade.
    short_blade=p('M3.05 11.1L12 2.15L14.35 1.65L13.85 4L4.9 12.95Z')
    short_hilt=st('M2.35 10.4L5.65 13.7M3.975 12.025L1.75 14.25')
    front_sword=un(st(short_blade),short_hilt)
    clear_blade=un(short_blade,st(short_blade,3.15))
    g('swords',un(op(api['mirror'](front_sword),clear_blade,po.PathOp.DIFFERENCE),front_sword))
    g('tic-tac-toe',un(st('M5.55 1.65V14.35M10.45 1.65V14.35M1.65 5.55H14.35M1.65 10.45H14.35M1.95 2.05L3.55 3.65M1.95 3.65L3.55 2.05M12.45 12.45L14.05 14.05M12.45 14.05L14.05 12.45'),st(ci(13,2.9,1.05))))
    s('tombstone','M3 14V6C3-1 13-1 13 6V14Z','M1 14H15M8 4V9M6 6H10')
    s('toy-brick',rr(1.75,5.9,12.5,7.65),st('M3.35 5.9V3.05H6.45V5.9M9.55 5.9V3.05H12.65V5.9M1.9 11.15H14.1'))
    # Chess pieces share a base, with distinct identifying silhouettes.
    chess={
      'pawn':'M6 7Q3 4 5 2Q8-1 11 2Q13 4 10 7L11 12H5Z',
      'bishop':'M8 1Q15 6 10 8L11 12H5L6 8Q1 6 8 1Z',
      'king':'M4.75 6.1H11.25L10.05 12.2H5.95Z',
      'queen':'M3 4L6 7L8 2L10 7L13 4L11 12H5Z',
      'rook':'M2.5 2H4.8V4.55H6.95V2H9.05V4.55H11.2V2H13.5V6.45H11L10 12H6L5 6.45H2.5Z',
      'knight':'M4.5 12C4.5 9.4 7.7 9.1 8.1 6.6L5.6 7.7Q4.7 8.2 4.1 7.5L3.2 6.3L6.8 2.9L7.2 1.4L8.9 2.4C11.9 2.8 12.6 7.3 11.6 12Z',
    }
    for kind,b in chess.items():
        n='chess-'+kind;s(n,un(p(b),rr(3,12,10,2)),st('M7 4L9 6') if kind=='bishop' else (st('M8 1.6V6.1M6.15 3.5H9.85') if kind=='king' else (ci(7.4,4.6,.58) if kind=='knight' else None)))
    # Currency signs: original monoline lettering; Unicode charts establish identity,
    # never font outlines or reference-library SVG paths.
    currencies={
      'dollar-sign':'M12 4C10 1 4 2 4 5C4 8 12 7 12 11C12 14 6 15 3 12M8 1V15',
      'cent':'M12 5C5 1 3 7 5 11Q8 14 12 11M9 2L7 14',
      'euro':'M12 3C5-1 2 8 6 13Q9 15 12 12M2 6H10M2 9H9',
      'pound-sterling':'M12 3Q7-1 6 5V10Q6 13 3 14H13M3 8H10',
      'indian-rupee':'M3 2H13M3 5H13M5 2Q13 3 10 7Q8 9 4 8L12 14',
      'japanese-yen':'M3 2L8 8L13 2M8 8V14M3 8H13M3 11H13',
      'russian-ruble':'M5 14V2H9C14 2 14 8 9 8H2M2 11H9',
      'swiss-franc':'M6 14V2H13M6 7H11M3 11H9',
      'turkish-lira':'M6 1V14Q13 14 14 8M2 7L11 3M2 10L11 6',
      'armenian-dram':'M3 5C3 0 12 0 12 5V14M6 5V14M4 9H14M4 12H14',
      'azerbaijani-manat':'M2 13C2 0 14 0 14 13M8 1V14',
      'bangladeshi-taka':'M3 2L7 4V10Q7 15 12 12Q15 10 12 8M3 6H11',
      'belarusian-ruble':'M2.4 13V2.8H5.6C9.2 2.8 9.2 7.5 5.6 7.5H2.4M5.5 7.5C9.6 7.5 9.6 13 5.5 13H2.4M10.9 13V7.5M10.9 10Q11.8 7.5 14.1 7.5',
      'bitcoin':'M5.25 3.45H9.05C12.95 3.45 12.95 7.85 9.05 7.85H5.25M9.05 7.85C13.65 7.85 13.65 12.55 9.05 12.55H4.05M5.25 3.45V12.55M4.05 3.45H5.25M6.85 1.55V3.45M10 1.55V3.45M6.85 12.55V14.45M10 12.55V14.45',
      'emirati-dirham':'M4.65 2.3H7.95C15.7 2.3 15.7 13.7 7.95 13.7H4.65ZM2.05 6.15H14.45M2.05 9.85H14.45',
      'georgian-lari':'M12 8C12 1 3 1 3 8Q3 14 8 14H13M6 1V9M9 1V9M2 14H13',
      'kazakh-tenge':'M2 2H14M2 5H14M8 5V14',
      'nepali-rupee':'M1.85 3.65H7.65M3.6 3.65Q8.1 5.35 5.2 8Q4.5 8.65 3.6 8.6L7.1 12.05M8.65 7Q10.55 5.45 12.85 6.2Q14.45 7.4 11.65 8.9Q9.25 10.35 10.85 11.7Q12.35 12.65 14.15 11.45',
      'philippine-peso':'M5.25 14V2.15H8.8C14.5 2.15 14.5 10.15 8.8 10.15H5.25M2.15 4.65H14.35M2.15 7.3H14.35',
      'saudi-riyal':'M5.6 2.4V9.7L2.1 10.8M10.1 1.6V11.9L13.9 10.8M2.6 6.6L13.9 3.6M5.6 8.7L14 6.4M9.7 14.3L14 13.1',
    }
    for n,d in currencies.items():
        if n in scope:g(n,d)
    # Native centre lines leave room for the bowls and parallel crossbars.
    small_currency={
        'cent':'M10.3 5.55C6.8 3.5 4.5 7.3 5.9 9.8Q7.45 12.15 10.15 10.3M8.85 4L7.2 12',
        'dollar-sign':'M10.45 5.55C8.45 3.7 5.55 4.8 5.65 6.35C5.75 8.45 10.5 7.6 10.5 9.8C10.45 11.8 7.25 12.1 5.5 10.45M8 3.9V12.1',
        'euro':'M10.45 4.95C6.2 2.95 4.95 8.35 6.75 10.6Q8.2 12.3 10.4 10.85M4.8 6.85H8.8M4.8 9.05H8.5',
        'indian-rupee':'M5.35 4.7H10.65M5.35 7H10.65M7.1 4.7Q10.2 6.95 7.85 8.7Q6.95 9.25 5.65 9.05L9.8 12',
        'japanese-yen':'M5.4 4.45L8 7.95L10.6 4.45M8 7.95V12.05M5.6 8H10.4M5.6 10.15H10.4',
        'pound-sterling':'M10.1 5.3C8.1 3.65 6.7 5 6.8 6.85L7 9Q7 10.5 5.65 11.25H10.25M5.35 8.05H9.25',
        'russian-ruble':'M6.25 12V4.5H8.7C12 4.5 12 8 8.7 8H5M5 10.25H9.35',
        'swiss-franc':'M6.5 11.8V4.6H10.65M6.5 7.45H10M5 10H8.75',
        'turkish-lira':'M7 4.15V11.8Q10.55 11.75 11.05 8.85M4.95 7.05L9.2 5.45M4.95 9.3L9.2 7.7',
    }
    def currency_mark(kind):
        return st(tr(p(small_currency[kind]),scale=.91))

    g('currency',un(st(ci(8,8,4)),st('M2 2L5 5M11 11L14 14M2 14L5 11M11 5L14 2')))
    for typ in ('euro','pound-sterling'):
        s('circle-'+typ,ci(),currency_mark(typ))
    badge_body=api['badge_body']()
    for typ in small_currency:
        s('badge-'+typ,badge_body,currency_mark(typ))
    s('badge-percent',badge_body,un(st('M5.7 10.3L10.3 5.7'),dots((5.8,5.8),(10.2,10.2),r=.75)))
    receipt=p('M3.05 1.7L5.55 2.65L8 1.7L10.45 2.65L12.95 1.7V14.3L10.45 13.35L8 14.3L5.55 13.35L3.05 14.3Z')
    for typ in small_currency:
        if typ!='dollar-sign':
            s('receipt-'+typ,receipt,currency_mark(typ))
    s('receipt-text',p('M3 1L5 2L7 1L9 2L11 1L13 2V15L11 14L9 15L7 14L5 15L3 14Z'),'M5 5H11M5 8H11M5 11H9')
    for n,typ in [('banknote-check','check'),('banknote-x','x')]:badge(n,'banknote',api['check'](12.35,13.4,.58) if typ=='check' else api['cross'](13.05,12.8,.75),offset=(0,-1.85))
    for kind in ('down','up'):
        arrow=st('M12.7 9.65V14.55M10.65 12.5L12.7 14.55L14.75 12.5' if kind=='down' else
                 'M12.7 14.55V9.65M10.65 11.7L12.7 9.65L14.75 11.7')
        badge('banknote-arrow-'+kind,'banknote',arrow,rr(10.3,9.45,4.6,5.35),offset=(0,-1.85))
    s('credit-card-reader',rr(3.3,5.4,9.4,8.9),'M5.4 5.4V1.9H11V5.4M5.5 3.6H10.9M5.1 7.5H10.9M5.6 10H6.4M9 10H9.8M5.6 12.1H6.4M9 12.1H9.8')
    s('smartphone-nfc',rr(1.65,1.65,7.55,12.7),st('M1.75 10.75H9.1M4.65 12.6H6.2M11.35 6.1Q12.85 8 11.35 9.9M13.05 4.35Q16.15 8 13.05 11.65'))
    s('hand-coins','M1.7 10.1L4 9.7L6 8.1Q6.6 7.7 7.4 7.9L9.3 8.4Q10.8 8.9 9.8 10.1L8 10.4L12.9 8.5Q14.1 8.2 14.3 9.2Q14.5 10 13.7 10.6L8.4 13.9Q7.8 14.3 6.8 14.1L2.4 13.3Z','M6 10.5L8 10.4M4.3 5.4A1.7 1.7 0 1 0 4.3 2A1.7 1.7 0 1 0 4.3 5.4ZM10.3 5.3A1.5 1.5 0 1 0 10.3 2.3A1.5 1.5 0 1 0 10.3 5.3Z')
    s('cap','M2.1 9.75V8.05C2.1 1.4 11.7 1.4 11.7 8.05V9.75Z','M6.9 3.25V7.7M6.7 9.75H14.5Q13.6 12.4 10.6 12Q8.05 11.75 6.7 9.75Z')
    s('handbag','M3 5H13L14 14H2Z','M5 5V3Q8-1 11 3V5M5 7V9M11 7V9')
    s('perfume-bottle',rr(3,6,10,8),'M6 6V3H10V6M5 3H11V1H5ZM6 9H10V12H6Z')
    s('shirt','M5 2L1 5L3 8L5 7V14H11V7L13 8L15 5L11 2Q8 6 5 2Z')
    for kind in ('minus','plus'):
        symbol=api['plus'](8.6,7,.61) if kind=='plus' else ln((7.25,7),(9.95,7))
        face_mark('shopping-cart-'+kind,'shopping-cart',symbol)
    # Buildings distinguish rooflines, circulation, and specific functions.
    buildings={
      'brick-wall':(rr(1.6,2.1,12.8,11.8), 'M1.6 6H14.4M1.6 10H14.4M5.35 2.1V6M10.65 2.1V6M8 6V10M5.35 10V13.9M10.65 10V13.9'),
      'castle':('M1.65 3H4.25V5.8H6.65V3H9.35V5.8H11.75V3H14.35V13.95H1.65Z', 'M6.3 13.95V10.95Q8 8.55 9.7 10.95V13.95'),
      'church':('M3 13.95V7.55L8 4.25L13 7.55V13.95Z', 'M8 1.4V4.25M6.25 2.65H9.75M6.35 13.95V10.55Q8 8.1 9.65 10.55V13.95'),
      'dam':('M7.5 3.7H10.8L14.3 13.5H6.3Z', 'M1.5 6.3Q3 5.1 4.5 6.3T7.2 6.3M1.5 9.8Q3 8.6 4.5 9.8T6.7 9.8M9.1 3.7L10.9 13.5'),
      'dome':('M2.4 9.6C2.7 5.8 5 3.2 8 3.2C11 3.2 13.3 5.8 13.6 9.6V13.3H2.4Z', 'M1.5 9.6H14.5M8 1.6V3.2M5.3 9.8V13.2M10.7 9.8V13.2'),
      'door-stairwell':(rr(2,1,12,14),'M4 12H7V9H10V6H12'),
      'factory':('M1.65 13.95V7.85L5.05 5.05V7.75L8.6 5.05V8.15H11.05V2.05H14.35V13.95Z', 'M4.25 10.4V11.55M7.75 10.4V11.55M11.5 10.4V11.55'),
      'hotel':(rr(2.5,1.7,11,12.55), 'M6.05 4.3V8.65M9.95 4.3V8.65M6.05 6.5H9.95M6.4 14.15V11.15H9.6V14.15'),
      'lighthouse':('M5 5H11L12 14H4Z','M4 5H12M5 5V2H11V5M4 2L8 1L12 2M5 8H11M4.5 11H11.5M1 4H3M13 4H15'),
      'mosque':('M4.15 9.05C4.15 6.9 6.15 5.1 8 3.7C9.85 5.1 11.85 6.9 11.85 9.05V13.85H4.15Z', 'M1.6 13.85V5.55L2.85 2.5L4.1 5.55H1.6M14.4 13.85V5.55L13.15 2.5L11.9 5.55H14.4M1.6 13.85H4.15M11.85 13.85H14.4M6.65 13.85V11Q8 8.85 9.35 11V13.85'),
      'school':('M1.8 14.05V7.95H4.35V4.35L8 1.6L11.65 4.35V7.95H14.2V14.05Z', un(st('M6.25 14.05V10.35H9.75V14.05'),st(ci(8,5.75,1.85)),ln((8,5.75),(8.8,5.05)))),
      'university':('M1.65 5.95L8 1.65L14.35 5.95Z', 'M1.75 14.1H14.25M2.6 12.35H13.4M3.4 6V12.35M6.35 6V12.35M9.65 6V12.35M12.6 6V12.35'),
      'warehouse':('M1 14V6L8 2L15 6V14Z','M4 14V8H12V14M4 10H12M4 12H12'),
    }
    for n,(b,d) in buildings.items():s(n,b,d)
    mask_back=p('M1.65 2.2H9.1V7.1Q9.1 9.25 5.4 11Q1.65 9.25 1.65 7.1Z')
    mask_front=p('M8.2 6.05H14.65V10.75Q14.65 12.95 11.425 14.6Q8.2 12.95 8.2 10.75Z')
    expressions=un(dots((3.6,4.8),(7.05,4.8),(10,8.65),(12.85,8.65),r=.55),
                   st('M2.95 6.9Q4 8.65 5.15 6.9M10.05 11.7Q11.425 10.15 12.8 11.7'))
    stack('theater',[mask_back,mask_front],expressions)
    g('utility-pole','M8 1V15M2 3H14M4 6H12M3 2V4M13 2V4M5 5V7M11 5V7')
    house_badge('house-cog',tr(cog,dx=.8,dy=.47))
    house_badge('house-plus',api['plus'](12.85,12.8,.85))
    plug=st('M11.65 9.8V11.6M14.05 9.8V11.6M10.9 11.6H14.8Q14.7 13.75 12.85 13.75Q11 13.75 10.9 11.6ZM12.85 13.75V14.75')
    house_badge('house-plug',plug)
    house_face=drawings['home'][0]
    rear_house=tr(house_face,scale=.73,dx=-2.35,dy=-1.75)
    front_house=tr(house_face,scale=.74,dx=2.15,dy=1.8)
    stack('houses',[rear_house,front_house],st('M9 14.2V10.9H11.45V14.2'))
    transport={
      'bus-front':(rr(3,2,10,11), un(st(rr(4.5,5.15,7,3.6)),st('M3.05 3.9H12.95'),dots((5.5,10.7),(10.5,10.7),r=.68),st('M4.5 13V14.4M11.5 13V14.4M1.5 5.2V7.2M14.5 5.2V7.2'))),
      'car-battery':(rr(2,4.4,12,9.2), un(st('M3.55 4.4V2.1H6.6V4.4M9.4 4.4V2.1H12.45V4.4'),st('M4.1 8.9H7.1M5.6 7.4V10.4M9.5 8.9H12'))),
      'caravan':('M1.7 4H10.3Q12.8 4 13.1 7.1V11.8H1.7Z', 'M13.1 10.5H14.6M3.7 6.1H6.3V8.8H3.7ZM8.4 10.3V6.1H10.9V10.3'),
      'cable-car':(rr(3,6,10,8),'M1 1L15 4M8 2.5V6M3 10H13M8 6V10'),
      'engine':('M3.5 5.3H8.4L9.2 4.3H11.2V6.1H13.9V11.9H3.5V10H1.8V7.4H3.5Z', 'M3.55 7.4V10M5.9 5.3V3.3M4.1 3.3H7.7M8.2 6.6L6.8 8.7H9L7.9 10.3'),
      'ev-charger':(rr(2,2.1,7.6,11.9), 'M4 5H7.5M6.6 7.6L4.7 9.5H7L5.4 11.7M9.6 6.3Q11.8 6.3 11.8 8.5V11.6Q12.9 14 14.2 11.6V7M14.2 7L12.6 5.6V3.5L14.2 5Z'),
      'forklift':('M1.5 7.7H4.5L5.7 9.1H8V10.7H1.5Z', 'M2.1 7.7V3.5H6.4L8 9.1M10.2 3V11.6H14.3'),
      'helicopter':('M6.2 7.7Q6.5 5.8 9.2 5.8C12 5.8 13.9 7.5 14.4 10.3Q14.6 11.5 13.2 11.5H8.6Q6.8 11.5 6.2 9.8L2.2 8.2V6.7Z', 'M9.1 5.8V3M4.3 3H14.1M2.2 7.5L1.55 4.9M2.2 7.5L2.9 10M9.7 5.9L11 9H14M8.6 6V11.5M8.4 11.5V13.7M12.4 11.5V13.7M6.9 13.7H14.2'),
      'hot-air-balloon':('M8 1.5C4.65 1.5 2.2 3.5 2.2 6.05Q2.2 8.55 6.1 10.8H9.9Q13.8 8.55 13.8 6.05C13.8 3.5 11.35 1.5 8 1.5Z', 'M6.1 10.8L6.6 12.55H9.4L9.9 10.8M6.5 12.55V14.35H9.5V12.55M8 1.5C4.9 4.65 5.15 7.65 8 10.8C10.85 7.65 11.1 4.65 8 1.5M2.25 5.95H13.75'),
      'parking-meter':('M4.2 5.2C4.2.2 11.8.2 11.8 5.2V10.9H4.2Z', 'M8 10.9V14.4M6 5.8Q8 2.4 10 5.8ZM6.6 8.3H9.4'),
      'road':('M5 1H11L15 15H1Z','M8 3V5M8 8V10M8 13V15'),
      'sailboat':('M1 11H15L12 15H4Z','M8 11V1L14 9H8M6 3L2 9H6Z'),
      'ship-cargo':('M1.6 10.2H14.4L12.4 13.8H4.4Z', 'M2.5 10.2V7.2H9.35V10.2M5.9 7.2V10.2M3.4 7.2V4.55H6.75V7.2M11.05 10.2V3.6H13.7V10.2'),
      'tractor':('M1.75 7.1V2H7.3L8.2 6.6H12.75Q14.2 6.6 14.2 8V9.4H8.8L7.4 10.3Q6.45 7.2 3.9 7.1Z', 'M1.75 5.3H7.95M5.1 2V5.3M8.2 6.6V9.9M11.5 6.6V4.3M11.1 6.65V9.4'),
      'traffic-cone':('M7.05 1.8H8.95L12.75 12.8H3.25Z', 'M5.7 5.75H10.3M4.5 9.15H11.5M1.65 14.65H14.35'),
      'trailer':(rr(1.7,4,10.4,7.7), 'M12.1 9.1L14.6 10.7M4.3 6.3H9.4V9.7H4.3Z'),
      'train-front-tunnel':(rr(4.45,5.35,7.1,7.05), un(st('M1.65 13.25V7.1C1.65-.15 14.35-.15 14.35 7.1V13.25M5.8 12.4L4.75 14.5M10.2 12.4L11.25 14.5M4.5 8.8H11.5'),dots((6.65,10.6),(9.35,10.6),r=.55))),
      'tram-front':(rr(3,3.4,10,9.4), un(st(rr(4.5,5,7,3.4)),dots((5.4,10.5),(10.6,10.5),r=.68),st('M8 3.4V1.6M5.5 1.6H10.5M5.1 12.8L3.6 14.4M10.9 12.8L12.4 14.4'))),
      'van':('M1.7 4.5H9.9L14.2 8.3V11.9H1.7Z', 'M1.9 8.6H14M7.4 4.6V11.9'),
    }
    for n,(b,d) in transport.items():s(n,b,d)
    car_body=p('M2 8.45L4.15 4.25H11.85L14 8.45V12.55H2Z')
    lamps=st('M4.05 10.55H5.35M10.65 10.55H11.95')
    tires=st('M3.3 12.55V14.15M12.7 12.55V14.15')
    windshield=p('M4.8 5.05H11.2L12.85 8.75H3.15Z')
    for name in ('car-front','car-taxi-front'):
        roof_sign=st('M5.7 4.25V1.95H10.3V4.25') if name=='car-taxi-front' else po.Path()
        s(name,car_body,un(roof_sign,tires,lamps,st('M2 8.45H14')))
        chassis=un(drawings[name][0],st(drawings[name][0]),roof_sign,tires)
        overrides[name]={'solid':op(chassis,un(windshield,lamps),po.PathOp.DIFFERENCE)}
    for n in ['tractor']:
        b,d,o,c,t=drawings[n];drawings[n]=(b,un(d,st(ci(4,11.6,2.55)),st(ci(12.2,12.1,1.8))),o,c,t)
    b,d,o,c,t=drawings['forklift']
    drawings['forklift']=(b,un(d,dots((2.9,13),(7.2,13),r=1.25)),o,c,t)
    s('baggage-claim',rr(3.5,4.9,9,5.9),'M6 4.9V2H10V4.9M2.4 12.2H13.6Q15.2 13.4 13.6 14.4H2.4Q.8 13.4 2.4 12.2Z')
    s('circle-gauge',ci(),un(st('M4.65 8.9A3.35 3.35 0 0 1 11.35 8.9M8 9.35L10.35 7'),ci(8,9,.8)))
    s('octagon-minus',poly([(5.25,1.65),(10.75,1.65),(14.35,5.25),(14.35,10.75),(10.75,14.35),(5.25,14.35),(1.65,10.75),(1.65,5.25)]),st('M4.65 8H11.35'))
    g('drone',un(
        *(st(ci(x,y,2.25)) for x,y in [(4,4),(12,4),(4,12),(12,12)]),
        st('M4 4L12 12M4 12L12 4'),ci(8,8,1.25)))
    g('moped',un(st(ci(3.6,11.9,2)),st(ci(12.25,11.9,2)),st('M1.7 8.8Q2.2 5.8 5.5 6L6.6 8.8ZM2.75 3.9H5.65M4.75 3.9V6.05M3.6 8.8V11.9M6.6 8.8L7.3 10.6H9.1L11 6.3L10.3 3H8.6M11 6.3L12.25 11.9')))
    g('motorbike',un(st(ci(3.65,11.9,2)),st(ci(12.35,11.9,2)),st('M2.1 6L5.5 6.9L6.9 5.45Q8.6 4.6 10.3 6.2L9 8.6H6.7L5.5 6.9M10.3 6.2L9.6 3.15H11.5M10.3 6.2L12.35 11.9M3.65 11.9L6.7 8.6L8.5 11.3H9.6')))
    g('scooter',un(st(ci(3.35,12.35,1.85)),st(ci(12.55,12.35,1.85)),st('M3.35 12.35H8.4L10.95 7.95M5.2 12.35V10.55H9.45M12.55 12.35L9.25 2.35H7')))
    g('ship-wheel',un(st(ci(8,8,4.5)),ci(8,8,1),st('M8 1V15M1 8H15M3 3L13 13M3 13L13 3')))
    g('train-track',st('M5.9 1.65L3.2 14.4M10.1 1.65L12.8 14.4M4.35 3.6H11.65M3.75 6.15H12.25M2.9 9.45H13.1M1.65 13.35H14.35'))
    truck_body,truck_detail,*_=drawings['truck']
    s('truck-electric',truck_body,un(truck_detail,st('M6.6 4.8L4.5 7.1H6.7L4.65 9.6')))
    # Rotate the unexpanded airframe before outlining the wing and tail edges.
    for n,angle,dy in [('plane-takeoff',60,-1.9),('plane-landing',120,-.2)]:
        plane_body=tr(drawings['plane'][0],angle,.77,0,dy)
        s(n,plane_body,ln((2,14.1),(14,14.1)))
    ticket_face=drawings['ticket'][0]
    ticket_marks={
        'minus':ln((6.15,8),(8.15,8)),
        'plus':api['plus'](7.15,8,.5),
        'check':ln((5.95,7.95),(6.85,8.95),(8.5,7.1)),
        'x':api['cross'](7.1,8,.47),
    }
    for kind,symbol in ticket_marks.items():
        face_mark('ticket-'+kind,'ticket',symbol)
    percent=un(st('M5.3 10.2L8.15 5.8'),dots((5.25,5.85),(8.1,10.15),r=.56))
    face_mark('ticket-percent','ticket',percent)
    off('ticket-slash','ticket',min_fragment_area=.65)
    front_ticket=tr(ticket_face,scale=.86,dx=.65,dy=1.6)
    back_ticket=tr(ticket_face,scale=.83,dx=-.3,dy=-1.5)
    # The notches are cut through the stack; the rear edge cannot show through.
    front_mask=rr(0,3.75,16,12,0)
    def ticket_stack(name,detail):
        stack(name,[back_ticket,front_ticket],detail,front_mask=front_mask)
    ticket_stack('tickets',st('M10.15 7.8V8.65M10.15 10.55V11.4'))
    plane_mark=st('M8.65 7.35V11.6M6.85 9.8L8.65 8.6L10.45 9.8M7.8 11.95L8.65 11.4L9.5 11.95')
    ticket_stack('tickets-plane',plane_mark)
    # Travel infrastructure and destination cues.
    g('bridge','M1 13H15M3 3V15M13 3V15M3 4Q8 13 13 4M5 7V13M8 9V13M11 7V13')
    s('briefcase-business',rr(2,5.2,12,8.7),un(st('M5.3 5.2V2.3H10.7V5.2M2.2 8.1Q4.2 9.1 6.7 9.1M9.3 9.1Q11.8 9.1 13.8 8.1'),rr(6.7,8.3,2.6,1.9)))
    bag_face,bag_detail,*_=drawings['briefcase']
    s('briefcase-plus',bag_face,un(bag_detail,api['plus'](13.45,2.55,.6)))
    s('briefcase-conveyor-belt',rr(3.1,4.6,9.8,6.6),'M5.8 4.6V2H10.2V4.6M3 11.2H13C15 11.2 15 14.4 13 14.4H3C1 14.4 1 11.2 3 11.2ZM5.3 11.2V14.4M10.7 11.2V14.4')
    s('cigarette',rr(1,9,13,4),'M5 9V13M11 7Q13 5 11 3M14 7Q16 5 14 2')
    off('cigarette-off','cigarette')
    s('concierge-bell','M2.25 11.65C2.25 2.55 13.75 2.55 13.75 11.65Z','M1.65 14H14.35M8 4.85V2.45M6.45 2.45H9.55')
    s('parasol','M1 8Q8-3 15 8Z','M8 8V14M5 14H11M8 2Q4 5 4 8M8 2Q12 5 12 8')
    g('tent-tree',st('M1.55 14.05L6.15 5.05L10.75 14.05ZM4.25 14.05L6.15 10.1L8.05 14.05M10.25 8.1L12.5 2L14.75 8.1ZM12.5 8.1V12.85'))
    s('tower-control', 'M2.4 3H13.6L11.2 8.1H4.8Z', 'M1.7 3H14.3M6.5 8.1V13.8M9.5 8.1V13.8M4.9 13.8H11.1M6.6 3.1L7 7.9M9.4 3.1L9 7.9')
    # Human gestures and expression changes, with facial counters in Solid.
    for n,d in [('face-angry','M4.6 4.65L6.6 5.65M9.4 5.65L11.4 4.65M5.65 11.6Q8 9.45 10.35 11.6'),('face-expressionless','M4 6H6M10 6H12M5 11H11'),('face-grinning','M4.7 9H11.3Q10.6 12 8 12Q5.4 12 4.7 9Z')]:
        s(n,ci(),un(st(d),dots((5.3,7.9),(10.7,7.9),r=.55) if n=='face-angry' else dots((5,6),(11,6),r=.55) if n!='face-expressionless' else po.Path()))
    badge('face-slightly-smiling-plus','smile',api['plus'](13.35,13.35,.72),offset=(-.7,-.7))
    s('balloon','M8 1.65C11.25 1.65 13.1 3.9 13.1 6.45C13.1 9.4 10.8 11.8 8 12.5C5.2 11.8 2.9 9.4 2.9 6.45C2.9 3.9 4.75 1.65 8 1.65Z','M8 12.5L7.15 13.65H8.85ZM8 13.65Q8.7 15.05 10.45 14.35')
    s('biceps-flexed','M2 11.6L3.3 6.3Q3.6 5.1 4.4 3.8L5.3 2.4Q5.8 1.7 6.7 1.9L8.1 2.2Q9.2 2.5 8.9 3.6L8.6 4.6Q8.4 5.2 7.6 5.1L6.5 4.9L6.2 8.3C8.4 6.2 11.2 6.5 12.1 8.6Q14.1 8.3 14.2 10.7C14.3 13.2 11.6 14.2 8.2 14Q4.1 14 2 12.6Z','M6.2 8.3Q5.6 9.3 5.5 10.5')
    s('hand-helping','M1.7 11.1L4.3 10.5L6.1 8.5Q6.8 7.7 7.6 8.4Q8 8.9 7.6 9.6L6.9 10.6L9.7 9.7Q11 9.4 11 10.4Q11 10.9 10.3 11.4L7.2 13.6Q6.5 14.1 5.5 14L2 13.5Z','M14.1 2.4L10.8 2.5Q9.4 2.5 8.3 3.5L5.3 6.1Q4.9 6.7 5.7 7.1L9 5.3M9 5.3Q8.6 7 9.6 7Q10.3 7.2 11.1 6.3L12.6 4.9L14.3 4.8')
    s('hand-metal','M3.15 9.05V2.85C3.15 1.15 5.5 1.15 5.5 2.85V7.45Q6.35 5.2 7.95 6.95Q9.3 5.3 10.45 7.25V2.75C10.45 1.05 12.95 1.05 12.95 2.75V10.75Q12.95 14.35 9.1 14.35H6.95Q4.55 14.35 3.45 12.45L1.75 9.95Q1.15 8.45 2.25 8.3Q2.85 8.3 3.15 9.05Z','M5.5 7.45V9.9M7.95 6.95V9.35')
    s('heart-crack','M8 14.15L2.55 8.5C-.55 4.25 4.55 .45 8 4.25C11.45 .45 16.55 4.25 13.45 8.5Z','M8 4.25L6.45 7.2L9.3 9.1L8 14.15')
    s('heart-handshake','M8 14L2.8 9C-1 5.1 3.8-.2 8 4.1C12.2-.2 17 5.1 13.2 9Z','M8 4.1L5.6 6.4Q4.9 7.2 5.7 7.9Q6.4 8.5 7.3 7.8L8.9 6.6L12.4 9.7M6.2 8.9L9.8 12.15M8.7 8.6L11.4 10.85')
    # Rotate the cone and its elliptical opening together before outlining them.
    lip=ci(8,6.15,1).transform(3.55,0,0,1.65,8-8*3.55,6.15-6.15*1.65)
    cone=p('M4.45 6.15L8 14.35L11.55 6.15Z')
    def tilt_cone(face):
        return tr(face,38,dx=-1.9,dy=1.1)
    confetti=un(st('M8.7 4.15L9.85 1.9M11.8 7.15L14.4 5.95M11.95 3.55Q13.65 3.95 14.1 1.85'),dots((4.7,2.55),(14.15,10.45),r=.62))
    body=tilt_cone(un(cone,lip))
    opening=tilt_cone(lip)
    s('party-popper',body,un(st(opening),confetti))
    overrides['party-popper']={'solid':un(op(un(body,st(body)),opening,po.PathOp.DIFFERENCE),confetti)}
    # Weather compositions separate foreground clouds from sun/moon backgrounds.
    def cloud(scale,dx,dy):
        return tr(drawings['cloud'][0],scale=scale,dx=dx,dy=dy)
    rain=st('M4.85 11.75L4.05 13.65M7.7 11.75L6.9 13.65M10.55 11.75L9.75 13.65')
    for n,detail in [
        ('cloud-drizzle',dots((4.5,12.2),(7,14.25),(9.5,12.2),(12,14.25),r=.55)),
        ('cloud-hail',dots((4.4,13),(8,13),(11.6,13),r=.82)),
        ('cloud-rain-wind',st('M4.3 11.45L3.3 13.55M7.25 11.45L6.25 13.55M9.1 12H12.8Q14.7 12 14.05 10.25M9.1 14.5H12.85')),
    ]:
        s(n,cloud(.85,0,-2.15),detail)
    for wet in (False,True):
        y=-1.3 if wet else .55
        front=cloud(.70,-1.7,y)
        moon=tr(drawings['moon'][0],scale=.67,dx=2.6,dy=-2.25)
        stack('cloud-moon'+('-rain' if wet else ''),[moon,front],exterior=rain if wet else None)
        sun=ci(10.35,5.95,2.7)
        rays=st('M10.35 1.3V1.85M13.3 3L13.85 2.45M14.45 5.95H14.75')
        stack('cloud-sun'+('-rain' if wet else ''),[sun,front],exterior=un(rays,rain) if wet else rays)
    stack('cloudy',[cloud(.70,1.87,-2.05),cloud(.73,-1.52,1.75)])
    off('droplet-off','droplet');off('umbrella-off','umbrella')
    drops=[tr(drawings['droplet'][0],scale=.65,dx=-2.7,dy=1.8),
           tr(drawings['droplet'][0],scale=.43,dx=3.3,dy=-3.15)]
    stack('droplets',drops)
    solar_rays=st('M8 1.35V2.15M3.95 2.95L4.65 3.65M12.05 2.95L11.35 3.65M2 6.9H3M13 6.9H14')
    s('haze','M4.45 8.35A3.55 3.55 0 1 1 11.55 8.35Z',un(solar_rays,st('M1.8 10.95H14.2M3.4 13.6H12.6')))
    def snow(cx,cy,r):
        arm=ln((8,8),(8,8-r))
        return un(*(tr(arm,angle,dx=cx-8,dy=cy-8) for angle in range(0,360,60)))
    def sunlight(cx,cy):
        ray=st('M8 3.3V4.2')
        return un(*(tr(ray,angle,dx=cx-8,dy=cy-8) for angle in (0,45,180,225,270,315)))
    s('sun-snow',ci(5.95,6,2.25),un(sunlight(5.95,6),snow(11.35,11.5,3.2)))
    thermometer=p('M3.25 3.25A1.55 1.55 0 0 1 6.35 3.25V9.45A2.85 2.85 0 1 1 3.25 9.45Z')
    for kind in ('sun','snowflake'):
        symbol=un(st(ci(11.35,5.6,1.8)),st('M11.35 1.45V2M11.35 9.2V9.75M8.65 2.9L8.3 2.55M14.05 2.9L14.4 2.55M8.65 8.3L8.3 8.65M14.05 8.3L14.4 8.65')) if kind=='sun' else snow(11.35,6.4,3.35)
        s('thermometer-'+kind,thermometer,un(st('M4.8 5.85V11.35'),symbol))
    g('tornado','M1 2H15M3 5H13M5 8H11M7 11H12M8 14H10')
    g('waves-horizontal','M1 3Q4 1 7 3T15 3M1 8Q4 6 7 8T15 8M1 13Q4 11 7 13T15 13')
    g('waves-vertical','M3 1Q1 4 3 7T3 15M8 1Q6 4 8 7T8 15M13 1Q11 4 13 7T13 15')
    for direction in ('down','up'):
        arrow=st('M12.05 8.9V14.55M9.7 12.2L12.05 14.55L14.4 12.2' if direction=='down' else
                 'M12.05 14.55V8.9M9.7 11.25L12.05 8.9L14.4 11.25')
        wave=st('M1.6 3.3Q4.45 1.45 7.8 3.3T14.4 3.3M1.6 7.6Q4.45 5.75 7.8 7.6M1.6 11.9Q4.45 10.05 7.8 11.9')
        gust=st('M1.6 5H10.6Q13.85 5 13 2.9Q12.3 1.4 10.7 2.3M1.6 8.5H8M2 11.55H5.55Q8.55 11.55 7.75 13.65Q7 15.1 5.65 14')
        g('waves-arrow-'+direction,un(wave,arrow))
        g('wind-arrow-'+direction,un(gust,arrow))
    # Add the running gear before deriving the Solid window cutouts.
    for n,centers in {'caravan':[(4,12.5),(11,12.5)],'trailer':[(4,12.5),(11,12.5)],'van':[(3.5,13),(12,13)]}.items():
        b,d,o,c,t=drawings[n]
        wheels=un(*(ci(x,y,1.35) for x,y in centers))
        drawings[n]=(b,un(d,wheels),o,c,t)
    for n,counters in {
        'van':un(rr(2.75,5.35,3.65,2.35),p('M8.3 5.4H9.65L12.3 7.8H8.3Z')),
        'tram-front':rr(4.5,5,7,3.4),
        'bus-front':rr(4.5,5.15,7,3.6),
        'leafy-green':st('M4.3 11.7L10.65 5.15M6.5 9.4L6.4 6.9M6.5 9.4L9.4 9'),
        'turtle':shell_seams,
        'squirrel':st('M6.95 8.75Q5.3 9.35 5.85 11.7M11.9 6.6H12.15'),
        'feather':st('M4.4 11.2Q7 8.4 10.3 5.6'),
        'helicopter':p('M9.8 6.8Q12.1 7 13 8.7H10.7Z'),
        'cable-car':un(rr(4.4,7.4,2.9,2),rr(8.7,7.4,2.9,2)),
        'tower-control':st('M6.6 3.4L7 7.7M9.4 3.4L9 7.7'),
    }.items():
        duo,solid,mono=base_layers(n)
        overrides.setdefault(n,{})['solid']=op(solid,counters,po.PathOp.DIFFERENCE)
    hull=p('M8 1.4C12.6 4.75 12.6 11.25 8 14.6C3.4 11.25 3.4 4.75 8 1.4Z')
    cockpit=rr(6.65,5.05,2.7,5.9)
    shaft='M3.45 5.15L12.55 10.85'
    blade=p('M1.45 3.05Q2 2.7 2.8 3.1L4.65 4.45Q5.25 5.05 4.65 5.8Q4.1 6.5 3.25 6.05L1.6 4.55Q1.05 3.9 1.45 3.05Z')
    paddle=un(st(shaft),blade,tr(blade,180))
    s('kayak',hull,un(st(cockpit),paddle))
    hull_fill=op(un(hull,st(hull)),un(cockpit,st(shaft,3.2)),po.PathOp.DIFFERENCE)
    overrides['kayak']={'solid':un(hull_fill,paddle)}
    # Individual fruit masses remain distinct in a solid bunch.
    grape_solid=un(*(ci(x,y,1.85) for x,y in centres))
    overrides['grape']={'solid':un(grape_solid,grape_stem)}
    # Composite surfaces retain a receding body behind their opaque state mark.
    # These explicit surface compositions use glyph storage, not linear semantics.
    api['DUOTONE_GLYPHS'].update({name: 'Receding surface behind an opaque state mark or foreground subject.' for name in {
        'bean-off',
        'beef-off',
        'beer-off',
        'candy-off',
        'carton-off',
        'egg-off',
        'fish-off',
        'hop-off',
        'milk-off',
        'nut-off',
        'wine-off',
        'mop-sparkles',
        'toothbrush-sparkles',
        'door-closed-locked',
        'door-closed-package',
        'door-closed-cog',
        'house-heart',
        'house-wifi',
        'broom-sparkles',
        'shrimp-off',
        'banknote-check',
        'banknote-x',
        'banknote-arrow-down',
        'banknote-arrow-up',
        'shopping-cart-minus',
        'shopping-cart-plus',
        'house-cog',
        'house-plus',
        'house-plug',
        'truck-electric',
        'plane-takeoff',
        'plane-landing',
        'ticket-check',
        'ticket-minus',
        'ticket-plus',
        'ticket-x',
        'ticket-percent',
        'ticket-slash',
        'briefcase-plus',
        'cigarette-off',
        'face-slightly-smiling-plus',
        'cloud-drizzle',
        'cloud-hail',
        'cloud-rain-wind',
        'cloud-sun',
        'cloud-sun-rain',
        'cloud-moon',
        'cloud-moon-rain',
        'cloudy',
        'droplet-off',
        'umbrella-off',
        'droplets',
        'haze',
        'sun-snow',
        'thermometer-sun',
        'thermometer-snowflake',
    }})
    missing=set(NAMES)-set(drawings)
    assert not missing, 'World missing: '+', '.join(sorted(missing))
