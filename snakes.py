###### 1. Initialising the game ################################################

#### 1.1 Import libraries

import sys
sys.path.insert(1,'/home/pi/Go4Code/g4cSense/skeleton')

from sense_hat import SenseHat
from snake_lib import Snake
import random
from senselib import *

#### 1.2 Initialisation

sense = SenseHat() # This will be used to control the the SenseHat.
initialise(sense) # Initialises the senselib library, that provides us with some useful functions
sense.clear() # Clears all pixels on the screen.

#### 1.3 Set up the game variables

applePosition = [1, 1] # Set the starting position of the apple
snake = Snake([3,3]) # Creates the snake, and sets its starting position

snakeColour = [0, 255, 0] # Colour of the snake
appleColour = [255, 255, 255] # Colour of the apple

###### 2. Main game code #######################################################

while True:
    sense.clear()

    snake_body = snake.get_body() # Gets the body of the snake, containing all the positions.

    for bodypart in snake_body:
        sense.set_pixel(bodypart[0], bodypart[1], snakeColour[0], snakeColour[1], snakeColour[2])

    # Draw the apple

    sense.set_pixel(applePosition[0], applePosition[1], appleColour[0], appleColour[1], appleColour[2])

    #### 2.1 Let the user control the snake
    for event in sense.stick.get_events():
      if event.action == 'pressed':
        if event.direction == 'up':
          snake.turn_up()
          
        elif event.direction == "down":
          snake.turn_down()
        
            # Fill in with your own code

        elif event.direction == "left":
          snake.turn_left()
            # Fill in with your own code

        elif event.direction == "right":
          snake.turn_right()
            # Fill in with your own code

    #### 2.2 Draw the snake and the apple


    #### 2.3 Move the snake
    snake.move_forward()


    #### 2.4 Check if apple ate an apple
    if snake.get_position() == applePosition:
      snake.grow()
      applePosition = snake.get_new_apple_position()


    #### 2.5 Check if snake has collided with itself
    if snake.has_collided_with_self():
      count = 0
      for bodypart in snake_body:
          count += 1
      sense.show_message("You lose, your score is " + str(count), 0.05)
      snake.reset()
      


    #### 2.6 Add some delay
    wait(0.2)
