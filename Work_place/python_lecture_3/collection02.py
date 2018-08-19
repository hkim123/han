# Deque : 양방향 큐(데크)는 컨테이너 양쪽(앞뒤)에 아이템을 넣거나 뺄수 있다.
# 큐 : data 가 한쪽으로 들어가고 다른쪽으로 나간다. 먼저 들어간 data 가 먼저 나온다.
# stack : data 입구와 출구가 동일하다. 나중에 들어간 data 가 먼저 나온다, 즉 먼저 들어간 data 를 지우려면, 나중에 들어간 data 부터 빼내야 지울수 있다.

import collections
deq = collections.deque("Hello Python")
print (deq)
print(len(deq))
print(deq[0])
print(deq[-1]) # -1 인경우는 오른쪽을 의미한다.

deq.remove('o')  # o 가 remove 된다
print(deq)

deq.append('k') # 오른쪽으로 data 추가
print(deq)

deq.appendleft('k')  #왼쪽으로 data 추가
print(deq)

deq.extendleft('d') #왼쪽으로 data 추가
print(deq)

deq1 = collections.deque()
deq1.extend('abcdefg')
print(deq1)

deq1.append('x')
print(deq1)

deq1.extendleft('1')
print(deq1)

#item 꺼내기

print('오른쪽에서 부터 꺼내오기')
while True :
    try:
        print (deq.pop(), end= ''), #not sure 왜 comma 가 필요한지, 없어도 돌아감.
    except IndexError:
        break

#그냥 돌리면 아래는 아무것도 안나온다, 왜냐면 위에서 이미 다 빼서 남아 있는 data 가 없음. 아래를 확인하려면, 위를 comment out 해야 됨.
print('왼쪽에서 부터 꺼내오기')
while True :
    try:
        print (deq.popleft(), end= '') #not sure 왜 comma 가 필요한지, 없어도 돌아감.
    except IndexError:
        break
