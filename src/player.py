# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name , room):
        self.name = name
        self.room = room

    def move_player(self, room):
        self.room = room 
        print(f"Direction is {self.room}")   

