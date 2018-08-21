import queue

#FIFO 방식
q = queue.Queue()

for i in range(3):
#    print(i)
    q.put(i)

while not q.empty():
    print (q.get(), end = " ")
print()

lq = queue.LifoQueue()

for i in range(5):
    lq.put(i)

while not lq.empty():
    print(lq.get(), end = " ")