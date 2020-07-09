# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.current_room = current_room
        self.name = name

    def move_player(self, direction):
        move = f"{direction}"
        current_room = self.current_room
        if direction == "n" and current_room.n_to != None:
            self.current_room = current_room.n_to
            return True
        if direction == "s" and current_room.s_to != None:
            self.current_room = current_room.s_to
            return True
        if direction == "e" and current_room.e_to != None:
            self.current_room = current_room.e_to
            return True
        if direction == "w" and current_room.w_to != None:
            self.current_room = current_room.w_to
            return True
        else:
            return False

    def describe_room(self):
        room = self.current_room
