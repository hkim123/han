#example #1
# result = 0
#
# def adder(num):
#     global result
#     result += num
#     return result
#
# print(adder(3))
# print(adder(4))
# print (adder(3))
#

#Example #2
# result1 = 0
# result2 = 0
#
# def adder1(num):
#     global result1
#     result1 += num
#     return result1
#
# def adder2(num):
#     global result2
#     result2 += num
#     return result2
#
# print(adder1(3))
# print(adder1(4))
# print(adder2(3))
# print(adder2(7))


#Example #3

# class Calculator:
#     def __init__(self):
#         self.result = 0
#
#     def adder(self, num):
#         self.result += num
#         return self.result
#
# cal1 = Calculator()
# cal2 = Calculator()
#
# print(cal1.adder(3))
# print(cal1.adder(4))
# print(cal2.adder(3))
# print(cal2.adder(7))


#Example #4
# class Calculator:
#     def __init__(self):
#         self.result = 0
#
#     def adder(self, num):
#         self.result += num
#         return self.result
#
#     def sub(self, num):
#         self.result -= num
#         return self.result
#
# cal1 = Calculator()
# cal2 = Calculator()
#
# print(cal1.adder(3))
# print(cal1.adder(4))
# print(cal2.adder(3))
# print(cal2.adder(7))
#
# print (cal1.sub(5))  # Cal1's adder result is 7 so 7 - 5 = 2
# print (cal2.sub(4))  # Cal1's adder result is 10 so 10 - 4 = 6


#Example #5
class FourCal:
    pass

a = FourCal()
print (type (a))

#example #6
class Cookie:
    pass

a= Cookie()
b= Cookie()

print (a)
print (b)