class Human():

    def create(self, name, weight):
#        person = Human()
        person.name = name
        person.weight = weight
        return person

    def eat(self):
        self.weight += 0.1
        print ("{} eat so much so becomes {}kg now".format(self.name, self.weight))

    def walk(self):
        self.weight -= 0.1
        print ("{} walk a lot so becomes {}kg now".format(self.name, self.weight))

    def speak(self, message):
        print(message)


person = Human()
person.create("han", 60.5)
#person = Human.create("han", 60.5)

person.eat()

person.walk()

person.speak("hi how are you")

###########################################################
# class Person :
#     def __init__(self,name):
#         self.name = name
#     def say(self):
#         print ("my name is", self.name)
#
# p1 = Person('han kim')
# p1.say()

###########################################################
# class Person :
#     def __init__(self):
#         self.name = ""
#     def say(self,name):
#         self.name = "my name is + self.name"
#         print (self.name)
#
# p2 = Person()
# p2.say('han kim')
##############################################################

class Man :
    cnt = 0
    def __init__(self,name):
        self.name = name
        print ("{} is  creating......".format(self.name))
        Man.cnt += 1

    def die(self) :
       # "when man object die "
        print("{} is die !!!".format(self.name))
        Man.cnt -= 1

        if Man.cnt == 0 :
            print ("{} is last man".format(self.name))
        else :
            print ("Still {:d} man alive".format(Man.cnt))

    def say(self):
        print("Created!!!,  Hi My name is {}".format(self.name))

    @classmethod
    def how_many(cls):
        #check of how many object left
        print("Currently {} alive".format(Man.cnt))

gameActor1 = Man("Han")
gameActor1.say()
gameActor2 = Man("Kim")
gameActor2.say()

print ("-------------------------------------")
gameActor2.die()
gameActor1.die()
########################################################################