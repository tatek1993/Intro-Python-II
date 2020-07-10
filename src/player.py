# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.current_room = current_room
        self.name = name
        self.inv = []

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
        if len(items) < 1:
            print("This place has absolutely no fruit. Probably not worth staying...")
            print(" ")

    def get(self, item_name):
        found = False
        for item in self.current_room.items:
            if item.name == item_name:
                self.inv.append(item)
                self.current_room.items.remove(item)
                found = True
                print(
                    f"You picked up the {item_name} and put it in your comically large pocket.")
                print(" ")
        if found == False:
            print("There is nothing here. You looted the whole room. Who raised you?")
            print(" ")

    def drop(self, item_name):
        dropped = False
        for item in self.inv:
            if item.name == item_name:
                self.current_room.items.append(item)
                self.inv.remove(item)
                dropped = True
                print(
                    f"You dropped your {item_name} on the floor like some sort of animal.")
                print(" ")
        if dropped == False:
            print(f"Buddy, you don't even have a {item_name}.")
            print(" ")

    def describe_room(self):
        print(" ")
        print(f"___{self.current_room.name.upper()}___")
        print(" ")
        print(
            f"{self.current_room.description}")
        print(" ")
