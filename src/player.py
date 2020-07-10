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

    def look(self):
        items = self.current_room.items
        for item in items:
            print(item.description)
            print(" ")

    def get(self, item_name):
        inv = []
        found = False
        for item in self.current_room.items:
            if item.name == item_name:
                inv.append(item)
                self.current_room.items.remove(item)
                found = True
                print('You picked it up and put it in your comically large pocket.')
                print(" ")
        if found == False:
            print('There is nothing here. You looted the whole room. Who raised you?')
            print(" ")

    def drop(self, item):
        pass

    def describe_room(self):
        print(" ")
        print(f"{self.current_room.name.upper()}")
        print(" ")
        print(
            f"A little about this room : {self.current_room.description}")
        print(" ")
