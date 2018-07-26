#### class and instance variable ####

class Girl:
    gender = 'female'  #  this is class variable, it is usually default apply all 

    def __init__(self,name):
        self.name = name   ### new variable name, this is instance variable it should be unique

r = Girl('Rachel')
s = Girl('Stanky')
print (r.gender)   # print out gender
print (s.gender)
print (r.name)    # print out name
print (s.name)
print (r.gender,r.name) # print gender and name as well