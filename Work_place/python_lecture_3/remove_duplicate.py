## 시퀀스에서 중복 없애기

aa = [8,1,9,3,1,5,6,4,1,5,2]

bb = set(aa)  #set 은 중복값이 없고 순서가 없다, 순서가 유지 되지 않는다
print(bb)

### 순서를 유지하면서 중복을 없애는 방법

def remove_dup(items):
    set_a = set()
    for item in items:
         if item not in set_a:
             yield item
             set_a.add(item)

remove_dup(aa)
print(list(remove_dup(aa)))
