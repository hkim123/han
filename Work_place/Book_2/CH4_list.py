'''
catNames = []
while True:
    print('Enter the name of cat' + str(len(catNames) +1 ) + '(or Enter nothing to Stop):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # 반드시 name 에 대 괄호 필요

print('The cat names are :')
for name in catNames:
    print ('  ' + name)
'''




'''
supplies = ['pens', 'staplers', 'flame-throwers', 'blinders']

for i in range(len(supplies)):
    print ('Index  ' + str(i) + '  in supplies : ' + supplies[i])



myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name : ')
name = input()
if name not in myPets:
    print('I do not have a pet name ' + name)
else:
    print(name + ' is my pet list')


###### Remove item ######

myPets = ['Zophie', 'Pooka', 'Fat-tail']
del myPets[1]
print(myPets)
myPets.remove('Zophie')
print(myPets)
'''
########## list 와 tuple 함수로 유형 변경하기 #####
tuple = tuple(['cat','dog',5])
print(tuple)

list = list(('cat','dog',5))
print(list)

#list_1=list('hello')   ## 위의 list 를 comment out 해야 됨
#print(list_1)

