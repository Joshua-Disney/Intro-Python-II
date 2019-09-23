# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom

        self.items = []

    def __str__(self):
        return f"Name: {self.name}, Current Room: {self.currentRoom.name}, Items: {self.items}"

    def __repr__(self):
        return f"Player({repr(self.name)})"
