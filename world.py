from room import *
from flashlight import *
from character import *
from container import *

class World():
    # World constructor
    def __init__(self):

        # ********************************* SET UP THE ROOMS *********************************


        # Kitchen
        #
        # Room descriptions should include interactive containers like CABINET, BIN, DESK, SHELF, SHOEBOX that contain/hide other interactive items
        self.kitchen = Room("Kitchen","A dark and dirty room with flies buzzing around. There are dirty beakers, graduated cylinders, and pipettes in the sink. There is a CUPBOARD above the sink and a CABINET under the sink.")

        # The kitchen has a CUPBOARD object that contains/hides 3 interactive items, a sponge, a plate, a can of soup
        # Once this container is open, the interactive items will no longer be hidden in the container
        self.kitchen.cupboard = Container("cupboard above the sink",["sponge","plate","can of bopw soup","green flashlight"])
        # The kitchen has a CABINET object that contains/hides 2 interactive items, a knife and a twinkie
        # Once this container is open, the interactive items will no longer be hidden in the container
        self.kitchen.cabinet = Container("cabinet under the sink",["knife","twinkie"])
        self.greenFlashlight = Flashlight("green",0,False)

        # Create an interactive item that is shown in a room (not hidden in a container) with create_room_item()
        self.kitchen.create_room_item("spoon")
        self.kitchen.create_room_item("rat")


        # Small Office
        #
        self.smalloffice = Room("Small Office","A dark room with a mess of books and papers covering the desk. There is some mail and an ozon.ru PACKAGE. You can READ a book. You can look in the DESK.")
        self.smalloffice.desk = Container("desk",["battery","envelope"])
        self.smalloffice.package = Container("ozon.ru package",["sheet of bubble wrap","porcelain figurine of a bear","red flashlight"])
        self.smalloffice.create_room_item("guinea pig")
        self.redFlashlight = Flashlight("red",0,False)


        # Laboratory
        #
        self.lab = Room("Laboratory","A bright room with sunlight shining through windows secured by prison bars. There is a messy SHELF on the north wall.")
        # The lab has a SHELF object that contains 3 interactive items. Shelf gets a third argument because you'd say ON the shelf, not IN the shelf
        self.lab.shelf = Container("shelf",["brass key","spork","yellow flashlight"],"on")
        self.lab.create_room_item("rat")
        self.yellowFlashlight = Flashlight("yellow",1,True)


        # Supply Closet
        #
        self.supplycloset = Room("Supply Closet","A small dark room with a musty smell. On one side is a filing CABINET and a large plastic BIN. On the other side is a SHELF with supplies and a SHOEBOX.")


        # Create a fake room called locked that represents all permenently locked doors
        #
        self.locked = Room("locked","")

        
        # Connect the rooms. These are one-way connections.
        self.kitchen.link_room(self.locked, "EAST")
        self.kitchen.link_room(self.smalloffice, "SOUTH")
        self.kitchen.link_room(self.locked, "WEST")
        self.supplycloset.link_room(self.smalloffice, "EAST")
        self.smalloffice.link_room(self.kitchen, "NORTH")
        self.smalloffice.link_room(self.lab, "EAST")
        self.smalloffice.link_room(self.locked, "SOUTH")
        self.smalloffice.link_room(self.supplycloset, "WEST")
        self.lab.link_room(self.locked, "SOUTH")
        self.lab.link_room(self.smalloffice, "WEST")
        

        # Set up characters
        dmitry = Enemy("Dmitry", "A smelly zombie")
        dmitry.set_speech("Brrlgrh... rgrhl... brains...")
        dmitry.set_weaknesses(["FORK","SPORK","KNIFE"])
        self.supplycloset.set_character(dmitry)
    
