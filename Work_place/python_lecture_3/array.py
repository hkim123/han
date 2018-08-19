'''
#pprint(pretty printer)  :자료구조를 사람이 보기 좋게 출력하는 모듈

data = [(1,{'a':'가','b':'나','c':'다','d':'라'}),
        (2,{'e':'마','f':'바','g':'사','h':'아'})
        ]

#pprint 모둘에 pprint() 함수를 이용하여 자료구조를 츌력하기
print(data)
from pprint import pprint

pprint(data)

#array : 시퀴스 자료구조를 정의하는데, list 와의 차이점은 모든 자료형이 동일하다.
# 표준 module 로는 제공하지 않는다, 동일한 자료형만 사용가능, memoy를 효율적으로 사용가능
'''
import array
str = "abcdefgh"
arr = array.array('u', str)  #array(타입코드,값)
print(arr)  #array 객체를 생성

print (array.typecodes)

arr1 = array.array('i',range(5))
print (arr1)
arr1.extend(range(5))
print(arr1)
print(arr1[3:6])

print(list(enumerate(arr1)))

print(dir(array))