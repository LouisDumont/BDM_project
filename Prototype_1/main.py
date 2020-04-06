import numpy as np
import cv2
import os
import time
import enum

from place import Place
from places import *
from moments import *
from choices import *
from caracter import Caracter
from quests import *
from metadata import *
#from metadata_2 import *

    
if __name__=="__main__":
    print("Welcome")
    print("At any moment, you can press Q to quit.")
    type = input("Type 0 to play, 1 for developer logs: ")
    dev_log = (True if type=="1" else False)
    
    if type is not "Q":
                
        # Launching the adventure!
        caracter = Caracter()
        os.system('cls')
        #bar_daytime.trigger()
        bar_daytime.trigger()
    