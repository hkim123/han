a = ["e101-049-1", "e101-049-2", "e101-049-3", "e101-049-4","e101-050-1","e101-050-2","e101-050-3","e101-050-4"]
'''
i = a.strip('[]')
print(i)

j = i.replace('\'', '')
print(j)

k = j.split(",")
print(k)
'''
print(str(a))
l = eval(str(a))
print(l)