
from turtle import Turtle

import constante as cte
import game

class Bullet:
    def __init__(self, size,  posW, posH , screen):
        
        self.screen = screen
        self.size = size
        self.bullet_t = Turtle()
        self.bullet_t.shape("arrow")
        self.bullet_t.hideturtle()
        self.bullet_t.speed(10)
        self.bullet_t.penup()
        self.bullet_t.goto(posW,posH) 
        self.bullet_t.pendown()
        self.current_x = posW
        self.current_y = posH
        self.bullet_t.pen(fillcolor="white", pencolor="red", pensize=3)
        self.move_possible = True

    def draw(self):
        self.bullet_t.clear()
        
        self.bullet_t.seth(90)
        
        self.bullet_t.forward(self.size)
        

    def move(self ):
        self.bullet_t.penup()
        x,y = self.bullet_t.position()
        y = y + cte.BULLET_HEIGHT
        self.bullet_t.sety(y)        

        self.bullet_t.pendown()
        
        # check if bullet out of screen or collision or destroy
        if y >  cte.SCREEN_HEIGHT/2 :
            self.move_possible = False
            self.delete()
            return

        alien = self.check_collision(x,y)
        if alien != None:
            self.move_possible = False
            # alien explosion
            
            alien.set_crash()
            game.game_global.set_score("add",1)
            game.game_global.display_score()
            self.delete()
            return

        if self.move_possible :
            self.draw()
            self.screen.ontimer(self.move, cte.BULLET_SPEED)


    def check_collision(self,x_bullet, y_bullet):
        """
            input position bullet
            output 

            parse list des blocs : later
            parse fleet of alien
                get coord
                check if contact, yes return alien oject

        """
        
        return game.game_global.alien_fleet.get_alien_contact(x_bullet, y_bullet)


    def delete(self):
        # Memory management 
        #  
        self.bullet_t.clear()
        del self.bullet_t
        del self
        return