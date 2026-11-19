"""Catalog compositions for media, education, wellness, travel and culture."""
from pathlib import Path
import json
import re

from geometry import BOLD, DETAIL, EDGE, GUIDE, oval, rounded
from scenes.editorial_objects import At, OBJECTS
from scenes.editorial_briefs import MEDIA, EDUCATION, HEALTH, TRAVEL, CULTURE

GROUP_IDS = (
    "publishing-editorial-and-media",
    "education-and-events",
    "health-and-wellness",
    "travel-mobility-and-places",
    "culture-membership-and-communities",
)


def place(s, item, x, y, z=0, scale=1):
    OBJECTS[item][1](At(s,x,y,z,scale))


def check(s,x,y,z):
    s.line([(x-7,y+4,z),(x+3,y+7,z),(x-2,y-10,z)],BOLD)


def plate_outline(s,x,y,z,w,d,ink=DETAIL,dashed=False):
    ring=rounded(x,y,w,d,4)
    s.line([(*p,z) for p in [*ring,ring[0]]],ink,dashed=dashed)


def cancellation(s):
    s.box(0,0,0,100,70,5,5)
    s.line([(9,52,5),(37,52,5),(49,38,5)],EDGE)
    s.line([(60,28,5),(72,15,5),(91,15,5)],DETAIL,dashed=True)
    s.tube([(51,27,5),(60,45,5)],2,BOLD)
    place(s,"ticket",9,4,11,.69)
    s.ellipse(87,15,5,6,6)


def tuition(s):
    s.box(0,0,0,95,66,7,5)
    place(s,"records",8,12,7,1.04)
    for step in range(4):
        s.disk(75,43,7+step*4,13,13,3,BOLD if step==3 else EDGE)
    check(s,75,43,22)


def care_team(s):
    place(s,"badge",2,0,31,.88)
    place(s,"badge",54,8,54,.88)
    place(s,"badge",98,36,34,.88)
    for x,y,z in ((20,16,31),(74,18,54),(118,51,34)):
        s.line([(x,y,5),(x,y,z)],dashed=True)
    place(s,"records",27,29,0,1)


def family_bundle(s):
    place(s,"ticket",1,6,0,1.27)
    place(s,"badge",8,12,11,1.12)
    place(s,"badge",25,21,20,1)
    place(s,"badge",45,23,29,.9)
    s.face([(62,23,32),(72,23,32),(72,58,32),(62,58,32)],DETAIL)
    s.face([(62,58,32),(72,58,32),(72,58,8),(62,58,8)],DETAIL)


def wellbeing(s):
    place(s,"mat",1,8,0,1.45)
    place(s,"bottle",61,0,0,.79)
    place(s,"records",61,34,0,.76)


def class_register(s):
    s.box(11,0,0,80,8,70,4)
    for z in (22,37,52):
        s.line([(37,8,z),(81,8,z)])
        s.line([(x,8,y) for x,y in oval(27,z,3,3)],EDGE)
    s.line([(25,8,37),(27,8,34),(31,8,40)],BOLD)
    place(s,"calendar",42,24,0,.88)


def prescription_history(s):
    for i in range(3):
        x,y = i*49,i*10
        place(s,"pills",x,y,i*6,.92-i*.14)
    s.line([(9,63,0),(139,63,0)],EDGE)
    for x in (21,66,113):
        s.line([(x,59,0),(x,67,0)])


CUSTOM = {
    "trip-cancellation": ("A barrier interrupts the route beside a clipped ticket.",cancellation),
    "tuition-deposit-recorded": ("A sealed coin stack sits beside the deposit record.",tuition),
    "care-team-introduction": ("Three credentials lead down to one shared patient record.",care_team),
    "family-membership-bundle": ("A ticket and three credentials fan out from a single strap.",family_bundle),
    "employee-wellbeing-benefits": ("An exercise mat and a capped bottle sit beside a care record.",wellbeing),
    "class-register": ("A roster board records attendance beside a calendar.",class_register),
    "prescription-history": ("Three blister packs are spaced along a marked timeline.",prescription_history),
}


