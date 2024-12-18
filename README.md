# Space_invader_Gr4
Computional thinking project: Space invader 

Louis:

● space_invader_gr4/version_1.0

● supervised everyone else’s work

● Organised github

● algorithm modification Kenza:

● space_invader_gr4/version_1.1

● README

● algorithm modification

● pseudocode

Neel:

● space_invader_gr4/version_1.3

● complexity of the last version of the code

● algorithm modification

● pseudocode

Pollux:

● space_invader_gr4/version_1.5

● comment every line of code

● modify the last version of main with comments

● algorithm modification

● optimisation

Eliot:

● space_invader_gr4/version_1.4

● demonstration video of the game

● algorithm modification

● pseudocode

Alix:

● space_invader_gr4/version_1.2

● README

● algorithm modification

● optimisation

● pseudocode



How to play ?
The objective is to destroy all the alien ships to progress to the next level while avoiding their attacks. Use limited bullets strategically to achieve the highest score.
The game involves controlling a ship to defend against waves of aliens by shooting them down, avoiding being hit, and achieving the highest score. The aliens can drop bombs, the ship has to avoid them, if it is hitten, it dies and the player loses. Additionally, if the aliens arrive on the ground, the player loses. Points are awarded for destroying alien ships. Aim for the highest score.

The game features:
Keyboard controls for movement and actions.
Multiple levels of increasing difficulty.
Real-time updates for smooth gameplay.
Control with keyboard:
Arrow Keys:
Left: Move the ship left.
Right: Move the ship right.
Space Bar: Fire bullets.
H: Display help information.
Escape: Clear the help screen.
N: Start a new game.


1) Space_invaders.py
main(): the main function is the main entry point for the game. It initializes the game window and starts the main game loop by creating a Game instance and calling its run() method.

Initialize the Game Environment:
-Sets up the game window (screen size, title).
-Initializes necessary libraries like pygame.
-Sets the game’s frame rate (FPS).

Create Game Objects:
-Initializes the player’s ship, aliens, and bullets.
-Loads any necessary assets (images, sounds).

Game Loop:
-Runs a continuous loop to keep the game active until the player quits or the game ends.
-Handles user input (keyboard events like moving left, right, or shooting).
-Updates the state of game objects (player’s ship, bullets, aliens).
-Draws all game elements on the screen.
-Ensures the screen updates at a consistent frame rate.

Handle Events:
-Checks for events like quitting the game (pygame.QUIT) or key presses (moving the ship or shooting bullets).

Collision Detection:
-Checks for collisions between bullets and aliens.
-Updates the game state if a collision occurs (e.g., removing an alien or increasing the score).

Game Over Conditions:
-Determines if the game is over based on conditions like:
-Aliens reaching the bottom of the screen.
-The player’s ship being hit.
-Displays a game-over message and possibly restarts the game or exits.

2) game.py
Purpose: Manages the core game mechanics and overall flow.
Class Game:
__init__(self): Initializes the game by creating the ship, aliens, and a list of bullets.
run(self): The main game loop that handles events, updates game elements, and redraws the screen.
check_collisions(self): Checks for collisions between bullets and aliens.
draw(self, screen): Draws all game elements (ship, aliens, bullets) on the screen.

Game States: Handles different game states such as "playing," "game over," and "victory."

3) ship.py
Purpose: Handles the player's spaceship, including movement and drawing.
Class Ship:
__init__(self): Initializes the ship at its starting position.
move(self, direction): Updates the ship’s position based on the given direction (LEFT or RIGHT).
draw(self, screen): Draws the ship on the screen.
shoot(self): Creates and returns a Bullet object to represent firing a shot.
This class allows control over the ship’s movement and shooting functionality.

4) alien.py
Purpose:Defines the behavior of the enemy aliens.
Class Alien:
__init__(self, x, y): Initializes an alien at position (x, y).
move(self): Updates the alien’s position based on its speed (ALIEN_SPEED).
draw(self, screen): Draws the alien on the screen.

5) bullet.py
Purpose:Manages the bullets fired by the player.
Class Bullet:
__init__(self, x, y): Initializes a bullet at position (x, y).
move(self): Updates the bullet’s position based on its speed (BULLET_SPEED).
draw(self, screen): Draws the bullet on the screen.

6) constante.py
Purpose: Contains game constants and configurations.
Example of Constants:
SCREEN_WIDTH: The width of the game screen.
SCREEN_HEIGHT: The height of the game screen.
FPS: The number of frames per second.
BULLET_SPEED: The speed of the bullets.
ALIEN_SPEED: The speed of the aliens.

7. Files:
space_ship.gif: Image file for the player's spaceship.
alliens.gif / alien.gif: Image files for enemy aliens.

Heap Sort Algorithm and Its Role in Space Invader
In our Space Invader game, Heap Sort is used to sort the levels reached by the player. This ensures that the levels are always shown in an organized and clear way in real time during the game.
The levels reached are organized into a pyramid structure where the highest level is always at the top.
Sorting the Levels: The highest level is repeatedly extracted and placed in its final position. After each extraction, the heap is reorganized to maintain its structure.
Complexity of Heap Sort
Base case : Constructing the Max-Heap from an unsorted list has a time complexity of O(n).
Average case and worst case (Sorting the elements): Repeatedly reorganizing the heap and extracting the largest element takes O(log(n)) per element. For a list of size n, the total time complexity is O(n*log n).
Worst case: Like the average case, the worst-case time complexity is also O(n*log n) because the algorithm always processes all elements systematically.
Space complexity: Heap Sort is in-place, meaning it requires O(1) extra space





