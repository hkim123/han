# Attribute Critter
# Demonstrates creating and accessing object attributes

class Critter(object):
    """A virtual pet"""
    def __init__(self, name):
        print("A new critter has been born!")
        self.name = name

    def __str__(self):     ####################### This is for print, when main function print this class, it use this __str__ method. without this in below print(crit1) will error
        rep = "Critter object\n"
        rep += "name: " + self.name + "\n"
        return rep  

    def talk(self):
        print("Hi.  I'm", self.name, "\n")

# main
crit1 = Critter("Poochie")
crit1.talk()

crit2 = Critter("Randolph")
crit2.talk()

print("Printing crit1:")
print(crit1)

print("Directly accessing crit1.name:")
print(crit1.name)

input("\n\nPress the enter key to exit.")
