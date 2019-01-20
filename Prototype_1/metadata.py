import time

from caracter import Caracter
from places import *
from choices import *
from moments import *
from quests import *

#caracter = Caracter()
dev_log = False

### Environment Settings

# Initializing all Quests to default
quest1 = Quest_test1()
quests_tab = [quest1]

# Setting up the places in the universe
print("Setting up the Universe...")
        
temple = Temple(dev_log)
if dev_log: temple.print_description()
        
bar = Bar(dev_log)
if dev_log: bar.print_description()
        
townhall = Townhall(dev_log)
if dev_log: townhall.print_description()
        
        
print("Universe set up!")
time.sleep(1)
 
# Setting up the moments
        
print("Setting up the Moments...")
        
bar_daytime = Bar_daytime(bar, dev_log)
bar_night = Bar_night(bar, dev_log)
temple_regular = Temple_regular(temple, dev_log)
temple_priestConv = Temple_priestConv(temple, dev_log)
temple_office = Temple_office(temple, dev_log)
townhall_daytime = Townhall_daytime(townhall, dev_log)
        
print("Moments set up!")
time.sleep(1)
        
# Setting up the navigation links
        
print("Setting up the navigation links...")
        
# Inherent to places
bar.add_choice("go to the temple.", temple_regular)
bar.add_choice("go to the townhall.", townhall_daytime)        
temple.add_choice("go to a bar.", bar_daytime)
temple.add_choice("go to the townhall.", townhall_daytime)        
townhall.add_choice("go to a bar.", bar_daytime)
townhall.add_choice("go to the temple.", temple_regular)
# Related to the moments
bar_daytime.add_choice("wait until the night.", bar_night)
bar_night.add_choice("drink all night long.", bar_daytime)
temple_regular.add_choice("talk to a priest.", temple_priestConv)
temple_priestConv.add_choice("say \"I want to assist to an office\"", temple_office)
temple_priestConv.add_choice("say \"It's nothing\"", temple_regular)
        
print("Navigation links set up!")
time.sleep(1)

### Quests initialization

order_beer = Choice_updateQuest("order a beer.", quest1, "1", bar_night)
drunkly_dance = Choice_updateQuest("drunkly dance on a table.", quest1, "2", bar_night)
get_confessed = Choice_updateQuest("get confessed", quest1, "3", temple_priestConv)
quest1.add_impact(bar_daytime, ["0"], order_beer, True)
quest1.add_impact(bar_night, ["0"], order_beer, True)
quest1.add_impact(bar_daytime, ["1"], order_beer, False)
quest1.add_impact(bar_night, ["1"], order_beer, False)
quest1.add_impact(bar_night, ["1"], drunkly_dance, True)
quest1.add_impact(temple_priestConv, ["2"], get_confessed, True)

#for key in caracter.quests_status:
    #print(key)
    #print(caracter.quests_status[key])

for quest in quests_tab:
    quest.apply_impacts()