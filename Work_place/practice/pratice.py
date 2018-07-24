# '''
# i = 0
# while i < 10:
#     i += 1
#     if i % 2 == 0:
#         continue
#     else:
#         print(i)
#
# aa = list(range(1, 5))
# print(aa)
#
# for j in range(1, 5, 2):
#     print(j)
#
# # def show(name, gender ="M", age) :
# #     print ("my name is :" name)
# #     if gender == "M" :
# #         print ("Man")
# #     else :
# #         print ("Woman")
# #     print ("My age is :" age)
# #
# # show("han","f",23)
#
#
# print("you've {0} a friend".format("got"))
#
# str = "{2} {0} {1}".format('a',100,200)
# print(str)
#
# print("오늘은 우리가 사귄지 {0}일째!!, 요일은 {day}".format(300, day='sunday'))
#
# aa = 'abdcde'
# cnt = aa.count('d')
# print (cnt)
# cnt_1 = len(aa)
# print (cnt_1)
#
# kk = [1,2,3,4,5]
# kk.append([6,7])
# print(kk)
# '''
#
#
#
# import re
# p = re.compile('[a-z]+')
# m = p.match("python")
# if m :
#     print ("match found: ", m.group())
# else:
#     print('no match')

#
# class Person :
#     def __init__(self,name):
#         self.name = name
#     def say(self):
#         print ("my name is", self.name)
#
# p1 = Person('han kim')
# p1.say()


# class Person :
#     def __init__(self):
#         self.name = ""
#     def say(self,name):
#         self.name = "my name is + self.name"
#         print (self.name)
#
# p2 = Person()
# p2.say('han kim')

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
Man.how_many()