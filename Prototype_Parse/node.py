import os

from choice import Choice

class Node():
    def __init__(self, description, name='', dev_log=False):
        self.name_ = name
        self.description_ = description
        self.dev_log_ = dev_log
        self.visit_num_ = 0
        self.choices_ = []
        if self.dev_log_:
            print("INFO: New node instance created. Name is " + self.name_ + ".")
        
    def print_description(self):
        print(self.description_)
        if self.dev_log_: print("Visit numer " + str(self.visit_num_))
        return()
        
    def present_choices(self):
        for idx, choice in enumerate(self.choices_):
            print("Type " + str(idx) + " to " + choice.description_)
            
    def add_choiceC(self, choice):
        self.choices_ = [choice] + self.choices_
    
    def add_choice(self, description, res_node):
        self.choices_ = [Choice(description, res_node)] + self.choices_
        print("INFO: New choice added: links node " + self.name_ + " with node " + res_node.name_ + ".")
        
    def make_choice(self):
        chosen = input("Type your choice: ")
        if chosen == "Q": return()
        
        os.system('cls')
        chosen = int(chosen)
        self.choices_[chosen].print_description()
        self.choices_[chosen].apply_effect()
        self.choices_[chosen].res_node_.trigger()
        
    def trigger(self):
        self.visit_num_ += 1
        self.print_description()
        self.present_choices()
        self.make_choice()
        