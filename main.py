# TRISTAN PARRY - ICS3U 2020 - SEMESTER 2 - CULMINATING TASK - PYGAME GAME - MONOCHROME (PLATFORMER GAME)
# FILE: main




# BEFORE RUNNING THIS CODE, AND/OR THE PROVIDED .EXE FILE FOR THE CODE, PLEASE ENSURE THAT ALL ASSET FILES ARE DOWNLOADED AND PLACED IN THE CORRECT FOLDER, PICTURES.
#READ THE "READ_ME" FILE ATTACHED FOR MORE INFORMATION BEFORE USING THIS CODE, OR THE PROVIDED .EXE FILE


# THIS IS A GAME, CREATED WITH PYTHON AND PYGAME, IN WHICH YOU MUST COMPLETE PLATFORMER LEVELS AS A GLYPH (CHARACTER). USING LEFT AND RIGHT ARROW KEYS TO MOVE, AS WELL AS THE SPACEBAR (TO JUMP), COMPLETE ALL 5 LEVELS TO WIN.
# NOTE: ALL LEVELS HAVE BEEN TESTED AND ARE WINNABLE


# HAVE FUN & ENJOY THE GAME




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




# IMPORTING PYTHON MODULES

import random # Random is a python module that allows the computer to make a random choice between a range/list of given options, every time the code is run (see below)
import time # Time is a python module that allows the computer to track the time, in seconds, that the code is run, allowing for time manipulation within the code (see below)
import pygame # Pygame is a python module that allows for the creation and integration of a GUI, or graphics-based activity, within a code/program (this module allows the game to run in a graphics window, with graphic commands/sequences, see below)


# IMPORTING CREATED PY FILES

from setup_and_run import * # Imports all assets and information from the setup_and_run file
from asset_registry import * # Imports all assets and information from the asset_registry file
from level_registry import * # Imports all assets and information from the level_registry file




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




# CREATING THE PYGAME WINDOW, TO RENDER THE GAME IN

pygame.init() # Initializes pygame, to be used in the program
pygame.mixer.init() # Initializes the pygame sound mixer, to be used in the program
pygame.font.init() # Initializes pygame's use of fonts, to be used in the program
window=pygame.display.set_mode(window_resolution) # Creates the pygame window, to execute the game in
pygame.display.set_caption(window_caption) # Sets the caption of the pygame window
pygame.display.set_icon(windowIcon) # Sets the icon of the pygame window
windowClock=pygame.time.Clock() # Creates a clock, to regulate the tick speed and running of the game/program




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




# CREATING EMPTY GLOBAL userNameFinal, userSpriteAsset AND userSpriteNumber VARIABLES, TO BE CHANGED LATER IN THE PROGRAM (DEPENDING ON USER'S GLYPH (CHARACTER) CHOICE)

userNameFinal=None # userNameFinal it is set on the global level, and can be used in functions throughout the rest of the program, by calling "global userNameFinal" at the beginning of each function using the score variable.
userSpriteAsset=None # userSpriteAsset it is set on the global level, and can be used in functions throughout the rest of the program, by calling "global userSpriteAsset" at the beginning of each function using the score variable.
userSpriteNumber=None # userSpriteNumber it is set on the global level, and can be used in functions throughout the rest of the program, by calling "global userSpriteNumber" at the beginning of each function using the score variable.




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




# CREATING THE STORY FUNCTION, STARTING THE GAME

