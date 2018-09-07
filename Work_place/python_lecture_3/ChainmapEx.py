#Chainmap class :여러개의 dictionary (매핑데이타)가 있을때 하나의 딕셔너리로 합쳐서 검색을 할때 사용한다
#               첫번째 매핑데이타에서 검색 한 후에 그다음 매핑데이타에서 검색을 한다

aa = {'name':'홍길동','id':'test','email':'abab@naver.com'}
bb = {'order':'김말동','tel':'010-1234-1234','email':'abab@naver.com'}

from collections import ChainMap
chain = ChainMap(aa,bb)

print(chain['order'])
print(chain['name'])
print(chain['email']) #같은 key 가 있으면 첫번째 것만 가지고 온다.


print(len(chain))  #같은 key 가 있으면 한번만 카운트 한다
print(list(chain.keys()))
print(list(chain.values()))

chain['email'] = 'test123@naver.com'
chain['order'] = '강길동'   #### aa에 추가된다
print(list(chain.values()))

#data delete(dictionary 는 data를 수정할수 있다)
del chain['name']
print(list(chain.values()))

print(aa)
print(bb)
chain['pw'] = 1234  ## aa에 추가
print(aa)

#del chain['tel']  매핑값을 추가하거나 삭제하는 경우 항상 첫번째 매핑데이타에만 영항을 준다.

#chainMap 과 비슷한기능을 하는 update() 함수가 있다.

aa = {'name':'홍길동','id':'test','email':'abab@naver.com'}
bb = {'order':'김말동','tel':'010-1234-1234','email':'abab@naver.com'}
merge = dict(bb)
merge.update(aa)
print(merge['name'])
print(merge['order'])