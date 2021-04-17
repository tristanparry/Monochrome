# TRISTAN PARRY - ICS3U 2020 - SEMESTER 2 - CULMINATING TASK - TURTLE GAME - MONOCHROME (PLATFORMER GAME)
# FILE: level_registry




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




# IMPORTING PYTHON MODULES/CREATED PY FILES

import pygame # Pygame is a python module that allows for the creation and integration of a GUI, or graphics-based activity, within a code/program (this module allows the game to run in a graphics window, with graphic commands/sequences, see below)
from setup_and_run import * # Imports all assets and information from the setup_and_run file
from asset_registry import * # Imports all assets and information from the asset_registry file




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




# CREATE PLATFORM LISTS, FOR EACH LEVEL IN THE GAME

platformListLevel1=[pygame.Rect(0,700,350,100),pygame.Rect(450,600,200,35),pygame.Rect(750,535,100,35),
                    pygame.Rect(1000,400,200,35),pygame.Rect(1450,300,100,35),pygame.Rect(1775,175,500,35)] # Defines the list of platforms in level 1
platformListLevel2=[pygame.Rect(0,700,350,100),pygame.Rect(450,535,200,35),pygame.Rect(100,375,150,35),
                    pygame.Rect(500,200,200,35),pygame.Rect(1200,400,75,35),pygame.Rect(1400,350,200,35),
                    pygame.Rect(1900,250,500,35)] # Defines the list of platforms in level 2
platformListLevel3=[pygame.Rect(0,700,350,100),pygame.Rect(0,525,350,35),pygame.Rect(0,350,350,35),
                    pygame.Rect(650,200,400,35),pygame.Rect(1900,300,500,35),pygame.Rect(2350,750,250,35)] # Defines the list of platforms in level 3
platformListLevel4=[pygame.Rect(0,700,350,100),pygame.Rect(600,700,250,35),pygame.Rect(1100,525,50,35),
                    pygame.Rect(550,400,225,35),pygame.Rect(1050,250,125,35),pygame.Rect(1400,150,720,35)] # Defines the list of platforms in level 4
platformListLevel5=[pygame.Rect(0,700,350,100),pygame.Rect(0,200,75,35),pygame.Rect(200,200,75,35),pygame.Rect(400,200,75,35),
                    pygame.Rect(600,200,75,35),pygame.Rect(800,200,75,35),pygame.Rect(1000,200,75,35),pygame.Rect(1200,200,75,35),
                    pygame.Rect(1400,200,75,35),pygame.Rect(1600,200,75,35),pygame.Rect(1800,200,75,35),pygame.Rect(2000,200,75,35),
                    pygame.Rect(2100,350,75,35),pygame.Rect(300,350,75,35),pygame.Rect(500,350,75,35),pygame.Rect(700,350,75,35),
                    pygame.Rect(900,350,75,35),pygame.Rect(1100,350,75,35),pygame.Rect(1300,350,75,35),pygame.Rect(1500,350,75,35),
                    pygame.Rect(1700,350,75,35),pygame.Rect(1900,350,75,35),
                    pygame.Rect(0,500,75,35),pygame.Rect(200,500,75,35),pygame.Rect(400,500,75,35),
                    pygame.Rect(600,500,75,35),pygame.Rect(800,500,75,35),pygame.Rect(1000,500,75,35),pygame.Rect(1200,500,75,35),
                    pygame.Rect(1400,500,75,35),pygame.Rect(1600,500,75,35),pygame.Rect(1800,500,75,35),pygame.Rect(2000,500,75,35),
                    pygame.Rect(2100,650,75,35),pygame.Rect(500,650,75,35),pygame.Rect(700,650,75,35),
                    pygame.Rect(900,650,75,35),pygame.Rect(1100,650,75,35),pygame.Rect(1300,650,75,35),pygame.Rect(1500,650,75,35),
                    pygame.Rect(1700,650,75,35),pygame.Rect(1900,650,75,35)] # Defines the list of platforms in level 5




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




# CREATE ENEMY LISTS, FOR EACH LEVEL IN THE GAME

