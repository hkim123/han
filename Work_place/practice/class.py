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