def scene_for(mode, first, second):
    a,b = OBJECTS[first][0], OBJECTS[second][0]

    def draw(s):
        if mode == "display":
            s.box(0,0,0,94,75,6,6)
            s.box(11,10,6,62,54,7,5)
            place(s,first,14,13,13)
            place(s,second,70,48,6,.56)
        elif mode == "select":
            s.box(0,0,0,144,66,6,6)
            plate_outline(s,7,8,6,69,47,EDGE)
            place(s,first,12,10,6,.86)
            place(s,second,86,14,6,.87)
            s.box(25,51,6,33,9,4,3,BOLD)
        elif mode == "queue":
            for step in range(3):
                x,y = step*33, step*11
                s.box(x,y,0,33,43,5,4)
                if step == 1:
                    plate_outline(s,x+4,y+4,5,25,35,dashed=True)
                else:
                    place(s,first if step==0 else second,x+4,y+8,5,.47)
            s.line([(10,57,0),(113,68,0)],DETAIL,dashed=True)
        elif mode == "stage":
            s.box(0,0,0,81,65,6,6)
            for x,y in ((9,7),(67,8),(69,53)):
                s.line([(x,y,7),(x,y,25)],dashed=True)
            place(s,second,19,19,6,.67)
            place(s,first,11,-2,39,.96)
        elif mode == "pair":
            s.box(0,0,0,138,70,7,6)
            s.line([(69,8,7),(69,61,7)])
            place(s,first,8,11,7,.87)
            place(s,second,82,14,7,.86)
        elif mode == "route":
            s.box(0,0,0,155,83,5,7)
            s.tube([(17,66,6),(53,66,6),(69,46,6),(85,36,6),(122,36,6)],1.65,DETAIL)
            for x,y in ((53,66),(69,46),(85,36)):
                s.disk(x,y,5,3,3,3)
            place(s,first,11,38,5,.82)
            place(s,second,105,14,5,.77)
        elif mode == "detail":
            # A clearly isolated detail sits on a small round turntable.
            s.disk(39,40,0,40,34,7)
            place(s,first,13,18,7,.91)
            s.line([(61,34,13),(97,34,13),(103,47,13)],EDGE,dashed=True)
            s.disk(108,48,0,24,21,5,DETAIL)
            place(s,second,94,35,5,.58)
        elif mode == "confirm":
            s.box(0,0,0,126,63,8,6)
            place(s,first,11,7,8,.97)
            place(s,second,83,10,8,.58)
            s.disk(103,44,8,13,13,5,BOLD)
            check(s,102,45,13)
        elif mode == "receive":
            s.box(0,0,0,124,58,6,6)
            s.box(0,0,6,124,6,13,3)
            s.box(0,52,6,124,6,13,3)
            place(s,first,12,10,6,.9)
            place(s,second,75,10,25,.66)
            s.line([(80,29,6),(80,29,25)],dashed=True)
        elif mode == "hold":
            s.box(0,0,0,119,70,7,6)
            place(s,second,14,11,7,.84)
            plate_outline(s,68,12,7,43,44,dashed=True)
            place(s,first,69,10,27,.72)
            s.line([(71,16,8),(71,16,26)],dashed=True)
        elif mode == "protect":
            s.box(0,0,0,106,70,7,6)
            place(s,first,12,14,7,.9)
            s.tube([(5,6,7),(101,6,7),(101,63,7),(5,63,7),(5,6,7)],1.8)
            place(s,second,75,42,12,.55)
        elif mode == "arrange":
            s.box(0,0,0,110,106,6,6)
            for x,y in ((9,9),(58,9),(9,57),(58,57)):
                plate_outline(s,x,y,6,42,39,dashed=(x,y)==(58,57))
            place(s,first,12,12,6,.64)
            place(s,second,60,12,6,.67)
            place(s,first,11,60,8,.61)
        elif mode == "signal":
            place(s,first,7,21,0,1)
            place(s,second,82,1,0,.89)
            for radius in (13,24,34):
                s.ellipse(76,43,25,radius,radius,EDGE if radius==24 else DETAIL,-35,75)
        elif mode == "rise":
            for i in range(3):
                s.box(i*37,5,0,36,52,7+i*14,4)
            place(s,second,5,15,7,.54)
            place(s,first,74,7,35,.78)
        elif mode == "open":
            s.box(0,0,0,115,75,6,7)
            s.face([(0,3,6),(115,3,6),(110,-8,47),(5,-8,47)],EDGE)
            place(s,second,65,17,6,.67)
            place(s,first,9,14,6,.83)
            s.box(0,66,6,115,9,11,3)
        else:
            raise ValueError(f"Unknown composition {mode!r}")

    descriptions = {
        "display": f"A shallow raised display presents {a} beside {b}.",
        "select": f"A highlighted position picks out {a} beside {b}.",
        "queue": f"Three waiting bays place {a} ahead of {b}, with one open position.",
        "stage": f"Alignment guides hold {a} above {b}.",
        "pair": f"One divided platform presents {a} and {b} side by side.",
        "route": f"A marked path connects {a} with {b}.",
        "detail": f"A locating guide connects {a} to a separate view of {b}.",
        "confirm": f"A seal beside {a} and {b} marks the completed state.",
        "receive": f"A receiving tray holds {a} below an arriving {b[2:] if b.startswith('a ') else b[3:] if b.startswith('an ') else b}.",
        "hold": f"An open position sits underneath {a}, next to {b}.",
        "protect": f"A raised border surrounds {a} and {b}.",
        "arrange": f"Marked positions organize {a} and {b}, leaving one position open.",
        "signal": f"Three signal arcs bridge the gap between {a} and {b}.",
        "rise": f"Stepped surfaces lead from {b} up to {a}.",
        "open": f"An open case holds {a} and {b} side by side.",
    }
    return descriptions[mode],draw


