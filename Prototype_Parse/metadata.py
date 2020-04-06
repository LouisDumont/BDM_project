import time

from choice import *
from nodes import *

#caracter = Caracter()
dev_log = False

### Environment Settings

 
# Setting up the moments
        
print("Setting up the Moments...")
        
#scene_1_0 = Scene_1_0()
#scene_1_1 = Scene_1_1()
#scene_1_2 = Scene_1_2()
        
print("Moments set up!")
time.sleep(1)
        
# Setting up the navigation links
        
print("Setting up the navigation links...")
        
# Related to the moments
scene_1_0.add_choice("Entrer à l’intérieur.", scene_1_1)
scene_1_0.add_choice("Aller voir les policiers à l’extérieur.", scene_1_2)
        
print("Navigation links set up!")
time.sleep(1)
