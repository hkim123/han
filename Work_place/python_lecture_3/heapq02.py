import heapq
# 힙생성 : heappush(), heapify()
from showHeap import show_tree
from heapData import data

heapq.heapify(data)
show_tree(data)