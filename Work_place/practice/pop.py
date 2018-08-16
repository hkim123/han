import random
# def pop_list(data):
#     n = random.randint(0,len(data)-1)
#     return data.pop(n)
# if __name__ == "__main__":
#     data = [1,3,5,6,7]
#     while data:print(pop_list(data))
aa = [1,3,5,6,7]
while  aa :
    bb = aa.pop(random.randint(0,len(aa)-1))
    print(bb)
#    print(aa)
