i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    else:
        print(i)

aa = list(range(1, 5))
print(aa)

for j in range(1, 5, 2):
    print(j)

# def show(name, gender ="M", age) :
#     print ("my name is :" name)
#     if gender == "M" :
#         print ("Man")
#     else :
#         print ("Woman")
#     print ("My age is :" age)
#
# show("han","f",23)


print("you've {0} a friend".format("got"))

str = "{2} {0} {1}".format('a',100,200)
print(str)

print("오늘은 우리가 사귄지 {0}일째!!, 요일은 {day}".format(300, day='sunday'))

aa = 'abdcde'
cnt = aa.count('d')
print (cnt)
cnt_1 = len(aa)
print (cnt_1)

kk = [1,2,3,4,5]
kk.append([6,7])
print(kk)
