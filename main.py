from room import *
from flashlight import *
from character import *
from container import *
from world import *

heldItems = []
myHealth = 53
visitedRooms = []

world = World()
current_room = world.kitchen

# This is a procedure that simply prints the items the player is holding and tells them if they can do something with that item
def playerItems():
    # Print out the player's Held Items and let player know if they can USE an item to fight a character or something
    if len(heldItems) == 1:
        print("You are holding a "+heldItems[0])
        print("You can DROP "+heldItems[0].upper())
        if current_room.character is not None:
            print("You can USE "+heldItems[0].upper()+" to fight "+current_room.character.name)
    elif len(heldItems) >= 2:
        print("Your hands are full. You must drop something before you can pick anything else up.")
        print("You are holding a "+heldItems[0]+" and a "+heldItems[1])
        print("You can DROP "+heldItems[0].upper()+" or DROP "+heldItems[1].upper())
        if current_room.character is not None:
            print("You can USE "+heldItems[0].upper()+" to fight "+current_room.character.name+" or USE "+heldItems[1].upper())
            
    # ********************************* SPECIAL ITEM INFO *********************************
    # If holding a special item, then display the item's description/behaviors with .info()
    if "red flashlight" in heldItems:
        world.redFlashlight.info(heldItems,current_room)
    if "yellow flashlight" in heldItems:
        world.yellowFlashlight.info(heldItems,current_room)
    if "green flashlight" in heldItems:
        world.greenFlashlight.info(heldItems,current_room)

# This fuction checks the player's command and then runs the corresponding method
def checkUserInput(current_room,command,heldItems):
    if ("red flashlight" in heldItems and world.redFlashlight.isOn) or ("yellow flashlight" in heldItems and world.yellowFlashlight.isOn) or ("green flashlight" in heldItems and world.greenFlashlight.isOn):
        holdingFlashlight = True
    else:
        holdingFlashlight = False
    # Convert it to ALL CAPS
    command = command.upper()
    # All possible user input commands go here
    print("\n")
    
    # ********************************* SPECIAL USER INPUT *********************************
    # If holding a special item, then check for that item's info with check_input()
    if "red flashlight" in heldItems and "RED FLASHLIGHT" in command:
        world.redFlashlight.check_input(command,heldItems,current_room)
    elif "yellow flashlight" in heldItems and "YELLOW FLASHLIGHT" in command:
        world.yellowFlashlight.check_input(command,heldItems,current_room)
    elif "green flashlight" in heldItems and "GREEN FLASHLIGHT" in command:
        world.greenFlashlight.check_input(command,heldItems,current_room)

    # ********************************* USE, TAKE, DROP *********************************
    # Use an item to fight an enemy
    elif "USE " in command and current_room.get_character() is not None:
        # command[4:] is used to get the characters typed after "USE "
        enemyHealth = current_room.character.fight(command[4:])
        if enemyHealth < 1:
            print(current_room.character.name+" is dead")
            current_room.remove_character() # If the enemy is dead, then remove them from the room
    # Take lets you pick up an item
    elif "TAKE " in command:
        # command[5:] is used to get the characters typed after "TAKE "
        heldItems = current_room.take_room_item(command[5:],heldItems)
    # Drop lets you set down an item
    elif "DROP " in command:
        # command[5:] is used to get the characters typed after "DROP "
        heldItems = current_room.add_room_item(command[5:],heldItems)
    # Talk and Fight aren't currently used in this version of the game, but could be implemented in your version of the game
    elif "TALK" in command and current_room.get_character() is not None:
        current_room.character.talk()
    elif "FIGHT" in command and current_room.get_character() is not None:
        current_room.character.talk()
    
    # ********************************* ROOM SPECIFIC USER INPUTS *********************************
    # Interactive containers look like this...   elif current_room.name == "Laboratory" and command == "SHELF"
    elif current_room.name == "Kitchen" and command == "CUPBOARD":
        # Open kitchen.cupboard and concat each of the contents to the end of room_items
        current_room.room_items += world.kitchen.cupboard.open()
    # Can only open cabinet if holding a flashlight that isOn
    elif current_room.name == "Kitchen" and command == "CABINET" and holdingFlashlight:
        # Open kitchen.cabinet and concat each of the contents to the end of room_items
        print("You use the flashlight to look inside the cabinet.")
        current_room.room_items += world.kitchen.cabinet.open()
    elif current_room.name == "Kitchen" and command == "CABINET" and not holdingFlashlight:
        print("You check the cabinet, but it's too dark to see if there is anything inside.")
    elif current_room.name == "Small Office" and command == "PACKAGE":
        # Open smalloffice.desk and concat each of the contents to the end of room_items
        current_room.room_items += world.smalloffice.package.open()
    elif current_room.name == "Small Office" and command == "READ":
        print("POCCNR??? You can't read it. It's written is some strange Cyrillic script.")
    elif current_room.name == "Small Office" and command == "DESK" and "brass key" in heldItems:
        # Open smalloffice.desk and concat each of the contents to the end of room_items
        print("You use the brass key to unlock the desk.")
        current_room.room_items += world.smalloffice.desk.open()
    elif current_room.name == "Small Office" and command == "DESK":
        print("The desk drawer is locked.")
    elif current_room.name == "Laboratory" and command == "SHELF":
        # Open lab.shelf and concat each of the contents to the end of room_items
        current_room.room_items += world.lab.shelf.open()

    # ********************************* MOVE *********************************
    else:
        current_room = current_room.move(command,visitedRooms) # If it was none of those commands, assume it was a direction. Try to move.
    return current_room


#THE LOOP
while True:
    print("\n")
    # Print current room info
    myHealth = current_room.info(heldItems,myHealth,visitedRooms) # this returns myHealth cuz an enemy in the room could hurt you
    if myHealth <= 0:
        print("You died.\nGAME OVER")
        break
    # Print player items
    playerItems()
    # Get user input
    command = input("> ")
    # Check the user input
    current_room = checkUserInput(current_room,command,heldItems)
