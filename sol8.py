###### 1. Initialising the program #############################################

#### 1.1 Import libraries

import sys
sys.path.insert(1,'/home/pi/Go4Code/g4cSense/skeleton')

from sense_hat import SenseHat
from senselib import *
import random

#### 1.2 Initialisation

sense = SenseHat() # This will be used to control the the SenseHat.
sense.clear() # Clears all pixels on the screen.
initialise(sense) # Initialises the senselib library, that provides us with some useful functions
sense.set_imu_config(False, True, True) # Enable the gyroscope

sense.show_message("Ask the ball a question!", scroll_speed=0.04)

#### 1.3 Write answers

answers = ["It is certain",
"It is decidedly so",
"Without a doubt",
"Yes definitely",
"You may rely on it",
"As I see it, yes",
"Most likely",
"Outlook good",
"Yes",
"No",
"Signs point to yes",
"Reply hazy try again",
"Ask again later",
"Better not tell you now",
"Cannot predict now",
"Concentrate and ask again",
"Don't count on it",
"My reply is no",
"My sources say no",
"Outlook not so good",
"Very doubtful"]

###### 2. Main program code  ###################################################

while True:

    #### 2.1 Check if the user shaken the Sense HAT

    ac = sense.get_accelerometer_raw()
    x = ac["x"]
    y = ac["y"]
    z = ac["z"]

    shake = x*x + y*y + z*z

    if shake > 5.0:
        random_message = random.choice(answers)
        sense.show_message(random_message)
