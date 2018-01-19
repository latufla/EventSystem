from datetime import datetime

from jinja2 import Environment, select_autoescape, FileSystemLoader

from view.config import Config as ViewConfig
from view.data.event import Event as EventData, EventResult
from view.data.user import User as PlayerData

from view.enum.event_label import EventLabels
from view.enum.event_state import EventStates
from view.loc import Loc
from view.view.event import View

e = EventData(1, "Lesson 1: Greeting", datetime(2017, 12, 6), EventLabels.LESSON, "http://google.com")
e.description = "<p>Jack Dempsey duckbilled barracudina Razorback sucker longfin escolar; mahseer midshipman warbonnet bramble shark. Blackchin bigeye squaretail eeltail catfish rough scad! Stonecat Cornish Spaktailed Bream hillstream loach longnose lancetfish eel lyretail eel saury: salmon shark Hammerjaw loach minnow, walking catfish.</p>" \
                "<p>Jack yellowfin cutthroat trout clingfish arrowtooth eel yellowtail horse mackerel redmouth whalefish tubeblenny herring tripletail, Owens pupfish summer flounder. Horsefish beachsalmon smalltooth sawfish mud cat catfish tadpole fish.</p>" \
                "<p>Slickhead stoneroller minnow sailfish yellowtail horse mackerel Long-finned sand diver cod, dojo loach sand knifefish lamprey yellowfin croaker labyrinth fish spiny dogfish kappy ground shark. Delta smelt ide noodlefish eel hammerhead shark cookie-cutter shark clown loach sixgill shark bluefish sea chub powen Modoc sucker.</p>" \
                "<p>Southern flounder kelp perch armored searobin yellow-and-black triplefin fangtooth South American Lungfish. Southern Dolly Varden zebra shark smelt-whiting bamboo shark clownfish atka mackerel, shrimpfish. Platy airbreathing catfish Cornish Spaktailed Bream lampfish lagena. Orangespine unicorn fish ribbon sawtail fish, squeaker Blind shark upside-down catfish darter flagfin, blue catfish. Zebra tilapia ilisha stonefish popeye catafula treefish Redhorse sucker. Alooh vendace pomfret ghoul scup kuhli loach ghost carp muskellunge luderick Mexican golden trout orangespine unicorn fish dory, bluntnose minnow orbicular velvetfish, leaffish.</p>" \
                "<p>Nurseryfish zebra trout Alaska blackfish dace squaretail blue eye. Butterflyfish barb; icefish, dorado bandfish snubnose parasitic eel Black mackerel river loach.</p>"
e.state = EventStates.FINISHED
e.participant_list.append(PlayerData(1, "Alex", ""))
e.participant_list.append(PlayerData(2, "La", ""))
e.participant_list.append(PlayerData(3, "Uri", ""))
e.participant_list.append(PlayerData(4, "William", ""))

e.wait_list.append(PlayerData(5, "Ann", ""))
e.wait_list.append(PlayerData(6, "Dick", ""))
e.wait_list.append(PlayerData(7, "Jimmy", ""))

e.results.append(EventResult("Alex","/Alex", 1, 1000))
e.results.append(EventResult("La", "/La", 2, 500))
e.results.append(EventResult("Uri", "/Uri", 3, 300))
e.results.append(EventResult("William", "/William", 4, 0))
e.results.append(EventResult("Ann", "/Ann", 5, 0))
e.results.append(EventResult("Dick", "/Dick", 6, 0))
e.results.append(EventResult("Jimmy", "/Jimmy", 7, 0))

view = View(e, True, "", "")

env = Environment(
    loader=FileSystemLoader('../../templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('testbed/try_event.html')
html = template.render(view=view, config=ViewConfig(), loc=Loc("ru"))

with open("test_bed.html", "w") as file:
    file.write(html)