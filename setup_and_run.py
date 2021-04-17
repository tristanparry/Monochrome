# TRISTAN PARRY - ICS3U 2020 - SEMESTER 2 - CULMINATING TASK - TURTLE GAME - MONOCHROME (PLATFORMER GAME)
# FILE: setup_and_run




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




# IMPORTING PYTHON MODULES

import pygame # Pygame is a python module that allows for the creation and integration of a GUI, or graphics-based activity, within a code/program (this module allows the game to run in a graphics window, with graphic commands/sequences, see below)




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




# DEFINE COLOURS IN THE PROGRAM

BLACK = (0,0,0) # Defines the colour variable, via a RGB code, in tuple form
WHITE = (255,255,255) # Defines the colour variable, via a RGB code, in tuple form
LIGHT_GREY=(120,120,120) # Defines the colour variable, via a RGB code, in tuple form




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




# CREATING/SETTING UP THE PYGAME WINDOW ATTRIBUTES

window_resolution=[1600,800] # Defines the width and height of the pygame window, in list form
window_caption="TRISTAN PARRY - MONOCHROME" # Defines the pygame window caption
window_fps=60 # Defines the pygame window FPS




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




# CREATING/SETTING UP THE FONTS USED IN THE GAME

pygame.font.init() # Initializes pygame's use of fonts, to be used in the program
largeFont=pygame.font.Font(r"C:\Users\trist\Pictures\MONOCHROME\DATA\Android.ttf",120) # Defines the parameters for a large font
mediumLargeFont=pygame.font.Font(r"C:\Users\trist\Pictures\MONOCHROME\DATA\Android.ttf",75) # Defines the parameters for a medium large font
mediumFont=pygame.font.Font(r"C:\Users\trist\Pictures\MONOCHROME\DATA\Android.ttf",60) # Defines the parameters for a medium font
mediumSmallFont=pygame.font.Font(r"C:\Users\trist\Pictures\MONOCHROME\DATA\Android.ttf",35) # Defines the parameters for a medium small font
mediumSmallerFont=pygame.font.Font(r"C:\Users\trist\Pictures\MONOCHROME\DATA\Android.ttf",30) # Defines the parameters for another medium snall font
smallFont=pygame.font.Font(r"C:\Users\trist\Pictures\MONOCHROME\DATA\Android.ttf",20) # Defines the parameters for a small font