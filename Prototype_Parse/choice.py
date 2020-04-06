import os

class Choice:
    def __init__(self, description, res_node):
        self.description_ = description
        self.res_node_ = res_node
        
    def print_description(self):
        print(self.description_)
        
    def apply_effect(self):
        #print("Choice made")
        os.system('cls')
        return()
        