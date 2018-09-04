##dictionary key 값을 여러값에 매핑하기(collections,defaultfict)
d = {}

d.setdefault('sel',[]).append('02')
d.setdefault('sel',[]).append('서울')
print(d)

#위와 똑같은 결과, 초기화가 필요없고, 바로 리스트 값을 추가할수 있다.
from collections import defaultdict

d = defaultdict(list)  ## 리스트로 define 해서 초기화 한다.
d['sel'].append('02')
d['sel'].append('서울')
print(d)

##집합인경우(set)
d= defaultdict(set)
d['inchoen'].add('032')  ##set 은 add 명령문을 사용한다
d['inchoen'].add('인천')
print(d)

#####
color = [('blue',3),('yellow',3),('red',1),('blue',4),('yellow',5)]
d = defaultdict(list)
for key, val in color:
    d[key].append(val)
li = list(d.items())
print(li)

### 위를 defaultdic 을 사용하지 않고 하기
d = {}
for key, val in color:
    d.setdefault(key,[]).append(val)
li = list(d.items())
print(li)

####
str = "hello hi goodmorning"
d = defaultdict(int)
for key in str:   #알파벳 과 스페이스가 몇번 나왔는지를 보여 준다.
    d[key] += 1

li = list(d.items())  
print(li)
