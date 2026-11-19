from geometry import BOLD, EDGE, DETAIL, oval, rounded


def documentation(s):
    s.box(0,0,0,132,76,5,5)
    # The gutter stays low while the outer shoulders of the open book rise.
    left = [(5,4,14),(58,4,11),(66,8,6),(66,71,6),(57,73,11),(5,73,14)]
    right = [(66,8,6),(75,4,12),(126,4,18),(126,73,18),(75,73,12),(66,71,6)]
    s.face(left)
    s.face(right,BOLD)
    for y,width in ((22,38),(32,28),(42,35),(52,22)):
        s.line([(12,y,13),(12+width,y,12)])
        s.line([(77,y,13),(77+width,y,17)],DETAIL)
    s.line([(53,8,12),(53,1,12),(49,-7,8),(44,0,10)],EDGE)


def video_library(s):
    # Perforated film crosses a tilted viewing gate.
    s.box(0,18,0,134,55,6,6)
    s.face([(5,35,8),(130,35,8),(130,35,49),(5,35,49)])
    for x in range(12,125,9):
        for z in (13,44):
            s.line([(x,35,z),(x+3,35,z)])
    for x in (19,57,95):
        stencil = rounded(x,19,26,19,2)
        s.line([(a,35,z) for a,z in [*stencil,stencil[0]]],EDGE)
        if x==57:
            s.face([(66,35,23),(66,35,34),(75,35,28.5)],BOLD)
    s.box(51,31,49,37,8,9,2,BOLD)


def audio_playback(s):
    arch = [(64+45*x,21,19+75*(max(0,1-x*x)**.54)) for x in (k/24 for k in range(-24,25))]
    s.tube(arch,4.5,BOLD)
    s.box(9,12,2,20,27,32,7)
    s.box(26,13,6,7,25,24,3,DETAIL)
    s.box(100,13,6,7,25,24,3,DETAIL)
    s.box(106,12,2,20,27,32,7)
    s.line([(113,39,14),(120,39,14)])


def photo_gallery(s):
    s.box(60,0,0,58,75,4,4,DETAIL)
    s.box(48,14,4,54,70,4,4)
    s.face([(0,52,5),(94,52,5),(94,17,65),(0,17,65)],BOLD)
    def panel(x,z):
        return (x, 52-(z-5)*35/60, z)
    inset = rounded(8,13,78,44,4)
    s.line([panel(x,z) for x,z in [*inset,inset[0]]])
    s.line([panel(x,z) for x,z in ((8,22),(28,43),(43,29),(57,47),(86,21))],EDGE)
    s.line([panel(x,z) for x,z in oval(70,48,5,5)],DETAIL)


def newsletter(s):
    # The broadsheet bends along its fold as it comes out of a delivery sleeve.
    s.box(-4,11,0,124,74,5,6)
    s.face([(5,16,7),(102,16,7),(102,53,41),(5,53,41)],BOLD)
    s.face([(5,53,41),(102,53,41),(102,88,16),(5,88,16)],BOLD)
    def fold(x,y):
        z = 41-25*(y-53)/35 if y>=53 else 7+34*(y-16)/37
        return (x,y,z)
    s.line([fold(5,53),fold(102,53)])
    s.line([fold(18,29),fold(89,29)],EDGE)
    s.line([fold(x,y) for x,y in ((18,37),(51,37),(51,49),(18,49),(18,37))])
    for y,w in ((38,25),(44,30),(48,21)):
        s.line([fold(58,y),fold(58+w,y)])
    s.line([fold(17,59),fold(90,59)],EDGE)
    s.line([fold(x,y) for x,y in ((17,65),(50,65),(50,76),(17,76),(17,65))])
    for y,w in ((66,30),(71,25),(76,31)):
        s.line([fold(58,y),fold(58+w,y)])
    s.box(-4,77,5,124,8,15,4)


