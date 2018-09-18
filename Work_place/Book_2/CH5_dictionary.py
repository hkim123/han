'''
birthdays = {'Alice':'Apr 1','Bob':'Dec 2','Carol':'Mar 4'}
while True:
    print('Enter your name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is a birthday of ' + name)
    else :
        print('I do not have birthday information for ' + name )
        print('what is your birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated')
        print (birthdays)
'''
#keys(),values(),items()

spam = {'color':'red','age':'42'}
print (spam.keys())   # 이것은 tuple 이다.
print(list(spam.keys()))  #list 로 바꿔 줘야 된다

for k in spam.keys():
    print(k)
for v in spam.values():
    print(v)
for i in spam.items():
    print(i)

for k,v in spam.keys(),spam.values():
    print(k,v)

#아래와 같이 3개로 하면 error , don't know why ???

#for i,v,k in spam.items(),spam.values(),spam.keys():
#    print(i,v,k)


# get() method

picnicItems = {'apples':5,'cups':2}
print ('I am brining ' + str(picnicItems.get('cups',0)) + ' cups')
print ('I am brining ' + str(picnicItems.get('eggs',0)) + ' eggs')  #egg 는 없으므로 0 을 리턴한다.