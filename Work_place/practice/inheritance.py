# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print ("{} is creating......".format(self.name))
#
#     def speak(self):
#         print("My name is '{}', age is '{}'".format(self.name,self.age))
#
#
# class Student(Person):
#     def __init__(self,name,age,hakbun):
#         Person.__init__(self,name,age)
#         self.hakbun = hakbun
#         print ("{} Student object is creating".format(self.name))
#
#     def speak(self):
#         Person.speak(self)
#         print("My hakbun is {:d}".format(self.hakbun))
#
#
# class Professor(Person):
#     def __init__(self,name,age,pay):
#         Person.__init__(self,name,age)
#         self.pay = pay
#         print("{} Professor object is creating".format(self.name))
#
#     def speak(self):
#         Person.speak(self)
#         print("Professor who has pay {} is creating".format(self.pay))
#
# s = Student("Han",15,86)
# p = Professor("kim",52,10000)
#
# s.speak()
# p.speak()
# # print(s)
# # print(p)
# #
# # member = [s, p]
# # for aa in member:
# #     aa.speak()

lines = 'Very good morning Jacob Abraham.\n How are you doing today!'
for line in lines:
    print (line)
#for line in lines.splitlines():
#    print (line.strip())