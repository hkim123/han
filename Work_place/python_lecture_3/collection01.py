import collections
print(collections.Counter(['aa','cc','dd','aa','bb','ee']))   #counter 함수를 이용해서 초기화
print(collections.Counter({"A":3,"B":2,"C":4}))  #자동적으로 많은 것부터 정렬 (C 부터 정렬)
print(collections.Counter(a=2,b=4,c=1))
#[collections]
#Counter : 컨테이너레 동일한 값의 자료가 몇개인지를 파악하는데 사용하는 객체

#추가 하는 방법

container = collections.Counter()
print(container)

container.update("aabcdeffgg")
print(container)

container.update({'c':2,'f':3})  # c를 2개 추가,f를 3개 추가
print(container)

#Counter 접근하기

for n in "abdfeh" :
    print("%s: %d" %(n,container[n]))  #위의 container 에서 a의 갯수, b의 갯수, d의 갯수,f의 갯수,e의 갯수를 가져온다. h 는 없기 땨문에  0 으로 나타난다

ct = collections.Counter("Hello  Jenny")
ct['x'] = 0
print(ct)  #Hello Jenny 의 각 알파벳의 숫자를 나타낸다, x 는 0 으로 나타낸다.
print(list(ct.elements())) # list 로 만들어서 각각의 객체를 하나씩 출력한다.

# most_common(n) mothod를 사용하는 방법, 인자값 n 을 이용하여 상위 n개를 시퀀스로 만든다.test.txt file 을 만든다.
ct2=collections.Counter()
with open('test.txt','rt') as f: #file test.txt file 을 텍스트 읽기모드 로 f 라는 이름으로 연다.
    for li in f:
        ct2.update(li.rstrip().lower())

for item, cnt in ct2.most_common(5): #상위 5개 의 값, test.txt file 에서는 o 가 제일 많다. 만약 5 를 제거하면 전체 요소의 갯수를 보여준다.
    print('%s : %2d' %(item,cnt))

print(ct2.most_common()) # 튜플 형태로 출력, 모든 요소의 갯수 출력

#Counter 객체는 산술/집합 연산이 가능하다.
ct3 = collections.Counter(['a','b','c','b','d','a'])
ct4 = collections.Counter('aeroplane')
print(ct3)
print(ct4)
print(ct3+ct4)
print(ct3-ct4)
print(ct3 & ct4)  #교집합
print("union", ct3 | ct4)  #합집합

#defaultdic() 함수는 컨테이너를 초기화 만들때 default 값을 지정한다

def default_aa():
    return "aa"

dic = collections.defaultdict(default_aa,n1 = "hi")
print(dic)
print(dic['n1'])

print(dic['n2'])  # n2값이 없으면 aa를 출력한다

