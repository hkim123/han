import decimal
print(decimal.Decimal(2.675))
print(round(2.675,2)) #2.67 로 나타난다, 위의 결과를 보면 알수 있다(2.675 = 2.674999999...)
print(round(2454,-2))
print(round(2454,-3))

s = 'A'
print(ord(s))
k = 'AB'
print(list(bytes(b'AB')))  #display 2 character value
print([ord(c) for c in k]) #display 2 character value

b = '12'
print([ord(c) for c in b])
#d = 12
#print([ord(c) for c in d])

print('0041')
print("\u0041")
print("\u00c0") # differenct character of above. this is not A
print(chr(98))   # print b
print(chr(ord('h')-32)) # print uppercase H
print(chr(ord('a')+3))  # print d

x = 1100
print(id(x))
y = x
print(id(y))
x = 200
print(id(y))
print(y)

print(format(12.34546,".2f"))
print(format(12.34546,".3f"))


x = format(16.4,"10.3f")  #토탈 10
print(x)  #앞에 space 가 있다. 6개의 스페이스가 있다(16.4 = 4자리)
x = format(16.4,"<10.3f")
print(x)

print(format(0.53457,"10.2%"))  # % means 곱하기 100

print(format('abs',">20s"))

