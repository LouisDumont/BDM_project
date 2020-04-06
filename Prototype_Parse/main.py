import numpy as np
import os
import time

from node import *
from choices import *
#from metadata import *
from parse_txt import *

    
if __name__=="__main__":
    print("Welcome")
    print("At any moment, you can type Q to quit.")
    type = input("Type 0 to play, 1 for developer logs: ")
    dev_log = (True if type=="1" else False)
    
    if type is not "Q":
                
        # Launching the adventure!
        nodes_list = graph_from_text("content")
        #os.system('cls')
        idx_start = find_node(nodes_list, "scene_begin")
        nodes_list[idx_start].trigger()
    