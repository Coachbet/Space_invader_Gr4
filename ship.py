import os# Import os for file path operations
from turtle import Turtle # Import the Turtle class

import constante as cte # Import constants from constante.py
from bullet import Bullet# Import the Bullet class
import game# Import the game module


class Ship:# Class to manage the player's ship
    """
    class Ship

    Manage bullet count and score
    Only one instance used as a global variable
    """

    def __init__(self, posW, posH , screen): # Initialize Ship attributes
        """
        __init__
        Input : size, posW : start position, posH : start position, screen
        Output : none

        Initialize attribut and Turtle object iwth image
        """    
         

        self.ship_image_path = os.path.join(cte.DIRECTORY_IMAGE, cte.IMAGE__SHIP_FILE) # Path to the ship image
        if os.path.exists(self.ship_image_path ):# Check if the ship image file exists
            screen.addshape(self.ship_image_path )  # Add the ship image to the screen
        else:
            print(f"Error: Image file '{self.ship_image_path }' not found!") # Log error if file is missing
            return
            return
        
        self.boom_image_path = os.path.join(cte.DIRECTORY_IMAGE, cte.IMAGE__BOOM_FILE)# Path to the explosion image
        if os.path.exists(self.boom_image_path ):# Check if the explosion image file exists
            screen.addshape(self.boom_image_path )  # Add the explosion image to the screen
        else:
            print(f"Error: Image file '{self.boom_image_path }' not found!")# Log error if file is missing
            return
        
        self.ship_t = Turtle()# Create a Turtle object for the ship
        self.ship_t.shape(self.ship_image_path)# Set the ship's shape to the ship image
        # self.ship_t.hideturtle()
        self.ship_t.speed(5)# Set the ship's movement speed
        self.ship_t.penup()# Disable drawing while moving
        self.ship_t.goto(posW,posH) # Set the ship's initial position
        self.ship_t.pendown()# Enable drawing again
        self.current_x = posW# Track the current X position of the ship
        self.current_y = posH# Track the current Y position of the ship
        self.screen = screen# Reference to the screen object


        self.bullet_list = [] # List to manage bullets fired by the ship
        self.bullet_loader = 0 # Count of available bullets


    def set_bullet_loader(self,value): # Set the bullet loader count

        """
        set_bullet_loader
        Input : value
        Output : none

        Update attribut with value
        """   
        self.bullet_loader = value  # Update the bullet loader attribute
        return
    
    def get_bullet_loader(self):# Get the current bullet loader count
        """
        get_bullet_loader
        Input : none
        Output : bullet loader count

        return attribut 
        """   
        return self.bullet_loader # Return the bullet loader attribute

        

    def move(self,key ): # Move the ship based on the input key
        """
        move
        Input : key
        Output : none

        Move the turtle object ship depending on the key Left or Right
        """   
  

        if key == "Left" and self.current_x - cte.STEP_SHIP > - cte.SCREEN_WIDTH/2: # Move left if within bounds
            self.current_x=self.current_x - 2*cte.STEP_SHIP# Update the X position
            self.ship_t.setx(self.current_x)# Move the ship to the new X position
        elif key == "Right" and self.current_x + 6 * cte.STEP_SHIP < cte.SCREEN_WIDTH/2:# Move right if within bounds
            self.current_x=self.current_x + cte.STEP_SHIP # Update the X position
            self.ship_t.setx(self.current_x) # Move the ship to the new X position


        # print (self.ship_t.position())
        return

    def fire(self ):# Fire a bullet from the ship
        """
        fire
        Input : nonr
        Output : none

        on space
        check if the loader is not empty
        set up a new object bullet
        update the bullet loader count
        display the bullet loader count
        """   
  
        #  ammunition management

        if (self.bullet_loader) == 0 :# Check if there are bullets left
                game.game_global.display_bullet_count("no more", self.bullet_loader)# Notify no bullets left
                return


        bullet_id = Bullet( 10, self.ship_t.xcor() , self.current_y + cte.SHIP_HEIGHT , self.screen) # Create a bullet
        self.bullet_list.append (bullet_id)# Add the bullet to the list
        self.bullet_loader -= 1# Decrease the bullet count

        game.game_global.display_bullet_count("in progress", self.bullet_loader )# Display updated bullet count

        bullet_id.move() # Start the bullet's movement
        return
    
    def display_crash(self):# Display a crash animation for the ship
        
        self.ship_t.shape(self.boom_image_path) # Change the ship's shape to the explosion image
        self.screen.ontimer(game.game_global.end_game, 500) # Schedule the end game sequence



     
    def get_ship_contact(self, x_bomb , y_bomb): # Check if the ship is hit by a bomb
        
            
        if x_bomb < self.current_x + cte.SHIP_WIDTH / 2 and x_bomb > self.current_x - cte.SHIP_WIDTH /2 :# Check X collision
            if y_bomb < -cte.SCREEN_HEIGHT/2  + cte.SHIP_HEIGHT :  # Check Y collision
                print("contact ship")# Log the collision
                return True# Return collision detected


        return False# Return no collision

        
