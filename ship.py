import os
from turtle import Turtle

import constante as cte
from bullet import Bullet
import game


class Ship:
    """
    class Ship

    Manage bullet count and score
    Only one instance used as a global variable
    """

    def __init__(self, posW, posH , screen):
        """
        __init__
        Input : size, posW : start position, posH : start position, screen
        Output : none

        Initialize attribut and Turtle object iwth image
        """    
         
        self.ship_image_path = os.path.join(cte.DIRECTORY_IMAGE, cte.IMAGE__SHIP_FILE)
        if os.path.exists(self.ship_image_path ):
            screen.addshape(self.ship_image_path )
        else:
            print(f"Error: Image file '{self.ship_image_path }' not found!")
            return
        
        self.boom_image_path = os.path.join(cte.DIRECTORY_IMAGE, cte.IMAGE__BOOM_FILE)
        if os.path.exists(self.boom_image_path ):
            screen.addshape(self.boom_image_path )
        else:
            print(f"Error: Image file '{self.boom_image_path }' not found!")
            return
        
        self.ship_t = Turtle()
        self.ship_t.shape(self.ship_image_path)
        # self.ship_t.hideturtle()
        self.ship_t.speed(5)
        self.ship_t.penup()
        self.ship_t.goto(posW,posH) 
        self.ship_t.pendown()
        self.current_x = posW
        self.current_y = posH
        self.screen = screen

        self.bullet_list = [] # pas sur que necessaire
        self.bullet_loader = 0

    def set_bullet_loader(self,value):
        """
        set_bullet_loader
        Input : value
        Output : none

        Update attribut with value
        """   
        self.bullet_loader = value
        return
    
    def get_bullet_loader(self):
        """
        get_bullet_loader
        Input : none
        Output : bullet loader count

        return attribut 
        """   
        return self.bullet_loader 
        

    def move(self,key ):
        """
        move
        Input : key
        Output : none

        Move the turtle object ship depending on the key Left or Right
        """   
  
        if key == "Left" and self.current_x - cte.STEP_SHIP > - cte.SCREEN_WIDTH/2:
            self.current_x=self.current_x - 2*cte.STEP_SHIP
            self.ship_t.setx(self.current_x)
        elif key == "Right" and self.current_x + 6 * cte.STEP_SHIP < cte.SCREEN_WIDTH/2:
            self.current_x=self.current_x + cte.STEP_SHIP
            self.ship_t.setx(self.current_x)

        # print (self.ship_t.position())
        return

    def fire(self ):
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

        if (self.bullet_loader) == 0 :
                game.game_global.display_bullet_count("no more", self.bullet_loader)
                return

        bullet_id = Bullet( 10, self.ship_t.xcor() , self.current_y + cte.SHIP_HEIGHT , self.screen)
        self.bullet_list.append (bullet_id) # pas sur que necessaire
        self.bullet_loader -= 1

        game.game_global.display_bullet_count("in progress", self.bullet_loader )

        bullet_id.move()
        return
    
    def display_crash(self):
        
        self.ship_t.shape(self.boom_image_path)
        self.screen.ontimer(game.game_global.end_game, 500) 


     
    def get_ship_contact(self, x_bomb , y_bomb):
        
            
        if x_bomb < self.current_x + cte.SHIP_WIDTH / 2 and x_bomb > self.current_x - cte.SHIP_WIDTH /2 :
            if y_bomb < -cte.SCREEN_HEIGHT/2  + cte.SHIP_HEIGHT : 
                print("contact ship")
                return True

        return False
