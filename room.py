from random import *
#from container import Container

# Room class
# Rooms can have:
#   a name
#   a description
#   multiple linked_rooms
#   multiple room_items
#   multiple room_containers
#   one character
class Room():
    # Room constructor
    def __init__(self, room_name, room_description):
        self.name = room_name
        self.description = room_description
        self.linked_rooms = {} # A dictionary of linked rooms
        self.room_items = list() # A blank array of room items
        self.character = None

    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name

    def set_character(self, myCharacter):
        self.character = myCharacter

    def get_character(self):
        return self.character

    def remove_character(self):
        self.character = None

    # Instanciate a room item. This is also used when an item is revealed from within a container.
    def create_room_item(self,item):
        self.room_items.append(item)

    # Drop an item from your hands (heldItems) into the room (room_items)
    def add_room_item(self,item,heldItems):
        item = item.lower()
        if heldItems.count(item) > 0:
            self.room_items.append(item)
            heldItems.remove(item)
        elif heldItems.count(item) <= 0:
            print("You can't DROP "+item.upper()+" because you aren't holding that")
        return heldItems

    # Pick up an item
    def take_room_item(self,item,heldItems):
        item = item.lower()
        if len(heldItems) < 2 and self.room_items.count(item) > 0:
            self.room_items.remove(item)
            heldItems.append(item)
            print("You pick up the "+item.upper())
        elif len(heldItems) >= 2:
            print("You can't TAKE "+item.upper()+" because your hands are full")
        elif self.room_items.count(item) <= 0:
            print("You can't TAKE "+item.upper())
        return heldItems

    # Procedure that prints all interactive items in the room
    def get_room_items(self,heldItems):
        # Create new string
        output = ""
        for i in self.room_items:
            output += "There is a "+i+". "
            # If you have an empty hand, you can TAKE it
            if len(heldItems) < 2:
                output += "You can TAKE "+i.upper()+". "
        print(output)

    # Sets a one-way link from one room to another
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    # Sets the current room, if permitted by the linked_rooms array
    def move(self, direction, visitedRooms):
        if direction == "N":
            direction = "NORTH"
        if direction == "S":
            direction = "SOUTH"
        if direction == "E":
            direction = "EAST"
        if direction == "W":
            direction = "WEST"
        if direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            if room.get_name() == "locked":
                print("The " + direction + " door is locked.")
                return self
            else:
                output = "You head " + direction
                if room.get_name() in visitedRooms:
                    output += " to the " + room.get_name()
                print(output)
                return self.linked_rooms[direction]
        else:
            print("Sorry, but you can't " + direction + ".")
            return self

    # Procedure that prints the linked rooms for the current room
    def get_room_directions(self, visitedRooms):
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            if room.get_name() in visitedRooms:
                print( "The " + room.get_name() + " is " + direction)
            else:
                print( "There is a door to the " + direction)

    # Procedure that prints all info about the room
    def info(self,heldItems,myHealth,visitedRooms):
        print("=============")
        print(self.name) # The name of the room
        print("-------------")
        print(self.description) # The description of the room

        #Add current room to visitedRooms array
        if self.name not in visitedRooms:
            visitedRooms.append(self.name)

        #Room Items
        self.get_room_items(heldItems)

        #Directions
        self.get_room_directions(visitedRooms)

        #Characters
        if self.get_character() is not None:
            self.character.describe()
            if self.character.isEnemy():
                myHealth = myHealth - self.character.enemyAttack()
                print("You have "+str(myHealth)+" HP")
        return myHealth
