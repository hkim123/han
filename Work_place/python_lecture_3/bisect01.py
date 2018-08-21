##bisect module: 정렬된 상태로 (데이타)를 추가 할수 있는 모듈, 데이타가 많은 리스트를 사용할 경우 heap 방식보다 시간과 메모리 낭비를 줄일수 있다.
import bisect
import random

random.seed(1)  #똑같은 난수 발생, 괄호 안에 숫자를 넣지 않으면 다른 난수를 계속 발생 시킨다.

'''
for i in range(5):
    print ('%5.4f' %random.random(),end = " ")
'''

print('New Index List')
print('=== ===== ====')

li = []
for i in range(1,15):
    num = random.randint(1,100)
    pos = bisect.bisect(li, num)  #item 이 추가되었을때 인덱스 값을 반환
    bisect.insort(li, num)   #리스트를 정렬상태로 유지시키는 함수
    print('%3d %3d  ' %(num, pos), li)
#    print (num, end = "  ")