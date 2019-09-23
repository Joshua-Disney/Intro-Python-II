from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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


player = Player('Link', room['outside'])

print(f"{player.name}'s info: {player} ")

# for i in room:
#     print(f"{room[i]}")
# Write a loop that:
# <------------------------------I don't understand why this would be a loop or how to turn it into one.
print(f"{player.name} stands in the {player.currentRoom.name}.  {player.currentRoom.description}")

#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

quit = False

while not quit:
    command = input(f"\n(N)orth\n(S)outh\n(E)ast\n(W)est\n(Q)uit\n\nCommand: ")
    command = command.lower().strip()
    if command == '':
        continue
    command = command[0]
    if command == 'q':  # quit
        quit = True
    elif command == 'n':
        if player.currentRoom.n_to:
            player.currentRoom = player.currentRoom.n_to
            print(
                f"{player.name} moves north into the {player.currentRoom.name}.  {player.currentRoom.description}")
        else:
            print(
                f"You don't see a path in that direction.  {player.currentRoom.description}")
    elif command == 'w':
        if player.currentRoom.w_to:
            player.currentRoom = player.currentRoom.w_to
            print(
                f"{player.name} moves west into the {player.currentRoom.name}.  {player.currentRoom.description}")
        else:
            print(
                f"You don't see a path in that direction.  {player.currentRoom.description}")
    elif command == 'e':
        if player.currentRoom.e_to:
            player.currentRoom = player.currentRoom.e_to
            print(
                f"{player.name} moves east into the {player.currentRoom.name}.  {player.currentRoom.description}")
        else:
            print(
                f"You don't see a path in that direction.  {player.currentRoom.description}")
    elif command == 's':
        if player.currentRoom.s_to:
            player.currentRoom = player.currentRoom.s_to
            print(
                f"{player.name} moves south into the {player.currentRoom.name}.  {player.currentRoom.description}")
        elif player.currentRoom.name == "Outside Cave Entrance":
            print(f"""{player.name} decides to go home.  Thank you for playing.
-
-
-
-
-
-
-
""")
            quit = True
        else:
            print(
                f"You don't see a path in that direction.  {player.currentRoom.description}")
