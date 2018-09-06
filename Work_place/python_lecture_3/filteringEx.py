#filtering: list comprehension

li = [1,10,23,11,-21,4,-11,-3,5]

#list comprehension

print([n for n in li if n > 0])  ### List comprehension

print([n for n in li if n < 0])   ### 음수만 출력

plus_number = (n for n in li if n>0)

for x in plus_number:
    print(x)



#filter() 이용  : filter() 함수는 iterator를 생성한다

li_1 = ["10","-12","20","-13",'=','*']

def is_int(val):
    try:
        aa = int(val)
        return True
    except ValueError:
        return False

intVal = list(filter(is_int, li_1))
print(intVal)

#필터링은 조건에 만족하는 값만 걸러내기도 하고 새로운 값으로 치환할수도 있다

mylist = [10,20,-1,11,-3,-13]
val_1 = [n if n>0 else 0 for n in mylist]  ### 0 보다 작은 값은 다 0 으로 대체한다.
print(val_1)

#itertools.compress() : 어떤 시퀸스의 필터링 결과를 다른 시킌스에 적용할때 사용한다

local = [
    '서울','경기','인천','대구','광주','부산'
]

cnt = [2,4,10,3,8,12,8]

from itertools import compress

filter_cnt = [i>5 for i in cnt] #boolean(True,False)으로 리턴 된다
print(filter_cnt)

filter_local = list(compress(local,filter_cnt))  ### True 에 해당되는 값만 처리
print(filter_local)