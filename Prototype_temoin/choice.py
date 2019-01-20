import os

class Choice:
    def __init__(self, description, res_moment):
        self.description_ = description
        self.res_moment_ = res_moment
        
    def print_description(self):
        print(self.description_)
        
    def apply_effect(self):
        #print("Choice made")
        os.system('cls')
        return()
        