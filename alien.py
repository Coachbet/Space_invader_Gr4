import threading
from turtle import Turtle
import os

import constante as cte
import game

class Alien_fleet:
    def __init__(self, size, posW, posH, screen):
        self.screen = screen
        self.fleet = []
        self.posX_init = posW
        self.posY_init = posH
        

    def launch_tempo(self):
        return

    def start(self):
        for i in range (0,5):
            alien = Alien(self.posX_init + i*100 ,self.posY_init ,self.screen)
            self.fleet.append(alien)

            timer = threading.Timer(i, alien.start)
            timer.start()

        return

    def get_alien_contact(self , x_bullet, y_bullet):
        """
            input position bullet
            output 

            parse list des blocs : later
            parse fleet of alien
                get coord
                check if contact, yes return alien oject

        """
        
        for alien in self.fleet :
            x_alien, y_alien = alien.get_position()
            if x_bullet < x_alien + cte.ALIEN_WIDTH / 2 and x_bullet > x_alien - cte.ALIEN_WIDTH /2 :
                if y_bullet - cte.BULLET_HEIGHT > y_alien - cte.ALIEN_HEIGHT/2 : # and y_bullet + cte.BULLET_HEIGHT < y_alien -cte.BULLET_HEIGHT :
                    print("contact")
                    return (alien)

        return None
    
    def remove_alien (self, alien):
        self.fleet.remove(alien)
    
    def remove_fleet(self):
        for alien in self.fleet :
            alien.delete()
        self.fleet.clear()

    def remove (self, alien):
        self.fleet.remove(alien)
    
    def remove_fleet(self):
        for alien in self.fleet :
            alien.delete()
        self.fleet.clear()


class Alien:
    def __init__(self, posW, posH, screen):

        self.move_possible = True
        self.current_x = posW
        self.current_y = posH
        self.width = cte.ALIEN_WIDTH
        self.heigth = cte.ALIEN_HEIGHT # if later we want modify alien with new model and new file
        self.available = True
        self.screen = screen

        alien_image_path = os.path.join(cte.DIRECTORY_IMAGE, cte.IMAGE__ALIEN_FILE)
        if os.path.exists(alien_image_path ):
            screen.addshape(alien_image_path )
        else:
            print(f"Error: Image file '{alien_image_path }' not found!")
            return

        self.boom_image_path = os.path.join(cte.DIRECTORY_IMAGE, cte.IMAGE__BOOM_FILE)
        if os.path.exists(self.boom_image_path ):
            screen.addshape(self.boom_image_path )
        else:
            print(f"Error: Image file '{self.boom_image_path }' not found!")
            return

        self.alien_t = Turtle()
        self.alien_t.shape(alien_image_path)
        self.alien_t.speed(5)
        self.alien_t.penup()
        self.alien_t.goto(posW,posH)
        self.alien_t.pendown()

    def get_position(self):
        return self.alien_t.position()

    def start (self):
        speed = int(cte.ALIEN_SPEED / game.game_global.get_level())
        self.move(cte.ALIEN_WIDTH ,cte.ALIEN_HEIGHT /5, speed )

    def move(self, step_x, step_y, speed):

        # if not self : return # if the object has been delete during the ontimer
        if not hasattr(self, 'alien_t'): 
            print ('move impossible no alien_t')
            return

        if not self.available : return # if n move launch by timer : security

     
        # print (self.alien_t.position())
        self.alien_t.penup()
        current_x, current_y = self.alien_t.position()
        # if alien goes out of screen, inverse step_x
        if current_x + step_x > cte.SCREEN_WIDTH /2 or current_x + step_x < -cte.SCREEN_WIDTH /2 :
            step_x = -step_x

        current_x = current_x + step_x
        current_y = current_y - step_y
        self.alien_t.setx(current_x) 
        self.alien_t.sety(current_y) 
        self.alien_t.pendown()



        # check if alien out of screen or collision  TODO
        if current_y < - cte.SCREEN_HEIGHT/2 :
            self.move_possible = False
            game.game_global.end_game()


        if self.move_possible :
            self.screen.ontimer(lambda: self.move(step_x,step_y,speed), speed)

    def display_crash(self):
        self.alien_t.shape(self.boom_image_path)
        self.screen.ontimer(self.set_crash, 500) 


    def set_crash(self):


        self.available = False
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