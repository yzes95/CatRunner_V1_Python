# Cat Hunt - An Adventure in Pygame
# Description:
Cat Hunt is an adventurous Python game crafted with the Pygame library. It immerses players in an exhilarating journey where they assume control of a character on a mission to hunt down enemies and gather bonuses. Key features include:

    1-Start Screen: Upon initiation, players are welcomed by a start screen, prompting them to input their username and commence their gaming experience.

    2-Gameplay: Players maneuver a character through a diverse array of obstacles, enemies, and bonuses, adding layers of excitement and challenge to     their quest.

    3-Encounter Enemy Tigers: Throughout the game, players confront enemy tigers, presenting them with the choice to evade or engage in combat.

    4-Flying Grounds: Certain sections of the game introduce flying grounds, providing players with an additional element of challenge as they leap and   navigate through the environment.

    5-Score Boosts: Bonus items sporadically appear, granting players valuable score boosts upon collection.

    6-Heart Indicator: A heart indicator displays the remaining lives of players, serving as a crucial gauge of survival amidst the game's perils.

    7-Immersive Background Music: Engage your senses with immersive background music that enriches the gaming experience, enhancing immersion and     enjoyment.

    8-Game Over Screen: Upon depletion of lives, the game over screen emerges, affording players the option to either restart their adventure or  gracefully exit the game.

As for how to Play,Run the Python script project.py then enter your username on the start screen and use the arrow keys to control the character (Up Arrow for now) and navigate through obstacles, defeat enemies, and collect bonuses to increase your score.Moreover,avoid collisions with enemies to prevent losing lives.Hence,when you run out of lives, the game over screen will appear. You can choose to restart or quit the game.

More into the project content , the project is divided into 3 main files which are the Main.py , Player_Enemy.py and I_O_display.py ,so lets clear them starting with main.py which include several functions beside the main fnc which will be discussed soon , so the main fnc is where the super loop/great loop which keep the game running exist besided the loop it starts with initilaizing pygame then defining the clock , display surface where our game will be displayed on it unlike regular surface that represent each object to be displayed on the main surface which is game screen which is display surface as mentioned .

Moreover,we start by assiging objects and groups for each game element we have or that does need to have a class more of that will be mentioned when we discuss the other files since those classes are improted from those files additonally some flags are defined as well which were used to control some code patterns along the way so some snippets of the code will be ddodged until a flag triggers ,also we created userevents where we summona certain objects at a desired interval while the game is running which was a 1st kind of exp to me to have used the random class in creating somthing in a game experinceing it as a player when i play a different game .Inside the super loop we 1st check for events through event loop which was a common thing to have among users of pygame thats as far as i knew from the guides i read/ watched where in this loop we check for custome events we created beside other events as user pressing on keys and mouse .

Then there is a snipped of code that startes after a flag named game_SF is equal to true that flag is equal to true when the user is finished form entering his name and clicking the start button once the suer is finished with thise 2 process it enter this section of code where it check for another flag called frozen where it get trigger if there is a collision between player char and the enemy avatar else the game cont. where enemy ,player,bonuses chars all get drawn beside the floating floors then followed by several collisions checks that one of them trigger frozen and others trigger other factors like score increase of collided with a certain object or heart increase depend on which object you collide with.

Somthing to mention that frozen section of code start with initilizing the game tracks and removing the intro tracks and since we mentioned we use some flags to control certain code snippets thats here where one of them is sued to itnialzie game track for once then get around it while the game is running .

Furthermore,after we finish this previouse section of code what if the game didnt start or what if there was a collision thats where the second part of code comes ,if there is a collions frozen get trigger escaping to another part of code where it freez the game as it is and only the collision between the player and the enemy is animted well the other objects like bonus and score booster should keep movig but it caused several problem to my game when i controlled it so i avoided it for now .

Then after this code snippet there is a part where if the game didnt start then i am either in after game sence or in game intro sence where for before game start there are 2 stages where one of them start with entering the player name then press keybad enter button to enter second screen where he use thge mouse to select the start button

As for the after you lose your chances in the game , the end game display is show where it show your last score and 2 options where either to restart the game or quit not to mention that this scrreen can be accesed anytime during the game if u pressed esc button.

