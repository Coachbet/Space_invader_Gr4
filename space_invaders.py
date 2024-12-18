# from turtle import *
import constante as cte

from turtle import Turtle
from turtle import Screen

# import turtle

from ship import Ship
from alien import Alien_fleet

import game

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

level_game = 1


def create_screen():
    """
    create_screen
    Input : nono
    Output : none

    Define main characteristic of the screen
    """
    # screen = turtle.Screen()
    screen = Screen()
    screen.title("Space Invader _ Grp 3")
    screen.bgcolor("black")
    screen.setup (width=cte.SCREEN_WIDTH, height=cte.SCREEN_HEIGHT)
    screen.tracer(0)
    return screen

def update(screen):
    """
    update
    Input : screen object
    Output : none

    Update the screen at regular intervals depending on FPS definie in constante.py
    """
    screen.update()
    screen.ontimer(lambda: update(screen), int(1000 / cte.FPS)) # lambda== a function

def space_invaders():
    """
    Main program
    Input : none
    Output : none

    Initialize main object : Game, Ship,  Alien_fleet
    Define user action with the keyboard

    """

    screen = create_screen()
    game.game_global.add_screen(screen)

    ship = Ship( -cte.SCREEN_WIDTH/2 + 20 ,- cte.SCREEN_HEIGHT/2 + 40 , screen)
    game.game_global.add_ship(ship)
    game.game_global.new_game("init")
    game.game_global.alien_fleet = Alien_fleet(40,  -380, 380, screen)
    game.game_global.alien_fleet.start()


    # define user action with keyboard
    screen.listen()
    screen.onkeypress(lambda: game.game_global.new_game (""), "n") 
    screen.onkeypress(lambda: game.game_global.new_game (""), "N")
    screen.onkeypress(lambda: ship.move("Left"),"Left") 
    screen.onkeypress(lambda: ship.move("Right"),"Right") 
    screen.onkeypress(ship.fire, "space") 

    update(screen)  
    screen.mainloop()

    return

"""
    # initialize the level
    game.game_global.set_level("reset",5)
    game.game_global.display_level()

    # initialize the score
    game.game_global.set_score("reset",0)
    game.game_global.display_score()

    # Initialize the Ship and amunitions
    ship = Ship( -cte.SCREEN_WIDTH/2 + 20 ,- cte.SCREEN_HEIGHT/2 + 40 , screen)
    game.game_global.add_ship(ship)
    ship.set_bullet_loader(cte.MAX_BULLET_BY_LEVEL + cte.NB_BULLET_BY_LEVEL * (game.game_global.level-1))
    game.game_global.display_bullet_count("in progress", ship.get_bullet_loader())

    # initialize the Alien_fleet and start the game with 
    game.game_global.alien_fleet = Alien_fleet(40,  -380, 380, screen)
    game.game_global.alien_fleet.start()
"""

space_invaders()






