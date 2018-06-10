#!/usr/bin/python
class Human():
    '''people'''


person1 = Human()
person2 = Human()

person1.language = "Korean"
person2.language = "English"

#print (person1.language)
#print (person2.language)

person1.name = "Korean"
person2.name = "American"

def speak(person):
    print ("{} speak {}". format(person.name,person.language))

speak(person1)
speak(person2)