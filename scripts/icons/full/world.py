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
        cat(n);shape(n,p(b) if isinstance(b,str) else b,st(d,1.1) if isinstance(d,str) else d)
    def stack(n, planes, detail=None):
        # Mask each rear plane with the complete face in front of it.
        outline=po.Path()
        solid=po.Path()
        for face in planes:
            rim=st(face,1.25)
            outline=un(op(outline,face,po.PathOp.DIFFERENCE),rim)
            clearance=un(face,st(face,3.25))
            solid=un(op(solid,clearance,po.PathOp.DIFFERENCE),face,rim)
        detail=detail or po.Path()
        ink=un(outline,detail)
        surface=un(*planes)
        s(n,surface,ink)
        overrides[n]={'duotone':[(op(surface,ink,po.PathOp.DIFFERENCE),.24),(ink,1)],
                      'stroke':ink,'solid':op(solid,detail,po.PathOp.DIFFERENCE)}

    def base_layers(n):
        b,d,outlined,*_=drawings[n];outer=st(b,1.25) if outlined else po.Path();ink=un(outer,d) if outlined else un(b,d)
        if outlined:
            filled=un(b,outer);interior=op(filled,st(filled,1.8),po.PathOp.DIFFERENCE)
            counters=[];structural=[]
            for part in api['components'](d):
                (structural if op(part,filled,po.PathOp.DIFFERENCE).area>part.area*.12 else counters).append(part)
            solid=un(op(filled,op(un(*counters),interior,po.PathOp.INTERSECTION),po.PathOp.DIFFERENCE),*structural)
            duo=[(op(b,ink,po.PathOp.DIFFERENCE),.24),(ink,1)]
        else:solid=ink;duo=[(ink,1)]
        ov=overrides.get(n,{})
        return ov.get('duotone',duo),ov.get('solid',solid),ov.get('stroke',ink)
    def off(n,base):
        duo,solid,mono=base_layers(base);slash=ln((2,2),(14,14));clear=st('M2 2L14 14',2.65)
        cut=lambda a:op(a,clear,po.PathOp.DIFFERENCE)
        g(n,un(cut(mono),slash));overrides[n]={'duotone':[(cut(a),v) for a,v in duo]+[(slash,1)],'solid':un(cut(solid),slash),'stroke':un(cut(mono),slash)}
    def badge(n,base,mark):
        duo,solid,mono=base_layers(base);f=lambda a:tr(a,scale=.78,dx=-1.1,dy=-1)
        clear=un(mark,st(mark,1.7));cut=lambda a:op(f(a),clear,po.PathOp.DIFFERENCE)
        g(n,un(cut(mono),mark));overrides[n]={'duotone':[(cut(a),v) for a,v in duo]+[(mark,1)],'solid':un(cut(solid),mark),'stroke':un(cut(mono),mark)}
    def mark(kind):
        return {'plus':api['plus'](12,12,.9),'minus':ln((10,12),(14,12)), 'x':api['cross'](12,12,.85),'check':api['check'](12,12,.7),'heart':tr(p('M8 13L2.5 7.5C-1 2 5-1 8 4C11-1 17 2 13.5 7.5Z'),scale=.29,dx=4,dy=4),'percent':un(ci(10.5,10.5,.55),ci(13.5,13.5,.55),ln((10.2,13.8),(13.8,10.2),width=1))}[kind]
    # Foods use distinct silhouettes, with only identifying interior detail.
    food={
      'amphora':('M5.9 1.8H10.1C9.6 3.5 9.6 4.4 10.7 5.8C13 8.7 11.2 12.4 8 14.3C4.8 12.4 3 8.7 5.3 5.8C6.4 4.4 6.4 3.5 5.9 1.8Z',un(st('M5.9 4.2C5.9 5.2 4.5 5 3.4 5C.7 5 1.6 8.6 4.5 9.9',1.15),api['mirror'](st('M5.9 4.2C5.9 5.2 4.5 5 3.4 5C.7 5 1.6 8.6 4.5 9.9',1.15)))),
      'avocado':('M8 1C11 1 10 5 13 8C16 13 11 15 8 15C3 15 1 12 3 8C6 5 5 1 8 1Z',None),
      'bacon':('M5 1Q7 3 9 1L11 3Q9 6 11 9L9 15Q7 13 5 15L3 13Q5 10 3 7Z','M6 3Q4.5 7 6 9Q7 11 6 13M8 3Q6.5 7 8 9Q9 11 8 13'),
      'barrel':('M4 2Q1 8 4 14H12Q15 8 12 2Z','M3 5H13M3 11H13M6 2Q4.5 8 6 14M10 2Q11.5 8 10 14'),
      'bean':('M11 2C16 2 15 9 11 12C7 16 1 15 1.5 10C2 6 6 9 7 6C7 3 8 2 11 2Z','M5 11Q10 11 11 6'),
      'beef':('M2.1 7Q1.8 4 4.8 3.4L10.4 2.3C14.5 1.6 16.1 6.7 12.6 8.7L10.1 10.2Q9 14.3 5.8 13.8C2.7 13.5 2 10.4 2.1 7Z',un(st(ci(10.9,5.4,1.3),1.15),st('M4.3 7.6Q4.3 10.6 6.4 11',1.15))),
      'beer':('M3 5H11V14H3Z','M11 6H13Q15 6 15 9Q15 12 11 12M5 7V12M8 7V12M3 5C0 2 4 0 6 2C8 0 11 1 11 5'),
      'blender':('M3 2H12L11 10H5Z','M5 10L3 14H13L11 10M12 3H14V7H12M6 5H8M7 12H9'),
      'bottle-wine':('M6 1H10V5Q13 7 13 9V14H3V9Q3 7 6 5Z','M6 3H10M3 9H13'),
      'broccoli':('M6 9C2 11 0 7 3 5C1 1 6 0 8 3C10 0 15 1 13 5C16 7 14 11 10 9L11 14H5Z','M6 6L8 9L11 6M8 9V13'),
      'cake-slice':('M1.9 6.9L10.8 3.1Q13.6 4.2 14.1 6.5V12.2L1.9 13Z', 'M1.9 6.9L14.1 6.5M2 9.4Q4 8.5 6 9.2T10 9.1T14 8.6'),
      'can':(rr(4,2,8,12,2),'M4 5H12M4 12H12M7 3.5H9'),
      'can-soda':(rr(4,2,8,12,2),'M4 5H12M4 12H12M7 3.5H9M7 7L9 9L7 10'),
      'candy':('M5 4Q8 2 11 5Q14 8 11 11Q8 14 5 11Q2 8 5 4Z','M4 4L1 2V6L3 7M12 12L15 14V10L13 9M5 5L11 11'),
      'carton':('M5 1H11L14 5V14H2V5Z','M2 5H14M5 1V5M11 1L8 5V14M10 8H12'),
      'cheese':('M2 7L12 2Q15 4 14 7V10Q11 10 12 13L14 14H2Z','M2 7H14M5 10H5.1M8 12H8.1'),
      'citrus':('M2 4.9L14 7.2C13.1 11.4 10.5 13.4 6.7 12.7C3 12 1.4 8.8 2 4.9Z', 'M2.3 5.1C2.4 11.3 10.8 13.5 13.8 7.3M8 6.1L5.3 9.6M8 6.1L9.4 10.6'),
      'cooking-pot':(rr(3,5,10,9,2),'M1 6H3M13 6H15M2 5H14M6 2H10M8 2V5'),
      'croissant':('M1.7 10.3Q1.7 7.8 3.5 6.6Q4 4.1 6.1 4Q7.7 1.9 9.5 3Q11.6 2.8 12.4 5.2Q14.3 6.5 14.1 9Q14.8 11.2 13.4 13.3Q12.3 10.8 10.3 9.2Q8.4 8.2 6.4 9.3Q4.5 10.2 2.2 12.6Q1.6 11.4 1.7 10.3Z', 'M3.5 6.6Q4.4 7 5.1 9.9M6.1 4Q7.4 5.4 7.8 8.6M9.5 3Q11.1 5.2 10.3 9.2M12.4 5.2Q13.1 7.2 12 10.6'),
      'cup-soda':('M3 5H13L11.5 14H4.5Z','M2 5H14M9 5L10 1H13'),
      'cupcake':('M3 8H13L11 14H5Z','M3 8C0 5 3 3 5 4C4 0 9 0 10 3C15 2 16 7 13 8M6 10L7 12M10 10L9 12'),
      'dessert':('M3 8H13V13H3Z','M1 13H15M3 10H13M4 8C1 5 4 3 6 5C6 1 11 2 11 5C14 4 15 7 13 8'),
      'donut':(ci(8,8,6),'M5 4L6 4.5M11 5L12 6M4 10L4.5 11M10 12L11 11.5'),
      'drumstick':('M5.7 8.4C4.4 6.1 5.9 3 8.1 2.1C11.6 .6 14.7 3 14.3 6.3C14 9.4 11.3 11.2 8.2 10.2L5.9 12.2C6.6 14.8 3.3 15.2 3 13C.8 13 .9 9.8 3.6 10.4Z', 'M5.7 8.4Q6.5 9.7 8.2 10.2'),
      'egg':('M8 1C10 1 14 7 14 10C14 17 2 17 2 10C2 7 6 1 8 1Z',None),
      'egg-fried':('M2 6C1 3 5 1 8 3C12 0 15 4 13 7C17 10 14 15 10 13C6 16 2 14 3 11C0 10 0 7 2 6Z',None),
      'glass-water':('M3 2H13L11.5 14H4.5Z','M4 8Q6 6 8 8T12 8'),
      'ham':('M2.5 5.4C3.4 2.5 7.5 1.6 11.2 3.6C14.7 5.4 15.5 8.3 13.4 11.7C11.7 14.6 7.6 14.8 4.3 12.4C1.7 10.5 1.3 8.3 2.5 5.4Z', 'M2.5 5.4C5.6 .7 16.3 7.2 11.3 12.4Q9.8 13.9 7.6 13.7M5.8 7.1C6.4 5.8 8.6 6.4 8.2 7.9C7.7 9.6 5.2 8.6 5.8 7.1Z'),
      'hamburger':('M2 6.7C2.9 .8 13.1 .8 14 6.7ZM2.5 11.8H13.5Q13.2 14 10.9 14H5.1Q2.8 14 2.5 11.8Z', 'M2 9.1H6L8.3 10.2L10 9.1H14'),
      'ice-cream-bowl':('M2 8H14Q13 13 8 13Q3 13 2 8Z','M8 13V15M5 15H11M3 8C0 4 5 1 7 5C8 0 14 2 13 8'),
      'leafy-green':('M3 12C-1 7 4 0 7 3C11-1 16 3 13 6C17 10 12 15 7 13L2 15Z','M4 12L11 5M7 9V6M7 9H10'),
      'lollipop':(ci(6.5,6,4.5),'M9.5 9.5L14 14M5 4Q9 3 8 6Q7 8 5 6'),
      'mango':('M7.4 3.8C10.9 1.9 14.1 4.1 14 7.6C13.9 11.9 8.6 14.7 3.3 13.8Q2.5 13.6 1.6 12.8C4.2 11.6 3.6 6.1 7.4 3.8Z', 'M9.4 3.4Q8.7 1.6 7.3 1.6'),
      'martini':('M2 2H14L8 9Z','M8 9V14M4 14H12M4 5H12'),
      'microwave':(rr(1.5,3,13,10,1.5),'M10.5 3V13M3.5 5.5H8.5V10.5H3.5ZM12.5 6V7M12.5 10H12.6'),
      'milk':('M5 1H11L13 5V14H3V5Z','M3 5H13M5 1V5M10 5V14M5 9H8'),
      'nut':('M3 6.6C2.2 6.5 2.1 5.9 2.5 5C3.5 2.6 5.8 2.2 8 2.2C10.2 2.2 12.5 2.6 13.5 5C13.9 5.9 13.8 6.5 13 6.6L12.4 6.8C12.4 10 10.6 12.6 8 14.3C5.4 12.6 3.6 10 3.6 6.8Z', 'M3.1 6.6Q8 7.3 12.9 6.6M8 2.4Q8.2 1.6 9 1.4'),
      'paper-bag':('M3 3H13V14H3Z','M3 3L5 1L7 3L9 1L11 3L13 1V3M5 6Q8 9 11 6'),
      'popcorn':('M3 6H13L11 14H5Z','M3 6C0 4 2 1 5 3C5 0 9 0 9 3C13 0 16 4 13 6M6 8L7 12M10 8L9 12'),
      'popsicle':(rr(4,1,8,10,3),'M7 11V15H9V11M7 4V8M10 4V8'),
      'salad':('M2 8H14Q13 14 8 14Q3 14 2 8Z','M4 8C0 4 4 1 7 5C7 0 12 1 12 5M9 8Q13 3 15 5M7 5L9 8'),
      'soup':('M2 8H14Q13 14 8 14Q3 14 2 8Z','M5 2Q3 4 5 6M9 1Q7 3 9 5M13 2L10 8'),
    }
    for n,(b,d) in food.items():s(n,b,d)
    # Counters that belong to recognizable ring-like food silhouettes.
    for n,center in [('avocado',ci(8,10,2.5)),('donut',ci(8,8,2.1)),('egg-fried',ci(8,8,2.5))]:
        b,d,outlined,category,tags=drawings[n];drawings[n]=(b,un(d,st(center,1.1)),outlined,category,tags)
        if n=='donut':
            duo,solid,mono=base_layers(n);hole=ci(8,8,1.5);overrides[n]={'duotone':[(op(a,hole,po.PathOp.DIFFERENCE),v) for a,v in duo],'solid':op(solid,hole,po.PathOp.DIFFERENCE),'stroke':mono}
    g('candy-cane','M5 14V5C5 0 13 0 13 5V7H10V5C10 3 8 3 8 5V14ZM5 8H8M5 11H8M7 2L9 4M10 2L12 4')
    g('faucet','M2 8V14M2 10H9V7H14V10M5 10V5H10M7.5 5V2M5 2H10')
    s('fish-symbol','M3 8Q8 0 12 8Q8 16 3 8Z',un(ln((3,8),(1,5),(1,11),(3,8)),ci(9,7,.6)))
    berry=ci(0,0,2.1)
    centres=[(5,5.7),(10.3,5.7),(5.5,9.2),(10,9.2),(7.8,12),(7.8,7.5)]
    berries=[berry.transform(1,0,0,1,x,y) for x,y in centres]
    grape_body=un(*berries)
    grape_edges=po.Path()
    for fruit in berries:
        grape_edges=un(op(grape_edges,fruit,po.PathOp.DIFFERENCE),st(fruit,1.25))
    grape_stem=st('M7.9 4.7Q8.7 1.7 11.7 1.7',1.35)
    s('grape',grape_body,un(grape_edges,grape_stem))
    s('groceries','M2 7H14L12 14H4Z',un(st('M4 7V3H6V7M9 7L11 2L13 3L12 7M6 10V12M10 10V12',1.1),ci(8,6,1.3)))
    s('hand-platter','M2.5 7.8Q2.8 3.2 8 3.2Q13.2 3.2 13.5 7.8Z','M1.6 8H14.4M8 1.6V3.2M1.8 12.2L4.3 11.9L6.1 10.2H9.1Q10.1 10.4 9.4 11.4L7.8 12.2L12.4 10.2Q13.7 9.8 13.8 10.8L9.1 14.1H4.1')
    s('hop','M8 2.1Q10.6 2.3 12.3 4.5L11.9 5.4L13.5 5.3Q13.5 8.3 12 9.4L12.6 9.6Q11.6 12.4 8 14.4Q4.4 12.4 3.4 9.6L4 9.4Q2.5 8.3 2.5 5.3L4.1 5.4L3.7 4.5Q5.4 2.3 8 2.1Z', 'M4.1 5.4Q6.2 5.4 8 7.5Q9.8 5.4 11.9 5.4M4 9.4Q6.5 9.3 8 11.4Q9.5 9.3 12 9.4')
    g('utensils-crossed','M2 1L7 6M1 3L6 8M4 1L8 5Q10 7 7 9L2 14M14 2Q8 4 10 8L14 14M14 2L10 8')
    g('vegan','M2 5L7 14L13 3M8 7Q6 1 14 1Q14 8 8 7')
    g('wheat','M3 14L12 3M6 11Q1 11 2 7Q6 7 6 11ZM8 8Q4 7 5 4Q9 4 8 8ZM10 6Q8 2 11 1Q13 3 10 6ZM6 11Q10 12 11 8Q8 7 6 11ZM9 8Q13 8 14 5Q11 4 9 8Z')
    for n,base in [('bean-off','bean'),('beef-off','beef'),('beer-off','beer'),('candy-off','candy'),('carton-off','carton'),('egg-off','egg'),('fish-off','fish'),('hop-off','hop'),('milk-off','milk'),('nut-off','nut'),('wheat-off','wheat'),('wine-off','wine')]:off(n,base)
    homes={
      'air-vent':(rr(2,2,12,12,1.5),'M4 5H12M4 8H12M4 11H12'),
      'alarm-smoke':('M1.8 3.3Q1.8 2.2 3.3 2.2H12.7Q14.2 2.2 14.2 3.3V4.7C14.2 7.3 1.8 7.3 1.8 4.7Z', 'M4.5 4.1H6.3M9.7 4.1H11.5M5.7 9Q4.2 10.4 5.6 11.7Q6.6 12.8 5.3 14M10.5 8.9Q8.9 10.4 10.3 11.7Q11.2 12.8 10 14'),
      'armchair':('M4 3H12V8H14V13H2V8H4Z','M4 8V10H12V8M4 13V15M12 13V15'),
      'bed-double':('M2 5H14V13H2Z','M2 9H14M8 5V9M4 5V3H12V5M2 13V15M14 13V15'),
      'bed-single':('M2 7.7H11.6Q14 7.7 14 9.8V11.2H2Z', 'M2 4V13.6M14 11.2V13.6M4.2 5.8H6.6'),
      'blinds':(rr(2,2,12,10,1),'M2 5H14M2 8H14M11 2V14M10 14H12'),
      'fence':('M2 3L4 1L6 3V14H2ZM10 3L12 1L14 3V14H10Z','M1 6H15M1 11H15'),
      'fire-extinguisher':('M6 7Q6 5.7 7.5 5.3V4.5H10V5.3Q11.6 5.7 11.6 7V13Q11.6 14.3 10.3 14.3H7.3Q6 14.3 6 13Z', 'M7 4L12.8 2.2M8.5 4.3L12.6 4.8M7.5 4.6Q3 4.2 3 8.3V11M6.2 9H11.4'),
      'heater':(rr(2,4,12,9,1),'M5 6V11M8 6V11M11 6V11M4 13V15M12 13V15M4 1V2M8 1V2M12 1V2'),
      'lamp-ceiling':('M3 7H13L15 11H1Z','M8 1V7M6 13Q8 15 10 13'),
      'lamp-desk':('M6.3 3.2L9.3 1.8L12.9 4.9L7.9 8.2Z', 'M6.5 4.6L3.1 7.5L7.1 13.6M3.7 13.8H11.8'),
      'lamp-floor':('M5 2H11L13 7H3Z','M8 7V14M4 14H12'),
      'lamp-wall-down':('M7 7H13L15 12H5Z','M2 2V9M2 5H10V7'),
      'lamp-wall-up':('M7 7H13L15 2H5Z','M2 6V13M2 10H10V7'),
      'plant-pot':('M4 9H12L11 14H5Z','M8 9V5M8 6Q1 6 3 2Q8 1 8 6ZM8 5Q8 0 13 2Q14 6 8 5Z'),
      'shelving-unit':(rr(2,2,12,12,1),'M2 7H14M2 12H14M5 3V7M8 4V7M5 10V12M11 9V12'),
      'soap-dispenser-droplet':(rr(2,6,7,8,1.5),'M5.5 6V3M3 3H10V5M13 7Q9 11 13 13Q17 11 13 7Z'),
      'solar-panel':('M3 2H13L15 11H1Z','M2 6.5H14M6 2L5 11M10 2L11 11M8 11V14M5 14H11'),
      'towel-rack':('M6 4H12V14H6Z','M1 5H15M2 3V7M14 3V7M6 11H12M8 4V9'),
      'brush-cleaning':('M1.8 7.2H14.2V9.7H1.8Z', 'M4.2 7.2V5.1Q4.2 3.8 5.5 3.8H10.5Q11.8 3.8 11.8 5.1V7.2M2.6 9.7V12.8M5.3 9.7V12.8M8 9.7V12.8M10.7 9.7V12.8M13.4 9.7V12.8'),
      'mop':('M4.7 8.7L7.5 9.4Q8 11.3 10.3 13Q9.4 14.7 7.8 13.6Q6.4 15.1 4.8 13.6Q3 14.7 1.7 13.1Q4.1 11.3 4.7 8.7Z', 'M6.1 9L10.1 1.8M3.9 12.8L5 11.5'),
      'toothbrush':(rr(6,1.5,3,5,1),'M7.5 6.5V14M3.5 2.5H6M3.5 4H6M3.5 5.5H6'),
    }
    for n,(b,d) in homes.items():s(n,b,d)
    g('bubbles',un(st(ci(5,10,4),1.2),st(ci(11,4,2.5),1.2),ci(13,12,1)))
    g('rocking-chair','M4 1V9H12M5 9L3 14M10 9L12 14M1 13Q8 17 15 13M4 6H12V9')
    g('shower-head','M2 3Q3 1 5 2L8 5M5 8L11 2M6 9L5 10M9 9L8 10M12 8L11 9M8 12L7 13M11 11L10 12M14 10L13 11')
    sparkle=un(st('M12 9L12.7 11.3L15 12L12.7 12.7L12 15L11.3 12.7L9 12L11.3 11.3Z',.9))
    shine=p('M12.6 6.5Q13 8.7 15 9.1Q13 9.5 12.6 11.7Q12.2 9.5 10.2 9.1Q12.2 8.7 12.6 6.5Z')
    mop_body,mop_detail,*_=drawings['mop']
    s('mop-sparkles',mop_body,un(mop_detail,shine))
    badge('toothbrush-sparkles','toothbrush',sparkle)
    badge('door-closed-locked','door-closed',un(rr(10,11.5,4,3,.5),st('M11 11.5V10.5A1 1 0 0 1 13 10.5V11.5',1)))
    badge('door-closed-package','door-closed',un(st(rr(10,10,4.5,4.5,.5),1),st('M10 11.5H14.5M12.2 10V12',.9)))
    cog=un(st(ci(12,12,2.1),1),st('M12 8.8V9.8M12 14.2V15.2M8.8 12H9.8M14.2 12H15.2M9.7 9.7L10.5 10.5M13.5 13.5L14.3 14.3M9.7 14.3L10.5 13.5M13.5 10.5L14.3 9.7',1))
    badge('door-closed-cog','door-closed',cog)
    badge('house-heart','home',mark('heart'))
    badge('house-wifi','home',un(st('M9 11Q12 8 15 11M10.5 12.5Q12 11 13.5 12.5',1),ci(12,14,.6)))
    # Hand tools retain characteristic heads and working edges.
    tools={
      'anvil':('M1.4 5.3H7V4H14.5V7.6H11.7Q9.7 9.9 11.8 11.4L13.2 12.4V13H5.3V12.4L6.8 11.4Q8 10 7.5 8.8C4.9 8.8 2.6 7.4 1.4 5.3Z', None),
      'axe':('M5.9 3.7L8.2 2.4L9.7 4Q11.2 5.3 14.3 4.6Q14.6 8.4 11.6 10.3Q10.3 7.8 7.8 6.7L6.7 6.2Z', 'M7.1 5.7L2.2 13.9'),
      'bolt':(poly([(4.9,2.5),(11.1,2.5),(14.3,8),(11.1,13.5),(4.9,13.5),(1.7,8)]),st(ci(8,8,2.65),1.25)),
      'broom':('M7 7L12 10L8 15L1 11Z','M9 8L14 1M4 10L3 12M6 11L5 13M8 12L7 14'),
      'drill':('M2 3H10V8H8L7 14H3L4 8H2Z','M10 5H15M11 3V7M3 5H6M4 11H7'),
      'gavel':('M7 1L13 7L10 10L4 4Z','M8 7L2 13M8 14H14'),
      'hard-hat':('M2 10Q2 3 8 3Q14 3 14 10L15 12H1Z','M6 4V9M10 4V9M1 12H15'),
      'inspection-panel':(rr(2,2,12,12,1),'M4 4H12V12H4ZM10 7V9'),
      'laser':('M1 6H8V10H1Z','M8 8H15M11 3L9 5M11 13L9 11M14 4L12 6M14 12L12 10'),
      'mound-shovel':('M2 14Q6 7 10 14ZM10 6L14 7L13 11L9 10Z','M12 7L14 1M13 1H15'),
      'pickaxe':('M1.5 7.1C3.7 2.6 9.8 1.4 14.5 4.7L13 6.1C9.2 3.7 5.9 4.5 1.5 7.1Z', 'M8 4.4L5.1 14.1'),
      'pocket-knife':('M2.1 10.1Q2 8.7 3.5 8.6L11.9 8.3C15 8.1 15.2 12.5 12.4 12.8L4.2 13.7Q2.2 14 2.1 12Z', 'M3.8 8.6L13.5 2.3C13.4 5.4 11 7 8.1 8.4M4.8 11H4.9'),
      'screw':('M3.7 2.1H12.3V4.8H10.1V10.8L8 14.3L5.9 10.8V4.8H3.7Z', 'M4 4.8H12M6 8.3L10 6.6M6 11L10 9.3'),
      'spool':('M3 2H13V4H11V12H13V14H3V12H5V4H3Z','M5 6H11M5 9H11'),
      'tool-case':(rr(2,5,12,9,1.5),'M5 5V2H11V5M2 9H14M5 8V10M11 8V10'),
      'toolbox':('M2 5H14V14H2Z','M5 5V2H11V5M2 9H14M6 8H10V10H6Z'),
    }
    for n,(b,d) in tools.items():s(n,b,d)
    bolt_hole=ci(8,8,2.1)
    bolt_duo,bolt_solid,bolt_stroke=base_layers('bolt')
    overrides['bolt']={'solid':op(bolt_solid,ci(8,8,3.2),po.PathOp.DIFFERENCE),
                       'duotone':[(op(part,bolt_hole,po.PathOp.DIFFERENCE),alpha) for part,alpha in bolt_duo]}
    badge('broom-sparkles','broom',sparkle)
    g('pencil-ruler','M2 1L6 1V14H2ZM2 4H4M2 7H4M2 10H4M10 2L14 3L11 14L8 15L8 12ZM10 5L13 6')
    g('ruler-dimension-line','M2 5H14V10H2ZM5 5V7M8 5V8M11 5V7M2 14H14M2 12V15M14 12V15')
    # Nature and animals: silhouettes remain distinguishable without labels.
    nature={
      'birdhouse':('M3 5.5L8 1.5L13 5.5V13H3Z','M1.7 6.5L3 5.5M13 5.5L14.3 6.5M8 13V15M6 11H10'),
      'feather':('M3.6 11.9C2.6 7.5 6.6 2 13.7 1.7Q14.2 5.1 12.2 7.5L10.2 8.2L11.1 8.6C9.3 11.6 6.6 12.7 3.6 11.9Z', 'M2 14.1Q5.6 9.9 10.3 5.6'),
      'flame-kindling':('M8 1Q8 5 11 5L12 3Q16 9 11 11Q5 14 3 9Q1 5 8 1Z','M2 12L14 15M2 15L14 12'),
      'flower-2':('M8 5C2-1 0 5 5 8C-1 11 5 17 8 11C11 17 17 11 11 8C17 5 11-1 8 5Z',st(ci(8,8,1.6),1.1)),
      'mountain-snow':('M1 14L7 2L15 14Z','M5 6L7 8L9 6M10 14L12 9'),
      'rose':('M3 5.4Q2.6 3 5.5 3.2Q7.2 .8 9.4 2.6Q12.4 2.1 12.9 4.9C13.1 7.3 10.5 9.5 8.1 9.5Q4.8 9.6 3 5.4Z', 'M3 5Q5 4.8 7.2 7Q9.8 4.7 12.8 4.9M5.5 3.2Q7.6 2.9 8.5 4.7M8.1 9.5V14.3M8.1 13Q10.8 12.9 12.3 10.7'),
      'shovel':('M5 8H11V11Q11 15 8 15Q5 15 5 11Z','M8 8V5M5 1H11V3Q11 5 8 5Q5 5 5 3Z'),
      'shrub':('M1.6 10.4C1 8.5 2 6.7 4 6.6C4 4.4 6.1 3.2 7.8 4.5C10 2.9 12.4 4.3 12.5 6.7C15.5 7 15.1 11.2 12.8 11.5Q10.4 12.3 8 11.6Q4.2 12.7 1.6 10.4Z', 'M4.6 10.9L5.1 13.7M8 10.5V13.9M11.7 10.9L11 13.7'),
      'stone':('M1.8 9.9L3.6 6.4L7.5 3.9L11.5 4.6L14.2 8.4L13.3 11.9L9.3 13L3.2 12Z', 'M3.6 6.4L7 7.5L10.5 6.5M7 7.5L5.9 10.5'),
      'tree-deciduous':('M4 11C-1 9 1 4 5 5C4 0 11 0 11 5C16 4 17 10 12 11Z','M8 8V15M5 15H11'),
      'tree-palm':('M6.7 14Q8.5 9.1 8.3 5.9L9.3 5.9Q10 10.7 8.7 14Z', 'M8.8 6Q4.6 4.5 1.6 8.6Q2.5 3 8.8 6Q5.1 1.8 2.8 2.8M8.8 6Q9.2 1.9 12.8 1.9M8.8 6Q12.9 2.9 14.5 6.4M8.8 6Q13.9 5.8 13.9 10.4'),
      'bone':('M3.9 5.7C1.1 6.4 .8 2.6 3.3 2.3Q4.3 2.2 4.9 3C6.6 .6 9 3.1 7.4 5.2Q6.8 6 7.7 7L9 8.3Q10 9.2 10.8 8.6C12.9 7 15.4 9.4 13 11.1Q13.8 11.7 13.7 12.7C13.4 15.2 9.6 14.9 10.3 12.1Q10.4 11.4 9.6 10.6L5.4 6.4Q4.6 5.6 3.9 5.7Z', None),
      'origami':('M1 6L15 1L10 15L6 10L1 6Z','M1 6L9 6L15 1M9 6L6 10M9 6L10 15'),
      'panda':(un(ci(3.9,4.1,2.15),ci(12.1,4.1,2.15),p('M8 3.3C11.7 3.3 14 6 14 9.2C14 15.7 2 15.7 2 9.2C2 6 4.3 3.3 8 3.3Z')),un(p('M3.8 8.8C4.2 7 5.8 6.4 6.4 7.4C7.1 8.5 5.7 10.3 4.7 10.2Q3.7 10.1 3.8 8.8Z'),p('M12.2 8.8C11.8 7 10.2 6.4 9.6 7.4C8.9 8.5 10.3 10.3 11.3 10.2Q12.3 10.1 12.2 8.8Z'),rr(7,10.5,2,1.3,.65))),
      'rat':('M4.8 9.8C4.6 6.3 7.1 4.5 9.8 5.5C9.3 2.9 12.6 2.9 12.4 5.6L14.4 8.5Q14.9 9.2 14 9.5L12 10.1C10.8 12.3 6.5 12.5 4.8 9.8Z', 'M5.3 10.4C2.6 13.2 .6 10.3 2.1 8Q3.7 5.7 1.5 4.7M11.9 7.6H12'),
      'shell':('M7 14C1 11-1 4 3 3C3 0 7 1 8 3C10 0 14 1 13 4C18 5 14 12 9 14Z','M8 3V14M4 4L7 13M12 5L9 13M6 14H10'),
      'shrimp':('M12.3 5.4Q10.8 3 7.4 3.2C3.9 3.4 1.8 5.4 2 8.7C2.3 12.3 6 14.3 9.8 13Q11 12.6 11.7 11.8Q13.2 13.1 14.1 12.5L13.5 10.7L14.1 9Q12.5 8.9 11.5 10.2C7 12.6 4.7 10.3 5.6 8.2Q6.6 6.2 10.7 7.5Z', 'M10.4 4.2Q10.9 2 13 1.6M12.1 5Q13.4 4 14.5 4.1M3.2 5.8L5.7 7.1M3 10.8L5.4 9.5'),
      'snail':(un(ci(7,8,4),p('M2 13H13Q15 13 14 10V8H11V11H2Z')),'M6 6Q10 5 9 9Q8 11 6 9M12 8V6M14 8L15 6'),
      'squirrel':('M6.1 11.2C-.2 11.1 .8 3.9 4.4 2.4C8.1 .9 9.4 5 6.6 6.3C4.7 7 4.7 8.7 6.1 8.8Q7.7 7.1 9 8.1L9.8 6.4L9.9 3.6L11.5 5.1Q13 4.8 13.5 6.5L14.4 7.5L12.9 8.8L11.8 8.9L12 10.1L13.8 10.3L13.1 11.2H11.7L11.5 12.7L13.5 13.6Q11 14.5 7.5 14Q5.8 13.6 6.1 11.2Z', 'M6.2 11.5Q6.4 9.6 8.6 9.6'),
      'turtle':(p('M2.4 8C2.4 5.4 4.5 3.7 7.2 3.7C9.5 3.7 11.1 5.2 11.1 8C11.1 10.8 9.5 12.3 7.2 12.3C4.5 12.3 2.4 10.6 2.4 8Z'),un(st('M4.1 5.1L2.5 3.3M4.1 10.9L2.5 12.7M9.2 4.5L10.4 2.8M9.2 11.5L10.4 13.2M11.1 8H13.1',1.35),ci(13.3,8,1.25),st('M5 7L7 5.8L9 7L8.4 9.8H5.6Z',1.15))),
      'worm':('M1.6 9.5C3.6 10.1 4.2 8.9 4.7 6.3C5.4 2.5 9.5 2.3 10.3 5.7C10.9 7.8 9.6 9.2 10.6 9.9Q11.5 10.4 12 9.2C13.1 7.3 15.5 9.4 14.2 11.4C12.4 14.4 8.1 13.5 7.5 10.8C6.9 8.7 8.5 6.2 7.4 6.1C6.3 6 7.1 10.4 4.4 11.4Q2.2 12 1.6 9.5Z', 'M4.7 7.5L6.5 8.1M8 10.9L9.9 10.1'),
    }
    for n,(b,d) in nature.items():s(n,b,d)
    b,d,o,c,t=drawings['birdhouse'];drawings['birdhouse']=(b,un(d,st(ci(8,7.8,1.6),1)),o,c,t)
    g('cannabis',un(p('M8 11.4C6.6 8.1 6.5 4.7 8 1.4C9.5 4.7 9.4 8.1 8 11.4ZM7.9 11.8C4.6 10 2.5 7.5 1.6 4.5C4.8 5.7 7 8.1 7.9 11.8ZM8.1 11.8C9 8.1 11.2 5.7 14.4 4.5C13.5 7.5 11.4 10 8.1 11.8ZM8 11.8Q4.2 12.7 2.1 10.1Q5.5 9.6 8 11.8Q10.5 9.6 13.9 10.1Q11.8 12.7 8 11.8Z'),st('M8 10.7V14.4')))
    off('cannabis-off','cannabis')
    off('shrimp-off','shrimp')
    # A park/tree grouping intentionally shows separate trunks and canopies.
    g('park','M3 11V15M1 15H15M1 8L3 2L5 8ZM7 10H14M8 10V13M13 10V13M8 7H14V10')
    pine=p('M4.7 2.1L8.1 8.9H6.2L7.6 11.1H5.3V14H4.1V11.1H1.6L3.1 8.9H1.5Z')
    broadleaf=p('M10.7 4.1C12.1 3 14 4.1 13.8 5.9C16 7.4 14.5 10.7 12.1 10.7L12.3 13.9H10.2L10.4 10.7C7.7 11 6.4 8.2 8 6.4Q7.8 4.2 10.7 4.1Z')
    stack('trees',[pine,broadleaf])
    # Board games and leisure symbols.
    g('bow-arrow','M2.2 2.7Q12.5 3.5 13.3 13.8L4.3 11.7ZM2.3 13.7L13.9 2.1M10.7 2.1H13.9V5.3')
    s('bomb',ci(7,9,5),st('M10 5L12 3Q13 1 15 2M13 1V3',1.2))
    leaf=p('M8 8C7.9 6.6 5.4 5.1 5.5 3.4C5.6 1.3 7.2 1.1 8 2.2C8.8 1.1 10.4 1.3 10.5 3.4C10.6 5.1 8.1 6.6 8 8Z')
    clover=un(*(tr(leaf,angle) for angle in (0,90,180,270)))
    s('clover',clover,st('M8 8Q10 12.8 13.6 14.1',1.2))
    s('crown','M2 4L5 7L8 2L11 7L14 4L12 13H4Z','M4 10H12')
    for n in range(1,7):
        positions={1:[(8,8)],2:[(5,5),(11,11)],3:[(5,5),(8,8),(11,11)],4:[(5,5),(11,5),(5,11),(11,11)],5:[(5,5),(11,5),(8,8),(5,11),(11,11)],6:[(5,5),(11,5),(5,8),(11,8),(5,11),(11,11)]}[n]
        s(f'dice-{n}',rr(2,2,12,12,2),dots(*positions,r=.7))
    s('dices',un(rr(1.7,1.7,8.4,8.4,1.65),rr(6,6,8.3,8.3,1.65)),un(st(rr(6,6,8.3,8.3,1.65),1.25),dots((4,4),(8.6,8.6),(11.7,11.7),r=.72)))
    front_die=rr(6,6,8.3,8.3,1.65)
    rear_die=rr(1.7,1.7,8.4,8.4,1.65)
    clearance=un(front_die,st(front_die,3.25))
    rear_solid=op(un(rear_die,st(rear_die,1.25)),un(clearance,ci(4,4,.76)),po.PathOp.DIFFERENCE)
    overrides['dices']={'solid':un(rear_solid,op(un(front_die,st(front_die,1.25)),dots((8.6,8.6),(11.7,11.7),r=.76),po.PathOp.DIFFERENCE))}
    s('gamepad-2','M5 4H11Q14 4 15 12Q15 15 12 13L10 11H6L4 13Q1 15 1 12Q2 4 5 4Z',un(st('M3 7H7M5 5V9',1),dots((11,6),(13,8),r=.6)))
    s('gamepad-directional','M6 1.8H10V5.9H14.2V10.1H10V14.2H6V10.1H1.8V5.9H6Z','M8 4V5M4 8H5M11 8H12M8 11V12')
    s('gem','M4 2H12L15 6L8 15L1 6Z','M1 6H15M4 2L6 6L8 15M12 2L10 6L8 15')
    s('ghost','M2 14V7C2-1 14-1 14 7V14L11 12L8 14L5 12Z',dots((5.5,7),(10.5,7),r=.8))
    g('goal',un(st('M1.8 13V3.5H11.5V13',1.35),st('M11.5 3.5L14.2 6.6V12.6L11.5 13M1.8 13L4.4 10.5H11.5M4.4 10.5V6.6H14.2M7.8 6.6V10.5',1.15)))
    s('joystick',rr(2,10,12,4,1.5),un(ln((8,10),(8,5)),ci(8,3,2),ci(4,12,.5)))
    s('playing-card',rr(3,1,10,14,1.5),poly([(8,5),(11,8),(8,11),(5,8)]))
    s('playing-cards',un(rr(1,1,9,12,1.5),rr(6,3,9,12,1.5)),un(st(rr(6,3,9,12,1.5),1.1),poly([(10.5,7),(12.5,9),(10.5,11),(8.5,9)])))
    fan_card=rr(5.1,2.4,6.9,11.2,1.15)
    fan=[tr(fan_card,-23,dx=-2.4,dy=.2),tr(fan_card,-8,dx=-.7),tr(fan_card,12,dx=1.5,dy=.2)]
    stack('playing-cards-fan',fan,tr(poly([(9,6),(10.4,8),(9,10),(7.6,8)]),12,dx=1.5,dy=.2))
    for n,text in [('scroll',False),('scroll-text',True)]:
        s(n,'M4 2H13Q15 2 15 4V5H12V12Q12 15 9 15H3Q1 15 1 12H4Z',st('M4 2V5M4 12H9Q8 15 9 15'+('M6 6H10M6 9H10' if text else ''),1.1))
    s('skull','M5 13V10C-1 8 0 1 8 1C16 1 17 8 11 10V13Z',un(ci(5,6,1.3),ci(11,6,1.3),poly([(8,7),(9,9),(7,9)]),st('M7 11V13M9 11V13',.8)))
    blade=p('M6.1 9.1L11.8 2.7L14 1.9L13.3 4.3L6.9 10.1Z')
    sword=un(blade,st('M4.1 8.5L7.7 12.1M5.9 10.3L2.6 13.6M1.9 12.9L3.3 14.3',1.35))
    g('sword',sword)
    rear_sword=api['mirror'](sword)
    g('swords',un(op(rear_sword,un(sword,st(sword,1.9)),po.PathOp.DIFFERENCE),sword))
    g('tic-tac-toe','M6 1V15M10 1V15M1 6H15M1 10H15M2 2L4 4M2 4L4 2M12 12L14 14M12 14L14 12',st(ci(13,3,1.4),1))
    s('tombstone','M3 14V6C3-1 13-1 13 6V14Z','M1 14H15M8 4V9M6 6H10')
    s('toy-brick','M1 6H15V14H1Z','M3 6V3H6V6M10 6V3H13V6M1 10H15')
    # Chess pieces share a base, with distinct identifying silhouettes.
    chess={
      'pawn':'M6 7Q3 4 5 2Q8-1 11 2Q13 4 10 7L11 12H5Z',
      'bishop':'M8 1Q15 6 10 8L11 12H5L6 8Q1 6 8 1Z',
      'king':'M5 5H11L10 12H6ZM8 1V5M6 3H10',
      'queen':'M3 4L6 7L8 2L10 7L13 4L11 12H5Z',
      'rook':'M3 2H5V4H7V2H9V4H11V2H13V6H11L10 12H6L5 6H3Z',
      'knight':'M4.5 12C4.5 9.4 7.7 9.1 8.1 6.6L5.6 7.7Q4.7 8.2 4.1 7.5L3.2 6.3L6.8 2.9L7.2 1.4L8.9 2.4C11.9 2.8 12.6 7.3 11.6 12Z',
    }
    for kind,b in chess.items():
        n='chess-'+kind;s(n,un(p(b),rr(3,12,10,2,.4)),st('M7 4L9 6',1) if kind=='bishop' else (st('M8 1V5M6 3H10',1.25) if kind=='king' else (ci(7.4,4.6,.58) if kind=='knight' else None)))
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
      'bitcoin':'M5 3H9Q14 3 12 7Q15 12 9 13H4M5 3V13M4 7.5H10M7 1V3M10 1V3M7 13V15M10 13V15',
      'emirati-dirham':'M4 2H8C16 2 16 14 8 14H4M5 2V14M2 6H14M2 10H14',
      'georgian-lari':'M12 8C12 1 3 1 3 8Q3 14 8 14H13M6 1V9M9 1V9M2 14H13',
      'kazakh-tenge':'M2 2H14M2 5H14M8 5V14',
      'nepali-rupee':'M2 2H8M4 2Q10 4 5 7L9 12M10 6Q14 4 14 7Q10 8 11 10Q12 12 15 10',
      'philippine-peso':'M5 14V2H9C14 2 14 8 9 8H5M2 4H15M2 6H15',
      'saudi-riyal':'M6 2V10L2 11M10 1V12L14 11M3 7L14 5M2 10L14 8M10 15L14 14',
    }
    for n,d in currencies.items():
        if n in scope:g(n,d)
    cm={n:st(d,1.8) for n,d in currencies.items()}
    g('currency',un(st(ci(8,8,4),1.25),st('M2 2L5 5M11 11L14 14M2 14L5 11M11 5L14 2')))
    for n,typ in [('circle-euro','euro'),('circle-pound-sterling','pound-sterling')]:s(n,ci(),tr(cm[typ],scale=.58))
    badge_body=api['badge_body']()
    for typ in ['cent','dollar-sign','euro','indian-rupee','japanese-yen','pound-sterling','russian-ruble','swiss-franc','turkish-lira']:
        s('badge-'+typ,badge_body,tr(cm[typ],scale=.55))
    s('badge-percent',badge_body,un(st('M5.7 10.3L10.3 5.7',1.1),st(ci(5.7,5.7,.85),1),st(ci(10.3,10.3,.85),1)))
    receipt=p('M3 1L5 2L7 1L9 2L11 1L13 2V15L11 14L9 15L7 14L5 15L3 14Z')
    for typ in ['cent','euro','indian-rupee','japanese-yen','pound-sterling','russian-ruble','swiss-franc','turkish-lira']:
        s('receipt-'+typ,receipt,tr(cm[typ],scale=.55))
    s('receipt-text',receipt,'M5 5H11M5 8H11M5 11H9')
    for n,typ in [('banknote-check','check'),('banknote-x','x')]:badge(n,'banknote',mark(typ))
    for n,d in [('banknote-arrow-down','M12 9V15M9.5 12.5L12 15L14.5 12.5'),('banknote-arrow-up','M12 15V9M9.5 11.5L12 9L14.5 11.5')]:badge(n,'banknote',st(d,1.1))
    s('credit-card-reader',rr(3,4,10,11,1.5),'M5 4V1H11V4M5 7H11M5 10H5.1M8 10H8.1M11 10H11.1M5 13H5.1M8 13H8.1')
    s('smartphone-nfc',rr(2,1,8,14,1.5),st('M5 12H7M12 5Q15 8 12 11M11 7Q12 8 11 9',1.1))
    s('hand-coins','M1.7 10.1L4 9.7L6 8.1Q6.6 7.7 7.4 7.9L9.3 8.4Q10.8 8.9 9.8 10.1L8 10.4L12.9 8.5Q14.1 8.2 14.3 9.2Q14.5 10 13.7 10.6L8.4 13.9Q7.8 14.3 6.8 14.1L2.4 13.3Z','M6 10.5L8 10.4M4.3 5.4A1.7 1.7 0 1 0 4.3 2A1.7 1.7 0 1 0 4.3 5.4ZM10.3 5.3A1.5 1.5 0 1 0 10.3 2.3A1.5 1.5 0 1 0 10.3 5.3Z')
    s('cap','M2 10V8C2 0 12 0 12 8V10Z','M2 10H15Q14 14 7 12M7 3V8')
    s('handbag','M3 5H13L14 14H2Z','M5 5V3Q8-1 11 3V5M5 7V9M11 7V9')
    s('perfume-bottle',rr(3,6,10,8,2),'M6 6V3H10V6M5 3H11V1H5ZM6 9H10V12H6Z')
    s('shirt','M5 2L1 5L3 8L5 7V14H11V7L13 8L15 5L11 2Q8 6 5 2Z')
    for n,t in [('shopping-cart-minus','minus'),('shopping-cart-plus','plus')]:badge(n,'shopping-cart',mark(t))
    # Buildings distinguish rooflines, circulation, and specific functions.
    buildings={
      'brick-wall':(rr(1,2,14,12,.4),'M1 6H15M1 10H15M5 2V6M11 2V6M8 6V10M4 10V14M12 10V14'),
      'castle':('M1 3H3V5H5V3H7V7H9V3H11V5H13V3H15V14H1Z','M6 14V10Q8 7 10 10V14'),
      'church':('M3 14V7L8 3L13 7V14Z','M8 1V4M6 2H10M6 14V10Q8 8 10 10V14'),
      'dam':('M8.3 2.4H11.1L14.2 13.5H6.3Z', 'M1.6 6.5Q3 5.3 4.4 6.5T7.6 6.5M1.6 9.9Q3 8.7 4.4 9.9T6.9 10.2M9.9 5.5L11.4 11.4'),
      'dome':('M2.4 9.6C2.7 5.8 5 3.2 8 3.2C11 3.2 13.3 5.8 13.6 9.6V13.3H2.4Z', 'M1.5 9.6H14.5M8 1.6V3.2M5.3 9.8V13.2M10.7 9.8V13.2'),
      'door-stairwell':(rr(2,1,12,14,.6),'M4 12H7V9H10V6H12'),
      'factory':('M1 14V7L6 4V7L11 4V8H15V14ZM12 8V1H14V8','M4 10V12M8 10V12M12 10V12'),
      'hotel':(rr(2,1,12,14,.5),'M5 4V8M11 4V8M5 6H11M6 15V11H10V15'),
      'lighthouse':('M5 5H11L12 14H4Z','M4 5H12M5 5V2H11V5M4 2L8 1L12 2M5 8H11M4.5 11H11.5M1 4H3M13 4H15'),
      'mosque':('M4 8Q4 5 8 3Q12 5 12 8V14H4ZM1 14V4H3V14M13 14V4H15V14','M7 14V11Q8 9 9 11V14M8 3V1'),
      'school':('M2 14V7H5V4L8 1L11 4V7H14V14Z',un(st('M6 14V10H10V14M3.5 9H3.6M12.5 9H12.6',1.1),st(ci(8,5.2,1.45),.85),st('M8 4.5V5.2H8.6',.65))),
      'theater':('M1 2H9V8Q5 13 1 8ZM8 6H15V12Q11.5 17 8 12Z','M3 5H3.1M7 5H7.1M3 7Q5 9 7 7M10 9H10.1M13 9H13.1M10 13Q11.5 11 13 13'),
      'university':('M1 6L8 1L15 6Z','M2 14H14M3 7V12M6 7V12M10 7V12M13 7V12'),
      'warehouse':('M1 14V6L8 2L15 6V14Z','M4 14V8H12V14M4 10H12M4 12H12'),
    }
    for n,(b,d) in buildings.items():s(n,b,d)
    g('utility-pole','M8 1V15M2 3H14M4 6H12M3 2V4M13 2V4M5 5V7M11 5V7')
    for n,what in [('house-cog',cog),('house-plus',mark('plus')),('house-plug',st('M11 9V11M14 9V11M10 11H15V12Q15 14 12.5 14V15M10 11V12Q10 14 12.5 14',1))]:badge(n,'home',what)
    duo,solid,mono=base_layers('home');back=lambda a:tr(a,scale=.65,dx=-2.5,dy=-1);front=lambda a:tr(a,scale=.65,dx=2.5,dy=2)
    front_ink=front(solid);clear=un(front_ink,st(front_ink,1.6))
    g('houses',un(op(back(mono),clear,po.PathOp.DIFFERENCE),front(mono)))
    overrides['houses']={'solid':un(op(back(solid),clear,po.PathOp.DIFFERENCE),front_ink)}
    transport={
      'bus-front':(rr(3,1.5,10,12,2),'M3 5H13M3 9H13M5 11H5.1M11 11H11.1M4 13V15M12 13V15M1 5V8M15 5V8'),
      'car-battery':(rr(2,4,12,10,1),'M4 4V2H6V4M10 4V2H12V4M4 9H7M5.5 7.5V10.5M10 9H12'),
      'car-front':('M2 8L4 3H12L14 8V13H2Z','M2 8H14M4 10H5M11 10H12M3 13V15M13 13V15'),
      'car-taxi-front':('M2 8L4 4H12L14 8V13H2Z','M2 8H14M6 4V1H10V4M4 10H5M11 10H12M3 13V15M13 13V15'),
      'caravan':('M1 4H10Q13 4 13 7V12H1Z','M13 11H15M3 6H6V9H3ZM8 6H11V12M3 12V14M11 12V14'),
      'cable-car':(rr(3,6,10,8,2),'M1 1L15 4M8 2.5V6M3 10H13M8 6V10'),
      'engine':('M3 5H8V3H12V6H14V12H3V10H1V7H3Z','M5 3H8M6 2V5M14 8H15M8 7L6 9H9L7 11'),
      'ev-charger':(rr(2,2,8,13,1),'M4 5H8M5 8L4 10H7L6 12M10 5H12V12Q15 14 15 10V5L13 3'),
      'forklift':('M1.5 7.7H4.5L5.7 9.1H8V10.7H1.5Z', 'M2.1 7.7V3.5H6.4L8 9.1M10.2 3V11.6H14.3'),
      'helicopter':('M6.2 7.7Q6.5 5.8 9.2 5.8C12 5.8 13.9 7.5 14.4 10.3Q14.6 11.5 13.2 11.5H8.6Q6.8 11.5 6.2 9.8L2.2 8.2V6.7Z', 'M9.1 5.8V3M4.3 3H14.1M2.3 6.7L1.6 5.4M9.7 6L11 9H14M8.4 11.5V13.7M12.4 11.5V13.7M6.9 13.7H14.2'),
      'hot-air-balloon':('M8 1C4.5 1 2 3.2 2 6Q2 9.3 6 12H10Q14 9.3 14 6C14 3.2 11.5 1 8 1Z','M6 12V15H10V12M8 1C4.5 4 4.5 8.5 8 12C11.5 8.5 11.5 4 8 1M2 6.5H14'),
      'kayak':('M7.9 1.5C11.8 4.8 11.8 11.2 8.1 14.5C4.2 11.2 4.2 4.8 7.9 1.5Z', 'M6.9 7.8C6.9 4.7 9.1 4.7 9.1 7.8C9.1 10.9 6.9 10.9 6.9 7.8ZM2.1 3.8L4.3 5.4L3.2 6.7L1.7 4.6ZM3.8 5.9L12.2 11M12 10L14.3 11.8L13.8 12.7L11.4 11.5Z'),
      'parking-meter':(rr(4,1,8,10,3),'M8 11V15M6 4H10V7H6ZM8 7V9'),
      'road':('M5 1H11L15 15H1Z','M8 3V5M8 8V10M8 13V15'),
      'sailboat':('M1 11H15L12 15H4Z','M8 11V1L14 9H8M6 3L2 9H6Z'),
      'ship-cargo':('M1.6 10.2H14.4L12.4 13.8H4.4Z', 'M2.8 10.2V7.1H9.2V10.2M6.1 7.1V10.2M4.2 7.1V4.8H7.9V7.1M10.7 10.2V3.8H13.2V10.2'),
      'tractor':('M2.4 7V2.1H7.3L8.1 6.6H12.2Q13.7 6.6 13.7 8V9.1H8.8L7.5 10H6.9Q6.5 7.2 3.9 7Z', 'M2.6 5.9H7.8M11.6 6.6V4.7'),
      'traffic-cone':('M7 1H9L13 13H3Z','M5 6H11M4 10H12M1 14H15'),
      'trailer':(rr(2,4,11,8,1),'M13 10H15M4 12V14M11 12V14M5 4V12'),
      'train-front-tunnel':(rr(4.7,5.7,6.6,6.3,1.65),un(st('M1.6 13V7C1.6-.1 14.4-.1 14.4 7V13M5.9 13.7L5.3 14.5M10.1 13.7L10.7 14.5',1.25),rr(6,7,4,1.7,.6),dots((6.7,10.3),(9.3,10.3),r=.6))),
      'tram-front':(rr(3,3,10,10,2),'M3 7H13M5 10H5.1M11 10H11.1M8 3V1M5 1H11M5 13L3 15M11 13L13 15'),
      'van':('M1 5H10L15 9V13H1Z','M3 5V9H14M8 5V13M3 13V15M12 13V15'),
    }
    for n,(b,d) in transport.items():s(n,b,d)
    for n in ['tractor']:
        b,d,o,c,t=drawings[n];drawings[n]=(b,un(d,st(ci(4,11.6,2.55),1.25),st(ci(12.2,12.1,1.8),1.25)),o,c,t)
    b,d,o,c,t=drawings['forklift']
    drawings['forklift']=(b,un(d,dots((2.9,13),(7.2,13),r=1.25)),o,c,t)
    s('baggage-claim',rr(3,2,9,8,1),'M5 2V1H10V2M1 12H15M1 15H15M3 12V15M7 12V15M11 12V15')
    s('circle-gauge',ci(),un(st('M4 8A4 4 0 0 1 12 8M8 9L11 6',1.1),ci(8,9,.8)))
    s('octagon-minus',poly([(5,1),(11,1),(15,5),(15,11),(11,15),(5,15),(1,11),(1,5)]),'M4 8H12')
    g('drone',un(st('M4 4L12 12M4 12L12 4',1.4),*(st(ci(x,y,2.5),1.1) for x,y in [(3.5,3.5),(12.5,3.5),(3.5,12.5),(12.5,12.5)]),ci(8,8,1.5)))
    g('moped',un(st(ci(3.5,11.8,1.9),1.25),st(ci(12.4,11.8,1.9),1.25),p('M1.6 9.1Q1.8 6.7 4.5 6.7H6L6.8 9.1Z'),st('M3 5.5H5.6M6 7.4L7.4 10.6H9.4L11.4 6.6L10.3 3.5H8.8M11.4 6.6L12.4 11.7',1.35)))
    g('motorbike',un(st(ci(3.5,11.8,1.9),1.25),st(ci(12.4,11.8,1.9),1.25),p('M5.8 7.4Q6.5 5.2 9.6 5.6L10.6 7.5L8.6 8.7H7.1Z'),st('M2.3 6.4L5.5 7.4H6.5M10.4 6.7L9.8 3.6H11.8M10.4 6.7L12.4 11.8M3.5 11.8L6.1 9.6L7.9 11.1H9.1',1.35)))
    g('scooter',un(st(ci(3,13,2),1.1),st(ci(13,13,2),1.1),st('M3 13H10L12 2H9M12 2L13 13',1.2)))
    g('ship-wheel',un(st(ci(8,8,4.5),1.2),ci(8,8,1),st('M8 1V15M1 8H15M3 3L13 13M3 13L13 3',1.1)))
    g('train-track','M5 1L2 15M11 1L14 15M4.5 4H11.5M4 7H12M3.5 10H12.5M3 13H13')
    badge('truck-electric','truck',poly([(12,8),(9,12),(12,12),(11,15),(15,10),(12,10)]))
    # Sloping aircraft orientation and a separate ground line make takeoff/landing explicit.
    for n,angle in [('plane-takeoff',60),('plane-landing',120)]:
        duo,solid,mono=base_layers('plane');f=lambda a:tr(a,angle, .72,0,-2)
        ground=ln((2,14),(14,14));g(n,un(f(mono),ground));overrides[n]={'duotone':[(f(a),v) for a,v in duo]+[(ground,1)],'solid':un(f(solid),ground),'stroke':un(f(mono),ground)}
    for typ in ['check','minus','plus','x']:
        m=mark(typ) if typ!='percent' else un(st('M10 14L14 10',.9),ci(10,10,.55),ci(14,14,.55))
        badge('ticket-'+typ,'ticket',m)
    ticket_face=drawings['ticket'][0]
    percent=un(st('M6.1 10.4L9.9 5.6',1.25),dots((6.1,5.9),(9.9,10.1),r=.73))
    s('ticket-percent',ticket_face,percent)
    off('ticket-slash','ticket')
    duo,solid,mono=base_layers('ticket');front=lambda a:tr(a,scale=.75,dx=1.3,dy=2);back=lambda a:tr(a,scale=.75,dx=-1.3,dy=-2)
    clear=un(front(solid),st(front(solid),1.6));g('tickets',un(op(back(mono),clear,po.PathOp.DIFFERENCE),front(mono)))
    overrides['tickets']={'solid':un(op(back(solid),clear,po.PathOp.DIFFERENCE),front(solid))}
    ticket_front=tr(ticket_face,scale=.83,dx=.7,dy=1.3)
    ticket_rear=tr(ticket_face,scale=.83,dx=-.7,dy=-1.7)
    plane_mark=p('M8.6 5.9Q9.1 5.6 9.3 6.3L9.6 8.1L11.9 9.8V10.6L9.5 9.9L9.1 11.6L9.6 12.1L9 12.4L8.4 12L7.6 12.3L7.2 11.9L7.9 11.4V9.8L5.4 10.2V9.4L7.9 7.9Z')
    stack('tickets-plane',[ticket_rear,ticket_front],plane_mark)
    # Travel infrastructure and destination cues.
    g('bridge','M1 13H15M3 3V15M13 3V15M3 4Q8 13 13 4M5 7V13M8 9V13M11 7V13')
    s('briefcase-business',rr(2,5,12,9,1.5),'M5 5V2H11V5M2 8Q8 12 14 8M7 9V11H9V9')
    badge('briefcase-plus','briefcase',mark('plus'))
    s('briefcase-conveyor-belt',rr(3,3,10,7,1),'M6 3V1H10V3M1 12H15M1 15H15M3 12V15M7 12V15M11 12V15')
    s('cigarette',rr(1,9,13,4,.3),'M5 9V13M11 7Q13 5 11 3M14 7Q16 5 14 2')
    off('cigarette-off','cigarette')
    s('concierge-bell','M2 12C2 2 14 2 14 12Z','M1 14H15M8 5V2M6 2H10')
    s('parasol','M1 8Q8-3 15 8Z','M8 8V14M5 14H11M8 2Q4 5 4 8M8 2Q12 5 12 8')
    g('tent-tree','M1 14L6 5L11 14ZM6 5V14M10 7L13 1L15 7ZM13 7V14')
    s('tower-control','M3 3H13L11 8H5Z','M1 3H15M7 8V14M9 8V14M5 14H11M6 4V7M10 4V7')
    # Human gestures and expression changes, with facial counters in Solid.
    for n,d in [('face-angry','M4 5L6.5 6M9.5 6L12 5M5 11Q8 8 11 11'),('face-expressionless','M4 6H6M10 6H12M5 11H11'),('face-grinning','M4.7 9H11.3Q10.6 12 8 12Q5.4 12 4.7 9Z')]:
        s(n,ci(),un(st(d,1.1),dots((5,6),(11,6),r=.55) if n!='face-expressionless' else po.Path()))
    badge('face-slightly-smiling-plus','smile',mark('plus'))
    s('balloon','M8 1C17 1 15 12 8 13C1 12-1 1 8 1Z','M8 13L7 15H9M8 15Q11 17 13 14')
    s('biceps-flexed','M2 11.6L3.3 6.3Q3.6 5.1 4.4 3.8L5.3 2.4Q5.8 1.7 6.7 1.9L8.1 2.2Q9.2 2.5 8.9 3.6L8.6 4.6Q8.4 5.2 7.6 5.1L6.5 4.9L6.2 8.3C8.4 6.2 11.2 6.5 12.1 8.6Q14.1 8.3 14.2 10.7C14.3 13.2 11.6 14.2 8.2 14Q4.1 14 2 12.6Z','M6.2 8.3Q5.6 9.3 5.5 10.5')
    s('hand-helping','M1.7 11.1L4.3 10.5L6.1 8.5Q6.8 7.7 7.6 8.4Q8 8.9 7.6 9.6L6.9 10.6L9.7 9.7Q11 9.4 11 10.4Q11 10.9 10.3 11.4L7.2 13.6Q6.5 14.1 5.5 14L2 13.5Z','M14.1 2.4L10.8 2.5Q9.4 2.5 8.3 3.5L5.3 6.1Q4.9 6.7 5.7 7.1L9 5.3M9 5.3Q8.6 7 9.6 7Q10.3 7.2 11.1 6.3L12.6 4.9L14.3 4.8')
    s('hand-metal','M3 9V2Q5 0 5 3V7H7V5H9V7H11V2Q13 0 13 3V11Q13 15 9 15H6Q4 15 3 12L1 9Q1 7 3 9Z','M5 7V10M9 7V10')
    s('heart-crack',p('M8 14L2 8C-1 3 5-1 8 4C11-1 17 3 14 8Z'),'M8 4L6 7L9 9L7 12')
    s('heart-handshake','M8 14L2.8 9C-1 5.1 3.8-.2 8 4.1C12.2-.2 17 5.1 13.2 9Z','M8 4.1L5.6 6.4Q4.9 7.2 5.7 7.9Q6.4 8.5 7.3 7.8L8.9 6.6L12.4 9.7M8.4 9.2L10.3 11.2')
    s('party-popper','M2 14L5 5L11 11Z','M5 5L11 11M8 4L10 2M12 7L15 5M11 3Q14 4 14 1M4 1V2M14 11H15')
    # Weather compositions separate foreground clouds from sun/moon backgrounds.
    def compose(n,parts,detail=None):
        secondary=[];primary=[];solids=[];monos=[]
        for name,scale,dx,dy in parts:
            duo,solid,mono=base_layers(name);f=lambda a:tr(a,scale=scale,dx=dx,dy=dy)
            foreground=f(solid);clear=un(foreground,st(foreground,1.3))
            secondary=[op(a,clear,po.PathOp.DIFFERENCE) for a in secondary]
            primary=[op(a,clear,po.PathOp.DIFFERENCE) for a in primary]
            solids=[op(a,clear,po.PathOp.DIFFERENCE) for a in solids]
            monos=[op(a,clear,po.PathOp.DIFFERENCE) for a in monos]
            for a,v in duo:(secondary if v<1 else primary).append(f(a))
            solids.append(foreground);monos.append(f(mono))
        if detail:primary.append(detail);solids.append(detail);monos.append(detail)
        primary=un(*primary);secondary=op(un(*secondary),primary,po.PathOp.DIFFERENCE)
        mono=un(*monos);g(n,mono);overrides[n]={'duotone':([(secondary,.24)] if secondary else [])+[(primary,1)],'solid':un(*solids),'stroke':mono}
    rain=st('M5 12L4 14M9 12L8 14M13 12L12 14',1.15)
    for n,detail in [('cloud-drizzle',dots((4,12),(7,14),(10,12),(13,14),r=.55)),('cloud-hail',dots((4,13),(8,13),(12,13),r=.9)),('cloud-rain-wind',st('M3 11L2 13M7 11L6 13M9 12H13Q15 12 14 10M8 15H13',1))]:compose(n,[('cloud',.82,0,-2)],detail)
    for kind in ['sun','moon']:
        for wet in [False,True]:compose('cloud-'+kind+('-rain' if wet else ''),[(kind,.58,3,-3),('cloud',.74,-1,0 if not wet else -1)],rain if wet else None)
    compose('cloudy',[('cloud',.75,2,-2),('cloud',.75,-2,2)])
    off('droplet-off','droplet');off('umbrella-off','umbrella')
    compose('droplets',[('droplet',.65,-3,2),('droplet',.45,4,-3)])
    compose('haze',[('sun',.6,0,-3)],st('M1 10H15M3 12H13M1 14H15',1.1))
    compose('sun-snow',[('sun',.6,-3,-2),('snowflake',.52,3,3)])
    for kind in ['sun','snowflake']:compose('thermometer-'+kind,[('thermometer',.8,-3,0),(kind,.48,4,-2)])
    g('tornado','M1 2H15M3 5H13M5 8H11M7 11H12M8 14H10')
    g('waves-horizontal','M1 3Q4 1 7 3T15 3M1 8Q4 6 7 8T15 8M1 13Q4 11 7 13T15 13')
    g('waves-vertical','M3 1Q1 4 3 7T3 15M8 1Q6 4 8 7T8 15M13 1Q11 4 13 7T13 15')
    for base in ['waves','wind']:
        for direction in ['down','up']:
            m=st('M12 9V15M9.5 12.5L12 15L14.5 12.5' if direction=='down' else 'M12 15V9M9.5 11.5L12 9L14.5 11.5',1.1)
            badge(base+'-arrow-'+direction,'waves-horizontal' if base=='waves' else base,m)
    for n,counters in {
        'feather':st('M4.4 11.2Q7 8.4 10.3 5.6',1.2),
        'helicopter':p('M9.8 6.8Q12.1 7 13 8.7H10.7Z'),
        'kayak':rr(6.8,5.5,2.4,4.7,1.2),
        'cable-car':un(rr(4.4,7.4,2.9,2,.3),rr(8.7,7.4,2.9,2,.3)),
        'tower-control':un(st('M6 4L6.5 6.7M10 4L9.5 6.7',1.1)),
    }.items():
        duo,solid,mono=base_layers(n)
        overrides.setdefault(n,{})['solid']=op(solid,counters,po.PathOp.DIFFERENCE)
    # Individual fruit masses remain distinct in a solid bunch.
    grape_solid=po.Path()
    for fruit in berries:
        grape_solid=un(op(grape_solid,un(fruit,st(fruit,1.9)),po.PathOp.DIFFERENCE),fruit)
    overrides['grape']={'solid':un(grape_solid,grape_stem)}
    # Wheel circles give transport silhouettes actual wheels rather than feet.
    for n,centers in {'caravan':[(4,12.5),(11,12.5)],'trailer':[(4,12.5),(11,12.5)],'van':[(3.5,13),(12,13)]}.items():
        b,d,o,c,t=drawings[n]
        wheels=un(*(ci(x,y,1.35) for x,y in centers))
        drawings[n]=(b,un(d,wheels),o,c,t)
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
