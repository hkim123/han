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


# class Person1 :
#     def __init__(self):
#         self.info = ""   #변수를 만들어 준다.
#
#     def showInfo(self,name,age):
#         self.info = "name: " + name + ",  age :" + age
#         print (self.info)
#
# man = Person1()
# woman = Person1()
#
# man.showInfo("han","52")
# woman.showInfo("grace","48")


class Person :
    def __init__(self):
        self.name = ""   #변수를 만들어 준다.
        self.age = ""
    def say(self,name,age):
        self.name = ("my name is : " + name)
        self.age = ("my age is :" + age)
        print(self.name)
        print(self.age)

p2 = Person()
p2.say("han kim","52")

##### 위의 방법을 아래와 같이 할수 있다 ##########

class Person2:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def say(self):
        print("my name is :" + self.name)
        print("my age is :" + self.age)

p3 = Person2("han kim","52")
p3.say()
