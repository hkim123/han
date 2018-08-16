#method 1
def positive(li):
    res = []
    for i in li :
        if i > 0 :
            res.append(i)
    return res

print(positive([1,-12,3,0,-3,-7]))

method#2
def positive(x):
    return x > 0
print(list(filter(positive,[1,-12,3,0,-3,-7])))


method#3
print(list(filter(lambda x : x > 0,[1,-12,3,0,-3,-7])))


# all 3 methods are same.
