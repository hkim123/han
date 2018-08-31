#str 은 '' 을 제거하고 return 한다
#repr 은 string 을 '' 한번 더 감싸고 return 한다.
#eval 은 '' 을 제거하고 계산을 한다.

simpleString = '1+2'
print(simpleString)
print(str(simpleString))
print(repr(simpleString))
print(eval(str(simpleString)))
print(eval(repr(simpleString)))
print(eval(eval(repr(simpleString))))

