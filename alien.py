import threading# Import threading to create threads for alien movement
import random # Import random for random movements
from turtle import Turtle# Import Turtle module for game graphics
import os# Import os for file path operations

import constante as cte# Import constants from constante.py
import game# Import the game module

from bomb import Bomb # Import the Bomb class

class Alien_fleet:
    def __init__(self, size, posW, posH, screen):# Initialize the alien fleet attributes
        self.screen = screen # Screen instance
        self.fleet = []# List to store Alien instances
        self.posX_init = posW # Initial X position of the fleet
        self.posY_init = posH# Initial Y position of the fleet
        

    def launch_tempo(self):# Placeholder for future functionality
        return

    def start(self):
        """
        Create aliens and add them to the fleet list.
        Each alien starts its movement in its own thread with a delay.
        """

        for i in range (0,cte.NB_MAX_ALIEN):  # Iterate for the maximum number of aliens
            alien = Alien(self.posX_init + i*100 ,self.posY_init ,self.screen)# Create an alien
            self.fleet.append(alien)# Add the alien to the fleet list

            th_timer = threading.Timer(i, alien.start)  # Start alien movement in a separate thread with a delay

            th_timer.start()

        return

    def get_alien_contact(self , x_bullet, y_bullet):
        """
        Check if a bullet has hit any alien in the fleet.
        Returns the alien if a hit is detected.
        """

        for alien in self.fleet :# Iterate through the fleet
            x_alien, y_alien = alien.get_position()# Get the position of the alien
              # Check if the bullet coordinates overlap with the alien
            if x_bullet < x_alien + cte.ALIEN_WIDTH / 2 and x_bullet > x_alien - cte.ALIEN_WIDTH /2 :
                if y_bullet - cte.BULLET_HEIGHT > y_alien - cte.ALIEN_HEIGHT/2 : 
                    print("contact")# Log the contact

                    return (alien)

        return None # No contact detected
    
    def remove_alien (self, alien):
        """
        Remove an alien from the fleet.
        """

        self.fleet.remove(alien)
    
    def remove_fleet(self):
        """
        Remove all aliens from the fleet.
        """
        for alien in self.fleet :
            alien.delete()
        self.fleet.clear()

    def get_nb_alien(self):
        """
        Return the number of remaining aliens in the fleet.
        """
        return len(self.fleet)
    
# Class representing an individual alien

