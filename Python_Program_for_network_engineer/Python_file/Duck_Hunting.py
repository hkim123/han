class Duck_Hunting:
    ducks = 3
    def hunting(self):
        print ("Catch !!")
        self.ducks -= 1

    def check_ducks(self):
        if self.ducks <= 0 :
            print ("Good Dog !!!!")
        else :
            print (str(self.ducks) + " duscks left")

dog1 = Duck_Hunting()
dog1.hunting()
dog1.check_ducks()

#dog2 = Duck_Hunting()
#dog2.check_ducks()