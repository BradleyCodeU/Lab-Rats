class Flashlight():
    #constructor with 3 params
    def __init__(self,color,batteries,deadBattery):#constructor
        self.color = color #red, yellow, etc
        self.batteries = batteries #0 or 1
        self.deadBattery = deadBattery #true or false
        self.isOn = False


    #getter that returns description/behaviors of flashlight
    #params exist in case a special item changes behavior based on room/other held item
    def info(self,heldItems,current_room):
        if self.isOn and not self.deadBattery:
            print("The "+self.color+" flashlight is switched on and shining. You can TURN "+self.color.upper()+" FLASHLIGHT OFF")
        elif self.isOn and self.deadBattery:
            print("The "+self.color+" flashlight is switched on but its not working. You can TURN "+self.color.upper()+" FLASHLIGHT OFF")
        else:
            print("The "+self.color+" flashlight is switched off. You can TURN "+self.color.upper()+" FLASHLIGHT ON")
        if self.batteries == 0 and "battery" in heldItems:
            print("You can ADD BATTERY TO "+self.color.upper()+" FLASHLIGHT")
        if self.batteries > 0:
            print("You can REMOVE "+self.color.upper()+" FLASHLIGHT BATTERY")


    #procedure that checks for keywords and calls other setter methods. this procedure is called when player tries to use the item.
    def check_input(self,command,heldItems,current_room):
        if command == "TURN "+self.color.upper()+" FLASHLIGHT OFF":
            self.turn_off()
        if command == "TURN "+self.color.upper()+" FLASHLIGHT ON":
            self.turn_on()
        if command == "ADD BATTERY TO "+self.color.upper()+" FLASHLIGHT" and self.batteries == 0 and "battery" in heldItems:
            self.add_batteries(heldItems)
        if command == "REMOVE "+self.color.upper()+" FLASHLIGHT BATTERY" and self.batteries == 1:
            self.remove_batteries(heldItems,current_room)

    #setter that removes 1 battery if there are batteries in the flashlight
    #returns 1 if successful, to add 1 battery to room
    def remove_batteries(self,heldItems,current_room):
        if self.batteries > 0:
            self.batteries -= 1
            if self.deadBattery:
                print("You remove 1 dead battery from the "+self.color+" flashlight.")
                current_room.room_items.append("dead battery")
            else:
                print("You remove 1 good battery from the "+self.color+" flashlight.")
                current_room.room_items.append("battery")
        else:
            print("There aren't any batteries in the "+self.color+" flashlight.")

    #setter that removes the bulb if there is a bulb in the flashlight
    #returns 1 if successful, to add 1 bulb to room
    def remove_bulb(self):
        if self.bulb > 0:
            self.bulb -= 1
            print("You remove the flashlight bulb.")
            return 1 #add 1 bulb to room
        else:
            print("There isn't a bulb in the flashlight.")
            return 0

    #setter that adds 1 battery if there are batteries in the room and space in the flashlight
    #returns -1 if successful, to remove 1 battery from room
    def add_batteries(self,heldItems):
        if self.batteries < 1 and "battery" in heldItems:
            self.batteries += 1
            print("You put 1 battery in the "+self.color+" flashlight.")
            heldItems.remove("battery")
            self.deadBattery = False
        elif self.batteries > 0:
            print("The "+self.color+" flashlight already has enough batteries.")
        elif not "battery" in heldItems:
            print("You aren't holding a battery")

    #setter that adds 1 bulb if there are bulbs in the room and space in the flashlight
    #returns -1 if successful, to remove 1 bulb from room
    def add_bulb(self,roomBulbs):
        if self.bulb <= 0 and roomBulbs > 0:
            self.bulb = 1
            print("You remove the flashlight bulb.")
            return -1 #-1 bulb in the room
        elif self.batteries < 2 and roomBulbs <= 0:
            print("There are no flashlight bulbs in the room.")
            return 0
        else:
            print("There is already a bulb in the flashlight.")
            return 0

    #setter that turns the flashlight on
    def turn_on(self):
        if not self.isOn:
            if self.batteries == 1 and not self.deadBattery:
                self.isOn = True
                print("You flip the "+self.color+" flashlight's switch to on. The light turns on.")
            else:
                print("You flip the switch to on, but it won't turn on. Maybe the battery is dead.")

    #setter that turns the flashlight off
    def turn_off(self):
        if self.isOn:
            self.isOn = False
            print("You flip the "+self.color+" flashlight switch to off. The light goes out.")