class Alien:
    def __init__(self, posW, posH, screen):    # Initialize alien attributes

        self.move_possible = True  # Flag for movement
        self.current_x = posW# Current X position
        self.current_y = posH# Current Y position
        self.width = cte.ALIEN_WIDTH# Alien width
        self.heigth = cte.ALIEN_HEIGHT  # Alien height
        self.previous_nb_alien = cte.NB_MAX_ALIEN# Initial number of aliens
        self.screen = screen

        alien_image_path = os.path.join(cte.DIRECTORY_IMAGE, cte.IMAGE__ALIEN_FILE)
        if os.path.exists(alien_image_path ):
            screen.addshape(alien_image_path )
        else:
            print(f"Error: Image file '{alien_image_path }' not found!")
            return
        
 # Load explosion image
        self.boom_image_path = os.path.join(cte.DIRECTORY_IMAGE, cte.IMAGE__BOOM_FILE)
        if os.path.exists(self.boom_image_path ):
            screen.addshape(self.boom_image_path )
        else:
            print(f"Error: Image file '{self.boom_image_path }' not found!")
            return
        
 # Create the Turtle object for the alien
        self.alien_t = Turtle()
        self.alien_t.shape(alien_image_path)
        self.alien_t.speed(5)
        self.alien_t.penup()
        self.alien_t.goto(posW,posH)
        self.alien_t.pendown()

    def get_position(self):
        """
        Return the current position of the alien.
        """
        return self.alien_t.position()

    def start (self):
        """
        Start the alien's movement based on the current game level.
        """
        # speed increases by 10% by level
        speed = int(cte.ALIEN_SPEED -( game.game_global.get_level() - 1)*cte.ALIEN_SPEED/10 )
        print(f"speed init : {speed}")
        self.move(cte.ALIEN_WIDTH ,cte.ALIEN_HEIGHT /5, speed )

    def move(self, step_x, step_y, speed):
        """
        Input : position (x,y) , speed
        Output: recursive on timer
        
        move the alien regarding level
        check if alien out of screen 

        """
        # return  if the object has been delete during the ontimer
        if not hasattr(self, 'alien_t'): 
            print ('move impossible no alien_t')
            return

        self.alien_t.penup()
        current_x, current_y = self.alien_t.position()
        level = game.game_global.get_level()
        if  level <= 3 :
            # if alien goes out of screen, inverse step_x
            if current_x + step_x > cte.SCREEN_WIDTH /2 or current_x + step_x < -cte.SCREEN_WIDTH /2 :
                step_x = -step_x

            current_x = current_x + step_x
            current_y = current_y - step_y
            self.alien_t.setx(current_x) 
            self.alien_t.sety(current_y) 

        elif level > 3 and level <= 6 :
            direction = random.randint(-1, 1) # value-1,0,1
            if current_x + step_x > cte.SCREEN_WIDTH /2 or current_x + step_x < -cte.SCREEN_WIDTH /2 :
                step_x = -step_x

            current_x = current_x + direction * step_x
            if current_x  > cte.SCREEN_WIDTH /2 :
                current_x  = cte.SCREEN_WIDTH /2 -10
            if current_x  < -cte.SCREEN_WIDTH /2 :
                current_x  = -cte.SCREEN_WIDTH /2+10
            current_y = current_y - step_y
            self.alien_t.setx(current_x) 
            self.alien_t.sety(current_y)    

            if random.randint(1, 100) > 98: # Bomb in 2%
                bomb = Bomb(  6 ,  current_x, current_y , self.screen) 
                bomb.move()

        
        elif level > 6  :
            direction = random.randint(-1, 1) # value-1,0,1
            if current_x + 2 * step_x > cte.SCREEN_WIDTH /2 or current_x + 2 * step_x < -cte.SCREEN_WIDTH /2 :
                step_x = -step_x

            current_x = current_x + direction * 2 * step_x
            if current_x  > cte.SCREEN_WIDTH /2 :
                current_x  = cte.SCREEN_WIDTH /2 -10
            if current_x  < -cte.SCREEN_WIDTH /2 :
                current_x  = -cte.SCREEN_WIDTH /2+10
            current_y = current_y - step_y
            self.alien_t.setx(current_x) 
            self.alien_t.sety(current_y)    

            if random.randint(1, 100) > 96 : # Bomb in 4%
                bomb = Bomb(  6 ,  current_x, current_y , self.screen) 
                bomb.move()

        self.alien_t.pendown()



        # check if alien out of screen or collision  TODO
        if current_y < - cte.SCREEN_HEIGHT/2 :
            self.move_possible = False
            game.game_global.end_game()

        if self.move_possible :
            # to increase the speed if the number of alien decrease
            if game.game_global.alien_fleet.get_nb_alien() != self.previous_nb_alien :
                speed = int(speed * 0.9)
                print(f"speed change : {speed}")
                self.previous_nb_alien -=1

            self.screen.ontimer(lambda: self.move(step_x,step_y,speed), speed)

    def display_crash(self):
        self.alien_t.shape(self.boom_image_path)
        self.screen.ontimer(self.delete_alien, 500) 


    def delete_alien(self):

        self.delete()
        if self in game.game_global.alien_fleet.fleet :
            game.game_global.alien_fleet.remove_alien(self)
        # game.game_global.alien_fleet.fleet.remove(self)

        # if alien fleet is empty, go to the next level
        if not game.game_global.alien_fleet.fleet :
            game.game_global.next_level()
            return
        
        

    def delete(self):
        # Memory management : need to del object in the fleet_list and the object itself
        #  
        if not hasattr(self, 'alien_t'): 
            print ('delete impossible no alien_t')
            return
        self.alien_t.hideturtle()
       
        del self.alien_t
        del self
        return