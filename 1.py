# Import libraries

import sys
sys.path.insert(1,'/home/pi/Go4Code/g4cSense/skeleton')
from sense_hat import SenseHat
import random
from senselib import *
import time

# Initialisation

sense = SenseHat() # This will be used to control the the SenseHat.
initialise(sense) # Initialises the senselib library, that provides us with some useful functions
sense.set_imu_config(True, True, True) 
sense.clear() # Clears all pixels on the screen.

###Your Code here
sense.show_message("pull up to see the temperature. push down to see the compass", scroll_speed = 0.01)
while True:
  for event in sense.stick.get_events():
    if event.action == "pressed":
      
      if event.direction == "up":
        while True:
          temp=int(sense.get_temperature())
          if temp > 10:
            text_colour = [255,0,0]
            draw_two_digit_number(temp,text_colour[0], text_colour[1], text_colour[2])
          
          elif temp < 10:
            text_colour = [0,0,255]
            draw_two_digit_number(temp,text_colour[0], text_colour[1], text_colour[2])
    
          else:
            text_colour = [0,255,0]
            draw_two_digit_number(temp,text_colour[0], text_colour[1], text_colour[2])
            
          wait (5.0)
          sense.clear()

    if event.direction == "down":
      while True:
        comp=int(sense.get_compass())
        if comp > 180:
          text_colour = [144,73,126]
        
        elif comp < 180:
          text_colour = [206,36,59]
          
        else:
          text_colour = [151,149,79]
      
        sense.show_message("you are " + str(comp) + " degrees from north")
        wait (5.0) 
        sense.clear()
    
    if event.direction == "right":
      while True:
        hum=int(sense.get_humidity())
        if hum > 50:
          text_colour = [100,0,0]
          draw_two_digit_number((hum),text_colour[0], text_colour[1], text_colour[2])
          
        elif hum < 50:
          text_colour = [200,0,0]
          draw_two_digit_number((hum),text_colour[0], text_colour[1], text_colour[2])
          
        else: 
          text_colour = [50,0,0]
          draw_two_digit_number((hum),text_colour[0], text_colour[1], text_colour[2])
          sense.clear()
      
    if event.direction == "left":
      while True:
        tehu=int(sense.get_temperature_from_humidity())
        if tehu > 10:  
          text_colour = [255,0,0]
          draw_two_digit_number(tehu,text_colour[0], text_colour[1], text_colour[2])
                
        elif tehu < 10:
          text_colour = [0,0,255]
          draw_two_digit_number(tehu,text_colour[0], text_colour[1], text_colour[2])
      
        else:
          text_colour = [0,255,0]
          draw_two_digit_number(tehu,text_colour[0], text_colour[1], text_colour[2])
        sense.clear()
      #sense.show_message("it is " + str(tehu))
