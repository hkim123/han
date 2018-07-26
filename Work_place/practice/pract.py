# aa = 0
# # while 1 :
# #     aa += 1
# #     print ('aa is %d' %aa)
# #     if aa == 10 :
# #         print('aa is done')
# #         break

# class FourCal:
#     def __init__(self,first,second):
#         self.first = first
#         self.second = second
#
#     def sum(self):
#         result = self.first + self.second
#         return result
# a = FourCal(4,2)
# #a.setdata(4,2)
# print (a.sum())


# class Person :
#     def __init__(self):
#         self.info = ""
#
#     def showInfo(self,name,age):
#         self.info = "name: " + name + ",  age :" + age
#         print (self.info)
#
# man = Person()
# woman = Person()
#
# man.showInfo("han","52")
# woman.showInfo("grace","48")


class Person :
    def __init__(self):
        self.name = ""
    def say(self,name):
        self.name = ("my name is : " + name)
        print(self.name)

p2 = Person()
p2.say("han kim")