###### 1. Initialising the program #############################################

#### 1.1 Import libraries

import sys
sys.path.insert(1,'/home/pi/Go4Code/g4cSense/skeleton')

from sense_hat import SenseHat
from senselib import *
import random

#### 1.2 Initialisation

sense = SenseHat() # This will be used to control the the SenseHat.sense.clear() # Clears all pixels on the screen.
initialise(sense) # Initialises the senselib library, that provides us with some useful functions
sense.set_imu_config(False, True, True) # Enable the gyroscope

sense.show_message("Ask the ball a question!", scroll_speed=0.15,text_colour=[255,0,0])

#### 1.3 Write answers

answers = ["yes", "no", "ask again later","Ask again later", "Better not tell you now", "Concentrate and ask again", "Don’t count on it"]

###### 2. Main program code  ###################################################

while True:
  

  #### 2.1 Check if the user shaken the Sense HAT

  ac = sense.get_accelerometer_raw()
  x = ac["x"]
  y = ac["y"]
  z = ac["z"]

  shake = x*x + y*y + z*z

  random_message = random.choice(answers)

  if shake > 5:
      sense.show_message(random_message, scroll_speed=0.1, text_colour= [100,225,100])    
