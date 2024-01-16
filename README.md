# retrogamerevamp

## **Overview**

&nbsp;&nbsp;&nbsp;&nbsp;Our game is based off of the 1980 arcade game Pacman. The twist we added to the game was making the world procedurally generated with bosses scattered throughout, rather than the classic level-based system of the old Pacman game.

&nbsp;&nbsp;&nbsp;&nbsp;We decided to divide our game into 3 main components, a home screen, an intro level, and the main game. We started off with a home screen in order to provide one place for users to learn how to play the game, adjust settings, and begin the game. 

&nbsp;&nbsp;&nbsp;&nbsp;We decided to make the intro level separate from the main game, due to their vast differences. The main game is the procedurally generated maze, far different than anything previously seen in a Pacman game. Whereas the intro level is a homage to the first level of the 1980 game. For the intro level we tried to replicate the exact movements and graphics seen in the first game allowing users to experience the nostalgia of the old game, before being transported to a new world of Pacman.

&nbsp;&nbsp;&nbsp;&nbsp;In the main game users can experience 4 distinct biomes with unique ghosts and boss fights available in each, and since the maze is procedurally generated, no two playthroughs will ever quite be the same.

### **Running the Game:**

To run the game first download the following libraries.

-	PyAutoGUI - `pip install pyautogui`
  
-	PyGame – `pip install pygame`
  
After downloading the appropriate libraries to run the game run the file `homescreen.py`
Upon running this you will be presented a screen including instructions, settings and a button to begin the game

## Architecture

&nbsp;&nbsp;&nbsp;&nbsp; The program is divided into 3 main components that the user interacts with, **homescreen introlevel and mazegen**, we decided to do this in part to make it easier to divide the work, 

## **User Experience** 

Overall, the game is meant to provide a fresh spin on a classic game, the combination of nostalgia and unique gameplay is what we hope would attract users to the game initially. 

### **First Time User:** 

&nbsp;&nbsp;&nbsp;&nbsp;For a first-time user when they enter the game, they are brought to a loading screen with many different options, we would hope that at this point they would first click on the instructions tab which should be one of the first things they see on the screen, as well as settings, begin and quit. The controls for the game are relatively simple for the first level, so even if they do not check the instructions, they should be able to complete the first level relatively easily. 

&nbsp;&nbsp;&nbsp;&nbsp;After checking the instructions and adjusting any settings needed (volume, screen size, etc.) the user would then begin the first level. The first level is a clone of the original Pacman game, providing a bit of nostalgia for users who played the original game, and even if they did not play the original Pacman, the simplicity of this level provides a smooth introduction for a beginner. The first level should take users a few tries at most, with any failures likely coming due to a learning curve adapting to the ghosts. 

&nbsp;&nbsp;&nbsp;&nbsp;After completing the first level users are then transported to the main game and the much larger world it contains. This could be overwhelming for some users. To alleviate this the world is divided into 4 clear sections, each with a unique theme, this allows users to only need to focus on specific achievable objectives (beating the boss) in each quadrant. This part of the game relies less on nostalgia and more on a sense of adventure to entertain the user. 

&nbsp;&nbsp;&nbsp;&nbsp;In total the game should not take any new player an excessively long time to complete, but it should provide a challenging and rewarding experience, and since the game generates a new map for every playthrough users would never have the same experience twice, encouraging them to return. 

### **Returning User:** 

&nbsp;&nbsp;&nbsp;&nbsp;For a returning user upon loading the game it would be expected that they would either go straight to the first level or spend a brief moment adjusting their settings. The first level should be very easy for a returning user, having now had time to practice with the timing and patterns of the ghosts they should have no trouble navigating the first level in 1-2 attempts. 

&nbsp;&nbsp;&nbsp;&nbsp;Upon completing the intro level, they will once again be transported to the main game, but the map they receive this playthrough will likely be far different than their previous games. The user should have no trouble with the movement mechanics, but with the new world to explore it will likely take them some time to navigate each quadrant of the maze successfully. 

&nbsp;&nbsp;&nbsp;&nbsp;The boss fights in each section of the maze and should still prevent a challenge to the user, due to the boss’s strong tracking abilities, allowing a rewarding feeling for the user upon victory. Similar to a new user, the whole game should not take an excessively long time for the user to complete, allowing returning users to have a rewarding potentially nostalgic experience that will hopefully have them continuing to return. 

## Retrospective
