### Inheritance : getting something from someone. in real life example ; I am inherited my dad's eye or
                ### I am inherited my mom's nose, 유산도 one of inheritant

class Parent():

    def print_last_name(self):
        print ('Kim')

class Child(Parent):  ### This class include Parent class as well.

    def print_first_name(self):
        print ('Han')

##    def print_last_name(self):  ### we can overwite as well. even if this function comes from Parent class we can overwrite.
##        print ('Test')


Han = Child()   ### called only Child class
Han.print_last_name()  ### but you can use Parent class as well.
Han.print_first_name()


#### Multiple inheritance

class Mario():

    def move(self):
        print ('I am moving')

class Shroom():

    def eat_shroom(self):
        print ("Now i am big !!")

class BigMario(Mario, Shroom):  ## add 2 class Mario and Shroom,BigMrio has 2 function from Mario and Shroom
    pass      ### Do nothing


bm = BigMario()
bm.move()
bm.eat_shroom()