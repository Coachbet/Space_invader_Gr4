from turtle import Turtle
import os
import constante as cte
import game

class Bomb:
    def __init__(self, speed ,  posW, posH , screen):
        
        self.screen = screen

        bomb_image_path = os.path.join(cte.DIRECTORY_IMAGE, cte.IMAGE__BOMB_FILE)
        if os.path.exists(bomb_image_path ):
            screen.addshape(bomb_image_path )
        else:
            print(f"Error: Image file '{bomb_image_path }' not found!")
            return

        self.bomb_t = Turtle()
        # self.bomb_t.hideturtle()
        self.bomb_t.shape(bomb_image_path)
        self.bomb_t.speed(speed)
        self.bomb_t.penup()
        self.bomb_t.goto(posW,posH) 
        self.bomb_t.pendown()
        self.current_x = posW
        self.current_y = posH
        
        self.move_possible = True


    def move(self ):
        if not hasattr(self, 'bomb_t'): 
            print ('move impossible no bomb_t')
            return
        
        self.bomb_t.penup()
        x,y = self.bomb_t.position()
        y = y - cte.BOMB_HEIGHT
        self.bomb_t.sety(y)        

        self.bomb_t.pendown()
        
        # check if bomb out of screen or collision or destroy
        if y <  -cte.SCREEN_HEIGHT/2 :
            
            self.delete()
            return

        # check only if y in the lower quarter
        if y <  -cte.SCREEN_HEIGHT/4 and self.check_collision(x,y) :
            # ship explosion
            self.bomb_t.hideturtle()
            game.game_global.get_ship().display_crash()
            self.delete()
            return

        self.screen.ontimer(self.move, cte.BOMB_SPEED)


    def check_collision(self,x_bomb, y_bomb):
        """
            input position bomb
            output True / False
        """
        
        return game.game_global.get_ship().get_ship_contact(x_bomb, y_bomb)


    def delete(self):
        # Memory management 
        #  
        self.bomb_t.clear()
        del self.bomb_t
        del self
        return