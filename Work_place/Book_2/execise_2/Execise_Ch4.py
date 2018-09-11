#Question2
spam2 = [2,4,6,8,10]
spam2[2] = 'hello'
print(spam2)

#Question3

spam3 = ['A','B','C','D']
print(spam3[int(3)])

bacon = [3.14,'cat',11,'cat',True]
print(bacon.index('cat'))
bacon.append(99)
print(bacon)
bacon.remove('cat')
print(bacon)

a = (42,)
b = (42)
c = ('hi',)
d = ('hi')
print(type(a))   # a는 튜플이다, 왜냐면 42 다음에 ,를 찍어서 이것을 튜플임을 알려준다
print(type(b))   # b 는 int 이다
print(type(c))   # c 는 튜플이다, 왜냐면 hi 다음에 ,를 찍어서 이것을 튜플임을 알려준다
print(type(d))   # d 는 string 이다