EXISTING = """
blog-home display article book
reading-experience detail book pencil
knowledge-base arrange folio book
embargoed-release protect article calendar
editorial-calendar pair calendar article
author-profile stage badge article
content-syndication route press article
featured-article stage article book
book-excerpts detail book article
content-licensing protect photo badge
video-captions display screen dialogue
podcast-episodes queue mics mic
image-lightbox stage photo easel
interactive-map-story pair map article
reading-list queue book article
editorial-corrections detail pencil article
creative-asset-delivery receive folio photo
live-streaming signal camera screen
media-transcoding route reel screen
rights-clearance confirm badge reel
course-catalog arrange book test
start-a-course rise easel book
course-progress route test medal
course-completion confirm medal book
event-registration receive ticket calendar
event-schedule pair calendar stage
event-speakers display podium badge
live-webinar signal podium screen
workshop open easel goggles
student-assessment detail test pencil
practice-exercises select test book
flashcards stage test folio
grading-rubric pair test test
portfolio-submission receive folio easel
waitlisted-event queue ticket seat
event-check-in confirm ticket badge
seating-plan detail seats seat
event-replay stage reel stage
live-polling signal podium test
funded-scholarship open medal test
open-enrollment open folio book
credential-verification confirm badge medal
laboratory-safety-training protect goggles sample
clinician-appointment pair calendar records
remote-consultation signal screen records
medical-records protect records folio
prescription-refill receive pills bottle
care-plan pair records test
lab-results detail sample records
find-a-clinic route map landmark
dental-care display records goggles
physical-therapy route mat bench
sleep-tracking detail bed watch
hydration-reminder stage bottle watch
workout-planning pair calendar dumbbell
heart-rate-trend signal watch screen
movement-goal rise mat watch
meditation-session display mat bowl
nutrition-plan pair bowl records
accessibility-aids-fitting stage seat scale
wearable-data-sync signal watch records
destination-guide display map landmark
trip-itinerary pair calendar map
hotel-search select room map
route-planning route map pin
find-a-nearby-location detail pin map
transit-stops queue stop vehicle
departure-board display screen stop
boarding-pass confirm ticket case
baggage-tracking signal case pin
bike-share open rack map
ev-charging-station pair charger vehicle
parking-availability hold vehicle map
road-closure protect map beacon
accessible-transport stage seat vehicle
trail-conditions detail mountain map
luggage-allowance pair scale case
trip-cancellation protect ticket calendar
multiple-stops route stop pin
car-rental-pickup receive vehicle key
accommodation-amenities arrange room seat
fleet-dispatch route vehicle stop
community-forum signal dialogue dialogue
member-directory arrange badge dialogue
membership-benefits display badge key
museum-collection arrange sculpture archive
exhibition-tickets pair ticket sculpture
join-a-group receive badge dialogue
community-guidelines open book dialogue
threaded-discussion rise dialogue dialogue
flag-inappropriate-content protect dialogue beacon
member-achievement confirm medal badge
mentorship pair podium seat
club-events select calendar stage
membership-renewal stage badge calendar
venue-accessibility pair stage seat
artifact-conservation protect sculpture goggles
exhibition-map route map sculpture
digital-archive protect archive screen
oral-history-project pair mics archive
collective-funding stage sculpture badge
"""

def registration(group, ident, title, placement, mode, first, second):
    visual,draw = CUSTOM[ident] if ident in CUSTOM else scene_for(mode,first,second)
    return (group,ident,title,placement,visual,draw)


def original_briefs():
    groups = json.loads((Path(__file__).resolve().parents[2]/"catalog/use-cases.json").read_text())["groups"]
    authored = {case["id"]:(group["id"],case) for group in groups if group["id"] in GROUP_IDS
                for case in group["cases"] if not case.get("asset")}
    for line in EXISTING.strip().splitlines():
        ident,mode,first,second = line.split()
        group,case = authored.pop(ident)
        yield registration(group,ident,case["title"],case["placement"],mode,first,second)
    if authored:
        raise ValueError(f"Unmapped briefs: {', '.join(authored)}")


def add_briefs(group, rows):
    for row in rows.strip().splitlines():
        title,placement,recipe = row.split("|")
        ident = re.sub(r"[^a-z0-9]+","-",title.lower()).strip("-")
        yield registration(group,ident,title,placement,*recipe.split())


PACK = list(original_briefs())
for group, briefs in zip(GROUP_IDS, (MEDIA, EDUCATION, HEALTH, TRAVEL, CULTURE)):
    PACK.extend(add_briefs(group, briefs))
