import numpy as np
import cv2
import os
import time
import enum

from place import place
from places import *

    
if __name__=="__main__":
    print("Welcome")
    print("At any moment, you can press Q to quit.")
    type = input("Type 0 to play, 1 for developer logs: ")
    dev_log = (True if type=="1" else False)
    
    if type is not "Q":
        
        # Setting up the universe
        print("Setting up the Universe...")
        
        temple1 = temple(dev_log)
        if dev_log: temple1.print_description()
        
        bar1 = bar(dev_log)
        if dev_log: bar1.print_description()
        
        townhall1 = townhall(dev_log)
        if dev_log: townhall1.print_description()
        
        bar1.add_choice("go to the temple.", temple1)
        bar1.add_choice("go to the townhall.", townhall1)
        
        temple1.add_choice("go to a bar.", bar1)
        temple1.add_choice("go to the townhall.", townhall1)
        
        townhall1.add_choice("go to a bar.", bar1)
        townhall1.add_choice("go to the temple.", temple1)
        
        # Launching the adventure!
        
        os.system('cls')
        bar1.print_description()
        bar1.present_choices()
        bar1.make_choice()
    