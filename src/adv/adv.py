import os
from time import sleep
from textwrap  import wrap
from room import Room
from player import Player 
# Declare all the rooms

room = {
    # outside: {name: "Outside cave enterance", description: "North of you, the cave mouth beckons", n_to: {POINTS TO FOYER}}
    'outside':  Room("Outside Cave Entrance","North of you, the cave mount beckons"),
    'foyer':    Room("Foyer","Dim light filters in from the south. Dusty passages run north and east."),
    'overlook': Room("Grand Overlook","A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."),
    'narrow':   Room("Narrow Passage","The narrow passage bends here from west to north. The smell of gold permeates the air."),
    'bathroom': Room("Pit stop", "Remember to wash your hands!", "You may continue from west to north"),
    'treasure': Room("Treasure Chamber","You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."),
    # Add my own room
    
}
#debugging


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['narrow'].e_to = room['bathroom']
room['bathroom'].w_to = room['treasure']
room['bathroom'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


player = Player('any', room['outside'])
direction = None

while(True):
    
    os.system('clear')
    print(
        '\n You are currently here:','\n'.join(wrap(player.location.name, width=10)),
        '\n Description:', '\n'.join(wrap(player.location.description, width=50))) 
    direction = input('\nWhich way would you like to go?\n(N, E, S, W) or (Q to quit) pick one:').lower()
    player.move_to(direction)