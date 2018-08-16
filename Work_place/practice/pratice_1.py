import random
# def pop_list(data):
#     n = random.randint(0,len(data)-1)
#     return data.pop(n)
# if __name__ == "__main__":
#     data = [1,3,5,6,7]
#     while data:print(pop_list(data))
n = 0
while  n < 6 :
    aa = [8,4,10,4,9]
    bb = aa.pop(random.randint(0,len(aa)-1))
    print(bb)
    print(aa)
    n = n + 1