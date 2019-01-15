import os

from choice import choice

class place:
    def __init__(self, dev_log):
        self.description_ = "The place is empty place."
        self.dev_log_ = dev_log
        self.choices_ = []
        self.links_ = []
        self.visit_num_ = 0
        if self.dev_log_:
            print("INFO: New place instance created.")
    
    def get_description(self):
        return(self.description_)
    
    def print_description(self):
        print(self.description_)
        if self.dev_log_: print("Visit numer " + str(self.visit_num_))
        return()
    
    def add_choice(self, description, link):
        self.choices_.append(choice(description))
        self.links_.append(link)
    
    def present_choices(self):
        for idx, choice in enumerate(self.choices_):
            print("Type " + str(idx) + " to " + choice.description_)
    
    def make_choice(self):
        self.visit_num_ += 1
        chosen = input("Type your choice: ")
        if chosen == "Q": return()
        
        os.system('cls')
        chosen = int(chosen)
        self.links_[chosen].print_description()
        self.links_[chosen].present_choices()
        self.links_[chosen].make_choice()
        
    