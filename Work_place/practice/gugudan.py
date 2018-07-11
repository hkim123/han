#!/usr/local/bin/python3
for i in range(2,10) :
    for j in range(1,9) :
        print("%d * %d = %d" %(i,j,i*j), end=', ')
    print("")




a = [1,2,3,4,5,6,7,8,9]
gugudan = []
for i in a :
    for j in a :
        gugudan.append(i * j)
print (gugudan)


gugudan = [i * j for i in range(2,10)
                 for j in range (1,10)]
print (gugudan)
