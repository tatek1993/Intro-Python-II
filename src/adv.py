from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("banana", "What's a room without a single, ripe banana sitting in the middle of the floor?")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("melon", "A single melon sits in a chair. It looks melon-cholic. Hm.")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("grapes", "This room is far too narrow for a regular sized fruit, but there are some grapes lined up single-file against the wall.")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("bowl", "Maybe you didn't find treasure, but someone did leave behind a bowl which looks to be roughly fruit salad-sized.")]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

new_player = Player("Portobello", room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def game():
    player_name = input(f"\n What is your name? \n Enter Your Name : ")
    current_player = Player(player_name, room["outside"])
    is_playing = True

    print(" ")
    print(f"Welcome, {player_name}. Explore and see what you can find.")
    print(" ")
    current_player.describe_room()

    while is_playing == True:

        action = input("\n".join(textwrap.wrap(
            "\nMOVE using 'n' for North, 's' for South, 'e' for East, and 'w' for Waffle. \nLOOK for loot using 'look'.\nGET an item you find using 'get ___' \nDROP an item using 'drop ___' \nQUIT using 'q'.\nWhat would you like to do? :")))
        if action in ["n", "s", "e", "w"]:
            if current_player.move_player(action) == True:
                current_player.describe_room()
            else:
                print(" ")
                print("!!! -- OOPS, YOU CAN'T MOVE THERE. -- !!!")
        elif action == "look":
            print(" ")
            current_player.look()
        elif action.startswith("get"):
            print(" ")
            current_player.get(action[4:])
        elif action.startswith("drop"):
            print(" ")
            current_player.drop(action[5:])
        elif action == "q":
            is_playing = False
            # close()
        else:
            print(" ")
            print(
                "!!! -- OOPS, THAT'S NOT SOMETHING YOU CAN DO. -- !!!")
            print(" ")


game()
