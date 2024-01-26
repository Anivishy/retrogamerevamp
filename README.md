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

&nbsp;&nbsp;&nbsp;&nbsp; The program is divided into 3 main components that the user interacts with, **homescreen introlevel and mazegen**, we decided to do this in part to make it easier to divide the work, but also to make it easier to combine the elements of the game in the end.


### **Homescreen:**

&nbsp;&nbsp;&nbsp;&nbsp;The homescreen is the first interaction that the user has with our game. Here, the user has options to view instructions, adjust settings, and start the game. We wanted to ensure that the home screen was themed around the design of the game to ensure a coherent and logical transition between this screen and the actual game. We also structured our game in clear and defined classes, developing centralized files which can be easily called into our homescreen file, allowing for seperate development of each aspect of our game, while providing an outlet for easy integration when bringing the whole game together. 

### **Introlevel:**

&nbsp;&nbsp;&nbsp;&nbsp;The introlevel file mostly acts as a standalone game to pay tribute to the classic game of Pacman. We utilized a lot of inheritance within this file, in order to create distinct ghost and pacman objects that could still easily interact with each other. Additionally, we made it so that the whole file can be encapsalated in a single class **run()** which allows for the file to be quickly accessed by homescreen. To transition from this file to the main game we call the mazegen class after the user defeats the introlevel and the end of level animation finishes playing.


### **Mazegen:**

&nbsp;&nbsp;&nbsp;&nbsp;The mazegen file serves as the central collection and implementation of many classes that make our main game. This is where our main game loop is run, where movements and key presses are tracked, interactions between the player and game objects are handled and where calls to helper classes are managed. In order to ensure a clear and easy to manage game streucutre, we seperated each game element or feature into its own class or collection. Furthermore, we ensured that elements and features that were logically connected to eachother were developed together in their own class, making the integration into the central mazegen file much easier. 

  - **Health:** The health file contains code focused around genertaing the palyer's health and sheild bar, which are grouped together due to their similar nature and their interaction with eachother. The class handles everything to do with these values, including calculations for regeneration, and tracking both values. There are also helper functions to take care of healing and taking damage, which can simply be called within the game loop in the mazegen file whenever specific interactions occour. This makes handling damage and healing much easier and consice.

  - **Pelletsandammo:** The pellets and ammo file contains all the code pertaining to score tracking, when a player picks up pellets, as well as handling ammo, which is gained for every 5 pellets that the player picks up. The display and UI aspect for both of these elements is also taken care of in this file. The file also contians helper methods which can be called in the main game loop to increment and decrement the player's score and ammo with specific interactions, such as when the players shoots or when the player collects a pellet. 

  - **Mousetargettracker:** The mouse target tracker is simply a file which handles the crossair that player usues to aim their shots in the game. This file was created for the purpose of keeping the main game loop clean and organized. the file take care of loading in and re-rendering the crossair as the user moves their mouse pointer, only requiring a call to the class' draw function to acheive this

  - **UpdatedShooting:** This is the third itteration of the shooting logic for the player. This file consists of functions to calculate and render the bullets shot by the player. Each bullet is created as its own object, with a x and y velocity calculated based on the angled between the player's current coordinates and the coordinates of the player's mouse (where the crossair is located.) The bullet object is called and created in the main game loop everytime the player shoots, where these objects are added to a list. This file also contains a funcction to update and re-render the bullet as it moves, which is once again called on every bullet object in the list of current bullets in the main game loop. 

  - **WallGeneration:** 

### **Diagram:**

![architecture](https://github.com/Anivishy/retrogamerevamp/assets/90056323/d812cdce-1640-4c97-bfd0-15737a899a26)


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
### Overall Process:
Overall, the process of writing this game went smoothly. Due to the task tracker, we all had clarity on our responsibilities, what others are currently working on, and what items were pending. 
This eliminated any duplication of work, or confusion about what to work on. 

We did not have any significant issues with GitHub or syncing code, mainly because we each focused on a different portion of the code. 
This allowed all of us to keep our code up to date. 

With a clear idea of what needed to be worked on, and well-managed code and tasks, we were able to make effective use of class time, which is why we were able to get the key aspects of our game done within the given time. 

Finally, throughout the project our group had a consensus on what we wanted to create, and how to go about it. 
This was essential in that it allowed us to move forward with our project, without conflicting ideas/functions in different parts of the game. 

### Communication: 
Throughout our project, our main source of communication – our high point - was in our standups. During each standup, we shared what we had done since our last meeting, our plan for the day, and any other significant information. 
This allowed everyone to stay updated on what is currently being worked on, and what changes have been made, throughout the project. 

Outside of this, we asked questions of one another periodically, whenever we required help or found something important to update others on. 
This allowed us to take other’s input into account and incorporate details to accommodate their code. 

One low point in terms of communication was that, when encountering challenges, we had a tendency to resolve it on our own, rather than asking others if they know of a solution. 
In the future, we may be more intentional in asking others for help when stuck, as asking for help from others who may have a solution allows for a quicker resolution of issues. 

### Surprises: 

### Takeaways:
Throughout our project, we learned a few things, some of which we can improve from changing, and others we plan to continue with. 

Next time, we may try to improve on our timeline, as we orignially had goals to create a final boss, but ended up running out of time to do this. 
To avoid this, we could try having an earlier deadline to have a fully functioning basic game, and then add more details from there, rather than working on each section independently and combining them at the end. 

Something we plan to continue is task tracking. By using this, we were able to see what others were working on, preventing duplication of work, and we knew what tasks were pending. These allowed us to work more efficiently.

Finally, by using standups throughout our project, we were able to ensure everyone was on the same page about what others are working on, and what needed to be done for the day. By continuing to use this, we will produce higher quality work through discussion to refine ideas, and efficiency through clarity on tasks. 