enemyListLevel1=[pygame.Rect(1075,314,63,86)] # Defines the list of enemies in level 1
enemyListLevel2=[pygame.Rect(600,114,63,86),pygame.Rect(1500,264,63,86)] # Defines the list of enemies in level 2
enemyListLevel3=[pygame.Rect(2000,214,63,86),pygame.Rect(2350,664,63,86),pygame.Rect(2540,664,63,86),pygame.Rect(750,114,63,86),pygame.Rect(850,114,63,86)] # Defines the list of enemies in level 3
enemyListLevel4=[pygame.Rect(740,614,63,86),pygame.Rect(662,314,63,86),pygame.Rect(550,314,63,86),pygame.Rect(1112,164,63,86),pygame.Rect(1500,64,63,86),pygame.Rect(1830,64,63,86)] # Defines the list of enemies in level 4
enemyListLevel5=[pygame.Rect(0,114,63,86),pygame.Rect(200,114,63,86),pygame.Rect(400,114,63,86),pygame.Rect(600,114,63,86),
                 pygame.Rect(1000,114,63,86),pygame.Rect(1400,114,63,86),pygame.Rect(1620,114,63,86),pygame.Rect(1800,114,63,86),
                 pygame.Rect(300,264,63,86),pygame.Rect(700,264,63,86),pygame.Rect(900,264,63,86),
                 pygame.Rect(1100,264,63,86),pygame.Rect(1300,264,63,86),pygame.Rect(1700,264,63,86),pygame.Rect(1900,264,63,86),pygame.Rect(0,414,63,86),
                 pygame.Rect(200,414,63,86),pygame.Rect(600,414,63,86),pygame.Rect(800,414,63,86),pygame.Rect(1000,414,63,86),pygame.Rect(1200,414,63,86),
                 pygame.Rect(1600,414,63,86),pygame.Rect(1800,414,63,86),pygame.Rect(2000,414,63,86),pygame.Rect(500,564,63,86),
                 pygame.Rect(900,564,63,86),pygame.Rect(1100,564,63,86),pygame.Rect(1300,564,63,86),pygame.Rect(1500,564,63,86),pygame.Rect(1700,564,63,86)] # Defines the list of enemies in level 5




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




# CREATE THE OBJECTIVE, FOR EACH LEVEL IN THE GAME

objectiveLevel1Rect=pygame.Rect(1800,50,100,100) # Defines the objective in level 1
objectiveLevel2Rect=pygame.Rect(2000,100,100,100) # Defines the objective in level 2
objectiveLevel3Rect=pygame.Rect(2420,630,60,60) # Defines the objective in level 3
objectiveLevel4Rect=pygame.Rect(1900,25,100,100) # Defines the objective in level 4
objectiveLevel5Rect=pygame.Rect(2200,500,100,100) # Defines the objective in level 5




#------




# SET BACKGROUND, FOR EACH LEVEL

gameBackgroundLevel1=pygame.image.load(gameBackgrounds[0]) # Uses the random function to choose an image from the backgrounds list
gameBackgroundLevel1=pygame.transform.rotozoom(gameBackgroundLevel1, 0, 1.5) # Zooms in the chosen background image by 1.5x, to fill the window
gameBackgroundLevel2=pygame.image.load(gameBackgrounds[1]) # Uses the random function to choose an image from the backgrounds list
gameBackgroundLevel2=pygame.transform.rotozoom(gameBackgroundLevel2, 0, 1.5) # Zooms in the chosen background image by 1.5x, to fill the window
gameBackgroundLevel3=pygame.image.load(gameBackgrounds[2]) # Uses the random function to choose an image from the backgrounds list
gameBackgroundLevel3=pygame.transform.rotozoom(gameBackgroundLevel3, 0, 1.5) # Zooms in the chosen background image by 1.5x, to fill the window
gameBackgroundLevel4=pygame.image.load(gameBackgrounds[3]) # Uses the random function to choose an image from the backgrounds list
gameBackgroundLevel4=pygame.transform.rotozoom(gameBackgroundLevel4, 0, 1.5) # Zooms in the chosen background image by 1.5x, to fill the window
gameBackgroundLevel5=pygame.image.load(gameBackgrounds[0]) # Uses the random function to choose an image from the backgrounds list
gameBackgroundLevel5=pygame.transform.rotozoom(gameBackgroundLevel5, 0, 1.5) # Zooms in the chosen background image by 1.5x, to fill the window