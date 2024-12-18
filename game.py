from turtle import Turtle
import turtle

import datetime
import heapq



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
        self.game_in_progress = True

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
        self.game_score_t = Turtle()
        self.game_score_t.shape("arrow")
        self.game_score_t.hideturtle()
        self.game_help_t = Turtle()
        self.game_help_t.hideturtle()  



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
    
        self.game_score_t.clear()
        self.game_score_t.penup()
        self.game_score_t.goto(230,380)
        self.game_score_t.pendown()
        self.game_score_t.color("white")
        texte = "Score : "+ str(self.score)
        self.game_score_t.write(texte, align="right", font=("Arial", 10, "normal"))
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
    

    def display_msg(self,  size, color,texte, offset_y):
        self.game_msg_t.penup()
        self.game_msg_t.goto(0, cte.SCREEN_HEIGHT/8 - offset_y)
        self.game_msg_t.pendown()
        self.game_msg_t.color(color)
        self.game_msg_t.write(texte, align="Center", font=("Arial", size, "bold"))
        

    def hide_msg(self):
        self.game_msg_t.clear()
     

    def new_game(self,status):
        self.game_in_progress = True

        if self.alien_fleet :  
            self.alien_fleet.remove_fleet()


        self.game_msg_t.clear()

        # initialize the level

        self.set_level("reset",5) # 5 instead of 1 for testing


        self.set_level("reset",5) # 5 instead of 1 for testing


        self.display_level()

        # initialize the score
        self.set_score("reset",0)
        self.display_score()

        # Initialize the Ship and amunitions
        self.ship.set_bullet_loader(cte.MAX_BULLET_BY_LEVEL + cte.NB_BULLET_BY_LEVEL * (self.level-1))
        self.display_bullet_count("in progress", self.ship.get_bullet_loader())
        
        if status != "init" :
        # initialize a new Alien_fleet and start the game with 
            self.alien_fleet = Alien_fleet(40,  -380, 380, self.screen)
            self.alien_fleet.start()


    

    def next_level(self):


        self.display_msg(20, "yellow","NEXT LEVEL",0)
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

    
    def end_game(self):
        # allow to execute only once per game the method 
        if not self.game_in_progress : return
        self.game_in_progress = False

        if self.alien_fleet :  
            self.alien_fleet.remove_fleet()

        self.display_msg(30,"red","END GAME",0)
        
        # store score
        player_name = self.screen.textinput("Player Name", "Please enter your name:")
        self.screen.listen() # reactivate the listener because if not yhe onkeypressed doesn't work
       
        if player_name != None :
            self.record_score(player_name, self.score, self.level-1)

        # get 5 top scores and display them
        top_scores = self.get_top_scores ( 5)
        i=1
        for score in top_scores:
            display_string = f"{str(i)} : {score[1].ljust(15)}\t: {score[0]}\t (Date: {score[2]}) Level : {score[3]}"
            self.display_msg(10,"white", display_string, i*20)
            i+=1

        return   
    

    def get_top_scores(self, top_n):
        try:
            # Lire le fichier et extraire les données
            scores = []
            with open(cte.SCORE_FILE, "r") as file:
                for line in file:
                    # Analyse de la ligne pour extraire la date, le nom et le score
                    parts = line.strip().split(", ")
                    if len(parts) == 4:
                        date, name, score, level = parts
                        scores.append((int(score), name, date, level))
            

            # Use heapq to get the top_n top scores
            top_scores = heapq.nlargest(top_n, scores)

            return top_scores
        
        except Exception as e:
            print(f"An error occurred: {e}")

    def record_score(self, player, score, level):
        
        current_date = datetime.datetime.now().strftime("%d/%m/%Y")

        file_name = cte.SCORE_FILE
    
        content = f"{current_date}, {player}, {score}, {level}\n"

        with open(file_name, "a") as file:
            file.write(content)

        
        return 

    
    def display_help(self):
        self.hide_msg() # if help asked and the score is displayed

        self.game_help_t.penup()
        self.game_help_t.color("white")
        offset_y = 20
        
        self.game_help_t.goto(0, cte.SCREEN_HEIGHT/8 - offset_y)
        texte = "first line "
        self.game_help_t.write(texte, align="Center", font=("Arial", 10, "bold"))
        
        self.game_help_t.goto(0, cte.SCREEN_HEIGHT/8 - 2*offset_y)
        texte = "seconf line "
        self.game_help_t.write(texte, align="Center", font=("Arial", 10, "bold"))
        
        self.game_help_t.goto(0, cte.SCREEN_HEIGHT/8 - 3*offset_y)
        texte = "third line"
        self.game_help_t.write(texte, align="Center", font=("Arial", 10, "bold"))

        self.game_help_t.pendown()

        return
    
    def clear_help(self):
        self.game_help_t.clear()
        return
    
        

        
game_global = Game()