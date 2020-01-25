import os
import pygame
from pygame.locals import *
pygame.init()

#Import classes
from player import Player
from room import Room
#from item import Item

#General Variables
BACKGROUND_COLOR = (0,0,0)
RED = (255,0,0)
GREEN = (0,200,0)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 900
IMAGE_WIDTH = 700
IMAGE_HEIGHT = 280

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance", 
                     "North of you, the cave mount beckons"),
    'foyer':    Room("Foyer", 
                     """Dim light filters in from the south. Dusty passages run north and east."""),
    'overlook': Room("Grand Overlook", 
                     """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),
    'narrow':   Room("Narrow Passage", 
                     """The narrow passage bends here from west to north. The smell of gold permeates the air."""),
    'treasure': Room("Treasure Chamber", 
                     """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
}

# Link rooms together
room_directions = {
    'outside': [{'north': 'foyer'}],
    'foyer': [{'south': 'outside'}, {'north': 'overlook'}, {'east': 'narrow'}],
    'overlook': [{'south''foyer'},],
    'narrow': [{'west': 'foyer'}, {'north': 'treasure'}],
    'treasure': [{'south': 'narrow'},]
}

#Main Windows Set up
game_windows = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT)) 
pygame.display.set_caption("Lambda Adventures")

#Function to load Initial Logo and Sound
def load_logo():
    current_path = os.path.dirname(__file__)

    #Loading Sound
    music = pygame.mixer.music.load(os.path.join(current_path, 'audio.mp3'))
    pygame.mixer.music.play(-1)

    #Image Load
    logo_image = pygame.image.load(os.path.join(current_path, 'lambdaventures.png'))
    logo_x_coordinates = (SCREEN_WIDTH - IMAGE_WIDTH)/2
    logo_y_coordinates = (SCREEN_HEIGHT - IMAGE_HEIGHT)/2
    game_windows.blit(logo_image, (logo_x_coordinates ,logo_y_coordinates))

    #Loading Text
    #question_text = pygame.font.Font('freesansbold.ttf', 50)
    #TextSurf , TextRect = text_object('Solucion', question_text)
    #TextRect.center = ((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2)) 
    #game_windows.blit(TextSurf , TextRect)
    #time.sleep(2)

    pygame.draw.rect(game_windows, GREEN, (150,750,100,50))
    pygame.draw.rect(game_windows, RED, (SCREEN_WIDTH-350,750,100,50))
class Main():
    #Loading Logo
    load_logo()
    want_to_play = input("Do you Want to Play LambdaVentures? Yes/No: ")
    
    if want_to_play.lower() == "yes":
        your_name = input("Enter Your Name: ")
        print("Good Luck with your Venture")
        room_type = 'outside'
        user_choice = ''
        new_player = Player(your_name , room[room_type])
       
        running = True
        
        while user_choice != 'q':
            print(f"Hello {new_player.name} ,\nYou are currently on room: {new_player.room.name}, described as: {new_player.room.description}")
            user_choice = input("['n'] Move North, ['s'] Move South, ['e'] Move East, ['w'] Move West ['q'] quit ")
            
            current_room_directions = room_directions[room_type]
            for dic in current_room_directions:
                for key, value in dic.items():
                    if key[:1].lower() == user_choice.lower():
                        print('the key', key) 
                        print('this is the value', value)
                        room_type = value
                        new_player.move_player(room[room_type])
                    else:
                        print('The direction is not valid')    
        print(f"Bye Bye, {new_player.name}")                
        pygame.display.quit()
        pygame.quit()
        exit()
        
    else:
        print(f"Bye Bye, {new_player.name}")
        pygame.display.quit()
        exit()
        



