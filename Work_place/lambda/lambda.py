#!/usr/bin/python

def map_test(li) :
	res = []
	for i in li :
		res.append(i * 3)
	return res

res = map_test([10,20,30,40])
print(res)

#위의 긴 문장을 아래의 한 줄로 줄일수 있다.

#print(map(lambda x : x *3, [10,20,30]))
