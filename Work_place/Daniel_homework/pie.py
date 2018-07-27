#user input 을 받아서 소수점 자리 까지 보여주기 ###
### 위의 것은 반올림 되는것
### 아래 것은 string 으로 바꾸어서 출력

import math
x=math.pi
#
# i = input ("please enter number : ")
# k = (int(i))
#
# print (round(x,k))


#print ("%0.4f" % float(x))  # 소수점 자리 까지 보여주는 fuction


##### change pie to string and then slicing ####
i = input ("please enter number : ")
k = (int(i) + 2)

y = str(x)
print (y[0:k])
print (y)