def case_studies(s):
    # An open folio contains a model and the annotated record of its outcome.
    s.box(0,0,0,124,83,5,7)
    s.box(4,4,5,54,74,3,4)
    s.box(65,4,5,53,74,3,4,BOLD)
    s.line([(61,9,5),(61,74,5)])
    s.box(14,19,8,34,29,3,3,DETAIL)
    s.box(20,24,11,9,17,13,2)
    s.box(31,24,11,9,17,24,2,BOLD)
    for y,w in ((17,34),(26,30),(35,23),(49,32),(58,35),(67,24)):
        s.line([(73,y,8),(73+w,y,8)],EDGE if y==17 else DETAIL)


def press_kit(s):
    s.box(0,0,0,126,82,6,7)
    s.box(4,4,6,118,74,4,5)
    s.box(10,10,10,53,52,3,4,BOLD)
    s.line([(18,18,13),(51,18,13)],EDGE)
    for y,w in ((27,35),(35,26),(43,32),(51,23)):
        s.line([(18,y,13),(18+w,y,13)])
    for k in range(3):
        s.box(75+k*5,14+k*4,10+k*3,30,43,2,3)
    s.ellipse(98,44,16,7,7)
    s.box(4,75,9,118,4,3,1.5,DETAIL)
    s.box(27,68,12,72,9,2,2,EDGE)


def multilingual(s):
    # Two page faces share the same typesetting rhythm in opposite directions.
    s.box(0,0,0,57,6,64,4)
    s.box(80,27,0,57,6,64,4,BOLD)
    for i,w in enumerate((32,39,25,33,16)):
        z = 49-i*9
        s.line([(9,6,z),(9+w,6,z)],EDGE if i==0 else DETAIL)
        s.line([(128-w,33,z),(128,33,z)],EDGE if i==0 else DETAIL)
    s.tube([(54,6,15),(66,6,15),(72,14,15),(72,23,15),(84,27,15)],1.9,DETAIL)


def testimonials(s):
    # The notches in the lower edges distinguish speech from document cards.
    for x,y,z,w,h in ((30,0,28,100,40),(0,26,10,104,46)):
        shape = [(x+7,y,z),(x+19,y,z),(x+18,y,z-11),(x+33,y,z),
                 (x+w-6,y,z),(x+w,y,z+6),(x+w,y,z+h-6),(x+w-6,y,z+h),
                 (x+6,y,z+h),(x,y,z+h-6),(x,y,z+6)]
        s.face(shape,BOLD if y else EDGE)
        for i,span in enumerate((47,61,34)):
            level = z+h-13-i*10
            s.line([(x+12,y,level),(x+12+span,y,level)])


def learning_path(s):
    # An uphill track ties the milestones together and ends at a raised pennant.
    milestones = [(14,45,7),(45,40,19),(77,28,34),(107,15,51)]
    s.box(0,0,0,121,62,5,6)
    for x,y,z in milestones:
        s.disk(x,y,5,5,5,z-4,DETAIL)
    s.tube(milestones,2.2,EDGE)
    for x,y,z in milestones:
        s.disk(x,y,z,6,6,3,BOLD if z==51 else EDGE)
    s.tube([(107,15,54),(107,15,80)],1.4)
    s.face([(107,15,80),(132,15,74),(107,15,68)],BOLD)


FIGURES = [
    (documentation,"Documentation","An open reference book keeps two pages in view."),
    (video_library,"Video library","A viewing gate selects a frame on a strip of film."),
    (audio_playback,"Audio playback","A continuous headband connects two cushioned earpieces."),
    (photo_gallery,"Photo gallery","A framed landscape rises above adjoining prints."),
    (newsletter,"Newsletter","An illustrated issue unfolds from its delivery sleeve."),
    (case_studies,"Case studies","An open folio pairs a measured result with its written account."),
    (press_kit,"Press kit","A media pack keeps a fact sheet and image cards together."),
    (multilingual,"Multilingual content","Two versions of a page use different reading directions."),
    (testimonials,"Testimonials","One reader's quote comes forward in a pair of speech panels."),
    (learning_path,"Learning path","A continuous track connects four milestones and a finish flag."),
]