Now we go to the functions defined and used in this file which are [New_User,Get_User,Update_User,text_fnc,Score_f,Collision_Enemy_T_check,Collision_Enemy_T_ressult,print_const_text] .SO starting with New_User it is a fnc where it allow the user to store its name in an external csv file while checking that this new of a user does not existed before so it cant ave multiple users of same name, Get_User gets user data  and Update_User updates user data very simple ones .While for text_fnc it is a fnc that is responsible for displaying and editing and controling all text objects in the project it control the fonts, size and location and color, as for the print_const_text it is used in the part where the gameover screen is displayed and this fnc is made to avoide repeating several code lines many time so i added them ina fnc .

Moreover,Collision_Enemy_T_check it is a fnc which is used to check for the collision between the user and enemy which return several values most imp of them is frozen and x_collide and y_clollide which are the coordinates of the collision between the objects and those coordinates used to determine where we draw our fight cloud  which resemmble the fight between 2 chars as in animation,hence to apply this animations and use those coodrinates we use the fnc Collision_Enemy_T_result.

Thats almost all for the main file, hope i explained as much as you might need to get general idea of how the project works and how it is coded as for the next section i will just provide general ideas of the content of the other files since both of them are classes for the objects used int he main file .

Player_Enemy.py is a file that defines several classes related to game entities using the Pygame library. Let's break down each class:

    Player: This class represents the player character in the game. It loads player images, manages player movement, handles jumping, animation, and    updates player state.

    Enemy_T: This class represents a type of enemy in the game. It loads enemy images, handles enemy animation, and updates enemy state.

    cloud: This class represents clouds in the game. It loads cloud images, handles cloud animation, and updates cloud state.

    heart_D: This class represents the player's heart status. It loads heart images, manages heart animation based on the number of remaining hearts,   and updates heart state.

    Bonus_F: This class represents a type of bonus in the game. It loads bonus images, handles bonus animation, and updates bonus state.

    Sparkle_F: This class represents a type of sparkle effect in the game. It loads sparkle images, handles sparkle animation, and updates sparkle  state.

    Score_Boost: This class represents a score booster in the game. It loads score booster images, handles score booster animation, and updates score   booster state.

Each class encapsulates functionality related to its respective game entity, including initialization, animation, updating position, and handling interactions. These classes collectively form the game's entities and their behaviors.

I_O_display.py defines several classes and their methods for creating sprites and managing their animation and movement in a Pygame environment. Here's a brief overview of each class:

    StartScreen: Represents the start screen of the game. It loads a series of images for animation and displays them sequentially.

    StartButton: Represents the start button on the start screen. Similar to StartScreen, it loads a series of images for animation.

    Game_BackG: Represents the background of the game. It loads a series of images for animation, scales them to fit the screen, and scrolls them   vertically to create a parallax effect.

    Draw_Ground: Manages the drawing and movement of the ground in the game. It loads two images for the ground and scrolls them horizontally to    simulate movement.

    Flying_Grounds: Represents flying objects in the game. It loads different images for these objects and moves them horizontally across the screen.

Each class has an update() method that is called once per frame to update the state of the sprite, including animation and movement.

while for the test_project.py it contains a series of test cases implemented using the pytest framework and typeguard library to test various functions from the project module. Let's break down each test case:

    test_New_User: This test case checks the New_User function. It asserts that calling the function with incorrect argument types should raise a   TypeError. It uses pytest.raises to check for the expected exception.

    test_Get_User: Similar to the previous test case, this one checks the Get_User function. It verifies that passing incorrect argument types to the   function raises a TypeError.

    test_Update_User: This test case checks the Update_User function. Like the others, it ensures that providing incorrect argument types triggers a    TypeError.

    test_Score_f: This test case checks the Score_f function. It validates that passing arguments of incorrect types to the function results in a   TypeError.

    test_print_const_text: This test case focuses on the print_const_text function. It creates a pygame.Surface object to simulate the display surface  and ensures that passing incorrect arguments to the function raises a BoundaryError.

Overall, these test cases cover different functions from the project module and verify their behavior when provided with invalid input types. They are essential for ensuring the robustness and reliability of the codebase.

# Background Music: [Online Ai Tool] (https://soundraw.io/)
# Font Credits: https://www.dafont.com/high-mount.font and https://github.com/clear-code-projects/UltimatePygameIntro/tree/main/font
# Artwork: https://www.artstation.com/artwork/GX3EQa and https://giphy.com/TEEY/legend-of-zelda and https://in.pinterest.com/pin/306104105924029733/
# Guidance : https://www.youtube.com/watch?v=AY9MnQ4x3zk and https://www.pygame.org/docs/tut/newbieguide.html and https://www.youtube.com/watch?v=tJiKYMQJnYg and https://pygame.readthedocs.io/en/latest/rect/rect.html
