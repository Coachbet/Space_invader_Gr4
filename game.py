from turtle import Turtle
import turtle
import time


import constante as cte
from alien import Alien_fleet

class Game :
    """
    class Game

    Manage bullet count and score
    Only one instance used as a global variable
    """
    def __init__(self):
        """
        __init__
        Input : none
        Output : none

        Initialize attribut and Turtle object
        """    
        self.level = 1
        self.score = 0
        self.game_time  = 0
        self.bullet_count = cte.MAX_BULLET_BY_LEVEL
        self.alien_fleet = None
        self.ship = None
        self.screen = 0
        self.game_msg_t = Turtle()
        self.game_msg_t.hideturtle()  
        self.game_level_t_t = Turtle()
        self.game_level_t_t.hideturtle()
        self.game_bullet_t = Turtle()
        self.game_bullet_t.shape("arrow")
        self.game_bullet_t.hideturtle()
        self.game_score = Turtle()
        self.game_score.shape("arrow")
        self.game_score.hideturtle()

    def add_screen (self,screen):
        """
        add_screen
        Input : screen
        Output : none

        Add screen as attribut
        """   
        self.screen = screen
        return
    
    def add_ship (self,ship):
        """
        add_screen
        Input : ship object
        Output : none

        Add screen as attribut
        """   
        self.ship = ship
        return
    
    def set_score(self,action, value):
        """
        set_score
        Input : action, value
        Output : none

        Update the score attribut
        action = add, update score with value
        action = reset, reset score to 0
        """   
        if action == "add":
            self.score += value
        elif action == "reset":
            self.score = 0

    def display_score(self):
        """
        display_score
        Input : none
        Output : none

        Display the score
        """   
    
        self.game_score.clear()
        self.game_score.penup()
        self.game_score.goto(230,380)
        self.game_score.pendown()
        self.game_score.color("white")
        texte = "Score : "+ str(self.score)
        self.game_score.write(texte, align="right", font=("Arial", 10, "normal"))
        return
    
    def get_level(self):
        """
        get_level
        Input : none
        Output : level

        """   

        return self.level 

    def set_level(self,action, value):
        """
        set_level
        Input : action, value
        Output : none

        Update the score attribut
        action = add, update score with value
        action = reset, reset score to 0
        """   
        if action == "add":
            self.level += value
        elif action == "reset":
            self.level = value

    def display_level(self):
        """
        display_level
        Input : none
        Output : none

        Display the level
        """   
    
        self.game_level_t_t.clear()
        self.game_level_t_t.penup()
        self.game_level_t_t.goto(160,380)
        self.game_level_t_t.pendown()
        self.game_level_t_t.color("white")
        texte = "Level : "+ str(self.level)
        self.game_level_t_t.write(texte, align="right", font=("Arial", 10, "normal"))
        return

    def display_bullet_count(self, action, value):
        """
        display_bullet_count
        Input : action, value
        Output : none

        Display the bullet count
        Displat value or message depending on action
        """   

        self.game_bullet_t.clear()
        self.game_bullet_t.penup()
        self.game_bullet_t.goto(350,380)
        self.game_bullet_t.pendown()
        self.game_bullet_t.color("orange")

        if action == "no more":
            texte = "No more bullet"
            self.game_bullet_t.write(texte, align="right", font=("Arial", 10, "normal"))
            
        elif action == "in progress":
            texte = "Bullet count : "+str(value)
            self.game_bullet_t.write(texte, align="right", font=("Arial", 10, "normal"))
            
        return    
    
    def display_msg(self,size,color,texte):
        self.game_msg_t.penup()
        self.game_msg_t.home()
        self.game_msg_t.pendown()
        self.game_msg_t.color(color)
        self.game_msg_t.write(texte, align="Center", font=("Arial", size, "bold"))

    def end_game(self):
    
        self.display_msg(30,"red","END GAME")
        # add score on another line just behind TODO

        return    

    def new_game(self):
        self.alien_fleet.fleet.clear()

        self.game_msg_t.clear()

        # initialize the level
        self.set_level("reset",1)

        self.display_level()

        # initialize the score
        self.set_score("reset",0)
        self.display_score()

        # Initialize the Ship and amunitions
        self.ship.set_bullet_loader(cte.MAX_BULLET_BY_LEVEL + cte.NB_BULLET_BY_LEVEL * (self.level-1))
        self.display_bullet_count("in progress", self.ship.get_bullet_loader())

        # initialize the Alien_fleet and start the game with 
        self.alien_fleet = Alien_fleet(40,  -380, 380, self.screen)
        self.alien_fleet.start()


    def hide_msg(self):
        self.game_msg_t.clear()

    def next_level(self):

        self.display_msg(20,"yellow","NEXT LEVEL")
        self.screen.ontimer(self.hide_msg, 1000) 
        

        self.set_level("add",1)
        self.display_level()

# Initialize  amunitions
        self.ship.set_bullet_loader(cte.MAX_BULLET_BY_LEVEL + cte.NB_BULLET_BY_LEVEL * (self.level-1))
        self.display_bullet_count("in progress", self.ship.get_bullet_loader())
        
        self.alien_fleet.fleet.clear()
        # initialize the Alien_fleet and start the game with 
        self.alien_fleet = Alien_fleet(40,  -380, 380, self.screen)
        self.alien_fleet.start()
        return
        
game_global = Game()