def story():
    global userNameFinal # This command allows the function to use and change the global variable, "userNameFinal"
    
    pygame.mixer.music.set_volume(0.5) # Sets the volume of the music
    pygame.mixer.music.play(-1) # Plays the music on an endless loop
    
    menuBox=menuBackground.get_rect() # This command creates a pygame Rect object for the menu background image (this helps to position/display it on the screen after)
    menuBox.center=(1600//2, 400//2) # This command centres the pygame Rect object around a single coordinate
    window.blit(menuBackground,menuBox) # This command renders the image onto the window
    
    userName = "" # Creates a userName variable, an empty string
    userNameEnter=True # Sets a userNameEnter variable to True, to manipulate in the while loop (below)
    
    while userNameEnter: # This loops forever, unles userNameEnter becomes False
        window.blit(menuBackground,menuBox) # This command renders the background onto the window
        enterUsername=mediumFont.render("ENTER USERNAME:",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
        enterUsernameBox=enterUsername.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        enterUsernameBox.center=(1600//2, 500//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(enterUsername,enterUsernameBox) # This command renders text onto the pygame window
        for event in pygame.event.get(): # For every one of the events that occur during the pygame execution:
            if event.type==pygame.KEYDOWN: # If a key is pressed down:
                if event.unicode.isalpha(): # If the entered characters can be recognized in unicode:
                    userName += event.unicode # Add the characters to the userName variable
                elif event.key==pygame.K_BACKSPACE: # If the backspace key is pressed down:
                    userName = userName[:-1] # Takes away the last character from the entered string
                elif event.key==pygame.K_RETURN: # If the enter (return) key is pressed down:
                    window.blit(menuBackground,menuBox) # This command renders the background onto the window
                    userNameFinal=userName # userNameFinal variable is set equal to the current userName variable
                    userName="" # the userName variable is set back to an empty string
                    enterUsername=mediumFont.render("",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
                    userNameEnter=False # Breaks the loop, by setting the userNameEnter variable to False
            elif event.type == pygame.QUIT: # If the window is closed:
                exit() # Terminate the program
        userNamePrint=mediumSmallFont.render(userName.upper(),True,WHITE) # This command creates a text variable, usable by pygame
        userNamePrintBox=userNamePrint.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        userNamePrintBox.center=(1600//2,800//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(userNamePrint, userNamePrintBox) # This command renders text onto the pygame window
        pygame.display.flip() # This command updates every asset in the current pygame display window
    
    ########################################################
    
    window.blit(menuBackground,menuBox) # This command renders the background onto the window
    time.sleep(1) # This command uses the time module, to stop all action in the pygame window, for 1 second
    userNameFinalPrint=mediumSmallFont.render("Hello  "+userNameFinal,True,LIGHT_GREY) # This command creates a text variable, usable by pygame
    userNameFinalPrintBox=userNameFinalPrint.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
    userNameFinalPrintBox.center=(1600//2,800//2) # This command centres the pygame Rect object around a single coordinate
    window.blit(userNameFinalPrint, userNameFinalPrintBox) # This command renders text onto the pygame window
    pygame.display.flip() # This command updates every asset in the current pygame display window
    time.sleep(2) # This command uses the time module, to stop all action in the pygame window, for 2 seconds
    window.blit(menuBackground,menuBox) # This command renders the background onto the window
    userNameFinalPrint3=mediumSmallFont.render("Welcome to",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
    userNameFinalPrintBox3=userNameFinalPrint3.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
    userNameFinalPrintBox3.center=(1600//2,800//2) # This command centres the pygame Rect object around a single coordinate
    window.blit(userNameFinalPrint3, userNameFinalPrintBox3) # This command renders text onto the pygame window
    pygame.display.flip() # This command updates every asset in the current pygame display window
    time.sleep(2) # This command uses the time module, to stop all action in the pygame window, for 2 seconds
    gameMenu() # Call the gameMenu() function




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




# CREATING A GAME MENU FUNCTION, TO ORGANIZE/START THE GAME

def gameMenu():
    global userSpriteAsset # This command allows the function to use and change the global variable, "userSpriteAsset"
    global userSpriteNumber # This command allows the function to use and change the global variable, "userSpriteNumber"
    
    menuBox=menuBackground.get_rect() # This command creates a pygame Rect object for the image (this helps to position/display it on the screen after)
    menuBox.center=(1600//2, 400//2) # This command centres the pygame Rect object around a single coordinate
    window.blit(menuBackground,menuBox) # This command renders the background onto the window
    iconBox=objectiveMenuPic.get_rect() # This command creates a pygame Rect object for the image (this helps to position/display it on the screen after)
    iconBox.center=(1550//2, 800//2) # This command centres the pygame Rect object around a single coordinate
    window.blit(objectiveMenuPic,iconBox) # This command renders the objective picture onto the window
    
    while True: # Loops forever, unless broken out of
        menuTitle=largeFont.render("MONO",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
        titleBox=menuTitle.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        titleBox.center=(1045//2, 400//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(menuTitle,titleBox) # This command renders text onto the pygame window
        menuTitle2=largeFont.render("CHROME",True,WHITE) # This command creates a text variable, usable by pygame
        titleBox2=menuTitle2.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        titleBox2.center=(1985//2, 400//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(menuTitle2,titleBox2) # This command renders text onto the pygame window
        
        playTitle=mediumFont.render("PLAY",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
        playBox=playTitle.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        playBox.center=(950//2, 900//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(playTitle,playBox) # This command renders text onto the pygame window
        playTitle2=smallFont.render("PRESS [P]",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
        playBox2=playTitle.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        playBox2.center=(1025//2, 1075//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(playTitle2,playBox2) # This command renders text onto the pygame window
        
        glyphsTitle=mediumFont.render("GLYPHS",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
        glyphsBox=glyphsTitle.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        glyphsBox.center=(2200//2, 900//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(glyphsTitle,glyphsBox) # This command renders text onto the pygame window
        glyphsTitle2=smallFont.render("PRESS G",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
        glyphsBox2=glyphsTitle2.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        glyphsBox2.center=(2200//2, 1045//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(glyphsTitle2,glyphsBox2) # This command renders text onto the pygame window
        
        controlsTitle=mediumFont.render("CONTROLS",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
        controlsBox=controlsTitle.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        controlsBox.center=(1560//2, 1250//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(controlsTitle,controlsBox) # This command renders text onto the pygame window
        controlsTitle2=smallFont.render("PRESS C",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
        controlsBox2=controlsTitle2.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        controlsBox2.center=(1560//2, 1395//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(controlsTitle2,controlsBox2) # This command renders text onto the pygame window
        
        ########################################################
        
        for event in pygame.event.get(): # For every one of the events that occur during the pygame execution:
            if event.type==pygame.KEYDOWN: # If a key is pressed down:
                if event.key==pygame.K_p: # If the p key is pressed down:
                    userSpriteNumber=random.randint(0,2) # Use the random function, to choose a random number between 0 and 2
                    userSpriteAsset=pygame.image.load(userSpriteAssets[userSpriteNumber][0]) # Load the facing forward image for one of the sprites, based on the random number just chosen
                    level1() # Call the level1() function
                elif event.key==pygame.K_g: # If the g key is pressed down:
                    glyphs_menu() # Call the glyphs_menu() function
                elif event.key==pygame.K_c: # If the c key is pressed down:
                    controls_menu() # Call the controls_menu() function
            elif event.type == pygame.QUIT:
                exit() # Terminate the program
                    
        pygame.display.update() # This command updates the pygame window, every frame




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




# CREATING THE GLYPH (CHARACTER) MENU

def glyphs_menu():
    global userSpriteAsset # This command allows the function to use and change the global variable, "userSpriteAsset"
    global userSpriteNumber # This command allows the function to use and change the global variable, "userSpriteNumber"
    
    menuBox=menuBackground.get_rect() # This command creates a pygame Rect object for the image (this helps to position/display it on the screen after)
    menuBox.center=(1600//2, 400//2) # This command centres the pygame Rect object around a single coordinate
    window.blit(menuBackground,menuBox) # This command renders the background onto the window
    
    while True:
        window.blit(menuBackground,menuBox) # This command renders the background onto the window
        menuTitle=mediumLargeFont.render("CHOOSE GLYPH",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
        titleBox=menuTitle.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        titleBox.center=(1600//2, 300//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(menuTitle,titleBox) # This command renders text onto the pygame window
        
        ########################################################
        
        sprite1Play=smallFont.render("PRESS  ONE",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
        playBox1=sprite1Play.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        playBox1.center=(600//2, 1200//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(sprite1Play,playBox1) # This command renders text onto the pygame window
        sprite2Play=smallFont.render("PRESS  TWO",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
        playBox2=sprite2Play.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        playBox2.center=(1585//2, 1200//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(sprite2Play,playBox2) # This command renders text onto the pygame window
        sprite3Play=smallFont.render("PRESS  THREE",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
        playBox3=sprite3Play.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        playBox3.center=(2600//2, 1200//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(sprite3Play,playBox3) # This command renders text onto the pygame window
        menuSubtitle=smallFont.render("PRESS ESC TO RETURN TO MENU",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
        subtitleBox=menuSubtitle.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        subtitleBox.center=(1600//2, 1400//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(menuSubtitle,subtitleBox) # This command renders text onto the pygame window
        
        ########################################################
        
        spriteBox=sprite2Menu.get_rect() # This command creates a pygame Rect object for the image (this helps to position/display it on the screen after)
        spriteBox.center=(610//2, 900//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(sprite1Menu,spriteBox)
        spriteBox2=sprite2Menu.get_rect() # This command creates a pygame Rect object for the image (this helps to position/display it on the screen after)
        spriteBox2.center=(1575//2, 800//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(sprite2Menu,spriteBox2)
        spriteBox3=sprite3Menu.get_rect() # This command creates a pygame Rect object for the image (this helps to position/display it on the screen after)
        spriteBox3.center=(2600//2, 800//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(sprite3Menu,spriteBox3)
        
        ########################################################
        
        for event in pygame.event.get(): # For every one of the events that occur during the pygame execution:
            if event.type==pygame.KEYDOWN: # If a key is pressed down:
                if event.key==pygame.K_ESCAPE: # If the escape key is pressed down:
                    gameMenu() # Call the gameMenu() function
                elif event.key==pygame.K_1: # If the 1 key is pressed down:
                    userSpriteNumber=0 # userSpriteNumber is set to 0
                    userSpriteAsset=pygame.image.load(userSpriteAssets[userSpriteNumber][0]) # Load the facing forward image for one of the sprites, based on the glyph just chosen
                    level1() # Call the level1() function
                elif event.key==pygame.K_2: # If the 2 key is pressed down:
                    userSpriteNumber=1 # userSpriteNumber is set to 1
                    userSpriteAsset=pygame.image.load(userSpriteAssets[userSpriteNumber][0]) # Load the facing forward image for one of the sprites, based on the glyph just chosen
                    level1() # Call the level1() function
                elif event.key==pygame.K_3: # If the 3 key is pressed down:
                    userSpriteNumber=2 # userSpriteNumber is set to 2
                    userSpriteAsset=pygame.image.load(userSpriteAssets[userSpriteNumber][0]) # Load the facing forward image for one of the sprites, based on the glyph just chosen
                    level1() # Call the level1() function
            elif event.type == pygame.QUIT: # If the window is closed:
                exit() # Terminate the program
    
        pygame.display.update() # This command updates the pygame window, every frame




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




# CREATING THE CONTROLS MENU

def controls_menu():
    menuBox=menuBackground.get_rect() # This command creates a pygame Rect object for the image (this helps to position/display it on the screen after)
    menuBox.center=(1600//2, 400//2) # This command centres the pygame Rect object around a single coordinate
    window.blit(menuBackground,menuBox) # This command renders the background onto the window
    
    while True:
        window.blit(menuBackground,menuBox) # This command renders the background onto the window
        menuTitle=mediumLargeFont.render("CONTROLS",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
        titleBox=menuTitle.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        titleBox.center=(1600//2, 300//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(menuTitle,titleBox) # This command renders text onto the pygame window
        
        ########################################################
        
        controlsText=mediumSmallerFont.render("USE LEFT AND RIGHT ARROWS TO MOVE",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
        textBox=controlsText.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        textBox.center=(1060//2, 600//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(controlsText,textBox) # This command renders text onto the pygame window
        controlsText2=mediumSmallerFont.render("USE SPACE TO JUMP",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
        textBox2=controlsText2.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        textBox2.center=(748//2, 750//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(controlsText2,textBox2) # This command renders text onto the pygame window
        controlsText3=mediumSmallerFont.render("AVOID ENEMIES",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
        textBox3=controlsText3.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        textBox3.center=(660//2, 900//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(controlsText3,textBox3) # This command renders text onto the pygame window
        controlsText4=mediumSmallerFont.render("GET TO THE OBJECTIVE",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
        textBox4=controlsText4.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        textBox4.center=(800//2, 1050//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(controlsText4,textBox4) # This command renders text onto the pygame window
        controlsText4=smallFont.render("ENEMIES",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
        textBox4=controlsText4.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        textBox4.center=(2325//2, 1200//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(controlsText4,textBox4) # This command renders text onto the pygame window
        controlsText5=smallFont.render("OBJECTIVE",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
        textBox5=controlsText5.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        textBox5.center=(2800//2, 1200//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(controlsText5,textBox5) # This command renders text onto the pygame window
        
        ########################################################
        
        enemyBox=enemySpriteMenuPic.get_rect() # This command creates a pygame Rect object for the image (this helps to position/display it on the screen after)
        enemyBox.center=(2325//2, 800//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(enemySpriteMenuPic,enemyBox) # This command renders the enemy picture onto the window
        objectiveBox=objectiveSpriteAsset.get_rect() # This command creates a pygame Rect object for the image (this helps to position/display it on the screen after)
        objectiveBox.center=(2800//2, 900//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(objectiveSpriteAsset,objectiveBox) # This command renders the objective picture onto the window
        
        menuSubtitle=smallFont.render("PRESS ESC TO RETURN TO MENU",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
        subtitleBox=menuSubtitle.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        subtitleBox.center=(1600//2, 1400//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(menuSubtitle,subtitleBox) # This command renders the text onto the window
        
        for event in pygame.event.get(): # For every one of the events that occur during the pygame execution:
            if event.type==pygame.KEYDOWN: # If a key is pressed down:
                if event.key==pygame.K_ESCAPE: # If the escape key is pressed down:
                    gameMenu() # Call the gameMenu() function
            elif event.type == pygame.QUIT: # If the window is closed:
                exit() # Terminate the program
    
        pygame.display.update() # This command updates the pygame window, every frame




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




# CREATING THE "GAME OVER" MENU

def gameOverMenu():
        global userSpriteNumber # This command allows the function to use and change the global variable, "userSpriteNumber"
        global userNameFinal # This command allows the function to use and change the global variable, "userNameFinal"
        
        menuBox=menuBackground.get_rect() # This command creates a pygame Rect object for the image (this helps to position/display it on the screen after)
        menuBox.center=(1600//2, 400//2) # This command centres the pygame Rect object around a single coordinate
        spritePic=pygame.image.load(userSpritesMenu[userSpriteNumber]) # This command loads the image for the user's sprite
        
        while True: # Loops forever, unless broken out of
            window.blit(menuBackground,menuBox) # This command renders the background onto the window
            gameOverTitle=mediumFont.render("GAME OVER",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
            titleBox=gameOverTitle.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
            titleBox.center=(1560//2, 300//2) # This command centres the pygame Rect object around a single coordinate
            window.blit(gameOverTitle,titleBox) # This command renders text onto the pygame window
            spriteBox=spritePic.get_rect() # This command creates a pygame Rect object for the image (this helps to position/display it on the screen after)
            spriteBox.center=(1550//2, 925//2) # This command centres the pygame Rect object around a single coordinate
            window.blit(spritePic,spriteBox) # This command renders the image onto the pygame window
            gameOverTitle2=mediumSmallFont.render(userNameFinal+"  died.",True,WHITE) # This command creates a text variable, usable by pygame
            titleBox2=gameOverTitle2.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
            titleBox2.center=(1575//2, 450//2) # This command centres the pygame Rect object around a single coordinate
            window.blit(gameOverTitle2,titleBox2) # This command renders text onto the pygame window
            gameOverTitle3=smallFont.render("PRESS O to return to menu",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
            titleBox3=gameOverTitle3.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
            titleBox3.center=(1560//2, 1450//2) # This command centres the pygame Rect object around a single coordinate
            window.blit(gameOverTitle3,titleBox3) # This command renders text onto the pygame window
            pygame.display.flip() # This command updates every asset in the current pygame display window
            
            ########################################################
            
            for event in pygame.event.get(): # For every one of the events that occur during the pygame execution:
                if event.type==pygame.KEYDOWN: # If a key is pressed down:
                    if event.key==pygame.K_o: # If the o key is pressed down:
                        gameMenu() # Call the gameMenu() function
                elif event.type == pygame.QUIT: # If the window is closed:
                    exit() # Terminate the program
        
        pygame.display.update() # This command updates the pygame window, every frame




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




# CREATING A FUNCTION FOR LEVEL 1

def level1():
    global userSpriteAsset # This command allows the function to use and change the global variable, "userSpriteAsset"
    global userSpriteNumber # This command allows the function to use and change the global variable, "userSpriteNumber"
    
    # Creating a pause menu for the level
    def pauseGame():
        global userSpriteNumber # This command allows the function to use and change the global variable, "userSpriteNumber"
        
        menuBox=menuBackground.get_rect() # This command creates a pygame Rect object for the menu background image (this helps to position/display it on the screen after)
        menuBox.center=(1600//2, 400//2) # This command centres the pygame Rect object around a single coordinate
        spritePic=pygame.image.load(userSpritesMenu[userSpriteNumber]) # This command uses pygame to load an image (from the file directory), into the game as the character sprite
        
        isGamePaused=True # This variable is used in the creation of a while True loop (see below), when the pauseGame() function is entered, it makes the pause variable true
            
        while isGamePaused: # This loop will iterate forever, while isGamePaused remains True
            # Rendering menu assets/text
            window.blit(menuBackground,menuBox) # This command renders an image onto the pygame window
            pauseTitle=mediumFont.render("PAUSED",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
            pauseBox=pauseTitle.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
            pauseBox.center=(1560//2, 300//2) # This command centres the pygame Rect object around a single coordinate
            window.blit(pauseTitle,pauseBox) # This command renders text onto the pygame window
            spriteBox=spritePic.get_rect() # This command creates a pygame Rect object for an image (this helps to position/display it on the screen after)
            spriteBox.center=(1550//2, 825//2) # This command centres the pygame Rect object around a single coordinate
            window.blit(spritePic,spriteBox) # This command renders text onto the pygame window
            pauseTitle2=smallFont.render("PRESS esc to continue",True,LIGHT_GREY)
            pauseBox2=pauseTitle2.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
            pauseBox2.center=(1560//2, 1395//2) # This command centres the pygame Rect object around a single coordinate
            window.blit(pauseTitle2,pauseBox2) # This command renders text onto the pygame window
            pauseTitle3=smallFont.render("PRESS O to return to menu",True,LIGHT_GREY)
            pauseBox3=pauseTitle3.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
            pauseBox3.center=(1560//2, 1450//2) # This command centres the pygame Rect object around a single coordinate
            window.blit(pauseTitle3,pauseBox3) # This command renders text onto the pygame window
            pygame.display.flip() # This command updates every asset in the current pygame display window
            
            # Pygame event loop for menu
            for event in pygame.event.get(): # For every one of the events that occur during the pygame execution:
                if event.type==pygame.KEYDOWN: # If a key is pressed down:
                    if event.key==pygame.K_ESCAPE: # If the escape key is pressed down:
                        isGamePaused=False # The isGamePaused variable becomes false, effectively leaving the pauseGame() function
                    elif event.key==pygame.K_o: # If the O key is pressed down:
                        isGamePaused=False # The isGamePaused variable becomes false, effectively leaving the pauseGame() function
                        for platform in platformListLevel1: # For every one of the platforms in the window:
                            platform.x+=scrollCount # Move the platforms back to their original place (if the window has scrolled them to a different location)
                        for enemy in enemyListLevel1: # For every one of the enemies in the window:
                            enemy.x+=scrollCount # Move the enemies back to their original place (if the window has scrolled them to a different location)
                        objectiveLevel1Rect.x+=scrollCount # Move the objective box back to its original place (if the window has scrolled it to a different location)
                        gameMenu() # Call the gameMenu() function
                elif event.type == pygame.QUIT: # If the window is closed:
                    exit() # Terminate the program
        
        pygame.display.update() # This command updates the pygame window, every frame
    
    ########################################################
    
    backgroundBox=gameBackgroundLevel1.get_rect() # This command creates a pygame Rect object for the background image (this helps to position/display it on the screen after)
    backgroundBox.center=(1600//2, 800//2) # This command centres the pygame Rect object around a single coordinate
    
    # Create location, moving, gravity, and rect variables for the user's sprite, to make writing collision code and other game aspects easier
    # Defining the userSprite's abilities and parameters
    userSpriteMoveLeft=False # The userSpriteMoveLeft variable is set to False
    userSpriteMoveRight=False # The userSpriteMoveRight variable is set to False
    jumpTimer=0 # The jumpTimer variable for the userSprite is set to 0
    userSpriteLocationXY=[200,600] # This creates the player's starting location in the pygame window [x,y]
    forceOfGravity=0 # The forceOfGravity variable for the userSprite is set to 0
    userSpriteRect=pygame.Rect(userSpriteLocationXY[0],userSpriteLocationXY[1],userSpriteAsset.get_width(),userSpriteAsset.get_height()) # This command creates a pygame Rect object for the userSprite (to check for rect collisions later)
    
    # Creating a variable to aid in window scrolling throughout the level
    scrollCount=0 # The scrollCount variable (for the objects in the pygame window) is set to 0
    
    ########################################################
    
    # Main game loop
    while True: # This loops forever, unless a certain event breaks the loop
        # Rendering images onto the pygame window
        window.blit(gameBackgroundLevel1,backgroundBox) # This command renders an image onto the pygame window
        window.blit(userSpriteAsset,(userSpriteLocationXY)) # This command renders the userSprite onto the pygame window, in its starting location
        
        # Rendering enemies onto screen
        for enemy in enemyListLevel1: # For every one of the enemies in the window:
            window.blit(pygame.image.load(enemySpriteAsset),enemy) # This command renders the enemy onto the pygame window
            
        # Rendering platforms onto pygame window
        for platform in platformListLevel1: # For every one of the platforms in the window:
            pygame.draw.rect(window,BLACK,platform) # This command renders the platform onto the pygame window
        
        # Rendering the objective box onto pygame window
        window.blit(objectiveSpriteAsset,objectiveLevel1Rect) # This command renders the objective onto the pygame window
        
        ########################################################
        
        # Scrolling the pygame window
        if userSpriteLocationXY[0]>(window_resolution[0]/4) and (userSpriteMoveRight==True) and (userSpriteLocationXY[0]+userSpriteAsset.get_width()<=window_resolution[0]): # If the player is moving right, and they are on the right 2/3 of the screen:
            scrollCount+=5 # Increment the scrollCount variable by 5
            for platform in platformListLevel1: # For every one of the platforms in the window:
                platform.x-=5 # Move the platform 5 pixels left
            for enemy in enemyListLevel1: # For every one of the enemies in the window:
                enemy.x-=5 # Move the enemy 5 pixels left
            objectiveLevel1Rect.x-=5 # Move the objective 5 pixels left
        
        ########################################################
        
        # Applying/Managing player sprite movement on the X axis
        if userSpriteMoveLeft==True: # If the user is moving left:
            userSpriteLocationXY[0]-=8 # Move the userSprite 8 pixels to the left:
            userSpriteAsset=pygame.image.load(userSpriteAssets[userSpriteNumber][1]) # Display the user's image (for moving left)
        if userSpriteMoveRight==True: # If the user is moving right:
            userSpriteLocationXY[0]+=8 # Move the userSprite 8 pixels to the right:
            userSpriteAsset=pygame.image.load(userSpriteAssets[userSpriteNumber][2]) # Display the user's image (for moving right)
        if (userSpriteMoveLeft==False) and (userSpriteMoveRight==False): # If the user is not moving left or right:
            userSpriteAsset=pygame.image.load(userSpriteAssets[userSpriteNumber][0]) # Display the user's image (for facing forward)
        
        # Applying/Managing forceOfGravity variable
        userSpriteLocationXY[1]+=forceOfGravity # Increment the user's y coordinate by the forceOfGravity value
        forceOfGravity+=0.8 # Increment the forceOfGravity value by 0.8
        if forceOfGravity>16: # If the forceOfGravity value is over 16:
            forceOfGravity=16 # Set the forceOfGravity value to 16 (gravity strength cap=16)
        
        # Reloading the userSpriteRect object in the user's new location (after movement)
        userSpriteRect.x=userSpriteLocationXY[0] # Update the X position of the user Rect object to the X position of the user image
        userSpriteRect.y=userSpriteLocationXY[1] # Update the Y position of the user Rect object to the Y position of the user image
        
        ########################################################
        
        # Check for collisions with the left/right screen borders
        if (userSpriteLocationXY[0]+userSpriteAsset.get_width())>window_resolution[0]: # If the user collides with the right side of the screen:
            userSpriteLocationXY[0]=window_resolution[0]-userSpriteAsset.get_width() # Set the user's location to the right side of the screen (but not off it)
        if userSpriteLocationXY[0]<0: # If the user collides with the left side of the screen:
            userSpriteLocationXY[0]=0 # Set the user's location to the left side of the screen (but not off it)
        
        # Check if player falls down out of screen (if so, game over)
        if (userSpriteLocationXY[1]+userSpriteAsset.get_height())>window_resolution[1]: # If the user collides with the bottom edge of the screen:
            hitSoundEffect.set_volume(1.5) # Set the volume of the hitSoundEffect
            hitSoundEffect.play() # Play the hitSoundEffect
            for platform in platformListLevel1: # For every one of the platforms in the window:
                platform.x+=scrollCount # Move the platforms back to their original place (if the window has scrolled them to a different location)
            for enemy in enemyListLevel1: # For every one of the enemies in the window:
                enemy.x+=scrollCount # Move the enemies back to their original place (if the window has scrolled them to a different location)
            objectiveLevel1Rect.x+=scrollCount # Move the objective back to its original place (if the window has scrolled it to a different location)
            gameOverMenu() # Call the gameOverMenu() function
        
        #Check for userSprite collisions with platforms
        onTop=False # The onTop variable is set to False
        onBottom=False # The onBottom variable is set to False
        for platform in platformListLevel1: # For every one of the platforms in the window (user and platform):
            platformLocationX=platform.x # Define a variable for the platform Rect object's X location
            platformLocationY=platform.y # Define a variable for the platform Rect object's Y location
            if userSpriteRect.colliderect(platform): # If two pygame Rect objects collide:
                # Colliding with top of the platform
                if (userSpriteLocationXY[1] + userSpriteAsset.get_height() >= platformLocationY) and (userSpriteLocationXY[1] + userSpriteAsset.get_height() <= platformLocationY + platform.height): # If the user collides with the top of the platform:
                    userSpriteLocationXY[1]=platformLocationY-userSpriteAsset.get_height() # Set the user's location to the top of the platform
                    onTop=True # The onTop variable is set to True
                    forceOfGravity=0 # The forceOfGravity variable is set to 0 (stops the user from shooting down, if they stand on the platform for a while, and then jump off of it)
                # Colliding with bottom of the platform
                if (userSpriteLocationXY[1] <= platformLocationY + platform.height) and (userSpriteLocationXY[1] >= platformLocationY): # If the user collides with the bottom of the platform:
                    userSpriteLocationXY[1]=platformLocationY + platform.height # Set the user's location to the bottom of the platform
                    onBottom=True # The onBottom variable is set to True
                
                if (onTop==False) and (onBottom==False): # If the onTop and onBottom variables are set to False (the user is not colliding with the top or bottom of the platform):
                    # Colliding with left side of the platform
                    if (userSpriteLocationXY[0] + userSpriteAsset.get_width() >= platformLocationX) and (userSpriteLocationXY[0] + userSpriteAsset.get_width() <= platformLocationX + platform.width): # If the user collides with the left side of the platform:
                        userSpriteLocationXY[0] = platformLocationX - userSpriteAsset.get_width() # Set the user's location to the left side of the platform
                    # Colliding with right side of the platform
                    if (userSpriteLocationXY[0] <= platformLocationX + platform.width) and (userSpriteLocationXY[0] >= platformLocationX): # If the user collides with the right side of the platform:
                        userSpriteLocationXY[0] = platformLocationX + platform.width # Set the user's location to the right side of the platform
        
        # Check for userSprite collisions with enemies
        for enemy in enemyListLevel1: # For every one of the enemies in the window:
            enemyLocationX=enemy.x # Define a variable for the emeny Rect object's X location
            enemyLocationY=enemy.y # Define a variable for the emeny Rect object's Y location
            if userSpriteRect.colliderect(enemy): # If two pygame Rect objects collide (user and enemy):
                hitSoundEffect.set_volume(1.5) # Set the volume of the hitSoundEffect
                hitSoundEffect.play() # Play the hitSoundEffect
                for platform in platformListLevel1: # For every one of the platforms in the window:
                    platform.x+=scrollCount # Move the platforms back to their original place (if the window has scrolled them to a different location)
                for enemy in enemyListLevel1: # For every one of the enemies in the window:
                    enemy.x+=scrollCount # Move the enemies back to their original place (if the window has scrolled them to a different location)
                objectiveLevel1Rect.x+=scrollCount # Move the objective back to its original place (if the window has scrolled it to a different location)
                gameOverMenu() # Call the gameOverMenu() function
        
        # Check for userSprite collisions with objective
        if userSpriteRect.colliderect(objectiveLevel1Rect): # If two pygame Rect objects collide (user and objective):
            levelCompleteSoundEffect.set_volume(0.75) # Set the volume of the levelCompleteSoundEffect
            levelCompleteSoundEffect.play() # Play the levelCompleteSoundEffect
            for platform in platformListLevel1: # For every one of the platforms in the window:
                platform.x+=scrollCount # Move the platforms back to their original place (if the window has scrolled them to a different location)
            for enemy in enemyListLevel1: # For every one of the enemies in the window:
                enemy.x+=scrollCount # Move the enemies back to their original place (if the window has scrolled them to a different location)
            objectiveLevel1Rect.x+=scrollCount # Move the objective back to its original place (if the window has scrolled it to a different location)
            level2() # Call the level2() function
        
        ########################################################
        
        # Manipulating the jumpTimer variable (ensures that the user cannot jump while in the air)
        if onTop==True: # If the user is not jumping:
            jumpTimer=0 # Set the jumpTimer to 0
        else: # This conditional statement is entered if the value in onTop is False (user is in the air)
            jumpTimer+=1 # Increment the jumpTimer by 1
        
        ########################################################
        
        # Rendering the pause caption onto the pygame window
        pauseCaption=smallFont.render("press esc to pause",True,WHITE,BLACK) # This command creates a text variable, usable by pygame
        captionBox=pauseCaption.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        captionBox.center=(300//2, 1550//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(pauseCaption,captionBox) # This command renders text onto the pygame window
        
        # Rendering the level number onto the pygame window
        levelCaption=smallFont.render("Level One",True,WHITE,BLACK) # This command creates a text variable, usable by pygame
        levelBox=levelCaption.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        levelBox.center=(175//2, 50//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(levelCaption,levelBox) # This command renders text onto the pygame window
        
        ########################################################
        
        # Main pygame event loop
        for event in pygame.event.get(): # For every one of the events that occur during the pygame execution:
            if event.type==pygame.KEYDOWN: # If a key is pressed down:
                if event.key==pygame.K_ESCAPE: # If the escape key is pressed down:
                    pauseGame() # Call the pauseGame() function()
                if event.key==pygame.K_LEFT: # If the left arrow key is pressed down:
                    userSpriteMoveLeft=True # The player moves left
                if event.key==pygame.K_RIGHT: # If the right arrow key is pressed down:
                    userSpriteMoveRight=True # The player moves right
                if event.key==pygame.K_SPACE: # If the space key is pressed down:
                    if onTop==True: # If the player is on top of a platform:
                        jumpSoundEffect.set_volume(0.5) # Set the volume of the jumpSoundEffect
                        jumpSoundEffect.play() # Play the jumpSoundEffect
                    if jumpTimer<4: # If the jumpTimer is less than 4:
                        forceOfGravity=-16 # Subtract 16 from the forceOfGravity variable (makes the player go up)
            elif event.type==pygame.KEYUP: # If a key is released:
                if event.key==pygame.K_LEFT: # If the left arrow key is released:
                    userSpriteMoveLeft=False # The player stops moving left
                if event.key==pygame.K_RIGHT: # If the right arrow key is released:
                    userSpriteMoveRight=False # The player stops moving right
            elif event.type == pygame.QUIT: # If the window is closed:
                exit() # Terminate the program
        
        ########################################################
        
        # Update the window, and make the game run at 60FPS
        pygame.display.update() # This command updates the pygame window, every frame
        windowClock.tick(window_fps) # This command makes the program run at a designated frame rate (in this case, window_fps is set to 60)




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




# CREATING A FUNCTION FOR LEVEL 2

def level2():
    global userSpriteAsset # This command allows the function to use and change the global variable, "userSpriteAsset"
    global userSpriteNumber # This command allows the function to use and change the global variable, "userSpriteNumber"
    
    # Creating a pause menu for the level
    def pauseGame():
        global userSpriteNumber # This command allows the function to use and change the global variable, "userSpriteNumber"
        
        menuBox=menuBackground.get_rect() # This command creates a pygame Rect object for the menu background image (this helps to position/display it on the screen after)
        menuBox.center=(1600//2, 400//2) # This command centres the pygame Rect object around a single coordinate
        spritePic=pygame.image.load(userSpritesMenu[userSpriteNumber]) # This command uses pygame to load an image (from the file directory), into the game as the character sprite
        
        isGamePaused=True # This variable is used in the creation of a while True loop (see below), when the pauseGame() function is entered, it makes the pause variable true
            
        while isGamePaused: # This loop will iterate forever, while isGamePaused remains True
            # Rendering menu assets/text
            window.blit(menuBackground,menuBox) # This command renders an image onto the pygame window
            pauseTitle=mediumFont.render("PAUSED",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
            pauseBox=pauseTitle.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
            pauseBox.center=(1560//2, 300//2) # This command centres the pygame Rect object around a single coordinate
            window.blit(pauseTitle,pauseBox) # This command renders text onto the pygame window
            spriteBox=spritePic.get_rect() # This command creates a pygame Rect object for an image (this helps to position/display it on the screen after)
            spriteBox.center=(1550//2, 825//2) # This command centres the pygame Rect object around a single coordinate
            window.blit(spritePic,spriteBox) # This command renders text onto the pygame window
            pauseTitle2=smallFont.render("PRESS esc to continue",True,LIGHT_GREY)
            pauseBox2=pauseTitle2.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
            pauseBox2.center=(1560//2, 1395//2) # This command centres the pygame Rect object around a single coordinate
            window.blit(pauseTitle2,pauseBox2) # This command renders text onto the pygame window
            pauseTitle3=smallFont.render("PRESS O to return to menu",True,LIGHT_GREY)
            pauseBox3=pauseTitle3.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
            pauseBox3.center=(1560//2, 1450//2) # This command centres the pygame Rect object around a single coordinate
            window.blit(pauseTitle3,pauseBox3) # This command renders text onto the pygame window
            pygame.display.flip() # This command updates every asset in the current pygame display window
            
            # Pygame event loop for menu
            for event in pygame.event.get(): # For every one of the events that occur during the pygame execution:
                if event.type==pygame.KEYDOWN: # If a key is pressed down:
                    if event.key==pygame.K_ESCAPE: # If the escape key is pressed down:
                        isGamePaused=False # The isGamePaused variable becomes false, effectively leaving the pauseGame() function
                    elif event.key==pygame.K_o: # If the O key is pressed down:
                        isGamePaused=False # The isGamePaused variable becomes false, effectively leaving the pauseGame() function
                        for platform in platformListLevel2: # For every one of the platforms in the window:
                            platform.x+=scrollCount # Move the platforms back to their original place (if the window has scrolled them to a different location)
                        for enemy in enemyListLevel2: # For every one of the enemies in the window:
                            enemy.x+=scrollCount # Move the enemies back to their original place (if the window has scrolled them to a different location)
                        objectiveLevel2Rect.x+=scrollCount # Move the objective box back to its original place (if the window has scrolled it to a different location)
                        gameMenu() # Call the gameMenu() function
                elif event.type == pygame.QUIT: # If the window is closed:
                    exit() # Terminate the program
        
        pygame.display.update() # This command updates the pygame window, every frame
    
    ########################################################
    
    backgroundBox=gameBackgroundLevel2.get_rect() # This command creates a pygame Rect object for the background image (this helps to position/display it on the screen after)
    backgroundBox.center=(1600//2, 800//2) # This command centres the pygame Rect object around a single coordinate
    
    # Create location, moving, gravity, and rect variables for the user's sprite, to make writing collision code and other game aspects easier
    # Defining the userSprite's abilities and parameters
    userSpriteMoveLeft=False # The userSpriteMoveLeft variable is set to False
    userSpriteMoveRight=False # The userSpriteMoveRight variable is set to False
    jumpTimer=0 # The jumpTimer variable for the userSprite is set to 0
    userSpriteLocationXY=[200,600] # This creates the player's starting location in the pygame window [x,y]
    forceOfGravity=0 # The forceOfGravity variable for the userSprite is set to 0
    userSpriteRect=pygame.Rect(userSpriteLocationXY[0],userSpriteLocationXY[1],userSpriteAsset.get_width(),userSpriteAsset.get_height()) # This command creates a pygame Rect object for the userSprite (to check for rect collisions later)
    
    # Creating a variable to aid in window scrolling throughout the level
    scrollCount=0 # The scrollCount variable (for the objects in the pygame window) is set to 0
    
    ########################################################
    
    # Main game loop
    while True: # This loops forever, unless a certain event breaks the loop
        # Rendering images onto the pygame window
        window.blit(gameBackgroundLevel2,backgroundBox) # This command renders an image onto the pygame window
        window.blit(userSpriteAsset,(userSpriteLocationXY)) # This command renders the userSprite onto the pygame window, in its starting location
        
        # Rendering enemies onto screen
        for enemy in enemyListLevel2: # For every one of the enemies in the window:
            window.blit(pygame.image.load(enemySpriteAsset),enemy) # This command renders the enemy onto the pygame window
            
        # Rendering platforms onto pygame window
        for platform in platformListLevel2: # For every one of the platforms in the window:
            pygame.draw.rect(window,BLACK,platform) # This command renders the platform onto the pygame window
        
        # Rendering the objective box onto pygame window
        window.blit(objectiveSpriteAsset,objectiveLevel2Rect) # This command renders the objective onto the pygame window
        
        ########################################################
        
        # Scrolling the pygame window
        if userSpriteLocationXY[0]>(window_resolution[0]/4) and (userSpriteMoveRight==True) and (userSpriteLocationXY[0]+userSpriteAsset.get_width()<=window_resolution[0]): # If the player is moving right, and they are on the right 2/3 of the screen:
            scrollCount+=5 # Increment the scrollCount variable by 5
            for platform in platformListLevel2: # For every one of the platforms in the window:
                platform.x-=5 # Move the platform 5 pixels left
            for enemy in enemyListLevel2: # For every one of the enemies in the window:
                enemy.x-=5 # Move the enemy 5 pixels left
            objectiveLevel2Rect.x-=5 # Move the objective 5 pixels left
        
        ########################################################
        
        # Applying/Managing player sprite movement on the X axis
        if userSpriteMoveLeft==True: # If the user is moving left:
            userSpriteLocationXY[0]-=8 # Move the userSprite 8 pixels to the left:
            userSpriteAsset=pygame.image.load(userSpriteAssets[userSpriteNumber][1]) # Display the user's image (for moving left)
        if userSpriteMoveRight==True: # If the user is moving right:
            userSpriteLocationXY[0]+=8 # Move the userSprite 8 pixels to the right:
            userSpriteAsset=pygame.image.load(userSpriteAssets[userSpriteNumber][2]) # Display the user's image (for moving right)
        if (userSpriteMoveLeft==False) and (userSpriteMoveRight==False): # If the user is not moving left or right:
            userSpriteAsset=pygame.image.load(userSpriteAssets[userSpriteNumber][0]) # Display the user's image (for facing forward)
        
        # Applying/Managing forceOfGravity variable
        userSpriteLocationXY[1]+=forceOfGravity # Increment the user's y coordinate by the forceOfGravity value
        forceOfGravity+=0.8 # Increment the forceOfGravity value by 0.8
        if forceOfGravity>16: # If the forceOfGravity value is over 16:
            forceOfGravity=16 # Set the forceOfGravity value to 16 (gravity strength cap=16)
        
        # Reloading the userSpriteRect object in the user's new location (after movement)
        userSpriteRect.x=userSpriteLocationXY[0] # Update the X position of the user Rect object to the X position of the user image
        userSpriteRect.y=userSpriteLocationXY[1] # Update the Y position of the user Rect object to the Y position of the user image
        
        ########################################################
        
        # Check for collisions with the left/right screen borders
        if (userSpriteLocationXY[0]+userSpriteAsset.get_width())>window_resolution[0]: # If the user collides with the right side of the screen:
            userSpriteLocationXY[0]=window_resolution[0]-userSpriteAsset.get_width() # Set the user's location to the right side of the screen (but not off it)
        if userSpriteLocationXY[0]<0: # If the user collides with the left side of the screen:
            userSpriteLocationXY[0]=0 # Set the user's location to the left side of the screen (but not off it)
        
        # Check if player falls down out of screen (if so, game over)
        if (userSpriteLocationXY[1]+userSpriteAsset.get_height())>window_resolution[1]: # If the user collides with the bottom edge of the screen:
            hitSoundEffect.set_volume(1.5) # Set the volume of the hitSoundEffect
            hitSoundEffect.play() # Play the hitSoundEffect
            for platform in platformListLevel2: # For every one of the platforms in the window:
                platform.x+=scrollCount # Move the platforms back to their original place (if the window has scrolled them to a different location)
            for enemy in enemyListLevel2: # For every one of the enemies in the window:
                enemy.x+=scrollCount # Move the enemies back to their original place (if the window has scrolled them to a different location)
            objectiveLevel2Rect.x+=scrollCount # Move the objective back to its original place (if the window has scrolled it to a different location)
            gameOverMenu() # Call the gameOverMenu() function
        
        #Check for userSprite collisions with platforms
        onTop=False # The onTop variable is set to False
        onBottom=False # The onBottom variable is set to False
        for platform in platformListLevel2: # For every one of the platforms in the window (user and platform):
            platformLocationX=platform.x # Define a variable for the platform Rect object's X location
            platformLocationY=platform.y # Define a variable for the platform Rect object's Y location
            if userSpriteRect.colliderect(platform): # If two pygame Rect objects collide:
                # Colliding with top of the platform
                if (userSpriteLocationXY[1] + userSpriteAsset.get_height() >= platformLocationY) and (userSpriteLocationXY[1] + userSpriteAsset.get_height() <= platformLocationY + platform.height): # If the user collides with the top of the platform:
                    userSpriteLocationXY[1]=platformLocationY-userSpriteAsset.get_height() # Set the user's location to the top of the platform
                    onTop=True # The onTop variable is set to True
                    forceOfGravity=0 # The forceOfGravity variable is set to 0 (stops the user from shooting down, if they stand on the platform for a while, and then jump off of it)
                # Colliding with bottom of the platform
                if (userSpriteLocationXY[1] <= platformLocationY + platform.height) and (userSpriteLocationXY[1] >= platformLocationY): # If the user collides with the bottom of the platform:
                    userSpriteLocationXY[1]=platformLocationY + platform.height # Set the user's location to the bottom of the platform
                    onBottom=True # The onBottom variable is set to True
                
                if (onTop==False) and (onBottom==False): # If the onTop and onBottom variables are set to False (the user is not colliding with the top or bottom of the platform):
                    # Colliding with left side of the platform
                    if (userSpriteLocationXY[0] + userSpriteAsset.get_width() >= platformLocationX) and (userSpriteLocationXY[0] + userSpriteAsset.get_width() <= platformLocationX + platform.width): # If the user collides with the left side of the platform:
                        userSpriteLocationXY[0] = platformLocationX - userSpriteAsset.get_width() # Set the user's location to the left side of the platform
                    # Colliding with right side of the platform
                    if (userSpriteLocationXY[0] <= platformLocationX + platform.width) and (userSpriteLocationXY[0] >= platformLocationX): # If the user collides with the right side of the platform:
                        userSpriteLocationXY[0] = platformLocationX + platform.width # Set the user's location to the right side of the platform
        
        # Check for userSprite collisions with enemies
        for enemy in enemyListLevel2: # For every one of the enemies in the window:
            enemyLocationX=enemy.x # Define a variable for the emeny Rect object's X location
            enemyLocationY=enemy.y # Define a variable for the emeny Rect object's Y location
            if userSpriteRect.colliderect(enemy): # If two pygame Rect objects collide (user and enemy):
                hitSoundEffect.set_volume(1.5) # Set the volume of the hitSoundEffect
                hitSoundEffect.play() # Play the hitSoundEffect
                for platform in platformListLevel2: # For every one of the platforms in the window:
                    platform.x+=scrollCount # Move the platforms back to their original place (if the window has scrolled them to a different location)
                for enemy in enemyListLevel2: # For every one of the enemies in the window:
                    enemy.x+=scrollCount # Move the enemies back to their original place (if the window has scrolled them to a different location)
                objectiveLevel2Rect.x+=scrollCount # Move the objective back to its original place (if the window has scrolled it to a different location)
                gameOverMenu() # Call the gameOverMenu() function
        
        # Check for userSprite collisions with objective
        if userSpriteRect.colliderect(objectiveLevel2Rect): # If two pygame Rect objects collide (user and objective):
            levelCompleteSoundEffect.set_volume(0.75) # Set the volume of the levelCompleteSoundEffect
            levelCompleteSoundEffect.play() # Play the levelCompleteSoundEffect
            for platform in platformListLevel2: # For every one of the platforms in the window:
                platform.x+=scrollCount # Move the platforms back to their original place (if the window has scrolled them to a different location)
            for enemy in enemyListLevel2: # For every one of the enemies in the window:
                enemy.x+=scrollCount # Move the enemies back to their original place (if the window has scrolled them to a different location)
            objectiveLevel2Rect.x+=scrollCount # Move the objective back to its original place (if the window has scrolled it to a different location)
            level3() # Call the level3() function
        
        ########################################################
        
        # Manipulating the jumpTimer variable (ensures that the user cannot jump while in the air)
        if onTop==True: # If the user is not jumping:
            jumpTimer=0 # Set the jumpTimer to 0
        else: # This conditional statement is entered if the value in onTop is False (user is in the air)
            jumpTimer+=1 # Increment the jumpTimer by 1
        
        ########################################################
        
        # Rendering the pause caption onto the pygame window
        pauseCaption=smallFont.render("press esc to pause",True,WHITE,BLACK) # This command creates a text variable, usable by pygame
        captionBox=pauseCaption.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        captionBox.center=(300//2, 1550//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(pauseCaption,captionBox) # This command renders text onto the pygame window
        
        # Rendering the level number onto the pygame window
        levelCaption=smallFont.render("Level Two",True,WHITE,BLACK) # This command creates a text variable, usable by pygame
        levelBox=levelCaption.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        levelBox.center=(175//2, 50//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(levelCaption,levelBox) # This command renders text onto the pygame window
        
        ########################################################
        
        # Main pygame event loop
        for event in pygame.event.get(): # For every one of the events that occur during the pygame execution:
            if event.type==pygame.KEYDOWN: # If a key is pressed down:
                if event.key==pygame.K_ESCAPE: # If the escape key is pressed down:
                    pauseGame() # Call the pauseGame() function()
                if event.key==pygame.K_LEFT: # If the left arrow key is pressed down:
                    userSpriteMoveLeft=True # The player moves left
                if event.key==pygame.K_RIGHT: # If the right arrow key is pressed down:
                    userSpriteMoveRight=True # The player moves right
                if event.key==pygame.K_SPACE: # If the space key is pressed down:
                    if onTop==True: # If the player is on top of a platform:
                        jumpSoundEffect.set_volume(0.5) # Set the volume of the jumpSoundEffect
                        jumpSoundEffect.play() # Play the jumpSoundEffect
                    if jumpTimer<4: # If the jumpTimer is less than 4:
                        forceOfGravity=-16 # Subtract 16 from the forceOfGravity variable (makes the player go up)
            elif event.type==pygame.KEYUP: # If a key is released:
                if event.key==pygame.K_LEFT: # If the left arrow key is released:
                    userSpriteMoveLeft=False # The player stops moving left
                if event.key==pygame.K_RIGHT: # If the right arrow key is released:
                    userSpriteMoveRight=False # The player stops moving right
            elif event.type == pygame.QUIT: # If the window is closed:
                exit() # Terminate the program
        
        ########################################################
        
        # Update the window, and make the game run at 60FPS
        pygame.display.update() # This command updates the pygame window, every frame
        windowClock.tick(window_fps) # This command makes the program run at a designated frame rate (in this case, window_fps is set to 60)




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




# CREATING A FUNCTION FOR LEVEL 3

def level3():
    global userSpriteAsset # This command allows the function to use and change the global variable, "userSpriteAsset"
    global userSpriteNumber # This command allows the function to use and change the global variable, "userSpriteNumber"
    
    # Creating a pause menu for the level
    def pauseGame():
        global userSpriteNumber # This command allows the function to use and change the global variable, "userSpriteNumber"
        
        menuBox=menuBackground.get_rect() # This command creates a pygame Rect object for the menu background image (this helps to position/display it on the screen after)
        menuBox.center=(1600//2, 400//2) # This command centres the pygame Rect object around a single coordinate
        spritePic=pygame.image.load(userSpritesMenu[userSpriteNumber]) # This command uses pygame to load an image (from the file directory), into the game as the character sprite
        
        isGamePaused=True # This variable is used in the creation of a while True loop (see below), when the pauseGame() function is entered, it makes the pause variable true
            
        while isGamePaused: # This loop will iterate forever, while isGamePaused remains True
            # Rendering menu assets/text
            window.blit(menuBackground,menuBox) # This command renders an image onto the pygame window
            pauseTitle=mediumFont.render("PAUSED",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
            pauseBox=pauseTitle.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
            pauseBox.center=(1560//2, 300//2) # This command centres the pygame Rect object around a single coordinate
            window.blit(pauseTitle,pauseBox) # This command renders text onto the pygame window
            spriteBox=spritePic.get_rect() # This command creates a pygame Rect object for an image (this helps to position/display it on the screen after)
            spriteBox.center=(1550//2, 825//2) # This command centres the pygame Rect object around a single coordinate
            window.blit(spritePic,spriteBox) # This command renders text onto the pygame window
            pauseTitle2=smallFont.render("PRESS esc to continue",True,LIGHT_GREY)
            pauseBox2=pauseTitle2.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
            pauseBox2.center=(1560//2, 1395//2) # This command centres the pygame Rect object around a single coordinate
            window.blit(pauseTitle2,pauseBox2) # This command renders text onto the pygame window
            pauseTitle3=smallFont.render("PRESS O to return to menu",True,LIGHT_GREY)
            pauseBox3=pauseTitle3.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
            pauseBox3.center=(1560//2, 1450//2) # This command centres the pygame Rect object around a single coordinate
            window.blit(pauseTitle3,pauseBox3) # This command renders text onto the pygame window
            pygame.display.flip() # This command updates every asset in the current pygame display window
            
            # Pygame event loop for menu
            for event in pygame.event.get(): # For every one of the events that occur during the pygame execution:
                if event.type==pygame.KEYDOWN: # If a key is pressed down:
                    if event.key==pygame.K_ESCAPE: # If the escape key is pressed down:
                        isGamePaused=False # The isGamePaused variable becomes false, effectively leaving the pauseGame() function
                    elif event.key==pygame.K_o: # If the O key is pressed down:
                        isGamePaused=False # The isGamePaused variable becomes false, effectively leaving the pauseGame() function
                        for platform in platformListLevel3: # For every one of the platforms in the window:
                            platform.x+=scrollCount # Move the platforms back to their original place (if the window has scrolled them to a different location)
                        for enemy in enemyListLevel3: # For every one of the enemies in the window:
                            enemy.x+=scrollCount # Move the enemies back to their original place (if the window has scrolled them to a different location)
                        objectiveLevel3Rect.x+=scrollCount # Move the objective box back to its original place (if the window has scrolled it to a different location)
                        gameMenu() # Call the gameMenu() function
                elif event.type == pygame.QUIT: # If the window is closed:
                    exit() # Terminate the program
        
        pygame.display.update() # This command updates the pygame window, every frame
    
    ########################################################
    
    backgroundBox=gameBackgroundLevel3.get_rect() # This command creates a pygame Rect object for the background image (this helps to position/display it on the screen after)
    backgroundBox.center=(1600//2, 800//2) # This command centres the pygame Rect object around a single coordinate
    
    # Create location, moving, gravity, and rect variables for the user's sprite, to make writing collision code and other game aspects easier
    # Defining the userSprite's abilities and parameters
    userSpriteMoveLeft=False # The userSpriteMoveLeft variable is set to False
    userSpriteMoveRight=False # The userSpriteMoveRight variable is set to False
    jumpTimer=0 # The jumpTimer variable for the userSprite is set to 0
    userSpriteLocationXY=[200,600] # This creates the player's starting location in the pygame window [x,y]
    forceOfGravity=0 # The forceOfGravity variable for the userSprite is set to 0
    userSpriteRect=pygame.Rect(userSpriteLocationXY[0],userSpriteLocationXY[1],userSpriteAsset.get_width(),userSpriteAsset.get_height()) # This command creates a pygame Rect object for the userSprite (to check for rect collisions later)
    
    # Creating a variable to aid in window scrolling throughout the level
    scrollCount=0 # The scrollCount variable (for the objects in the pygame window) is set to 0
    
    ########################################################
    
    # Main game loop
    while True: # This loops forever, unless a certain event breaks the loop
        # Rendering images onto the pygame window
        window.blit(gameBackgroundLevel3,backgroundBox) # This command renders an image onto the pygame window
        window.blit(userSpriteAsset,(userSpriteLocationXY)) # This command renders the userSprite onto the pygame window, in its starting location
        
        # Rendering enemies onto screen
        for enemy in enemyListLevel3: # For every one of the enemies in the window:
            window.blit(pygame.image.load(enemySpriteAsset),enemy) # This command renders the enemy onto the pygame window
            
        # Rendering platforms onto pygame window
        for platform in platformListLevel3: # For every one of the platforms in the window:
            pygame.draw.rect(window,BLACK,platform) # This command renders the platform onto the pygame window
        
        # Rendering the objective box onto pygame window
        window.blit(objectiveSpriteAsset,objectiveLevel3Rect) # This command renders the objective onto the pygame window
        
        ########################################################
        
        # Scrolling the pygame window
        if userSpriteLocationXY[0]>(window_resolution[0]/4) and (userSpriteMoveRight==True) and (userSpriteLocationXY[0]+userSpriteAsset.get_width()<=window_resolution[0]): # If the player is moving right, and they are on the right 2/3 of the screen:
            scrollCount+=10 # Increment the scrollCount variable by 5
            for platform in platformListLevel3: # For every one of the platforms in the window:
                platform.x-=10 # Move the platform 5 pixels left
            for enemy in enemyListLevel3: # For every one of the enemies in the window:
                enemy.x-=10 # Move the enemy 5 pixels left
            objectiveLevel3Rect.x-=10 # Move the objective 5 pixels left
        
        ########################################################
        
        # Applying/Managing player sprite movement on the X axis
        if userSpriteMoveLeft==True: # If the user is moving left:
            userSpriteLocationXY[0]-=8 # Move the userSprite 8 pixels to the left:
            userSpriteAsset=pygame.image.load(userSpriteAssets[userSpriteNumber][1]) # Display the user's image (for moving left)
        if userSpriteMoveRight==True: # If the user is moving right:
            userSpriteLocationXY[0]+=8 # Move the userSprite 8 pixels to the right:
            userSpriteAsset=pygame.image.load(userSpriteAssets[userSpriteNumber][2]) # Display the user's image (for moving right)
        if (userSpriteMoveLeft==False) and (userSpriteMoveRight==False): # If the user is not moving left or right:
            userSpriteAsset=pygame.image.load(userSpriteAssets[userSpriteNumber][0]) # Display the user's image (for facing forward)
        
        # Applying/Managing forceOfGravity variable
        userSpriteLocationXY[1]+=forceOfGravity # Increment the user's y coordinate by the forceOfGravity value
        forceOfGravity+=0.8 # Increment the forceOfGravity value by 0.8
        if forceOfGravity>16: # If the forceOfGravity value is over 16:
            forceOfGravity=16 # Set the forceOfGravity value to 16 (gravity strength cap=16)
        
        # Reloading the userSpriteRect object in the user's new location (after movement)
        userSpriteRect.x=userSpriteLocationXY[0] # Update the X position of the user Rect object to the X position of the user image
        userSpriteRect.y=userSpriteLocationXY[1] # Update the Y position of the user Rect object to the Y position of the user image
        
        ########################################################
        
        # Check for collisions with the left/right screen borders
        if (userSpriteLocationXY[0]+userSpriteAsset.get_width())>window_resolution[0]: # If the user collides with the right side of the screen:
            userSpriteLocationXY[0]=window_resolution[0]-userSpriteAsset.get_width() # Set the user's location to the right side of the screen (but not off it)
        if userSpriteLocationXY[0]<0: # If the user collides with the left side of the screen:
            userSpriteLocationXY[0]=0 # Set the user's location to the left side of the screen (but not off it)
        
        # Check if player falls down out of screen (if so, game over)
        if (userSpriteLocationXY[1]+userSpriteAsset.get_height())>window_resolution[1]: # If the user collides with the bottom edge of the screen:
            hitSoundEffect.set_volume(1.5) # Set the volume of the hitSoundEffect
            hitSoundEffect.play() # Play the hitSoundEffect
            for platform in platformListLevel3: # For every one of the platforms in the window:
                platform.x+=scrollCount # Move the platforms back to their original place (if the window has scrolled them to a different location)
            for enemy in enemyListLevel3: # For every one of the enemies in the window:
                enemy.x+=scrollCount # Move the enemies back to their original place (if the window has scrolled them to a different location)
            objectiveLevel3Rect.x+=scrollCount # Move the objective back to its original place (if the window has scrolled it to a different location)
            gameOverMenu() # Call the gameOverMenu() function
        
        #Check for userSprite collisions with platforms
        onTop=False # The onTop variable is set to False
        onBottom=False # The onBottom variable is set to False
        for platform in platformListLevel3: # For every one of the platforms in the window (user and platform):
            platformLocationX=platform.x # Define a variable for the platform Rect object's X location
            platformLocationY=platform.y # Define a variable for the platform Rect object's Y location
            if userSpriteRect.colliderect(platform): # If two pygame Rect objects collide:
                # Colliding with top of the platform
                if (userSpriteLocationXY[1] + userSpriteAsset.get_height() >= platformLocationY) and (userSpriteLocationXY[1] + userSpriteAsset.get_height() <= platformLocationY + platform.height): # If the user collides with the top of the platform:
                    userSpriteLocationXY[1]=platformLocationY-userSpriteAsset.get_height() # Set the user's location to the top of the platform
                    onTop=True # The onTop variable is set to True
                    forceOfGravity=0 # The forceOfGravity variable is set to 0 (stops the user from shooting down, if they stand on the platform for a while, and then jump off of it)
                # Colliding with bottom of the platform
                if (userSpriteLocationXY[1] <= platformLocationY + platform.height) and (userSpriteLocationXY[1] >= platformLocationY): # If the user collides with the bottom of the platform:
                    userSpriteLocationXY[1]=platformLocationY + platform.height # Set the user's location to the bottom of the platform
                    onBottom=True # The onBottom variable is set to True
                
                if (onTop==False) and (onBottom==False): # If the onTop and onBottom variables are set to False (the user is not colliding with the top or bottom of the platform):
                    # Colliding with left side of the platform
                    if (userSpriteLocationXY[0] + userSpriteAsset.get_width() >= platformLocationX) and (userSpriteLocationXY[0] + userSpriteAsset.get_width() <= platformLocationX + platform.width): # If the user collides with the left side of the platform:
                        userSpriteLocationXY[0] = platformLocationX - userSpriteAsset.get_width() # Set the user's location to the left side of the platform
                    # Colliding with right side of the platform
                    if (userSpriteLocationXY[0] <= platformLocationX + platform.width) and (userSpriteLocationXY[0] >= platformLocationX): # If the user collides with the right side of the platform:
                        userSpriteLocationXY[0] = platformLocationX + platform.width # Set the user's location to the right side of the platform
        
        # Check for userSprite collisions with enemies
        for enemy in enemyListLevel3: # For every one of the enemies in the window:
            enemyLocationX=enemy.x # Define a variable for the emeny Rect object's X location
            enemyLocationY=enemy.y # Define a variable for the emeny Rect object's Y location
            if userSpriteRect.colliderect(enemy): # If two pygame Rect objects collide (user and enemy):
                hitSoundEffect.set_volume(1.5) # Set the volume of the hitSoundEffect
                hitSoundEffect.play() # Play the hitSoundEffect
                for platform in platformListLevel3: # For every one of the platforms in the window:
                    platform.x+=scrollCount # Move the platforms back to their original place (if the window has scrolled them to a different location)
                for enemy in enemyListLevel3: # For every one of the enemies in the window:
                    enemy.x+=scrollCount # Move the enemies back to their original place (if the window has scrolled them to a different location)
                objectiveLevel3Rect.x+=scrollCount # Move the objective back to its original place (if the window has scrolled it to a different location)
                gameOverMenu() # Call the gameOverMenu() function
        
        # Check for userSprite collisions with objective
        if userSpriteRect.colliderect(objectiveLevel3Rect): # If two pygame Rect objects collide (user and objective):
            levelCompleteSoundEffect.set_volume(0.75) # Set the volume of the levelCompleteSoundEffect
            levelCompleteSoundEffect.play() # Play the levelCompleteSoundEffect
            for platform in platformListLevel3: # For every one of the platforms in the window:
                platform.x+=scrollCount # Move the platforms back to their original place (if the window has scrolled them to a different location)
            for enemy in enemyListLevel3: # For every one of the enemies in the window:
                enemy.x+=scrollCount # Move the enemies back to their original place (if the window has scrolled them to a different location)
            objectiveLevel3Rect.x+=scrollCount # Move the objective back to its original place (if the window has scrolled it to a different location)
            level4() # Call the level4() function
        
        ########################################################
        
        # Manipulating the jumpTimer variable (ensures that the user cannot jump while in the air)
        if onTop==True: # If the user is not jumping:
            jumpTimer=0 # Set the jumpTimer to 0
        else: # This conditional statement is entered if the value in onTop is False (user is in the air)
            jumpTimer+=1 # Increment the jumpTimer by 1
        
        ########################################################
        
        # Rendering the pause caption onto the pygame window
        pauseCaption=smallFont.render("press esc to pause",True,WHITE,BLACK) # This command creates a text variable, usable by pygame
        captionBox=pauseCaption.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        captionBox.center=(300//2, 1550//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(pauseCaption,captionBox) # This command renders text onto the pygame window
        
        # Rendering the level number onto the pygame window
        levelCaption=smallFont.render("Level Three",True,WHITE,BLACK) # This command creates a text variable, usable by pygame
        levelBox=levelCaption.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        levelBox.center=(175//2, 50//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(levelCaption,levelBox) # This command renders text onto the pygame window
        
        ########################################################
        
        # Main pygame event loop
        for event in pygame.event.get(): # For every one of the events that occur during the pygame execution:
            if event.type==pygame.KEYDOWN: # If a key is pressed down:
                if event.key==pygame.K_ESCAPE: # If the escape key is pressed down:
                    pauseGame() # Call the pauseGame() function()
                if event.key==pygame.K_LEFT: # If the left arrow key is pressed down:
                    userSpriteMoveLeft=True # The player moves left
                if event.key==pygame.K_RIGHT: # If the right arrow key is pressed down:
                    userSpriteMoveRight=True # The player moves right
                if event.key==pygame.K_SPACE: # If the space key is pressed down:
                    if onTop==True: # If the player is on top of a platform:
                        jumpSoundEffect.set_volume(0.5) # Set the volume of the jumpSoundEffect
                        jumpSoundEffect.play() # Play the jumpSoundEffect
                    if jumpTimer<4: # If the jumpTimer is less than 4:
                        forceOfGravity=-16 # Subtract 16 from the forceOfGravity variable (makes the player go up)
            elif event.type==pygame.KEYUP: # If a key is released:
                if event.key==pygame.K_LEFT: # If the left arrow key is released:
                    userSpriteMoveLeft=False # The player stops moving left
                if event.key==pygame.K_RIGHT: # If the right arrow key is released:
                    userSpriteMoveRight=False # The player stops moving right
            elif event.type == pygame.QUIT: # If the window is closed:
                exit() # Terminate the program
        
        ########################################################
        
        # Update the window, and make the game run at 60FPS
        pygame.display.update() # This command updates the pygame window, every frame
        windowClock.tick(window_fps) # This command makes the program run at a designated frame rate (in this case, window_fps is set to 60)




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




# CREATING A FUNCTION FOR LEVEL 4

def level4():
    global userSpriteAsset # This command allows the function to use and change the global variable, "userSpriteAsset"
    global userSpriteNumber # This command allows the function to use and change the global variable, "userSpriteNumber"
    
    # Creating a pause menu for the level
    def pauseGame():
        global userSpriteNumber # This command allows the function to use and change the global variable, "userSpriteNumber"
        
        menuBox=menuBackground.get_rect() # This command creates a pygame Rect object for the menu background image (this helps to position/display it on the screen after)
        menuBox.center=(1600//2, 400//2) # This command centres the pygame Rect object around a single coordinate
        spritePic=pygame.image.load(userSpritesMenu[userSpriteNumber]) # This command uses pygame to load an image (from the file directory), into the game as the character sprite
        
        isGamePaused=True # This variable is used in the creation of a while True loop (see below), when the pauseGame() function is entered, it makes the pause variable true
            
        while isGamePaused: # This loop will iterate forever, while isGamePaused remains True
            # Rendering menu assets/text
            window.blit(menuBackground,menuBox) # This command renders an image onto the pygame window
            pauseTitle=mediumFont.render("PAUSED",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
            pauseBox=pauseTitle.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
            pauseBox.center=(1560//2, 300//2) # This command centres the pygame Rect object around a single coordinate
            window.blit(pauseTitle,pauseBox) # This command renders text onto the pygame window
            spriteBox=spritePic.get_rect() # This command creates a pygame Rect object for an image (this helps to position/display it on the screen after)
            spriteBox.center=(1550//2, 825//2) # This command centres the pygame Rect object around a single coordinate
            window.blit(spritePic,spriteBox) # This command renders text onto the pygame window
            pauseTitle2=smallFont.render("PRESS esc to continue",True,LIGHT_GREY)
            pauseBox2=pauseTitle2.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
            pauseBox2.center=(1560//2, 1395//2) # This command centres the pygame Rect object around a single coordinate
            window.blit(pauseTitle2,pauseBox2) # This command renders text onto the pygame window
            pauseTitle3=smallFont.render("PRESS O to return to menu",True,LIGHT_GREY)
            pauseBox3=pauseTitle3.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
            pauseBox3.center=(1560//2, 1450//2) # This command centres the pygame Rect object around a single coordinate
            window.blit(pauseTitle3,pauseBox3) # This command renders text onto the pygame window
            pygame.display.flip() # This command updates every asset in the current pygame display window
            
            # Pygame event loop for menu
            for event in pygame.event.get(): # For every one of the events that occur during the pygame execution:
                if event.type==pygame.KEYDOWN: # If a key is pressed down:
                    if event.key==pygame.K_ESCAPE: # If the escape key is pressed down:
                        isGamePaused=False # The isGamePaused variable becomes false, effectively leaving the pauseGame() function
                    elif event.key==pygame.K_o: # If the O key is pressed down:
                        isGamePaused=False # The isGamePaused variable becomes false, effectively leaving the pauseGame() function
                        for platform in platformListLevel4: # For every one of the platforms in the window:
                            platform.x+=scrollCount # Move the platforms back to their original place (if the window has scrolled them to a different location)
                        for enemy in enemyListLevel4: # For every one of the enemies in the window:
                            enemy.x+=scrollCount # Move the enemies back to their original place (if the window has scrolled them to a different location)
                        objectiveLevel4Rect.x+=scrollCount # Move the objective box back to its original place (if the window has scrolled it to a different location)
                        gameMenu() # Call the gameMenu() function
                elif event.type == pygame.QUIT: # If the window is closed:
                    exit() # Terminate the program
        
        pygame.display.update() # This command updates the pygame window, every frame
    
    ########################################################
    
    backgroundBox=gameBackgroundLevel4.get_rect() # This command creates a pygame Rect object for the background image (this helps to position/display it on the screen after)
    backgroundBox.center=(1600//2, 800//2) # This command centres the pygame Rect object around a single coordinate
    
    # Create location, moving, gravity, and rect variables for the user's sprite, to make writing collision code and other game aspects easier
    # Defining the userSprite's abilities and parameters
    userSpriteMoveLeft=False # The userSpriteMoveLeft variable is set to False
    userSpriteMoveRight=False # The userSpriteMoveRight variable is set to False
    jumpTimer=0 # The jumpTimer variable for the userSprite is set to 0
    userSpriteLocationXY=[200,600] # This creates the player's starting location in the pygame window [x,y]
    forceOfGravity=0 # The forceOfGravity variable for the userSprite is set to 0
    userSpriteRect=pygame.Rect(userSpriteLocationXY[0],userSpriteLocationXY[1],userSpriteAsset.get_width(),userSpriteAsset.get_height()) # This command creates a pygame Rect object for the userSprite (to check for rect collisions later)
    
    # Creating a variable to aid in window scrolling throughout the level
    scrollCount=0 # The scrollCount variable (for the objects in the pygame window) is set to 0
    
    ########################################################
    
    # Main game loop
    while True: # This loops forever, unless a certain event breaks the loop
        # Rendering images onto the pygame window
        window.blit(gameBackgroundLevel4,backgroundBox) # This command renders an image onto the pygame window
        window.blit(userSpriteAsset,(userSpriteLocationXY)) # This command renders the userSprite onto the pygame window, in its starting location
        
        # Rendering enemies onto screen
        for enemy in enemyListLevel4: # For every one of the enemies in the window:
            window.blit(pygame.image.load(enemySpriteAsset),enemy) # This command renders the enemy onto the pygame window
            
        # Rendering platforms onto pygame window
        for platform in platformListLevel4: # For every one of the platforms in the window:
            pygame.draw.rect(window,BLACK,platform) # This command renders the platform onto the pygame window
        
        # Rendering the objective box onto pygame window
        window.blit(objectiveSpriteAsset,objectiveLevel4Rect) # This command renders the objective onto the pygame window
        
        ########################################################
        
        # Scrolling the pygame window
        if userSpriteLocationXY[0]>(window_resolution[0]/4) and (userSpriteMoveRight==True) and (userSpriteLocationXY[0]+userSpriteAsset.get_width()<=window_resolution[0]): # If the player is moving right, and they are on the right 2/3 of the screen:
            scrollCount+=5 # Increment the scrollCount variable by 5
            for platform in platformListLevel4: # For every one of the platforms in the window:
                platform.x-=5 # Move the platform 5 pixels left
            for enemy in enemyListLevel4: # For every one of the enemies in the window:
                enemy.x-=5 # Move the enemy 5 pixels left
            objectiveLevel4Rect.x-=5 # Move the objective 5 pixels left
        
        ########################################################
        
        # Applying/Managing player sprite movement on the X axis
        if userSpriteMoveLeft==True: # If the user is moving left:
            userSpriteLocationXY[0]-=8 # Move the userSprite 8 pixels to the left:
            userSpriteAsset=pygame.image.load(userSpriteAssets[userSpriteNumber][1]) # Display the user's image (for moving left)
        if userSpriteMoveRight==True: # If the user is moving right:
            userSpriteLocationXY[0]+=8 # Move the userSprite 8 pixels to the right:
            userSpriteAsset=pygame.image.load(userSpriteAssets[userSpriteNumber][2]) # Display the user's image (for moving right)
        if (userSpriteMoveLeft==False) and (userSpriteMoveRight==False): # If the user is not moving left or right:
            userSpriteAsset=pygame.image.load(userSpriteAssets[userSpriteNumber][0]) # Display the user's image (for facing forward)
        
        # Applying/Managing forceOfGravity variable
        userSpriteLocationXY[1]+=forceOfGravity # Increment the user's y coordinate by the forceOfGravity value
        forceOfGravity+=0.8 # Increment the forceOfGravity value by 0.8
        if forceOfGravity>16: # If the forceOfGravity value is over 16:
            forceOfGravity=16 # Set the forceOfGravity value to 16 (gravity strength cap=16)
        
        # Reloading the userSpriteRect object in the user's new location (after movement)
        userSpriteRect.x=userSpriteLocationXY[0] # Update the X position of the user Rect object to the X position of the user image
        userSpriteRect.y=userSpriteLocationXY[1] # Update the Y position of the user Rect object to the Y position of the user image
        
        ########################################################
        
        # Check for collisions with the left/right screen borders
        if (userSpriteLocationXY[0]+userSpriteAsset.get_width())>window_resolution[0]: # If the user collides with the right side of the screen:
            userSpriteLocationXY[0]=window_resolution[0]-userSpriteAsset.get_width() # Set the user's location to the right side of the screen (but not off it)
        if userSpriteLocationXY[0]<0: # If the user collides with the left side of the screen:
            userSpriteLocationXY[0]=0 # Set the user's location to the left side of the screen (but not off it)
        
        # Check if player falls down out of screen (if so, game over)
        if (userSpriteLocationXY[1]+userSpriteAsset.get_height())>window_resolution[1]: # If the user collides with the bottom edge of the screen:
            hitSoundEffect.set_volume(1.5) # Set the volume of the hitSoundEffect
            hitSoundEffect.play() # Play the hitSoundEffect
            for platform in platformListLevel4: # For every one of the platforms in the window:
                platform.x+=scrollCount # Move the platforms back to their original place (if the window has scrolled them to a different location)
            for enemy in enemyListLevel4: # For every one of the enemies in the window:
                enemy.x+=scrollCount # Move the enemies back to their original place (if the window has scrolled them to a different location)
            objectiveLevel4Rect.x+=scrollCount # Move the objective back to its original place (if the window has scrolled it to a different location)
            gameOverMenu() # Call the gameOverMenu() function
        
        #Check for userSprite collisions with platforms
        onTop=False # The onTop variable is set to False
        onBottom=False # The onBottom variable is set to False
        for platform in platformListLevel4: # For every one of the platforms in the window (user and platform):
            platformLocationX=platform.x # Define a variable for the platform Rect object's X location
            platformLocationY=platform.y # Define a variable for the platform Rect object's Y location
            if userSpriteRect.colliderect(platform): # If two pygame Rect objects collide:
                # Colliding with top of the platform
                if (userSpriteLocationXY[1] + userSpriteAsset.get_height() >= platformLocationY) and (userSpriteLocationXY[1] + userSpriteAsset.get_height() <= platformLocationY + platform.height): # If the user collides with the top of the platform:
                    userSpriteLocationXY[1]=platformLocationY-userSpriteAsset.get_height() # Set the user's location to the top of the platform
                    onTop=True # The onTop variable is set to True
                    forceOfGravity=0 # The forceOfGravity variable is set to 0 (stops the user from shooting down, if they stand on the platform for a while, and then jump off of it)
                # Colliding with bottom of the platform
                if (userSpriteLocationXY[1] <= platformLocationY + platform.height) and (userSpriteLocationXY[1] >= platformLocationY): # If the user collides with the bottom of the platform:
                    userSpriteLocationXY[1]=platformLocationY + platform.height # Set the user's location to the bottom of the platform
                    onBottom=True # The onBottom variable is set to True
                
                if (onTop==False) and (onBottom==False): # If the onTop and onBottom variables are set to False (the user is not colliding with the top or bottom of the platform):
                    # Colliding with left side of the platform
                    if (userSpriteLocationXY[0] + userSpriteAsset.get_width() >= platformLocationX) and (userSpriteLocationXY[0] + userSpriteAsset.get_width() <= platformLocationX + platform.width): # If the user collides with the left side of the platform:
                        userSpriteLocationXY[0] = platformLocationX - userSpriteAsset.get_width() # Set the user's location to the left side of the platform
                    # Colliding with right side of the platform
                    if (userSpriteLocationXY[0] <= platformLocationX + platform.width) and (userSpriteLocationXY[0] >= platformLocationX): # If the user collides with the right side of the platform:
                        userSpriteLocationXY[0] = platformLocationX + platform.width # Set the user's location to the right side of the platform
        
        # Check for userSprite collisions with enemies
        for enemy in enemyListLevel4: # For every one of the enemies in the window:
            enemyLocationX=enemy.x # Define a variable for the emeny Rect object's X location
            enemyLocationY=enemy.y # Define a variable for the emeny Rect object's Y location
            if userSpriteRect.colliderect(enemy): # If two pygame Rect objects collide (user and enemy):
                hitSoundEffect.set_volume(1.5) # Set the volume of the hitSoundEffect
                hitSoundEffect.play() # Play the hitSoundEffect
                for platform in platformListLevel4: # For every one of the platforms in the window:
                    platform.x+=scrollCount # Move the platforms back to their original place (if the window has scrolled them to a different location)
                for enemy in enemyListLevel4: # For every one of the enemies in the window:
                    enemy.x+=scrollCount # Move the enemies back to their original place (if the window has scrolled them to a different location)
                objectiveLevel4Rect.x+=scrollCount # Move the objective back to its original place (if the window has scrolled it to a different location)
                gameOverMenu() # Call the gameOverMenu() function
        
        # Check for userSprite collisions with objective
        if userSpriteRect.colliderect(objectiveLevel4Rect): # If two pygame Rect objects collide (user and objective):
            levelCompleteSoundEffect.set_volume(0.75) # Set the volume of the levelCompleteSoundEffect
            levelCompleteSoundEffect.play() # Play the levelCompleteSoundEffect
            for platform in platformListLevel4: # For every one of the platforms in the window:
                platform.x+=scrollCount # Move the platforms back to their original place (if the window has scrolled them to a different location)
            for enemy in enemyListLevel4: # For every one of the enemies in the window:
                enemy.x+=scrollCount # Move the enemies back to their original place (if the window has scrolled them to a different location)
            objectiveLevel4Rect.x+=scrollCount # Move the objective back to its original place (if the window has scrolled it to a different location)
            level5() # Call the level5() function
        
        ########################################################
        
        # Manipulating the jumpTimer variable (ensures that the user cannot jump while in the air)
        if onTop==True: # If the user is not jumping:
            jumpTimer=0 # Set the jumpTimer to 0
        else: # This conditional statement is entered if the value in onTop is False (user is in the air)
            jumpTimer+=1 # Increment the jumpTimer by 1
        
        ########################################################
        
        # Rendering the pause caption onto the pygame window
        pauseCaption=smallFont.render("press esc to pause",True,WHITE,BLACK) # This command creates a text variable, usable by pygame
        captionBox=pauseCaption.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        captionBox.center=(300//2, 1550//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(pauseCaption,captionBox) # This command renders text onto the pygame window
        
        # Rendering the level number onto the pygame window
        levelCaption=smallFont.render("Level Four",True,WHITE,BLACK) # This command creates a text variable, usable by pygame
        levelBox=levelCaption.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        levelBox.center=(175//2, 50//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(levelCaption,levelBox) # This command renders text onto the pygame window
        
        ########################################################
        
        # Main pygame event loop
        for event in pygame.event.get(): # For every one of the events that occur during the pygame execution:
            if event.type==pygame.KEYDOWN: # If a key is pressed down:
                if event.key==pygame.K_ESCAPE: # If the escape key is pressed down:
                    pauseGame() # Call the pauseGame() function()
                if event.key==pygame.K_LEFT: # If the left arrow key is pressed down:
                    userSpriteMoveLeft=True # The player moves left
                if event.key==pygame.K_RIGHT: # If the right arrow key is pressed down:
                    userSpriteMoveRight=True # The player moves right
                if event.key==pygame.K_SPACE: # If the space key is pressed down:
                    if onTop==True: # If the player is on top of a platform:
                        jumpSoundEffect.set_volume(0.5) # Set the volume of the jumpSoundEffect
                        jumpSoundEffect.play() # Play the jumpSoundEffect
                    if jumpTimer<4: # If the jumpTimer is less than 4:
                        forceOfGravity=-16 # Subtract 16 from the forceOfGravity variable (makes the player go up)
            elif event.type==pygame.KEYUP: # If a key is released:
                if event.key==pygame.K_LEFT: # If the left arrow key is released:
                    userSpriteMoveLeft=False # The player stops moving left
                if event.key==pygame.K_RIGHT: # If the right arrow key is released:
                    userSpriteMoveRight=False # The player stops moving right
            elif event.type == pygame.QUIT: # If the window is closed:
                exit() # Terminate the program
        
        ########################################################
        
        # Update the window, and make the game run at 60FPS
        pygame.display.update() # This command updates the pygame window, every frame
        windowClock.tick(window_fps) # This command makes the program run at a designated frame rate (in this case, window_fps is set to 60)




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




# CREATING A FUNCTION FOR LEVEL 5

def level5():
    global userSpriteAsset # This command allows the function to use and change the global variable, "userSpriteAsset"
    global userSpriteNumber # This command allows the function to use and change the global variable, "userSpriteNumber"
    
    # Creating a pause menu for the level
    def pauseGame():
        global userSpriteNumber # This command allows the function to use and change the global variable, "userSpriteNumber"
        
        menuBox=menuBackground.get_rect() # This command creates a pygame Rect object for the menu background image (this helps to position/display it on the screen after)
        menuBox.center=(1600//2, 400//2) # This command centres the pygame Rect object around a single coordinate
        spritePic=pygame.image.load(userSpritesMenu[userSpriteNumber]) # This command uses pygame to load an image (from the file directory), into the game as the character sprite
        
        isGamePaused=True # This variable is used in the creation of a while True loop (see below), when the pauseGame() function is entered, it makes the pause variable true
            
        while isGamePaused: # This loop will iterate forever, while isGamePaused remains True
            # Rendering menu assets/text
            window.blit(menuBackground,menuBox) # This command renders an image onto the pygame window
            pauseTitle=mediumFont.render("PAUSED",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
            pauseBox=pauseTitle.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
            pauseBox.center=(1560//2, 300//2) # This command centres the pygame Rect object around a single coordinate
            window.blit(pauseTitle,pauseBox) # This command renders text onto the pygame window
            spriteBox=spritePic.get_rect() # This command creates a pygame Rect object for an image (this helps to position/display it on the screen after)
            spriteBox.center=(1550//2, 825//2) # This command centres the pygame Rect object around a single coordinate
            window.blit(spritePic,spriteBox) # This command renders text onto the pygame window
            pauseTitle2=smallFont.render("PRESS esc to continue",True,LIGHT_GREY)
            pauseBox2=pauseTitle2.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
            pauseBox2.center=(1560//2, 1395//2) # This command centres the pygame Rect object around a single coordinate
            window.blit(pauseTitle2,pauseBox2) # This command renders text onto the pygame window
            pauseTitle3=smallFont.render("PRESS O to return to menu",True,LIGHT_GREY)
            pauseBox3=pauseTitle3.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
            pauseBox3.center=(1560//2, 1450//2) # This command centres the pygame Rect object around a single coordinate
            window.blit(pauseTitle3,pauseBox3) # This command renders text onto the pygame window
            pygame.display.flip() # This command updates every asset in the current pygame display window
            
            # Pygame event loop for menu
            for event in pygame.event.get(): # For every one of the events that occur during the pygame execution:
                if event.type==pygame.KEYDOWN: # If a key is pressed down:
                    if event.key==pygame.K_ESCAPE: # If the escape key is pressed down:
                        isGamePaused=False # The isGamePaused variable becomes false, effectively leaving the pauseGame() function
                    elif event.key==pygame.K_o: # If the O key is pressed down:
                        isGamePaused=False # The isGamePaused variable becomes false, effectively leaving the pauseGame() function
                        for platform in platformListLevel5: # For every one of the platforms in the window:
                            platform.x+=scrollCount # Move the platforms back to their original place (if the window has scrolled them to a different location)
                        for enemy in enemyListLevel5: # For every one of the enemies in the window:
                            enemy.x+=scrollCount # Move the enemies back to their original place (if the window has scrolled them to a different location)
                        objectiveLevel5Rect.x+=scrollCount # Move the objective box back to its original place (if the window has scrolled it to a different location)
                        gameMenu() # Call the gameMenu() function
                elif event.type == pygame.QUIT: # If the window is closed:
                    exit() # Terminate the program
        
        pygame.display.update() # This command updates the pygame window, every frame
    
    ########################################################
    
    backgroundBox=gameBackgroundLevel5.get_rect() # This command creates a pygame Rect object for the background image (this helps to position/display it on the screen after)
    backgroundBox.center=(1600//2, 800//2) # This command centres the pygame Rect object around a single coordinate
    
    # Create location, moving, gravity, and rect variables for the user's sprite, to make writing collision code and other game aspects easier
    # Defining the userSprite's abilities and parameters
    userSpriteMoveLeft=False # The userSpriteMoveLeft variable is set to False
    userSpriteMoveRight=False # The userSpriteMoveRight variable is set to False
    jumpTimer=0 # The jumpTimer variable for the userSprite is set to 0
    userSpriteLocationXY=[200,600] # This creates the player's starting location in the pygame window [x,y]
    forceOfGravity=0 # The forceOfGravity variable for the userSprite is set to 0
    userSpriteRect=pygame.Rect(userSpriteLocationXY[0],userSpriteLocationXY[1],userSpriteAsset.get_width(),userSpriteAsset.get_height()) # This command creates a pygame Rect object for the userSprite (to check for rect collisions later)
    
    # Creating a variable to aid in window scrolling throughout the level
    scrollCount=0 # The scrollCount variable (for the objects in the pygame window) is set to 0
    
    ########################################################
    
    # Main game loop
    while True: # This loops forever, unless a certain event breaks the loop
        # Rendering images onto the pygame window
        window.blit(gameBackgroundLevel5,backgroundBox) # This command renders an image onto the pygame window
        window.blit(userSpriteAsset,(userSpriteLocationXY)) # This command renders the userSprite onto the pygame window, in its starting location
        
        # Rendering enemies onto screen
        for enemy in enemyListLevel5: # For every one of the enemies in the window:
            window.blit(pygame.image.load(enemySpriteAsset),enemy) # This command renders the enemy onto the pygame window
            
        # Rendering platforms onto pygame window
        for platform in platformListLevel5: # For every one of the platforms in the window:
            pygame.draw.rect(window,BLACK,platform) # This command renders the platform onto the pygame window
        
        # Rendering the objective box onto pygame window
        window.blit(objectiveSpriteAsset,objectiveLevel5Rect) # This command renders the objective onto the pygame window
        
        ########################################################
        
        # Scrolling the pygame window
        if userSpriteLocationXY[0]>(window_resolution[0]/4) and (userSpriteMoveRight==True) and (userSpriteLocationXY[0]+userSpriteAsset.get_width()<=window_resolution[0]): # If the player is moving right, and they are on the right 2/3 of the screen:
            scrollCount+=5 # Increment the scrollCount variable by 5
            for platform in platformListLevel5: # For every one of the platforms in the window:
                platform.x-=5 # Move the platform 5 pixels left
            for enemy in enemyListLevel5: # For every one of the enemies in the window:
                enemy.x-=5 # Move the enemy 5 pixels left
            objectiveLevel5Rect.x-=5 # Move the objective 5 pixels left
        
        ########################################################
        
        # Applying/Managing player sprite movement on the X axis
        if userSpriteMoveLeft==True: # If the user is moving left:
            userSpriteLocationXY[0]-=8 # Move the userSprite 8 pixels to the left:
            userSpriteAsset=pygame.image.load(userSpriteAssets[userSpriteNumber][1]) # Display the user's image (for moving left)
        if userSpriteMoveRight==True: # If the user is moving right:
            userSpriteLocationXY[0]+=8 # Move the userSprite 8 pixels to the right:
            userSpriteAsset=pygame.image.load(userSpriteAssets[userSpriteNumber][2]) # Display the user's image (for moving right)
        if (userSpriteMoveLeft==False) and (userSpriteMoveRight==False): # If the user is not moving left or right:
            userSpriteAsset=pygame.image.load(userSpriteAssets[userSpriteNumber][0]) # Display the user's image (for facing forward)
        
        # Applying/Managing forceOfGravity variable
        userSpriteLocationXY[1]+=forceOfGravity # Increment the user's y coordinate by the forceOfGravity value
        forceOfGravity+=0.8 # Increment the forceOfGravity value by 0.8
        if forceOfGravity>16: # If the forceOfGravity value is over 16:
            forceOfGravity=16 # Set the forceOfGravity value to 16 (gravity strength cap=16)
        
        # Reloading the userSpriteRect object in the user's new location (after movement)
        userSpriteRect.x=userSpriteLocationXY[0] # Update the X position of the user Rect object to the X position of the user image
        userSpriteRect.y=userSpriteLocationXY[1] # Update the Y position of the user Rect object to the Y position of the user image
        
        ########################################################
        
        # Check for collisions with the left/right screen borders
        if (userSpriteLocationXY[0]+userSpriteAsset.get_width())>window_resolution[0]: # If the user collides with the right side of the screen:
            userSpriteLocationXY[0]=window_resolution[0]-userSpriteAsset.get_width() # Set the user's location to the right side of the screen (but not off it)
        if userSpriteLocationXY[0]<0: # If the user collides with the left side of the screen:
            userSpriteLocationXY[0]=0 # Set the user's location to the left side of the screen (but not off it)
        
        # Check if player falls down out of screen (if so, game over)
        if (userSpriteLocationXY[1]+userSpriteAsset.get_height())>window_resolution[1]: # If the user collides with the bottom edge of the screen:
            hitSoundEffect.set_volume(1.5) # Set the volume of the hitSoundEffect
            hitSoundEffect.play() # Play the hitSoundEffect
            for platform in platformListLevel5: # For every one of the platforms in the window:
                platform.x+=scrollCount # Move the platforms back to their original place (if the window has scrolled them to a different location)
            for enemy in enemyListLevel5: # For every one of the enemies in the window:
                enemy.x+=scrollCount # Move the enemies back to their original place (if the window has scrolled them to a different location)
            objectiveLevel5Rect.x+=scrollCount # Move the objective back to its original place (if the window has scrolled it to a different location)
            gameOverMenu() # Call the gameOverMenu() function
        
        #Check for userSprite collisions with platforms
        onTop=False # The onTop variable is set to False
        onBottom=False # The onBottom variable is set to False
        for platform in platformListLevel5: # For every one of the platforms in the window (user and platform):
            platformLocationX=platform.x # Define a variable for the platform Rect object's X location
            platformLocationY=platform.y # Define a variable for the platform Rect object's Y location
            if userSpriteRect.colliderect(platform): # If two pygame Rect objects collide:
                # Colliding with top of the platform
                if (userSpriteLocationXY[1] + userSpriteAsset.get_height() >= platformLocationY) and (userSpriteLocationXY[1] + userSpriteAsset.get_height() <= platformLocationY + platform.height): # If the user collides with the top of the platform:
                    userSpriteLocationXY[1]=platformLocationY-userSpriteAsset.get_height() # Set the user's location to the top of the platform
                    onTop=True # The onTop variable is set to True
                    forceOfGravity=0 # The forceOfGravity variable is set to 0 (stops the user from shooting down, if they stand on the platform for a while, and then jump off of it)
                # Colliding with bottom of the platform
                if (userSpriteLocationXY[1] <= platformLocationY + platform.height) and (userSpriteLocationXY[1] >= platformLocationY): # If the user collides with the bottom of the platform:
                    userSpriteLocationXY[1]=platformLocationY + platform.height # Set the user's location to the bottom of the platform
                    onBottom=True # The onBottom variable is set to True
                
                if (onTop==False) and (onBottom==False): # If the onTop and onBottom variables are set to False (the user is not colliding with the top or bottom of the platform):
                    # Colliding with left side of the platform
                    if (userSpriteLocationXY[0] + userSpriteAsset.get_width() >= platformLocationX) and (userSpriteLocationXY[0] + userSpriteAsset.get_width() <= platformLocationX + platform.width): # If the user collides with the left side of the platform:
                        userSpriteLocationXY[0] = platformLocationX - userSpriteAsset.get_width() # Set the user's location to the left side of the platform
                    # Colliding with right side of the platform
                    if (userSpriteLocationXY[0] <= platformLocationX + platform.width) and (userSpriteLocationXY[0] >= platformLocationX): # If the user collides with the right side of the platform:
                        userSpriteLocationXY[0] = platformLocationX + platform.width # Set the user's location to the right side of the platform
        
        # Check for userSprite collisions with enemies
        for enemy in enemyListLevel5: # For every one of the enemies in the window:
            enemyLocationX=enemy.x # Define a variable for the emeny Rect object's X location
            enemyLocationY=enemy.y # Define a variable for the emeny Rect object's Y location
            if userSpriteRect.colliderect(enemy): # If two pygame Rect objects collide (user and enemy):
                hitSoundEffect.set_volume(1.5) # Set the volume of the hitSoundEffect
                hitSoundEffect.play() # Play the hitSoundEffect
                for platform in platformListLevel5: # For every one of the platforms in the window:
                    platform.x+=scrollCount # Move the platforms back to their original place (if the window has scrolled them to a different location)
                for enemy in enemyListLevel5: # For every one of the enemies in the window:
                    enemy.x+=scrollCount # Move the enemies back to their original place (if the window has scrolled them to a different location)
                objectiveLevel5Rect.x+=scrollCount # Move the objective back to its original place (if the window has scrolled it to a different location)
                gameOverMenu() # Call the gameOverMenu() function
        
        # Check for userSprite collisions with objective
        if userSpriteRect.colliderect(objectiveLevel5Rect): # If two pygame Rect objects collide (user and objective):
            levelCompleteSoundEffect.set_volume(0.75) # Set the volume of the levelCompleteSoundEffect
            levelCompleteSoundEffect.play() # Play the levelCompleteSoundEffect
            for platform in platformListLevel5: # For every one of the platforms in the window:
                platform.x+=scrollCount # Move the platforms back to their original place (if the window has scrolled them to a different location)
            for enemy in enemyListLevel5: # For every one of the enemies in the window:
                enemy.x+=scrollCount # Move the enemies back to their original place (if the window has scrolled them to a different location)
            objectiveLevel5Rect.x+=scrollCount # Move the objective back to its original place (if the window has scrolled it to a different location)
            winMenu() # Call the winMenu() function
        
        ########################################################
        
        # Manipulating the jumpTimer variable (ensures that the user cannot jump while in the air)
        if onTop==True: # If the user is not jumping:
            jumpTimer=0 # Set the jumpTimer to 0
        else: # This conditional statement is entered if the value in onTop is False (user is in the air)
            jumpTimer+=1 # Increment the jumpTimer by 1
        
        ########################################################
        
        # Rendering the pause caption onto the pygame window
        pauseCaption=smallFont.render("press esc to pause",True,WHITE,BLACK) # This command creates a text variable, usable by pygame
        captionBox=pauseCaption.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        captionBox.center=(300//2, 1550//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(pauseCaption,captionBox) # This command renders text onto the pygame window
        
        # Rendering the level number onto the pygame window
        levelCaption=smallFont.render("Level Five",True,WHITE,BLACK) # This command creates a text variable, usable by pygame
        levelBox=levelCaption.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
        levelBox.center=(175//2, 50//2) # This command centres the pygame Rect object around a single coordinate
        window.blit(levelCaption,levelBox) # This command renders text onto the pygame window
        
        ########################################################
        
        # Main pygame event loop
        for event in pygame.event.get(): # For every one of the events that occur during the pygame execution:
            if event.type==pygame.KEYDOWN: # If a key is pressed down:
                if event.key==pygame.K_ESCAPE: # If the escape key is pressed down:
                    pauseGame() # Call the pauseGame() function()
                if event.key==pygame.K_LEFT: # If the left arrow key is pressed down:
                    userSpriteMoveLeft=True # The player moves left
                if event.key==pygame.K_RIGHT: # If the right arrow key is pressed down:
                    userSpriteMoveRight=True # The player moves right
                if event.key==pygame.K_SPACE: # If the space key is pressed down:
                    if onTop==True: # If the player is on top of a platform:
                        jumpSoundEffect.set_volume(0.5) # Set the volume of the jumpSoundEffect
                        jumpSoundEffect.play() # Play the jumpSoundEffect
                    if jumpTimer<4: # If the jumpTimer is less than 4:
                        forceOfGravity=-16 # Subtract 16 from the forceOfGravity variable (makes the player go up)
            elif event.type==pygame.KEYUP: # If a key is released:
                if event.key==pygame.K_LEFT: # If the left arrow key is released:
                    userSpriteMoveLeft=False # The player stops moving left
                if event.key==pygame.K_RIGHT: # If the right arrow key is released:
                    userSpriteMoveRight=False # The player stops moving right
            elif event.type == pygame.QUIT: # If the window is closed:
                exit() # Terminate the program
        
        ########################################################
        
        # Update the window, and make the game run at 60FPS
        pygame.display.update() # This command updates the pygame window, every frame
        windowClock.tick(window_fps) # This command makes the program run at a designated frame rate (in this case, window_fps is set to 60)




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




# CREATING THE WIN MENU FUNCTION, TO END THE GAME AND CONGRAGULATE THE USER

def winMenu():
    menuBox=menuBackground.get_rect() # This command creates a pygame Rect object for the menu background image (this helps to position/display it on the screen after)
    menuBox.center=(1600//2, 400//2) # This command centres the pygame Rect object around a single coordinate
    window.blit(menuBackground,menuBox) # This command renders the background onto the window
    time.sleep(1) # This command uses the time module, to stop all action in the pygame window, for 1 second
    text=mediumSmallFont.render("Congratulations  "+userNameFinal,True,LIGHT_GREY) # This command creates a text variable, usable by pygame
    textBox=text.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
    textBox.center=(1600//2,800//2) # This command centres the pygame Rect object around a single coordinate
    window.blit(text, textBox) # This command renders text onto the pygame window
    pygame.display.flip() # This command updates every asset in the current pygame display window
    time.sleep(2) # This command uses the time module, to stop all action in the pygame window, for 2 seconds
    window.blit(menuBackground,menuBox) # This command renders the background onto the window
    text2=mediumSmallFont.render("You  have  beaten  Monochrome.",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
    textBox2=text2.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
    textBox2.center=(1600//2,800//2) # This command centres the pygame Rect object around a single coordinate
    window.blit(text2, textBox2) # This command renders text onto the pygame window
    pygame.display.flip() # This command updates every asset in the current pygame display window
    time.sleep(2) # This command uses the time module, to stop all action in the pygame window, for 2 seconds
    window.blit(menuBackground,menuBox) # This command renders the background onto the window
    text3=mediumSmallFont.render("Created by Tristan Parry.",True,LIGHT_GREY) # This command creates a text variable, usable by pygame
    textBox3=text3.get_rect() # This command creates a pygame Rect object for the text (this helps to position/display it on the screen after)
    textBox3.center=(1600//2,800//2) # This command centres the pygame Rect object around a single coordinate
    window.blit(text3, textBox3) # This command renders text onto the pygame window
    pygame.display.flip() # This command updates every asset in the current pygame display window
    time.sleep(3) # This command uses the time module, to stop all action in the pygame window, for 3 seconds
    window.blit(menuBackground,menuBox) # This command renders the background onto the window
    gameMenu() # Call the gameMenu() function
    
    while True: # Loops forever, unless broken out of
        for event in pygame.event.get(): # For every one of the events that occur during the pygame execution:
            if event.type == pygame.QUIT: # If the window is closed:
                    exit() # Terminate the program
            else: # If the event is not a closing of the window:
                None # Do nothing (this statement helped to catch lag errors in this function)




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




# CALLING THE STORY FUNCTION, TO RUN THE GAME FROM ITS BEGINNING

story() # This command allows the program to run, starting at the story() function. The rest of the transitions happen within the other functions in the program




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




# CREATING THE MAIN RUN LOOP, THAT EXECUTES THE PROGRAM IN THE PYGAME WINDOW

gameRunning=True # Creates a gameRunning variable, set to True, to run the program, and stop it (if needed), in the below while loop
while gameRunning: # Effectively loops forever, only when the game is running
    for event in pygame.event.get(): # For every one of the events that occur during the pygame execution:
        if event.type==pygame.QUIT: # If the window is closed:
            gameRunning=False # Set the gameRunning variable to False (terminating the program)
pygame.quit() # Terminate the pygame module