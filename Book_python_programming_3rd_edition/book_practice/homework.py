# this is homework for python project

'''
from 1 to 100 print out every 4 의 배수
'''


# from 1 to 100 divide to 4 if remainder is 0 it print out...
for n in range(1,100):
    if n % 4 == 0:
        print (n)


# start 0 until 100 but steps are 4
for x in range(0, 100, 4):
    print(x)


# Continue mean similar as skip
# 만약 n 이 numberTaken에 있으면 skip 하고 다음 숫자로 감

numbersTaken = [2, 4, 5, 12, 33, 17]

print ("Here are the numbers are still available:")
for n in range (1,20):
    if n in numbersTaken:
        continue
    print(n)