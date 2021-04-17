# TRISTAN PARRY - ICS3U 2020 - SEMESTER 2 - CULMINATING TASK - TURTLE GAME - MONOCHROME (PLATFORMER GAME)
# FILE: asset_registry




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




# IMPORTING PYTHON MODULES

import pygame # Pygame is a python module that allows for the creation and integration of a GUI, or graphics-based activity, within a code/program (this module allows the game to run in a graphics window, with graphic commands/sequences, see below)




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




# INITIALIZE THE PYGAME MIXER

pygame.mixer.init() # Initializes the pygame sound mixer, to be used in the program




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




# REGISTER ASSETS IN THE PYGAME WINDOW

#Game Icons/Menu Assets
windowIcon=pygame.image.load(r"C:\Users\trist\Pictures\MONOCHROME\DATA\monochrome_icon.png") # Loads the icon image
menuBackground=pygame.image.load(r"C:\Users\trist\Pictures\MONOCHROME\DATA\menu_screen_background.jpg") # Loads the background image
objectiveMenuPic=pygame.image.load(r"C:\Users\trist\Pictures\MONOCHROME\DATA\transparent_menu_icon.png") # Loads the menu icon image

# In-Game Assets (Backgrounds)
gameBackgrounds=[r"C:\Users\trist\Pictures\MONOCHROME\DATA\game_background1.jpg",
                 r"C:\Users\trist\Pictures\MONOCHROME\DATA\game_background2.jpg",
                 r"C:\Users\trist\Pictures\MONOCHROME\DATA\game_background3.jpg",
                 r"C:\Users\trist\Pictures\MONOCHROME\DATA\game_background4.jpg"] # Loads the list of game background images

# In-Game Assets (Player Assets)
userSpritesMenu=[r"C:\Users\trist\Pictures\MONOCHROME\DATA\sprite1_menu.png",
                 r"C:\Users\trist\Pictures\MONOCHROME\DATA\sprite2_menu.png",
                 r"C:\Users\trist\Pictures\MONOCHROME\DATA\sprite3_menu.png"] # Loads the list of sprite images for the menu
sprite1Menu=pygame.image.load(userSpritesMenu[0]) # Defines the specific image for user sprite 1
sprite2Menu=pygame.image.load(userSpritesMenu[1]) # Defines the specific image for user sprite 2
sprite3Menu=pygame.image.load(userSpritesMenu[2]) # Defines the specific image for user sprite 3
userSpriteAssets=[[r"C:\Users\trist\Pictures\MONOCHROME\DATA\SpriteAnimations\Sprite1\facing_forward.png",
                  r"C:\Users\trist\Pictures\MONOCHROME\DATA\SpriteAnimations\Sprite1\walking_left.png",
                  r"C:\Users\trist\Pictures\MONOCHROME\DATA\SpriteAnimations\Sprite1\walking_right.png"],
                  
                  [r"C:\Users\trist\Pictures\MONOCHROME\DATA\SpriteAnimations\Sprite2\facing_forward.png",
                  r"C:\Users\trist\Pictures\MONOCHROME\DATA\SpriteAnimations\Sprite2\walking_left.png",
                  r"C:\Users\trist\Pictures\MONOCHROME\DATA\SpriteAnimations\Sprite2\walking_right.png"],
                  
                  [r"C:\Users\trist\Pictures\MONOCHROME\DATA\SpriteAnimations\Sprite3\facing_forward.png",
                  r"C:\Users\trist\Pictures\MONOCHROME\DATA\SpriteAnimations\Sprite3\walking_left.png",
                  r"C:\Users\trist\Pictures\MONOCHROME\DATA\SpriteAnimations\Sprite3\walking_right.png"]] # Loads the list of sprite images for the game

# In-Game Assets (Enemy Assets)
enemySpriteAsset=r"C:\Users\trist\Pictures\MONOCHROME\DATA\SpriteAnimations\Enemy1\facing_forward.png" # Loads the enemy image for the menu
enemySpriteMenuPic=pygame.transform.rotozoom(pygame.image.load(enemySpriteAsset),0,3) # Zooms in the chosen image by 3x, to be the desired menu size

# In-Game Assets (Objective Assets)
objectiveSpriteAsset=pygame.image.load(r"C:\Users\trist\Pictures\MONOCHROME\DATA\SpriteAnimations\Objective1\objective.png") # Loads the objective image for the game




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#




# REGISTER SOUNDS/MUSIC IN THE PYGAME WINDOW

jumpSoundEffect=pygame.mixer.Sound(r"C:\Users\trist\Pictures\MONOCHROME\DATA\Sound\jump_sound.wav") # Loads the jumpSoundEffect
hitSoundEffect=pygame.mixer.Sound(r"C:\Users\trist\Pictures\MONOCHROME\DATA\Sound\enemy_hit_sound.wav") # Loads the hitSoundEffect
levelCompleteSoundEffect=pygame.mixer.Sound(r"C:\Users\trist\Pictures\MONOCHROME\DATA\Sound\level_complete_sound.wav") # Loads the levelCompleteSoundEffect

menuMusic=pygame.mixer.music.load(r"C:\Users\trist\Pictures\MONOCHROME\DATA\Sound\main_music.ogg") # Loads the menuMusic