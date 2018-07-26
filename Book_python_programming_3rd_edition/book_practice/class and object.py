
## class means group of similar variable and functions together. Usually start upper case

class Enemy: ### usually start upper case just differenciate between variable and class, below funxtions are belong to
            ### class Enermy
    life = 3  # life is variable

    def attack(self): ## this is function called attack,self means it is inside of class.
        print('ouch!!')
        self.life -=1  ## this is how to access variale inside class. have to use self.

    def super_attack(self):
        print ('WOW this is powerfull attack')
        self.life -= 3

    def checklife(self):
        if self.life <= 0:
            print ('I am dead')

        else:
            print (str(self.life) + " life left")

## object : A way to access stuff inside class. in order to use inside class special way to access, it is called object
## attack() this approach doesn't work. we need special way to access inside class

#attack()   : can't call function inside class like this.

enemy1 = Enemy()
enemy2 = Enemy()  ## enermy2 also called class enermy

enemy1.attack()    ## call attack function inside class
enemy1.attack()   ## only attact enermy1 so it doesn't affect enermy2

enemy1.checklife()  ## call checklife function inside class Enermy
enemy2.checklife()


##### Init function : special object, you don't have to call, when call another function inside class, it automatcally
##### start as well.
class Tuna:

    def __init__(self):  # this is initial function. whenever called function, it will called this init.
        print ('I am a init you can not avoid me')

    def swim(self):
        print ('I can swim now')

flipper = Tuna() ### tuna class assigned to flipper
flipper.swim()   ### called function swim inside class Tuna, evenif only called swim function it will execute __init__ as well.


### this is Init example

class Battle:

    def __init__(self, x):
        self.energy = x

    def attack(self):
        self.energy -= 1

    def get_energy(self):
        print(self.energy)

jason = Battle(5)
Sandy = Battle(18)


jason.attack()
Sandy.attack()

jason.get_energy()
Sandy.get_energy()

