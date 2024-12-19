
from turtle import Turtle  # Import the Turtle class from the turtle module

import constante as cte  # Import constants from constante.py
import game # Import the game module

class Bullet:# Class representing a bullet
    def __init__(self, size,  posW, posH , screen):# Initialize Bullet attributes
        
        self.screen = screen# Screen object for rendering
        self.size = size# Size of the bullet
        self.bullet_t = Turtle() # Turtle object for the bullet
        self.bullet_t.shape("arrow") # Set the bullet's shape
        self.bullet_t.hideturtle()  # Hide the turtle initially
        self.bullet_t.speed(10)# Set the speed of the turtle
        self.bullet_t.penup()# Disable drawing while moving
        self.bullet_t.goto(posW,posH) # Set the initial position 
        self.bullet_t.pendown() # Enable drawing again
        self.current_x = posW# Track the current X position
        self.current_y = posH # Track the current Y position
        self.bullet_t.pen(fillcolor="white", pencolor="red", pensize=3) # Customize the pen
        self.move_possible = True# Flag to indicate if movement is allowed

    def draw(self):# Draw the bullet
        self.bullet_t.clear()# Clear any previous drawings
        
        self.bullet_t.seth(90)# Set the direction to upward
        
        self.bullet_t.forward(self.size)# Move forward by bullet size
        

    def move(self ):# Move the bullet
        self.bullet_t.penup()# Disable drawing while moving
        x,y = self.bullet_t.position()# Get the current position
        y = y + cte.BULLET_HEIGHT# Update the Y-coordinate by bullet height
        self.bullet_t.sety(y) # Move to the new position

        self.bullet_t.pendown()# Enable drawing again
        
        # check if bullet out of screen or collision or destroy
        if y >  cte.SCREEN_HEIGHT/2 :# Check if bullet is out of screen
            self.move_possible = False # Disable further movement
            self.delete() # Delete the bullet
            return

        alien = self.check_collision(x,y)# Check for collisions
        if alien != None:# If collision detected
            self.move_possible = False# Disable further movement
            # alien explosion
            
            alien.display_crash()# Trigger alien's crash animation
            game.game_global.set_score("add",1) # Increment score
            game.game_global.display_score() # Display updated score
            self.delete() # Delete the bullet
            return

        if self.move_possible :# If movement is still allowed
            self.draw()# Redraw the bullet
            self.screen.ontimer(self.move, cte.BULLET_SPEED)  # Schedule the next move


    def check_collision(self,x_bullet, y_bullet):# Check if bullet collides with an alien
        """
            input position bullet
            output 

            parse list des blocs : later
            parse fleet of alien
                get coord
                check if contact, yes return alien oject

        """
        
        return game.game_global.alien_fleet.get_alien_contact(x_bullet, y_bullet) # Delegate collision check


    def delete(self): # Delete the bullet object
        # Memory management 
        #  
        self.bullet_t.clear()# Clear the turtle's drawing
        del self.bullet_t # Delete the turtle object
        del self# Delete the bullet instance

        return