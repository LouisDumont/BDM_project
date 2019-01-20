from choice import Choice
#from metadata import *
from caracter import *

class Choice_travel(Choice):
    def __init__(self, description, destination):
        super().__init__(self)
        
class Choice_updateQuest(Choice):
    def __init__(self, description, quest, status, destination):
        super().__init__(description, destination)
        self.quest_ = quest
        self.status_ = status
    
    def apply_effect(self):
        super().apply_effect()
        #print("CHECK")
        #print("Quest " + self.quest_.name_ + "previous status: " + caracter.quests_status[self.quest_.name_])
        caracter.quests_status[self.quest_.name_] = self.status_
        #print("Quest " + self.quest_.name_ + "new status: " + caracter.quests_status[self.quest_.name_])
        self.quest_.apply_impacts()