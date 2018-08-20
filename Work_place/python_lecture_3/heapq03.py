#heap data 접근하기 , heappop() 을 이용하여 가장 작은 값을 하나씩 끄집어 낸다.

import heapq
from heapData import data
from showHeap import show_tree

"""
heapq.heapify(data)
show_tree(data)

for n in range(5):
    min_val = heapq.heappop(data)
    show_tree(data)
    print(min_val)

heap data 수정  heapreplace


heapq.heapify(data)
show_tree(data)

for n in [3,15] :
    min_val = heapq.heapreplace(data,n)
    print(min_val)
    show_tree(data)
heap 의 최대,최소 값 구하기 : nlargest(), nsmallest()
"""

print(heapq.nlargest(2,data))
print(heapq.nsmallest(2,data))