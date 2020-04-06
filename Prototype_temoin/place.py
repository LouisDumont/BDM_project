import os

from choice import Choice

class Place:
    def __init__(self, dev_log=False):
        self.name_ = "Void Place"
        self.description_ = "The place is empty place."
        self.dev_log_ = dev_log
        self.choices_ = []
        self.visit_num_ = 0
        if self.dev_log_:
            print("INFO: New place instance created.")
    
    def get_description(self):
        return(self.description_)
    
    def print_description(self):
        print(self.description_)
        if self.dev_log_: print("Visit numer " + str(self.visit_num_))
        return()
    
    def add_choice(self, description, res_moment):
        self.choices_.append(Choice(description, res_moment))
    
    def present_choices(self):
        for idx, choice in enumerate(self.choices_):
            print("Type " + str(idx) + " to " + choice.description_)
    
    def make_choice(self):
        self.visit_num_ += 1
        chosen = input("Type your choice: ")
        if chosen == "Q": return()
        
        os.system('cls')
        chosen = int(chosen)
        self.choices_[chosen].print_description()
        self.choices_[chosen].apply_effects()
        self.choices_[chosen].res_moment.trigger()
        
    