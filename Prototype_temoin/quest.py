from moment import Moment
from moments import *
from choice import Choice
from choices import *
#from metadata import *
from caracter import *

class Impact:
    def __init__(self, moment, status, choice, toggle):
        self.moment_ = moment # Moment
        self.status_ = status # list of string
        self.choice_ = choice # Choice
        self.toggle_ = toggle # Bool
            

class Quest:
    def __init__(self, name="Dev test quest"):
        self.name_ = name
        self.impacts_ = []
        caracter.quests_status[self.name_] = "0"
        
    def add_impact(self, moment, status, choice, toggle):
        #print("Impact added to " + self.name_)
        self.impacts_.append(Impact(moment, status, choice, toggle))
        
    def apply_impacts(self):
        for impact in self.impacts_:
            if caracter.quests_status[self.name_] in impact.status_:
                if impact.toggle_ and impact.choice_  not in impact.moment_.choices_:
                    impact.moment_.add_choiceC(impact.choice_)
                if impact.choice_ in impact.moment_.choices_ and not impact.toggle_:
                    impact.moment_.choices_.remove(impact.choice_)