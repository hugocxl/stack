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
      'amphora':('M5 2H11L10 5Q14 7 12 12Q11 15 8 15Q5 15 4 12Q2 7 6 5Z','M5 6Q0 4 2 9L4 10M11 6Q16 4 14 9L12 10M5 2H11'),
      'avocado':('M8 1C11 1 10 5 13 8C16 13 11 15 8 15C3 15 1 12 3 8C6 5 5 1 8 1Z',None),
      'bacon':('M5 1Q7 3 9 1L11 3Q9 6 11 9L9 15Q7 13 5 15L3 13Q5 10 3 7Z','M6 3Q4.5 7 6 9Q7 11 6 13M8 3Q6.5 7 8 9Q9 11 8 13'),
      'barrel':('M4 2Q1 8 4 14H12Q15 8 12 2Z','M3 5H13M3 11H13M6 2Q4.5 8 6 14M10 2Q11.5 8 10 14'),
      'bean':('M11 2C16 2 15 9 11 12C7 16 1 15 1.5 10C2 6 6 9 7 6C7 3 8 2 11 2Z','M5 11Q10 11 11 6'),
      'beef':('M4 3C8 0 15 2 14 7C13 9 10 8 10 11C9 16 3 15 2 11C0 8 1 5 4 3Z','M5 5L9 7M7 6L6 11'),
      'beer':('M3 5H11V14H3Z','M11 6H13Q15 6 15 9Q15 12 11 12M5 7V12M8 7V12M3 5C0 2 4 0 6 2C8 0 11 1 11 5'),
      'blender':('M3 2H12L11 10H5Z','M5 10L3 14H13L11 10M12 3H14V7H12M6 5H8M7 12H9'),
      'bottle-wine':('M6 1H10V5Q13 7 13 9V14H3V9Q3 7 6 5Z','M6 3H10M3 9H13'),
      'broccoli':('M6 9C2 11 0 7 3 5C1 1 6 0 8 3C10 0 15 1 13 5C16 7 14 11 10 9L11 14H5Z','M6 6L8 9L11 6M8 9V13'),
      'cake-slice':('M2 7L12 2L14 7V14H2Z','M2 7H14M2 10H14M6 7L7 9L9 7'),
      'can':(rr(4,2,8,12,2),'M4 5H12M4 12H12M7 3.5H9'),
      'can-soda':(rr(4,2,8,12,2),'M4 5H12M4 12H12M7 3.5H9M7 7L9 9L7 10'),
      'candy':('M5 4Q8 2 11 5Q14 8 11 11Q8 14 5 11Q2 8 5 4Z','M4 4L1 2V6L3 7M12 12L15 14V10L13 9M5 5L11 11'),
      'carton':('M5 1H11L14 5V14H2V5Z','M2 5H14M5 1V5M11 1L8 5V14M10 8H12'),
      'cheese':('M2 7L12 2Q15 4 14 7V10Q11 10 12 13L14 14H2Z','M2 7H14M5 10H5.1M8 12H8.1'),
      'citrus':('M2 3L14 12C10 17 3 15 1 10C0 7 1 5 2 3Z','M3 5Q0 12 11 12M3 5L7 12M3 5L4 10'),
      'cooking-pot':(rr(3,5,10,9,2),'M1 6H3M13 6H15M2 5H14M6 2H10M8 2V5'),
      'croissant':('M2 6Q4 1 8 2Q12 1 14 6L15 12Q11 10 11 7Q8 5 5 7Q5 10 1 12Z','M5 3L5 7M11 3L11 7M8 2V6'),
      'cup-soda':('M3 5H13L11.5 14H4.5Z','M2 5H14M9 5L10 1H13'),
      'cupcake':('M3 8H13L11 14H5Z','M3 8C0 5 3 3 5 4C4 0 9 0 10 3C15 2 16 7 13 8M6 10L7 12M10 10L9 12'),
      'dessert':('M3 8H13V13H3Z','M1 13H15M3 10H13M4 8C1 5 4 3 6 5C6 1 11 2 11 5C14 4 15 7 13 8'),
      'donut':(ci(8,8,6),'M5 4L6 4.5M11 5L12 6M4 10L4.5 11M10 12L11 11.5'),
      'drumstick':('M6 3C10-1 17 4 13 9C11 12 8 10 6 9L4 12Q6 15 3 15Q0 15 1 12Q0 9 3 10L5 7Q3 5 6 3Z',None),
      'egg':('M8 1C10 1 14 7 14 10C14 17 2 17 2 10C2 7 6 1 8 1Z',None),
      'egg-fried':('M2 6C1 3 5 1 8 3C12 0 15 4 13 7C17 10 14 15 10 13C6 16 2 14 3 11C0 10 0 7 2 6Z',None),
      'glass-water':('M3 2H13L11.5 14H4.5Z','M4 8Q6 6 8 8T12 8'),
      'ham':('M3 4C6 1 12 2 14 6C16 10 11 15 7 14L3 10Q0 8 3 4Z','M9 6C6 8 7 11 10 11C13 10 13 7 11 6Z'),
      'hamburger':('M2 7C2 0 14 0 14 7ZM2 11H14Q14 14 11 14H5Q2 14 2 11Z','M1 9H15M4 8L7 10L10 8M6 4H6.1M10 4H10.1'),
      'ice-cream-bowl':('M2 8H14Q13 13 8 13Q3 13 2 8Z','M8 13V15M5 15H11M3 8C0 4 5 1 7 5C8 0 14 2 13 8'),
      'leafy-green':('M3 12C-1 7 4 0 7 3C11-1 16 3 13 6C17 10 12 15 7 13L2 15Z','M4 12L11 5M7 9V6M7 9H10'),
      'lollipop':(ci(6.5,6,4.5),'M9.5 9.5L14 14M5 4Q9 3 8 6Q7 8 5 6'),
      'mango':('M6 3C13-1 17 7 12 12C8 16 1 15 2 10C2 7 4 5 6 3Z','M7 4Q12 3 13 7M7 3Q6 1 9 1'),
      'martini':('M2 2H14L8 9Z','M8 9V14M4 14H12M4 5H12'),
      'microwave':(rr(1.5,3,13,10,1.5),'M10.5 3V13M3.5 5.5H8.5V10.5H3.5ZM12.5 6V7M12.5 10H12.6'),
      'milk':('M5 1H11L13 5V14H3V5Z','M3 5H13M5 1V5M10 5V14M5 9H8'),
      'nut':('M5 4Q3 1 8 1Q13 1 11 4L13 6V11L9 15H7L3 11V6Z','M3 6H13M6 8V11M10 8V11'),
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
    s('grape',un(*(ci(x,y,1.7) for x,y in [(5,5),(9,5),(12,7),(7,8),(10,10),(7,12),(4,9)])),st('M8 3Q8 1 12 1',1.1))
    s('groceries','M2 7H14L12 14H4Z',un(st('M4 7V3H6V7M9 7L11 2L13 3L12 7M6 10V12M10 10V12',1.1),ci(8,6,1.3)))
    s('hand-platter','M3 7Q3 2 8 2Q13 2 13 7Z',st('M1 8H15M7 1H9M1 12H5L7 10H11Q13 10 12 12L8 15H3',1.2))
    s('hop','M8 2Q14 5 12 10L8 14L4 10Q2 5 8 2Z','M8 2V14M4 5L8 8L12 5M4 9L8 12L12 9')
    g('utensils-crossed','M2 1L7 6M1 3L6 8M4 1L8 5Q10 7 7 9L2 14M14 2Q8 4 10 8L14 14M14 2L10 8')
    g('vegan','M2 5L7 14L13 3M8 7Q6 1 14 1Q14 8 8 7')
    g('wheat','M3 14L12 3M6 11Q1 11 2 7Q6 7 6 11ZM8 8Q4 7 5 4Q9 4 8 8ZM10 6Q8 2 11 1Q13 3 10 6ZM6 11Q10 12 11 8Q8 7 6 11ZM9 8Q13 8 14 5Q11 4 9 8Z')
    for n,base in [('bean-off','bean'),('beef-off','beef'),('beer-off','beer'),('candy-off','candy'),('carton-off','carton'),('egg-off','egg'),('fish-off','fish'),('hop-off','hop'),('milk-off','milk'),('nut-off','nut'),('wheat-off','wheat'),('wine-off','wine')]:off(n,base)
    homes={
      'air-vent':(rr(2,2,12,12,1.5),'M4 5H12M4 8H12M4 11H12'),
      'alarm-smoke':(ci(8,7,5),'M5 6H11M6 9H10M3 13L2 15M13 13L14 15'),
      'armchair':('M4 3H12V8H14V13H2V8H4Z','M4 8V10H12V8M4 13V15M12 13V15'),
      'bed-double':('M2 5H14V13H2Z','M2 9H14M8 5V9M4 5V3H12V5M2 13V15M14 13V15'),
      'bed-single':('M4 5H12V13H4Z','M4 9H12M5 5V3H11V5M4 13V15M12 13V15'),
      'blinds':(rr(2,2,12,10,1),'M2 5H14M2 8H14M11 2V14M10 14H12'),
      'fence':('M2 3L4 1L6 3V14H2ZM10 3L12 1L14 3V14H10Z','M1 6H15M1 11H15'),
      'fire-extinguisher':(rr(5,5,7,9,2),'M6 5V2H11M8 2V5M11 2H14V7M5 6Q2 6 2 10M2 9V13M7 9H10'),
      'heater':(rr(2,4,12,9,1),'M5 6V11M8 6V11M11 6V11M4 13V15M12 13V15M4 1V2M8 1V2M12 1V2'),
      'lamp-ceiling':('M3 7H13L15 11H1Z','M8 1V7M6 13Q8 15 10 13'),
      'lamp-desk':('M4 5L9 2L13 7L8 10Z','M4 5L2 8L6 13M3 14H11M9 2L11 1'),
      'lamp-floor':('M5 2H11L13 7H3Z','M8 7V14M4 14H12'),
      'lamp-wall-down':('M7 7H13L15 12H5Z','M2 2V9M2 5H10V7'),
      'lamp-wall-up':('M7 7H13L15 2H5Z','M2 6V13M2 10H10V7'),
      'plant-pot':('M4 9H12L11 14H5Z','M8 9V5M8 6Q1 6 3 2Q8 1 8 6ZM8 5Q8 0 13 2Q14 6 8 5Z'),
      'shelving-unit':(rr(2,2,12,12,1),'M2 7H14M2 12H14M5 3V7M8 4V7M5 10V12M11 9V12'),
      'soap-dispenser-droplet':(rr(2,6,7,8,1.5),'M5.5 6V3M3 3H10V5M13 7Q9 11 13 13Q17 11 13 7Z'),
      'solar-panel':('M3 2H13L15 11H1Z','M2 6.5H14M6 2L5 11M10 2L11 11M8 11V14M5 14H11'),
      'towel-rack':('M6 4H12V14H6Z','M1 5H15M2 3V7M14 3V7M6 11H12M8 4V9'),
      'brush-cleaning':('M2 8H14L12 14H4Z','M6 8V3Q6 1 8 1Q10 1 10 3V8M6 11V14M10 11V14'),
      'mop':('M3 10H11L13 14H1Z','M7 10L12 1M4 12L3 14M7 12V14M10 12L11 14'),
      'toothbrush':(rr(6,1.5,3,5,1),'M7.5 6.5V14M3.5 2.5H6M3.5 4H6M3.5 5.5H6'),
    }
    for n,(b,d) in homes.items():s(n,b,d)
    g('bubbles',un(st(ci(5,10,4),1.2),st(ci(11,4,2.5),1.2),ci(13,12,1)))
    g('rocking-chair','M4 1V9H12M5 9L3 14M10 9L12 14M1 13Q8 17 15 13M4 6H12V9')
    g('shower-head','M2 3Q3 1 5 2L8 5M5 8L11 2M6 9L5 10M9 9L8 10M12 8L11 9M8 12L7 13M11 11L10 12M14 10L13 11')
    sparkle=un(st('M12 9L12.7 11.3L15 12L12.7 12.7L12 15L11.3 12.7L9 12L11.3 11.3Z',.9))
    for n,base in [('mop-sparkles','mop'),('toothbrush-sparkles','toothbrush')]:badge(n,base,sparkle)
    badge('door-closed-locked','door-closed',un(rr(10,11.5,4,3,.5),st('M11 11.5V10.5A1 1 0 0 1 13 10.5V11.5',1)))
    badge('door-closed-package','door-closed',un(st(rr(10,10,4.5,4.5,.5),1),st('M10 11.5H14.5M12.2 10V12',.9)))
    cog=un(st(ci(12,12,2.1),1),st('M12 8.8V9.8M12 14.2V15.2M8.8 12H9.8M14.2 12H15.2M9.7 9.7L10.5 10.5M13.5 13.5L14.3 14.3M9.7 14.3L10.5 13.5M13.5 10.5L14.3 9.7',1))
    badge('door-closed-cog','door-closed',cog)
    badge('house-heart','home',mark('heart'))
    badge('house-wifi','home',un(st('M9 11Q12 8 15 11M10.5 12.5Q12 11 13.5 12.5',1),ci(12,14,.6)))
    # Hand tools retain characteristic heads and working edges.
    tools={
      'anvil':('M1 4H15L13 7H10L9 11L12 14H3L6 11V7H4Z',None),
      'axe':('M5 2L12 2L14 6L8 8Z','M8 5L3 14'),
      'bolt':('M5 2H11L14 8L11 14H5L2 8Z',st(ci(8,8,2.2),1.2)),
      'broom':('M7 7L12 10L8 15L1 11Z','M9 8L14 1M4 10L3 12M6 11L5 13M8 12L7 14'),
      'drill':('M2 3H10V8H8L7 14H3L4 8H2Z','M10 5H15M11 3V7M3 5H6M4 11H7'),
      'gavel':('M7 1L13 7L10 10L4 4Z','M8 7L2 13M8 14H14'),
      'hard-hat':('M2 10Q2 3 8 3Q14 3 14 10L15 12H1Z','M6 4V9M10 4V9M1 12H15'),
      'inspection-panel':(rr(2,2,12,12,1),'M4 4H12V12H4ZM10 7V9'),
      'laser':('M1 6H8V10H1Z','M8 8H15M11 3L9 5M11 13L9 11M14 4L12 6M14 12L12 10'),
      'mound-shovel':('M2 14Q6 7 10 14ZM10 6L14 7L13 11L9 10Z','M12 7L14 1M13 1H15'),
      'pickaxe':('M2 5Q7-1 14 4L11 6Q7 3 4 7Z','M8 5L4 14'),
      'pocket-knife':(rr(2,9,12,5,2),'M5 9L12 1L14 3L8 9M5 11.5H5.1M10 9V5'),
      'screw':('M4 1H12V4H4Z','M8 4V14M5 6L11 8M5 9L11 11M6 12L9 14'),
      'spool':('M3 2H13V4H11V12H13V14H3V12H5V4H3Z','M5 6H11M5 9H11'),
      'tool-case':(rr(2,5,12,9,1.5),'M5 5V2H11V5M2 9H14M5 8V10M11 8V10'),
      'toolbox':('M2 5H14V14H2Z','M5 5V2H11V5M2 9H14M6 8H10V10H6Z'),
    }
    for n,(b,d) in tools.items():s(n,b,d)
    badge('broom-sparkles','broom',sparkle)
    g('pencil-ruler','M2 1L6 1V14H2ZM2 4H4M2 7H4M2 10H4M10 2L14 3L11 14L8 15L8 12ZM10 5L13 6')
    g('ruler-dimension-line','M2 5H14V10H2ZM5 5V7M8 5V8M11 5V7M2 14H14M2 12V15M14 12V15')
    # Nature and animals: silhouettes remain distinguishable without labels.
    nature={
      'birdhouse':('M3 5.5L8 1.5L13 5.5V13H3Z','M1.7 6.5L3 5.5M13 5.5L14.3 6.5M8 13V15M6 11H10'),
      'feather':('M3 12C-1 8 7-1 13 2C16 7 10 15 5 13Z','M2 15L11 4M5 12L5 8M8 9H12'),
      'flame-kindling':('M8 1Q8 5 11 5L12 3Q16 9 11 11Q5 14 3 9Q1 5 8 1Z','M2 12L14 15M2 15L14 12'),
      'flower-2':('M8 5C2-1 0 5 5 8C-1 11 5 17 8 11C11 17 17 11 11 8C17 5 11-1 8 5Z',st(ci(8,8,1.6),1.1)),
      'mountain-snow':('M1 14L7 2L15 14Z','M5 6L7 8L9 6M10 14L12 9'),
      'rose':('M8 8C2 9 0 3 4 2Q7 0 9 2Q14 0 14 5Q13 9 8 8Z','M4 2Q4 6 10 6M9 2L8 4M8 8V15M8 12Q3 12 3 9Q7 9 8 12'),
      'shovel':('M5 8H11V11Q11 15 8 15Q5 15 5 11Z','M8 8V5M5 1H11V3Q11 5 8 5Q5 5 5 3Z'),
      'shrub':('M3 12C-1 10 1 5 4 6C3 1 10 0 11 5C16 3 17 11 13 12Z','M8 9V15M8 12L5 10M8 12L11 9'),
      'stone':('M2 6L6 2L12 3L15 9L11 14L4 13L1 10Z','M2 6L7 7L12 3M7 7L11 14'),
      'tree-deciduous':('M4 11C-1 9 1 4 5 5C4 0 11 0 11 5C16 4 17 10 12 11Z','M8 8V15M5 15H11'),
      'tree-palm':('M8 5Q1 6 1 10Q5 8 8 5Q8 0 2 2Q4 5 8 5Q12 0 15 4Q12 6 8 5Q15 5 15 11Q11 8 8 5Z','M8 6L6 15M4 15H10'),
      'bone':('M3 1Q6 0 6 3L12 9Q15 9 15 12Q16 15 13 15Q10 16 10 13L4 7Q1 7 1 4Q0 1 3 1Z',None),
      'origami':('M1 6L15 1L10 15L6 10L1 6Z','M1 6L9 6L15 1M9 6L6 10M9 6L10 15'),
      'panda':('M4 4Q1 1 1 5Q1 7 3 7Q2 14 8 14Q14 14 13 7Q15 7 15 4Q15 1 12 4Q8 1 4 4Z',un(ci(5,8,1.25),ci(11,8,1.25),st('M7 11H9M8 11V12',1))),
      'rat':('M2 9Q4 5 8 6Q10 3 12 5L14 9L12 11H4Z','M4 11Q0 14 1 6M6 11V13M10 11V13M11 8H11.1'),
      'shell':('M7 14C1 11-1 4 3 3C3 0 7 1 8 3C10 0 14 1 13 4C18 5 14 12 9 14Z','M8 3V14M4 4L7 13M12 5L9 13M6 14H10'),
      'shrimp':('M12 4C8-1 1 1 1 7C1 12 7 15 12 13L15 14V10L12 11Q5 14 4 8Q4 4 8 5L12 7Z','M9 4L14 1M11 5L15 4M2 6L4 7M3 10L5 9M6 13L7 11M9 13L9 11M9 5H9.1'),
      'snail':(un(ci(7,8,4),p('M2 13H13Q15 13 14 10V8H11V11H2Z')),'M6 6Q10 5 9 9Q8 11 6 9M12 8V6M14 8L15 6'),
      'squirrel':('M5 13Q1 12 2 8Q0 4 4 2Q9-1 10 3Q10 5 7 6Q4 4 4 8Q4 10 7 10L9 7L9 4L12 5L14 8L12 10V13Z','M9 10L11 11M11.5 7H11.6M7 13V15H13'),
      'turtle':(un(ci(7,8,4),ci(13,8,1.8)),st('M4 5L2 3M4 11L2 13M10 5L11 3M10 11L11 13M4 7L7 5L10 7L9 10H5Z',1.1)),
      'worm':('M3 6C0 5 0 10 3 10H6Q8 15 12 13C16 12 16 6 12 7Q10 7 10 10Q8 7 6 7Z','M4 7V10M7 9L8 11M11 9L13 10M2 7H2.1'),
    }
    for n,(b,d) in nature.items():s(n,b,d)
    b,d,o,c,t=drawings['birdhouse'];drawings['birdhouse']=(b,un(d,st(ci(8,7.8,1.6),1)),o,c,t)
    g('cannabis','M8 15V2M8 11Q2 6 1 4Q6 4 8 11Q10 4 15 4Q14 7 8 11Q13 9 15 10Q13 13 8 11Q3 13 1 10Q3 9 8 11Q5 5 8 1Q11 5 8 11')
    off('cannabis-off','cannabis');off('shrimp-off','shrimp')
    # A park/tree grouping intentionally shows separate trunks and canopies.
    g('park','M3 11V15M1 15H15M1 8L3 2L5 8ZM7 10H14M8 10V13M13 10V13M8 7H14V10')
    g('trees','M2 10L5 3L8 10ZM5 10V15M10 12V15M8 10C5 7 8 3 10 5C11 1 16 5 14 8Q17 12 12 12')
    # Board games and leisure symbols.
    g('bow-arrow','M2 2Q14 2 14 14M2 2L7 9L14 14M2 14L12 4M9 4H12V7')
    s('bomb',ci(7,9,5),st('M10 5L12 3Q13 1 15 2M13 1V3',1.2))
    clover=un(*(ci(x,y,3.25) for x,y in [(5.8,5.8),(10.2,5.8),(5.8,10.2),(10.2,10.2)]))
    s('clover',clover,op(st('M9 10L14 15',1.1),clover,po.PathOp.DIFFERENCE))
    s('crown','M2 4L5 7L8 2L11 7L14 4L12 13H4Z','M4 10H12')
    for n in range(1,7):
        positions={1:[(8,8)],2:[(5,5),(11,11)],3:[(5,5),(8,8),(11,11)],4:[(5,5),(11,5),(5,11),(11,11)],5:[(5,5),(11,5),(8,8),(5,11),(11,11)],6:[(5,5),(11,5),(5,8),(11,8),(5,11),(11,11)]}[n]
        s(f'dice-{n}',rr(2,2,12,12,2),dots(*positions,r=.7))
    s('dices',un(rr(1,1,8,8,1.5),rr(6,6,9,9,1.5)),un(st(rr(6,6,9,9,1.5),1.1),dots((3,3),(7,7),(9,9),(12,12),r=.6)))
    s('gamepad-2','M5 4H11Q14 4 15 12Q15 15 12 13L10 11H6L4 13Q1 15 1 12Q2 4 5 4Z',un(st('M3 7H7M5 5V9',1),dots((11,6),(13,8),r=.6)))
    g('gamepad-directional','M6 2H10V6H14V10H10V14H6V10H2V6H6Z')
    s('gem','M4 2H12L15 6L8 15L1 6Z','M1 6H15M4 2L6 6L8 15M12 2L10 6L8 15')
    s('ghost','M2 14V7C2-1 14-1 14 7V14L11 12L8 14L5 12Z',dots((5.5,7),(10.5,7),r=.8))
    g('goal','M2 14V2H14V14M2 2L5 6H14M5 6V14M2 14H14M8 6V14M11 6V14M5 10H14')
    s('joystick',rr(2,10,12,4,1.5),un(ln((8,10),(8,5)),ci(8,3,2),ci(4,12,.5)))
    s('playing-card',rr(3,1,10,14,1.5),poly([(8,5),(11,8),(8,11),(5,8)]))
    s('playing-cards',un(rr(1,1,9,12,1.5),rr(6,3,9,12,1.5)),un(st(rr(6,3,9,12,1.5),1.1),poly([(10.5,7),(12.5,9),(10.5,11),(8.5,9)])))
    s('playing-cards-fan',un(tr(rr(4,2,8,12,1),-25),tr(rr(4,2,8,12,1),25),rr(5,3,7,12,1)),st('M5 4V15H12V4M7 8L8.5 6L10 8L8.5 10Z',1))
    for n,text in [('scroll',False),('scroll-text',True)]:
        s(n,'M4 2H13Q15 2 15 4V5H12V12Q12 15 9 15H3Q1 15 1 12H4Z',st('M4 2V5M4 12H9Q8 15 9 15'+('M6 6H10M6 9H10' if text else ''),1.1))
    s('skull','M5 13V10C-1 8 0 1 8 1C16 1 17 8 11 10V13Z',un(ci(5,6,1.3),ci(11,6,1.3),poly([(8,7),(9,9),(7,9)]),st('M7 11V13M9 11V13',.8)))
    g('sword','M3 13L13 3L14 1L11 2L2 11M1 9L7 15M2 14L1 15')
    g('swords','M2 1L4 2L13 12M1 2L2 4L12 13M15 1L13 2L3 12M15 2L14 4L4 13M1 10L6 15M10 15L15 10')
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
      'knight':'M4 12Q3 8 8 6L4 6L3 4L8 1L12 3L11 12Z',
    }
    for kind,b in chess.items():
        n='chess-'+kind;s(n,un(p(b),rr(3,12,10,2,.4)),st('M7 4L9 6',1) if kind=='bishop' else (st('M8 1V5M6 3H10',1.25) if kind=='king' else (ci(8,3,.5) if kind=='knight' else None)))
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
      'belarusian-ruble':'M2 2H5Q9 2 7 6Q11 10 6 12H2ZM2 6H5M10 13V7Q12 5 14 7',
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
    g('hand-coins','M1 11H5L7 9H11Q14 9 12 11L8 14H3M6 11H9',un(st(ci(6,4,2),1.2),st(ci(11,3,2),1.2)))
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
      'dam':('M5 2H11L14 14H2Z','M5 5H11M5 8H11M1 11H3M13 11H15M6 11V14M10 11V14'),
      'dome':('M1 11C1-1 15-1 15 11Z','M1 14H15M4 11V14M12 11V14M8 1V3'),
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
      'forklift':('M1 8H7V12H1Z','M2 8V3H7V12M7 9H11M11 2V13H15M2 12V14M6 12V14'),
      'helicopter':('M3 7H9Q14 7 14 11H4L2 7H1V5H3Z','M8 7V3M3 3H14M9 7V11M5 11V14M11 11V14M3 14H14'),
      'hot-air-balloon':('M8 1C4.5 1 2 3.2 2 6Q2 9.3 6 12H10Q14 9.3 14 6C14 3.2 11.5 1 8 1Z','M6 12V15H10V12M8 1C4.5 4 4.5 8.5 8 12C11.5 8.5 11.5 4 8 1M2 6.5H14'),
      'kayak':('M8 1C1 4 1 12 8 15C15 12 15 4 8 1Z','M2 3L14 13M1 2L4 3L3 5M12 11L15 13L14 15M6 8Q8 5 10 8Q8 11 6 8Z'),
      'parking-meter':(rr(4,1,8,10,3),'M8 11V15M6 4H10V7H6ZM8 7V9'),
      'road':('M5 1H11L15 15H1Z','M8 3V5M8 8V10M8 13V15'),
      'sailboat':('M1 11H15L12 15H4Z','M8 11V1L14 9H8M6 3L2 9H6Z'),
      'ship-cargo':('M1 10L5 12H11L15 10L13 14H3Z','M3 10V6H7V10M7 10V6H11V10M11 10V3H14V10M4 6V3H8V6'),
      'tractor':('M2 8H8V12H2ZM8 12V4H13L15 8V12Z','M3 8V5H5V8M9 8H14'),
      'traffic-cone':('M7 1H9L13 13H3Z','M5 6H11M4 10H12M1 14H15'),
      'trailer':(rr(2,4,11,8,1),'M13 10H15M4 12V14M11 12V14M5 4V12'),
      'train-front-tunnel':('M5 7H11V13H5Z','M2 14V7C2-1 14-1 14 7V14M5 10H11M6 13L5 15M10 13L11 15'),
      'tram-front':(rr(3,3,10,10,2),'M3 7H13M5 10H5.1M11 10H11.1M8 3V1M5 1H11M5 13L3 15M11 13L13 15'),
      'van':('M1 5H10L15 9V13H1Z','M3 5V9H14M8 5V13M3 13V15M12 13V15'),
    }
    for n,(b,d) in transport.items():s(n,b,d)
    for n in ['tractor']:
        b,d,o,c,t=drawings[n];drawings[n]=(b,un(d,st(ci(4,12,2.5),1.2),st(ci(12,12,1.8),1.2)),o,c,t)
    s('baggage-claim',rr(3,2,9,8,1),'M5 2V1H10V2M1 12H15M1 15H15M3 12V15M7 12V15M11 12V15')
    s('circle-gauge',ci(),un(st('M4 8A4 4 0 0 1 12 8M8 9L11 6',1.1),ci(8,9,.8)))
    s('octagon-minus',poly([(5,1),(11,1),(15,5),(15,11),(11,15),(5,15),(1,11),(1,5)]),'M4 8H12')
    g('drone',un(st('M4 4L12 12M4 12L12 4',1.4),*(st(ci(x,y,2.5),1.1) for x,y in [(3.5,3.5),(12.5,3.5),(3.5,12.5),(12.5,12.5)]),ci(8,8,1.5)))
    g('moped',un(st(ci(3.5,12,2.5),1.1),st(ci(12.5,12,2.5),1.1),st('M3.5 12H9L11 5H13M11 5L12.5 12M2 7H7V10M9 12L7 7',1.2)))
    g('motorbike',un(st(ci(3.5,12,2.5),1.1),st(ci(12.5,12,2.5),1.1),st('M3.5 12L6 7H9L11 4H13M11 4L12.5 12M6 7L8 12H3.5M3 6H6',1.2)))
    g('scooter',un(st(ci(3,13,2),1.1),st(ci(13,13,2),1.1),st('M3 13H10L12 2H9M12 2L13 13',1.2)))
    g('ship-wheel',un(st(ci(8,8,4.5),1.2),ci(8,8,1),st('M8 1V15M1 8H15M3 3L13 13M3 13L13 3',1.1)))
    g('train-track','M5 1L2 15M11 1L14 15M4.5 4H11.5M4 7H12M3.5 10H12.5M3 13H13')
    badge('truck-electric','truck',poly([(12,8),(9,12),(12,12),(11,15),(15,10),(12,10)]))
    # Sloping aircraft orientation and a separate ground line make takeoff/landing explicit.
    for n,angle in [('plane-takeoff',60),('plane-landing',120)]:
        duo,solid,mono=base_layers('plane');f=lambda a:tr(a,angle, .72,0,-2)
        ground=ln((2,14),(14,14));g(n,un(f(mono),ground));overrides[n]={'duotone':[(f(a),v) for a,v in duo]+[(ground,1)],'solid':un(f(solid),ground),'stroke':un(f(mono),ground)}
    for typ in ['check','minus','plus','x','percent']:
        m=mark(typ) if typ!='percent' else un(st('M10 14L14 10',.9),ci(10,10,.55),ci(14,14,.55))
        badge('ticket-'+typ,'ticket',m)
    off('ticket-slash','ticket')
    duo,solid,mono=base_layers('ticket');front=lambda a:tr(a,scale=.75,dx=1.3,dy=2);back=lambda a:tr(a,scale=.75,dx=-1.3,dy=-2)
    clear=un(front(solid),st(front(solid),1.6));g('tickets',un(op(back(mono),clear,po.PathOp.DIFFERENCE),front(mono)))
    overrides['tickets']={'solid':un(op(back(solid),clear,po.PathOp.DIFFERENCE),front(solid))}
    badge('tickets-plane','tickets',tr(un(*[a for a,v in base_layers('plane')[0] if v==1]),scale=.3,dx=4,dy=4))
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
    s('biceps-flexed','M2 13L3 6L6 2H9L10 5H7L6 9Q12 5 14 10Q16 14 11 14Z','M6 9L5 11M3 6L5 7')
    g('hand-helping','M1 12H5L7 10H11Q14 10 12 12L8 15H3M4 8L7 5H10L12 2H15M5 7L8 8L10 6')
    s('hand-metal','M3 9V2Q5 0 5 3V7H7V5H9V7H11V2Q13 0 13 3V11Q13 15 9 15H6Q4 15 3 12L1 9Q1 7 3 9Z','M5 7V10M9 7V10')
    s('heart-crack',p('M8 14L2 8C-1 3 5-1 8 4C11-1 17 3 14 8Z'),'M8 4L6 7L9 9L7 12')
    s('heart-handshake',p('M8 14L2 8C-1 3 5-1 8 4C11-1 17 3 14 8Z'),'M3 8L6 5H9L6 8Q7 10 9 8L12 10M6 11L8 13')
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
        'cable-car':un(rr(4.4,7.4,2.9,2,.3),rr(8.7,7.4,2.9,2,.3)),
        'helicopter':rr(9.8,8,2.8,1.9,.4),
        'kayak':un(st('M6 8Q8 5 10 8Q8 11 6 8Z',1.1),st('M4 5L11 12',1.1)),
        'tower-control':un(st('M6 4L6.5 6.7M10 4L9.5 6.7',1.1)),
        'feather':st('M4 12L11 4M5 11V8M8 9H11',1.1),
    }.items():
        duo,solid,mono=base_layers(n)
        overrides.setdefault(n,{})['solid']=op(solid,counters,po.PathOp.DIFFERENCE)
    # Individual fruit masses remain distinct in a solid bunch.
    overrides['grape']={'solid':un(*(ci(x,y,1.25) for x,y in [(5,5),(9,5),(12,7),(7,8),(10,10),(7,12),(4,9)]),st('M8 3Q8 1 12 1',1.1))}
    # Wheel circles give transport silhouettes actual wheels rather than feet.
    for n,centers in {'caravan':[(4,12.5),(11,12.5)],'trailer':[(4,12.5),(11,12.5)],'van':[(3.5,13),(12,13)],'forklift':[(2.5,12.5),(6.5,12.5)]}.items():
        b,d,o,c,t=drawings[n]
        wheels=un(*(ci(x,y,1.35) for x,y in centers))
        drawings[n]=(b,un(d,wheels),o,c,t)
    b,d,o,c,t=drawings['motorbike'];drawings['motorbike']=(un(b,rr(6,6,4,2,1)),un(d,rr(7,9,2,2,.5)),o,c,t)
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
