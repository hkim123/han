#CH14 generator  : /yield

#yield 의 리턴값이 generator object 이다.
#yield는 generator 생성을 하고 generator 는 next() 함수를 가지고 있다.
#이 객체는 다른 작업이 있을때 다른 중요한 작업을 먼저하고 이 객체를 다시 할수 있다.

def generatorEx(n):
    for i in range(n):
        yield i ** 2

print(generatorEx(4))

gen  = generatorEx(4)
print(gen)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


def countdown(n) :
    while n > 0:
        yield n
        n -= 1
    print("end")

cnt = countdown(3)
print(cnt)
print(next(cnt))
print(next(cnt))
print(next(cnt))

for i in generatorEx(5):
    print(i)

