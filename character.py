from random import *


class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.speech = None

    def isEnemy(self):
        return False

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )
        print("You can TALK to "+self.name)

    # Set what this character will say when talked to
    def set_speech(self, speech):
        self.speech = speech

    # Talk to this character
    def talk(self):
        if self.speech is not None:
            print("[" + self.name + " says]: " + self.speech)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

# Enemy Is A Sub Class of Character
class Enemy(Character):

    # Constructor for enemy
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weaknesses = [] # Array for multiple weaknesses
        self.enemyHealth = randrange(20,40)

    def isEnemy(self):
        return True

    # set_weakness expects to be passed an array
    def set_weaknesses(self, newWeaknesses):
        self.weaknesses = newWeaknesses

    # Returns enemyHealth
    # If weapon matches weakness, then extra damage
    def fight(self, combat_item):
        combat_item = combat_item.lower()
        if combat_item in self.weaknesses:
            attack = randrange(1,7)+randrange(1,7)+randrange(1,7)+5
            print("-=-=-=-=-=- You fend " + self.name + " off with the " + combat_item + ". -=-=-=-=-=-")
            if attack > 12:
                print("-=-=-=-=-=- It's super effective!")
            print("-=-=-=-=-=- A -"+str(attack)+" attack!")
        else:
            attack = randrange(1,7)
            print("********** You use the " + combat_item + " for a -"+str(attack)+" attack! **********")
        self.enemyHealth -= attack
        return self.enemyHealth

    def enemyAttack(self):
        damage = randrange(1,7) + randrange(1,7)
        print("\n!@#$%^&*!@#$%^&* "+self.name+" attacks you! -"+str(damage)+" HP! *&^%$#@!*&^%$#@!\n")
        return damage
