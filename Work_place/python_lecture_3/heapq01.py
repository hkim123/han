'''
힙 정렬 알고리즘

#heap 이란 자식 노드와 부모 노드가 정렬관계를 가지는 트리형태의 자료 구조
이진 힙의 경우 array 나 list 를 사용해서 표현할수 있다(인덱스를 이용해서 표시할수 있다)
이때 수식은 n(인덱스) 을 부모로 하는 자식노드의 위치 수식은 2n+1,2n+2
max-heap : 위의 노드가 high value 를 가지는 구조(부모가 자식보다 크거나 같은 경우)
min-heap : 위의 노드가 less value 를 가지는 구조 (부모가 자식보다 작거나 같다, python 에서 제공) heapq module


'''
import heapq
# 힙생성 : heappush(), heapify()
from showHeap import show_tree
from heapData import data

heap = []
for n in data:
    print("%3d push :" %n)
    heapq.heappush(heap, n)
    show_tree(heap)
