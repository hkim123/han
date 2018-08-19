#namedtuple()

aa = ('홍길동',24,'남')
print(aa)

bb = ('강복녀',21,'여')
print(bb[0])

for n in [aa, bb] :
    print('%s은 %d 세의 %s성 입니다.'%n)  # 만약 aa 나 bb 의 요소가 많아지면 순서대로 찾아서 print 하는게 힘들어 진다. 이때 사용하는게 namedtuple 이다.
                                      # 각각의 요소에다 이름을 할당해서 사용한다, dictionary 와 비슷하다. dictionary 는 memory 효율성이 떨어진다.


#namedtuple example
import collections

Person = collections.namedtuple("person",'name age gender')  #namedtuple 객체
aa = Person(name='강길동',age='25',gender='남')
bb = Person(name='강길동',age='21',gender='여')

for n in [aa,bb] :
    print ('%s은 %s 세의 %s성 입니다.'%n)

# OrderedDict : 자료의 순서를 기억하는 클래스

dic = {}

dic['서울'] = 'LG트윈스'
dic['대구'] = '삼성라이온즈'
dic['광주'] = 'KIA 타이거즈'



for i,j in dic.items():
    print (i,j)

print("---------------")
dic1 = collections.OrderedDict()

dic1['서울'] = 'LG트윈스'
dic1['대구'] = '삼성라이온즈'
dic1['광주'] = 'KIA 타이거즈'

for i,j in dic1.items():
    print(i, j)

print("비교를 이용한 표준사전과 OrderedDic")

#표준 사전을 사용한 경우
dic3 = {}

dic3['서울'] = 'LG트윈스'
dic3['대구'] = '삼성라이온즈'
dic3['광주'] = 'KIA 타이거즈'

dic4 = {}
dic4['서울'] = 'LG트윈스'
dic4['광주'] = 'KIA 타이거즈'
dic4['대구'] = '삼성라이온즈'


print (dic3 == dic4)  # 입력순서는 틀리지만 True 값이 나온다, 표준 사전

dic5 = collections.OrderedDict()

dic5['서울'] = 'LG트윈스'
dic5['대구'] = '삼성라이온즈'
dic5['광주'] = 'KIA 타이거즈'

dic6 = collections.OrderedDict()

dic6['서울'] = 'LG트윈스'
dic6['광주'] = 'KIA 타이거즈'
dic6['대구'] = '삼성라이온즈'


print (dic5 == dic6)  #입력순서가 틀리기 때문에 False 가 나온다,OrderedDict